from sqlalchemy.orm import Session
from fastapi.params import Depends
from config.db import SessionLocal
from jwtApi.repositories import sqlAlchemy_userRepository
from jwtApi.services.userServicesImple import UserServiceImpl
from jwtApi.services.user_services import UserService



def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()



def get_service(db: Session=Depends(get_db))->UserService:
    return UserServiceImpl(sqlAlchemy_userRepository(db), db)