from models import db
from sqlalchemy.orm import sessionmaker

def pegar_session():
    try:
    # definindo a conexão da session com o banco de dados.
        Session = sessionmaker(bind=db)
        # atribuindo a "Session" a uma variável.
        session = Session()
        yield session # retorna a função mas não encerra ela.
    finally:
        session.close()
