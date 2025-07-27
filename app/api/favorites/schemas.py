from pydantic import BaseModel

class FavoriteCreate(BaseModel):
    pokemon_name: str

class FavoriteResponse(BaseModel):
    id: int
    pokemon_name: str
    created_at: str

class FavoriteDeleteResponse(BaseModel):
    success: bool
    message: str