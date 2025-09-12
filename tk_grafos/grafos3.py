"""
grafo1.py, grafos2.py, grafos3.py Matriz de Adjacência,
Exercício - Grafo Direcionado e Representações Gráficas

Crie um código em Python que crie a Matriz de Adjacência, a 
Tabela de Arestas e o Gráfico com os dados abaixo:

Matriz de Adjacência:
+-----+---+---+---+---+---+
| V\V | 0 | 1 | 2 | 3 | 4 |
+-----+---+---+---+---+---+
|  0  | 0 | 1 | 1 | 0 | 0 |
|  1  | 0 | 0 | 0 | 1 | 0 |
|  2  | 0 | 0 | 0 | 0 | 1 |
|  3  | 0 | 0 | 0 | 0 | 1 |
|  4  | 0 | 0 | 0 | 0 | 0 |
+-----+---+---+---+---+---+

Tabela de Arestas:
+--------+---------+
| Origem | Destino |
+--------+---------+
|   0    |    1    |
|   0    |    2    |
|   1    |    3    |
|   2    |    4    |
|   3    |    4    |
+--------+---------+
"""

# Importa a biblioteca PrettyTable, que é usada para criar tabelas 
# com uma aparência bonita no console.
from prettytable import PrettyTable

# Importa a biblioteca NetworkX, que é usada para a criação, manipulação 
# e visualização de estruturas de grafos.
import networkx as nx

# Importa a biblioteca Matplotlib's pyplot, que é uma coleção de funções e
# estilos que fazem com que o Matplotlib funcione como o MATLAB, é usada para plotar o grafo.
import matplotlib.pyplot as plt


