from pydantic import BaseModel, Field, EmailStr

class Message(BaseModel):
    id: int | None = None
    text: str = Field(..., min_length=8, max_length=50, description="El texto del mensaje debe tener entre 8 y 50 caracteres")
    author_email: EmailStr | None = Field(default=None, description="El correo electrónico del autor del mensaje")
    priority: int = Field(default=1, ge=1, le=5, description="La prioridad del mensaje debe estar entre 1 y 5. siendo 1 la prioridad más baja y 5 la más alta")