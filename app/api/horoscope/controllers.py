from typing import Dict
from app.services.zodiac_service import ZodiacService
from app.services.pokemon_service import PokemonService
from app.api.horoscope.schemas import HoroscopeRequest, HoroscopeResponse
from flask import abort
from datetime import datetime


class HoroscopeController:
    @staticmethod
    def format_date_for_display(date_str: str) -> str:
        """
        Convert date string from DD/MM/YYYY format to YYYY-MM-DD format.
        Args:
            date_str (str): Date string in DD/MM/YYYY format
        Returns:
            str: Date string in YYYY-MM-DD format
        """
        day, month, year = date_str.split('/')
        return f"{year}-{month}-{day}"

    @staticmethod
    def get_horoscope(request: HoroscopeRequest) -> HoroscopeResponse:
        """
        Get Pokémon horoscope based on birth date with full error handling.
        Args:
            request (HoroscopeRequest): Validated request containing:
                - name (str): User's name
                - fecha_nacimiento (str): Birth date in DD/MM/YYYY format
        Returns:
            HoroscopeResponse: Contains:
                - name (str): User's name
                - birth_date (str): Original DD/MM/YYYY format
                - zodiac_sign (str): Calculated zodiac sign
                - pokemon (dict): Complete Pokémon details
        """
        try:
            sign = ZodiacService.get_zodiac_sign(request.fecha_nacimiento)

            pokemon_name = ZodiacService.get_pokemon_for_sign(sign)

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