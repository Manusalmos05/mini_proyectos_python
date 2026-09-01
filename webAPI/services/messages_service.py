from typing import List, Optional
from models.message import Message
from abc import ABC, abstractmethod





#clase generica
class MessageService(ABC):
    @abstractmethod
    def find_all(self) -> List[Message]:
            ...

    @abstractmethod
    def find_by_id(self,message_id:int)-> Optional[Message]:
           ...








    
