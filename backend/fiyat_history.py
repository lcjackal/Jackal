import json, os, time

HISTORY_FILE = "coin_price_history.json"

def save_history(coin, price, timestamp=None):
    data = {}
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            data = json.load(f)
    timestamp = timestamp or int(time.time())
    if coin not in data:
        data[coin] = []
    data[coin].append({"time": timestamp, "price": price})
    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f)

def get_history(coin, window=48*3600):
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        data = json.load(f)
    now = int(time.time())
    return [x for x in data.get(coin, []) if now - x["time"] < window]