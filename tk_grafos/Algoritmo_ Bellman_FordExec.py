"""
Exercício de Bellman-Ford:

Suponha que temos um conjunto de cidades e estradas entre elas, e
queremos encontrar o caminho mais barato da Cidade A para a Cidade D.

Exemplo Visual

Descrição do gráfico:

    Cidade A tem uma estrada para a Cidade B com um custo de $5.
    Cidade A tem uma estrada para a Cidade C com um custo de $8.
    Cidade B tem uma estrada para a Cidade D com um custo de $2.
    Cidade C tem uma estrada para a Cidade D com um custo de $4.

Com base neste gráfico, o caminho mais barato da Cidade A para a 
Cidade D é A -> B -> D com um custo total de $7.

Crie um código que crie um Grafo com esse dados destacando o 
caminho mais barato.
"""

# Solução

# Importando as bibliotecas necessárias
import networkx as nx
import matplotlib.pyplot as plt

# Inicializando um grafo direcionado. Um grafo direcionado é um 
# conjunto de vértices (cidades) e arestas direcionadas (estradas) entre esses vértices.
grafo = nx.DiGraph()

# Adicionando arestas ao grafo para representar estradas entre
# cidades. O parâmetro 'weight' indica o custo de viajar por essa estrada.
grafo.add_edge('Cidade A', 'Cidade B', weight=5)
grafo.add_edge('Cidade A', 'Cidade C', weight=8)
grafo.add_edge('Cidade B', 'Cidade D', weight=2)
grafo.add_edge('Cidade C', 'Cidade D', weight=4)

# Aplicando o algoritmo de Bellman-Ford para calcular o caminho mais
# barato de 'Cidade A' para todas as outras cidades no grafo.
predecessores, distancias = nx.bellman_ford_predecessor_and_distance(grafo, 'Cidade A')

# Imprimindo as distâncias (ou custos) calculadas da 'Cidade A' para 
# todas as outras cidades no grafo.
# A função print é usada para exibir uma mensagem no console ou terminal.
print("Distâncias a partir da Cidade A:")

# O loop for é usado para iterar sobre cada item no dicionário 'distancias'. 
# O dicionário 'distancias' contém cada cidade como chave e a 
# distância (ou custo) da 'Cidade A' para essa cidade como valor.
for cidade, distancia in distancias.items():
    
    # Dentro do loop, a função print é usada novamente para 
    # exibir a cidade e sua respectiva distância.
    # O f-string (indicado pelo prefixo 'f') permite incorporar 
    # valores de variáveis diretamente na string.
    print(f"{cidade}: ${distancia}")
    

# Iniciando o processo de reconstrução do caminho mais barato da 'Cidade A' para a 'Cidade D'.
# Começamos com a 'Cidade D' porque queremos reconstruir o caminho de volta para a 'Cidade A'.
caminho = ['Cidade D']

# A variável 'no_atual' é usada para acompanhar a cidade atual enquanto reconstruímos o caminho.
# Como estamos reconstruindo de trás para frente, começamos com a 'Cidade D'.
no_atual = 'Cidade D'

# O loop while continuará enquanto 'no_atual' não for 'Cidade A', 
# ou seja, até que o caminho completo seja reconstruído.
while no_atual != 'Cidade A':
    
    # Atualizando 'no_atual' para ser a cidade predecessora da 
    # cidade atual no caminho mais barato.
    # O dicionário 'predecessores' fornece a cidade 
    # predecessora para cada cidade no grafo.
    no_atual = predecessores[no_atual][0]
    
    # Adicionando a cidade predecessora à lista 'caminho'.
    caminho.append(no_atual)
    
# Como o caminho foi construído começando pela 'Cidade D' e 
# terminando na 'Cidade A', ele está ao contrário.
# Portanto, usamos o método reverse() para inverter a lista e 
# obter o caminho correto da 'Cidade A' para a 'Cidade D'.
caminho.reverse()

# Usando o layout "spring" para determinar a disposição dos 
# vértices (neste caso, as cidades) no espaço bidimensional.
# Esta disposição tenta posicionar os vértices de forma que as
# arestas tenham aproximadamente o mesmo comprimento e haja pouca sobreposição.
pos = nx.spring_layout(grafo)

# Desenhando o grafo no espaço determinado pelo layout 'spring'.
# O parâmetro 'with_labels=True' indica que queremos que os nomes das cidades sejam exibidos.
# 'node_color' define a cor dos círculos que representam as cidades.
nx.draw(grafo, pos, with_labels=True, node_color='lightblue')

# Recuperando os pesos (ou custos) associados a cada aresta (neste caso, estrada) no grafo.
# Estes serão usados para mostrar os custos das estradas entre as cidades.
etiquetas_arestas = nx.get_edge_attributes(grafo, 'weight')

# Adicionando rótulos às arestas (estradas) usando os custos recuperados anteriormente.
# 'edge_labels' especifica a informação que queremos mostrar em cada aresta.
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=etiquetas_arestas)

# Para destacar o caminho mais barato de 'Cidade A' para 'Cidade D', criamos
# uma lista de arestas que compõem esse caminho.
# A função zip() é usada para combinar cada cidade no 'caminho' com a 
# cidade seguinte, criando pares que representam as arestas.
caminho_arestas = list(zip(caminho, caminho[1:]))


# Desenhando as arestas do caminho mais barato com uma cor vermelha e uma espessura de linha de 2.
# 'edgelist' especifica quais arestas queremos desenhar, e 'edge_color' 
# e 'width' definem a cor e a espessura da linha, respectivamente.
nx.draw_networkx_edges(grafo, pos, edgelist=caminho_arestas, edge_color='r', width=2)

# Usando a função 'show' da biblioteca Matplotlib para exibir o gráfico gerado.
plt.show()



"""
Ao executar o código acima, você obterá a distância mais curta 
da Cidade A para todas as outras cidades e uma visualização do 
grafo. Isso deve fornecer uma representação clara e simples do 
algoritmo de Bellman-Ford em ação.
"""
print()