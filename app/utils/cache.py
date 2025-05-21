import aioredis
import os
import json

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
CACHE_TTL = 30  # saniye

_redis = None

async def get_redis():
    global _redis
    if _redis is None:
        _redis = await aioredis.from_url(REDIS_URL, encoding="utf8", decode_responses=True)
    return _redis

async def cache_get(key: str):
    redis = await get_redis()
    val = await redis.get(key)
    if val:
        return json.loads(val)
    return None

async def cache_set(key: str, value, ttl=CACHE_TTL):
    redis = await get_redis()
    await redis.set(key, json.dumps(value), ex=ttl)