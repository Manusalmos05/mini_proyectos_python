from fastapi import APIRouter, HTTPException,status
from fastapi.params import Depends
from dependencies.di import get_repository
from security.jwt import create_access_token
from repositories.user_repositorio import UserRepository
from security.passwords import verify_password
from schemas.auth import LoginRequest, TokenDto


router=APIRouter()

@router.post("/token", response_model= TokenDto)
def login(data:LoginRequest, repository: UserRepository=Depends(get_repository)):
    user=repository.find_by_email(str(data.email))

    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales invalidas")

    token=create_access_token(subject=str(user.id))
    return TokenDto(access_token=token)