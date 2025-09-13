# Importa a biblioteca 'networkx' com o apelido "rede".
# Esta biblioteca é utilizada para a criação, manipulação e estudo da estrutura de redes e grafos.
import networkx as rede

# Importa a biblioteca 'matplotlib.pyplot' com o apelido "grafico".
# Esta biblioteca é utilizada para plotar gráficos e visualizações em Python.
import matplotlib.pyplot as grafico

# Inicializa um grafo vazio do tipo simples (ou seja, sem direção nas conexões).
# Um grafo é uma estrutura que consiste de nós (também chamados de vértices) e conexões (arestas) entre estes nós.
grafo = rede.Graph()

# Adiciona conexões (arestas) ao grafo entre os nós indicados.
# A chamada 'add_edges_from' recebe uma lista de tuplas, onde cada tupla representa uma conexão.
# Por exemplo, ('A', 'B') indica uma conexão entre o nó 'A' e o nó 'B'.
# Neste código, nós 'A', 'B', 'C', 'D' e 'E' são adicionados ao grafo, e as conexões definidas são: 
# 'A' com 'B', 'A' com 'C', 'B' com 'D' e 'C' com 'E'.
grafo.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')])


# Definição da função de Busca em Largura (BFS - Breadth-First Search).
# Esta função realiza uma busca em largura em um grafo, começando a partir
# de um nó inicial especificado.
def busca_em_largura(grafo, no_inicio):
    
    # Cria uma lista vazia para armazenar os nós que já foram visitados.
    nos_visitados = []
    
    # Cria uma lista vazia que funcionará como uma fila.
    # Esta fila será utilizada para controlar a ordem de visita dos nós.
    fila = []
    
    # Adiciona o nó inicial às listas de nós visitados e à fila.
    nos_visitados.append(no_inicio)
    fila.append(no_inicio)

    # Cria uma lista vazia para armazenar a ordem de visita dos nós.
    ordem_visita = []

    # Enquanto houver elementos na fila, o loop continuará executando.
    while fila:
        
        # Remove e retorna o primeiro nó da fila, designando-o como o nó atual.
        no_atual = fila.pop(0)
        
        # Adiciona o nó atual à lista de ordem de visita.
        ordem_visita.append(no_atual)

        # Para cada vizinho do nó atual no grafo:
        for vizinho in grafo[no_atual]:
            
            # Se o vizinho ainda não foi visitado:
            if vizinho not in nos_visitados:
                
                # Adiciona o vizinho à lista de nós visitados.
                nos_visitados.append(vizinho)
                
                # Adiciona o vizinho ao final da fila.
                fila.append(vizinho)

    # Retorna a lista com a ordem de visita dos nós.
    return ordem_visita


# Chama a função busca_em_largura, passando o grafo e o nó 'A' como ponto de partida.
# O resultado (ordem de visita dos nós) é armazenado na variável "ordem".
ordem = busca_em_largura(grafo, 'A')

# Imprime a ordem de visita dos nós, obtida pela busca em largura.
print("Ordem de visita usando busca em largura:", ordem)


# Define as posições dos nós no desenho do grafo.
# Estas posições são coordenadas (x, y) para cada nó, permitindo
# que sejam desenhados em locais específicos.
posicoes = {'A': (0.5, 1), 'B': (0, 0.5), 'C': (1, 0.5), 'D': (0, 0), 'E': (1, 0)}

# Desenha os nós do grafo nas posições especificadas.
# Define a cor dos nós como azul claro ('lightblue') e o tamanho como 1000.
rede.draw_networkx_nodes(grafo, posicoes, node_color='lightblue', node_size=1000)

# Desenha as arestas (conexões) do grafo.
# A largura das arestas é definida como 1.0 e a transparência (alpha) como 0.5 (50% opaco).
rede.draw_networkx_edges(grafo, posicoes, width=1.0, alpha=0.5)

# Desenha os rótulos (nomes) dos nós nas posições especificadas.
# O tamanho da fonte dos rótulos é definido como 12.
rede.draw_networkx_labels(grafo, posicoes, font_size=12)

# Define o título da visualização do grafo.
grafico.title("Visualização do Grafo com Busca em Largura")

# Desativa os eixos x e y da visualização, para que o gráfico 
# fique mais limpo e focado apenas no grafo.
grafico.axis('off')

# Exibe o gráfico do grafo.
grafico.show()