import os
from typing import Final, List
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from motor.motor_asyncio import AsyncIOMotorClient
from databases import DatabaseURL

load_dotenv(".env")


base_path: Final[str] = "/api/v1"
MONGODB_URL = os.getenv("MONGODB_URL", "")

if not MONGODB_URL:
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_PORT = os.getenv("MONGO_PORT")
    MONGO_DB = os.getenv("MONGO_DB")
    print(MONGO_HOST)
    MONGODB_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"


app = FastAPI(
    title="FastAPI",
    root_path=base_path,
    openapi_url=None,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
