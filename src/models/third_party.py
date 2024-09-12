from pydantic import BaseModel, Field


class _LocationSchema(BaseModel):
    name: str = Field(..., description="Name of town or city", examples=["Boston"])


class _ConditionSchema(BaseModel):
    text: str = Field(
        ..., description="Description of current weather", examples=["Partly cloudy"]
    )


class _CurrentSchema(BaseModel):
    temp_c: float = Field(..., description="Temperature in °C", examples=[18.2])
    temp_f: float = Field(..., description="Temperature in °F", examples=[64.7])
    wind_kph: float = Field(..., description="Wind speed in km/h", examples=[11.2])
    wind_mph: float = Field(..., description="Wind speed in mph", examples=[6.8])
    humidity: int = Field(..., description="Percentage air humidity", examples=[87])
    condition: _ConditionSchema


class OriginalApiRealTimeSchema(BaseModel):
    location: _LocationSchema
    current: _CurrentSchema
