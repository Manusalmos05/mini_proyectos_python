from abc import ABC, abstractmethod
from typing import List
from schemas.user_request import UserRequest
from schemas.user_dto import UserDto

class UserService(ABC):


    @abstractmethod
    def find_all(self)->List[UserDto]:
        pass

    @abstractmethod
    def find_by_id(self, user_id:int)->UserDto |None:
        pass

    @abstractmethod
    def find_by_email(self, email: str)->UserDto |None:
        pass

    @abstractmethod
    def create_user(self, user:UserRequest)->UserDto:
        pass