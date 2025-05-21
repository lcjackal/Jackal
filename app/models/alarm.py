import sqlite3
import os

DB_PATH = os.getenv("ALARM_DB_PATH", "alarms.db")

def init_alarm_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS alarms (id INTEGER PRIMARY KEY AUTOINCREMENT, symbol TEXT, threshold REAL, direction TEXT, notified INTEGER DEFAULT 0)"
    )
    conn.commit()
    conn.close()

def add_alarm(symbol: str, threshold: float, direction: str):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO alarms (symbol, threshold, direction, notified) VALUES (?, ?, ?, 0)",
        (symbol, threshold, direction),
    )
    conn.commit()
    conn.close()

def get_alarms():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, symbol, threshold, direction, notified FROM alarms")
    alarms = c.fetchall()
    conn.close()
    return [
        {"id": a[0], "symbol": a[1], "threshold": a[2], "direction": a[3], "notified": bool(a[4])}
        for a in alarms
    ]

def mark_alarm_notified(alarm_id: int):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE alarms SET notified=1 WHERE id=?", (alarm_id,))
    conn.commit()
    conn.close()

def delete_alarm(alarm_id: int):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM alarms WHERE id=?", (alarm_id,))
    conn.commit()
    conn.close()