from fastapi import APIRouter, Depends, HTTPException
import crud, schemas
from sqlalchemy.orm import Session
from deps.deps import get_db, require_admin

api_router = APIRouter()




@api_router.get("/productos", response_model=list[schemas.ProductoResponse])
def listar_productos(db:Session=Depends(get_db)):
    return crud.obtener_productos(db)



@api_router.post("/productos", response_model=schemas.ProductoCreate, dependencies=[Depends(require_admin)])
def create_producto(producto: schemas.ProductoCreate, db:Session=Depends(get_db)):
    return crud.crear_producto(db, producto)

    
@api_router.put("/productos/{id}",  response_model=schemas.ProductoCreate)
def actualizar_producto(producto_id: int, datos:schemas.ProductoCreate, db:Session=Depends(get_db)):
    producto=crud.actualizar_producto(db,producto_id,datos)
    if not producto:
        raise HTTPException(status_code=404, detail="producto no encontrado")
    return producto
   

@api_router.delete("/productos/{id}")
def eliminar(producto_id:int, db: Session=Depends(get_db)):
    producto=crud.eliminar_producto(db, producto_id)
    if not producto:
            raise HTTPException(status_code=404, detail="producto no encontrado")
    return {"mensaje": "Producto eliminado"}