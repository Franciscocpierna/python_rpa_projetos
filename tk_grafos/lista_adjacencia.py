"""
Grafos
            
           Lista de Adjacência
           
A lista de adjacência é uma das formas mais comuns de representar
grafos em memória, especialmente quando o grafo é esparso (tem relativamente 
poucas arestas). Ela é especialmente útil em termos de economia de espaço
em comparação com a matriz de adjacência.

Exemplo
"""

# Importando os pacotes necessários:
# - networkx para manipulação e visualização de grafos;
# - numpy para operações de matriz;
# - matplotlib.pyplot para visualizações adicionais.
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Inicializando um grafo direcionado (DiGraph) que tem arestas com direção (setas).
grafo = nx.DiGraph()

# Adicionando vértices ao grafo:
# O loop for irá iterar 5 vezes, uma vez para cada número no 
# intervalo de 0 a 4 (5 não está incluído).

for vertice in range(5): # Iniciando um loop for que passará pelos números 0, 1, 2, 3 e 4.
    grafo.add_node(vertice) # Para cada iteração do loop, um vértice é adicionado ao grafo. 
                            # O número da iteração (de 0 a 4) é usado como o nome/identificador do vértice.
        

# Adicionando arestas ao grafo:
# As arestas são adicionadas ao grafo usando uma lista de tuplas, 
# onde cada tupla representa uma aresta.
# Cada tupla contém dois números: o primeiro é o vértice de origem
# e o segundo é o vértice de destino da aresta.

grafo.add_edges_from([(0, 1),   # Adiciona uma aresta do vértice 0 para o vértice 1.
                      (0, 2),   # Adiciona uma aresta do vértice 0 para o vértice 2.
                      (1, 3),   # Adiciona uma aresta do vértice 1 para o vértice 3.
                      (2, 4),   # Adiciona uma aresta do vértice 2 para o vértice 4.
                      (3, 4)    # Adiciona uma aresta do vértice 3 para o vértice 4.
                     ])


# Criando a matriz de adjacência:
# A matriz de adjacência é uma representação do grafo em forma de matriz.
# Cada linha e cada coluna da matriz representam um vértice do grafo.
# Se houver uma aresta do vértice "i" para o vértice "j", então o elemento
# da matriz na linha "i" e coluna "j" será 1. Caso contrário, será 0.

# Pegando a lista de todos os vértices/nós do grafo.
vertices = list(grafo.nodes())

# Calculando o número total de vértices no grafo.
num_vertices = len(vertices)

# Inicializando uma matriz quadrada (número de linhas = número de vértices
# e número de colunas = número de vértices) com todos os elementos setados para zero.
# A matriz é criada usando o pacote NumPy.
# Os elementos da matriz são do tipo inteiro.
matriz_adjacencia = np.zeros((num_vertices, num_vertices), dtype=int)


# Preenchendo a matriz de adjacência:
# Iterando sobre todas as arestas (conexões) presentes no grafo.
for origem, destino in grafo.edges():
    
    # Para cada aresta (origem, destino), encontramos o índice correspondente à origem
    # e o índice correspondente ao destino na lista de vértices.
    # Em seguida, atualizamos o elemento da matriz de adjacência na
    # posição (índice da origem, índice do destino) para 1.
    # Isso indica a existência de uma aresta direcionada do vértice de origem 
    # para o vértice de destino.
    matriz_adjacencia[vertices.index(origem), vertices.index(destino)] = 1
    
    
# Exibindo a matriz de adjacência:
print("Matriz de Adjacência:")

# Iterando sobre cada linha da matriz de adjacência.
for linha in matriz_adjacencia:
    
    # Imprimindo cada linha da matriz.
    # Cada linha da matriz representa as conexões do vértice correspondente
    # a essa linha com os outros vértices.
    print(linha)
    

# Exibindo a Lista de Adjacência:
print("\nLista de Adjacência:")

# Criando um dicionário vazio para armazenar a lista de adjacência.
# A chave será o vértice e o valor será uma lista de vértices vizinhos.
lista_adjacencia = {}

# Iterando sobre todos os vértices do grafo.
for vertice in grafo.nodes():
    
    # Para cada vértice, pegamos seus vértices vizinhos (ou seja, vértices
    # diretamente conectados a ele).
    # A função 'neighbors' do objeto grafo retorna um iterador
    # dos vizinhos do vértice em questão.
    # Convertendo esse iterador em uma lista e armazenando no dicionário 'lista_adjacencia'.
    lista_adjacencia[vertice] = list(grafo.neighbors(vertice))
    
    
# Iterando sobre os itens do dicionário 'lista_adjacencia' para imprimir.
for chave, valor in lista_adjacencia.items():
    
    # Imprimindo cada chave (vértice) e seus valores (lista de vértices vizinhos).
    # A saída mostra o vértice e seus vértices adjacentes no formato "chave: valor".
    print(f"{chave}: {valor}")
    
    
# Desenhando o grafo:

# Usando o algoritmo "spring layout" do NetworkX para calcular o posicionamento dos vértices.
# Este algoritmo tenta posicionar os vértices de tal forma que arestas de comprimentos semelhantes
# tenham tamanhos semelhantes e arestas cruzadas sejam minimizadas.
posicionamento = nx.spring_layout(grafo)

# Desenhando os vértices do grafo. 
# 'node_color' define a cor dos vértices.
# 'node_size' define o tamanho dos vértices.
nx.draw_networkx_nodes(grafo, posicionamento, node_color='lightblue', node_size=500)

# Desenhando as arestas do grafo.
# 'arrows' define se as setas (indicando a direção das
# arestas em grafos direcionados) devem ser desenhadas.
# 'arrowsize' define o tamanho das setas.
nx.draw_networkx_edges(grafo, posicionamento, arrows=True, arrowsize=20)

# Desenhando os rótulos dos vértices.
# Este método coloca um rótulo (o nome do vértice) em cada vértice.
nx.draw_networkx_labels(grafo, posicionamento)

# Configurando o título do gráfico que será exibido.
plt.title("Visualização do Grafo")

# Exibindo o gráfico.
# Esta é uma função do Matplotlib que exibe a figura/plot atual.
plt.show()

"""

A Matriz de Adjacência

    0 1 2 3 4
0: [0 1 1 0 0]
1: [0 0 0 1 0]
2: [0 0 0 0 1]
3: [0 0 0 0 1]
4: [0 0 0 0 0]


A Lista de Adjacência é:

Lista de Adjacência:
0: [1, 2]
1: [3]
2: [4]
3: [4]
4: []


Vamos descrever o gráfico com base na lista de adjacência:

    Temos um grafo direcionado com cinco vértices numerados de 0 a 4.
    
    O vértice 0 tem setas apontando para os vértices 1 e 2. Isso significa 
        que há uma aresta do vértice 0 para o vértice 1 e uma aresta do 
        vértice 0 para o vértice 2.
        
    O vértice 1 tem uma seta apontando para o vértice 3. Assim, há uma 
        aresta do vértice 1 para o vértice 3.
        
    O vértice 2 tem uma seta apontando para o vértice 4. Logo, há uma
        aresta do vértice 2 para o vértice 4.
        
    O vértice 3 também tem uma seta apontando para o vértice 4, indicando 
        uma aresta do vértice 3 para o vértice 4.
        
    O vértice 4 não tem arestas saindo dele, indicando que ele não se 
        conecta a nenhum outro vértice.

Em resumo, o grafo contém uma série de conexões unidirecionais entre os vértices, 
com os vértices 2, 3 e 4 atuando como destinos finais para as arestas entrantes.

"""
print()