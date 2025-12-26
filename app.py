from flask import Flask
from src.controllers.movie_controller import movie_bp

""" An API REST build to create, read, update and/or delete movies and series
 from a database"""


def create_app():
	app = Flask(__name__)
	app.register_blueprint(movie_bp)
	return app


if __name__ == "__main__":
	app = create_app()
	app.run(debug=True)
