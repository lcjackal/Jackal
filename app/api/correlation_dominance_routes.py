from fastapi import APIRouter, Query
from app.analysis.correlation_dominance import correlation_matrix, market_dominance

router = APIRouter()

@router.get("/analysis/correlation", tags=["Analiz"])
async def correlation(symbols: str = Query(..., description="Virgülle ayrılmış coin sembolleri (örn: bitcoin,ethereum,solana)")):
    symbol_list = [s.strip().lower() for s in symbols.split(",") if s.strip()]
    return await correlation_matrix(symbol_list)

@router.get("/analysis/dominance", tags=["Analiz"])
async def dominance(symbols: str = Query(..., description="Virgülle ayrılmış coin sembolleri (örn: bitcoin,ethereum)")):
    symbol_list = [s.strip().lower() for s in symbols.split(",") if s.strip()]
    return await market_dominance(symbol_list)