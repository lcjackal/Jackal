from fastapi import APIRouter
from pydantic import BaseModel
from app.models.portfolio import add_to_portfolio, remove_from_portfolio, get_portfolio
from app.services.aggregator import get_coins_with_fallback

router = APIRouter()

class PortfolioItem(BaseModel):
    symbol: str
    amount: float

@router.post("/portfolio", tags=["Portföy"])
def add_portfolio(item: PortfolioItem):
    add_to_portfolio(item.symbol, item.amount)
    return {"message": "Portföye eklendi."}

@router.delete("/portfolio/{symbol}", tags=["Portföy"])
def remove_portfolio(symbol: str):
    remove_from_portfolio(symbol)
    return {"message": "Portföyden kaldırıldı."}

@router.get("/portfolio", tags=["Portföy"])
async def get_portfolio_summary():
    port = get_portfolio()
    coin_data = await get_coins_with_fallback()
    prices = {c["symbol"]: c.get("price") or c.get("current_price") for c in coin_data["data"]}
    summary = []
    total = 0
    for sym, amt in port.items():
        val = amt * prices.get(sym, 0)
        summary.append({"symbol": sym, "amount": amt, "price": prices.get(sym, 0), "value": val})
        total += val
    return {"portfolio": summary, "total_value": total}