from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configuração da engine (mantida igual)
engine = create_engine(
    "mysql+pymysql://root:00000@localhost/movie",
    pool_pre_ping=True
)

# Criação do sessionmaker (sem global)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Função get_db corrigida
def get_db():
    db = SessionLocal()  # Cria uma nova sessão
    try:
        yield db
    finally:
        db.close()  # Fecha a sessão (agora sim fechando uma sessão real)