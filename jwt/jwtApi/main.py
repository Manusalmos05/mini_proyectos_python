from fastapi import FastAPI
from config.db import engine, Base
from routers import users

app= FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=['users'])

@app.get("/")
def read_root():
    return{"mensaje":"Otra API..."}