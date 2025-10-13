from enum import Enum
from pydantic import BaseModel

class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop' 

class Band(BaseModel):
    #     {"id": 1, 'name': 'The Kinks', 'genre': 'Rock'},  
    id: int
    name: str
    genre: str
    