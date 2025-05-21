from fastapi import APIRouter, HTTPException
from app.models.alarm import (
    add_alarm,
    get_alarms,
    delete_alarm,
    init_alarm_db,
)
from pydantic import BaseModel

router = APIRouter()

class AlarmRequest(BaseModel):
    symbol: str
    threshold: float
    direction: str  # "above" veya "below"

@router.on_event("startup")
def startup():
    init_alarm_db()

@router.post("/alarms", tags=["Alarm"])
def create_alarm(req: AlarmRequest):
    add_alarm(req.symbol, req.threshold, req.direction)
    return {"message": "Alarm kaydedildi."}

@router.get("/alarms", tags=["Alarm"])
def list_alarms():
    return {"alarms": get_alarms()}

@router.delete("/alarms/{alarm_id}", tags=["Alarm"])
def remove_alarm(alarm_id: int):
    delete_alarm(alarm_id)
    return {"message": "Alarm silindi."}