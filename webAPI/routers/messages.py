from models. message import Message
from typing import List, Optional
from fastapi import APIRouter
from services.messages_service import MessageService
from fastapi import Depends
from depends.message_depends import get_messages_service


router=APIRouter()



@router.get("/", response_model=List[Message])
async def list_messages(service: MessageService= Depends(get_messages_service)):
    return service.find_all()



@router.get("/view/{message_id}", response_model=Optional[Message])
async def get_message(message_id:int, service: MessageService=Depends(get_messages_service)):
    return service.find_by_id(message_id)