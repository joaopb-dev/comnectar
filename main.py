from fastapi import FastAPI

app = FastAPI()

# importando o roteador do arquivo routes.py para o main.
from routes import auth_router

# incluindo o roteador na instância.
app.include_router(auth_router)
