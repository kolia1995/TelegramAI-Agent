from pathlib import Path

PROMPT_FOLDER = Path(__file__).parent

def format_weather_text(weather: dict) -> str:
    prompt_file = PROMPT_FOLDER / "weather.txt"
    template = prompt_file.read_text(encoding="utf-8")

    return template.format(
        city=weather['city'],
        temperature=weather['temperature'],
        feels_like=weather['feels_like'],
        description=weather['description'],
        wind_speed=weather['wind_speed'],
        wind_direction=weather['wind_direction'],
        humidity=weather['humidity']
    )

def format_currency_text(currency: dict) -> str:
    prompt_file = PROMPT_FOLDER / "currency.txt"
    template = prompt_file.read_text(encoding="utf-8")

    return template.format(
        source_currency=currency["from"],
        target_currency=currency["to"],
        amount=currency["amount"],
        result=currency["result"]
    )

def format_news_text(news_list: list[dict]) -> str:
    prompt_file = PROMPT_FOLDER / "news.txt"
    template = prompt_file.read_text(encoding="utf-8")

    return template.format(news_list=news_list)