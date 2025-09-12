"""
Estruturas de Dados Não-Lineares
    
        Árvores
            
            Árvore Vermelho-Preto
            
As árvores Vermelho-Preto (Red-Black Trees) são uma forma de 
árvore de busca binária equilibrada. Elas mantêm seu equilíbrio 
através de uma série de rotações e alterações de cor em nós durante 
as operações de inserção e remoção.

Cada nó na árvore tem uma cor (vermelho ou preto) associada a ele, e 
há algumas propriedades que devem ser satisfeitas para a árvore ser 
considerada uma árvore Vermelho-Preto:

    Cada nó é vermelho ou preto.
    A raiz é sempre preta.
    Todos os nós folha (NIL ou nulo) são pretos.
    Se um nó vermelho tem filhos, então os filhos são sempre pretos.
    Cada caminho da raiz a qualquer nó folha contém o mesmo número de nós pretos.

A seguir, está um exemplo simples de implementação de uma Árvore Vermelho-Preto:
"""

# Importa a biblioteca NetworkX, que fornece estruturas de dados 
# para grafos e funções para análise e visualização de grafos.
import networkx as nx

# Importa a biblioteca Matplotlib, que fornece funções para criar visualizações 
# estáticas, animadas e interativas em Python.
import matplotlib.pyplot as plt

# Define uma classe chamada "No", que representa um nó da árvore.
class No:
    
    # O método de inicialização "__init__" é chamado automaticamente quando um
    # novo objeto "No" é criado.
    def __init__(self, dado, cor, pai=None):
        
        # "self" é uma referência ao objeto instância atual da classe e é 
        # usado para acessar as variáveis que pertencem à classe.

        # Atribui o valor passado como argumento "dado" para o atributo "dado" do nó.
        # Este atributo armazenará o valor contido no nó.
        self.dado = dado
        
        # Atribui o valor passado como argumento "cor" para o atributo "cor" do nó.
        # Este atributo determinará a cor do nó (geralmente usado em árvores 
        # Rubro-Negras para indicar se um nó é vermelho ou preto).
        self.cor = cor
        
        # Atribui o valor passado como argumento "pai" para o atributo "pai" do nó.
        # Este atributo mantém uma referência ao nó pai do nó atual.
        # O valor padrão é "None", indicando que, por padrão, um nó não tem pai a 
        # menos que especificado.
        self.pai = pai
        
        # Define o atributo "esquerda" como "None".
        # Este atributo manterá uma referência ao filho esquerdo do nó atual.
        self.esquerda = None
        
        # Define o atributo "direita" como "None".
        # Este atributo manterá uma referência ao filho direito do nó atual.
        self.direita = None
        
        
