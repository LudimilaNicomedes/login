#import pyodbc

#dados_conexao = (
    #'Driver={ODBC Driver 17 for SQL Server};'
    #'Server=DESKTOP-MIFM7EL\\SQLEXPRESS;'
    #'Database=Login;'
    #'Trusted_Connection=yes;'
#)

#conexao = pyodbc.connect(dados_conexao)
#print('Sucedido')

#cursor = conexao.cursor()


import json
import os

ARQUIVO_BANCO = "usuarios.json"

def inicializar_banco():
    """Garante que o arquivo JSON exista e tenha a estrutura correta."""
    if not os.path.exists(ARQUIVO_BANCO):
        with open(ARQUIVO_BANCO, "w", encoding="utf-8") as f:
            json.dump([], f)

def buscar_usuario_por_email(email):
    """Busca um usuário pelo e-mail no arquivo JSON."""
    inicializar_banco()
    with open(ARQUIVO_BANCO, "r", encoding="utf-8") as f:
        usuarios = json.load(f)
    for u in usuarios:
        if u["email"] == email:
            return u
    return None

def cadastrar_usuario(nome, email, senha):
    """Salva um novo usuário no arquivo JSON."""
    inicializar_banco()
    with open(ARQUIVO_BANCO, "r", encoding="utf-8") as f:
        usuarios = json.load(f)
        
    novo_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    usuarios.append(novo_usuario)
    
    with open(ARQUIVO_BANCO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)