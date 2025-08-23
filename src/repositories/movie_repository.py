from sqlalchemy import select, update
from src.models.movie_model import Movie
import datetime as date


class MovieRepository():
    def __init__(self, db):
        self.db = db

    def get_all_movies(self):
        return self.db.query(Movie).where(Movie.status==1).all()

    def update_entity(self, movie_id, data):
        return self.db.execute(update(Movie).where(Movie.id==movie_id).values(**data))

    def get_by_id(self, movie_id):
        result = self.db.execute(select(Movie).where(Movie.id==movie_id))
        return result.scalar_one()
