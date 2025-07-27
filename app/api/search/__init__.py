# This makes the horoscope package a Python package
# Can be empty or contain horoscope-specific initializations
from .controllers import SearchController
from .routes import search_bp

__all__ = ['SearchController', 'search_bp']