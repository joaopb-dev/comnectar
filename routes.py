from fastapi import APIRouter, Depends, HTTPException
from models import Pessoa, PessoaFisica, PessoaJuridica
from dependencies import pegar_session
from main import bcrypt_context
from schemas import PessoaSchema, PessoaFisicaSchema, PessoaJuridicaSchema
from sqlalchemy.orm import Session

# roteador do app no arquivo main.py definindo o prefixo do endpoint como auth e a tag do docs como auth também.
auth_router = APIRouter(prefix='/auth', tags= ['auth'])

# rota de cadastro.
@auth_router.post('/register')
def new_user(
    pessoa_schema: PessoaSchema,
    pessoaj_schema: PessoaJuridicaSchema,
    pessoaf_schema: PessoaFisicaSchema,
    session: Session = Depends(pegar_session)
    ):
    pessoa = session.query(Pessoa).filter(Pessoa).filter(Pessoa.email == pessoa_schema.email).first
    if pessoa:
        raise HTTPException(status_code=400, detail='E-mail de usuário já cadastrado.')
    else:
        senha_criptografada = bcrypt_context.hash(pessoa_schema.senha)
