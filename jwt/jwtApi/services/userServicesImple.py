import email

from repositories.user_repositorio import UserRepository
from schemas.user_dto import UserDto
from schemas.user_request import UserRequest
from services.user_services import UserService
from typing import List
from sqlalchemy.orm import Session
from entities.user import User as UserEntity


class UserServiceImpl(UserService):
    def __init__(self, repo: UserRepository, db: Session):
        self._db=db
        self._repo=repo

    def find_all(self)->List[UserDto]:
        return [UserDto.model_validate(user) for user in self._repo.find_all()] #va a tomar el entity y convertirlo en una instancia Dto

    def find_by_id(self, user_id:int)->UserDto |None:
        user=self._repo.find_by_id(user_id)
        if not user:
            return None
        return UserDto.model_validate(user)


    def find_by_email(self, email:str)-> UserDto | None:
        user= self._repo.find_by_email(email)
        if not user:
            return None
        return UserDto.model_validate(user)

    

    def create_user(self, user:UserRequest)->UserDto:
        if self._repo.find_by_email(user.email):
            raise ValueError('El email ya está asociado a una cuenta')

        user_entity=UserEntity(email=user.email,password=user.password)

        try:
            self._repo.crete_user(user_entity)
            self._db.add(user_entity)
            self._db.commit()
            self._db.refresh(user_entity)
            return UserDto.model_validate(user_entity)
        except Exception:
            self._db.rollback()
            raise
   