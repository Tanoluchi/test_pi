import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLITE_FILE_NAME = "../db.sqlite"
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, SQLITE_FILE_NAME)}"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind = engine)
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()