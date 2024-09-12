import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


class ApiServerSettings(BaseSettings):
    HOST: str
    PORT: int

    model_config = SettingsConfigDict(env_prefix="API_SERVER_")
