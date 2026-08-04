import crud, schemas
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from deps.deps import get_db

api_router = APIRouter()


@api_router.get("/categorias",response_model=list[schemas.CategoriaResponse])
def lista_categorias(db:Session=Depends(get_db)):
    return crud.obtener_categorias(db)



@api_router.post("/categorias", response_model=schemas.CategoriaResponse)
def create_categoria(categoria:schemas.CategoriaCreate, db:Session=Depends(get_db)):
    return crud.crear_categoria(db, categoria)