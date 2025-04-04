"""
2. Conceitos Básicos

    Atributos: Definindo e acessando atributos de uma classe.
    
"""

#Exemplo Prático: Gerenciamento de Jogadores em um Time de Futebol

#Descrição:

#Imagine que você está desenvolvendo um software simples para gerenciar 
#jogadores em um time de futebol. Cada jogador tem um nome, posição, número 
#da camisa e quantidade de gols marcados na temporada.

#1. Definição da Classe Jogador:

# Define a classe Jogador
class Jogador:
    
    # Método construtor da classe
    def __init__(self, nome, posicao, numero_camisa, gols=0):
        
        self.nome = nome              # Atribui o valor do parâmetro 'nome' ao atributo 'nome' do objeto
        self.posicao = posicao        # Atribui o valor do parâmetro 'posicao' ao atributo 'posicao' do objeto
        self.numero_camisa = numero_camisa  # Atribui o valor do parâmetro 'numero_camisa' ao atributo 'numero_camisa' do objeto
        self.gols = gols              # Atribui o valor do parâmetro 'gols' ao atributo 'gols' do objeto (com valor padrão 0 se não for fornecido)

        
#2. Instanciando e Acessando Atributos:

# Instanciando jogadores

# Cria uma nova instância da classe Jogador com os atributos
# nome="Roberto", posicao="Atacante" e numero_camisa=9
jogador1 = Jogador("Roberto", "Atacante", 9)

# Cria uma nova instância da classe Jogador com os atributos 
# nome="Carlos", posicao="Goleiro" e numero_camisa=1
jogador2 = Jogador("Carlos", "Goleiro", 1)


# Acessando atributos

# Utiliza a função print para mostrar os atributos nome, posicao e 
# numero_camisa do jogador1 em um formato legível
print(f"{jogador1.nome} é um {jogador1.posicao} e usa a camisa número {jogador1.numero_camisa}.")

# Utiliza a função print para mostrar os atributos nome, posicao e 
# numero_camisa do jogador2 em um formato legível
print(f"{jogador2.nome} é um {jogador2.posicao} e usa a camisa número {jogador2.numero_camisa}.")


# Suponha que Roberto marcou um gol, vamos atualizar o atributo gols dele

# Incrementa em 1 o número de gols do jogador1 (Roberto)
jogador1.gols += 1

# Incrementa novamente em 1 o número de gols do jogador1 (Roberto)
jogador1.gols += 1

# Mais um incremento de 1 gol para jogador1 (Roberto)
jogador1.gols += 1

# Continua incrementando o número de gols de jogador1 (Roberto)
jogador1.gols += 1

# E mais uma vez, incrementa em 1 o número de gols de jogador1 (Roberto)
jogador1.gols += 1


# Utiliza a função print para mostrar os atributos nome, posicao e 
# numero_camisa do jogador1 em um formato legível
# Utiliza a função print para mostrar a quantidade de gols que jogador1 (Roberto) marcou na temporada
print(f"{jogador1.nome} marcou {jogador1.gols} gol(s) nesta temporada.")


"""
O exemplo acima ajuda a entender como definir atributos em uma classe, 
como instanciar objetos dessa classe e como acessar e modificar esses atributos
diretamente.
"""
print()

"""
Exercício - Informações de Frutas em uma Mercearia

Em uma mercearia, várias frutas são vendidas, e você deseja criar um 
sistema simples para gerenciar as informações sobre essas frutas.

Objetivos:

    1. Definir uma classe chamada Fruta.
    2. Instanciar um ou mais objetos desta classe.
    3. Acessar e exibir os atributos dos objetos instanciados.

Instruções:

    1. Crie uma classe chamada Fruta com os seguintes atributos:
        - nome: o nome da fruta (ex: "Maçã", "Banana").
        - preco_por_kg: o preço da fruta por quilograma.
        - quantidade_em_estoque: a quantidade da fruta em estoque (em quilogramas).

    2. Instancie pelo menos duas frutas diferentes, fornecendo valores específicos para seus atributos.

    3. Acesse os atributos das frutas instanciadas e exiba suas informações de forma organizada, como:
    
        Nome da Fruta: [nome da fruta]
        Preço por Kg: [preço da fruta por quilograma]
        Quantidade em Estoque: [quantidade da fruta em estoque]

"""


#Solução:

"""
 1. Crie uma classe chamada Fruta com os seguintes atributos:
        - nome: o nome da fruta (ex: "Maçã", "Banana").
        - preco_por_kg: o preço da fruta por quilograma.
        - quantidade_em_estoque: a quantidade da fruta em estoque (em quilogramas).
"""
# Definindo a classe Fruta
class Fruta:
    
    # Método inicializador da classe Fruta
    def __init__(self, nome, preco_por_kg, quantidade_em_estoque):
        
        self.nome = nome  # Atribui o valor do parâmetro 'nome' ao atributo 'nome' da instância
        self.preco_por_kg = preco_por_kg  # Atribui o valor do parâmetro 'preco_por_kg' ao atributo 'preco_por_kg' da instância
        self.quantidade_em_estoque = quantidade_em_estoque  # Atribui o valor do parâmetro 'quantidade_em_estoque' ao atributo 'quantidade_em_estoque' da instância
        
    """
    3. Acesse os atributos das frutas instanciadas e exiba suas informações de forma organizada, como:
    
        Nome da Fruta: [nome da fruta]
        Preço por Kg: [preço da fruta por quilograma]
        Quantidade em Estoque: [quantidade da fruta em estoque]
    """
    
    # Definição do método para exibir informações da fruta
    def exibir_info(self):
        
        # Imprime o nome da fruta, acessando o atributo 'nome' da instância atual
        print(f"Nome da Fruta: {self.nome}")

        # Imprime o preço por Kg da fruta, formatando para duas casas decimais
        print(f"Preço por Kg: R${self.preco_por_kg:.2f}")

        # Imprime a quantidade em estoque da fruta, acessando o atributo 'quantidade_em_estoque' da instância atual
        print(f"Quantidade em Estoque: {self.quantidade_em_estoque}kg")



# 2. Instancie pelo menos duas frutas diferentes, fornecendo valores específicos para seus atributos.

# Instanciando duas frutas diferentes
maca = Fruta("Maçã", 2.5, 10)
banana = Fruta("Banana", 1.8, 15)

maca.exibir_info()
print("-------------")
banana.exibir_info()