from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    """Healthcheck endpoint."""
    return {"status": "ok"}

