from app.services.aggregator import get_coins_with_fallback
import numpy as np

async def detect_price_anomalies():
    out = await get_coins_with_fallback()
    coins = out["data"]
    # Basit: Ani değişim %X üzerindeyse anomali
    anomalies = []
    for c in coins:
        price = c.get("price") or c.get("current_price")
        # Simülasyon: price_history = [önceki fiyatlar] -> prod'da DB'den çekilir
        # Burada rastgele simüle ediyoruz
        if not price: continue
        old_price = price * (np.random.uniform(0.91, 1.09))  # %9 civarı dalgalanma
        change = ((price - old_price) / old_price) * 100
        if abs(change) > 5:  # %5 üzeri değişim anomali kabul
            anomalies.append({
                "name": c.get("name"),
                "symbol": c.get("symbol"),
                "price": price,
                "change": change,
            })
    return {"anomalies": anomalies}