import pyodbc

print(pyodbc.drivers())

#banco = sqlite3.connect('contaspagar.db')
#cursor = banco.cursor()
#Driver - Drive
#Server - Servidor
#Database - Nome do Banco de Dados
dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db")

#UID - Login
#PWD - Senha

#Criando a conexao
conexao = pyodbc.connect(dadosConexao)

print("Conectado com sucesso!")

#cursor - Ferramenta para exercutar os comandos em SQL
cursor = conexao.cursor()

#Selecionando a tabela do banco de dados
cursor.execute("Select * From Usuarios")

#Passar os dados para a variavel
valores = cursor.fetchall()

print(valores)