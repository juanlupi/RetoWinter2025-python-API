# This makes the horoscope package a Python package
# Can be empty or contain horoscope-specific initializations
from .controllers import FavoritesController
from .routes import favorites_bp

__all__ = ['FavoritesController', 'favorites_bp']