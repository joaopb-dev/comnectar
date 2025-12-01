from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

# criação do database.
db = create_engine('sqlite:///database.db')

# criação da base do database.
base = declarative_base()

# declaração das classes.
class Pessoa(base):
    __tablename__ = "Pessoas"

    id: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str]
    # juridica: Mapped[bool]
    estado: Mapped[str]
    municipio: Mapped[str]
    endereco: Mapped[str]
    email: Mapped[str]
    senha: Mapped[str]
    whatsapp: Mapped[str]
    website: Mapped[str]

    __mapper_args__ = {
        "polymorphic_identity": "pessoa",
        "polymorphic_on": "tipo",
        #"polymorphic_identity": False,
        #"polymorphic_on": "juridica",
    }

class PessoaJuridica(Pessoa):
    __tablename__ = "Pessoas_Juridicas"

    id: Mapped[int] = mapped_column(ForeignKey("Pessoas.id"), primary_key=True)
    cnpj: Mapped[str]
    nome_fantasia: Mapped[str]
    nome_replegal: Mapped[str]
    cpf_replegal: Mapped[str]

    __mapper_args__ = {
        "polymorphic_identity": "juridica",
        #"polymorphic_identity": True,
    }

class PessoaFisica(Pessoa):
    __tablename__ = "Pessoas_Fisicas"

    id: Mapped[int] = mapped_column(ForeignKey("Pessoas.id"), primary_key=True)
    cpf: Mapped[str]
    nome: Mapped[str]

    __mapper_args__ = {
        "polymorphic_identity": "fisica",
        #"polymorphic_identity": False,
    }

'''
class Pessoa(base):
    __tablename__ = 'Pessoas'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    juridica = Column('Juridica', Boolean, nullable=False, default=False)
    estado = Column('Estado', String, nullable=False)
    municipio = Column('Municipio', String, nullable=False)
    endereco = Column('Endereco', String, nullable=False)
    email = Column('EMail', String, nullable=False)
    senha = Column('Senha', String, nullable=False)
    whatsapp = Column('Whatsapp', Integer)
    website = Column('Website', String)

    def __init__(self, juridica, estado, municipio, endereco, email, senha, whatsapp, website):
        self.juridica = juridica
        self.estado = estado
        self.municipio = municipio
        self.endereco = endereco
        self.email = email
        self.senha = senha
        self.whatsapp = whatsapp
        self.website = website

class PessoaJuridica(Pessoa):
    __tablename__ = 'Pessoas_Juridicas'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    cnpj = Column('CNPJ', Integer, nullable=False)
    pessoa_id = Column('Pessoa_ID', ForeignKey('Pessoas.ID'))
    nome_replegal = Column('Nome_Representante_Legal', String, nullable=False)
    cpf_replegal = Column('CPF_Representante_Legal', Integer, nullable=False)
    nome_fantasia = Column('Nome_Fantasia', String)

    def __init__(self, juridica, estado, municipio, endereco, email, senha, whatsapp, website, cnpj, pessoa_id, nome_replegal, cpf_replegal, nome_fantasia):
        super().__init__(juridica, estado, municipio, endereco, email, senha, whatsapp, website)
        self.cnpj = cnpj
        self.pessoa_id = pessoa_id
        self.nome_replegal = nome_replegal
        self.cpf_replegal = cpf_replegal
        self.nome_fantasia = nome_fantasia

class PessoaFisica(Pessoa):
    __tablename__ = 'Pessoas_Fisicas'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    cpf = Column('CPF', Integer, nullable=False)
    pessoa_id = Column('Pessoa_ID', Integer, ForeignKey('Pessoas.ID'))
    nome = Column('Nome', String, nullable=False)

    def __init__(self, juridica, estado, municipio, endereco, email, senha, whatsapp, website, cpf, pessoa_id, nome):
        super().__init__(juridica, estado, municipio, endereco, email, senha, whatsapp, website)
        self.cpf = cpf
        self.pessoa_id = pessoa_id
        self.nome = nome
'''