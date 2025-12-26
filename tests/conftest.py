from flask_testing import TestCase
import requests
from testcontainers.mysql import MySqlContainer
from testcontainers.core.waiting_utils import wait_for_logs
import pytest

@pytest.fixture(scope="session")
def mysql_container():
    with MySqlContainer(
        "mysql:8.0",
        username="root",
        root_password="17111997",
        dbname="movie"
    ) as container:
        wait_for_logs(container, "port: 3306  MySQL Community Server - GPL", timeout=30)
        yield container
    container.stop()

@pytest.fixture(scope="session")
def app(mysql_container):
    from app import create_app
    """A test client for the app."""
    app = create_app()
    
    # Configura para usar o MySQL do container
    app.config['TESTING'] = True
    with app.app_context():
        yield app

@pytest.fixture(scope="function")
def client(app):
    """Client de teste."""
    return app.test_client()


