from app.services.aggregator import get_coin_history
import numpy as np

async def time_series_summary(symbol: str, days: int = 30):
    history = await get_coin_history(symbol, days)
    if not history or len(history) < 2:
        return {"error": "Yeterli veri yok"}
    prices = [point["price"] for point in history]
    volumes = [point.get("volume", 0) for point in history]
    # Son gün, 7 gün, 30 gün değişimi vs.
    current = prices[-1]
    prev_1d = prices[-2] if len(prices) > 1 else current
    prev_7d = prices[-8] if len(prices) > 7 else prices[0]
    prev_30d = prices[0]
    change_1d = 100 * (current - prev_1d) / prev_1d if prev_1d else 0
    change_7d = 100 * (current - prev_7d) / prev_7d if prev_7d else 0
    change_30d = 100 * (current - prev_30d) / prev_30d if prev_30d else 0
    # Hacimlerin ortalaması
    avg_vol_7d = float(np.mean(volumes[-7:])) if len(volumes) >= 7 else float(np.mean(volumes))
    avg_vol_30d = float(np.mean(volumes))
    return {
        "symbol": symbol,
        "current_price": current,
        "change_1d": change_1d,
        "change_7d": change_7d,
        "change_30d": change_30d,
        "avg_vol_7d": avg_vol_7d,
        "avg_vol_30d": avg_vol_30d,
    }