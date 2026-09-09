from dotenv import load_dotenv
from pydantic import BaseModel
import os

load_dotenv()

class Settings(BaseModel):
    JWT_SECRET:str= os.getenv("JWT_SECRET")
    JWT_ALG:str=os.getenv("JWT_ALG", "HS256")
    JWT_EXP_MINUTES: int=int(os.getenv("JWT_EXP_MINUTES", 60))
    DATABASE_URL:str=os.getenv("DATABASE_URL")


settings=Settings()
