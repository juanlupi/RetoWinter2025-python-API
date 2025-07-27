import requests
from functools import lru_cache
from app.config import Config
from flask import current_app
import json


class PokemonService:
    BASE_URL = Config.POKEAPI_BASE_URL

    @classmethod
    @lru_cache(maxsize=128)  # Cache responses to avoid repeated API calls
    def get_pokemon_details(cls, pokemon_name: str) -> dict:
        """
        Get detailed information about a Pokémon from PokeAPI
        Args:
            pokemon_name (str): Name of the Pokémon to look up
        Returns:
            dict: Pokémon details including name, image, types, etc.
        """
        try:
            response = requests.get(
                f"{cls.BASE_URL}/pokemon/{pokemon_name.lower()}",
                timeout=5
            )
            response.raise_for_status()

            pokemon_data = response.json()

            return {
                'name': pokemon_data['name'],
                'image': pokemon_data['sprites']['front_default'],
                'types': [t['type']['name'] for t in pokemon_data['types']],
                'height': pokemon_data['height'] / 10,  # Convert to meters
                'weight': pokemon_data['weight'] / 10,  # Convert to kilograms
                'abilities': [a['ability']['name'] for a in pokemon_data['abilities']],
                'stats': {stat['stat']['name']: stat['base_stat']
                          for stat in pokemon_data['stats']}
            }

        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"PokeAPI request failed: {str(e)}")
            return []

    @classmethod
    @lru_cache(maxsize=128)
    def search_pokemon(cls, name: str = None, type: str = None) -> list:
        """
        Search Pokémon by name and/or type
        Args:
            name (str): Name of the Pokémon to look up
            type (str): Type of Pokémon to look up
        Returns:
            dict: Pokémon details including name, image, types, etc, in case of being an exact match
            dict[]: Pokémons details including name, image, types, etc, of the first 10 matching pokemons
        """
        try:
            # Validate at least one search parameter exists
            if not name and not type:
                return []

            # Try exact match first if name provided
            if name:
                try:
                    exact_match = cls.get_pokemon_details(name)
                    if exact_match:  # Only return if we got a valid result
                        return [exact_match]
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 404:
                        current_app.logger.debug(f"No exact match for '{name}', trying partial match")
                    else:
                        current_app.logger.error(f"HTTP error in exact match: {str(e)}")
                        return []
                except Exception as e:
                    current_app.logger.error(f"Error in exact match: {str(e)}")
                    return []

            # Search by type if specified
            if type:
                try:
                    type_url = f"{cls.BASE_URL}/type/{type.lower()}"
                    type_response = requests.get(type_url, timeout=5)
                    type_response.raise_for_status()
                    type_data = type_response.json()

                    pokemon_list = [p['pokemon']['name'] for p in type_data['pokemon']]

                    # Filter by name if provided
                    if name:
                        pokemon_list = [p for p in pokemon_list if name.lower() in p.lower()]

                    # Get details with error handling
                    results = []
                    for pokemon_name in pokemon_list[:10]:
                        try:
                            details = cls.get_pokemon_details(pokemon_name)
                            if details:
                                results.append(details)
                        except Exception:
                            continue
                    return results
                except requests.exceptions.RequestException as e:
                    current_app.logger.error(f"Type search failed: {str(e)}")
                    return []

            # Fallback to name-based partial search
            if name:
                try:
                    search_url = f"{cls.BASE_URL}/pokemon?limit=1000"
                    search_response = requests.get(search_url, timeout=5)
                    search_response.raise_for_status()
                    search_data = search_response.json()

                    matches = [p['name'] for p in search_data['results']
                               if name.lower() in p['name'].lower()]

                    results = []
                    for pokemon_name in matches[:10]:
                        try:
                            details = cls.get_pokemon_details(pokemon_name)
                            if details:
                                results.append(details)
                        except Exception:
                            continue
                    return results
                except requests.exceptions.RequestException as e:
                    current_app.logger.error(f"Name search failed: {str(e)}")
                    return []

            return []

        except Exception as e:
            current_app.logger.error(f"Unexpected search error: {str(e)}")
            return []