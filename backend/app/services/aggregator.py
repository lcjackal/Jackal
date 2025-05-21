from app.providers.lunarcrush import LunarCrushProvider
from app.providers.defillama import DefiLlamaProvider
from app.providers.etherscan import EtherscanProvider
from app.providers.bscscan import BscScanProvider
from app.providers.solscan import SolscanProvider

# ... diğer importlar

PROVIDER_MAP = {
    # ... diğer providerlar
    "lunarcrush": LunarCrushProvider,
    "defillama": DefiLlamaProvider,
    "etherscan": EtherscanProvider,
    "bscscan": BscScanProvider,
    "solscan": SolscanProvider,
}

def get_coins_with_fallback(*args, **kwargs):
    # Dummy implementation - replace with real logic later
    return []