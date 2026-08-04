from pydantic import BaseModel, ConfigDict




class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass 

class CategoriaResponse(CategoriaBase):
    id: int
    class Config:
        model_config = ConfigDict(from_attributes=True)