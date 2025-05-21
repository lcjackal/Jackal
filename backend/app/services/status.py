SERVICE_INFO = {
    # ... diğer servisler
    "websocket_example": {
        "name": "WebSocket Borsası",
        "type": "WebSocket",
        "website": "https://example.com/docs/websocket",
        "needs_key": True,
        "needs_ws_url": True,
        "key_env": "EXAMPLE_WS_KEY",
        "ws_env": "EXAMPLE_WS_URL",
        "suggestion": "API/WebSocket anahtarınızı ve endpoint adresinizi girin. Alternatif olarak REST API kullanabilirsiniz."
    }
}

def get_service_status(service_name):
    import os
    info = SERVICE_INFO.get(service_name)
    if not info:
        return None
    status = {"active": True, **info}
    if info.get("needs_key") and not os.getenv(info["key_env"]):
        status["active"] = False
        status["reason"] = "API anahtarı eksik"
    if info.get("needs_ws_url") and not os.getenv(info["ws_env"]):
        status["active"] = False
        status["reason"] = "WebSocket adresi eksik"
    return status