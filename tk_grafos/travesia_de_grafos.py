"""
Grafos
            
            
        Travessias de Grafos

            Busca em Largura (BFS)
            

Travessias de grafos são técnicas que permitem visitar todos os 
vértices de um grafo de maneira sistemática. Estas travessias são 
fundamentais em muitos problemas de grafos, pois fornecem um meio
para inspecionar cada vértice e cada aresta.

Busca em Largura (BFS - Breadth-First Search) é uma das técnicas mais 
conhecidas para travessia de grafos.

Aqui está uma breve descrição da BFS:

Conceito:
A BFS explora o grafo em "camadas". Ela começa no vértice inicial e explora
todos os vértices vizinhos no mesmo nível de profundidade antes de se mover 
para os vértices no próximo nível de profundidade.

Mecanismo:

    - Comece com um nó inicial e marque-o como visitado.
    - Coloque este nó em uma fila.
    - Enquanto a fila não estiver vazia:
        - Remova um nó da fila.
        - Para cada vizinho desse nó:
            Se o vizinho não foi visitado:
                Marque-o como visitado.
                Coloque-o na fila.

Utilidades e Aplicações da BFS:

    - Descoberta do caminho mais curto: Em um grafo não ponderado, a BFS pode 
        ser usada para encontrar o caminho mais curto entre dois nós.
    
    - Análise de redes sociais: Por exemplo, pode ser usada para encontrar 
        amigos em um certo nível de separação.
        
    - Algoritmos de roteamento de rede: Como o algoritmo de roteamento OSPF.
    - Verificar a conectividade: Para verificar se um grafo é conectado ou não.
    - Resolução de quebra-cabeças: Como o quebra-cabeça do tipo "Deslizar", onde há 
        movimentos legais que podem ser interpretados como arestas e configurações 
        do tabuleiro como vértices.

Características da BFS:

    A BFS não é recursiva.
    Utiliza uma estrutura de dados de fila para manter o registro dos vértices 
        que precisam ser explorados.
    É garantido que a BFS visite os vértices mais próximos do nó inicial antes 
        de visitar vértices mais distantes.

Em resumo, a BFS é uma abordagem sistemática para explorar todos os vértices de um grafo, 
começando pelo vértice inicial e movendo-se em ondas através dos vértices, de acordo com 
sua proximidade ao ponto de partida.


                
Vamos dar um exemplo prático da Busca em Largura (BFS - Breadth First 
Search) utilizando a biblioteca NetworkX em Python.

Exemplo Prático:

Suponha que temos um grafo representando uma rede de amigos, e queremos 
saber a ordem em que os amigos seriam visitados se começarmos com uma pessoa 
específica e visitarmos seus amigos, depois os amigos de seus amigos e assim por diante.

Grafo:

  A
 / \
B   C
|   |
D   E

Aqui, "A" tem dois amigos "B" e "C". 
      "B" tem um amigo "D" e 
      "C" tem um amigo "E".

Vamos fazer a BFS começando pelo vértice "A".

"""

# Importa a biblioteca 'networkx', que é usada para a criação, 
# manipulação e estudo de estruturas
# de redes complexas (grafos). O "nx" é um apelido comum para
# simplificar chamadas subsequentes.
import networkx as nx

# Inicializa um novo grafo vazio. Neste caso, estamos criando 
# um grafo não-direcionado.
grafo = nx.Graph()

# Adiciona arestas ao grafo. Uma aresta é uma ligação entre dois nós.
# A função 'add_edges_from' permite adicionar múltiplas arestas de uma vez.
# Aqui, estamos adicionando arestas que ligam os 
# nós 'A' e 'B', 'A' e 'C', 'B' e 'D' e 'C' e 'E'.
grafo.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E')])


# Definição da função de Busca em Largura (BFS - Breadth-First Search).
# A função recebe um grafo e um nó inicial como parâmetros.
def busca_em_largura(grafo, no_inicial):

    # Lista que vai conter os nós que já foram visitados.
    nos_visitados = []

    # Lista que ajuda a controlar os próximos nós a serem visitados.
    # Funciona como uma fila, onde o primeiro nó inserido é o primeiro a ser retirado.
    fila = []

    # Adiciona o nó inicial à lista de nós visitados e à fila.
    nos_visitados.append(no_inicial)
    fila.append(no_inicial)

    # Continua o processo enquanto houver nós na fila para serem visitados.
    while fila:

        # Retira o primeiro nó da fila para ser o nó atualmente visitado.
        no_atual = fila.pop(0)

        # Imprime o nome do nó que está sendo visitado.
        print(no_atual, end=" -> ")
        
        # Loop para visitar cada vizinho (nó adjacente) do nó atual.
        for vizinho in grafo[no_atual]:

            # Verifica se o vizinho ainda não foi visitado.
            if vizinho not in nos_visitados:

                # Se o vizinho não foi visitado, ele é adicionado à lista de visitados.
                nos_visitados.append(vizinho)

                # E também é adicionado à fila para ser visitado em seguida.
                fila.append(vizinho)
                
                
# Imprime uma mensagem para indicar que a ordem de visita dos nós do grafo será mostrada
# usando o algoritmo de busca em largura (BFS).
print("Ordem de visita usando busca em largura:")

# Chama a função 'busca_em_largura' passando o grafo criado
# anteriormente e o nó 'A' como nó inicial.
# A função vai imprimir a ordem em que os nós são 
# visitados, começando pelo nó 'A'.
busca_em_largura(grafo, 'A')


"""
Por que o caminho mais curto é: A B C D E ?

Quando falamos de "caminho mais curto" em um grafo não ponderado 
usando a Busca em Largura (BFS), estamos nos referindo ao número
mínimo de arestas que precisamos atravessar para ir de um vértice a outro.

No grafo:

  A
 / \
B   C
|   |
D   E

Vamos descrever a ordem em que a BFS visita os vértices, 
começando pelo vértice A:

    - A é o ponto de partida.
    - A partir de A, os vizinhos mais próximos são B e C. A ordem 
        exata entre B e C pode variar dependendo de como os vizinhos 
        são armazenados e recuperados, mas suponhamos que B venha antes 
        de C. Portanto, B é visitado e depois C.
    
    - Após B e C, os próximos vértices na fila são D e E. D é o vizinho 
        de B e E é o vizinho de C. Novamente, a ordem entre D e E pode 
        variar, mas suponhamos que D venha antes de E. Portanto, D é visitado 
        e depois E.

Então, a ordem de visita é: A → B → C → D → E.

Essa ordem representa a menor quantidade de arestas que precisamos atravessar 
para chegar a cada vértice a partir de A. Por exemplo, para ir de A para D, precisamos 
passar por B, fazendo um total de 2 arestas. Mesmo conceito para E: de A para E 
passamos por C, totalizando 2 arestas.

Essa é a essência da BFS em grafos não ponderados: ela garante que visitamos todos
os vértices à mesma distância do ponto de partida antes de visitarmos os vértices 
que estão a uma maior distância.
"""
print()