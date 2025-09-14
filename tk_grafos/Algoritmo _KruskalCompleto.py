"""
Exemplo mais completo de Algoritmo de Kruskal para Árvores Geradoras Mínimas
"""

# Importando a biblioteca para trabalhar com grafos.
import networkx as nx

# Importando a biblioteca para visualização gráfica.
import matplotlib.pyplot as plt

# Inicializando um grafo não direcionado. Um grafo não direcionado não possui direção nas arestas.
grafo_cidades = nx.Graph()

# Adicionando uma aresta entre os vértices/nós 'A' e 'B' com um peso de 5.
grafo_cidades.add_edge('A', 'B', weight=5)

# Adicionando uma aresta entre os vértices/nós 'A' e 'C' com um peso de 10.
grafo_cidades.add_edge('A', 'C', weight=10)

# Adicionando uma aresta entre os vértices/nós 'A' e 'D' com um peso de 3.
grafo_cidades.add_edge('A', 'D', weight=3)

# Adicionando uma aresta entre os vértices/nós 'B' e 'D' com um peso de 7.
grafo_cidades.add_edge('B', 'D', weight=7)

# Adicionando uma aresta entre os vértices/nós 'B' e 'E' com um peso de 6.
grafo_cidades.add_edge('B', 'E', weight=6)

# Adicionando uma aresta entre os vértices/nós 'C' e 'E' com um peso de 9.
grafo_cidades.add_edge('C', 'E', weight=9)

# Adicionando uma aresta entre os vértices/nós 'C' e 'F' com um peso de 4.
grafo_cidades.add_edge('C', 'F', weight=4)

# Adicionando uma aresta entre os vértices/nós 'D' e 'F' com um peso de 2.
grafo_cidades.add_edge('D', 'F', weight=2)

# Adicionando uma aresta entre os vértices/nós 'D' e 'G' com um peso de 11.
grafo_cidades.add_edge('D', 'G', weight=11)

# Adicionando uma aresta entre os vértices/nós 'E' e 'H' com um peso de 12.
grafo_cidades.add_edge('E', 'H', weight=12)

# Adicionando uma aresta entre os vértices/nós 'E' e 'I' com um peso de 13.
grafo_cidades.add_edge('E', 'I', weight=13)

# Adicionando uma aresta entre os vértices/nós 'F' e 'J' com um peso de 1.
grafo_cidades.add_edge('F', 'J', weight=1)

# Adicionando uma aresta entre os vértices/nós 'G' e 'J' com um peso de 14.
grafo_cidades.add_edge('G', 'J', weight=14)

# Adicionando uma aresta entre os vértices/nós 'H' e 'I' com um peso de 15.
grafo_cidades.add_edge('H', 'I', weight=15)

# Adicionando uma aresta entre os vértices/nós 'I' e 'J' com um peso de 16.
grafo_cidades.add_edge('I', 'J', weight=16)


# Utilizar o algoritmo de Kruskal para encontrar a árvore geradora mínima do grafo 'grafo_cidades'.

# O conceito de uma "árvore geradora mínima" (AGM) é central em teoria dos grafos e aplicações práticas em redes.
# Uma AGM é um subconjunto de arestas de um grafo conectado, sem ciclos, que conecta todos os vértices juntos 
# com o mínimo de peso total.

# A biblioteca 'networkx' oferece uma função chamada 'minimum_spanning_edges' que retorna as arestas da AGM de um grafo.
# Essa função utiliza vários algoritmos para encontrar a AGM. Um dos mais populares é o algoritmo de Kruskal.

# Ao chamar a função:
# - Primeiro argumento: é o grafo para o qual queremos encontrar a AGM, que neste caso é 'grafo_cidades'.
# - 'algorithm="kruskal"': especifica que o algoritmo de Kruskal deve ser usado. Existem outros algoritmos possíveis, mas Kruskal é uma escolha comum.
# - 'data=True': indica que queremos que os dados associados a cada aresta (neste caso, o peso) sejam retornados junto com a aresta.

# A função 'minimum_spanning_edges' retorna um gerador, o que significa que não retorna todos os resultados de uma vez, 
# mas permite que você itere sobre eles um de cada vez. 
# Para converter esse gerador em uma lista (para que possamos trabalhar com os resultados mais facilmente ou referenciá-los várias vezes), 
# usamos a função 'list'.
arvore_minima = list(nx.minimum_spanning_edges(grafo_cidades, algorithm="kruskal", data=True))


# Calcular o custo total (ou peso) da árvore geradora mínima.

# Usamos uma compreensão de lista para iterar sobre cada aresta na árvore geradora mínima.
# Cada aresta na 'arvore_minima' é representada por uma tupla (cidade1, cidade2, peso).
# O underscore (_) é usado para descartar temporariamente os dois primeiros valores da tupla (cidade1 e cidade2), 
# já que estamos interessados apenas no 'peso'.
# O 'peso' é um dicionário que contém informações adicionais sobre a aresta. 
# Neste caso, estamos interessados no valor associado à chave 'weight', que representa o peso da aresta.
# 'sum()' é uma função que soma todos os valores produzidos pela compreensão de lista.
# O resultado é o custo total (ou peso) de todas as arestas na árvore geradora mínima.
custo_arvore_minima = sum(peso['weight'] for _, _, peso in arvore_minima)


