import requests
from config.settings import settings

def fetch_news_articles(query: str, max_articles: int = 5) -> list[dict]:
    try:
        params = {
            "q": query,
            "pageSize": max_articles,
            "page": 2,
            "apiKey": settings.NEWS_API_KEY
        }

        response = requests.get(settings.NEWS_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            return {"error": True, "message": data["error"].get("info", "API error")}

        articles = data.get("articles", [])
        result = []

        for article in articles:
            result.append({
                "author": article.get("author", "Unknown author"),
                "title": article.get("title", "No title"),
                "description": article.get("description", "No description"),
                "url": article.get("url", "No URL"),
                "published_at": article.get("publishedAt", "No date")
            })

        return result

    except requests.exceptions.RequestException:
        return {"error": True, "message": f"Network error for query: {query}"}

    except Exception as e:
        return {"error": True, "message": str(e)}