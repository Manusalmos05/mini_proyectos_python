from fastapi import FastAPI
from typing import List
from routers.messages import router

app=FastAPI()

app.include_router(router, prefix="/messages", tags=["messages"])

@app.get('/')
async def read_data():
    return {
        "mensage": "Tercera API REST con Python + FastAPI"
    } 


