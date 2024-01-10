# app/main.py

from fastapi import FastAPI
from app.api.endpoints import items, users
from app.core.config import settings

app = FastAPI(title=settings.app_name)

# Подключение роутеров
app.include_router(items.router, prefix="/api")
app.include_router(users.router, prefix="/api")
