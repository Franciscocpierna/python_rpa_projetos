import pyodbc

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

#Inserindo informações no banco de dados
dados_usuario = ("Jose", "987")
cursor.execute("INSERT INTO Usuarios (Nome, Senha) Values (?, ?)", dados_usuario)
conexao.commit() #Gravando no BD

#Selecionando a tabela do banco de dados
cursor.execute("Select * From Usuarios")

#Passar os dados para a variavel
valores = cursor.fetchall()

print(valores)

#Fechar o cursor e a conexao
cursor.close()
conexao.close()