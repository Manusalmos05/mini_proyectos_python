from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv

load_dotenv() 

## prueba ##


def crear_token(data:dict):
    to_encode=data.copy()
    expire=int(datetime.now(timezone.utc)) + int(timedelta(minutes=os.getenv("ACCCES_TOKEN_EXPIRE_MINUTES")))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))


def verificar_token(token:str):
    try:
        payload=jwt.decode(token, os.getenv("SECRET_KEY"), algorithm=[os.getenv("ALGORITHM")])
        return payload

    except JWTError: 
        return None

    
