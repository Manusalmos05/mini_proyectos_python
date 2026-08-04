from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base

class Usuario(Base):
    __tablename__="usuarios"
    id= Column(Integer,primary_key=True, index=True)
    nombre=Column(String, unique=True, index=True)
    email=Column(String, unique=True, index=True)
    hashed_password=Column(String)
    es_admin=Column(Boolean, default=False)