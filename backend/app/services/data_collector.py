import threading
def start_public_collector(exchange):
    # sadece public endpointlerle veri çek
    pass

def start_private_collector(exchange, api_key, api_secret):
    # private endpointlerle portföy, emir, alarm vs
    pass

def launch_exchange_service(exchange, mode, api_keys):
    stop_threads_for(exchange)  # var olan threadleri kapat
    threading.Thread(target=start_public_collector, args=(exchange,)).start()
    if mode == "full" and api_keys.get("key") and api_keys.get("secret"):
        threading.Thread(target=start_private_collector, args=(exchange, api_keys["key"], api_keys["secret"])).start()