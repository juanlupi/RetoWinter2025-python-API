# Pokémon Horoscope API 🚀

![Pokémon Logo](https://upload.wikimedia.org/wikipedia/commons/9/98/International_Pok%C3%A9mon_logo.svg)

## Descripción 📝

Este proyecto es una API Flask que proporciona información sobre Pokémons, incluyendo horóscopos Pokémon basados en fechas de nacimiento, búsqueda de Pokémon y gestión de favoritos.

## Características principales
- **Horóscopo Pokémon**: Obtén tu Pokémon según tu signo zodiacal.
- **Búsqueda de Pokémon**: Encuentra Pokémon por nombre o tipo.
- **Favoritos**: Guarda tus Pokémon favoritos por usuario.
- **API RESTful**: Endpoints claros y documentados

## Tecnologías utilizadas
- Python
- Flask
- SQLAlchemy (SQLite)
- Docker
- PokeAPI (como fuente de datos)

## Endpoints principales 🌐
### Variables de ejemplo
```
userName = Pepe
birthDate = 25/10/2008
pokemonName = pikachu
pokemonType = electric
favorite_id = 2
```
### Horóscopo Pokémon
``` 
POST /v1/horoscope
Headers: {"Content-Type": "application/json"}
Body: {"nombre": "{userName}", "fecha_nacimiento": "{birthDate}"}
```
### Búsqueda de Pokémon
```
GET /v1/pokemon?nombre={pokemonName}&tipo={pokemonType}
GET /v1/pokemon?nombre={pokemonName}
GET /v1/pokemon?tipo={pokemonType}
```
### Favoritos
```
POST /v1/favorites?usuario={userName}
Headers: {"Content-Type": "application/json"}
Body: {"pokemon_name": "{pokemonName}"}

GET /v1/favorites?usuario={userName}

DELETE /v1/favorites/{favorite_id}?usuario={userName}

GET /v1/favoritos/{favorite_id}?usuario={userName}
```
## Estructura del proyecto 🏗️
```
RetoWinter2025-python-API/
│
├── app/                                  # Main application package
│   ├── __init__.py                       # App factory and initialization
│   ├── config.py                         # Configuration settings
│   ├── extensions.py                     # Flask extensions initialization
│   │
│   ├── api/                              # API endpoints
│   │   ├── __init__.py
│   │   ├── favorites/                    # Favorites feature
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   ├── schemas.py
│   │   │   └── controllers.py
│   │   │
│   │   │
│   │   ├── horoscope/                    # Horoscope feature
│   │   │   ├── __init__.py
│   │   │   ├── routes.py
│   │   │   ├── schemas.py
│   │   │   └── controllers.py
│   │   │
│   │   │
│   │   └── search/                       # Search feature
│   │       ├── __init__.py
│   │       ├── routes.py
│   │       ├── schemas.py
│   │       └── controllers.py
│   │
│   ├── services/                         # Business logic
│   │   ├── __init__.py
│   │   ├── pokemon_service.py            # PokeAPI interactions
│   │   ├── zodiac_service.py             # Zodiac calculations
│   │   └── favorites_service.py          # Favorites storage
│   │
│   ├── models/                           # Data models
│   │   ├── __init__.py
│   │   └── favorite_model.py             # Favorite model
│   │
│   └── utils/                            # Utilities
│
│
├── docker-compose.yml                    # Docker compose configuration
├── Dockerfile                            # Docker configuration
├── requirements.txt                      # Python dependencies
└── README.md                             # Project documentation 
```

## Requisitos 📋

- Docker
- Docker Compose

## Cómo ejecutar el proyecto ⚡

```
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/pokemon-api.git
cd pokemon-api

# 2. Iniciar contenedores
docker-compose up -d --build