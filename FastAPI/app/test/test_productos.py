from fastapi.testclient import TestClient
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app


client= TestClient(app)
#token usuario admin
token="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJoZXJhQGV4YW1wbGUuY29tIiwiZXhwIjoxNzg2Nzk3NDcyLCJlc19hZG1pbiI6dHJ1ZX0.iIa5VxWb0kNxRmJZ_9TzzaK9cNN8wtU33eAfd870bYQ"

def test_crear_producto_exito():
    data={
        "nombre": "mouse bluetooth",
        "precio": 15,
        "stock":20,
        "en_stock": True,
        "categoria_id": 1
    }
    headers={"Authorization":token}
    response=client.post('/api/v1/productos/productos', json=data, headers=headers)
    assert response.status_code==200
    assert response.json()["nombre"]==data["nombre"]
    assert response.json()["precio"]==data["precio"]