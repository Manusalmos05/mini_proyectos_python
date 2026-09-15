from sqlalchemy.orm import Session
from fastapi.params import Depends
from config.db import SessionLocal
from repositories.user_repositorio import UserRepository
from repositories.sqlAlchemy_userRepository import SqlAlchemyUserRepository
from services.userServicesImple import UserServiceImpl
from services.user_services import UserService

def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()

def get_repository(db:Session=Depends(get_db))->UserRepository:
    return SqlAlchemyUserRepository(db)

def get_service(db: Session=Depends(get_db),
                repo:UserRepository=Depends(get_repository))->UserService:
    return UserServiceImpl(repo, db)