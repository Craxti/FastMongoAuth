# app/api/endpoints/items.py

from fastapi import APIRouter, Depends
from app.models.schemas import Item
from app.core.database import database

router = APIRouter()


@router.post("/items/")
async def create_item(item: Item):
    inserted_item = await database.items.insert_one(item.dict())
    return {"message": "Item created successfully", "item_id": str(inserted_item.inserted_id)}
