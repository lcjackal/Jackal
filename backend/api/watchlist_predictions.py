# ...önceki kod
@router.post("/api/watchlist-predictions")
async def watchlist_predictions(request: Request):
    body = await request.json()
    coins: List[str] = body.get("coins", [])
    api_keys = body.get("api_keys", {})
    if not coins:
        return {"predictions": [], "weekly_opportunities": []}
    live = all(api_keys.get(k) for k in ["binance", "etherscan", "lunarcrush"])
    demo = []
    weekopps = []
    # ...devamı yukarıdaki gibi