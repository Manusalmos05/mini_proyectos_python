import bcrypt

def hash_password(text:str)->str:
    return bcrypt.hashpw(text.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(text:str, hashed:str)->bool:
    return bcrypt.checkpw(text.encode("utf-8"), hashed.encode('utf-8'))