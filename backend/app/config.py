import os
from dotenv import load_dotenv

load_dotenv()

API_KEYS = {
    "coinmarketcap": os.getenv("COINMARKETCAP_API_KEY"),
    "coingecko": os.getenv("COINGECKO_API_KEY"),
    "messari": os.getenv("MESSARI_API_KEY"),
    "cryptocompare": os.getenv("CRYPTOCOMPARE_API_KEY"),
    "lunarcrush": os.getenv("LUNARCRUSH_API_KEY"),
    "defillama": os.getenv("DEFILLAMA_API_KEY"),
    "etherscan": os.getenv("ETHERSCAN_API_KEY"),
    "bscscan": os.getenv("BSCSCAN_API_KEY"),
    "solscan": os.getenv("SOLSCAN_API_KEY"),
    # Ek kaynaklar eklenebilir
}

# Sağlayıcı önceliği ayarlanabilir (kullanıcı ayarından da gelebilir)
PROVIDER_PRIORITY = [
    "coinmarketcap",
    "messari",
    "coingecko",
    "cryptocompare",
    "lunarcrush",
    "defillama",
    "etherscan",
    "bscscan",
    "solscan",
    # ...
]