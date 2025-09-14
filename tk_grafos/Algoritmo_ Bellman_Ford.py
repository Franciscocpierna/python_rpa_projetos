"""
Grafos
            
            Algoritmos Clássicos

                Algoritmo de Bellman-Ford
                
                
O Algoritmo de Bellman-Ford é usado para encontrar o caminho mais 
curto de um vértice de origem a todos os outros vértices em um grafo 
ponderado. Diferentemente do algoritmo de Dijkstra, o Bellman-Ford 
pode trabalhar com pesos negativos de arestas e pode detectar 
ciclos negativos.


Vamos imaginar que temos cidades interligadas por estradas que, devido
a certos fenômenos misteriosos, podem fazer você viajar no tempo!

Descrição do gráfico:

    Cidade A para Cidade B leva 2 horas.
    Cidade B para Cidade C leva 3 horas.
    Cidade A para Cidade C tem um fenômeno que reduz o tempo da 
        viagem em 4 horas (peso negativo).

A questão é: Qual é o caminho mais rápido da Cidade A para a Cidade C?

Codificação e resposta:
"""

# Importando as bibliotecas necessárias para a tarefa.
import networkx as nx
import matplotlib.pyplot as plt

# Criando um grafo direcionado (DiGraph) para 
# representar as conexões entre as estações.
grafo = nx.DiGraph()

# Estamos criando conexões (também conhecidas como arestas ou rotas) entre as estações no grafo. 
# Em um contexto de transporte ou viagem, as arestas podem representar rotas diretas entre duas estações.
# O parâmetro 'weight' em cada conexão especifica o tempo (ou custo) necessário para viajar entre essas duas estações.

# Adiciona uma rota direta da 'Estação Alfa' para a 'Estação Beta' que leva 4 unidades de tempo.
grafo.add_edge('Estação Alfa', 'Estação Beta', weight=4)

# Adiciona uma rota direta da 'Estação Alfa' para a 'Estação Gama' que leva 2 unidades de tempo.
grafo.add_edge('Estação Alfa', 'Estação Gama', weight=2)

# Adiciona uma rota direta da 'Estação Beta' para a 'Estação Delta'. 
# Aqui, temos um valor de duração negativo (-2), o que é raro em cenários reais. 
# No entanto, o algoritmo Bellman-Ford é capaz de lidar com pesos 
# negativos, o que é uma de suas características distintivas. 
# Em um contexto real, ter um peso negativo poderia representar um benefício, 
# recompensa ou algum tipo de incentivo.
grafo.add_edge('Estação Beta', 'Estação Delta', weight=-2)

# Adiciona uma rota direta da 'Estação Gama' para a 'Estação Delta' que 
# leva 3 unidades de tempo.
grafo.add_edge('Estação Gama', 'Estação Delta', weight=3)


# Aplicando o algoritmo de Bellman-Ford para calcular os caminhos mais curtos da 'Estação Alfa' para todas as outras estações.
# 'predecessores' é um dicionário que mapeia cada estação ao seu predecessor no caminho mais curto.
# 'distancias' é um dicionário que mapeia cada estação à sua distância mínima da 'Estação Alfa'.
predecessores, distancias = nx.bellman_ford_predecessor_and_distance(grafo, 'Estação Alfa')


# Inicializamos a reconstrução do caminho mais curto a partir da 
# 'Estação Delta', pois queremos determinar o caminho da 'Estação Alfa' 
# para a 'Estação Delta'.
# Começamos pelo destino e trabalhamos retroativamente até a origem.
caminho = ['Estação Delta']

# Iniciamos com o destino ('Estação Delta') como o nó atual.
no_atual = 'Estação Delta'

# Continuamos a encontrar o predecessor (estação anterior) de cada nó
# até chegarmos à origem ('Estação Alfa').
# A ideia é retroceder passo a passo, de estação em estação, 
# usando o dicionário de predecessores até que alcancemos a estação inicial.
while no_atual != 'Estação Alfa':
    
    # Obtemos o nó predecessor (estação anterior) do nó atual.
    # O dicionário "predecessores" fornece a próxima estação na 
    # rota mais curta de volta à estação de origem.
    no_atual = predecessores[no_atual][0]
    
    # Adicionamos esse nó predecessor ao nosso caminho.
    caminho.append(no_atual)

