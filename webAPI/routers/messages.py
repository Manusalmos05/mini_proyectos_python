from models. message import Message
from typing import List
from fastapi import APIRouter


simple_messages: List[Message]=[
    Message(id=1, text="Aprendiendo..."),
    Message(id=2, text="..fastApi..."),
    Message(id=3, text="... con Python")
]

router=APIRouter()



@router.get("/", response_model=List[Message])
async def list_messages():
    return simple_messages 