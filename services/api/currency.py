import requests
from config.settings import settings
from services.utils.geo_utils import GeoService

def convert_currency_by_city(
    source_currency: str,
    amount: float,
    target_currency: str = None,
    city_name: str = None
) -> dict:
    try:
        if not target_currency and city_name:
            geo_service = GeoService(city_name)
            target_currency = geo_service.currency_for_city()
            if not target_currency:
                return {"error": True, "message": "Cannot determine currency for city"}

        params = {
            "access_key": settings.CURRENT_API_KEY,
            "from": source_currency,
            "to": target_currency,
            "amount": amount
        }

        response = requests.get(
            settings.CURRENT_API_URL,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        if not data.get("success", True):
            return {
                "error": True,
                "message": data.get("error", {}).get("info", "API error")
            }

        return {
            "from": data["query"]["from"],
            "to": data["query"]["to"],
            "amount": data["query"]["amount"],
            "result": data["result"]
        }

    except requests.exceptions.RequestException:
        return {
            "error": True,
            "message": f"Network error for {source_currency}, {amount}, {target_currency}"
        }
    except Exception as e:
        return {
            "error": True,
            "message": str(e)
        }