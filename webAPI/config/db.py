from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "mysql+mysqlconnector://root:Manuela0512*@localhost:3306/db_crud_fastapi"
engine= create_engine(DATABASE_URL, echo=True, pool_size=20)
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)



Base= declarative_base()
