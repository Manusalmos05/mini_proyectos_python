from passlib.context import CryptContext

### hasheo de contraseñas ###

pwd_context=CryptContext(schemes=["bcrypt"], deprecate="auto")



def hash_password(password:str):
    return pwd_context.hash(password)


def varificar_password(password:str, hashed:str):
    return pwd_context.verify(password, hashed)