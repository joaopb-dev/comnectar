from fastapi import APIRouter, Depends, HTTPException
from models import Pessoa, PessoaFisica, PessoaJuridica
from dependencies import pegar_session
from security import get_password_hash, verify_password
from schemas import PessoaSchema, PessoaFisicaSchema, PessoaJuridicaSchema
from sqlalchemy.orm import Session

# roteador do app no arquivo main.py definindo o prefixo do endpoint como auth e a tag do docs como auth também.
auth_router = APIRouter(prefix='/auth', tags= ['auth'])

# rota de cadastro.
@auth_router.post('/register/juridica')
def register_pj(
    pessoaj_schema: PessoaJuridicaSchema,
    session: Session = Depends(pegar_session)
    ):
    pessoa = session.query(Pessoa).filter(Pessoa.email == pessoaj_schema.email).first()
    if pessoa:
        raise HTTPException(status_code=400, detail='E-mail de usuário já cadastrado.')
    else:
        hashed_password = get_password_hash(pessoaj_schema.senha)
        nova_pessoa = PessoaJuridica(
            tipo="juridica",
            estado= pessoaj_schema.estado,
            municipio= pessoaj_schema.municipio,
            endereco= pessoaj_schema.endereco,
            email= pessoaj_schema.email,
            senha= hashed_password,
            whatsapp= pessoaj_schema.whatsapp,
            website= pessoaj_schema.website,
            cnpj= pessoaj_schema.cnpj,
            nome_fantasia= pessoaj_schema.nome_fantasia,
            nome_replegal= pessoaj_schema.nome_replegal,
            cpf_replegal= pessoaj_schema.cpf_replegal
        )

        session.add(nova_pessoa)
        session.commit()
        return {"message": "Pessoa jurídica cadastrada.", "id": nova_pessoa.id}

@auth_router.post('/register/fisica')
def register_pf(
    pessoaf_schema: PessoaFisicaSchema,
    session: Session = Depends(pegar_session)
    ):
    pessoa = session.query(Pessoa).filter(Pessoa.email == pessoaf_schema.email).first()
    if pessoa:
        raise HTTPException(status_code=400, detail='E-mail de usuário já cadastrado.')
    else:
        hashed_password = get_password_hash(pessoaf_schema.senha)
        nova_pessoa = PessoaFisica(
            tipo="fisica",
            estado= pessoaf_schema.estado,
            municipio= pessoaf_schema.municipio,
            endereco= pessoaf_schema.endereco,
            email= pessoaf_schema.email,
            senha= hashed_password,
            whatsapp= pessoaf_schema.whatsapp,
            website= pessoaf_schema.website,
            cpf= pessoaf_schema.cpf,
            nome= pessoaf_schema.nome
        )

        session.add(nova_pessoa)
        session.commit()
        return {"message": "Pessoa jurídica cadastrada.", "id": nova_pessoa.id}
'''
@auth_router.post('/register')
def new_user(
    pessoa_schema: PessoaSchema,
    pessoaj_schema: PessoaJuridicaSchema,
    pessoaf_schema: PessoaFisicaSchema,
    session: Session = Depends(pegar_session)
    ):
    pessoa = session.query(Pessoa).filter(Pessoa.email == pessoa_schema.email).first
    if not pessoa:
        raise HTTPException(status_code=400, detail='E-mail de usuário já cadastrado.')
    else:
        senha_criptografada = bcrypt_context.hash(pessoa_schema.senha)
'''