from src.models.movie_model import Movie


class MovieRepository():
    def __init__(self, db):
        self.db = db
    def get_all_movies(self):
        return self.db.query(Movie).all()