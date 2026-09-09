from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.settings import settings



engine=create_engine(settings.DATABASE_URL, echo=True, pool_size=10)
SessionLocal=sessionmaker(autocommit=True, autoflush=False, bind=engine)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()