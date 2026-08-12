from fastapi import FastAPI
from api.v1.api import api_router





app=FastAPI(
    title="Ecommerce API",
    description="""
        API RESTful completa para la gestion de in E-commerce
        funcionalidades:
        - autenticacion con Jwt
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

app.include_router(api_router, prefix="/api/v1")


