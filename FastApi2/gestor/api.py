from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
import database as db
from pydantic import BaseModel, constr, field_validator
import helpers

class ModeloCliente(BaseModel):
    dni: constr(min_length=3, max_length=3)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)


class ModeloCrearCliente(ModeloCliente):
    @field_validator("dni")
    def validar_dni(cls, dni):
        if helpers.dni_valido(dni, db.Clientes.lista):
            return dni
        raise ValueError("Ya existe este cliente o el DNI es incorrecto")


headers={"content-type":"charset=utf-8"}
app=FastAPI(
    title= "Api de gestion de clientes",
    description="Permite, crear, borrar, actualizar, buscar clientes en una ddbb realizada sobre csv con funciones en Python"
)

@app.get("/clientes", tags=["clientes"])
async def clientes():
    content=[cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content=content, headers=headers)

@app.get("/clientes/buscar/{dni}", tags=["clientes"])
async def clientes_buscar(dni:str):
    cliente=db.Clientes.buscar(dni=dni)
    if cliente is None:
        raise HTTPException(status_code=404, detail="No existe este cliente")
    return JSONResponse(content=cliente.to_dict(), headers=headers)

@app.post("/clientes/crear/", tags=["clientes"])
async def clientes_crear(datos: ModeloCrearCliente):
    cliente=db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    if cliente:
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=401, details="cliente no creado")

@app.put("/clientes/actualizar/", tags=["clientes"])
async def clientes_actualizar(datos:ModeloCliente):
    if db.Clientes.buscar(datos.dni):
        cliente=db.Clientes.modificar(datos.dni, datos.nombre,datos.apellido)
        if cliente:
            return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="cliente no encontrado")

@app.delete("/clientes/eliminar/{dni}/",  tags=["clientes"])
async def clientes_eliminar(dni:str):
    if db.Clientes.buscar(dni=dni):
        cliente=db.Clientes.borrar(dni=dni)
        return JSONResponse(content=cliente.to_dict(), headers=headers)
    raise HTTPException(status_code=404, detail="cliente no encontrado")



print("Servidor de la api")
