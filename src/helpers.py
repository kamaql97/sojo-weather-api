import requests

from src.models import OriginalApiRealTimeSchema, TransformedCurrentWeatherSchema
from settings import WEATHER_API_KEY


def get_current_weather_from_api(location: str) -> dict:
    """
    Get current weather conditions for a specific location
    :param location: US Zipcode, UK Postcode, Canada Postalcode, IP address, Lat/Long (decimal degree) or city name
    :raises: HTTPError if API request fails (e.g. location is invalid, request limit exceeded)
    :return: response JSON loaded as a dictionary
    """
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params={"key": WEATHER_API_KEY, "q": location},
    )
    response.raise_for_status()
    return response.json()


def validate_original_api_response(
    original_response: dict,
) -> OriginalApiRealTimeSchema:
    """
    Validate and transform original response and return as a Pydantic model
    :param original_response: WeatherAPI original response JSON loaded as a dictionary
    :raises: ValidationError if original response validation fails (e.g. missing required field)
    :return: OriginalApiRealTimeSchema
    """
    return OriginalApiRealTimeSchema.model_validate(original_response)


def transform_validated_original_response(
    original_realtime_data: OriginalApiRealTimeSchema,
) -> TransformedCurrentWeatherSchema:
    """
    Transform validated original response and return transformed response as a Pydantic model
    :param original_realtime_data: OriginalApiRealTimeSchema
    :return: TransformedCurrentWeatherSchema
    """
    return TransformedCurrentWeatherSchema(
        location_name=original_realtime_data.location.name,
        current_temperature={
            "celsius": original_realtime_data.current.temp_c,
            "fahrenheit": original_realtime_data.current.temp_f,
        },
        wind_speed={
            "kph": original_realtime_data.current.wind_kph,
            "mph": original_realtime_data.current.wind_kph,
        },
        description=original_realtime_data.current.condition.text,
    )
