from app.models.prediction import Prediction, SessionLocal
from app.services.aggregator import get_coin_price
from datetime import datetime, timedelta
import time

# Bu fonksiyon bir Celery taskı veya basit bir arka plan thread'i olarak çalıştırılabilir
def validate_predictions():
    db = SessionLocal()
    now = datetime.utcnow()
    # Hedef zamanı geçmiş ve henüz doğrulanmamış tahminler
    preds = db.query(Prediction).filter(
        Prediction.status == "pending",
        Prediction.target_time <= now
    ).all()
    for pred in preds:
        actual = get_coin_price(pred.coin)
        if actual is None:
            continue  # API sorununda tekrar denenir
        abs_err = abs(pred.predicted_price - actual)
        rel_err = abs_err / actual if actual else 0
        # Basit başarı kriteri: %10'dan küçükse "hit", büyükse "miss"
        outcome = "hit" if rel_err < 0.10 else "miss"
        feedback = ""
        if outcome == "miss":
            if abs(actual - pred.source_data.get("websocket_price", actual)) > abs_err:
                feedback = "Websocket verisi ile büyük sapma."
            elif abs(actual - pred.source_data.get("scraped_price", actual)) > abs_err:
                feedback = "Scraping verisi ile büyük sapma."
            else:
                feedback = "Tahmin modeli güncellenmeli."
        pred.status = "validated"
        pred.actual_price = actual
        pred.absolute_error = abs_err
        pred.relative_error = rel_err
        pred.outcome = outcome
        pred.feedback = feedback
        db.commit()
    db.close()

# Kendi kendine düzenli aralıklarla çalışacak şekilde (örn. Celery beat, threading.Timer, cron, vs.)