from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="ANR Tiffins AI")

app.include_router(router)