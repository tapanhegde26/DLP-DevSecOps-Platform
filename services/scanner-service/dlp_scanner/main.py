from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from dlp_scanner.routes.scan import router as scan_router

app = FastAPI(
    title="Cloud-Native DLP Scanner"
)

app.include_router(scan_router)

Instrumentator().instrument(app).expose(app)


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
