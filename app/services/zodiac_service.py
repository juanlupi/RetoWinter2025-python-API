from datetime import datetime
from typing import Dict, Tuple


class ZodiacService:
    ZODIAC_DATES: Dict[str, Tuple[Tuple[int, int], Tuple[int, int]]] = {
        'aries': ((3, 21), (4, 19)),
        'taurus': ((4, 20), (5, 20)),
        'gemini': ((5, 21), (6, 20)),
        'cancer': ((6, 21), (7, 22)),
        'leo': ((7, 23), (8, 22)),
        'virgo': ((8, 23), (9, 22)),
        'libra': ((9, 23), (10, 22)),
        'scorpio': ((10, 23), (11, 21)),
        'sagittarius': ((11, 22), (12, 21)),
        'capricorn': ((12, 22), (1, 19)),
        'aquarius': ((1, 20), (2, 18)),
        'pisces': ((2, 19), (3, 20))
    }

    POKEMON_BY_SIGN: Dict[str, str] = {
        'aries': 'charizard',
        'taurus': 'tauros',
        'gemini': 'kadabra',
        'cancer': 'kingler',
        'leo': 'luxray',
        'virgo': 'celebi',
        'libra': 'alakazam',
        'scorpio': 'drapion',
        'sagittarius': 'decidueye',
        'capricorn': 'gogoat',
        'aquarius': 'vaporeon',
        'pisces': 'milotic'
    }

    @classmethod
    def parse_date(cls, date_str: str) -> datetime.date:
        # Parse date from dd/mm/yyyy format
        try:
            return datetime.strptime(date_str, '%d/%m/%Y').date()
        except ValueError:
            raise ValueError("Invalid date format. Please use DD/MM/YYYY")

    @classmethod
    def get_zodiac_sign(cls, birth_date: str) -> str:
        # Calculate zodiac sign based on birth date
        # Format: DD/MM/YYYY

        date_obj = cls.parse_date(birth_date)
        month_day = (date_obj.month, date_obj.day)

        # Special case for Capricorn (straddles December/January)
        if (12, 22) <= month_day <= (12, 31) or (1, 1) <= month_day <= (1, 19):
            return 'capricorn'

        # Check other signs
        for sign, ((start_month, start_day), (end_month, end_day)) in cls.ZODIAC_DATES.items():
            if sign == 'capricorn':
                continue  # Already handled

            if (start_month, start_day) <= month_day <= (end_month, end_day):
                return sign

        return 'capricorn'  # Default fallback

    @classmethod
    def get_pokemon_for_sign(cls, sign: str) -> str:
        # Get the associated Pokémon for a zodiac sign
        return cls.POKEMON_BY_SIGN.get(sign.lower(), 'pikachu')