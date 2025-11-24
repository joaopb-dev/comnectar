from pydantic import BaseModel

# definindo o esquema da classe "Pessoa".
class PessoaSchema(BaseModel):
    juridica: bool = False
    estado: str
    municipio: str
    endereco: str
    email: str
    whatsapp: str
    website: str
    senha: str

    # mostra que a classe "PessoaSchema" vai ser interpretado como ORM não como dict.
    class Config:
        from_attributes = True

class PessoaJuridicaSchema(PessoaSchema):
    cnpj: int
    cpf_replegal: int
    nome_replegal: str
    nome_fantasia: str

class PessoaFisicaSchema(PessoaSchema):
    cpf: int
    nome: str
