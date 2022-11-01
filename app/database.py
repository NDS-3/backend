from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_ENGINE="mysql+pymysql"
DB_USERNAME=os.environ.get('DB_USERNAME')
DB_PASSWORD=os.environ.get('DB_PASSWORD')
DB_HOST=os.environ.get('DB_HOST')
DB_PORT=os.environ.get('DB_PORT')
DB_DATABASE_NAME=os.environ.get('DB_DATABASE_NAME')
DB_URL = f'{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE_NAME}'

engine = create_engine(DB_URL, encoding='utf-8')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()