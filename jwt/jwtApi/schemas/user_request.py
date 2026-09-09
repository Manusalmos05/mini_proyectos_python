from pydantic import BaseModel, EmailStr, Field
#peticiones del cliente

class UserRequest(BaseModel):
    email:EmailStr
    password: str= Field(..., min_length=6, max_length=64)
