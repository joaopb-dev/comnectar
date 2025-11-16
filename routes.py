from fastapi import APIRouter

# roteador do app no arquivo main.py definindo o prefixo do endpoint como auth e a tag do docs como auth também.
auth_router = APIRouter(prefix='/auth', tags= ['auth'])

# rota de cadastro.
@auth_router.get('/register')
async def register_page():
    ...

# confirmar cadastro.
@auth_router.post('/register')
async def register():
    ...

# rota de login.
@auth_router.get('/login')
async def login_page():
    ...

# confirmar cadastro.
@auth_router.post('/login')
async def login():
    ...
