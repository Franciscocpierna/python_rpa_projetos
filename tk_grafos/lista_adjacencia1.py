"""
Exercício Grafo Lista de Adjacência

Modifique o exemplo anterior para criar um exemplo mais 
completo, considerando algumas adições:

    - Atributos de Vértices e Arestas: Adicione informações adicionais 
        a alguns vértices e arestas, como peso, cor, etc.
    
    - Cálculo de Alguns Parâmetros do Grafo: Calcule algumas 
        propriedades do grafo, como grau médio, densidade, entre outras.
        
    - Exibição em Formato Tabular de Informações: Use o pandas para exibir 
        as informações de vértices e arestas em formatos de tabela.
        
    - Personalização da Visualização: Personalizaremos ainda mais a visualização
        do grafo.

"""

import networkx as nx  # Importando a biblioteca NetworkX para manipulação de grafos.
import numpy as np     # Importando a biblioteca Numpy para cálculos numéricos.
import matplotlib.pyplot as plt  # Importando a biblioteca Matplotlib para visualização gráfica.
import pandas as pd    # Importando a biblioteca Pandas para manipulação de dados em formatos tabulares.

# Criando um grafo direcionado (com setas para indicar a direção das arestas).
grafo = nx.DiGraph()


# Definindo um dicionário para armazenar os atributos de cada vértice.
# A chave do dicionário representa o ID do vértice (um número inteiro neste caso).
# O valor associado a cada chave é outro dicionário contendo os atributos do vértice,
# especificamente a "cor" (um string representando a cor em inglês) e "tamanho" (um número inteiro).

vertices_atributos = {
    0: {"cor": "blue", "tamanho": 300},   # Vértice 0 terá cor azul e tamanho 300
    1: {"cor": "green", "tamanho": 400},  # Vértice 1 terá cor verde e tamanho 400
    2: {"cor": "red", "tamanho": 500},    # Vértice 2 terá cor vermelha e tamanho 500
    3: {"cor": "yellow", "tamanho": 600}, # Vértice 3 terá cor amarela e tamanho 600
    4: {"cor": "orange", "tamanho": 700}  # Vértice 4 terá cor laranja e tamanho 700
}

# Iterando sobre o dicionário 'vertices_atributos' para adicionar cada vértice ao grafo.
# Para cada iteração, 'vertice' recebe o ID do vértice (chave do dicionário) e 'atributos'
# recebe o dicionário associado contendo os atributos "cor" e "tamanho".
for vertice, atributos in vertices_atributos.items():
    
    # Adicionando o vértice ao grafo com os atributos definidos.
    # O operador '**' é utilizado para desempacotar o dicionário 'atributos' como argumentos nomeados.
    grafo.add_node(vertice, **atributos)
    

# Definindo um dicionário para armazenar os atributos de cada aresta.
# A chave do dicionário representa a tupla (origem, destino) de cada aresta.
# O valor associado a cada chave é outro dicionário contendo o atributo "peso" da aresta.

arestas_atributos = {
    (0, 1): {"peso": 5},  # A aresta de 0 para 1 possui peso 5
    (0, 2): {"peso": 3},  # A aresta de 0 para 2 possui peso 3
    (1, 3): {"peso": 2},  # A aresta de 1 para 3 possui peso 2
    (2, 4): {"peso": 7},  # A aresta de 2 para 4 possui peso 7
    (3, 4): {"peso": 4}   # A aresta de 3 para 4 possui peso 4
}

# Adicionando as arestas (sem os atributos) ao grafo.
# Utilizamos o método 'keys()' para obter apenas as tuplas (origem, destino) das arestas 
# e adicioná-las ao grafo.
grafo.add_edges_from(arestas_atributos.keys())


# Iterando sobre o dicionário 'arestas_atributos' para atualizar os atributos de cada aresta no grafo.
# Para cada iteração, 'aresta' recebe a tupla (origem, destino) da aresta e 'atributos' 
# recebe o dicionário associado contendo o atributo "peso".
for aresta, atributos in arestas_atributos.items():
    
    # Atualizando os atributos da aresta específica no grafo.
    # Utilizamos o método 'update()' para modificar/adicional o atributo "peso" à aresta no grafo.
    grafo[aresta[0]][aresta[1]].update(atributos)


# Calculando e imprimindo algumas propriedades do grafo.

# Calculando o grau médio do grafo. 
# O método 'degree()' retorna um objeto DegreeView com os graus de cada vértice.
# Convertendo isso para um dicionário e, em seguida, obtendo seus valores (graos).
# Finalmente, usando a função 'mean()' do numpy para calcular a média desses graus.

# Obtendo os graus (número de arestas) de todos os vértices do grafo.
graus = dict(grafo.degree())

# Extraindo apenas os valores (quantidades de arestas) do dicionário.
valores_graus = list(graus.values())

# Calculando a média dos graus dos vértices.
media_graus = np.mean(valores_graus)

# Imprimindo o grau médio.
print(f"Grau Médio: {media_graus}")


# Calculando a densidade do grafo.
# A densidade é uma medida que indica quão conectado é o grafo.
# Um valor de 1 significa que o grafo é completamente conectado, enquanto um valor de 0 indica que não há conexões.
densidade_do_grafo = nx.density(grafo)

# Imprimindo o valor da densidade.
print(f"Densidade: {densidade_do_grafo}\n")


# Imprimindo informações dos vértices e arestas em formato
# tabular usando a biblioteca pandas.

