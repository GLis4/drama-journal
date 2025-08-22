from ..models.movie_model import Movie
from src.repositories.movie_repository import MovieRepository
from datetime import datetime as date

class MovieService:
    def __init__(self, db):
        self.repo = MovieRepository(db)

    def find_all(self):
        return self.repo.get_all_movies()
    
    def create(self, movie_data):
        movie_data['release_date'] = date.strptime(movie_data.get('release_date'), '%Y-%m-%d')
        movie = Movie(**movie_data)
        self.repo.db.add(movie)
        return movie

    def update(self, movie_id, movie_data):
        movie = self.repo.get_by_id(movie_id)
        if not movie:
            raise ValueError(f"Movie with id {movie_id} not found")

        movie = self.repo.update_entity(movie_id, dict(movie_data))
        return movie.__dict__

    def find(self, movie_id):
        movie = self.repo.get_by_id(movie_id)
        if not movie:
            raise ValueError(f"Movie with id {movie_id} not found")
        return {
            "title": movie.title,
            "id": movie.id
            }