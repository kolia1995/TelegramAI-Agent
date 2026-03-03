import requests
from config.settings import settings

def fetch_weather(city_name: str) -> dict:
    try:
        params = {
            "access_key": settings.WEATHER_API_KEY,
            "query": city_name
        }

        response = requests.get(
            settings.WEATHER_API_URL,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            return {"error": True, "message": data["error"].get("info", "API error")}

        current_weather = data["current"]

        return {
            "error": False,
            "city": city_name,
            "temperature": current_weather["temperature"],
            "feels_like": current_weather["feels_like"],
            "description": current_weather["weather_descriptions"][0],
            "wind_speed": current_weather["wind_speed"],
            "wind_direction": current_weather["wind_dir"],
            "humidity": current_weather["humidity"]
        }

    except requests.exceptions.RequestException:
        return {"error": True, "message": f"Network error for city: {city_name}"}

    except Exception as e:
        return {"error": True, "message": str(e)}