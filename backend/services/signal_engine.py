from typing import List, Dict

def smart_signal_score(market, orderbook, volume, technicals, onchain, sentiment, futures, whales):
    score = 0.5

    # Emir defteri (Orderbook) etkisi
    if orderbook.get("buy_wall", 0) > 100000:  # USDT cinsinden yüksek alış duvarı
        score += 0.1
    if orderbook.get("spread", 0) < 0.1:
        score += 0.05

    # Hacim etkisi
    if volume.get("buy_volume", 0) > 2 * volume.get("avg_volume", 1):
        score += 0.1

    # Teknik göstergeler
    if technicals.get("rsi", 50) < 30:
        score += 0.1
    if technicals.get("macd_cross") == "bullish":
        score += 0.07

    # Zincir üstü veriler
    if onchain.get("whale_accumulation", False):
        score += 0.1
    if onchain.get("exchange_inflow", 0) > 50000:
        score -= 0.05  # borsaya giriş satış baskısı

    # Piyasa duyarlılığı
    if sentiment.get("news", "") == "positive":
        score += 0.05
    if sentiment.get("social", "") == "fud":
        score -= 0.07

    # Vadeli işlemler ve balina hareketleri (gizli ağırlıklandırma)
    if futures.get("open_interest_increase", False):
        score += 0.07
    if futures.get("funding_rate", 0) < -0.01:
        score -= 0.03
    if whales.get("large_buy", False):
        score += 0.09

    # Sınırlandır
    score = max(min(score, 1.0), 0.0)
    return score

def build_signal_row(coin, market, orderbook, volume, technicals, onchain, sentiment, futures, whales):
    score = smart_signal_score(market, orderbook, volume, technicals, onchain, sentiment, futures, whales)
    sources = [
        {"type": "orderbook", "detail": f"Buy wall {orderbook.get('buy_wall', 0)}"},
        {"type": "volume", "detail": f"Buy vol {volume.get('buy_volume', 0)}"},
        {"type": "rsi", "detail": f"RSI {technicals.get('rsi', '')}"},
        {"type": "macd", "detail": technicals.get("macd_cross", '')},
        {"type": "onchain", "detail": "Whale birikimi" if onchain.get("whale_accumulation") else ""},
        {"type": "sentiment", "detail": sentiment.get("news", "")},
    ]
    # Sadece dolu detayları göster
    sources = [s for s in sources if s["detail"]]
    rationale = "Emir defteri, hacim, teknik ve zincir üstü ile güçlendirilmiş sinyal."
    if futures.get("open_interest_increase", False) or whales.get("large_buy", False):
        rationale += " (Gizli: Vadeli işlemler ve balina hareketleri de algoritmada dikkate alındı.)"
    return {
        "coin": coin,
        "movement_type": "karma_sinyal",
        "sources": sources,
        "score": score,
        "max_potential_price": market.get("potential_price"),
        "expected_time_window": "1-3 saat",
        "notes": "",
        "rationale": rationale,
        "success_rate": 0.78  # Örnek
    }