from typing import List, Optional
from models.message import Message
from services.messages_service import MessageService


class MessageServiceImpl(MessageService):
    def __init__(self):
        self._messages: List[Message]=[
            Message(id=1, text="hacer la compra", author_email="user1@example.com", priority=3),
            Message(id=2, text="limpiar la casa", author_email="user2@example.com", priority=2),
            Message(id=3, text="estudiar Python", author_email="user3@example.com", priority=4),
            Message(id=4, text="sacar la basura", author_email="user4@example.com", priority=1)
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
                updated=Message(id=message_id, 
                                text=message.text, 
                                author_email=message.author_email, 
                                priority=message.priority)
                self._messages[index]=updated
                return updated
        return None

    def delete(self, message_id:int)-> bool:
        for index, msg in enumerate(self._messages):
            if msg.id==message_id:
                del self._messages[index]
                return True
            return False