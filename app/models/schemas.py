# app/models/schemas.py

from pydantic import BaseModel
from typing import Optional


class Item(BaseModel):
    name: str
    description: Optional[str] = None


class User(BaseModel):
    username: str
    email: str


class UserInDB(User):
    hashed_password: str
