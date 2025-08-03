
from flask import Blueprint, jsonify

movie_bp = Blueprint('movies', __name__, url_prefix='/api/movie')

@movie_bp.route('/', methods=['GET'])
def get_movie():
    return jsonify('GET Movie'), 200