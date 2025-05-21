import numpy as np
from app.services.aggregator import get_coin_history
from typing import List, Dict

async def get_price_histories(symbols: List[str], days: int = 30):
    # Her coin için fiyat serisi al
    history_map = {}
    for symbol in symbols:
        history = await get_coin_history(symbol, days=days)
        prices = [point["price"] for point in history]
        if len(prices) == days+1:  # CoinGecko "days" kadar aralık döndürür
            prices = prices[1:]     # ilk anı atla (günlük % değişim için)
        history_map[symbol] = prices
    return history_map

async def correlation_matrix(symbols: List[str], days: int = 30):
    history_map = await get_price_histories(symbols, days)
    price_arrays = [np.array(history_map[s]) for s in symbols if len(history_map[s]) == days]
    if len(price_arrays) < 2:
        return {"error": "Yeterli veri yok"}
    mat = np.corrcoef(price_arrays)
    corr_dict = {}
    for i, sym1 in enumerate(symbols):
        corr_dict[sym1] = {}
        for j, sym2 in enumerate(symbols):
            corr_dict[sym1][sym2] = float(mat[i, j]) if i < len(mat) and j < len(mat) else None
    return {"matrix": corr_dict}

async def market_dominance(symbols: List[str]):
    # Güncel fiyat+marketcap çek
    from app.services.aggregator import get_coins_with_fallback
    data = await get_coins_with_fallback()
    coins = data["data"]
    market_caps = {c["symbol"]: c.get("market_cap", 0) for c in coins if c.get("market_cap")}
    total_cap = sum(market_caps.values())
    dominance = {}
    for symbol in symbols:
        cap = market_caps.get(symbol.lower(), 0)
        dominance[symbol] = round(100 * cap / total_cap, 2) if total_cap else 0.0
    return {"dominance": dominance, "total_cap": total_cap}