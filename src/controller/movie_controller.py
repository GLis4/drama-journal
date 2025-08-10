
from flask import Blueprint, jsonify
from sqlalchemy.orm import Session
from src.services.movie_service import MovieService
from src.utils.database_conn import get_db

movie_bp = Blueprint('movies', __name__, url_prefix='/api/movie')

@movie_bp.route('/', methods=['GET'])
def find():
    db = next(get_db())
    MovieService(db).get_movies()
    return jsonify('GET Movie'), 200

@movie_bp.route('/', methods=['POST'])
def create():
    db = next(get_db())
    return jsonify('POST Movie'), 201

