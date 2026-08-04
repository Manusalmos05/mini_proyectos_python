from pydantic import BaseModel, ConfigDict, EmailStr


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
        model_config = ConfigDict(from_attributes=True)

