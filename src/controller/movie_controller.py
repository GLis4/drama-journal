
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import Session
from src.services.movie_service import MovieService
from src.utils.database_conn import get_db

movie_bp = Blueprint('movies', __name__, url_prefix='/api/movie')

@movie_bp.route('/', methods=['GET'])
def find_all():
    with get_db() as db:
        MovieService(db).get_movies()
        return jsonify('GET Movie'), 200

@movie_bp.route('/', methods=['POST'])
def create():
    with get_db() as db:
        MovieService(db).create_movie(request.get_json())
        return jsonify('POST Movie'), 201

