# app/core/database.py

from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings


client = AsyncIOMotorClient(settings.mongodb_url)
database = client.get_database(settings.app_name)
