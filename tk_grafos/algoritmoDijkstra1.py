"""
Exercício Caminho mais curto usando o Algoritmo de Dijkstra

Contexto:

Você recebeu um mapa de uma cidade que mostra diferentes pontos
de interesse conectados por estradas. Cada estrada tem uma distância
associada, que representa a distância em quilômetros entre dois pontos de interesse.

Mapa da Cidade:

    Pontos de interesse: A, B, C, D, E.
    Estradas e suas distâncias:
        A - B: 50 km
        A - C: 30 km
        B - D: 40 km
        C - D: 20 km
        C - E: 60 km
        D - E: 70 km

Tarefa:
Utilize o algoritmo de Dijkstra para determinar o caminho mais 
curto entre o ponto A e o ponto E. Após determinar o caminho, visualize
o mapa da cidade e destaque o caminho encontrado.

Requisitos:

    - Crie um grafo ponderado que represente o mapa da cidade.
    
    - Adicione vértices e arestas ao grafo com os respectivos pesos (distâncias).
    
    - Aplique o algoritmo de Dijkstra para determinar o caminho mais curto de A para E.
    
    - Imprima o caminho mais curto e sua distância total.
    
    - Visualize o mapa da cidade em forma de um gráfico, mostrando os pontos
        de interesse, as estradas e suas distâncias.
    
    - No gráfico, destaque o caminho mais curto encontrado entre A e E.

"""


# Importando a biblioteca networkx para manipulação e análise de grafos.
# Importando a biblioteca matplotlib.pyplot para visualização dos grafos.
import networkx as nx
import matplotlib.pyplot as plt

# Criando um grafo ponderado, onde as arestas têm pesos associados.
grafo_ponderado = nx.Graph()

# O grafo_ponderado é uma estrutura de dados que representa um conjunto de 
# vértices (ou nós) e arestas (ou conexões) entre esses vértices.
# Em um grafo ponderado, cada aresta tem um valor associado a ela, chamado de "peso".
# O método add_edge é usado para adicionar uma aresta ao grafo.

# Adiciona uma aresta entre o vértice 'A' e o vértice 'B' com um peso de 50 ao grafo_ponderado.
grafo_ponderado.add_edge('A', 'B', weight=50)

# Adiciona uma aresta entre o vértice 'A' e o vértice 'C' com um peso de 30 ao grafo_ponderado.
grafo_ponderado.add_edge('A', 'C', weight=30)

# Adiciona uma aresta entre o vértice 'B' e o vértice 'D' com um peso de 40 ao grafo_ponderado.
grafo_ponderado.add_edge('B', 'D', weight=40)

# Adiciona uma aresta entre o vértice 'C' e o vértice 'D' com um peso de 20 ao grafo_ponderado.
grafo_ponderado.add_edge('C', 'D', weight=20)

# Adiciona uma aresta entre o vértice 'C' e o vértice 'E' com um peso de 60 ao grafo_ponderado.
grafo_ponderado.add_edge('C', 'E', weight=60)

# Adiciona uma aresta entre o vértice 'D' e o vértice 'E' com um peso de 70 ao grafo_ponderado.
grafo_ponderado.add_edge('D', 'E', weight=70)

# O algoritmo de Dijkstra é utilizado para encontrar o caminho mais curto em
# grafos ponderados, considerando os pesos das arestas.
# NetworkX, uma biblioteca Python, fornece uma implementação deste
# algoritmo através da função "shortest_path".

# Usando a função shortest_path para determinar a sequência de vértices 
# no caminho mais curto de 'A' a 'E' no grafo_ponderado.
# O argumento "weight" especifica que o atributo 'weight' 
# das arestas deve ser usado como peso para calcular o caminho.
caminho_mais_curto = nx.shortest_path(grafo_ponderado, 'A', 'E', weight='weight')

# Utilizando a função shortest_path_length para determinar a soma 
# dos pesos das arestas no caminho mais curto de 'A' a 'E'.
# Assim como anteriormente, o argumento "weight" indica que o 
# atributo 'weight' das arestas deve ser considerado.
distancia_mais_curta = nx.shortest_path_length(grafo_ponderado, 'A', 'E', weight='weight')

# Imprimindo o resultado do caminho mais curto e sua distância (soma dos pesos das arestas) total.
print(f"Caminho mais curto de A para E: {caminho_mais_curto}")
print(f"Distância total: {distancia_mais_curta}")

