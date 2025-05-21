from firsat_manager import detect_opportunities, refresh_opportunities, opportunity_pool, OpportunityStatus
import time

def test_opportunity_flow():
    # 1. Tespit (scan)
    scan_data = [{"coin": "zcoin", "prediction": "%500 artış 2 saat"}]
    detect_opportunities(scan_data)
    assert "zcoin-%500 artış 2 saat" in opportunity_pool

    # 2. Canlı veri ile güncelleme (satış baskısı)
    live_data = {"zcoin": {"sell_pressure": 0.7}}
    opps = refresh_opportunities(live_data)
    found = [o for o in opps if o.coin == "zcoin"][0]
    assert found.status == OpportunityStatus.CANCELLED

    # 3. Tekrar fırsat gelirse yeni entry
    scan_data2 = [{"coin": "zcoin", "prediction": "%100 artış 1 saat"}]
    detect_opportunities(scan_data2)
    assert "zcoin-%100 artış 1 saat" in opportunity_pool

    print("Tüm testler başarıyla geçti.")

if __name__ == "__main__":
    test_opportunity_flow()