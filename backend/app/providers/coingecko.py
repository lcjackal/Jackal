import httpx
from app.config import API_KEYS

BASE_URL = "https://api.coingecko.com/api/v3"

class CoinGeckoProvider:
    @staticmethod
    async def get_coins():
        url = f"{BASE_URL}/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 20,
            "page": 1
        }
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get(url, params=params)
            if r.status_code == 200:
                return r.json()
            else:
                raise Exception(f"CoinGecko error: {r.status_code} {r.text}")