# Bu servis, eşik aşılırsa bildirim tetikler
def should_alert(signal, threshold_score=0.9, min_move=0.2):
    """
    signal: DetectedMovement veya PotentialOpportunity
    threshold_score: Skor eşiği (örn. %90)
    min_move: minimum hareket (örn. %20)
    """
    if signal.score >= threshold_score and (signal.max_potential_price or 0) / signal.current_price - 1 >= min_move:
        return True
    return False