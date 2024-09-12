from pydantic import BaseModel, Field


class _CurrentTemperatureSchema(BaseModel):
    celsius: float = Field(..., description="Temperature in °C", examples=[18.2])
    fahrenheit: float = Field(..., description="Temperature in °F", examples=[64.7])


class _WindSpeedSchema(BaseModel):
    kph: float = Field(..., description="Wind speed in km/h", examples=[11.2])
    mph: float = Field(..., description="Wind speed in mph", examples=[6.8])


class TransformedCurrentWeatherSchema(BaseModel):
    location_name: str = Field(
        ..., description="Name of town or city", examples=["Boston"]
    )
    current_temperature: _CurrentTemperatureSchema
    wind_speed: _WindSpeedSchema
    description: str = Field(
        ..., description="Description of current weather", examples=["Partly cloudy"]
    )
