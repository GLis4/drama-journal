
from flask import Blueprint, jsonify, request
from sqlalchemy.orm import Session
from src.dtos.movie_dto import MovieRequestDto
from src.services.movie_service import MovieService
from src.utils.database_conn import get_db

movie_bp = Blueprint('movies', __name__, url_prefix='/movie')

@movie_bp.route('', methods=['GET'])
def find_all():
    with get_db() as db:
        response, status = MovieService(db).find_all()
        return jsonify(response), status

@movie_bp.route('', methods=['POST'])
def create():
    movie = _request_to(request.get_json())
    with get_db() as db:
        status = MovieService(db).create(movie)
        return jsonify('POST Movie'), status

@movie_bp.route('/<int:code>', methods=['PUT'])
def update(code):
    movie = _request_to(request.get_json())
    with get_db() as db:
        status = MovieService(db).update(code, movie)
        return jsonify('PUT Movie'), status

@movie_bp.route('/<int:code>', methods=['GET'])
def find(code):
    with get_db() as db:
        response, status = MovieService(db).find(code)
        return jsonify(response), status

@movie_bp.route('/<int:code>', methods=['DELETE'])
def delete(code):
    with get_db() as db:
        status = MovieService(db).delete(code)
        return jsonify(''), status

def _request_to(data):
    return MovieRequestDto(**data)


