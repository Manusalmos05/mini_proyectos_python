from services.messages_service import MessageService

def get_messages_service() -> MessageService:
    return MessageService()