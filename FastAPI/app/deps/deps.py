from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError
from sqlalchemy.orm import Session
from db.database import SessionLocal
from app.authS import verificar_token
import crud


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    db= SessionLocal()
    try:
        yield db 
    finally:
        db.close()


def get_current_user(token:str= Depends(oauth2_scheme),
                     db: Session =Depends(get_db)
):

    cred_exc=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No autenticado",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload=verificar_token(token)
        email:str|None =payload.get("sub")
        if email is None:
            raise cred_exc

    except JWTError: 
        raise cred_exc

    user=crud.obtener_usuario_por_email(db, email)
    if user is None:
        raise cred_exc
    return user


def require_admin(current_user= Depends(get_current_user)):
    if not current_user.es_admin:
        raise HTTPException(status_code=403, detail="No autorizado, solo admins")




