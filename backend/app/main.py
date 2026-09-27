from fastapi import FastAPI

from app.routers.auth import router as auth_router


app = FastAPI(
    title="AGAMOTTO API",
    description="Hackathon competition and judging engine",
    version="0.1.0",
)


app.include_router(auth_router)


@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "service": "agamotto-api",
    }
