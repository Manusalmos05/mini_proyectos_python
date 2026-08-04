from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import os
from dotenv import load_dotenv

load_dotenv() 


pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")


def crear_token(sub:str, es_admin: bool):
    minutos_expiracion = int(os.getenv("ACCCES_TOKEN_EXPIRE_MINUTES", 30))
    expire = datetime.now(timezone.utc) + timedelta(minutes=minutos_expiracion)

    data={
        "sub": sub ,
        "exp": expire,
        "es_admin": es_admin
    }

    token=jwt.encode(data, os.getenv("SECRET_KEY"), algorithm="HS256")
    return token
    


def verificar_token(token:str):
    try:
        payload=jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        return payload

    except JWTError: 
        return None

    


### hasheo de contraseñas ###


def hash_password(password:str):
    return pwd_context.hash(password)


def verificar_password(password:str, hashed:str):
    return pwd_context.verify(password, hashed)