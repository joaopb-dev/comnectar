from pydantic import BaseModel
from typing import Optional

# definindo o esquema da classe "Pessoa".
class PessoaSchema(BaseModel):
    #juridica: bool = False
    estado: str
    municipio: str
    endereco: str
    email: str
    whatsapp: Optional[str]
    website: Optional[str]
    senha: str

    # Classe "PessoaSchema" não precisa de "from_attributes = True"
    # Pois ela só é usada indiretamente pelas rotas
    '''
    # mostra que a classe "PessoaSchema" vai ser interpretado como ORM não como dict.
    class Config:
        from_attributes = True
    '''

class PessoaJuridicaSchema(PessoaSchema):
    cnpj: str
    cpf_replegal: str
    nome_replegal: str
    nome_fantasia: str

    class Config:
        from_attributes = True

class PessoaFisicaSchema(PessoaSchema):
    cpf: str
    nome: str

    class Config:
        from_attributes = True
