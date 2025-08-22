import os
import requests
from testcontainers.mysql import MySqlContainer
from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for_logs
import pytest

@pytest.fixture(scope="module")
def mysql_container():
    with MySqlContainer(
        "mysql:8.0",
        username="test",
        root_password="test",
        dbname="testdb"
    ) as container:
        yield container

def create_app():
    import app
    app['TESTING'] = True

def test_with_database(flask_app):
    host = flask_app.get_container_host_ip()
    port = flask_app.get_exposed_port(5000)
    base_url = f"http://{host}:{port}/api/movie"
    response = requests.get(base_url)
    print(response.json)
    assert response.status_code == 200
    assert response.json() == "GET Movie"
    # Testes que dependem do banco de dados...