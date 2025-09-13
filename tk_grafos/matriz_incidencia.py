"""
Grafos
            
            Matriz de Incidência
            

A Matriz de Incidência é outra maneira de representar grafos além 
da Matriz de Adjacência e da Lista de Adjacência. Em grafos direcionados, a 
Matriz de Incidência define a relação entre vértices e arestas, de tal forma que:

    Cada linha da matriz representa um vértice.
    Cada coluna da matriz representa uma aresta.
    Se o vértice v é a origem da aresta e, então a matriz terá -1 na posição correspondente.
    Se o vértice v é o destino da aresta e, então a matriz terá 1 na posição correspondente.
    Caso contrário, a matriz terá 0.

"""

# Importando a biblioteca 'networkx' e dando a ela o alias "rede".
# Esta biblioteca é usada para criar, manipular e estudar a 
# estrutura e a dinâmica de redes complexas.
import networkx as rede

# Importando o módulo 'pyplot' da biblioteca 'matplotlib' e 
# dando a ele o alias "grafico".
# 'matplotlib' é uma biblioteca usada para criar
# visualizações gráficas em Python. 
# O módulo 'pyplot' fornece uma interface que permite criar
# figuras e gráficos de forma semelhante ao MATLAB.
import matplotlib.pyplot as grafico

# Criando um novo grafo direcionado e armazenando-o na variável "grafo".
# Um grafo direcionado é um conjunto de vértices (ou nós) conectados
# por arestas direcionadas (ou setas),
# onde cada aresta tem uma direção, do ponto inicial ao ponto final.
grafo = rede.DiGraph()

# Adicionando arestas (ou conexões) ao grafo direcionado "grafo" 
# a partir de uma lista de tuplas.
# Cada tupla representa uma aresta, onde o primeiro elemento é o 
# nó de origem e o segundo é o nó de destino.
# Por exemplo, a tupla (0, 1) adiciona uma aresta do nó 0 ao nó 1.
# Se os nós não existirem no grafo, 'networkx' os criará automaticamente.
grafo.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)])

# Configurando a disposição dos nós do grafo usando o layout "spring".
# O layout "spring" (ou "Fruchterman-Reingold") é uma técnica que posiciona os nós
# de modo que arestas de comprimentos semelhantes fiquem igualmente espaçadas, tentando minimizar
# a quantidade de sobreposições entre as arestas.
# O resultado é um dicionário, armazenado na variável "posicao_nos", onde as chaves são os nós
# e os valores são as coordenadas (x, y) de cada nó.
posicao_nos = rede.spring_layout(grafo)

# Desenhando os nós do grafo na tela. 
# 'grafo' é o grafo que queremos visualizar.
# 'posicao_nos' determina a posição de cada nó.
# 'node_color' define a cor dos nós, neste caso, azul claro.
# 'node_size' especifica o tamanho dos nós, neste caso, 700.
rede.draw_networkx_nodes(grafo, posicao_nos, node_color='lightblue', node_size=700)

# Desenhando as arestas (ou conexões) do grafo na tela.
# 'grafo' é o grafo que queremos visualizar.
# 'posicao_nos' determina a posição inicial e final de cada aresta.
# 'arrows=True' indica que as arestas são direcionadas, ou seja, possuem uma seta indicando a direção.
# 'arrowsize' define o tamanho da seta, neste caso, 20.
rede.draw_networkx_edges(grafo, posicao_nos, arrows=True, arrowsize=20)


# Desenhando os rótulos dos nós na tela.
# Cada nó receberá um rótulo que corresponde ao seu identificador no grafo.
# 'grafo' é o grafo que queremos visualizar.
# 'posicao_nos' determina a posição onde o rótulo de cada nó será colocado.
rede.draw_networkx_labels(grafo, posicao_nos)


# Criando rótulos para as arestas (conexões) do grafo.
# Estamos usando uma compreensão de dicionário para criar um dicionário chamado "rotulos_conexoes".
# Cada chave deste dicionário é uma tupla representando uma aresta (início, fim).
# O valor associado a cada chave é uma string no formato "início->fim".
# Por exemplo, para a aresta que vai do nó 0 ao nó 1, teríamos a chave (0, 1) e o valor "0->1".
# rotulos_conexoes = {(inicio, fim): f"{inicio}->{fim}" for inicio, fim in grafo.edges()}

# Inicializando um dicionário vazio para armazenar os rótulos das conexões.
rotulos_conexoes = {}

# Iterando sobre cada aresta (conexão) do grafo.
# 'grafo.edges()' retorna uma lista de tuplas, onde cada tupla 
# representa uma conexão (início, fim).
for inicio, fim in grafo.edges():
    
    # Criando o rótulo da conexão no formato "início->fim".
    rotulo = f"{inicio}->{fim}"
    
    # Adicionando o rótulo ao dicionário, usando a tupla (início, fim) como chave.
    rotulos_conexoes[(inicio, fim)] = rotulo
    
# Desenhando os rótulos das arestas na tela.
# 'grafo' é o grafo que queremos visualizar.
# 'posicao_nos' determina a posição onde o rótulo de cada aresta será colocado.
# 'edge_labels' é o dicionário que contém os rótulos que queremos mostrar para cada aresta.
rede.draw_networkx_edge_labels(grafo, posicao_nos, edge_labels=rotulos_conexoes)

# Definindo o título da visualização gráfica. 
# Neste caso, o título será "Visualização do Grafo".
grafico.title("Visualização do Grafo")

# Exibindo a visualização gráfica na tela.
# Esta função irá mostrar uma janela com o grafo desenhado, incluindo nós, arestas e rótulos.
grafico.show()

"""
    O valor −1 indica que o vértice correspondente àquela linha é a origem 
        da aresta correspondente àquela coluna.

    O valor 1 indica que o vértice correspondente àquela linha é o destino da 
        aresta correspondente àquela coluna.

    O valor 0 indica que o vértice não está conectado à aresta em questão.

Assim, esses valores ajudam a representar e entender a direção de cada aresta no grafo.
    
temos as seguintes arestas:

    0 -> 1
    0 -> 2
    1 -> 3
    2 -> 4
    3 -> 4
    
+-----+----+-----+----+----+----+
| V\V | 0  | 1   | 2  | 3  | 4  |
+-----+----+-----+----+----+----+
|  0  | -1 | -1  |  0 |  0 |  0 |  <- Vértice 0: É a origem das arestas 0 e 1.
|  1  |  1 |  0  | -1 |  0 |  0 |  <- Vértice 1: É o destino da aresta 0 e a origem da aresta 2.
|  2  |  0 |  1  |  0 | -1 |  0 |  <- Vértice 2: É o destino da aresta 1 e a origem da aresta 3.
|  3  |  0 |  0  |  1 |  0 | -1 |  <- Vértice 3: É o destino da aresta 2 e a origem da aresta 4.
|  4  |  0 |  0  |  0 |  1 |  1 |  <- Vértice 4: É o destino das arestas 3 e 4.
+-----+----+-----+----+----+----+


    Aresta 0: vai do vértice 0 ao vértice 1
    Aresta 1: vai do vértice 0 ao vértice 2
    Aresta 2: vai do vértice 1 ao vértice 3
    Aresta 3: vai do vértice 2 ao vértice 4
    Aresta 4: vai do vértice 3 ao vértice 4
"""
print()