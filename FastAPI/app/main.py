from fastapi import FastAPI
from pydantic import BaseModel



app=FastAPI()


class Producto(BaseModel):
    nombre:str
    precio:float
    en_stock:bool



productos=[]

@app.get("/productos")
def listar_productos():
    return {"productos":productos}



@app.post("/productos")
def create_producto(producto:Producto):

    productos.append(producto)
    return {"mensaje": "producto agregadodo", "producto": producto}


@app.put("/productos/{id}")
def actualizar(id:int, nombre:str):
    productos[id]=nombre
    return {"mensaje": "producto actualizado", "producto": nombre}


@app.delete("/productos/{id}")
def eliminar(id:int):
    eliminado=productos.pop(id)
    return {"mensaje": "producto eliminado", "producto": eliminado}
