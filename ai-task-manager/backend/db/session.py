from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging
#import os
#from dotenv import load_dotenv

#load_dotenv()

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

"""
DB_USERNAME = os.getenv("TEST_DB_USERNAME")
DB_PASSWORD = os.getenv("TEST_DB_PASSWORD")
DB_HOST = os.getenv("TEST_DB_HOST")
DB_PORT = os.getenv("TEST_DB_PORT")
DB_NAME = os.getenv("TEST_DB_NAME") """

DATABASE_URL = "sqlite:///./study_planner.db"
print(f"Using database at: {DATABASE_URL}")

#engine = create_engine(DATABASE_URL)
"""
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()  # ✅ Ensure this line exists
"""
# Create engine and session
#engine = create_engine(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
