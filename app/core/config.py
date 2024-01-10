# app/core/config.py

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "MyApp"
    mongodb_url: str = "mongodb://localhost:27017"
    secret_key: str = "mysecretkey"

    class Config:
        env_file = ".env"


settings = Settings()
