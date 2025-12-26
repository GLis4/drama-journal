import stat
from ..services.service import BaseService
from ..dtos.movie_dto import MovieDto, MovieRequestDto
from ..models.movie_model import Movie
from src.repositories.movie_repository import MovieRepository

class MovieService(BaseService[Movie, MovieRepository]):
    def __init__(self, db):
        super().__init__(Movie, MovieRepository(db))
    def find_all(self):
        movies = self.repository.get_all_movies()
        return [self._to(movie).model_dump() for movie in movies], 200
   
    def create(self, movie_data: MovieRequestDto):
        movie = self.repository.db.add(Movie(**movie_data.model_dump()))
        return self._to(movie), 201

    def update(self, movie_id, movie_data):
        movie = self.repository.get_by_id(movie_id)
        if not movie:
            return {"error":"Movie {movie_id} not found"}, 404
        movie = self.repository.update_entity(movie_id, dict(movie_data))
        return self._to(movie).model_dump(), 200

    def find(self, movie_id):
        movie = self.repository.get_by_id(movie_id)
        if not movie:
            return {"error":"Movie {movie_id} not found"}, 404
        return self._to(movie), 200

    def delete(self, movie_id):
        _, status = self._find(movie_id)
        self.repository.update_entity(movie_id, {Movie.status: 0})
        return None, status

    def _to(self, movie: Movie) -> MovieDto:
        return MovieDto(*movie.serialize())

    
