from fastapi import APIRouter, HTTPException, Body
from app.services.aggregator import get_coins_with_fallback
from app.services.status import get_service_status, SERVICE_INFO

router = APIRouter()

@router.get("/coins", tags=["Coins"])
async def list_coins():
    try:
        result = await get_coins_with_fallback()
        provider = result["provider"]
        service_status = get_service_status(provider)
        return {
            "provider": provider,
            "service_status": service_status,
            "data": result["data"],
            "notification": f"{provider} kaynağından veri çekildi. API anahtarı ve bağlantı başarılı."
        }
    except Exception as ex:
        all_status = {p: get_service_status(p) for p in SERVICE_INFO}
        raise HTTPException(status_code=500, detail={
            "error": str(ex),
            "notification": "Veri alınamadı, API anahtarınızı ve bağlantınızı kontrol edin.",
            "services": all_status
        })

@router.post("/settings/provider", tags=["Ayarlar"])
def update_provider_settings(
    provider: str = Body(...),
    api_key: str = Body(None),
    ws_url: str = Body(None)
):
    # .env/config dosyasına yazmak için geliştirilmiş bir yöntem önerilir!
    import os
    if api_key:
        os.environ[provider.upper() + "_API_KEY"] = api_key
    if ws_url:
        os.environ[provider.upper() + "_WS_URL"] = ws_url
    return {
        "message": f"{provider} ayarları güncellendi.",
        "api_key": bool(api_key),
        "ws_url": bool(ws_url),
        "notification": "API anahtarı ve ayar güncellemesi başarılı."
    }