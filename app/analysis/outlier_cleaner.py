def clean_outliers(coins):
    # Fiyat veya değişim yüzdesi çok absürt olanları ayıkla
    filtered = []
    for c in coins:
        price = c.get("price") or c.get("current_price") or 0
        change = c.get("change_24h") or c.get("price_change_percentage_24h") or 0
        if price <= 0 or price > 1e7:  # ör: 10 milyon USD üzeri mantıksız fiyat!
            continue
        if abs(change) > 95:  # %95'ten fazla günlük değişim istisnai durum
            continue
        filtered.append(c)
    return filtered