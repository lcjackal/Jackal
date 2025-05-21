from fastapi import APIRouter, Query
from app.services.aggregator import get_coins_with_fallback

router = APIRouter()

@router.get("/filter/volume", tags=["Filtre"])
async def filter_by_volume(
    min_volume: float = Query(0, description="Minimum 24s işlem hacmi (USD)"),
    max_volume: float = Query(1e20, description="Maksimum 24s işlem hacmi (USD)"),
    sort: str = Query("desc", description="Sıralama: desc/asc"),
    limit: int = Query(20, description="En fazla gösterilecek coin sayısı")
):
    result = await get_coins_with_fallback()
    coins = result["data"]
    filtered = [c for c in coins if "volume_24h" in c and min_volume <= c["volume_24h"] <= max_volume]
    filtered.sort(key=lambda c: c["volume_24h"], reverse=(sort == "desc"))
    return {"coins": filtered[:limit]}

@router.get("/filter/liquidity", tags=["Filtre"])
async def filter_by_liquidity(
    min_liquidity: float = Query(0, description="Minimum likidite (USD, varsa)"),
    max_liquidity: float = Query(1e20, description="Maksimum likidite"),
    sort: str = Query("desc", description="Sıralama: desc/asc"),
    limit: int = Query(20, description="En fazla gösterilecek coin sayısı")
):
    result = await get_coins_with_fallback()
    coins = result["data"]
    filtered = [c for c in coins if "liquidity" in c and min_liquidity <= c["liquidity"] <= max_liquidity]
    filtered.sort(key=lambda c: c["liquidity"], reverse=(sort == "desc"))
    return {"coins": filtered[:limit]}