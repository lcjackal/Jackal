from fastapi import Request, HTTPException
from collections import defaultdict
import time

rate_limit_dict = defaultdict(list)

def rate_limit(request: Request, max_per_minute: int = 10):
    ip = request.client.host
    now = time.time()
    rate_limit_dict[ip] = [t for t in rate_limit_dict[ip] if now - t < 60]
    if len(rate_limit_dict[ip]) >= max_per_minute:
        raise HTTPException(status_code=429, detail="Çok sık istek, lütfen bekleyin.")
    rate_limit_dict[ip].append(now)