# Define uma classe chamada "GrafoDirecionado" para representar um grafo direcionado.
class GrafoDirecionado:
    
    # Método construtor da classe.
    # Ele é invocado quando criamos uma instância da classe e define as propriedades
    # iniciais do objeto.
    def __init__(self, numero_vertices):
        
        # Armazena o número de vértices do grafo.
        # Isso é necessário para criar a matriz de adjacência e saber quantas linhas 
        # e colunas ela terá.
        self.numero_vertices = numero_vertices
        
        # Cria a matriz de adjacência.
        # A matriz de adjacência é uma representação de um grafo onde o elemento 
        # M[i][j] é 1 se há uma aresta do vértice i para o vértice j, e 0 caso contrário.
        # Neste caso, estamos inicializando todos os elementos da matriz como 0, 
        # indicando que não há arestas no grafo inicialmente.
        # self.matriz_adjacencia = [[0 for j in range(numero_vertices)] for i in range(numero_vertices)]
        
        # Criando uma matriz de adjacência para representar um grafo.
        self.matriz_adjacencia = [
            
            # Para cada vértice 'i' em nosso grafo (representado pelo 
            # número total de vértices)
            [0 for j in range(numero_vertices)]
            
            # Estamos inicializando uma linha inteira com zeros. 
            # O zero indica que, inicialmente, não há arestas entre os vértices 'i' e 'j'.
            for i in range(numero_vertices)
            
            # Estamos fazendo isso para todos os vértices, criando assim uma matriz quadrada.
        ]

        
        # Lista para armazenar as arestas (ligações) do grafo.
        # Será útil para listar todas as arestas posteriormente e para visualizar o grafo.
        # Cada elemento da lista é uma tupla (i, j) representando uma aresta do vértice i para o vértice j.
        self.arestas = []
        
    # Método para adicionar uma aresta (ligação) direcionada ao grafo.
    # Ele recebe dois parâmetros: i e j, que são os vértices de origem e destino da aresta, respectivamente.
    def adiciona_aresta(self, i, j):
        
        # Verifica se os vértices de origem e destino são os mesmos.
        # Em outras palavras, está verificando se a aresta forma um laço, ou seja, começa e termina no mesmo vértice.
        if i == j:
            
            # Imprime uma mensagem de erro informando que laços (arestas que começam e terminam no mesmo vértice) não são permitidos neste grafo.
            print("Laços não são permitidos!")
            
            # Retorna prematuramente, terminando a execução do método sem fazer mais nada.
            # Isso é feito para evitar a adição da aresta inválida.
            return
        
        # Se não houver um laço, atualiza a matriz de adjacência.
        # O elemento da matriz na posição [i][j] é definido como 1, indicando 
        # a existência de uma aresta do vértice i para o vértice j.
        self.matriz_adjacencia[i][j] = 1
        
        # Adiciona a aresta à lista de arestas.
        # Isso é feito para manter um registro de todas as arestas 
        # adicionadas e facilitar outras operações, como a visualização do grafo.
        self.arestas.append((i, j))
        
        
    # O método especial "__str__" determina como o objeto será representado como uma string.
    # Isso é útil, por exemplo, quando você tenta imprimir o objeto usando a função print().
    def __str__(self):
        
        # Cria uma instância da classe PrettyTable.
        # PrettyTable é uma biblioteca que permite criar tabelas ASCII com uma aparência formatada e organizada.
        tabela = PrettyTable()
        
        # Define os nomes dos campos (colunas) da tabela.
        # O primeiro campo é "V\V", e os campos subsequentes são os números dos vértices do grafo.
        # A notação ["V\\V"] + [str(i) for i in range(self.numero_vertices)] cria uma lista que combina ["V\V"] com os números dos vértices convertidos para strings.
        # tabela.field_names = ["V\\V"] + [str(i) for i in range(self.numero_vertices)]
        
        # Configurando os nomes dos campos (ou cabeçalhos) para uma tabela.
        tabela.field_names = [
            
            # Primeira coluna da tabela terá o nome "V\V".
            "V\\V"
            
        ] + [
            
            # Para cada vértice 'i' em nosso grafo (representado pelo número total de vértices)
            # Convertendo o índice do vértice para uma string e adicionando-o à lista de nomes de campos.
            str(i) for i in range(self.numero_vertices)
            
            
        ]
        
        # Este loop percorre todos os vértices do grafo.
        for i in range(self.numero_vertices):
            
            # Adiciona uma linha à tabela para representar o vértice atual 'i'.
            # A primeira coluna da linha é o número do vértice 'i' (convertido para string).
            # As colunas subsequentes são os valores da linha correspondente na matriz de adjacência.
            # Juntos, eles representam as conexões do vértice 'i' com todos os outros vértices.
            tabela.add_row([str(i)] + self.matriz_adjacencia[i])
        
        # Retorna a representação da tabela como uma string.
        # Isso permite que, quando o objeto GrafoDirecionado for impresso ou convertido em string, seja exibida esta tabela.
        return str(tabela)
    
    
    # Método para criar e retornar uma tabela que mostra todas as arestas (ligações) do grafo.
    def tabela_arestas(self):
        
        # Cria uma nova instância da classe PrettyTable.
        # Esta biblioteca ajuda a formatar e exibir tabelas em formato ASCII de maneira limpa e organizada.
        tabela = PrettyTable()
        
        # Define os nomes dos campos (colunas) da tabela.
        # A tabela terá duas colunas: "Origem" para o vértice de origem da aresta e 
        # "Destino" para o vértice de destino da aresta.
        tabela.field_names = ["Origem", "Destino"]
        
        # Este loop percorre todas as arestas armazenadas na lista 'arestas' do objeto.
        for aresta in self.arestas:
            
            # Adiciona uma nova linha à tabela.
            # A linha contém dois elementos: o vértice de origem da aresta (aresta[0]) e o vértice de destino da aresta (aresta[1]).
            tabela.add_row([aresta[0], aresta[1]])
        
        # Retorna a representação da tabela em formato de string.
        # Isso permite que a tabela seja impressa ou convertida em uma string quando necessário.
        return str(tabela)
    
    
    # Método para visualizar o grafo como um diagrama.
    def visualizar(self):
        
        # Cria um objeto de grafo direcionado usando a biblioteca NetworkX.
        # NetworkX é uma biblioteca Python para criação, manipulação e estudo de estruturas de redes complexas.
        G = nx.DiGraph()  # Criar um grafo direcionado
        
        # Este loop percorre todas as arestas armazenadas na lista 'arestas' do objeto.
        for i, j in self.arestas:
            
            # Adiciona uma aresta ao objeto grafo G, de i para j.
            # Em outras palavras, estamos transferindo as arestas armazenadas em 
            # nossa estrutura para o objeto grafo da NetworkX.
            G.add_edge(i, j)
        
        # Define um dicionário para especificar as posições dos vértices (nós) no gráfico.
        # Isso é útil para manter uma representação gráfica consistente e clara.
        # Cada chave no dicionário representa um vértice, e o valor associado é uma 
        # tupla (x, y) que define a posição do vértice no gráfico.
        pos = {
            0: (0.5, 1),   # Vértice 0 está no centro superior
            1: (0, 0.5),   # Vértice 1 está no lado esquerdo, ao meio
            2: (1, 0.5),   # Vértice 2 está no lado direito, ao meio
            3: (0, 0),     # Vértice 3 está no canto inferior esquerdo
            4: (1, 0)      # Vértice 4 está no canto inferior direito
        }


        # Desenha o grafo G usando as posições definidas em 'pos' e várias outras opções de estilo.
        nx.draw(
            G,                    # Especifica que o grafo 'G' deve ser desenhado.
            pos=pos,              # Define as posições dos vértices (nós) conforme especificado anteriormente.
            with_labels=True,     # Exibe os rótulos (números) dos vértices.
            font_weight='bold',   # Define a espessura da fonte dos rótulos como 'bold' (negrito).
            node_color='skyblue', # Define a cor dos vértices como 'skyblue' (azul céu).
            node_size=1000,       # Define o tamanho dos vértices.
            edge_color='gray',    # Define a cor das arestas como cinza.
            arrows=True,          # Indica que as arestas devem ser desenhadas com setas para indicar direção.
            arrowstyle='-|>'      # Define o estilo das setas. '-|>' significa uma linha que termina com uma ponta de seta triangular.
        )
    
    # Exibe o gráfico.
    # Este é um comando da biblioteca matplotlib.pyplot, e ele renderiza 
    # e exibe o gráfico preparado.
    plt.show()

    
        
