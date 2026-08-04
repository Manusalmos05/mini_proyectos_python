from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from deps.deps import get_db
from crud.categoria import obtener_categorias, crear_categoria
from schemas.categoria import CategoriaCreate, CategoriaResponse

api_router = APIRouter()


@api_router.get("/categorias",response_model=list[CategoriaResponse])
def lista_categorias(db:Session=Depends(get_db)):
    return obtener_categorias(db)



@api_router.post("/categorias", response_model=CategoriaResponse)
def create_categoria(categoria:CategoriaCreate, db:Session=Depends(get_db)):
    return crear_categoria(db, categoria)