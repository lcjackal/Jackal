from app.analysis.technical import get_technical_indicators

@router.get("/analysis/technical/{symbol}", tags=["Analiz"])
async def technical_analysis(symbol: str):
    return await get_technical_indicators(symbol)