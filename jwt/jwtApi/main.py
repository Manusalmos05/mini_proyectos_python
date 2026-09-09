from fastapi import FastAPI
from config.db import engine, Base
import entities.user

app= FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return{"mensaje":"Otra API..."}