from repositories.user_repositorio import UserRepository
from sqlalchemy.orm import Session
from entities.user import User
from typing import List, Optional
from sqlalchemy import select

class SqlAlchemyUserRepository(UserRepository):

    def __init__(self, db:Session):
        self._db=db


    def find_all(self)->List[User]:
        stmt=select(User).order_by(User.id.asc())
        return list(self._db.scalars(stmt).all())

    def find_by_id(self, user_id:int)->Optional[User]:
        return self._db.get(User, user_id)
    
    def find_by_email(self, email: str)->Optional[User]:
        stmt=select(User).where(User.email==email)
        return self._db.scalar(stmt)
    
    def crete_user(self, user:User)->User:
        self._db.add(user)
        return user