from typing import List, Optional
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
        return self._messages

    def find_by_id(self, message_id: int)-> Optional[Message]:
        message_found= next((msg for msg in self._messages if msg.id==message_id), None)
        if message_found is None:
            raise ValueError(f"El mensage con ID {message_id} no existe")
        return message_found