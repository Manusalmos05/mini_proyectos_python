from sqlalchemy import Column, Integer, String,Float, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base


class Categoria(Base):
    __tablename__="categorias"
    id= Column(Integer,primary_key=True, index=True)
    nombre=Column(String, unique=True, index=True)
    productos=relationship("Producto", back_populates="categorias")