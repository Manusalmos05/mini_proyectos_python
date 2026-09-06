from services.messages_service import MessageService
#from functools import lru_cache
from config.db import SessionLocal
from sqlalchemy.orm import Session
from repositories.sql_alchemy_message_repo import SqlAlchemyMessageRepository
from fastapi.params import Depends

def get_db():
    
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_message_repository(db: Session= Depends(get_db))->MessageRpository:
    return SqlAlchemyMessageRepository(db)


#@lru_cache ## persistencia del url durante toda la sesión de la aplicación
def get_messages_service(repo: MessageRpository= Depends(get_message_repository)) -> MessageService:
    return SqlAlchemyMessageService(repo)

    