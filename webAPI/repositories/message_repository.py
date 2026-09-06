from abc import ABC, abstractmethod
from typing import List
from repositories.sql_alchemy_message_repo import SqlAlchemyMessageRepository
from entities.message import Message

class MessageRepository(ABC): 
    @abstractmethod
    def find_all(self)-> List[Message]:
        ...

    @abstractmethod
    def find_by_id(self, message_id:int)-> Message | None:
        ...

    @abstractmethod
    def save(self, message:Message)-> Message:
        ...

    @abstractmethod
    def delete(sef, message_id:int)-> None:
        ...

    