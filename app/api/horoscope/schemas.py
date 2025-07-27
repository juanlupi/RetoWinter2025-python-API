from pydantic import BaseModel, validator
from datetime import datetime
import re


class HoroscopeRequest(BaseModel):
    name: str
    fecha_nacimiento: str  # Format: DD/MM/YYYY

    @validator('name')
    def name_not_empty(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty")
        return v.strip()

    @validator('fecha_nacimiento')
    def valid_date(cls, v):
        # Check format with regex first
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', v):
            raise ValueError("Date must be in DD/MM/YYYY format")

        # Validate the actual date
        try:
            day, month, year = map(int, v.split('/'))
            datetime(year=year, month=month, day=day)
        except ValueError:
            raise ValueError("Invalid date values")

        return v


class HoroscopeResponse(BaseModel):
    name: str
    birth_date: str
    zodiac_sign: str
    pokemon: dict

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Ash",
                "birth_date": "15/05/1990",
                "zodiac_sign": "taurus",
                "pokemon": {
                    "name": "tauros",
                    "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/128.png",
                    "types": ["normal"],
                    "height": 14,
                    "weight": 884,
                    "abilities": ["intimidate", "anger-point", "cud-chew"]
                }
            }
        }