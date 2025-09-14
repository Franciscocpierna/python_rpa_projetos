"""Grafos
            
            Algoritmos Clássicos

                Algoritmo de Kruskal para Árvores Geradoras Mínimas
                
                

O algoritmo de Kruskal é usado para encontrar uma árvore geradora 
mínima em um grafo conectado e ponderado. Uma árvore geradora mínima 
é um subgrafo que conecta todos os vértices do grafo original
sem formar ciclos e tem o menor peso total possível.

Vamos usar um exemplo prático envolvendo um sistema de distribuição de energia:

Enunciado:

Imagine que temos várias cidades e queremos conectá-las com linhas de transmissão
de energia. Cada possível conexão entre duas cidades tem um custo associado. 

Nosso objetivo é construir uma rede de transmissão que conecte todas as 
cidades e tenha o menor custo total.

Descrição do gráfico:

    Cidade A e Cidade B podem ser conectadas com um custo de $5.
    Cidade A e Cidade C podem ser conectadas com um custo de $10.
    Cidade A e Cidade D podem ser conectadas com um custo de $3.
    Cidade B e Cidade D podem ser conectadas com um custo de $7.
    Cidade C e Cidade D podem ser conectadas com um custo de $8.

Vamos agora codificar o exemplo:
"""

# Importando as bibliotecas necessárias
import networkx as nx
import matplotlib.pyplot as plt

# Importa a biblioteca NetworkX para manipulação de grafos
import networkx as nx

# Inicializa uma instância da classe Graph do NetworkX, que representa um grafo não-direcionado.
# Neste ponto, o grafo está vazio, sem vértices ou arestas.
grafo = nx.Graph()

# Utiliza o método 'add_edge' para adicionar uma aresta entre os vértices 'A' e 'B' com um peso de 5.
# Se 'A' e 'B' não existem ainda no grafo, eles são adicionados automaticamente.
grafo.add_edge('A', 'B', weight=5)

# Adiciona uma aresta entre 'A' e 'C' com um peso de 10.
# Novamente, se os vértices não existem, são adicionados.
grafo.add_edge('A', 'C', weight=10)

# Adiciona uma aresta entre 'A' e 'D' com um peso de 3.
grafo.add_edge('A', 'D', weight=3)

# Adiciona uma aresta entre 'B' e 'D' com um peso de 7.
grafo.add_edge('B', 'D', weight=7)

# Adiciona uma aresta final entre 'C' e 'D' com um peso de 8.
grafo.add_edge('C', 'D', weight=8)


# Utiliza a função 'minimum_spanning_edges' do NetworkX para obter
# as arestas que compõem a Árvore Geradora Mínima (AGM)
# do grafo usando o algoritmo de Kruskal.
# - O parâmetro 'algorithm="kruskal"' especifica que queremos usar o algoritmo de Kruskal.
# - O parâmetro 'data=True' garante que os dados associados a cada 
# aresta (como o peso) sejam retornados junto com a aresta.
arvore_geradora_minima = list(nx.minimum_spanning_edges(grafo, algorithm="kruskal", data=True))

# Imprime a mensagem inicial para indicar a listagem das arestas da AGM.
print("Arestas da Árvore Geradora Mínima:")

# Itera sobre cada aresta na árvore geradora mínima.
# Cada item (u, v, w) consiste em:
# - 'u' e 'v': os dois vértices que a aresta conecta.
# - 'w': um dicionário contendo os atributos da aresta (neste 
# caso, estamos interessados no peso, que é acessado com 'w['weight']').
for u, v, w in arvore_geradora_minima:
    
    # Imprime a aresta e seu peso no formato "(vértice1, vértice2): $peso".
    print(f"({u}, {v}): ${w['weight']}")
    

# Define a posição dos nós do grafo usando o "spring layout", 
# que posiciona os nós usando uma simulação de forças
# em que arestas são tratadas como molas que se repeliriam ou 
# atraem. Isso ajuda a distribuir os nós de forma que
# o grafo seja esteticamente agradável e fácil de entender.
pos = nx.spring_layout(grafo)

# Desenha o grafo na posição definida anteriormente.
# 'with_labels=True' indica que os rótulos (neste caso, os nomes) dos nós devem ser desenhados.
# 'node_color='lightblue'' define a cor de fundo dos nós.
nx.draw(grafo, pos, with_labels=True, node_color='lightblue')

# Obtém os pesos (atributos 'weight') de todas as arestas do grafo. 
# Isso nos dá um dicionário onde as chaves são pares de 
# nós (representando arestas) e os valores são os pesos correspondentes.
etiquetas_arestas = nx.get_edge_attributes(grafo, 'weight')


# Desenha as etiquetas (neste caso, os pesos) nas arestas do grafo.
# 'edge_labels=etiquetas_arestas' indica que as etiquetas das arestas 
# são os pesos que acabamos de obter.
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=etiquetas_arestas)


# Destaca as arestas que fazem parte da árvore geradora mínima.
# 'edgelist' especifica a lista de arestas que queremos desenhar. Neste caso, estamos construindo essa lista a partir 
# da árvore geradora mínima que foi calculada anteriormente.
# 'edge_color='r'' define a cor das arestas como vermelho, o que as destaca em relação às outras arestas.
# 'width=2' especifica a largura da linha usada para desenhar as arestas.
# nx.draw_networkx_edges(grafo, pos, edgelist=[(u, v) for u, v, w in arvore_geradora_minima], edge_color='r', width=2)

# Construir a lista de arestas que pertencem à árvore geradora mínima.
# Esta lista contém os pares de nós (u, v) que representam as arestas da árvore geradora mínima.
arestas_mst = [(u, v) for u, v, w in arvore_geradora_minima]

# Desenhar as arestas da árvore geradora mínima em destaque.
# 'edgelist' especifica quais arestas desenhar. Estamos fornecendo a lista que acabamos de construir.
# 'edge_color' define a cor das arestas (neste caso, vermelho).
# 'width' define a largura das linhas que representam as arestas. Um valor maior do que o padrão destaca as arestas.
nx.draw_networkx_edges(grafo, pos, edgelist=arestas_mst, edge_color='r', width=2)


# Exibe o grafo desenhado.
# Este comando é essencial quando se usa a biblioteca matplotlib para visualização, pois instrui o matplotlib a 
# renderizar e exibir o plot/gráfico que foi construído até agora.
plt.show()




"""
Neste exemplo, você verá o grafo com as possíveis conexões entre as cidades 
e a árvore geradora mínima destacada em vermelho, representando o menor custo 
total para conectar todas as cidades.


Resultado:

O algoritmo de Kruskal procura a árvore geradora mínima de um grafo conectado, 
ou seja, um subconjunto das arestas que conecta todos os vértices juntos sem
formar qualquer ciclo e com o peso total mínimo.

Neste exemplo, as arestas selecionadas para a árvore geradora mínima foram:

    ('A', 'D') com peso 3
    ('A', 'B') com peso 5
    ('B', 'D') com peso 7

Estas arestas foram selecionadas porque formam uma árvore (ou seja, não
têm ciclos) e têm o peso total mínimo possível, que é 15.


    Cidade A e Cidade B podem ser conectadas com um custo de $5.
    Cidade A e Cidade C podem ser conectadas com um custo de $10.
    Cidade A e Cidade D podem ser conectadas com um custo de $3.
    Cidade B e Cidade D podem ser conectadas com um custo de $7.
    Cidade C e Cidade D podem ser conectadas com um custo de $8.
"""
print()
