from typing import Any

from pymongo import MongoClient
from pydantic import BaseSettings


class Config(BaseSettings):
    CORS_ORIGINS: list[str] = ["*"]
    CORS_HEADERS: list[str] = ["*"]
    CORS_METHODS: list[str] = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]

    MONGOHOST: str = "localhost"
    MONGOPORT: str = "27017"
    MONGOUSER: str = "root"
    MONGOPASSWORD: str = "password"
    MONGODATABASE: str = "fastapi"
    MONGO_URL: str = ""


# environmental variables
env = Config()

# FastAPI configurations
fastapi_config: dict[str, Any] = {
    "title": "API",
}

mongo_url = (
    f"mongodb://{env.MONGOUSER}:{env.MONGOPASSWORD}@{env.MONGOHOST}:{env.MONGOPORT}/"
)
if env.MONGO_URL:
    mongo_url = env.MONGO_URL

# MongoDB connection
client = MongoClient(mongo_url)

# MongoDB database
database = client[env.MONGODATABASE]
