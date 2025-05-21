from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app, include_in_schema=False, should_gzip=True)

# ... diğer router eklemeleri