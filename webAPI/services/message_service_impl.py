from typing import List, Optional
from fastapi import HTTPException
from models.message import Message
from services.messages_service import MessageService


class MessageServiceImpl(MessageService):
    def __init__(self):
        self._messages: List[Message]=[
            Message(id=1, text="Aprendiendo..."),
            Message(id=2, text="..fastApi..."),
            Message(id=3, text="... con Python"),
            Message(id=4, text="prueba con Depends")
        ]

    def find_all(self) -> List[Message]:
        #print(f"Service ID: {id(self)}")
        return self._messages

    def find_by_id(self, message_id: int)-> Optional[Message]:
        return next((msg for msg in self._messages if msg.id==message_id), None)
        