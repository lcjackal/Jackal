from backend.db import init_db, save_opportunity, load_opportunities

def test_save_and_load():
    init_db()
    class Dummy: pass
    opp = Dummy()
    opp.id = "test-1"
    opp.coin = "zcoin"
    opp.initial_prediction = "yükseliş"
    opp.current_prediction = "yükseliş"
    opp.status = "aktif"
    opp.reason = "test"
    opp.first_detected = 1
    opp.last_update = 1
    opp.history = [{"time": 1, "status": "aktif", "prediction": "yükseliş", "reason": "test"}]
    save_opportunity(opp)
    loaded = load_opportunities()
    assert any(o["id"] == "test-1" for o in loaded)