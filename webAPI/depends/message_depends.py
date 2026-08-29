from services.messages_service import MessageServiceImpl, MessageService

def get_messages_service() -> MessageService:
    return MessageServiceImpl()