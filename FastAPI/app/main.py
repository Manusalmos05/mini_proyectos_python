from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
import crud as crud, schemas as schemas
from database import get_db



app=FastAPI()


class Producto(BaseModel):
    nombre:str
    precio:float
    en_stock:bool





@app.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db:Session=Depends(get_db)):
    return crud.obtener_productos(db)

    



@app.post("/productos", response_model=schemas.ProductoCreate)
def create_producto(producto: schemas.ProductoCreate, db:Session=Depends(get_db)):
    return crud.crear_producto(db, producto)

    


@app.put("/productos/{id}",  response_model=schemas.ProductoCreate)
def actualizar_producto(producto_id: int, datos:schemas.ProductoCreate, db:Session=Depends(get_db)):
    producto=crud.actualizar_producto(db,producto_id,datos)
    if not producto:
        raise HTTPException(status_code=404, detail="producto no encontrado")
    return producto
   

@app.delete("/productos/{id}")
def eliminar(producto_id:int, db: Session=Depends(get_db)):
    producto=crud.eliminar_producto(db, producto_id)
    if not producto:
            raise HTTPException(status_code=404, detail="producto no encontrado")
    return {"mensaje": "Producto eliminado"}


##### categorias###

@app.get("/categorias",response_model=list[schemas.CategoriaResponse])
def lista_categorias(db:Session=Depends(get_db)):
     return crud.obtener_categorias(db)



@app.post("/categorias", response_model=schemas.CategoriaResponse)
def create_categoria(categoria:schemas.CategoriaCreate, db:Session=Depends(get_db)):
     return crud.crear_categoria(db, categoria)

