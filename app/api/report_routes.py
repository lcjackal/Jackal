from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import csv
from app.models.portfolio import get_portfolio
from app.services.aggregator import get_coins_with_fallback
from io import StringIO

router = APIRouter()

@router.get("/report/portfolio_csv", tags=["Rapor"])
async def download_portfolio_csv():
    port = get_portfolio()
    coin_data = await get_coins_with_fallback()
    prices = {c["symbol"]: c.get("price") or c.get("current_price") for c in coin_data["data"]}
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["Coin", "Miktar", "Fiyat", "Değer"])
    for sym, amt in port.items():
        val = amt * prices.get(sym, 0)
        writer.writerow([sym, amt, prices.get(sym, 0), val])
    output.seek(0)
    return StreamingResponse(output, headers={"Content-Disposition": "attachment;filename=portfolio.csv"}, media_type="text/csv")