# Define uma classe chamada "ArvoreVermelhoPreto", que representa uma árvore Rubro-Negra.
# Árvores Rubro-Negras são árvores binárias de busca auto-balanceadas, onde cada 
# nó tem uma cor (vermelho ou preto).
# Elas mantêm o equilíbrio ao pintar cada nó de uma das duas cores e garantem que
# a árvore satisfaça certas propriedades coloridas.
class ArvoreVermelhoPreto:
    
    # O método de inicialização "__init__" é chamado automaticamente quando um 
    # novo objeto "ArvoreVermelhoPreto" é criado.
    def __init__(self):
        
        # "self" é uma referência ao objeto instância atual da classe e é usado 
        # para acessar as variáveis que pertencem à classe.
        
        # Define o atributo "raiz" como "None".
        # A "raiz" é o ponto de partida da árvore. Quando a árvore é criada, ela está 
        # vazia, portanto, a raiz é "None".
        self.raiz = None
        
        
    # Define um método privado chamado "_rotacao_esquerda".
    # A rotação à esquerda é uma operação fundamental para manter 
    # a árvore Rubro-Negra balanceada após inserções e remoções.
    def _rotacao_esquerda(self, no):

        # Armazena o nó filho à direita do nó atual em uma variável temporária chamada "temp".
        # O nó à direita será movido para a posição do nó atual após a rotação.
        temp = no.direita

        # Atualiza o filho direito do nó atual para ser o filho esquerdo de "temp".
        no.direita = temp.esquerda

        # Se o filho esquerdo de "temp" existir, atualiza o pai desse filho para ser o nó atual.
        if temp.esquerda:
            temp.esquerda.pai = no

        # Atualiza o pai do nó "temp" para ser o pai do nó atual.
        temp.pai = no.pai

        # Se o nó atual não tiver um pai (ou seja, se for a raiz da árvore),
        # atualiza a raiz da árvore para ser "temp".
        if not no.pai:
            self.raiz = temp
            
        # Se o nó atual for o filho esquerdo de seu pai, atualiza o filho
        # esquerdo do pai para ser "temp".
        elif no == no.pai.esquerda:
            no.pai.esquerda = temp
            
        # Caso contrário, o nó atual deve ser o filho direito de 
        # seu pai, então atualiza o filho direito do pai para ser "temp".
        else:
            no.pai.direita = temp

        # Define o filho esquerdo de "temp" para ser o nó atual.
        temp.esquerda = no

        # Atualiza o pai do nó atual para ser "temp".
        no.pai = temp
        
        
    # Define um método privado chamado "_rotacao_direita".
    # A rotação à direita é outra operação fundamental para 
    # manter a árvore Rubro-Negra balanceada após inserções e remoções.
    def _rotacao_direita(self, no):

        # Captura o filho à esquerda do nó atual e o armazena em uma 
        # variável temporária chamada "temp".
        # Isso porque, na rotação à direita, o filho esquerdo atual do nó 
        # será movido para a posição do nó original.
        temp = no.esquerda

        # Atualiza o filho esquerdo do nó atual para ser o filho direito de "temp".
        # Esta ação desloca o filho direito do nó que estamos rotacionando (temp) para
        # a esquerda do nó atual.
        no.esquerda = temp.direita

        # Se o filho direito de "temp" existir, atualiza o pai
        # desse filho para apontar para o nó atual.
        # Isso garante que o nó direito de "temp" conheça seu novo 
        # pai após a rotação.
        if temp.direita:
            temp.direita.pai = no

        # Atualiza o pai do nó "temp" para ser o pai do nó atual.
        # Isso garante que "temp" tenha o mesmo pai que o nó original tinha antes da rotação.
        temp.pai = no.pai

        # Se o nó atual não tiver um pai (ou seja, se ele for a raiz da árvore),
        # atualiza a raiz da árvore para ser "temp" pois após a 
        # rotação, "temp" ocupará a posição do nó original.
        if not no.pai:
            self.raiz = temp
            
        # Se o nó atual for o filho esquerdo de seu pai, atualiza o 
        # filho esquerdo do pai para ser "temp".
        # Isso garante que o pai do nó original aponte para "temp" após a rotação.
        elif no == no.pai.esquerda:
            no.pai.esquerda = temp
            
        # Caso contrário, o nó atual deve ser o filho direito de seu pai. 
        # Nesse caso, atualiza o filho direito do pai para ser "temp".
        else:
            no.pai.direita = temp

        # Agora, movemos o nó original (que estava acima de "temp") para a direita de "temp".
        temp.direita = no

        # Finalmente, atualiza o pai do nó original para ser "temp", completando a rotação.
        no.pai = temp
        
        
    # Define o método "inserir" que é responsável por inserir um novo
    # valor na árvore Rubro-Negra.
    def inserir(self, valor):

        # Se a árvore está vazia (i.e., não possui uma raiz).
        if not self.raiz:
            
            # Cria um novo nó com o valor fornecido e define sua cor como "preto".
            # A raiz de uma árvore Rubro-Negra deve sempre ser preta.
            self.raiz = No(valor, "preto")
            
        else:
            
            # Se a árvore não está vazia, chama o método auxiliar "_inserir" 
            # para inserir o valor na posição correta.
            self._inserir(self.raiz, valor)

            # Após inserir o novo valor, chama o método "balancear" para garantir 
            # que a árvore continue obedecendo as propriedades Rubro-Negras.
            # O balanceamento começa a partir da raiz.
            self.balancear(self.raiz)
            
            
    # Define o método "balancear", que ajusta a cor dos nós e realiza rotações para
    # manter as propriedades da árvore Rubro-Negra após a inserção.
    def balancear(self, no):

        # Inicia um loop que continuará enquanto o nó possuir um 
        # pai e a cor do pai for vermelha.
        # Isso ocorre porque inserir um nó vermelho sob outro nó 
        # vermelho viola as propriedades da árvore Rubro-Negra.
        while no.pai and no.pai.cor == "vermelho":

            # Se o pai do nó atual for o filho esquerdo de seu avô.
            if no.pai == no.pai.pai.esquerda:

                # O tio é definido como o filho direito do avô.
                tio = no.pai.pai.direita

                # Se o tio existe e sua cor é vermelha.
                if tio and tio.cor == "vermelho":
                    
                    # Altera a cor do pai e do tio para preto e a cor do avô para vermelho.
                    # Essa re-coloração move a violação Rubro-Negra para cima na árvore.
                    no.pai.cor = "preto"
                    tio.cor = "preto"
                    no.pai.pai.cor = "vermelho"

                    # Atualiza o nó para o avô e continua o loop.
                    no = no.pai.pai
                    
                else:
                    
                    # Se o nó for o filho direito do pai.
                    if no == no.pai.direita:
                        
                        # Atualiza o nó para o pai e realiza uma rotação à esquerda no nó.
                        no = no.pai
                        self._rotacao_esquerda(no)

                    # Altera a cor do pai para preto e a cor do avô para vermelho.
                    no.pai.cor = "preto"
                    no.pai.pai.cor = "vermelho"

                    # Realiza uma rotação à direita no avô.
                    self._rotacao_direita(no.pai.pai)

            # Caso o pai do nó atual seja o filho direito de seu
            # avô (caso simétrico ao anterior).
            else:
                
                # O tio é definido como o filho esquerdo do avô.
                tio = no.pai.pai.esquerda

                # Se o tio existe e sua cor é vermelha.
                if tio and tio.cor == "vermelho":
                    
                    # Altera a cor do pai e do tio para preto e a cor do avô para vermelho.
                    no.pai.cor = "preto"
                    tio.cor = "preto"
                    no.pai.pai.cor = "vermelho"

                    # Atualiza o nó para o avô e continua o loop.
                    no = no.pai.pai
                    
                else:
                    
                    # Se o nó for o filho esquerdo do pai.
                    if no == no.pai.esquerda:
                        
                        # Atualiza o nó para o pai e realiza uma rotação à direita no nó.
                        no = no.pai
                        self._rotacao_direita(no)

                    # Altera a cor do pai para preto e a cor do avô para vermelho.
                    no.pai.cor = "preto"
                    no.pai.pai.cor = "vermelho"

                    # Realiza uma rotação à esquerda no avô.
                    self._rotacao_esquerda(no.pai.pai)

        # Garante que a raiz da árvore seja sempre preta, conforme a 
        # propriedade da árvore Rubro-Negra.
        self.raiz.cor = "preto"
            
            
    # Define o método "_inserir" que é um método auxiliar para a inserção 
    # de um novo valor na árvore Rubro-Negra.
    def _inserir(self, no_atual, valor):

        # Verifica se o valor a ser inserido é menor que o dado no nó atual.
        if valor < no_atual.dado:
            
            # Se o nó atual tem um filho à esquerda.
            if no_atual.esquerda:
                
                # Faz uma chamada recursiva ao método "_inserir" para 
                # continuar a busca pela posição correta para inserção na subárvore esquerda.
                self._inserir(no_atual.esquerda, valor)
                
            else:
                
                # Se o nó atual não tem um filho à esquerda, cria um novo nó 
                # com o valor fornecido e cor "vermelho",
                # e define este nó como filho esquerdo do nó atual.
                no_atual.esquerda = No(valor, "vermelho", no_atual)

                # Chama o método "balancear" para garantir que a subárvore esquerda
                # continue obedecendo as propriedades Rubro-Negras após a inserção.
                self.balancear(no_atual.esquerda)
            
            
        # Verifica se o valor a ser inserido é maior que o dado no nó atual.
        elif valor > no_atual.dado:
            
            # Se o nó atual tem um filho à direita.
            if no_atual.direita:
                
                # Faz uma chamada recursiva ao método "_inserir" para continuar 
                # a busca pela posição correta para inserção na subárvore direita.
                self._inserir(no_atual.direita, valor)
                
            else:
                
                # Se o nó atual não tem um filho à direita, cria um novo 
                # nó com o valor fornecido e cor "vermelho",
                # e define este nó como filho direito do nó atual.
                no_atual.direita = No(valor, "vermelho", no_atual)

                # Chama o método "balancear" para garantir que a subárvore
                # direita continue obedecendo as propriedades Rubro-Negras após a inserção.
                self.balancear(no_atual.direita)
        
    
