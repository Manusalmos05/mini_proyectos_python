from services.messages_service import MessageService
from services.message_service_impl import MessageServiceImpl
from functools import lru_cache

@lru_cache ## persistencia del url durante toda la sesión de la aplicación
def get_messages_service() -> MessageService:
    return MessageServiceImpl()