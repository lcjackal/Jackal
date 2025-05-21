import pytest
from httpx import AsyncClient
from app.main import app
import os

@pytest.mark.asyncio
async def test_coins_api_key_success(monkeypatch):
    # Doğru API anahtarıyla gerçek veri alınabiliyor mu?
    monkeypatch.setenv("COINMARKETCAP_API_KEY", "doğru_key")  # Gerçek anahtar olmalı
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/coins")
    assert resp.status_code == 200
    data = resp.json()
    assert "provider" in data
    assert data["service_status"]["active"] is True
    assert "notification" in data

@pytest.mark.asyncio
async def test_coins_api_key_failure(monkeypatch):
    # Hatalı API anahtarıyla uygun hata ve öneri dönüyor mu?
    monkeypatch.setenv("COINMARKETCAP_API_KEY", "")
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/coins")
    assert resp.status_code == 500
    data = resp.json()
    assert "notification" in data["detail"]
    assert "API anahtarınızı ve bağlantınızı kontrol edin" in data["detail"]["notification"]

@pytest.mark.asyncio
async def test_settings_api_key_update():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/settings/provider", json={
            "provider": "coinmarketcap",
            "api_key": "testkey123"
        })
    assert resp.status_code == 200
    assert resp.json()["notification"] == "API anahtarı ve ayar güncellemesi başarılı."