import httpx
from app.config import API_KEYS

BASE_URL = "https://data.messari.io/api/v2"

class MessariProvider:
    @staticmethod
    async def get_coins():
        headers = {
            "x-messari-api-key": API_KEYS["messari"]
        }
        url = f"{BASE_URL}/assets"
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get(url, headers=headers, params={"limit": 20})
            if r.status_code == 200:
                return r.json()["data"]
            else:
                raise Exception(f"Messari error: {r.status_code} {r.text}")