# Exibir as arestas que fazem parte da árvore geradora mínima.
print("Arestas da Árvore Geradora Mínima:")

# Iterar sobre as arestas na árvore geradora mínima e exibir cada aresta junto com seu peso.

# A estrutura 'for' permite-nos percorrer cada aresta da 'arvore_minima'.
# Cada aresta é uma tupla que consiste em dois nós (representando as cidades) e um dicionário (peso).
# 'cidade1' e 'cidade2' representam os dois nós da aresta, enquanto 'peso' é um dicionário contendo informações adicionais sobre a aresta.

# No loop:
for cidade1, cidade2, peso in arvore_minima:
    
    # A função 'print' é usada para exibir a informação.

    # Usamos uma string formatada (f-string) para inserir os valores de 'cidade1', 'cidade2', e o peso da aresta 
    # diretamente na string a ser impressa.
    # Dentro da f-string, {cidade1} e {cidade2} são substituídos pelos nomes das cidades da aresta atual.
    # {peso['weight']} acessa o valor associado à chave 'weight' no dicionário 'peso', que é o peso da aresta.
    # O resultado final é uma string que mostra as duas cidades conectadas pela aresta e o peso dessa conexão.
    print(f"({cidade1}, {cidade2}): ${peso['weight']}")


# Exibir o custo total (ou peso) da árvore geradora mínima.
print(f"Custo total da Árvore Geradora Mínima: ${custo_arvore_minima}")


# Desenhar o grafo 'grafo_cidades'.

# Utilizar o layout de mola (spring layout) para determinar a posição dos nós no gráfico.
# O layout de mola posiciona os nós usando um sistema de forças simuladas.
# Em termos simples, ele faz com que os nós que estão diretamente conectados fiquem próximos,
# enquanto os nós que não estão conectados se repelem.
posicionamento = nx.spring_layout(grafo_cidades)

# Usar a função 'nx.draw()' para desenhar o grafo.
# 'grafo_cidades' é o grafo que queremos desenhar.
# 'posicionamento' é um dicionário que mapeia cada nó para uma posição no plano.
# 'with_labels=True' indica que os nós devem ser rotulados com seus nomes.
# 'node_color' define a cor dos nós. Aqui, todos os nós são coloridos de azul claro ('lightblue').
nx.draw(grafo_cidades, posicionamento, with_labels=True, node_color='lightblue')

# Obter as etiquetas (pesos) das arestas/conexões do grafo 'grafo_cidades'.
# 'nx.get_edge_attributes()' é uma função que recupera os atributos das arestas.
# Aqui, estamos interessados nos pesos das arestas, que é indicado pelo atributo 'weight'.
etiquetas_conexoes = nx.get_edge_attributes(grafo_cidades, 'weight')

# Desenhar as etiquetas (pesos) nas arestas/conexões do grafo.
# 'grafo_cidades' é o grafo que estamos desenhando.
# 'posicionamento' é o dicionário que mapeia cada nó para uma posição no plano.
# 'edge_labels' é um dicionário que mapeia cada aresta para seu peso.
# Portanto, cada conexão/aresta será rotulada com seu respectivo peso.
nx.draw_networkx_edge_labels(grafo_cidades, posicionamento, edge_labels=etiquetas_conexoes)


# Destacar a Árvore Geradora Mínima no grafo.

# Utilizar a função 'nx.draw_networkx_edges()' para desenhar apenas as arestas da árvore geradora mínima.
# 'grafo_cidades' é o grafo no qual estamos trabalhando.
# 'posicionamento' define a posição de cada nó no gráfico.
# 'edgelist=arvore_minima' especifica que queremos desenhar apenas as arestas presentes na árvore geradora mínima.
# 'edge_color="vermelho"' define a cor das arestas da árvore geradora mínima como vermelho. 
# (Nota: o correto seria 'edge_color="red"' para que a cor seja de fato reconhecida como vermelho.)
# 'width=2' define a largura das linhas das arestas para 2, tornando-as mais destacadas.
nx.draw_networkx_edges(grafo_cidades, posicionamento, edgelist=arvore_minima, edge_color='red', width=2)

# Exibir o gráfico desenhado.
# 'plt.show()' é uma função da biblioteca matplotlib que exibe a figura atual.
# Ela renderiza o gráfico na tela, permitindo visualizar todas as adições e modificações feitas anteriormente.
plt.show()


"""
No exemplo acima, temos 10 cidades (A a J) com várias conexões e pesos entre
elas. Depois de aplicar o algoritmo de Kruskal, obtemos a árvore geradora 
mínima. Ao visualizar o grafo, as arestas pertencentes à árvore geradora 
mínima são destacadas em vermelho.
"""
print()