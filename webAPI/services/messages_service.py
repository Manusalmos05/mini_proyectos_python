from typing import List
from models.message import Message
class MessageService:

    def __init__(self):
        self._messages: List[Message]=[
            Message(id=1, text="Aprendiendo..."),
            Message(id=2, text="..fastApi..."),
            Message(id=3, text="... con Python"),
            Message(id=4, text="prueba con Depends")
        ]
    def find_all(self) -> List[Message]:
        return self._messages
