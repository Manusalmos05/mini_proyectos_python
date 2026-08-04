from schemas.categoria import CategoriaCreate
from sqlalchemy.orm import Session
from models.categoria import Categoria


def crear_categoria(db: Session, categoria: CategoriaCreate):
    db_categoria =Categoria(nombre=categoria.nombre)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def obtener_categorias(db:Session):
    return db.query(Categoria).all()