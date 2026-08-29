from models. message import Message
from typing import List
from fastapi import APIRouter
from services.messages_service import MessageService
from fastapi import Depends
from depends.message_depends import get_messages_service


router=APIRouter()



@router.get("/", response_model=List[Message])
async def list_messages(service: MessageService= Depends(get_messages_service)):
    return service.find_all()