from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

#Parametros para conexão com Banco de Dados

db_user = "user"
db_password = "user_password"
db_host = "localhost"
db_port = "3306"
db_name = "meu_banco"

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

#Conectando ao banco de dados

db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

#Gerencinado sessão
@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commit()

    except Exception as erro:
        db.rollback() #Se der certo, desfez a operação.
        raise erro #Lança a exceção de erro
    finally:
        db.close() #Fechando a conexão