import pyodbc

dados_conexao = (
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=DESKTOP-MIFM7EL\\SQLEXPRESS;'
    'Database=Login;'
    'Trusted_Connection=yes;'
)

conexao = pyodbc.connect(dados_conexao)
print('Sucedido')

cursor = conexao.cursor()