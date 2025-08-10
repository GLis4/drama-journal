from src.repositories.movie_repository import MovieRepository


class MovieService:
    def __init__(self, db):
        self.repo = MovieRepository(db)
    def get_movies(self):
        return self.repo.get_all_movies()