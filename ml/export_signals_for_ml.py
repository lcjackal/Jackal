import csv

signals = [
    {
        "coin": "BTC",
        "movement_type": "rsi_cross",
        "sources": ["rsi", "onchain", "volume"],
        "predicted_price": 72200,
        "expected_time_window": "2 saat",
        "prediction_made_at": "2025-05-20T21:00:00Z",
        "achieved": True,
        "achieved_at": "2025-05-20T22:30:00Z",
        "actual_max_price": 72250,
        "explainability": "RSI<30, whale birikimi, hacim",
        "rationale": "RSI ve zincir üstü whale hareketiyle destekleniyor."
    },
    {
        "coin": "ETH",
        "movement_type": "orderbook_wall",
        "sources": ["orderbook", "volume"],
        "predicted_price": 4005,
        "expected_time_window": "3 saat",
        "prediction_made_at": "2025-05-20T21:30:00Z",
        "achieved": False,
        "achieved_at": "",
        "actual_max_price": 3993,
        "explainability": "Buy wall, hacim",
        "rationale": "Emir defteri ve hacim birlikte."
    },
]

with open("signals_ml_dataset.csv", "w", newline='') as csvfile:
    fieldnames = [
        "coin", "movement_type", "sources", "predicted_price",
        "expected_time_window", "prediction_made_at", "achieved",
        "achieved_at", "actual_max_price", "explainability", "rationale"
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for s in signals:
        writer.writerow({
            "coin": s["coin"],
            "movement_type": s["movement_type"],
            "sources": ";".join(s["sources"]),
            "predicted_price": s["predicted_price"],
            "expected_time_window": s["expected_time_window"],
            "prediction_made_at": s["prediction_made_at"],
            "achieved": s["achieved"],
            "achieved_at": s["achieved_at"],
            "actual_max_price": s["actual_max_price"],
            "explainability": s["explainability"],
            "rationale": s["rationale"],
        })