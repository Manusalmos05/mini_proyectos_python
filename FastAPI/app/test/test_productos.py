from fastapi.testclient import TestClient
import os
import sys


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from db.database import SessionLocal
from models.producto import Producto


client= TestClient(app)
#token usuario admin
token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoZXJhQGV4YW1wbGUuY29tIiwiZXhwIjoxNzg2ODEyNTk0LCJlc19hZG1pbiI6dHJ1ZX0.DcrfQa4o-GHZPP1Z-oxAcnewgVtJR34U3MgAwrRW8wA"

def test_crear_producto_exito():
    data={
        "nombre": "radio",
        "precio": 45,
        "stock":20,
        "en_stock": True,
        "categoria_id": 1
    }
    headers={"Authorization":token}
    response=client.post('/api/v1/productos/productos', json=data, headers=headers)
    assert response.status_code==200
    assert response.json()["nombre"]==data["nombre"]
    assert response.json()["precio"]==data["precio"]


#crear producto sin nombre
def test_crear_producto_fallas():
    data={
            "precio": 15,
            "stock":20,
            "en_stock": True,
            "categoria_id": 1
        }
    headers={"Authorization":token}
    response=client.post('/api/v1/productos/productos', json=data, headers=headers)
    assert response.status_code==422
    assert "nombre" in response.text
    

# mostrar todos los productos
def test_listar_productos():
    response=client.get("/api/v1/productos/")
    assert response.status_code==200
    assert isinstance(response.json(), list)


#eliminar producto

def test_eliminar_producto():
    db=SessionLocal()
    producto_existente=db.query(Producto).filter(Producto.id==15).first()
    id_producto=producto_existente.id
    db.close()
    response=client.delete(f"/api/v1/productos/productos/{id_producto}?producto_id={id_producto}")
    assert response.status_code==200


#actualizar producto

def test_actualizar_producto_exito():
    db=SessionLocal()
    producto_existente=db.query(Producto).filter(Producto.id==8).first()
    id_producto=producto_existente.id
    db.close()
    data={"nombre": "auriculares",
            "precio": 45,
            "stock":20,
            "en_stock": True,
            "categoria_id": 1}
    
    headers={"Authorization":token}
    response=client.put(f"/api/v1/productos/productos/{id_producto}?producto_id={id_producto}", json=data, headers=headers)
    assert response.status_code==200


    