import time
import uuid
import json
from backend.db import save_opportunity, load_opportunities

class OpportunityStatus:
    ACTIVE = "aktif"
    UPDATED = "güncellendi"
    CANCELLED = "iptal"
    COMPLETED = "gerçekleşti"

class Opportunity:
    def __init__(self, coin, initial_prediction, reason=None, id=None, first_detected=None, status=None, last_update=None, current_prediction=None, history=None):
        self.id = id or f"{coin}-{uuid.uuid4().hex[:8]}"
        self.coin = coin
        self.first_detected = first_detected or time.time()
        self.status = status or OpportunityStatus.ACTIVE
        self.last_update = last_update or self.first_detected
        self.initial_prediction = initial_prediction
        self.current_prediction = current_prediction or initial_prediction
        self.reason = reason or "İlk tespit"
        self.history = history or [{
            "time": self.first_detected,
            "status": self.status,
            "prediction": self.initial_prediction,
            "reason": self.reason
        }]

    def update(self, new_prediction, new_status, reason):
        self.status = new_status
        self.last_update = time.time()
        self.current_prediction = new_prediction
        self.reason = reason
        self.history.append({
            "time": self.last_update,
            "status": self.status,
            "prediction": new_prediction,
            "reason": reason
        })

    def to_dict(self):
        return {
            "id": self.id,
            "coin": self.coin,
            "initial_prediction": self.initial_prediction,
            "current_prediction": self.current_prediction,
            "status": self.status,
            "reason": self.reason,
            "first_detected": self.first_detected,
            "last_update": self.last_update,
            "history": self.history
        }

    @staticmethod
    def from_dict(d):
        return Opportunity(
            coin=d["coin"],
            initial_prediction=d["initial_prediction"],
            reason=d.get("reason"),
            id=d.get("id"),
            first_detected=d.get("first_detected"),
            status=d.get("status"),
            last_update=d.get("last_update"),
            current_prediction=d.get("current_prediction"),
            history=d.get("history")
        )

def detect_opportunities(scan_data):
    # Aktif fırsatlar
    current = {o["id"]: Opportunity.from_dict(o) for o in load_opportunities()}
    for result in scan_data:
        coin = result["coin"]
        pred = result["prediction"]
        key = f"{coin}-{pred}"
        if not any(o.coin == coin and o.initial_prediction == pred for o in current.values()):
            opp = Opportunity(coin, pred)
            current[opp.id] = opp
            save_opportunity(opp)
    return [o for o in current.values()]

def refresh_opportunities(live_data):
    current = {o["id"]: Opportunity.from_dict(o) for o in load_opportunities()}
    for opp in current.values():
        coin_data = live_data.get(opp.coin)
        if not coin_data:
            continue
        if coin_data.get("sell_pressure", 0) > 0.5:
            opp.update(opp.current_prediction, OpportunityStatus.CANCELLED, "Aşırı satış baskısı")
        elif coin_data.get("current_price", 0) >= coin_data.get("target_price", 999999):
            opp.update(opp.current_prediction, OpportunityStatus.COMPLETED, "Hedef fiyat gerçekleşti")
        elif coin_data.get("new_prediction") and coin_data.get("new_prediction") != opp.current_prediction:
            opp.update(coin_data["new_prediction"], OpportunityStatus.UPDATED, "Tahmin güncellendi")
        save_opportunity(opp)
    return [o for o in current.values()]