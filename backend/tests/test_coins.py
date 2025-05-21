import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_coins_success():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/coins")
    assert resp.status_code == 200
    data = resp.json()
    assert "provider" in data
    assert "service_status" in data
    assert "data" in data
    assert "notification" in data

@pytest.mark.asyncio
async def test_coins_failure(monkeypatch):
    # API anahtarlarını silerek veya bozuk bir provider ile testi zorla başarısız yap
    monkeypatch.setenv("COINMARKETCAP_API_KEY", "")
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/coins")
    assert resp.status_code == 500
    error = resp.json()
    assert "notification" in error["detail"]
    assert error["detail"]["notification"].startswith("Veri alınamadı")