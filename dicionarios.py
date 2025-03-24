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
if "id" in produto:
    print("o produto tem em produtos ", produto["id"])
print()    

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

#Dicionário fornecido:

estacionamento = {
    "A1": {
        "marca": "Toyota",
        "modelo": "Corolla",
        "dono": "Sr. Silva"
    },
    "B2": {
        "marca": "Honda",
        "modelo": "Civic",
        "dono": "Dona Maria"
    },
    "C3": {
        "marca": "Ford",
        "modelo": "Mustang",
        "dono": "Sr. Jorge"
    }
}

"""
Onde as chaves (A1, B2, C3) representam as vagas no estacionamento.

Instruções:

    1. Acesse e imprima o modelo do carro estacionado na vaga "B2".
    
    2. Altere o dono do carro na vaga "A1" para "Sra. Lúcia".
    
    3. Adicione um novo carro na vaga "D4" com as seguintes 
        informações: marca "Chevrolet", modelo "Onix", dono "Sr. Roberto".
        
    4. Acesse e imprima a marca do carro que agora pertence à "Sra. Lúcia".

"""
print("\nnome do estacionamento")
#print(estacionamento["nome"])
print("\nAcesse e imprima o modelo do carro estacionado na vaga B2")

print(estacionamento["B2"])
print("\nmodelo do carro C3")
print(estacionamento["C3"]["modelo"])
print()
print(estacionamento["A1"])
print("\nAltere o dono do carro na vaga A1 para Sra. Lúcia")

estacionamento["A1"]["dono"]="Sra. Lúcia"
print(estacionamento["A1"])
print('\nAdicione um novo carro na vaga "D4" com as seguintes informações: marca "Chevrolet", modelo "Onix", dono "Sr. Roberto"')
estacionamento["D4"] = {
        "marca": "Chevrolet",
        "modelo": "Onix",
        "dono": "Sr. Roberto"              
}
print("\n",estacionamento)
print("\nAcesse e imprima a marca do carro que agora pertence à 'Sra. Lúcia'")


    

for vaga, carro in estacionamento.items():
        # Verifica se o campo "dono" do dicionário 'carro' é igual a "Sra. Lúcia"
    if carro["dono"] == "Sra. Lúcia":      
        # Imprime a marca do carro que pertence à Sra. Lúcia
        print(f"Marca do carro da Sra. Lúcia: {carro['marca']}")
        
        # Encerra o loop após encontrar o carro da Sra. Lúcia
        break
  
'''estacionamento = {
    "nome": "estacionamento do sr Joaquim",
    "vagas": {
        "A1": {...},
        "B2": {...},
        "C3": {...}
    }
}





for vaga, carro in estacionamento["vagas"].items():
'''
estacionamento1 = {
    "nome": "estacionamento do sr Joaquim",
    "vagas":{
      "A1":{  
        "marca": "Toyota",
        "modelo": "Corolla",
        "dono": "Sra. Lúcia"
        },
      "B2": {
        "marca": "Honda",
        "modelo": "Civic",
        "dono": "Dona Maria"
       },
      "C3": {
        "marca": "Ford",
        "modelo": "Mustang",
        "dono": "Sr. Jorge"
      }
   } 
}

print("versão estacionamento1")
for vaga, carro in estacionamento1["vagas"].items():
     # Verifica se o campo "dono" do dicionário 'carro' é igual a "Sra. Lúcia"
    if carro["dono"] == "Sra. Lúcia":      
        # Imprime a marca do carro que pertence à Sra. Lúcia
        print(f"Marca do carro da Sra. Lúcia: {carro['marca']}")
        
        # Encerra o loop após encontrar o carro da Sra. Lúcia
        break
  
print("nome do estacionamento", estacionamento1['nome'])