# Verifica se este script está sendo executado como um programa principal.
# A condição __name__ == "__main__" é usada para garantir que o código a seguir
# seja executado apenas quando o script for executado diretamente,
# e não quando for importado como um módulo em outro script.
if __name__ == "__main__":
    
    # Cria uma nova instância da classe GrafoDirecionado com 5 vértices.
    grafo = GrafoDirecionado(5)

    # Adiciona várias arestas (ligações entre vértices) ao grafo.
    grafo.adiciona_aresta(0, 1)
    grafo.adiciona_aresta(0, 2)
    grafo.adiciona_aresta(1, 3)
    grafo.adiciona_aresta(2, 4)
    grafo.adiciona_aresta(3, 4)

    # Imprime o texto "Matriz de Adjacência:" para o console.
    print("Matriz de Adjacência:")
    
    # Imprime a representação da matriz de adjacência do grafo.
    # Graças ao método __str__ definido na classe, podemos imprimir
    # o objeto diretamente para obter a matriz formatada.
    print(grafo)
    
    # Imprime uma linha em branco para separação visual.
    print("\nTabela de Arestas:")
    
    # Imprime a tabela que mostra todas as arestas do grafo.
    # O método tabela_arestas() retorna a representação da tabela em formato de string.
    print(grafo.tabela_arestas())
    
    # Exibe o grafo visualmente.
    # Isso abrirá uma janela (ou aba) mostrando o diagrama do grafo com vértices, arestas e direções.
    grafo.visualizar()



"""
Aqui, temos um grafo com 5 vértices. O vértice 0 está conectado
aos vértices 1 e 2, o vértice 1 está conectado ao vértice 3, o vértice
2 ao 4 e os vértices 3 e 4 também estão conectados. A matriz de adjacência 
reflete isso e o gráfico mostrará essas conexões visualmente.
"""
print()