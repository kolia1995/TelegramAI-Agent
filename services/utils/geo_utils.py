import requests
from config.settings import settings

class GeoService:
    def __init__(self, city: str):
        self.city = city

    def get_country(self) -> dict | None:
        try:
            params = {
                "appid": settings.COUNTRIES_API_KEY,
                "q": self.city,
                "limit": 1
            }
            response = requests.get(settings.COUNTRIES_API_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            if not data:
                return None
            return {
                "name": data[0].get("name"),
                "country": data[0].get("country"),
                "state": data[0].get("state")
            }
        except requests.exceptions.RequestException:
            return None

    def get_currency_key(self) -> str | None:
        country_data = self.get_country()
        if not country_data:
            return None
        country_code = country_data["country"]
        try:
            url = f"{settings.CURRENCY_KEYS_API}/{country_code}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            currencies = data[0].get("currencies", {})
            return next(iter(currencies), None)
        except requests.exceptions.RequestException:
            return None

    def currency_for_city(self) -> str | None:
        return self.get_currency_key()