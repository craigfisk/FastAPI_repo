from datetime import date

from enum import Enum
from pydantic import BaseModel, field_validator
 
class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop' 

class GenreChoices(Enum):
    ROCK = 'Rock'
    ELECTRONIC = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip-hop' 

# class Band(BaseModel):
#     #     {"id": 1, 'name': 'The Kinks', 'genre': 'Rock'},  
#     id: int
#     name: str
#     genre: str
#     albums: list['Album'] = []

class BandBase(BaseModel):
    name: str
    genre: GenreChoices
    albums: list['Album'] = []

class BandCreate(BandBase):
    # @validator('genre', pre=True)
    @field_validator('genre')
    def genres_match(cls, v):
        if isinstance(v, str):
            v = v.strip().lower()
            for genre in GenreChoices:
                if genre.value.lower() == v:
                    return genre
        elif isinstance(v, GenreChoices):
            return v
        raise ValueError(f'Genre must be one of: {", ".join([g.value for g in GenreChoices])}')
          
class BandWithID(BandBase):
    id: int

class Album(BaseModel):
    title: str
    release_date: date
