"""
Exercício Busca em Largura (BFS)

Objetivo: Utilizar a biblioteca networkx para criar e visualizar grafos.

Descrição:

Você recebeu uma lista de conexões entre vários pontos. Sua tarefa é usar 
a biblioteca networkx para criar um grafo com essas conexões e, em seguida, 
visualizá-lo usando matplotlib.

Dados fornecidos:

    Lista de conexões (arestas):
        F-A
        F-B
        A-B
        A-D
        A-E
        B-C
        B-D

    Posições sugeridas para cada nó no gráfico:
        F: (0, 2)
        A: (-1, 1)
        B: (1, 1)
        D: (0, 0)
        E: (-2, 0)
        C: (2, 0)
        
Grafo

   F
  / \
 A   B
 |\  |\
 E   D C  
"""

# Importando a biblioteca "networkx" com o apelido "nx".
# Essa biblioteca é especializada em criação, manipulação e 
# estudo de estruturas e dinâmicas complexas de redes.
import networkx as nx

# Importando a biblioteca "matplotlib.pyplot" com o apelido "plt".
# Essa biblioteca é utilizada para criar visualizações gráficas.
import matplotlib.pyplot as plt

# Criando um novo grafo não direcionado e armazenando-o na variável "grafo".
grafo = nx.Graph()

# Definindo a lista de arestas que será adicionada ao grafo.
# Cada aresta é representada por um par de nós, indicando uma conexão entre eles.
arestas = [('F', 'A'), ('F', 'B'), ('A', 'B'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('B', 'D')]

# Adicionando todas as arestas definidas anteriormente ao grafo.
grafo.add_edges_from(arestas)

# Definindo um dicionário com as posições que cada nó deve ocupar na visualização do grafo.
# As posições são coordenadas (x, y) que indicam onde cada nó será posicionado no desenho.
# Por exemplo, o nó 'F' será posicionado na coordenada (0, 2).
posicoes = {
    'F': (0, 2),
    'A': (-1, 1),
    'B': (1, 1),
    'D': (0, 0),
    'E': (-2, 0),
    'C': (2, 0)
}

# Define o tamanho da figura que será gerada para a visualização do grafo.
# O tamanho é definido em polegadas, sendo 8 polegadas de largura e 6 de altura.
plt.figure(figsize=(8,6))


# Desenha o grafo na figura definida anteriormente usando as seguintes opções:
# - "grafo": O objeto grafo que foi criado anteriormente.
# - "posicoes": Posições pré-definidas para os nós do grafo.
# - "with_labels=True": Indica que os rótulos (nomes) dos nós serão mostrados.
# - "node_size=1500": Define o tamanho dos nós no desenho.
# - "node_color='lightblue'": Define a cor dos nós como azul claro.
# - "font_size=15": Define o tamanho da fonte dos rótulos dos nós.
# - "width=2": Define a largura das arestas.
# - "edge_color='gray'": Define a cor das arestas como cinza.
nx.draw(grafo, 
        posicoes, 
        with_labels=True, 
        node_size=1500, 
        node_color='lightblue', 
        font_size=15, 
        width=2, 
        edge_color='gray')


# Define o título da figura. O título aparecerá acima da visualização do grafo.
plt.title("Visualização do Grafo")

# Exibe a figura criada. Esta linha é necessária para que a figura apareça.
plt.show()

"""
Lista de conexões (arestas):
        F-A
        F-B
        A-B
        A-D
        A-E
        B-C
        B-D
"""
print()