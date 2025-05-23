import sqlite3
import os
import json
import time

DB_FILE = "opportunities.db"

def get_db():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    # Fırsatlar tablosu
    c.execute("""
    CREATE TABLE IF NOT EXISTS opportunities (
        id TEXT PRIMARY KEY,
        coin TEXT,
        initial_prediction TEXT,
        current_prediction TEXT,
        status TEXT,
        reason TEXT,
        first_detected REAL,
        last_update REAL,
        history TEXT
    )
    """)
    # Fiyat geçmişi tablosu
    c.execute("""
    CREATE TABLE IF NOT EXISTS price_history (
        coin TEXT,
        timestamp INTEGER,
        price REAL
    )
    """)
    # Coin izleme listesi
    c.execute("""
    CREATE TABLE IF NOT EXISTS watchlist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        coin TEXT UNIQUE,
        added_at REAL
    )
    """)
    # Kullanıcı ayarları tablosu
    c.execute("""
    CREATE TABLE IF NOT EXISTS user_settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)
    conn.commit()
    conn.close()

# --- Watchlist Fonksiyonları ---

def add_coin_to_watchlist(coin):
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO watchlist (coin, added_at) VALUES (?, ?)", (coin, time.time()))
    conn.commit()
    conn.close()

def remove_coin_from_watchlist(coin):
    conn = get_db()
    c = conn.cursor()
    c.execute("DELETE FROM watchlist WHERE coin=?", (coin,))
    conn.commit()
    conn.close()

def get_watchlist():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT coin FROM watchlist ORDER BY added_at")
    result = [row["coin"] for row in c.fetchall()]
    conn.close()
    return result

# --- User Settings Fonksiyonları ---

def save_setting(key, value):
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO user_settings (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

def load_setting(key, default=None):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT value FROM user_settings WHERE key=?", (key,))
    row = c.fetchone()
    conn.close()
    return row["value"] if row else default

# --- Opportunities Fonksiyonları ---

def save_opportunity(opportunity):
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO opportunities (
            id, coin, initial_prediction, current_prediction, status, reason,
            first_detected, last_update, history
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        opportunity.get("id"),
        opportunity.get("coin"),
        opportunity.get("initial_prediction"),
        opportunity.get("current_prediction"),
        opportunity.get("status"),
        opportunity.get("reason"),
        opportunity.get("first_detected"),
        opportunity.get("last_update"),
        json.dumps(opportunity.get("history", []))
    ))
    conn.commit()
    conn.close()

def load_opportunities():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM opportunities")
    rows = c.fetchall()
    conn.close()
    opportunities = []
    for row in rows:
        opp = dict(row)
        if "history" in opp and opp["history"]:
            try:
                opp["history"] = json.loads(opp["history"])
            except Exception:
                opp["history"] = []
        opportunities.append(opp)
    return opportunities