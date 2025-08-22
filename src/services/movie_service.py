from ..models.movie_model import Movie
from src.repositories.movie_repository import MovieRepository
from datetime import datetime as date

class MovieService:
    def __init__(self, db):
        self.repo = MovieRepository(db)

    def get_movies(self):
        return self.repo.get_all_movies()
    
    def create_movie(self, movie_data):
        movie_data['release_date'] = date.strptime(movie_data.get('release_date'), '%Y-%m-%d')
        movie = Movie(**movie_data)
        self.repo.db.add(movie)
        return movie