import os
from functools import lru_cache
from enum import Enum
from pydantic_settings import BaseSettings


class Environment(Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


class Settings(BaseSettings):

    OPENAI_API_KEY: str
    
    FAST_LLM_MODEL: str
    SMART_LLM_MODEL: str
    AMADEUS_API_KEY: str
    AMADEUS_API_SECRET: str
    
    # Optional settings
    ENVIRONMENT: str = Environment.PRODUCTION.value
    ORIGINS: list[str] = ["*"]


@lru_cache
def get_settings():
    return Settings()
