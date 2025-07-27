from app.models.favorites_model import Favorite
from app.extensions import db
from app.services import PokemonService


class FavoritesService:
    @staticmethod
    def add_favorite(username: str, pokemon_name: str) -> Favorite:
        """
        Add a new Pokémon to user's favorites
        Args:
            username (str): The username who is setting the Pokémon as favorite
            pokemon_name (str): Name of the Pokémon to add
        Returns:
            Favorite: The created Favorite model instance
        """
        favorite = Favorite(username=username, pokemon_name=pokemon_name)
        db.session.add(favorite)
        db.session.commit()
        return favorite

    @staticmethod
    def get_favorites(username: str) -> list:
        """
        Get all favorites for a specific user
        Args:
            username (str): The username to fetch favorites for
        Returns:
            list: List of Favorite model instances
        """
        return Favorite.query.filter_by(username=username).all()

    @staticmethod
    def get_favorite(username: str, favorite_id: int) -> Favorite:
        """
        Get a specific favorite by ID for a user
        Args:
            username (str): The username who owns the favorite
            favorite_id (int): ID of the favorite to retrieve
        Returns:
            Favorite: The requested Favorite model instance or None if not found
        """
        return Favorite.query.filter_by(username=username, id=favorite_id).first()

    @staticmethod
    def remove_favorite(username: str, favorite_id: int) -> bool:
        """
        Remove a favorite from user's collection
        Args:
            username (str): The username who owns the favorite
            favorite_id (int): ID of the favorite to remove
        Returns:
            bool: True if deletion was successful, False if favorite wasn't found
        """
        favorite = Favorite.query.filter_by(username=username, id=favorite_id).first()
        if favorite:
            db.session.delete(favorite)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_favorite_by_id(username: str, favorite_id: int) -> dict:
        """
        Get detailed information about a specific favorite including Pokémon data
        Args:
            username (str): The username who owns the favorite
            favorite_id (int): ID of the favorite to retrieve
        Returns:
            dict: Dictionary containing:
                - id (int): Favorite record ID
                - username (str): Owner username
                - pokemon (dict): Full Pokémon details from API
                - created_at (str): ISO formatted creation timestamp
                Returns empty dict if favorite not found
        """
        favorite = Favorite.query.filter_by(username=username, id=favorite_id).first()
        if not favorite:
            return {}

        pokemon_data = PokemonService.get_pokemon_details(favorite.pokemon_name)
        return {
            'id': favorite.id,
            'username': favorite.username,
            'pokemon': pokemon_data,
            'created_at': favorite.created_at.isoformat()
        }