from typing import Optional

from pydantic import BaseModel, field_validator


class CEPv1(BaseModel):
    cep: str
    state: str
    city: str
    neighborhood: Optional[str]
    street: Optional[str]
    service: str


class Coordinate(BaseModel):
    latitude: float
    longitude: float


class CEPLocation(BaseModel):
    type: str
    coordinates: Optional[Coordinate]

    @field_validator("coordinates", mode="before")
    @classmethod
    def handle_empty_dict(cls, v: dict) -> str:
        if v == {}:
            return None
        return v


class CEP(CEPv1):
    location: CEPLocation
