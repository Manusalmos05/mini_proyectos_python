from fastapi import HTTPException,status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from dependencies.di import get_repository
from config.settings import Settings
from repositories.user_repositorio import UserRepository
from entities.user import User as UserEntity

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/token/form")


def get_current_user(repo:UserRepository=Depends(get_repository), token:str=Depends(oauth2_scheme))->UserEntity:
    settings=Settings()
    try:
        payload=jwt.decode(token, settings.JWT_SECRET,algorithms=[settings.JWT_ALG])
        user_id=int(payload.get('sub'))

    except(JWTError, TypeError, ValueError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalido")
    
    user=repo.find_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user

    