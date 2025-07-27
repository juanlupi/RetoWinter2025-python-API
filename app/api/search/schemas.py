from pydantic import BaseModel, validator
from typing import Optional


class SearchRequest(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None

    @validator('name')
    def validate_name(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Name cannot be empty if provided")
        return v

    @validator('type')
    def validate_type(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Type cannot be empty if provided")
        return v


class PokemonSearchResult(BaseModel):
    name: str
    image: str
    types: list[str]
    height: int
    weight: int
    abilities: list[str]
