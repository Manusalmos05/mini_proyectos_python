from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
async def index():
    content={
        "mensaje": "mi segunda api"
    }
    return JSONResponse(content=content)

print("Servidor de la api")
