"""
Grafos
  grafo1.py, grafos2.py, grafos3.py Matriz de Adjacência,          
            Representação de Grafos

                Matriz de Adjacência
                Lista de Adjacência
                Matriz de Incidência

            Travessias de Grafos

                Busca em Largura (BFS)
                Busca em Profundidade (DFS)

            Algoritmos Clássicos

                Algoritmo de Dijkstra para Caminhos Mais Curtos
                Algoritmo de Bellman-Ford
                Algoritmo de Kruskal para Árvores Geradoras Mínimas
                
"""
print()

"""
Grafos
            
           Matriz de Adjacência
           
Um grafo pode ser representado de diversas maneiras e uma delas é 
através de uma matriz de adjacência. Nessa representação, o elemento aij da matriz é 1 (ou 
algum peso, no caso de um grafo ponderado) se houver uma aresta entre os 
vértices i e j, e 0 se não houver.

Vamos criar um exemplo simples em Python que demonstra como implementar e manipular 
um grafo utilizando matriz de adjacência:


Vamos supor que temos um grafo com 4 vértices (0, 1, 2 e 3).

E vamos ter as seguintes arestas:

    0 -> 1
    0 -> 2
    1 -> 2
    2 -> 3
    3 -> 0
   
    
    
Matriz de Adjacência:

A matriz é definida da seguinte forma: Se há uma aresta do vértice i para o 
vértice j, então a posição (i, j) na matriz terá o valor 1, caso contrário, 
terá o valor 0.


   0  1  2  3
0 [0, 1, 1, 0]
1 [0, 0, 1, 0]
2 [0, 0, 0, 1]
3 [1, 0, 0, 0]

"""

# Importando a biblioteca networkx com o alias 'nx'.
# A biblioteca networkx é amplamente usada para a criação, 
# manipulação e estudo da estrutura e funções de grafos complexos.
import networkx as nx

# Importando a biblioteca matplotlib.pyplot com o alias 'plt'.
# A biblioteca matplotlib é uma biblioteca gráfica usada para visualização em Python.
import matplotlib.pyplot as plt

# Criando um grafo direcionado (DiGraph).
# Um grafo direcionado possui arestas com direção, ou seja, cada aresta 
# move-se de um vértice de origem para um vértice de destino.
G = nx.DiGraph()

# Adicionando uma aresta ao grafo direcionado G.
# Esta aresta vai do vértice 0 para o vértice 1.
G.add_edge(0, 1)

# Adicionando outra aresta ao grafo G.
# Esta aresta começa no vértice 1 e termina no vértice 2.
G.add_edge(1, 2)

# Adicionando mais uma aresta ao grafo G.
# A aresta conecta o vértice 2 ao vértice 3.
G.add_edge(2, 3)

# Adicionando uma aresta que liga o vértice 3 de volta ao vértice 0.
# Isso cria um ciclo entre os vértices 0, 1, 2, e 3.
G.add_edge(3, 0)

# Adicionando a última aresta ao grafo G.
# Esta aresta conecta o vértice 0 diretamente ao vértice 2, formando um atalho entre eles.
G.add_edge(0, 2)


# Definindo um dicionário para armazenar as posições (coordenadas x, y) de cada vértice no gráfico.
# Isso ajudará a posicionar os vértices de forma personalizada quando desenharmos o gráfico.
pos = {
    0: (-1, 1),   # Atribuindo a posição (-1, 1) ao vértice 0, posicionando-o no topo esquerdo do gráfico.
    1: (1, 1),    # Atribuindo a posição (1, 1) ao vértice 1, colocando-o no topo direito do gráfico.
    2: (1, -1),   # Definindo a posição (1, -1) para o vértice 2, posicionando-o no canto inferior direito.
    3: (-1, -1)   # Estabelecendo a posição (-1, -1) para o vértice 3, fazendo com que ele fique no canto inferior esquerdo.
}

# Desenhando o grafo utilizando a função 'draw' da biblioteca 'networkx'.
# Os argumentos definem diversos aspectos da visualização.
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

# Usando a função 'show' da biblioteca 'matplotlib' para exibir o gráfico desenhado.
plt.show()

"""
    0 -> 1
    0 -> 2
    1 -> 2
    2 -> 3
    3 -> 0
"""
print()
