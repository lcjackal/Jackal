import sqlite3, time

def init_price_db():
    conn = sqlite3.connect("price_history.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS price_history (
        coin TEXT,
        timestamp INTEGER,
        price REAL
    )
    """)
    conn.commit()
    conn.close()

def save_price(coin, price, timestamp=None):
    timestamp = timestamp or int(time.time())
    conn = sqlite3.connect("price_history.db")
    c = conn.cursor()
    c.execute("INSERT INTO price_history (coin, timestamp, price) VALUES (?, ?, ?)", (coin, timestamp, price))
    conn.commit()
    conn.close()

def get_price_history(coin, window=48*3600):
    now = int(time.time())
    conn = sqlite3.connect("price_history.db")
    c = conn.cursor()
    c.execute("SELECT timestamp, price FROM price_history WHERE coin=? AND timestamp>? ORDER BY timestamp",
              (coin, now - window))
    result = [{"time": row[0], "price": row[1]} for row in c.fetchall()]
    conn.close()
    return result