"""
grafo1.py, grafos2.py, grafos3.py Matriz de Adjacência,
Vamos criar um grafo mais complexo, com mais vértices e arestas para demonstração.

Imagine um grafo com 7 vértices (0 a 6) e as seguintes arestas:

    0 -> 1
    0 -> 3
    1 -> 2
    1 -> 4
    2 -> 6
    3 -> 5
    4 -> 6
    5 -> 3
    6 -> 5
    6 -> 0

Matriz de Adjacência:

   0  1  2  3  4  5  6
0 [0, 1, 0, 1, 0, 0, 0]
1 [0, 0, 1, 0, 1, 0, 0]
2 [0, 0, 0, 0, 0, 0, 1]
3 [0, 0, 0, 0, 0, 1, 0]
4 [0, 0, 0, 0, 0, 0, 1]
5 [0, 0, 0, 1, 0, 0, 0]
6 [1, 0, 0, 0, 0, 1, 0]


"""

# Gráfico:

# Vamos usar o código para criar o gráfico deste exemplo:

# Importando a biblioteca 'networkx' com o alias 'nx'.
# Esta biblioteca é usada para a criação, manipulação e análise de estruturas de grafos.
import networkx as nx

# Importando a biblioteca 'matplotlib.pyplot' com o alias 'plt'.
# Esta biblioteca é usada para criar visualizações gráficas, como gráficos e diagramas.
import matplotlib.pyplot as plt

# Criando um novo grafo direcionado usando o método 'DiGraph' da biblioteca 'networkx'.
# Um grafo direcionado é um conjunto de vértices e arestas direcionadas (com um sentido definido).
G = nx.DiGraph()


# Comentário descrevendo a operação que será realizada a seguir: Adição de arestas ao grafo.
# Criando uma lista de tuplas chamada 'arestas'. 
# Cada tupla representa uma aresta direcionada, com o primeiro elemento sendo 
# o vértice de origem e o segundo elemento o vértice de destino.
arestas = [(0, 1), (0, 3), (1, 2), (1, 4), (2, 6), (3, 5), (4, 6), (5, 3), (6, 5), (6, 0)]

# Utilizando o método 'add_edges_from' do objeto 'G' (que é nosso grafo direcionado) 
# para adicionar todas as arestas definidas na lista 'arestas'.
# As arestas são adicionadas de acordo com as tuplas, criando uma conexão direcionada 
# entre os vértices.
G.add_edges_from(arestas)


# A função spring_layout cria uma disposição que parece "natural" para grafos
# Isso é útil quando temos um grafo mais complexo e não queremos definir 
# manualmente cada posição.
pos = nx.spring_layout(G)


nx.draw(
    G,               # Especifica o grafo 'G' que será desenhado.
    pos=pos,         # Usa o dicionário 'pos' para determinar a posição de cada vértice.
    with_labels=True, # Mostra os rótulos/identificadores dos vértices.
    font_weight='bold', # Define que o peso da fonte dos rótulos dos vértices será 'bold' (negrito).
    node_color='skyblue', # Define a cor dos vértices como 'skyblue' (azul claro).
    node_size=1000,      # Define o tamanho dos vértices. 
    edge_color='gray',   # Define a cor das arestas/linhas entre os vértices como cinza.
    arrows=True,         # Especifica que as arestas terão setas (pois é um grafo direcionado).
    arrowstyle='-|>'     # Define o estilo da seta.
)


# Utilizando a função 'show' do pacote 'matplotlib.pyplot' para exibir 
# a visualização do grafo que foi gerada pela função 'draw'.
plt.show()

"""
    0 -> 1
    0 -> 3
    1 -> 2
    1 -> 4
    2 -> 6
    3 -> 5
    4 -> 6
    5 -> 3
    6 -> 5
    6 -> 0
"""
print()