from fastapi import FastAPI
from api.v1.api import api_router
from fastapi.responses import HTMLResponse





app=FastAPI(
    title="Ecommerce API",
    description="""
        API RESTful completa para la gestion de in E-commerce
        funcionalidades:
        - Autenticacion con Jwt
        -Administración de productos y categorias
        -Carrito de compras
        -Gestión de pedidos
    """,
    version="1.0.0",
    contact={
        "name": "Manuela Salazar Moscoso",
        "url": "https://github.com/Manusalmos05/mini_proyectos_python/tree/main/FastAPI",
        "email": "manuelasalazarmoscoso@gmail.com"
    },
    license_info={
        "name": "MIT Lincense",
        "url": "https://opensource.org/license/MIT"
    }

)
@app.get('/', tags=['inicio'])
def read_root():
    return HTMLResponse('<h2> Esta es mi primera API con FASTAPI </h2>')




app.include_router(api_router, prefix="/api/v1")


