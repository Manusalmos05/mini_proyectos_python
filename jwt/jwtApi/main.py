from fastapi import FastAPI
from fastapi.params import Depends
from config.db import engine, Base
from middlewares.security_middleware import security_middleware
from middlewares.timing_middleware import timing_middleware
from routers import auth,users
from fastapi.security import HTTPBearer
app= FastAPI()

Base.metadata.create_all(bind=engine)

bearer= HTTPBearer()

app.include_router(users.router, prefix="/users", tags=['users'], dependencies=[Depends(bearer)])
app.include_router(auth.router, prefix="/auth",tags=['auth'])


app.middleware("http")(timing_middleware)
app.middleware("http")(security_middleware)



