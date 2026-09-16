from fastapi import Form
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenDto(BaseModel):
    access_token:str
    token_type:str="bearer"