from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class Categoria(Base):
    __tablename__="categorias"
    id= Column(Integer,primary_key=True, index=True)
    nombre=Column(String, unique=True, index=True)
    productos=relationship("Producto", back_populates="categorias")