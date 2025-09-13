"""
Grafos
            
        Travessias de Grafos

            Busca em Profundidade (DFS)
            
A Busca em Profundidade (DFS - Depth First Search) é um algoritmo 
de travessia de grafo que visita todos os vértices de um grafo ou 
árvore em profundidade, seguindo tão longe quanto possível ao longo 
de cada ramo antes de retroceder. Aqui está um exemplo prático de 
como a DFS funciona:

Grafo Exemplificado:

Vamos considerar o seguinte grafo:

  A
 / \
B   C
|   |
D   E

A representação do grafo acima em uma lista de adjacências seria:

A -> [B, C]
B -> [D]
C -> [E]
D -> []
E -> []

Algoritmo de Busca em Profundidade (DFS):

Vamos começar a busca no vértice A.

    - Visite o vértice A.
    - Mova-se para um vértice adjacente de A. Digamos, B.
    - Visite o vértice B.
    - Mova-se para um vértice adjacente de B. No caso, D.
    - Visite o vértice D. Como D não tem adjacentes não visitados, retornamos.
    - Volte para A e visite o próximo vértice adjacente, C.
    - Visite o vértice C.
    - Mova-se para um vértice adjacente de C. No caso, E.
    - Visite o vértice E.

Ordem de visitação: A, B, D, C, E.
Código Python para DFS:
"""

# Função que implementa o algoritmo de Busca em 
# Profundidade (DFS - Depth-First Search).
# Ela percorre o grafo começando por um vértice 
# específico e explorando o mais profundamente possível
# antes de retroceder.
def busca_em_profundidade(grafo, vertice_atual, vertices_visitados=[]):
    
    # Verifica se o vértice atual ainda não foi visitado.
    if vertice_atual not in vertices_visitados:
        
        # Adiciona o vértice atual à lista de vértices visitados.
        vertices_visitados.append(vertice_atual)
        
        # Itera sobre os vértices vizinhos do vértice atual.
        for vizinho in grafo[vertice_atual]:
            
            # Realiza uma chamada recursiva da função para explorar 
            # os vizinhos do vértice atual.
            busca_em_profundidade(grafo, vizinho, vertices_visitados)
    
    # Retorna a lista de vértices visitados ao final da execução.
    return vertices_visitados
    
    
# Representação do grafo em forma de lista de adjacências.
# Chave é o vértice e o valor é uma lista dos vértices vizinhos.
grafo_representacao = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

# Realiza uma chamada da função de busca em profundidade começando pelo vértice 'A'.
sequencia_visita = busca_em_profundidade(grafo_representacao, 'A')

# Imprime a sequência de vértices visitados pelo algoritmo de busca em profundidade.
print("Ordem de visitação:", sequencia_visita)