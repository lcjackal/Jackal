import httpx
from app.config import API_KEYS

BASE_URL = "https://pro-api.coinmarketcap.com/v1"

class CoinMarketCapProvider:
    @staticmethod
    async def get_coins():
        headers = {
            "X-CMC_PRO_API_KEY": API_KEYS["coinmarketcap"]
        }
        url = f"{BASE_URL}/cryptocurrency/listings/latest"
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get(url, headers=headers, params={"limit": 20})  # limit örnek
            if r.status_code == 200:
                return r.json()["data"]
            else:
                raise Exception(f"CoinMarketCap error: {r.status_code} {r.text}")