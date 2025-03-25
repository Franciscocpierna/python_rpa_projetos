"""
Dicionários e Funções
        Passando dicionários como argumentos para funções
        Retornando dicionários de funções
"""

print("Exemplo Prático: Dicionários e Funções")
#Vamos criar um sistema simples de gestão de perfis de usuários:

#1. Passando dicionários como argumentos para funções:
#Suponha que temos um dicionário representando um perfil de usuário e 
#queremos exibir este perfil.

#2. Retornando dicionários de funções:
#Vamos criar uma função que pode criar um novo perfil de usuário 
#com base em informações fornecidas.

# Definição do dicionário do perfil do usuário

# Iniciando um dicionário chamado 'usuario'

usuario = {
    "nome": "João",
    "idade": 25,
    "email": "joao@email.com"
}

# 1. Passando dicionários como argumentos para funções

# Define uma função chamada 'exibir_perfil' que aceita um dicionário 'perfil' como parâmetro
def exibir_perfil(perfil):
    
    # Para cada par de chave-valor no dicionário 'perfil'
    for chave, valor in perfil.items():
        
        # Imprime a chave (formatada com a primeira letra maiúscula) e seu respectivo valor
        print(f"{chave.title()}: {valor}")

# Chama a função 'exibir_perfil' passando o dicionário 'usuario' como argumento
exibir_perfil(usuario)

# 2. Retornando dicionários de funções

# Definindo uma função chamada 'criar_perfil'
def criar_perfil(nome, idade, email):
    
    """Retorna um dicionário representando um perfil de usuário"""
    
    print("\nCriando e retornando um dicionário com as informações do perfil do usuário")
    return {
        "nome": nome,   # Chave: "nome", Valor: valor da variável 'nome'
        "idade": idade, # Chave: "idade", Valor: valor da variável 'idade'
        "email": email  # Chave: "email", Valor: valor da variável 'email'
    }

# Criando um novo perfil de usuário usando a função 'criar_perfil'
novo_usuario = criar_perfil("Ana", 30, "ana@email.com")

print("\nNovo Perfil Criado:")
print("novo_usuario = criar_perfil('Ana', 30, 'ana@email.com')")
# Exibindo o perfil do novo usuário
exibir_perfil(novo_usuario)


def registrar_livro(titulo, autor, ano):
   
      return{
       "titulo": "1984",
       "autor":  "George Orwel",
       "ano":  1949  
       
   }
livro = registrar_livro("1984", "George Orwell", 1949)  
print(livro)
print()
def exibir_livro(livro_dicionario):
    for chave, valor in livro_dicionario.items():
          print(f"{chave}: {valor}")
    
exibir_livro(livro)    
print("\nBoas Práticas")    
livros = {
    "978-1234567890": {               # Chave: ISBN do livro "A Arte da Guerra"
        "titulo": "A Arte da Guerra", # Chave: "titulo", Valor: "A Arte da Guerra"
        "autor": "Sun Tzu",           # Chave: "autor", Valor: "Sun Tzu"
        "ano_publicacao": 500         # Chave: "ano_publicacao", Valor: 500 (ano aproximado de publicação)
    },
    "978-0987654321": {               # Chave: ISBN do livro "1984"
        "titulo": "1984",             # Chave: "titulo", Valor: "1984"
        "autor": "George Orwell",     # Chave: "autor", Valor: "George Orwell"
        "ano_publicacao": 1949        # Chave: "ano_publicacao", Valor: 1949
    }
}
print(livros)    

#2. Cuidados com tipos de chaves mutáveis

#Evite usar tipos mutáveis, como listas, como chaves de dicionário. 
#Eles podem causar comportamento inesperado e erros, pois, se a lista 
#for alterada depois de ser usada como chave, ela poderá interferir no 
#mapeamento do dicionário.


ruim = {}
lista_chave = [1, 2, 3]
#ruim[lista_chave] = "valor"  # Isso vai lançar um TypeError
"""
Aqui, tentamos usar uma lista como chave para o dicionário ruim. Se 
você descomentar a linha #ruim[lista_chave] = "valor", obterá um TypeError, 
pois listas são mutáveis e não podem ser usadas como chaves de dicionário.
"""
print("Bom")
bom = {}
tupla_chave = (1, 2, 3)
bom[tupla_chave] = "valor"  # Isso é perfeitamente válido

print(bom)

"""
Neste exemplo, usamos uma tupla (que é um tipo imutável) como 
chave para o dicionário bom. As tuplas são "hashable" e podem ser 
usadas como chaves de dicionário sem problemas.
"""


#3. Dicionários vs. Listas: quando usar cada um

#Use listas quando a ordem dos itens for importante e quando 
#você precisar de uma coleção ordenada de itens. Listas são ótimas 
#para sequências onde os itens são frequentemente recuperados por 
#sua posição na coleção.

filmes_favoritos = ["Pulp Fiction", "Cidade de Deus", "O Poderoso Chefão"]

# Recuperando o primeiro filme favorito
primeiro_filme = filmes_favoritos[0]

print(primeiro_filme)


#Use dicionários quando você precisar associar valores a chaves 
#únicas e desejar uma recuperação eficiente por chave. Dicionários 
#são ideais para armazenar e recuperar dados de forma não sequencial.

# Inicializando um dicionário chamado 'contatos'.
contatos = {
    "Alice": "555-1234",  # Adicionando uma chave "Alice" com valor "555-1234" ao dicionário.
    "Bob": "555-5678"     # Adicionando uma chave "Bob" com valor "555-5678" ao dicionário.
}

# Recuperando o número de telefone de Alice
telefone_alice = contatos["Alice"]

print(telefone_alice)
