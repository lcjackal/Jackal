from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()

# Örnek veri
detected_movements = [
    {
        "coin": "BTC",
        "movement_type": "rsi_cross",
        "sources": [
            {"type": "rsi", "detail": "RSI<30"},
            {"type": "onchain", "detail": "Whale birikimi"},
            {"type": "volume", "detail": "Yüksek alım hacmi"}
        ],
        "detected_at": "2025-05-20T21:00:00Z",
        "score": 0.94,
        "max_potential_price": 72200,
        "expected_time_window": "2 saat",
        "notes": "RSI ve zincir üstü whale hareketiyle destekleniyor.",
        "rationale": "RSI oversold, büyük cüzdan girişleri ve alım hacmi aynı anda.",
        "success_rate": 0.78  # Son 30 benzer sinyalde başarı oranı
    },
    {
        "coin": "ETH",
        "movement_type": "orderbook_wall",
        "sources": [
            {"type": "orderbook", "detail": "Buy wall 1200 ETH"},
            {"type": "volume"}
        ],
        "detected_at": "2025-05-20T21:30:00Z",
        "score": 0.89,
        "max_potential_price": 4005,
        "expected_time_window": "1-3 saat",
        "notes": "Emir defterinde güçlü alış duvarı ve hacim yükseliyor.",
        "rationale": "Buy wall + hacim artışı.",
        "success_rate": 0.71
    }
]

potential_opportunities = [
    {
        "coin": "BTC",
        "sources": ["rsi", "onchain", "volume"],
        "price_target": 72200,
        "expected_time": "2 saat içinde",
        "score": 0.96,
        "rationale": "Aynı anda RSI<30, balina birikimi ve hacim spike.",
        "success_rate": 0.78,
        "current_price": 69000
    },
    {
        "coin": "ETH",
        "sources": ["orderbook", "volume"],
        "price_target": 4005,
        "expected_time": "1-3 saat",
        "score": 0.91,
        "rationale": "Orderbook'ta büyük alış duvarı ve yüksek hacim.",
        "success_rate": 0.71,
        "current_price": 3870
    }
]

@app.get("/api/detected-movements")
def get_detected_movements():
    return detected_movements

@app.get("/api/potential-opportunities")
def get_potential_opportunities():
    return potential_opportunities