# Como construímos o caminho do destino para a origem, o caminho está ao contrário.
# Por isso, invertemos a lista para que ela comece na 'Estação Alfa' e 
# termine na 'Estação Delta'.
caminho.reverse()

# Definindo uma disposição (layout) espacial para os 
# vértices (neste caso, estações) do grafo.
# O layout "spring" (mola) posiciona os vértices de tal 
# forma que todas as arestas tenham mais ou menos o mesmo comprimento
# e tenta minimizar o número de arestas que se cruzam no gráfico.
pos = nx.spring_layout(grafo)

# Desenhando o grafo:
# - `pos` especifica as posições dos vértices.
# - `with_labels=True` garante que os rótulos dos vértices sejam exibidos.
# - `node_color='lightblue'` dá uma cor azul clara aos vértices.
# - `edge_color='gray'` dá uma cor cinza às arestas.
nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray')


# Extraindo os pesos (neste contexto, durações das rotas 
# entre estações) das arestas do grafo.
# O resultado é um dicionário onde a chave é uma tupla 
# representando a aresta e o valor é o peso dessa aresta.
etiquetas_arestas = nx.get_edge_attributes(grafo, 'weight')


# Desenhando as etiquetas (pesos/durações) nas arestas do grafo.
# - `edge_labels=etiquetas_arestas` especifica o que será exibido nas arestas.
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=etiquetas_arestas)


# Destacando o caminho mais curto entre 'Estação Alfa' e 'Estação Delta' no gráfico:

# Iterando sobre cada par de estações consecutivas no caminho mais curto.
# Por exemplo, se o caminho for ['Estação Alfa', 'Estação Beta', 'Estação Delta'],
# as combinações de estações serão [('Estação Alfa', 'Estação Beta'), ('Estação Beta', 'Estação Delta')].
for i in range(len(caminho) - 1):
    
    # Obtendo as coordenadas x e y da primeira estação do par no layout definido.
    x0, y0 = pos[caminho[i]]
    
    # Obtendo as coordenadas x e y da segunda estação do par no layout definido.
    x1, y1 = pos[caminho[i+1]]
    
    # Usando a função `plot` do Matplotlib para desenhar uma linha entre as duas estações.
    # A linha é desenhada em vermelho ('color='r'`) e tem largura 2 (`lw=2`), 
    # tornando-a mais espessa.
    plt.plot([x0, x1], [y0, y1], color='r', lw=2)

# Mostrando o gráfico final.
plt.show()


"""
Explicação:


há quatro estações: Alfa, Beta, Gama e Delta. Temos as seguintes 
rotas entre as estações:

    Estação Alfa -> Estação Beta: Duração de 4 horas.
    Estação Alfa -> Estação Gama: Duração de 2 horas.
    Estação Beta -> Estação Delta: Duração de -2 horas.
    Estação Gama -> Estação Delta: Duração de 3 horas.

Aqui, é crucial observar que a rota da Estação Beta para a Estação
Delta tem uma duração de -2 horas, o que significa que é uma rota
"rápida", onde, em vez de adicionar tempo à jornada, na verdade, você 
"ganha" 2 horas. Isto é para mostrar a capacidade do Bellman-Ford de 
lidar com pesos negativos.

Ao aplicar o algoritmo de Bellman-Ford, buscamos o caminho mais 
rápido (ou seja, de menor duração) da Estação Alfa para a Estação Delta:

    Caminho Direto através da Estação Gama: Alfa -> Gama -> Delta = 2 horas + 3 horas = 5 horas.
    Caminho através da Estação Beta: Alfa -> Beta -> Delta = 4 horas - 2 horas = 2 horas.

O caminho mais rápido é através da Estação Beta com um tempo total de 2 horas, 
graças à rota "rápida" da Estação Beta para a Estação Delta.

Na visualização, o caminho mais rápido é destacado em vermelho, mostrando 
claramente a rota ótima de Alfa -> Beta -> Delta.
"""
print()