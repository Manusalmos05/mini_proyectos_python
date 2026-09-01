from services.messages_service import MessageService
from services.message_service_impl import MessageServiceImpl

def get_messages_service() -> MessageService:
    return MessageServiceImpl()