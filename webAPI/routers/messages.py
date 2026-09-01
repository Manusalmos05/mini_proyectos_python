
from models. message import Message
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from services.messages_service import MessageService
from fastapi import Depends
from depends.message_depends import get_messages_service


router=APIRouter()



@router.get("/", response_model=List[Message])
async def list_messages(service: MessageService= Depends(get_messages_service)):
    #print(f"Service ID: {id(service)}")
    return service.find_all()


@router.get("/view/{message_id}", response_model=Optional[Message])
async def get_message(message_id:int, service: MessageService=Depends(get_messages_service)):
    message = service.find_by_id(message_id)
    if message is None:
        raise HTTPException(status_code=404, detail=f"El mensaje con ID {message_id} no existe")
    return message

@router.get("/details/", response_model=Optional[Message])
def get_message_url_params(id:int= Query(default=..., ge=1),
                            service: MessageService=Depends(get_messages_service)):
    message = service.find_by_id(id)
    if message is None:
        raise HTTPException(status_code=404, detail=f"El mensaje con ID {id} no existe")
    return message