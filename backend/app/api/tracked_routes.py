from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.tracked_coins import load_tracked, add_tracked, remove_tracked

router = APIRouter()

class TrackIn(BaseModel):
    symbol: str

@router.get("/tracked", tags=["Tracking"])
def get_tracked():
    return {"tracked": load_tracked()}

@router.post("/tracked", tags=["Tracking"])
def add_track(track: TrackIn):
    ok = add_tracked(track.symbol)
    if not ok:
        raise HTTPException(status_code=400, detail="Takip limiti aşıldı.")
    return {"status": "ok"}

@router.delete("/tracked/{symbol}", tags=["Tracking"])
def remove_track(symbol: str):
    remove_tracked(symbol)
    return {"status": "ok"}