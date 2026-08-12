from fastapi import APIRouter, Depends, HTTPException
from crud.producto import obtener_productos, crear_producto, actualizar_producto, eliminar_producto
from schemas.producto import ProductoCreate, ProductoResponse
from schemas.producto import ProductoCreate, ProductoResponse
from sqlalchemy.orm import Session
from deps.deps import get_db, require_admin

api_router = APIRouter()




@api_router.get("/productos", summary="obtener producto", response_description="producto mostrado correctamente", response_model=list[ProductoResponse])
def listar_productos(db:Session=Depends(get_db)):
    return obtener_productos(db)



@api_router.post("/productos", summary="crear producto", response_description="producto creado correctamente", response_model=ProductoCreate, dependencies=[Depends(require_admin)])
def create_producto(producto: ProductoCreate, db:Session=Depends(get_db)):
    return crear_producto(db, producto)

    
@api_router.put("/productos/{id}",summary="actualizar producto", response_description="producto actualizado correctamente",  response_model=ProductoCreate)
def actualizar_producto(producto_id: int, datos:ProductoCreate, db:Session=Depends(get_db)):
    producto=actualizar_producto(db,producto_id,datos)
    if not producto:
        raise HTTPException(status_code=404, detail="producto no encontrado")
    return producto
   

@api_router.delete("/productos/{id}",summary="eliminar producto", response_description="producto eliminado correctamente")
def eliminar(producto_id:int, db: Session=Depends(get_db)):
    producto=eliminar_producto(db, producto_id)
    if not producto:
            raise HTTPException(status_code=404, detail="producto no encontrado")
    return {"mensaje": "Producto eliminado"}