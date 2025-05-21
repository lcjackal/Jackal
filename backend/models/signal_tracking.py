from pydantic import BaseModel
from typing import List, Optional

class SignalOutcome(BaseModel):
    coin: str
    movement_type: str
    sources: List[str]  # orderbook, rsi, etc.
    predicted_price: float
    expected_time_window: str  # e.g. "2 saat"
    prediction_made_at: str    # ISO datetime
    achieved: bool             # hedefe ulaşıldı mı?
    achieved_at: Optional[str] # gerçekleştiyse zamanı
    actual_max_price: Optional[float] # o periyotta görülen en yüksek fiyat
    explainability: str        # "RSI<30, whale alımı, buy wall"
    rationale: str             # kısa algoritmik açıklama