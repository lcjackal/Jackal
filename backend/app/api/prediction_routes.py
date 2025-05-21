from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.prediction import Prediction, SessionLocal
from datetime import datetime, timedelta

router = APIRouter()

class PredictionIn(BaseModel):
    coin: str
    predicted_price: float
    prediction_time: datetime
    target_time: datetime
    method: str  # "websocket", "scraping", "api", "ensemble"
    source_data: dict

@router.post("/prediction", tags=["Prediction"])
def log_prediction(pred: PredictionIn):
    db = SessionLocal()
    p = Prediction(
        coin=pred.coin,
        predicted_price=pred.predicted_price,
        prediction_time=pred.prediction_time,
        target_time=pred.target_time,
        method=pred.method,
        source_data=pred.source_data,
        status="pending"
    )
    db.add(p)
    db.commit()
    db.refresh(p)
    db.close()
    return {"id": p.id, "message": "Tahmin kaydedildi."}

@router.get("/prediction/pending", tags=["Prediction"])
def list_pending_predictions():
    db = SessionLocal()
    preds = db.query(Prediction).filter(Prediction.status == "pending").all()
    db.close()
    return preds

@router.get("/prediction/results", tags=["Prediction"])
def list_validated_predictions():
    db = SessionLocal()
    preds = db.query(Prediction).filter(Prediction.status == "validated").all()
    db.close()
    return preds

@router.get("/prediction/summary", tags=["Prediction"])
def prediction_summary():
    db = SessionLocal()
    total = db.query(Prediction).count()
    validated = db.query(Prediction).filter(Prediction.status == "validated").count()
    hits = db.query(Prediction).filter(Prediction.outcome == "hit").count()
    misses = db.query(Prediction).filter(Prediction.outcome == "miss").count()
    avg_abs_err = db.query(func.avg(Prediction.absolute_error)).filter(Prediction.absolute_error != None).scalar() or 0.0
    avg_rel_err = db.query(func.avg(Prediction.relative_error)).filter(Prediction.relative_error != None).scalar() or 0.0
    db.close()
    return {
        "total": total,
        "validated": validated,
        "hit": hits,
        "miss": misses,
        "avg_abs_err": avg_abs_err,
        "avg_rel_err": avg_rel_err
    }