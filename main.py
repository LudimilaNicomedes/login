from fastapi import FastAPI
from pydantic import BaseModel
# from db import conexao
import db
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Permite que o front-end acesse o back-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],  
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (POST, GET, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)


# Modelos para organizar os dados que vêm do Swagger
class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
class LoginSchema(BaseModel):
    email: str
    senha: str
class chat(BaseModel):
    perguinta: str


@app.post('/conta')
async def conta(dados: LoginSchema):
    # Busca o usuário no arquivo JSON simulação
    usuario = db.buscar_usuario_por_email(dados.email)
    
    # Valida e-mail e senha
    if usuario is None or usuario["senha"] != dados.senha:
        return {"erro": "E-mail ou senha inválidos"}
        
    return {"status": "Login efetuado com sucesso"}

@app.post('/criar_conta')
async def criar_conta(dados: UsuarioSchema):
    # Verifica se o e-mail já está cadastrado
    usuario_existente = db.buscar_usuario_por_email(dados.email)
    if usuario_existente:
        return {"erro": "E-mail já cadastrado"}
        
    # Cadastra o novo usuário no arquivo JSON
    db.cadastrar_usuario(dados.nome, dados.email, dados.senha)
    return {"status": "Conta criada com sucesso!"}


















"""
#@app.post('/conta')
async def conta(dados: LoginSchema):
    cursor = conexao.cursor() 
    cursor.execute(
        "SELECT * FROM usuario WHERE email = ? AND senha = ?",
        (dados.email, dados.senha))
    usuario = cursor.fetchone()
    cursor.close()  # Fecha apenas o cursor desta requisição
    
    if usuario is None:
        return {"erro": "E-mail ou senha inválidos"}
        
    return {"status": "Login efetuado com sucesso"}

@app.post('/criar_conta')
async def criar_conta(dados: UsuarioSchema):
    cursor = conexao.cursor()
    # 1. Verifica se o e-mail já existe
    cursor.execute(
        "SELECT * FROM usuario WHERE email = ?",
        (dados.email,))
    usuario = cursor.fetchone()
    
    if usuario:
        cursor.close()
        return {"erro": "Este e-mail já está cadastrado."}
    else:
        cursor.execute(
        "INSERT INTO usuario (nome, email, senha) VALUES (?, ?, ?)",
        (dados.nome, dados.email, dados.senha))
    conexao.commit()
    cursor.close()
    return {'status': 'Conta criada com sucesso'}  
"""
    
  