from pydantic import BaseModel



class ProductoCreate(BaseModel):
    nombre: str
    precio: float
    en_stock: bool
    categoria_id:int


class ProductoResponse(ProductoCreate):
    id:int
    class Config:
        orm_mod=True