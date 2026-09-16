from fastapi import FastAPI
from config.db import engine, Base
from routers import auth,users

app= FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=['users'])
app.include_router(auth.router, prefix="/auth",tags=['auth'])