# A função "spring_layout" de NetworkX utiliza o algoritmo 
# Fruchterman-Reingold para gerar uma disposição espacial dos vértices.
# Esse algoritmo simula uma série de molas entre os vértices, fazendo 
# com que vértices conectados se atraiam e os não conectados se repelem.
# O resultado é uma disposição que tende a destacar a estrutura do grafo.
posicoes = nx.spring_layout(grafo_ponderado)

# A função "draw" de NetworkX é utilizada para visualizar o grafo.
# - "posicoes" determina onde cada vértice será posicionado no gráfico.
# - "with_labels=True" indica que queremos que os nomes dos vértices sejam exibidos.
# - "node_size=500" define o tamanho de cada vértice.
# - "node_color='lightblue'" especifica a cor dos vértices.
nx.draw(grafo_ponderado, posicoes, with_labels=True, node_size=500, node_color='lightblue')


# Desenhando os rótulos (pesos) nas arestas do grafo.
# nx.draw_networkx_edge_labels(grafo_ponderado, posicoes, edge_labels={(u, v): grafo_ponderado[u][v]['weight'] for u, v in grafo_ponderado.edges()})


# Inicializando um dicionário vazio chamado 'rotulos_arestas'. 
# Esse dicionário irá armazenar os pares de vértices das arestas 
# como chaves e os respectivos pesos como valores.
rotulos_arestas = {}

# Começando a iteração por todas as arestas do grafo ponderado. 
# Cada aresta é representada por um par de vértices (u, v).
for u, v in grafo_ponderado.edges():
    
    # Para cada aresta, obtemos o peso associado a ela no grafo ponderado.
    # O peso é obtido acessando o atributo 'weight' da aresta entre os vértices 'u' e 'v'.
    # Esse peso é então armazenado no dicionário 'rotulos_arestas', 
    # usando o par de vértices (u, v) como chave e o peso como valor.
    rotulos_arestas[(u, v)] = grafo_ponderado[u][v]['weight']

# Após coletar todos os rótulos das arestas, usamos a 
# função 'draw_networkx_edge_labels' para desenhar os rótulos.
# Passamos o grafo ponderado, as posições previamente definidas
# dos vértices ('posicoes') e o dicionário de rótulos das arestas.
# Dessa forma, a visualização do grafo mostrará os pesos das arestas
# ao lado de cada aresta correspondente.
nx.draw_networkx_edge_labels(grafo_ponderado, posicoes, edge_labels=rotulos_arestas)


# Destacando no gráfico o caminho mais curto encontrado, 
# desenhando-o com cor vermelha e espessura maior.
# A função 'zip' é usada para combinar dois ou mais 
# iteráveis. Aqui, estamos combinando o 'caminho_mais_curto' com uma versão
# deslocada de si mesmo (caminho_mais_curto[1:]). O objetivo é 
# criar pares consecutivos de vértices que representam as arestas 
# no caminho mais curto.
# Por exemplo, se caminho_mais_curto = ['A', 'B', 'C'], o resultado 
# do 'zip' será [('A', 'B'), ('B', 'C')], que representa as arestas
# do caminho mais curto.
arestas_caminho = list(zip(caminho_mais_curto, caminho_mais_curto[1:]))

# Agora, usando a função 'draw_networkx_edges', desenhamos apenas 
# as arestas que fazem parte do caminho mais curto no grafo.
# 'grafo_ponderado' é o grafo onde queremos visualizar o caminho, 
# 'posicoes' determina a posição de cada vértice no gráfico.
# 'edgelist=arestas_caminho' indica que queremos desenhar apenas as 
# arestas listadas em 'arestas_caminho'.
# 'edge_color='r'' dá a cor vermelha para essas arestas, destacando-as no grafo.
# 'width=2' define a largura dessas arestas para ser um pouco mais espessa, 
# tornando-as mais proeminentes.
nx.draw_networkx_edges(grafo_ponderado, posicoes, edgelist=arestas_caminho, edge_color='r', width=2)

# Exibindo o gráfico.
plt.show()

"""
Pontos de interesse: A, B, C, D, E.
    Estradas e suas distâncias:
        A - B: 50 km
        A - C: 30 km
        B - D: 40 km
        C - D: 20 km
        C - E: 60 km
        D - E: 70 km
"""
print()