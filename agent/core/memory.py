from db.models import Memory
from db.session import DBSession

TRIGGERS = {
    "positive": [
        "i like", "i love", "like me", "enjoy", "amazing", "мені подобається", "я люблю"
    ],
    "negative": [
        "i hate", "i don't like", "dislike", "terrible", "bad", "не подобається", "не люблю"
    ],
    "work": [
        "meeting", "deadline", "project", "promotion", "boss", "colleague", "overtime", "job stress"
    ],
    "study": [
        "exam", "homework", "assignment", "lecture", "study group", "test", "grade", "research"
    ],
    "family": [
        "parents", "siblings", "children", "spouse", "relatives", "family dinner",
        "vacation with family", "family problems"
    ],
    "location": [
        "i live in", "i'm from", "i am from", "living in", "my city", "my town",
        "where i live", "my hometown", "place i live", "my address", "born in", "from the city"
    ],
    "name": [
        "my name is", "i am called", "call me", "it's", "мене звати", "я", "моя кличка"
    ],
    "instructions": [
        "please", "could you", "i want you to", "follow this", "do this", "help me", 
        "покажи", "зроби це", "допоможи мені", "будь ласка"
    ]
}

def save_user_fact(user_id: str, content: str) -> None:
    if not content:
        return

    text = content.lower().strip()

    for trigger_type, phrases in TRIGGERS.items():
        for phrase in phrases:
            if phrase in text:
                after_trigger = text.split(phrase, 1)[1].strip()

                if not after_trigger or len(after_trigger) < 3 or "?" in after_trigger:
                    continue

                memory = Memory(
                    telegram_id=user_id,
                    key=trigger_type,
                    value=after_trigger
                )

                with DBSession() as session:
                    memory.save(session)
                    return

def get_user_facts(user_id: str) -> list[dict] | None:
    with DBSession() as session:
        memory = Memory(telegram_id=user_id, key="", value="")
        if memory.exists(session) is None:
            return None
        return memory.get_all(session)