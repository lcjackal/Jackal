from fastapi import APIRouter
from backend.models.detected_movement import DetectedMovement
from backend.models.potential_opportunity import PotentialOpportunity

router = APIRouter()

# Mock veri ile örnek endpointler
@router.get("/detected-movements", response_model=list[DetectedMovement])
def get_detected_movements():
    # Burada gerçek analiz fonksiyonu çağrılır.
    return [
        DetectedMovement(
            coin="BTC",
            movement_type="rsi_cross",
            sources=[{"type": "rsi", "detail": "RSI<30"}],
            detected_at="2025-05-21T06:00:00Z",
            score=0.92,
            max_potential_price=72000,
            expected_time_window="2 saat",
            notes="RSI, zincir üstü ve hacim desteğiyle"
        ),
        DetectedMovement(
            coin="ETH",
            movement_type="orderbook_wall",
            sources=[{"type": "orderbook", "detail": "Buy wall 1000 ETH"}, {"type": "volume"}],
            detected_at="2025-05-21T06:05:00Z",
            score=0.87,
            max_potential_price=4000,
            expected_time_window="1-3 saat",
            notes="Orderbook ve hacim birlikte"
        ),
    ]

@router.get("/potential-opportunities", response_model=list[PotentialOpportunity])
def get_potential_opportunities():
    # Algoritmanın çıkardığı fırsatlar
    return [
        PotentialOpportunity(
            coin="BTC",
            sources=["rsi", "onchain", "volume"],
            price_target=72000,
            expected_time="2 saat içinde",
            score=0.95,
            rationale="RSI ve zincir üstü whale birikimi"
        ),
        PotentialOpportunity(
            coin="ETH",
            sources=["orderbook", "volume"],
            price_target=4000,
            expected_time="1-3 saat",
            score=0.9,
            rationale="Orderbook buy wall ve yüksek alım hacmi"
        )
    ]