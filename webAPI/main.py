from fastapi import FastAPI
from typing import List
from routers import messages

app=FastAPI()

app.include_router(messages.router, prefix="/messages", tags=["messages"])

@app.get('/')
async def read_data():
    return {
        "mensage": "Tercera API REST con Python + FastAPI"
    } 


