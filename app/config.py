import os

class Config:
    POKEAPI_BASE_URL = 'https://pokeapi.co/api/v2'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////app/favorites.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False