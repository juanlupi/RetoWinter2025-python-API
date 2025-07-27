from flask import abort
from app.services.pokemon_service import PokemonService
from app.api.search.schemas import SearchRequest, PokemonSearchResult


class SearchController:
    @staticmethod
    def search_pokemon(name: str = None, type: str = None) -> list:
        """
        Search for Pokémon by name and/or type with proper validation and error handling.

        Args:
        name (str, optional): The name or partial name of the Pokémon to search for.
                            Case-insensitive. Can be None if searching only by type.
        type (str, optional): The Pokémon type to filter by (e.g., 'fire', 'water').
                               Can be None if searching only by name.
        Returns:
        list[PokemonSearchResult]: A list of formatted Pokémon search results matching
                                    the criteria. Returns empty list if no matches found.
       """

        try:
            # Validate input
            search_request = SearchRequest(name=name, type=type)

            # Perform search
            results = PokemonService.search_pokemon(
                name=search_request.name,
                type=search_request.type
            )

            # Format response
            formatted_results = []
            for pokemon in results:
                formatted_results.append(
                    PokemonSearchResult(
                        name=pokemon['name'],
                        image=pokemon['image'],
                        types=pokemon['types'],
                        height=pokemon['height'],
                        weight=pokemon['weight'],
                        abilities=pokemon['abilities']
                    )
                )

            return formatted_results

        except ValueError as e:
            abort(400, description=str(e))
        except Exception as e:
            abort(500, description="Internal server error")