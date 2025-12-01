from pwdlib import PasswordHash
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

pwd_context = PasswordHash.recommended()


#def create_access_token(data: dict):

# Função para gerar o hash da senha
def get_password_hash(password: str):
    return pwd_context.hash(password)

# Função para verificar senha
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
