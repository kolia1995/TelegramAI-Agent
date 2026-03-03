# settings.py
import os
from dotenv import load_dotenv

load_dotenv()  #.env

class Settings:
    # Postgres
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")

    # Telegram API
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    # Weather API
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    WEATHER_API_URL = os.getenv("WEATHER_API_URL")

    # Currency API
    CURRENT_API_KEY = os.getenv("CURRENT_API_KEY")
    CURRENT_API_URL = os.getenv("CURRENT_API_URL")

    # News API
    NEWS_API_URL = os.getenv("NEWS_API_URL")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    # API utils
    COUNTRIES_API_URL = os.getenv("COUNTRIES_API_URL")
    COUNTRIES_API_KEY = os.getenv("COUNTRIES_API_KEY")
    CURRENCY_KEYS_API = os.getenv("CURRENCY_KEYS_API")

    # LLM
    LLM_API_KEY = os.getenv("LLM_API_KEY")
    LLM_MODEL = os.getenv("LLM_MODEL")

settings = Settings()