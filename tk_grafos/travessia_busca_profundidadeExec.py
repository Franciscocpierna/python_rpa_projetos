"""
Exercício Busca em Profundidade (DFS)

Dada uma lista de cidades do estado de São Paulo e suas respectivas
conexões, o objetivo deste exercício é criar um programa que visualize
essas cidades e as conexões entre elas em um gráfico.

Requisitos:

    - As cidades e suas conexões são as seguintes:
        São Paulo (SP) está conectada com Guarulhos (GRU), Osasco (OSC) e São Caetano (SC).
        Guarulhos (GRU) está conectada com São Paulo (SP) e Arujá (ARU).
        Osasco (OSC) está conectada com São Paulo (SP) e Barueri (BAR).

    - Para representar visualmente o grafo, defina as posições das cidades 
     da seguinte forma:
        'SP': (0, 3),  # Colocando SP no topo
        'GRU': (-1, 2),
        'ARU': (-1, 1),
        'OSC': (0, 2),
        'BAR': (0, 1),
        'SC': (1, 2)

    - A figura resultante deve ter tamanho 10x8 (figsize).

    - As cidades devem ser representadas com um tamanho de nó de 1500, cor 
        'lightblue' e tamanho de fonte 15.

    - As conexões (arestas) entre as cidades devem ter largura 2 e cor 'gray'.

    - O gráfico deve conter um título: "Visualização do Grafo - Cidades de SP".

Observação:

Não é necessário criar funções adicionais ou tratar exceções. O foco deste exercício 
é a representação gráfica e manipulação de um grafo simples.

   SP
  / | \
GRU OSC SC
 |   |
ARU BAR
"""

# Importando as bibliotecas necessárias:
# 'networkx' é uma biblioteca que fornece estruturas de dados 
# Importando as bibliotecas necessárias:
# 'networkx' é uma biblioteca que fornece estruturas de dados para representar grafos e muitos algoritmos para analisá-los.
# 'matplotlib.pyplot' é uma biblioteca para criar visualizações gráficas.
import networkx as rede
import matplotlib.pyplot as grafico

# Inicializando um grafo vazio. Aqui, estamos criando um grafo não direcionado.
grafo_cidades = rede.Graph()

# Definindo uma lista de arestas que representam ligações entre cidades.
# Cada tupla representa uma ligação entre duas cidades.
ligacoes_cidades = [
    ('SP', 'GRU'),
    ('SP', 'OSC'),
    ('SP', 'SC'),
    ('GRU', 'ARU'),
    ('OSC', 'BAR')
]

# Adicionando todas as ligações ao grafo de uma só vez.
grafo_cidades.add_edges_from(ligacoes_cidades) 

# Definindo as posições dos vértices (cidades) para desenhar o grafo. 
# As posições são especificadas como coordenadas cartesianas (x, y) para 
# representar a posição de cada vértice no gráfico.

# Criando um dicionário para armazenar as coordenadas de cada cidade.
# As chaves do dicionário são os nomes das cidades (vértices) e os valores
# são tuplas representando as coordenadas (x, y).
coordenadas_cidades = {
    'SP': (0, 3),      # A cidade de São Paulo (SP) é posicionada na coordenada (0, 3).
    'GRU': (-1, 2),    # Guarulhos (GRU) é posicionada em (-1, 2).
    'ARU': (-1, 1),    # Arujá (ARU) é posicionada em (-1, 1).
    'OSC': (0, 2),     # Osasco (OSC) é posicionada em (0, 2).
    'BAR': (0, 1),     # Barueri (BAR) é posicionada em (0, 1).
    'SC': (1, 2)       # Outra cidade (SC) é posicionada em (1, 2).
}


# Configurando o tamanho da figura onde o grafo será desenhado.
grafico.figure(figsize=(10,8))

# Desenhando o grafo com as configurações especificadas.
# 'pos=coordenadas_cidades': determina a posição de cada cidade no desenho.
# 'with_labels=True': mostra o rótulo de cada cidade.
# 'node_size=1500': determina o tamanho dos vértices (cidades).
# 'node_color='lightblue'': determina a cor dos vértices (cidades).
# 'font_size=15': tamanho da fonte dos rótulos das cidades.
# 'width=2': largura das arestas (ligações entre cidades).
# 'edge_color='gray'': cor das arestas.
rede.draw(grafo_cidades, 
          pos=coordenadas_cidades, 
          with_labels=True, 
          node_size=1500, 
          node_color='lightblue', 
          font_size=15, width=2, 
          edge_color='gray')

# Definindo o título da visualização.
grafico.title("Visualização do Grafo - Cidades de SP")

# Exibindo o grafo desenhado.
grafico.show()

"""
   SP
  / | \
GRU OSC SC
 |   |
ARU BAR
"""
print()