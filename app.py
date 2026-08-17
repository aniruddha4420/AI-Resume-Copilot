
from flask import Flask, request, render_template, redirect, session
from db import Base, engine, SessionLocal
import models
import PyPDF2
import docx
import json

from ai import analyse_resume

app = Flask(__name__)
app.secret_key = 'secret123'

Base.metadata.create_all(bind=engine)

#HOME

@app.route("/")
def home():
    return redirect("/dashboard")
    return redirect("/login")


#------SIGNUP
@app.route("/signup", methods=["GET","POST"])
def signup():
    db = SessionLocal()

    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        existing_user = db.query(models.User).filter_by(email=email).first()
        if existing_user:
            return "User already exists"

        user = models.User(email=email, password=password)
        db.add(user)
        db.commit()

        return redirect("/login")
    return render_template("/signup.html")

#LOGIN
@app.route("/login", methods=["GET","POST"])
def login():
    db = SessionLocal()

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = db.query(models.User).filter_by(email=email, password=password).first()

        if user:
            session["user"] = user.email
            return redirect("/dashboard")
        else:
            return "Invalid Credentials"

    return render_template("login.html")

#DASHBOARD
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":
        user_goal = request.form.get("role")
        resume_text = request.form.get("resume")

        file = request.files.get("file")




        #File handling
        if file and file.name != "":
            if file.filename.endswith(".pdf"):
                try:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text() or ""
                    resume_text = text
                except Exception as e:
                    result = {"error": f"PDF error: {str(e)}"}

            elif file.filename.endswith(".docx"):
                try:
                    doc = docx.Document(file)
                    text = ""
                    for para in doc.paragraphs:
                        text += para.text +"\n"
                    resume_text = text
                except Exception as e:
                    result = {"error": f"Docx error: {str(e)}"}
        #Analyse Resume
        if resume_text and user_goal:
            try:
                result = analyse_resume(resume_text, user_goal)

                #Save to database
                db = SessionLocal()
                user = db.query(models.User).filter_by(email=session["user"]).first()

                report = models.Report(
                    user_id = user.id,
                    resume_text = resume_text,
                    result = json.dumps(result)
                )

                db.add(report)
                db.commit()

            except Exception as e:
                result = {"error": f"AI error: {str(e)}"}
    return render_template(
        "dashboard.html",
            user=session["user"],
            result = result
        )

#History
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/login")

    db = SessionLocal()
    user = db.query(models.User).filter_by(email=session["user"]).first()

    report = db.query(models.Reports).filter_by(user_id = user.id).all()

    #Convert JSON string > dict
    pasred_report = []
    for r in report:
        try:
            pasred_report = json.loads(r.result)

        except:
            pasred_result = []

        pasred_report.append({
            "resume":r.resume_text,
            "result":pasred_result
        })

    return render_template("history.html",report=pasred_report)


#Logout route
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect("/login")




if __name__ == "__main__":
    app.run(debug=True)