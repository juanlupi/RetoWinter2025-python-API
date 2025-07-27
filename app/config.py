import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    POKEAPI_BASE_URL = 'https://pokeapi.co/api/v2'