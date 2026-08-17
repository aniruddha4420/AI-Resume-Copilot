from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


database_url = "mysql+pymysql://HeBUiXvRyM8TAmx.root:9FUJ96RoV7lAuYuZ@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/test?&ssl_ca=/etc/ssl/cert.pem"

engine = create_engine(
    database_url,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ca": "/etc/ssl/cert.pem"
        }
    }
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()