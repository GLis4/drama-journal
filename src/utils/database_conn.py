from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuração da engine (mantida igual)
engine = create_engine(
    "mysql+pymysql://root:17111997@localhost/movie",
    pool_pre_ping=True
)

# Criação do sessionmaker (sem global)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine
)

# Função get_db corrigida
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    finally:
        db.close()