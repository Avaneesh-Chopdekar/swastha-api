import os
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


async def connect_to_database():
    # Beanie uses Motor async client under the hood
    client = AsyncIOMotorClient(os.getenv("DB_URI"))

    # Initialize beanie
    await init_beanie(database=client.db_name, document_models=[])
