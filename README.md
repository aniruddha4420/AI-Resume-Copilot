# AI-Resume-Copilot
# 🤖 AI Resume Copilot

**AI Resume Copilot** is an AI-powered career assistant that helps users improve their resumes based on their target job role.

Users can **upload their resume and specify the role they are interested in**. The application analyzes the resume and provides personalized career guidance, including relevant skills, missing skills, a learning roadmap, and potential interview questions.

---

## 🚀 Features

### 📄 Resume Analysis

Upload your resume and let AI analyze your existing skills, experience, and qualifications.

### 🎯 Job Role-Based Feedback

Enter the job role you are targeting and receive feedback tailored specifically to that career path.

### 🧠 AI-Powered Recommendations

The application provides:

* ✅ **Skills Identified** — Skills already present in your resume
* ❌ **Missing Skills** — Skills you may need for your target role
* 🗺️ **Learning Roadmap** — A suggested path to develop the missing skills
* 💬 **Interview Questions** — Potential interview questions relevant to the target role

### 👤 User Authentication

Users can create accounts and securely log in to access their personalized career information.

### 📊 Dashboard

A dedicated dashboard allows users to access their resume analysis and career recommendations.

### 📚 Analysis History

Users can view their previous resume analyses and track their career preparation over time.

### ☁️ Cloud Database

User login information, resume-related data, and analysis results are stored in **TiDB Cloud**.

---

## 🛠️ Technologies Used

| Technology             | Purpose                                |
| ---------------------- | -------------------------------------- |
| 🐍 Python              | Backend development                    |
| 🌐 Flask               | Web application framework              |
| 🎨 HTML                | Frontend structure                     |
| 🎨 CSS                 | Frontend styling                       |
| 🤖 OpenAI GPT-4.1-mini | Resume analysis and AI recommendations |
| 🗄️ TiDB Cloud         | Database                               |
| 🔐 Authentication      | Login & Sign Up                        |

---

## 🔄 How It Works

```text
        👤 User
          │
          ▼
   Create Account / Login
          │
          ▼
    Upload Resume
          │
          ▼
   Enter Target Job Role
          │
          ▼
    🤖 AI Resume Analysis
          │
          ├── Skills
          │
          ├── Missing Skills
          │
          ├── Learning Roadmap
          │
          └── Interview Questions
          │
          ▼
       Dashboard
          │
          ▼
      Analysis History
```

---

## 💡 Example Use Case

Suppose a user wants to become a **Data Scientist**.

The user uploads their current resume and selects:

> **Target Role: Data Scientist**

AI Resume Copilot analyzes the resume and provides:

**Skills**

* Python
* SQL
* Pandas
* Machine Learning

**Missing Skills**

* Deep Learning
* TensorFlow/PyTorch
* Statistics
* Model Deployment

**Learning Roadmap**

1. Strengthen Statistics fundamentals
2. Learn Deep Learning
3. Practice TensorFlow/PyTorch
4. Build Machine Learning projects
5. Learn model deployment

**Interview Questions**

* Explain the difference between supervised and unsupervised learning.
* How do you handle missing data?
* What is overfitting and how can you prevent it?
* Explain precision, recall, and F1-score.

---

## 📂 Project Structure

```text
AI-Resume-Copilot/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   └── history.html
│
├── static/
│   └── css/
│       └── style.css
│
└── ...
```

> The project structure may vary depending on your current implementation.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/aniruddha4420/AI-Resume-Copilot.git
```

```bash
cd AI-Resume-Copilot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project directory and add your required credentials:

```env
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=your_tidb_database_url
```

**Never commit your `.env` file or API keys to GitHub.**

Your `.gitignore` should contain:

```gitignore
.env
.env.*
learn.txt
test_connection.py
```

---

## ▶️ Running the Application

After configuring your environment variables, start the Flask application:

```bash
python app.py
```

Then open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🎯 Project Goal

The goal of **AI Resume Copilot** is to help job seekers understand:

> **"Where am I now, what skills am I missing, and what should I learn to reach my target role?"**

Instead of simply analyzing a resume, the application provides a **personalized career pathway** based on the user's current skills and desired job role.

---

## 🔮 Future Improvements

Potential improvements include:

* 📊 Resume score and visual analytics
* 🎯 Job description matching
* 🔍 Job recommendation system
* 📄 AI-powered resume rewriting
* 💼 LinkedIn profile analysis
* 📈 Career progress tracking
* 🎤 AI mock interview
* 📑 Resume PDF export
* 🌎 Support for multiple languages

---

## 👨‍💻 Author

**Aniruddha**

Built with Python, Flask, OpenAI, and TiDB Cloud.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**GitHub:**
https://github.com/aniruddha4420/AI-Resume-Copilot

