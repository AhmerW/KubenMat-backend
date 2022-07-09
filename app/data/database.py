from motor.motor_asyncio import AsyncIOMotorClient
from app import globals


class DatabaseClient(AsyncIOMotorClient):
    ...


class Database:
    client: DatabaseClient = None


async def connect_db():
    Database.client = DatabaseClient(
        globals.MONGODB_URL,
        maxPoolSize=10,
        minPoolSize=10,
    )


async def close_db():
    Database.client.close()
    Database.client = None


def get_client() -> DatabaseClient:
    return Database.client.app


def get_collection(name: str) -> DatabaseClient:
    client = get_client()
    return getattr(client, name)
