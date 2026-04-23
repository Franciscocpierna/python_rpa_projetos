# Obtendo Dados - Parte 1
### Banco de Dados
# Como cientísta de dados, você interagirá com bancos de dados constantemente. Por esse motivo, você deve saber como *ler, buscar, criar e escrever* em diferentes bancos de dados.

# O primeiro passo é conhecer a linguagem SQL (Structured Query Language).

# No curso **Python Profissional - na Udemy**, existe um módulo específico sobre Banco de Dados, onde mostro como interagir com os principais bancos de dados comerciais e também apresento um curso básico de SQL.

# Para mostrar mais um opção, vamos mostrar nessa primeira parte do curso como interarir com banco de dados utilizando um Pacote/Biblioteca específica do Python conhecida como **SQLAlchemy** (uma caixa de ferramentas para manipulação de bancos de dados).

# Vamos fazer todas as interações com o banco de dados SQLite... mas tudo pode ser reproduzido com outras bases de dados, modificando apenas o trecho de "estabelecendo a conexão com o banco de dados".

# Vamos começar...

# Para instalar o pacote você pode utilizar o PIP ou o CONDA (do ambiente Anaconda)
# Primeira Opção (PIP):
# pip install -q sqlalchemy==2.0.25
# Segunda Opção (CONDA):
#! conda install -c anaconda sqlalchemy

# Uma vez instalado, basta realizar a importação
import sqlalchemy as db

# Vamos verificar a versão
print(db.__version__)

### Estabelecendo uma Conexão com o Banco de Dados (engine)



# Para estabelecer uma conexão, você pode seguir o guia (documentação oficial) do pacote sqlalchemy disponível 
# no seguinte link: [Documentação Oficial - Alchemy - Engines](https://docs.sqlalchemy.org/en/20/core/engines.html)

# Criando uma nova Engine
engine = db.create_engine("sqlite:///db//dados.db")

# Criando uma nova conexão
bd = engine.connect()


try:
 # Criando uma Nova Tabela
 sql = db.text("CREATE TABLE clientes (nome VARCHAR(255), endereco VARCHAR(255))")

    # 2. Tenta executar # Executando a expressão SQL

 bd.execute(sql)
 bd.commit()
 print("Tabela criada com sucesso!")

except Exception as e:
    # 3. Verifica se o erro é porque a tabela já existe
    if "already exists" in str(e):
        print("Aviso: A tabela 'clientes' já existe. Continuando...")
    else:
        # Se for outro erro (ex: erro de sintaxe), ele avisa
        print(f"Ocorreu um erro diferente: {e}")

#Verificando o nome da tabela e fechando a conexão
inspetor = db.inspect(engine)
print("Nome da Tabela: ", inspetor.get_table_names())
bd.close()


# Abrindo novamente a conexão...
engine = db.create_engine("sqlite:///db//dados.db")
conexao = engine.connect()

try:
   # Executando expressão SQL  de inserção de registros
   sql = db.text("INSERT INTO clientes (nome, endereco) VALUES ('Piva Jr', 'Sorocaba, SP')")
   conexao.execute(sql)
except  Exception as e:
   print(f"Ocorreu um erro : {e}")
   conexao.close

### Consultando dados de uma Tabela
try:
   # Executando expressão SQL  de inserção de registros
   sql = db.text("SELECT * from clientes")
   conexao.execute(sql)
   resultado = conexao.execute(sql)
   dados = resultado.fetchall()
   if not dados:
       print("a tabela clientes está vazia")   
   else: 
       print("Dados da Tabela: ", dados)
except Exception as e:
   print(f"Ocorreu um erro : {e}")
   # Verifica se a conexão está fechada
if conexao.closed:
    print("A conexão está FECHADA.")
else:
    print("A conexão ainda está ABERTA.")
    

    ### Alterando os dados de uma Tabela

# Expressão sql para alteração de dados...
sql = db.text("UPDATE clientes SET endereco = 'Itu, SP' WHERE endereco = 'Sorocaba, SP'")
conexao.execute(sql)
print("Registro(s) alterados!")
sql = db.text("SELECT * from clientes")
resultado = conexao.execute(sql)
print("Dados da Tabela: ", resultado.fetchall())  

### Deletando um registro de uma Tabela

# Expressão sql de deleção de um registro específico
sql = db.text("DELETE FROM clientes WHERE endereco = 'Itu, SP'")
conexao.execute(sql)
print("Registro deletado!")
sql = db.text("SELECT * from clientes")
resultado = conexao.execute(sql)
print("Dados da Tabela: ", resultado.fetchall())

### Fazendo consultas (SELECT)
# Criando duas novas tabelas e inserindo alguns valores...

sql = db.text("CREATE TABLE IF NOT EXISTS usuarios (id INT, nome VARCHAR(255), produto_id INT)")
conexao.execute(sql)
sql = db.text("INSERT INTO usuarios (id, nome, produto_id) VALUES (1, 'Piva Jr.', 111), (2, 'Adriana', 112), (3, 'Ronny', 113)")
conexao.execute(sql)
sql = db.text("CREATE TABLE IF NOT EXISTS produtos (id INT, nome VARCHAR(255))")
conexao.execute(sql)
sql = db.text("INSERT INTO produtos (id, nome) VALUES (111, 'Apple'), (112, 'Samsung'), (113, 'Sonny')")
conexao.execute(sql)


sql = db.text("SELECT usuarios.nome, produtos.nome FROM usuarios INNER JOIN produtos ON usuarios.produto_id = produtos.id")
resultado = conexao.execute(sql)
meu_resultado = resultado.fetchall()
for produto_comprado in meu_resultado:
    print(produto_comprado)

if conexao.closed:
    print("A conexão está FECHADA.")
else:
    print("A conexão ainda está ABERTA. fechando")
    conexao.close
#Com isso, fizemos uma revisão de acesso a banco de dados, incluindo um novo pacote, SQLAlchemy.

# FIM

     