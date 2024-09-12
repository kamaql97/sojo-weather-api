import logging
from http import HTTPStatus

from fastapi import APIRouter, HTTPException, Query
from pydantic import ValidationError
from requests import HTTPError

from src.models import TransformedCurrentWeatherSchema as CurrentWeatherSchema

from src.helpers import (
    get_current_weather_from_api,
    validate_original_api_response,
    transform_validated_original_response,
)

router = APIRouter()


@router.get(
    "/weather",
    response_model=CurrentWeatherSchema,
    tags=["Current Weather"],
)
def get_current_weather(
    city: str = Query(
        ...,
        description="US Zipcode, UK Postcode, Canada Postalcode, IP address, Lat/Long (decimal degree) or city name",
    )
):
    """
    Get current weather conditions for a specific location
    """
    try:
        original_response = get_current_weather_from_api(city)
    except HTTPError as exc:

        error_message = (
            exc.response.json().get("error", {}).get("message", "Unknown error")
        )
        logging.error(
            "Could not get current weather for location = %s - error = %s - status_code = %s",
            city,
            error_message,
            exc.response.status_code,
        )
        raise HTTPException(status_code=exc.response.status_code, detail=error_message)

    try:
        validated_realtime_data = validate_original_api_response(original_response)
    except ValidationError as exc:
        logging.error(
            "Got an invalid response from WeatherAPI for location = %s - original response = %s - errors = %d",
            city,
            original_response,
            exc.error_count(),
        )
        raise HTTPException(
            status_code=HTTPStatus.FAILED_DEPENDENCY,
            detail="Third party API returned an invalid response",
        )

    return transform_validated_original_response(validated_realtime_data)
