from abc import ABC, abstractmethod
from entities.user import User
from typing import List, Optional


class UserRepository(ABC):
    @abstractmethod
    def find_by_email(self, email: str)->Optional[User]:
        pass

    @abstractmethod
    def find_by_id(self, user_id:int)->Optional[User]:
        pass

    @abstractmethod
    def find_all(self)->List[User]:
        pass

    @abstractmethod
    def crete_user(self, user:User)->User:
        pass