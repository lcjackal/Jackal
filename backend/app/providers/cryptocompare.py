import httpx
from app.config import API_KEYS

BASE_URL = "https://min-api.cryptocompare.com/data"

class CryptoCompareProvider:
    @staticmethod
    async def get_coins():
        url = f"{BASE_URL}/top/mktcapfull"
        params = {
            "limit": 20,
            "tsym": "USD",
            "api_key": API_KEYS.get("cryptocompare")
        }
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get(url, params=params)
            if r.status_code == 200:
                return r.json()["Data"]
            else:
                raise Exception(f"CryptoCompare error: {r.status_code} {r.text}")