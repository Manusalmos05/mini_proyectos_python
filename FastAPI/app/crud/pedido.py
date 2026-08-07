from sqlalchemy.orm import Session
from models.producto import Producto
from models.pedidos import Pedido, Carrito, DetallePedido


def crear_pedido(db: Session, usuario_id: int):
    carrito=db.query(Carrito).filter(usuario_id=usuario_id).first()
    if not carrito or not carrito.items:
        raise ValueError("El carrito está vacío o no existe")
    total=0
    pedido=Pedido(usuario_id=usuario_id, total=0)
    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    for item in carrito.items:
        producto=db.query(Producto).get(item.producto_id)
        if producto.en_stock is False or producto.precio<0:
            raise ValueError(f"El producto {producto.nombre} no está disponible o tiene un precio inválido")

        if item.cantidad>0 and item.cantidad<=producto.stock:
            producto.stock -= item.cantidad
            subtotal=producto.precio*item.cantidad
            detalle=DetallePedido(
                pedido_id=pedido.id,
                producto_id=producto.id,
                cantidad=item.cantidad,
                subtotal=subtotal
            )
            db.add(detalle)
            total+=subtotal

    pedido.total=total
    db.commit()
    for item in carrito.items:
        db.delete(item)
    db.commit()
    return pedido



