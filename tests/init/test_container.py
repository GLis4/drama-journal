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
                
@pytest.fixture(scope="module")
def flask_app(mysql_container):
    # Configura a URL de conexão
    db_url = (
        f"mysql+pymysql://test:test@"
        f"{mysql_container.get_container_host_ip()}:"
        f"{mysql_container.get_exposed_port(3306)}/testdb"
    )
    
    # Cria container Flask
    with DockerContainer("python:3.9") as container:
        container.with_exposed_ports(5000)
        container.with_volume_mapping(os.getcwd(), "/app")
        container.with_env("DATABASE_URL", db_url)
        container.with_command(
            "sh -c 'pip install -r /app/requirements.txt && "
            "FLASK_APP=/app/app.py flask run --host=0.0.0.0'"
        )
        container.start()  
        import time
        time.sleep(5)      
        yield container

def test_with_database(flask_app):
    host = flask_app.get_container_host_ip()
    port = flask_app.get_exposed_port(5000)
    base_url = f"http://{host}:{port}/api/movie/"
    response = requests.get(base_url)
    print(response.json)
    assert response.json() == "GET Movie"
    # Testes que dependem do banco de dados...