from fastapi import APIRouter
from api.v1 import auth, productos, categorias


api_router=APIRouter()


api_router.include_router(auth.api_router,prefix="/auth", tags=["auth"])
api_router.include_router(productos.api_router,prefix="/productos", tags=["productos"])
api_router.include_router(categorias.api_router,prefix="/categorias", tags=["categorias"])