# Define a função 'adicionar_ao_grafo' que é uma função auxiliar para 
# adicionar nós e arestas de uma árvore Rubro-Negra a um grafo do NetworkX.
def adicionar_ao_grafo(no, G):
    
    # Verifica se o nó passado como argumento não é None.
    # Isso serve para garantir que a função não tente adicionar nós vazios ao grafo.
    if no is not None:
        
        # Adiciona o nó atual ao grafo 'G'. A cor e o valor do nó são armazenados
        # como atributos do nó no grafo.
        G.add_node(no, color=no.cor, valor=no.dado)
        
        # Verifica se o nó atual tem um nó pai.
        if no.pai:
            
            # Se tiver, adiciona uma aresta entre o nó pai e o nó atual ao grafo 'G'.
            G.add_edge(no.pai, no)
        
        # Chama a função 'adicionar_ao_grafo' recursivamente para o 
        # filho esquerdo do nó atual.
        adicionar_ao_grafo(no.esquerda, G)
        
        # Chama a função 'adicionar_ao_grafo' recursivamente para o 
        # filho direito do nó atual.
        adicionar_ao_grafo(no.direita, G)
        
        
# Define a função 'converter_cores_para_ingles' que converte uma lista de
# cores do português para o inglês.
def converter_cores_para_ingles(cores):

    # Cria um dicionário para mapear as cores do português para o inglês.
    # A chave do dicionário é a cor em português e o valor correspondente é a 
    # tradução para o inglês.
    mapeamento_cores = {
        "preto": "black",    # Mapeia "preto" para "black"
        "vermelho": "red"    # Mapeia "vermelho" para "red"
    }

    # Usa uma compreensão de lista para criar uma nova lista.
    # Para cada cor na lista 'cores' fornecida como argumento, o valor 
    # correspondente no dicionário 'mapeamento_cores' é obtido.
    # O resultado é uma nova lista de cores traduzidas para o inglês.
    return [mapeamento_cores[cor] for cor in cores]


