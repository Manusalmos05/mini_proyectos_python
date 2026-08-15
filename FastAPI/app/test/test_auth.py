from fastapi.testclient import TestClient
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app


client= TestClient(app)
#login

def test_login_invalido():
    response=client.post(
        "/api/v1/auth/login", 
        data={
            "username":"example@example.com",
            "password": "7895"
         })
    assert response.status_code==401

# ping docs-verifica que sea accesible docs

def test_ping_docs():
    response=client.get("/docs")
    assert response.status_code==200