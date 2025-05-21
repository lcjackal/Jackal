from backend.db import init_db, add_coin_to_watchlist, get_watchlist, save_opportunity, load_opportunities
from backend.firsat_manager import Opportunity

def test_watchlist_and_opportunity():
    init_db()
    add_coin_to_watchlist("BTC")
    wl = get_watchlist()
    assert "BTC" in wl

    opp = Opportunity("BTC", "%200 artış 1 gün")
    save_opportunity(opp)
    loaded = load_opportunities()
    assert any(o["id"] == opp.id for o in loaded)
    print("Watchlist ve fırsat kaydı test edildi.")

# Daha fazla fonksiyon ve edge-case eklenebilir.