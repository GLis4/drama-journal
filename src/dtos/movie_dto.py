from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MovieDto(BaseModel):
    id: int
    title: Optional[str]
    description: Optional[str]
    release_date: Optional[ datetime]
    genre_id: Optional[str]
    director_id: Optional[int]
    cast_movie: Optional[str]
    duration: Optional[str]
    rate_id: Optional[int]
    studio: Optional[str]
    status: int