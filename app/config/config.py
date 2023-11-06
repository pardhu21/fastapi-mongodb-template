import os
from typing import Optional, cast

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    PORT: int = cast(int, os.getenv("PORT", 8000))
    API_KEY: str = cast(str, os.getenv("API_KEY"))
    ALLOWED_ORIGINS_REGISTRY: Optional[str] = cast(
        str, os.getenv("ALLOWED_ORIGINS_REGISTRY", False)
    )
    MONGODB_URI: str = cast(str, os.getenv("MONGODB_URI"))
    MONGODB_DATABASE: str = cast(str, os.getenv("MONGODB_DATABASE"))

    class Config:
        case_sensitive = False


def get_allowed_origins(config: Config) -> list:
    origins = ["*"]
    if config.ALLOWED_ORIGINS_REGISTRY:
        with open(config.ALLOWED_ORIGINS_REGISTRY, "r") as origins_file:
            origins = []
            for line in origins_file:
                origins.append(line.strip())

    return origins


config = Config()
