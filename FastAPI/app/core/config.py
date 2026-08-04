from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    SECRET_KEY: str
    ACCCES_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str
    ALGORITHM: str= "HS256"

    class Config:
        env_file = ".env"

settings = Setting()