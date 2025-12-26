import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=os.getenv("CORS_ALLOWED_ORIGINS", "").split(","), 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from routes import api
app.include_router(api.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}