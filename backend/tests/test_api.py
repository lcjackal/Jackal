import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    r = client.get("/")
    assert r.status_code == 200

def test_alarm_add_and_list():
    r = client.post("/alarms", json={"symbol": "bitcoin", "threshold": 50000, "direction": "above"})
    assert r.status_code == 200
    r2 = client.get("/alarms")
    assert r2.status_code == 200
    data = r2.json()
    assert any(a["symbol"] == "bitcoin" for a in data["alarms"])

def test_portfolio_add_and_get():
    r = client.post("/portfolio", json={"symbol": "ethereum", "amount": 1.5})
    assert r.status_code == 200
    r2 = client.get("/portfolio")
    assert r2.status_code == 200
    data = r2.json()
    assert any(p["symbol"] == "ethereum" for p in data["portfolio"])