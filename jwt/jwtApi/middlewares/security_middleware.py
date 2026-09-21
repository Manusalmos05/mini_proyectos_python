from fastapi import Request, status, HTTPException
from jose import jwt, JWTError
from config.settings import Settings
from fastapi.responses import JSONResponse
from config.db import SessionLocal
from repositories.sqlAlchemy_userRepository import SqlAlchemyUserRepository
EXCLUDED_PREFIX=("/docs", "/redoc", "/openapi.json")
EXCLUEDED_PATHS=["/", "/auth/token", "/auth/token/form"]


async def security_middleware(request:Request, call_next):
    settings=Settings()
    path=request.url.path
    if path in EXCLUEDED_PATHS or path.startswith(EXCLUDED_PREFIX):
        return await call_next(request)
    auth=request.headers.get("Authorization", "")
    if not auth.startswith("Bearer"):
         return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"datail":"No autenticado"})
    token=auth.removeprefix("Bearer").strip()
    try:
            payload=jwt.decode(token, settings.JWT_SECRET,algorithms=[settings.JWT_ALG])
            user_id=int(payload.get('sub'))
    
    except(JWTError, TypeError, ValueError):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"datail":"Token invalido"})

    with SessionLocal() as db:
        user=SqlAlchemyUserRepository(db).find_by_id(user_id)
        if not user:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"datail":"Usuario no encontrado"})
        
        request.state.user=user
    return await call_next(request)