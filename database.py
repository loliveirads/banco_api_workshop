from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")


# Conexão com o banco de dados
DATABASE_URL = "postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco"
engine = create_engine(DATABASE_URL)

# Base ORM
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo Produto
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)
    disponivel = Column(Boolean, nullable=False, default=True) 

# Criar a tabela no banco
Base.metadata.create_all(engine)
print("Tabela criada com sucesso!")