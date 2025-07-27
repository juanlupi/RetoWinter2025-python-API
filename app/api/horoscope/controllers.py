from typing import Dict
from app.services.zodiac_service import ZodiacService
from app.services.pokemon_service import PokemonService
from app.api.horoscope.schemas import HoroscopeRequest, HoroscopeResponse
from flask import abort
from datetime import datetime


class HoroscopeController:
    @staticmethod
    def format_date_for_display(date_str: str) -> str:
        """Convert from DD/MM/YYYY to YYYY-MM-DD for consistent display"""
        day, month, year = date_str.split('/')
        return f"{year}-{month}-{day}"

    @staticmethod
    def get_horoscope(request: HoroscopeRequest) -> HoroscopeResponse:
        try:
            # Get zodiac sign
            sign = ZodiacService.get_zodiac_sign(request.fecha_nacimiento)

            # Get associated Pokémon name
            pokemon_name = ZodiacService.get_pokemon_for_sign(sign)

            # Get Pokémon details from PokeAPI
            pokemon_data = PokemonService.get_pokemon_details(pokemon_name)

            return HoroscopeResponse(
                name=request.name,
                birth_date=request.fecha_nacimiento,  # Keep original DD/MM/YYYY format
                zodiac_sign=sign,
                pokemon=pokemon_data
            )

        except ValueError as e:
            raise abort(400, description=str(e))
        except Exception as e:
            raise abort(500, description="Internal server error")