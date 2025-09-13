# Importando as bibliotecas necessárias:
# 'networkx' é uma biblioteca que fornece estruturas de dados 
# para representar grafos e muitos algoritmos para analisá-los.
# 'matplotlib.pyplot' é uma biblioteca para criar visualizações gráficas.
import networkx as rede
import matplotlib.pyplot as grafico

# Inicializando um grafo vazio. Aqui, estamos criando um grafo não direcionado.
grafo = rede.Graph()

# Definindo uma lista de arestas para serem adicionadas ao grafo.
# Cada tupla representa uma aresta entre dois vértices.
arestas = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')]
grafo.add_edges_from(arestas)  # Adicionando todas as arestas ao grafo de uma única vez.


# Definindo as posições dos vértices para desenhar o grafo. 
# As posições são representadas como coordenadas (x, y) em um plano.
posicoes_vertices = {
    'A': (0, 2),   # Vértice 'A' está na posição x=0 e y=2.
    'B': (-1, 1),  # Vértice 'B' está na posição x=-1 e y=1.
    'C': (1, 1),   # Vértice 'C' está na posição x=1 e y=1.
    'D': (-1, 0),  # Vértice 'D' está na posição x=-1 e y=0.
    'E': (1, 0)    # Vértice 'E' está na posição x=1 e y=0.
}

# Configurando o tamanho da figura onde o grafo será desenhado.
grafico.figure(figsize=(8,6))


# Desenhando o grafo com as configurações especificadas.
# 'pos=posicoes_vertices': determina a posição de cada vértice no desenho.
# 'with_labels=True': mostra o rótulo de cada vértice.
# 'node_size=1500': determina o tamanho dos vértices.
# 'node_color='lightblue'': determina a cor dos vértices.
# 'font_size=15': tamanho da fonte dos rótulos dos vértices.
# 'width=2': largura das arestas.
# 'edge_color='gray'': cor das arestas.
rede.draw(grafo, 
          pos=posicoes_vertices, 
          with_labels=True, 
          node_size=1500, 
          node_color='lightblue', 
          font_size=15, 
          width=2, 
          edge_color='gray')

# Definindo o título da visualização.
grafico.title("Visualização do Grafo")

# Exibindo o grafo desenhado.
grafico.show()