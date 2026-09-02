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
        self._next_id = 5

    def find_all(self) -> List[Message]:
        #print(f"Service ID: {id(self)}")
        return self._messages

    def find_by_id(self, message_id: int)-> Optional[Message]:
        return next((msg for msg in self._messages if msg.id==message_id), None)

    def create(self, new_message: Message) -> Message:
        new_message.id = self._next_id
        self._messages.append(new_message)
        self._next_id += 1
        return new_message

    def update(self, message_id:int, message:Message)-> Optional[Message]:
        for index, msg in enumerate(self._messages):
            if msg.id==message_id:
                updated=Message(id=message_id, text=message.text)
                self._messages[index]=updated
                return updated
        return None

    def delete(self, message_id:int)-> bool:
        for index, msg in enumerate(self._messages):
            if msg.id==message_id:
                del self._messages[index]
                return True
            return False