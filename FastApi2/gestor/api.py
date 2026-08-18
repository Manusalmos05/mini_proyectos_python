from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
import database as db
from pydantic import BaseModel, constr, field_validator
import helpers

class ModeloCliente(BaseModel):
    dni: str=constr(min_length=3, max_length=3)
    nombre: str=constr(min_length=2, max_length=30)
    apellido:str=constr(min_length=2, max_length=30)


class ModeloCrearCliente(ModeloCliente):
    @field_validator("dni")
    def validar_dni(cls, dni):
        if helpers.dni_valido(dni, db.Clientes.lista):
            return dni
        raise ValueError("Ya existe este cliente o el DNI es incorrecto")


headers={"content-type":"charset=utf-8"}

app = FastAPI()
@app.get("/")
async def index():
    content={
        "mensaje": "mi segunda api"
    }
    return JSONResponse(content=content, headers=headers, media_type="aplication/json")

@app.get("/html/")
async def html():
    content="""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>¡Hola mundo!</title>
    </head>
    <body>
        <h1>¡Hola mundo!</h1>
    </body>
    </html>
    """
    return Response(content=content,media_type="text/html")

@app.get("/clientes")
async def clientes():
    content=[cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content=content, headers=headers)

@app.get("/clientes/buscar/{dni}")
async def clientes_buscar(dni:str):
    cliente=db.Clientes.buscar(dni=dni)
    if cliente is None:
        raise HTTPException(status_code=404, detail="No existe este cliente")
    return JSONResponse(content=cliente.to_dict(), headers=headers)

@app.post("/clientes/crear/")
async def clientes_crear(datos: ModeloCrearCliente):
    cliente=db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    if cliente:
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=401, details="cliente no creado")






print("Servidor de la api")
