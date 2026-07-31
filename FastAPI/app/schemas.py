from pydantic import BaseModel, EmailStr


### productos ###

class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    categoria_id:int


class ProductoResponse(ProductoCreate):
    id:int
    class Config:
        orm_mod=True
### categoria ###

class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass 

class CategoriaResponse(CategoriaBase):
    id: int
    class Config:
        orm_mode=True


### usuario ###

class UsuarioBase(BaseModel):
    nombre:str
    email: EmailStr


class Usuariocreate(UsuarioBase):
    password: str
    es_admin: bool=False


class UsuarioResponse(UsuarioBase):
    id:int
    es_admin: bool= False
    class Config:
        orm_mode=True

class Token (BaseModel):
    access_token: str
    token_type:str= "bearer"