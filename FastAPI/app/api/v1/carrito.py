from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import carrito as crud_carrito
from deps.deps import get_db,get_current_user


api_router = APIRouter()


@api_router.get("/", summary="Ver contenido del carrito")
def ver_carrito(db:Session= Depends(get_db), user=Depends(get_current_user)):
    carrito=crud_carrito.obtener_carrito(db, user.id)
    return carrito


@api_router.post("/agregar/{producto_id}")
def agregar_producto(producto_id:int, cantidad:int=1, db:Session=Depends(get_db), user=Depends(get_current_user)):
    carrito=crud_carrito.obtener_carrito(db, user.id)
    item=crud_carrito.agregar_item(db, carrito.id, producto_id, cantidad)
    return {"message": "Producto agregado al carrito", "item": item}



@api_router.delete("/eliminar/{item_id}")
def eliminar_producto(item_id:int, db:Session=Depends(get_db), user=Depends(get_current_user)):
   crud_carrito.eliminar_item(db, item_id)
   return {"message": "Producto eliminado del carrito"}
