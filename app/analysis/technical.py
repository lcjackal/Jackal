import numpy as np
from app.services.aggregator import get_coin_history

def rsi(prices, period=14):
    deltas = np.diff(prices)
    ups = deltas.clip(min=0)
    downs = -deltas.clip(max=0)
    avg_gain = np.convolve(ups, np.ones(period)/period, mode='valid')
    avg_loss = np.convolve(downs, np.ones(period)/period, mode='valid')
    rs = avg_gain / (avg_loss + 1e-9)
    rsi = 100 - (100 / (1 + rs))
    return rsi[-1] if len(rsi) else None

def macd(prices, slow=26, fast=12, signal=9):
    ema_fast = pd.Series(prices).ewm(span=fast, adjust=False).mean()
    ema_slow = pd.Series(prices).ewm(span=slow, adjust=False).mean()
    macd_line = ema_fast - ema_slow
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    return float(macd_line.iloc[-1]), float(signal_line.iloc[-1])

def volatility(prices, period=14):
    ret = np.diff(prices) / prices[:-1]
    return float(np.std(ret[-period:]))

async def get_technical_indicators(symbol: str):
    # Fiyat geçmişini al (ör: son 30 gün)
    history = await get_coin_history(symbol)
    prices = [point["price"] for point in history]
    indicators = {}
    if len(prices) >= 30:
        indicators["rsi"] = rsi(prices)
        indicators["volatility"] = volatility(prices)
        try:
            indicators["macd"], indicators["macd_signal"] = macd(prices)
        except Exception:
            indicators["macd"], indicators["macd_signal"] = None, None
    else:
        indicators["error"] = "Yeterli veri yok"
    return indicators