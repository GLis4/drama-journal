from sqlalchemy import select, update
from ..models.movie_model import Movie


class MovieRepository():
    def __init__(self, db):
        self.db = db

    def get_all_movies(self, conditions=None):
        conditions.append(Movie.status==1)
        return self.db.query(Movie).where(*conditions).all()

    def update_entity(self, movie_id, data):
        return self.db.execute(update(Movie).where(Movie.id==movie_id).values(**data))

    def get_by_id(self, movie_id):
        result = self.db.execute(select(Movie).where(Movie.id==movie_id))
        return result.scalar()
