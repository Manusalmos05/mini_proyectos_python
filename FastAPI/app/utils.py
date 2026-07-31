from passlib.context import CryptContext

### hasheo de contraseñas ###

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")



def hash_password(password:str):
    return pwd_context.hash(password)


def verificar_password(password:str, hashed:str):
    return pwd_context.verify(password, hashed)