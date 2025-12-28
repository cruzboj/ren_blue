import os
from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv(find_dotenv())

app = FastAPI()

raw_origins = os.getenv("CORS_ALLOWED_ORIGINS", "NOT_FOUND_IN_ENV")

allowed_origins = [origin.strip() for origin in raw_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.routes import api

app.include_router(api.router)

@app.get("/")
def read_root():
    return {
        "status": "Check complete",
        # "looking_for_file": find_dotenv(),
        # "raw_value": raw_origins,
        # "list": allowed_origins
    }