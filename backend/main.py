from fastapi import FastAPI
from backend.api import router

app = FastAPI(
    title="FlyVisRL API",
    description="Train vision-based fruit fly agents via HTTP",
    version="0.1.0"
)

app.include_router(router)