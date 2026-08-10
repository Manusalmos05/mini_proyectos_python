from sqlalchemy.orm import Session
from models.pedidos import Carrito, ItemCarrito


def obtener_carrito(db: Session, usuario_id: int):
    carrito= db.query(Carrito).filter(Carrito.usuario_id == usuario_id).first()
    if carrito:
        return carrito
    else:
        carrito= Carrito(usuario_id=usuario_id)
        db.add(carrito)
        db.commit()
        db.refresh(carrito)
        return carrito

def agregar_item(
        db:Session,
        carrito_id:int,
        producto_id:int,
        cantidad:int = 1
):
    item = db.query(ItemCarrito).filter(ItemCarrito.carrito_id == carrito_id, ItemCarrito.producto_id == producto_id).first()
    if item:
        item.cantidad += cantidad
    else:
        item = ItemCarrito(carrito_id=carrito_id, producto_id=producto_id, cantidad=cantidad)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item


def eliminar_item(db: Session, item_id: int):
    item=db.query(ItemCarrito).get(item_id)
    if item:
        db.delete(item)
        db.commit()
       