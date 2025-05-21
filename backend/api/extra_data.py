from fastapi import APIRouter, Request
import requests

router = APIRouter()

@router.post("/api/extra-data")
async def extra_data(request: Request):
    body = await request.json()
    coin = body.get("coin", "")
    api_keys = body.get("api_keys", {})
    res = {}

    # On-chain: Etherscan (örnek olarak ETH için)
    if coin.upper() == "ETH" and api_keys.get("etherscan"):
        try:
            url = f"https://api.etherscan.io/api?module=stats&action=ethprice&apikey={api_keys['etherscan']}"
            data = requests.get(url).json()
            if data["status"] == "1":
                res["onchain"] = {
                    "ethusd": data["result"]["ethusd"],
                    "ethbtc": data["result"]["ethbtc"]
                }
        except Exception as e:
            res["onchain_error"] = str(e)

    # Sentiment: LunarCrush örneği
    if api_keys.get("lunarcrush"):
        try:
            url = f"https://api.lunarcrush.com/v2?data=assets&key={api_keys['lunarcrush']}&symbol={coin.upper()}"
            data = requests.get(url).json()
            if data["data"]:
                res["sentiment"] = {
                    "galaxy_score": data["data"][0].get("galaxy_score"),
                    "alt_rank": data["data"][0].get("alt_rank"),
                    "social_volume": data["data"][0].get("social_volume"),
                    "news": data["data"][0].get("news"),
                }
        except Exception as e:
            res["sentiment_error"] = str(e)
    return res