# Inicializa uma variável global 'ordem_no' para manter a ordem 
# dos nós conforme são visitados.
ordem_no = 0


# Define a função 'calcular_posicoes' que calcula as posições x e y 
# de cada nó em uma árvore binária para visualização gráfica.
def calcular_posicoes(raiz, pos={}, y=0):
    
    # Usa a palavra-chave 'global' para indicar que estamos nos 
    # referindo à variável global 'ordem_no' e não criando uma nova.
    global ordem_no

    # Verifica se o nó atual (raiz) é válido.
    if raiz is not None:

        # Primeiro, visita a subárvore à esquerda do nó atual (travessia em ordem).
        calcular_posicoes(raiz.esquerda, pos, y - 1)

        # Atribui a posição (x, y) ao nó atual:
        # x é baseado na ordem em que o nó é visitado (ordem_no).
        # y é baseado na profundidade do nó na árvore (quanto mais
        # profundo, menor o valor de y).
        pos[raiz] = (ordem_no, y)

        # Incrementa a ordem do nó para que o próximo nó visitado tenha um valor x maior.
        ordem_no += 1

        # Por último, visita a subárvore à direita do nó atual.
        calcular_posicoes(raiz.direita, pos, y - 1)

    # Retorna o dicionário 'pos', que mapeia cada nó para sua posição (x, y).
    return pos
        
        
        
