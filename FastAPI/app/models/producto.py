from sqlalchemy import Column, Integer, String,Float, Boolean,ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Producto(Base):
    __tablename__="productos"
    id= Column(Integer,primary_key=True, index=True)
    nombre=Column(String, unique=True, index=True)
    precio=Column(Float)
    en_stock= Column(Boolean, default=True)
    categoria_id=Column(Integer, ForeignKey("categorias.id"))
    categorias=relationship("Categoria", back_populates="productos")