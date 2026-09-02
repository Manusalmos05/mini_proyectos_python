
from models. message import Message
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query,status
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


@router.post("/", response_model=Message, status_code=status.HTTP_201_CREATED)
def create_message(message: Message, service:MessageService=Depends(get_messages_service)):
    return service.create(message)

@router.put("/{message_id}", response_model=Optional[Message])
def update_message(message_id:int, message: Message, service:MessageService=Depends(get_messages_service)):
    message_update = service.update(message_id, message)
    if message_update is None:
        raise HTTPException(status_code=404, detail=f"El mensaje con ID {message_id} no existe")
    return message_update


@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(message_id:int, service:MessageService=Depends(get_messages_service)):
    deleted = service.delete(message_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"El mensaje con ID {message_id} no existe")
    return None