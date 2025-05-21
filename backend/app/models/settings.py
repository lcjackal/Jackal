import json, os
from app.utils.crypto import encrypt, decrypt

SETTINGS_PATH = "settings.json"

DEFAULT_SETTINGS = {
    #...
    "exchanges_settings": {
        # borsa_adi: {mode, api_keys}
        "binance": {
            "mode": "public",  # "public" veya "full"
            "api_keys": {"key": "", "secret": ""}
        },
        "kucoin": {
            "mode": "public",
            "api_keys": {"key": "", "secret": ""}
        }
        # diğer borsalar...
    }
}

def load_settings():
    if not os.path.exists(SETTINGS_PATH):
        save_settings(DEFAULT_SETTINGS)
    with open(SETTINGS_PATH, "r") as f:
        data = json.load(f)
        # api anahtarlarını şifre çöz
        for ex, exdata in data.get("exchanges_settings", {}).items():
            for k in exdata.get("api_keys", {}):
                if exdata["api_keys"][k]:
                    try:
                        exdata["api_keys"][k] = decrypt(exdata["api_keys"][k])
                    except Exception:
                        exdata["api_keys"][k] = ""  # bozuksa sil
        return data

def save_settings(settings):
    # api anahtarlarını şifrele
    for ex, exdata in settings.get("exchanges_settings", {}).items():
        for k in exdata.get("api_keys", {}):
            if exdata["api_keys"][k]:
                exdata["api_keys"][k] = encrypt(exdata["api_keys"][k])
    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=2)