import httpx
from app.config import API_KEYS

BASE_URL = "https://api.bscscan.com/api"

class BscScanProvider:
    @staticmethod
    async def get_coins():
        params = {
            "module": "account",
            "action": "tokentx",
            "address": "0x0000000000000000000000000000000000000000",  # örnek adres
            "apikey": API_KEYS.get("bscscan"),
            "page": 1,
            "offset": 10,
            "sort": "desc"
        }
        async with httpx.AsyncClient(timeout=8) as client:
            r = await client.get(BASE_URL, params=params)
            if r.status_code == 200:
                return r.json()
            else:
                raise Exception(f"BscScan error: {r.status_code} {r.text}")