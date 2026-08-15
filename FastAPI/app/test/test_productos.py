from fastapi.testclient import TestClient
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app


client= TestClient(app)
#token usuario admin
token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoZXJhQGV4YW1wbGUuY29tIiwiZXhwIjoxNzg2Nzk5MDY0LCJlc19hZG1pbiI6dHJ1ZX0.WtHNptoJV70VNIt1Y3KrTHw3uegOAtJbf7aD6OykMs8"

def test_crear_producto_exito():
    data={
        "nombre": "altavoz",
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