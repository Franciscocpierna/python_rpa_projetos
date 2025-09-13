"""
Grafos
            
            Algoritmos Clássicos

                Algoritmo de Dijkstra para Caminhos Mais Curtos
                

    O algoritmo de Dijkstra é usado para encontrar o caminho mais curto de 
um nó (vértice) de origem para todos os outros nós em um grafo ponderado e 
direcionado, onde todas as arestas têm peso não negativo. É amplamente 
utilizado em aplicações como sistemas de roteamento de redes de 
computadores, sistemas de navegação por GPS, entre outros.

Vamos considerar um exemplo prático:

Imagine que temos uma cidade com várias interseções (nós) e ruas que as 
conectam (arestas). Cada rua tem uma distância associada a ela (peso da 
aresta). Suponha que queremos encontrar a rota mais curta do ponto A para o 
ponto B na cidade.

Aqui está uma representação simplificada:

A - 4 - B - 2 - D
|       |       |
2       1       3
|       |       |
C - 5 - E       F

No grafo acima:

    A, B, C, D, E, F são interseções (nós).
    
    Os números representam a distância entre as interseções (peso das arestas).

    Se quisermos encontrar a rota mais curta de A para F, podemos 
usar o algoritmo de Dijkstra.

Aqui está uma implementação simples usando a biblioteca networkx:
"""

# Importando a biblioteca networkx para manipulação e análise de grafos.
import networkx as nx

# Criando um grafo direcionado (DiGraph). Grafos direcionados 
# são aqueles onde as arestas têm uma direção específica, de um vértice 
# origem para um vértice destino.
G = nx.DiGraph()

# Adicionando arestas ao grafo junto com seus pesos.
# A função add_edge adiciona uma aresta direcionada do 
# primeiro vértice para o segundo com um atributo de peso especificado.
G.add_edge('A', 'B', weight=4)   # Aresta de A para B com peso 4
G.add_edge('A', 'C', weight=2)   # Aresta de A para C com peso 2
G.add_edge('B', 'E', weight=1)   # Aresta de B para E com peso 1
G.add_edge('B', 'D', weight=2)   # Aresta de B para D com peso 2
G.add_edge('C', 'E', weight=5)   # Aresta de C para E com peso 5
G.add_edge('D', 'F', weight=3)   # Aresta de D para F com peso 3
G.add_edge('E', 'B', weight=1)   # Aresta de E para B com peso 1

# Utilizando o algoritmo de Dijkstra para determinar o caminho mais curto entr
# e os vértices A e F.
# A função single_source_dijkstra retorna a distância mínima e o 
# caminho mais curto de um vértice de origem para um destino.
distancia, caminho = nx.single_source_dijkstra(G, 'A', 'F')

# Imprimindo o caminho mais curto determinado pelo algoritmo de Dijkstra de A para F.
print(f"Caminho mais curto de A para F: {caminho}")

# Imprimindo a distância total (soma dos pesos) do caminho mais curto de A para F.
print(f"Distância total: {distancia}")

"""
A - 4 - B - 2 - D
|       |       |
2       1       3
|       |       |
C - 5 - E       F
"""
print()



"""
Vamos considerar um exemplo relacionado ao transporte aéreo.

Imagine que temos várias cidades e voos entre elas. Cada voo tem um custo 
associado. Queremos descobrir a maneira mais barata de voar de uma 
cidade (origem) para outra (destino), mesmo que isso signifique fazer escalas em outras cidades.

Aqui está uma representação simplificada:

Rio - 300 - SP - 150 - BH
  |          |         |
  200       250        80
  |          |         |
      Salvador - 100 - Brasília


No grafo acima:

    Rio, SP, BH, Salvador, Brasília são cidades (nós).
    Os números representam o custo dos voos entre as cidades (peso das arestas).

Se quisermos encontrar a maneira mais barata de voar do Rio para 
Brasília, podemos usar o algoritmo de Dijkstra.

Aqui está a implementação usando a biblioteca networkx:
"""

# Importando a biblioteca networkx para manipulação e análise de grafos.
import networkx as nx

# Criando um grafo direcionado (DiGraph). Grafos direcionados são 
# aqueles onde as arestas têm uma direção específica, de um vértice 
# origem para um vértice destino.
G = nx.DiGraph()

# Adicionando arestas ao grafo junto com seus custos.
# A função add_edge adiciona uma aresta direcionada do primeiro 
# vértice para o segundo com um atributo de peso especificado. Neste 
# contexto, os pesos representam os custos de viajar entre cidades.
G.add_edge('Rio', 'SP', weight=300)         # Rota do Rio para SP com custo de R$300
G.add_edge('Rio', 'Salvador', weight=200)   # Rota do Rio para Salvador com custo de R$200
G.add_edge('SP', 'Salvador', weight=250)    # Rota de SP para Salvador com custo de R$250
G.add_edge('SP', 'BH', weight=150)          # Rota de SP para BH com custo de R$150
G.add_edge('BH', 'Brasília', weight=80)     # Rota de BH para Brasília com custo de R$80
G.add_edge('Salvador', 'Brasília', weight=100) # Rota de Salvador para Brasília com custo de R$100

# Utilizando o algoritmo de Dijkstra para determinar a rota mais barata entre o Rio e Brasília.
# A função single_source_dijkstra retorna o custo mínimo e a rota mais 
# barata de um ponto de origem para um destino.
custo, rota = nx.single_source_dijkstra(G, 'Rio', 'Brasília')

# Imprimindo a rota mais barata determinada pelo algoritmo de Dijkstra do Rio para Brasília.
print(f"Rota mais barata do Rio para Brasília: {rota}")

# Imprimindo o custo total (soma dos pesos, ou custos) da rota mais barata do Rio para Brasília.
print(f"Custo total: R${custo}")

"""
Rio - 300 - SP - 150 - BH
  |          |         |
  200       250        80
  |          |         |
      Salvador - 100 - Brasília
      
Quando executamos o código acima, obtemos:

Rota mais barata do Rio para Brasília: ['Rio', 'Salvador', 'Brasília']
Custo total: R$300

O algoritmo mostra que a maneira mais barata de voar do Rio para Brasília 
é fazendo escala em Salvador, com um custo total de R$300.
"""
print()