# Define a função 'desenhar_arvore' que visualiza uma árvore Vermelho-Preto.
def desenhar_arvore(arvore):

    # Cria um grafo direcionado usando a biblioteca NetworkX.
    G = nx.DiGraph()

    # Chama a função 'adicionar_ao_grafo' para adicionar nós e arestas ao
    # grafo G a partir da árvore fornecida.
    adicionar_ao_grafo(arvore.raiz, G)

    # Coleta as cores de fundo de cada nó no grafo, usando atributos do nó.
    # cores_fundo = [nx.get_node_attributes(G, 'color')[no] for no in G.nodes()]
    
    # Inicializa uma lista vazia chamada cores_fundo para armazenar as cores de fundo dos nós.
    cores_fundo = []

    # Itera sobre todos os nós do grafo G.
    for no in G.nodes():

        # Para cada nó, obtém o atributo 'color' usando a função nx.get_node_attributes
        # e acessa a cor do nó atual usando [no].
        cor = nx.get_node_attributes(G, 'color')[no]

        # Adiciona a cor do nó atual à lista cores_fundo.
        cores_fundo.append(cor)


    # Converte as cores de fundo de português para inglês usando a função
    # 'converter_cores_para_ingles'.
    cores_fundo = converter_cores_para_ingles(cores_fundo)

    # Define as cores de borda dos nós com base na cor de fundo (nós pretos 
    # têm borda branca e nós vermelhos têm borda preta).
    # cores_borda = ['white' if cor == 'black' else 'black' for cor in cores_fundo]
    
    # Inicializa uma lista vazia chamada cores_borda para armazenar as cores de borda dos nós.
    cores_borda = []

    # Itera sobre cada cor na lista cores_fundo.
    for cor in cores_fundo:

        # Verifica se a cor atual é 'black' (preto).
        if cor == 'black':

            # Se a cor do nó for 'black', define a cor da borda como 'white' (branco).
            cores_borda.append('white')
            
        else:

            # Se a cor do nó não for 'black', define a cor da borda como 'black' (preto).
            cores_borda.append('black')


    # Calcula as posições dos nós na visualização usando a função 'calcular_posicoes'.
    pos = calcular_posicoes(arvore.raiz)

    # Desenha o grafo usando a biblioteca NetworkX.
    # Define várias propriedades visuais, como cores de nó, tamanho do nó, cor da aresta, etc.
    # nx.draw(G, pos, with_labels=False, node_color=cores_fundo, node_size=1000, edge_color='black', width=1.5, edgecolors=cores_borda, linewidths=2)
    nx.draw(
        G,                                  # O grafo a ser desenhado.
        pos,                                # Um dicionário com as posições dos nós. As chaves são os nós e os valores são as coordenadas (x, y).
        with_labels=False,                   # Especifica se os nós devem ser rotulados com seus identificadores (neste caso, não).
        node_color=cores_fundo,              # Define as cores de fundo dos nós, baseado na lista cores_fundo.
        node_size=1000,                      # Define o tamanho dos nós. Neste caso, cada nó terá um tamanho de 1000.
        edge_color='black',                  # Define a cor das arestas (linhas que conectam os nós) como preta.
        width=1.5,                           # Define a espessura das arestas. Neste caso, cada aresta terá uma espessura de 1.5.
        edgecolors=cores_borda,              # Define as cores das bordas dos nós, baseado na lista cores_borda.
        linewidths=2                        # Define a espessura da linha da borda ao redor de cada nó como 2.
    )

    
    # Para cada nó, exibe o valor do nó na posição calculada.
    # A cor do texto é branca para nós pretos e preta para nós vermelhos.
    # for no, (x, y) in pos.items():
    #    plt.text(x, y, str(no.dado), ha='center', va='center', color='white' if G.nodes[no]['color'] == 'preto' else 'black')
    
    # Iterando sobre os itens do dicionário 'pos', que contém as posições (x, y) de cada nó.
    for no, (x, y) in pos.items():

        # plt.text é usado para adicionar um texto em um gráfico do Matplotlib.
        # Neste caso, estamos adicionando o valor 'dado' de cada nó na sua respectiva posição (x, y).

        plt.text(
            x, y,                            # Coordenadas (x, y) onde o texto será posicionado.
            str(no.dado),                    # O texto a ser exibido. Aqui, estamos convertendo o atributo 'dado' do nó para string.
            ha='center',                     # Alinhamento horizontal do texto. 'center' significa que o texto será centralizado em relação à coordenada x.
            va='center',                     # Alinhamento vertical do texto. 'center' significa que o texto será centralizado em relação à coordenada y.

            # Definindo a cor do texto. Se a cor do nó for 'preto', o texto será 'white'. Caso contrário, será 'white'.
            color='white' if G.nodes[no]['color'] == 'preto' else 'white'
        )

    
    # Exibe a visualização da árvore.
    plt.show()
            

