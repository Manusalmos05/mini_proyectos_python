from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from fastapi import Depends



DATABASE_URL="postgresql://postgres:Manuela0512*@localhost:5432/ecommerce_db"


engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()



def get_db():
    db= SessionLocal()
    try:
        yield db 
    finally:
        db.close()