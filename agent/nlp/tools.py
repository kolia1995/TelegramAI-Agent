from services.api.weather import fetch_weather
from services.api.currency import convert_currency_by_city
from services.api.news import fetch_news_articles

from prompts.tool_prompts.load_tool_prompts import format_weather_text, format_currency_text, format_news_text

def tools_weather(city: str) -> str:
    resp = fetch_weather(city_name=city)

    if resp.get("error"):
        return resp.get("message", "Unable to fetch weather data.")
    
    return format_weather_text(weather=resp)

def tools_currency(source_currency: str, amount: float, target_currency: str, city_name: str) -> str:
    resp = convert_currency_by_city(
        source_currency=source_currency,
        target_currency=target_currency,
        amount=amount,
        city_name=city_name
    )

    if resp.get("error"):
        return resp.get("message", "Currency conversion failed.")
    
    return format_currency_text(currency=resp)

def tools_news(query: str) -> str:
    resp = fetch_news_articles(quit=query)

    if resp.get("error"):
        return resp.get("message", "Unable to fetch news articles.")
    
    return format_news_text(news_list=resp)