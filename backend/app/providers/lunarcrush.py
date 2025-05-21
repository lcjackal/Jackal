import httpx
from app.config import API_KEYS

BASE_URL = "https://api.lunarcrush.com/v2"

class LunarCrushProvider:
    @staticmethod
    async def get_coins():
        params = {
            "data": "market",
            "key": API_KEYS.get("lunarcrush"),
            "limit": 20
        }
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get(BASE_URL, params=params)
            if r.status_code == 200:
                return r.json().get("data", [])
            else:
                raise Exception(f"LunarCrush error: {r.status_code} {r.text}")