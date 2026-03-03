from db.models import Memory
from db.session import DBSession

from agent.nlp.parser import extract_intent
from agent.nlp.tools import tools_weather, tools_currency,  tools_news

def route_intent(context: str, telegram_id: int) -> str | None:
    result = extract_intent(context)

    if not result:
        return None

    if "city" not in result or not result["LOCATION"]:
        memory = Memory(
            telegram_id=telegram_id,
            key="location",
            value=""
        )

        with DBSession() as cur:
            saved = memory.get_by_key(cur)

            if saved:
                words = saved.split()
                capital_words = [
                    w for w in words
                    if w and w[0].isupper()
                ]

                if capital_words:
                    result["LOCATION"].append(capital_words[0])

    if result["TRIGGER"] == "weather":

        if "LOCATION" not in result["LOCATION"]:
            return "Please enter a city."

        return tools_weather(
            city=result["LOCATION"][0]
        )
    
    elif result["TRIGGER"] == "currency":

        if not all(k in result for k in ["from", "amount", "to"]):
            return "Example: USD 100 EUR"

        return tools_currency(
            froms=result["CURRENCY"][0],
            amount=result["AMOUNT"][0],
            to=result["CURRENCY"][1] if len(result["CURRENCY"]) > 1 else None, 
            city=result["LOCATION"][0]
        )

    elif result["TRIGGER"] == "news":
        if "TOPIC" not in result["TOPIC"]:
            return "Information is incorrect or topic is not defined."
        
        q = " AND ".join(result["TOPIC"] + result.get("LOCATION", []))

        return tools_news(
            name=q
        )

    return None