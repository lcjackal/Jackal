import json
import os

PORTFOLIO_PATH = os.getenv("PORTFOLIO_PATH", "portfolio.json")

def load_portfolio():
    if not os.path.exists(PORTFOLIO_PATH):
        return {}
    with open(PORTFOLIO_PATH, "r") as f:
        return json.load(f)

def save_portfolio(data):
    with open(PORTFOLIO_PATH, "w") as f:
        json.dump(data, f, indent=2)

def add_to_portfolio(symbol: str, amount: float):
    data = load_portfolio()
    data[symbol.lower()] = data.get(symbol.lower(), 0) + amount
    save_portfolio(data)

def remove_from_portfolio(symbol: str):
    data = load_portfolio()
    if symbol.lower() in data:
        del data[symbol.lower()]
        save_portfolio(data)

def get_portfolio():
    return load_portfolio()