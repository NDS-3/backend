from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_ENGINE="mysql+pymysql"
DB_USERNAME="admin"
DB_PASSWORD="12341234"
DB_HOST="testdb.c5s2vrj6myrp.ap-northeast-2.rds.amazonaws.com"
DB_PORT="3306"
DB_DATABASE_NAME="test"
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