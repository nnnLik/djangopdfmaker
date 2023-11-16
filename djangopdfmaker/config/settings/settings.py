from typing import List

from pydantic_settings import BaseSettings


class BaseApplicationSettings(BaseSettings):
    class Config:
        env_file = ".env"


class ServerSettings(BaseApplicationSettings):
    SECRET_KEY: str
    DEBUG: bool
    ALLOWED_HOSTS: List[str] = ["*"]


class CelerySettings(BaseApplicationSettings):
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str


class DatabaseSettings(BaseApplicationSettings):
    DB_ENGINE: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int


class Settings:
    server: ServerSettings = ServerSettings()
    database: DatabaseSettings = DatabaseSettings()
    celery: CelerySettings = CelerySettings()


settings: Settings = Settings()
