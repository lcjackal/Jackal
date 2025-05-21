from fastapi import APIRouter, Request
from backend.firsat_manager import detect_opportunities, refresh_opportunities
from backend.db import load_opportunities, load_opportunity_archive, get_price_history

router = APIRouter()

@router.post("/api/opportunity-scan")
async def opportunity_scan(request: Request):
    body = await request.json()
    scan_data = body.get("scan_data", [])
    opportunities = detect_opportunities(scan_data)
    return {"opportunities": [opp.to_dict() for opp in opportunities]}

@router.post("/api/opportunity-refresh")
async def opportunity_refresh(request: Request):
    body = await request.json()
    live_data = body.get("live_data", {})
    updated_opps = refresh_opportunities(live_data)
    return {"opportunities": [opp.to_dict() for opp in updated_opps]}

@router.get("/api/opportunity-archive")
async def opportunity_archive():
    archive = load_opportunity_archive()
    return {"opportunities": archive}

@router.get("/api/price-history/{coin}")
async def price_history(coin: str):
    return {"history": get_price_history(coin)}