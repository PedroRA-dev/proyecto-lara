from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.getenv("DATABASE_URL"), echo=bool(os.getenv("ENVIRONMENT")))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()