# Cria uma instância da classe ArvoreVermelhoPreto.
arvore = ArvoreVermelhoPreto()

# Define uma lista de valores que serão inseridos na árvore.
valores = [30, 15, 45, 7, 22, 40, 60, 5, 24, 35]
# valores = [50, 25, 75, 12, 37, 62, 87, 6, 18, 30, 42, 55, 68, 80, 92]

# valores = [
#    150, 75, 225, 37, 112, 187, 262, 18, 56, 94, 131, 168, 206, 243, 281,
#    9, 28, 45, 67, 84, 103, 120, 140, 157, 284
#]

# Para cada valor na lista 'valores', insere o valor na árvore.
for valor in valores:
    arvore.inserir(valor)
    

# Chama a função 'desenhar_arvore' para visualizar a árvore Vermelho-Preto.
# A função usa a biblioteca NetworkX para criar um grafo e a biblioteca Matplotlib 
# para desenhar e exibir a visualização.
desenhar_arvore(arvore)
            
"""
Em uma árvore vermelho e preto (RBT, Red-Black Tree), a cor de um nodo (seja ele vermelho
ou preto) é determinada por uma série de propriedades que a árvore deve manter a cada inserção
ou remoção. Estas propriedades garantem que a árvore permaneça aproximadamente equilibrada, 
resultando em tempos de busca, inserção e remoção eficientes.

As propriedades básicas de uma árvore vermelho e preto são:

- Cada nodo é ou vermelho ou preto.
- A raiz é sempre preta.
- Se um nodo é vermelho, então ambos os seus filhos são pretos.
- Todo caminho da raiz para um nodo NIL ou nulo contém o mesmo número de nodos pretos.
- Novos inserções são sempre nodos vermelhos.

A raiz da árvore (o primeiro valor, 150) seria preto devido ser a raiz. Quanto aos 
outros valores, a cor (preto ou vermelho) dependeria da sequência de inserções e das 
rotações necessárias para manter as propriedades da árvore vermelho e preto.

Os três primeiros nodos são pretos, é provável que a ordem e o método de inserção levaram a 
essa configuração para manter as propriedades da RBT.
"""
print()