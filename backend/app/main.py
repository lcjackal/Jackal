from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Pump&Dump Analysis API",
    description="Kripto analiz platformu için güvenli backend servisleri.",
    version="1.0.0"
)

app.include_router(router)