from db.models import Message
from db.session import DBSession

def save_chat_message(user_id: int, content: str, role: str) -> None:
    with DBSession() as session:
        message = Message(telegram_id=user_id, content=content, role=role)
        message.save(session)


def get_chat_history(user_id: int) -> list[dict] | None:
    with DBSession() as session:
        message = Message(telegram_id=user_id, content="", role="")
        if message.exists(session) is None:
            return None
        return message.get_all(session)