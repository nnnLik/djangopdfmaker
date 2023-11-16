from typing import List

from pydantic_settings import BaseSettings


class BaseApplicationSettings(BaseSettings):
    class Config:
        env_file = ".env"


class ServerSettings(BaseApplicationSettings):
    SECRET_KEY: str
    DEBUG: bool
    ALLOWED_HOSTS: List[str] = ["*"]


class DatabaseSettings(BaseApplicationSettings):
    DB_ENGINE: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int


class Settings(ServerSettings, DatabaseSettings):
    server: ServerSettings = ServerSettings()
    database: DatabaseSettings = DatabaseSettings()


settings: Settings = Settings()
