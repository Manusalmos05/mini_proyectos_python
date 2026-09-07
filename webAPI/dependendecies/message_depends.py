from services.messages_service import MessageService
#from functools import lru_cache
from config.db import SessionLocal
from sqlalchemy.orm import Session
from repositories.sql_alchemy_message_repo import SqlAlchemyMessageRepository
from fastapi.params import Depends
from repositories.message_repository import MessageRepository


def get_db():
    
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_message_repository(db: Session= Depends(get_db))->MessageRepository:
    return SqlAlchemyMessageRepository(db)


#@lru_cache ## persistencia del url durante toda la sesión de la aplicación
def get_messages_service(repo: MessageRepository= Depends(get_message_repository),db: Session= Depends(get_db)) -> MessageService:
    return (repo, db)

    