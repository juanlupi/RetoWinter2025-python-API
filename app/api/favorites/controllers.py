from flask import abort, current_app
from app.services.favorites_service import FavoritesService
from app.services.pokemon_service import PokemonService


class FavoritesController:
    @staticmethod
    def add_favorite(username: str, data):
        """
        Add a Pokémon to user's favorites with full validation.
        Args:
            username (str): The username of the user adding the favorite
            data (dict): Dictionary containing:
                - pokemon_name (str): Name of the Pokémon to add
        Returns:
            dict: Dictionary representation of the created favorite
        """
        # Verify the Pokémon exists
        pokemon_data = PokemonService.get_pokemon_details(data['pokemon_name'])
        if not pokemon_data:
            abort(404, description="Pokémon not found")

        favorite = FavoritesService.add_favorite(username, data['pokemon_name'])
        return favorite.to_dict()  # Return the dictionary directly

    @staticmethod
    def get_favorites(username: str):
        """
        Retrieve all favorites for a given user.
        Args:
            username (str): The username to fetch favorites for
        Returns:
            list: List of dictionaries representing each favorite Pokémon
        """
        favorites = FavoritesService.get_favorites(username)
        return [f.to_dict() for f in favorites]  # Return list of dictionaries

    @staticmethod
    def remove_favorite(username: str, favorite_id: int):
        """
        Remove a favorite Pokémon from user's collection.
        Args:
            username (str): The username removing the favorite
            favorite_id (int): ID of the favorite record to remove
        Returns:
            dict: Dictionary containing:
                - success (bool): Operation status
                - message (str): Result message
        """
        success = FavoritesService.remove_favorite(username, favorite_id)
        return {  # Return dictionary directly
            'success': success,
            'message': 'Favorite deleted' if success else 'Favorite not found'
        }

    @staticmethod
    def get_favorite_by_id(username: str, favorite_id: int) -> dict:
        """
        Retrieve a specific favorite record by ID for a user.
        Args:
            username (str): The username owning the favorite
            favorite_id (int): ID of the favorite record to retrieve
        Returns:
            dict: Dictionary representation of the favorite if found,
                empty dict if not found
        """
        try:
            return FavoritesService.get_favorite_by_id(username, favorite_id)
        except Exception as e:
            current_app.logger.error(f"Error getting favorite: {str(e)}")
            return {}