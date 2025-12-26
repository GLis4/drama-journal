from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_serializer


class MovieDto(BaseModel):
    id: int
    title: Optional[str]
    description: Optional[str]
    release_date: Optional[datetime]
    genre_id: Optional[str]
    director_id: Optional[int]
    cast_movie: Optional[str]
    duration: Optional[str]
    rate_id: Optional[int]
    studio: Optional[str]
    status: int

class MovieResponseDto(MovieDto):
    pass

class MovieRequestDto(MovieDto):
    
    @field_serializer('release_date')
    def date_serialize(self, release_date) -> Optional[str]:
        if release_date:
            return release_date.strftime("%Y-%m-%d")
        return None