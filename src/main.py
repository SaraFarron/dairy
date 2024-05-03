from __future__ import annotations

from fastapi import FastAPI

from src.router import router

app = FastAPI()


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    """Healthcheck endpoint."""
    return {"status": "ok"}


app.include_router(router)
