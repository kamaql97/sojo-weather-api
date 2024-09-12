from multiprocessing import freeze_support

from fastapi import FastAPI
from hypercorn.config import Config
from hypercorn.run import run

from src.routers import current_weather, health_check
from settings import ApiServerSettings

app = FastAPI()
app.include_router(health_check.router)
app.include_router(current_weather.router)


def serve_api():
    """
    Spin up FastAPI application using hypercorn
    """
    server_settings = ApiServerSettings()

    asgi_app_config = Config()
    asgi_app_config.application_path = "main:app"
    asgi_app_config.bind = f"{server_settings.HOST}:{server_settings.PORT}"

    freeze_support()  # For Windows systems
    run(config=asgi_app_config)


if __name__ == "__main__":
    serve_api()
