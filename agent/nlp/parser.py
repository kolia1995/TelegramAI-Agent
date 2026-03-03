import spacy
import re
import json

from agent.nlp.intents import TRIGGERS

CURRENCY_MAP = {
        "dollar": "USD",
        "dollars": "USD",
        "usd": "USD",
        "hryvnia": "UAH",
        "hryvnias": "UAH",
        "uah": "UAH",
        "euro": "EUR",
        "eur": "EUR"
    }

STOP_WORDS = {
    "the", "a", "an", "and", "or"
}

def extract_intent(text: str) -> dict | None:
    text_lower = text.lower()

    for trigger_type, phrases in TRIGGERS.items():
        for trigger in phrases:
            if trigger in text_lower:
                nlp = spacy.load("en_core_web_sm")
                doc = nlp(text)

                result = {
                    "TRIGGER": "",
                    "LOCATION": [],
                    "CURRENCY": [],
                    "AMOUNT": [],
                    "DATE": [],
                    "TOPIC": []
                }

                result["TRIGGER"] = trigger_type

                for ent in doc.ents:
                    if ent.label_ in ["GPE", "LOC"]:
                        result["LOCATION"].append(ent.text)
                    else:
                        result["DATE"].append(ent.text)

                for token in doc:
                    key = token.text.lower()
                    if key in CURRENCY_MAP:
                        result["CURRENCY"].append(CURRENCY_MAP[key])

                numbers = re.findall(r'\b\d+(\.\d+)?\b', text)
                for n in numbers:
                    try:
                        result["AMOUNT"].append(float(n))
                    except ValueError:
                        pass

                entities_flat = set(result["LOCATION"] + result["CURRENCY"] + [str(a) for a in result["AMOUNT"]] + result["DATE"])
                for token in doc:
                    word = token.text.strip()
                    if word not in entities_flat and word.lower() not in STOP_WORDS:
                        result["TOPIC"].append(word)

                result["LOCATION"] = list(set(result["LOCATION"]))
                result["CURRENCY"] = list(set(result["CURRENCY"]))
                result["AMOUNT"] = list(set(result["AMOUNT"]))
                result["DATE"] = list(set(result["DATE"]))

                return result
    return None