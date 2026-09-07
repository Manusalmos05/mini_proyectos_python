from entities.message import Message
from typing import List
from repositories.message_repository import MessageRepository
from sqlalchemy.orm import Session
from sqlalchemy import select



class SqlAlchemyMessageRepository(MessageRepository):

    def __init__(self, db: Session):
        self._db = db

    def find_all(self)-> List[Message]:
        selected =select(Message).order_by(Message.id.asc())
        return list(self._db.scalar(selected).all())

    def find_by_id(self, message_id:int)-> Message |None:
        return self._db.get(Message, message_id)

    def save(self, message:Message)-> Message:
        self._db.add(message)
        return message

    def delete(self, message:Message):
        self._db.delete(message)