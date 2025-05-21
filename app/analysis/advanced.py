from app.services.aggregator import get_coins_with_fallback
import numpy as np
from typing import List, Dict, Any

async def get_advanced_insights() -> Dict[str, Any]:
    out = await get_coins_with_fallback()
    coins = out["data"]

    prices = [c.get("price") or c.get("current_price") for c in coins if (c.get("price") or c.get("current_price"))]
    changes = [c.get("change_24h") or c.get("price_change_percentage_24h") or 0 for c in coins]

    # 1. Temel istatistikler
    stats = {
        "coin_count": len(coins),
        "price_avg": float(np.mean(prices)) if prices else None,
        "price_min": float(np.min(prices)) if prices else None,
        "price_max": float(np.max(prices)) if prices else None,
        "change_avg": float(np.mean(changes)) if changes else None,
        "change_max": float(np.max(changes)) if changes else None,
        "change_min": float(np.min(changes)) if changes else None,
    }

    # 2. En çok yükselen/düşen coinler (ilk 3)
    sorted_by_change = sorted(coins, key=lambda x: x.get("change_24h") or x.get("price_change_percentage_24h") or 0, reverse=True)
    top_gainers = sorted_by_change[:3]
    top_losers = sorted_by_change[-3:]

    # 3. Büyük hacimli ve yüksek değişim gösteren coinler (örnek sinyal)
    big_movers = [c for c in coins if abs((c.get("change_24h") or c.get("price_change_percentage_24h") or 0)) > 10]

    # 4. Fiyatı belirli bir eşik üzerinde (opsiyonel, örn: $10,000+)
    expensive_coins = [c for c in coins if (c.get("price") or c.get("current_price") or 0) > 10000]

    # 5. Anomali/uyarı (ani değişim)
    anomalies = []
    for c in coins:
        price = c.get("price") or c.get("current_price")
        change = c.get("change_24h") or c.get("price_change_percentage_24h") or 0
        if price and abs(change) > 20:
            anomalies.append({
                "name": c.get("name"),
                "symbol": c.get("symbol"),
                "price": price,
                "change": change,
            })

    return {
        "stats": stats,
        "top_gainers": top_gainers,
        "top_losers": top_losers,
        "big_movers": big_movers,
        "expensive_coins": expensive_coins,
        "anomalies": anomalies,
    }