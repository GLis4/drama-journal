from flask import Flask
from src.controller.movie_controller import movie_bp
""" An API REST build to create, read, update and/or delete movies and series
 from a database"""

app = Flask(__name__)
app.register_blueprint(movie_bp)
print(movie_bp)
app.run(debug=True)
