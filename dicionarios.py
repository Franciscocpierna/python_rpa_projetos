print("Criação de um dicionário chamado 'livro' com três pares chave-valor") 
livro = {
    "titulo": "1984",           # Chave 'titulo' com o valor "1984"
    "autor": "George Orwell",   # Chave 'autor' com o valor "George Orwell"
    "ano": 1949                 # Chave 'ano' com o valor 1949
}

# Imprime o valor associado à chave 'titulo' do dicionário 'livro'
print(livro["titulo"])  # Saída esperada: 1984
print(livro.get("ano"))

contatos = {
    "Alice": "555-1234",   # Chave 'Alice' com o valor "555-1234"
    "Bob": "555-5678"    # Chave 'Bob' com o valor "555-5678"
}

# Imprime o valor associado à chave 'Alice' no dicionário 'contatos'
print(contatos["Alice"])  # Saída esperada: 555-1234

# Criação de um dicionário chamado 'pessoa' com quatro pares chave-valor
pessoa = {
    "nome": "Maria",                        # Chave 'nome' com o valor "Maria"
    "idade": 30,                            # Chave 'idade' com o valor numérico 30
    "profissao": "Engenheira",              # Chave 'profissao' com o valor "Engenheira"
    "nacionalidade": "Brasileira"           # Chave 'nacionalidade' com o valor "Brasileira"
}

# Imprime o dicionário completo 'pessoa'
print(pessoa)
familia = {
    "geral": "familia Barnabe",
    # Subdicionário para o "pai"
    "pai": {
        "nome": "Roberto",  # Chave 'nome' com o valor "Roberto"
        "idade": 50         # Chave 'idade' com o valor numérico 50
    },
    
    # Subdicionário para a "mae"
    "mae": {
        "nome": "Clara",    # Chave 'nome' com o valor "Clara"
        "idade": 48         # Chave 'idade' com o valor numérico 48
    },
    
    # Subdicionário para o "filho"
    "filho": {
        "nome": "Pedro",    # Chave 'nome' com o valor "Pedro"
        "idade": 22         # Chave 'idade' com o valor numérico 22
    }
}


print(familia["pai"]["nome"])  # Saída: Roberto
#No exemplo acima, cada membro da família tem seu próprio dicionário 
#contendo informações sobre ele. Para acessar informações específicas, 
#você segue a cadeia de chaves.
print(familia["filho"]["idade"])
print()
print(familia["geral"])
print(familia.get("geral"))
print(familia) 
print(familia["mae"].get("nome"))


universidade = {
    "nome": "Universidade Federal",      # Chave 'nome' com o valor "Universidade Federal"
    "localidade": {
        "cidade": "Rio de Janeiro",      # Chave 'cidade' dentro do subdicionário com o valor "Rio de Janeiro"
        "bairro": "Centro"               # Chave 'bairro' dentro do subdicionário com o valor "Centro"
    }
}


print(universidade["nome"])  # Saída: Universidade Federal
print(universidade["localidade"]["cidade"])  # Saída: Rio de Janeiro

"""
Operações Básicas com Dicionários
        Adicionando itens
        Atualizando itens
        Removendo itens (del, pop(), popitem())
        Copiando dicionários (copy(), dict())
"""
produto = {
    "id": 12345,                  # Chave 'id' com o valor numérico 12345
    "nome": "Camisa Polo",        # Chave 'nome' com o valor "Camisa Polo"
    "cor": "Vermelho",            # Chave 'cor' com o valor "Vermelho"
    "preco": 49.90,               # Chave 'preco' com o valor numérico 49.90
    "estoque": 100                # Chave 'estoque' com o valor numérico 100
}
print()
print("1. Adicionando itens ao dicionário 'produto'")

# Adicionando a chave 'marca' com o valor "FashionBrand"
produto["marca"] = "FashionBrand"
#produto["cor"]="Azul" #mudando a cor
# Adicionando a chave 'desconto' com o valor numérico 10 (representa uma porcentagem)
produto["desconto"] = 10

# Imprimindo o dicionário 'produto' após a adição dos novos itens
print("Após adicionar itens:", produto)

print(" 3. Removendo itens (del, pop(), popitem())")
del produto["desconto"]  # remove o item "desconto" do dicionário
print("Após retirada do desconto:com del", produto)

print("Usando pop() para remover item por chave")
cor_removida = produto.pop("cor")
print(f"\nCor removida: {cor_removida}")
print("Após retirada cor :com pop('cor')", produto)

print("Usando popitem() para remover o último item inserido")
# 
item_removido = produto.popitem()
print("Item removido:", item_removido)

print("\nApós remover itens:", produto)

print("4. Copiando dicionários (copy(), dict()")
produto_copia_1 = produto.copy()

# Método dict()
produto_copia_2 = dict(produto)

print("\nCópias do produto:")
print("Cópia 1:", produto_copia_1)
print("Cópia 2:", produto_copia_2)