# Mostrando os atributos dos vértices em formato de tabela.
# Convertendo o dicionário 'vertices_atributos' em um DataFrame do pandas.
# A transposição (.T) torna os vértices como índices e os atributos como colunas.
print("Informações dos Vértices:")
vertices_df = pd.DataFrame(vertices_atributos).T
print(vertices_df, "\n")

# Mostrando os atributos das arestas em formato de tabela.
# Convertendo o dicionário 'arestas_atributos' em um DataFrame do pandas.
# Novamente, a transposição (.T) torna as arestas como índices e os atributos como colunas.
print("Informações das Arestas:")
arestas_df = pd.DataFrame(arestas_atributos).T
print(arestas_df, "\n")

# Desenhando o grafo
# Preparando os atributos visuais para a representação gráfica do grafo.

# Inicializando a lista para armazenar as cores dos vértices.
cores = []

# Iterando por todos os vértices e seus atributos no grafo.
for vertice, atributos in grafo.nodes(data=True):
    
    # Obtendo a cor do vértice atual a partir de seus atributos.
    cor_do_vertice = atributos["cor"]
    
    # Adicionando a cor à lista de cores.
    cores.append(cor_do_vertice)
    
    
# Inicializando a lista para armazenar os tamanhos dos vértices.
tamanhos = []

"""
    grafo.nodes(data=True):
    
        Este é um método da biblioteca networkx que retorna todos
        os vértices (nós) de um grafo.
        
        O argumento data=True indica que, além do vértice em si, 
        queremos também os atributos associados a esse vértice. Se esse 
        argumento fosse False ou não estivesse presente, obteríamos apenas 
        os vértices sem seus atributos.
        
        Portanto, grafo.nodes(data=True) retorna uma sequência de pares, onde
        cada par contém um vértice e seus atributos.

    for vertice, atributos in ...:
    
        Este é um loop for que itera sobre cada par (vértice, atributos) retornado
        por grafo.nodes(data=True).
        
        vertice é uma variável que armazena o vértice atual da iteração.
        
        atributos é uma variável que armazena os atributos do vértice atual
        da iteração (geralmente na forma de um dicionário).
"""
# Iterando por todos os vértices e seus atributos no grafo.
for vertice, atributos in grafo.nodes(data=True):
    
    # Obtendo o tamanho do vértice atual a partir de seus atributos.
    tamanho_do_vertice = atributos["tamanho"]
    
    # Adicionando o tamanho à lista de tamanhos.
    tamanhos.append(tamanho_do_vertice)
    
    
# Inicializar uma lista vazia para armazenar os pesos das arestas.
# Os pesos representam os valores associados a cada aresta. Por exemplo, 
# em um grafo de estradas, o peso pode representar a distância entre as cidades.
pesos = []

# Iterar sobre todas as arestas do grafo.
# A função 'edges' do grafo, quando chamada com o 
# argumento 'data=True', retorna uma lista de tuplas.
# Cada tupla contém o nó de origem, o nó de destino e um 
# dicionário de atributos associados à aresta.
for origem, destino, atributos in grafo.edges(data=True):
    
    # Obter o peso da aresta atual do dicionário de atributos.
    # Aqui, assumimos que cada aresta tem um atributo chamado "peso". 
    # Se não houver tal atributo, ocorrerá um erro.
    peso_atual = atributos["peso"]
    
    # Adicionar o peso atual à lista de pesos.
    # Isso constrói nossa lista de pesos à medida que iteramos sobre todas as arestas.
    pesos.append(peso_atual)
    
    
    
# Desenhando o grafo:

# Gerando um posicionamento dos vértices do grafo usando o 
# layout spring (também chamado de "Fruchterman-Reingold").
# Isso distribui os vértices de maneira que arestas de tamanhos
# semelhantes fiquem próximas uma da outra, imitando uma simulação de molas.
posicionamento = nx.spring_layout(grafo)

# Desenhando os vértices (nós) do grafo:
# - 'grafo': é o grafo que queremos desenhar.
# - 'posicionamento': especifica as coordenadas (x, y) para cada 
# vértice, determinando onde eles serão colocados no espaço de desenho.
# - 'node_color=cores': define a cor de cada vértice com base na 
# lista 'cores' que construímos anteriormente.
# - 'node_size=tamanhos': determina o tamanho de cada vértice usando a
# lista 'tamanhos' que também construímos anteriormente. 
# Este tamanho pode ser útil para destacar certos vértices ou 
# representar algum tipo de valor ou magnitude.
nx.draw_networkx_nodes(grafo, posicionamento, node_color=cores, node_size=tamanhos)

# Desenhando as arestas (conexões) entre os vértices do grafo:
# - 'arrows=True': como estamos trabalhando com um grafo direcionado, 
# queremos mostrar a direção de uma aresta 
# para outra usando setas.
# - 'arrowsize=20': determina o tamanho das setas. Um valor maior 
# resulta em setas mais largas.
# - 'width=pesos': controla a espessura ou largura de cada aresta usando
# a lista 'pesos'. Arestas com maior peso 
# serão mais grossas, o que pode ser útil para visualizar a importância 
# ou capacidade da conexão, por exemplo, em um grafo de tráfego rodoviário.
nx.draw_networkx_edges(grafo, posicionamento, arrows=True, arrowsize=20, width=pesos)

# Adicionando rótulos aos vértices, que são, por padrão, os
# próprios identificadores dos vértices.
nx.draw_networkx_labels(grafo, posicionamento)

# Adicionando um título ao gráfico.
plt.title("Visualização do Grafo Personalizada")

# Exibindo o gráfico.
plt.show()