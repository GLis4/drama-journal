from sqlalchemy import Column, Integer, VARCHAR
from src.models.base import Base

class Movie(Base):
    __tablename__ = 'movie'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(250), nullable=False)
    description = Column(VARCHAR(250))
    release_date = Column(VARCHAR(10))
    genre_id = Column(Integer)
    director_id = Column(Integer, nullable=False)
    cast_movie = Column(VARCHAR(250))
    duration = Column(Integer)
    rate_id = Column(Integer)
    studio = Column(VARCHAR(250))
    status = Column(Integer, nullable=False)
    
    def serialize(self):
        return  { column.name: getattr(self, column.name) for column in self.__table__.columns}