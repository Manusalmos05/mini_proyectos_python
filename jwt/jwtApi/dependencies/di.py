from sqlalchemy.orm import Session
from fastapi.params import Depends
from config.db import SessionLocal
from repositories.sqlAlchemy_userRepository import SqlAlchemyUserRepository
from services.userServicesImple import UserServiceImpl
from services.user_services import UserService

def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()



def get_service(db: Session=Depends(get_db))->UserService:
    return UserServiceImpl(SqlAlchemyUserRepository(db), db)