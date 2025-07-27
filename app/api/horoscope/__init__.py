# This makes the horoscope package a Python package
# Can be empty or contain horoscope-specific initializations
from .controllers import HoroscopeController
from .routes import horoscope_bp

__all__ = ['HoroscopeController', 'horoscope_bp']