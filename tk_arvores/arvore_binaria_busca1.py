"""
Árvores
            
        Tipos de Árvores

            Árvore Binária de Busca (ABB)
            
Uma Árvore Binária de Busca (ABB) é uma árvore binária em que cada nó tem um valor 
e dois ponteiros de filho, esquerdo e direito, e assegura as seguintes propriedades:

    - O valor no nó à esquerda é sempre menor do que o valor do nó pai.
    - O valor no nó à direita é sempre maior do que o valor do nó pai.

Isso permite uma busca eficiente, já que podemos ignorar metade
da árvore durante a busca.

A seguir, um exemplo de uma Árvore Binária de 
Busca (ABB) que inclui inserção, exclusão, alteração e pesquisa:

"""

# Importando o módulo "tkinter" e dando a ele o alias "tk".
# "tkinter" é uma biblioteca padrão para criar interfaces gráficas no Python.
import tkinter as tk

# Importando algumas classes específicas de "tkinter":
# "ttk" oferece acesso a um conjunto de widgets temáticos que podem 
# ser usados para construir GUIs.
# "messagebox" é usado para exibir caixas de mensagem.
from tkinter import ttk, messagebox

# Importando o módulo "networkx" com alias "nx".
# "networkx" é uma biblioteca para a criação, manipulação e estudo de redes e grafos complexos.
import networkx as nx

# Importando o módulo "pyplot" de "matplotlib" e dando a ele o alias "plt".
# "matplotlib" é uma biblioteca para criação de gráficos e visualizações em Python.
# "pyplot" é um módulo em "matplotlib" que oferece uma interface para plotagem no estilo MATLAB.
import matplotlib.pyplot as plt

# Importando "FigureCanvasTkAgg" do backend "backend_tkagg" de "matplotlib".
# Este é usado para integrar gráficos do matplotlib em aplicações baseadas em tkinter.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Definindo uma classe chamada "No".
# Esta classe representa um nó de uma árvore binária.
class No:

    # Construtor da classe. É chamado quando um objeto desta classe é instanciado.
    def __init__(self, valor):
        
        # Inicializando o atributo "valor" do objeto com o valor passado como
        # argumento para o construtor.
        self.valor = valor
        
        # Inicializando o atributo "esquerdo" do objeto com None.
        # Isso representa a referência ao filho esquerdo do nó, que 
        # inicialmente é nulo (não existe).
        self.esquerdo = None
        
        # Inicializando o atributo "direito" do objeto com None.
        # Isso representa a referência ao filho direito do nó, que inicialmente é 
        # nulo (não existe).
        self.direito = None
        

# Definindo uma classe chamada "ABB" que representa uma Árvore Binária de Busca.
class ABB:

    # Construtor da classe. É chamado quando um objeto desta classe é instanciado.
    def __init__(self):
        
        # Inicializando o atributo "raiz" do objeto com None.
        # A raiz é o nó superior de uma árvore e, inicialmente, a árvore está 
        # vazia (não tem raiz).
        self.raiz = None

    # Método para inserir um valor na árvore.
    def inserir(self, valor):
        
        # Verificando se a árvore está vazia (não possui uma raiz).
        if self.raiz is None:
            
            # Se a árvore está vazia, o novo valor se tornará a raiz da árvore.
            self.raiz = No(valor)
            
        else:
            
            # Se a árvore já tem uma raiz, usamos um método recursivo privado para 
            # inserir o valor
            # na posição correta (esquerda ou direita) na árvore.
            self._inserir_recursivo(self.raiz, valor)


    # Definindo um método privado para inserção recursiva.
    # A convenção de nome "_nome_do_método" indica que o método é de uso 
    # interno da classe (private).
    
    def _inserir_recursivo(self, no_atual, valor):

        # Verifica se o valor a ser inserido é menor do que o valor do nó atual.
        if valor < no_atual.valor:

            # Se o valor é menor, então ele deve ser inserido à esquerda.

            # Verifica se o nó esquerdo do nó atual está vazio (None).
            if no_atual.esquerdo is None:

                # Se estiver vazio, cria um novo nó com o valor e o coloca como 
                # filho esquerdo do nó atual.
                no_atual.esquerdo = No(valor)
                
            else:
                
                # Se o nó esquerdo já tem um valor, então a função é chamada recursivamente 
                # para tentar inserir o valor no subnó esquerdo do nó atual.
                self._inserir_recursivo(no_atual.esquerdo, valor)
                
        else:
            
            # Se o valor não for menor (ou seja, for maior ou igual), ele deve 
            # ser inserido à direita.

            # Verifica se o nó direito do nó atual está vazio (None).
            if no_atual.direito is None:

                # Se estiver vazio, cria um novo nó com o valor e o coloca como 
                # filho direito do nó atual.
                no_atual.direito = No(valor)
                
            else:
                
                # Se o nó direito já tem um valor, então a função é chamada recursivamente 
                # para tentar inserir o valor no subnó direito do nó atual.
                self._inserir_recursivo(no_atual.direito, valor)
                
    
    # Definindo um método para calcular o tamanho da subárvore.
    def tamanho_da_subarvore(self, no):

        # Verifica se o nó atual é None (ou seja, se está vazio).
        if no is None:

            # Se o nó estiver vazio, retorna 0 (pois não há elementos nesta subárvore).
            return 0

        # Retorna a soma de:
        # 1 (para o nó atual) 
        # + o tamanho da subárvore à esquerda (chamando a função recursivamente para o nó esquerdo)
        # + o tamanho da subárvore à direita (chamando a função recursivamente para o nó direito).
        return 1 + self.tamanho_da_subarvore(no.esquerdo) + self.tamanho_da_subarvore(no.direito)
      
    
    # Define um método para calcular as posições dos nós na visualização da árvore.
    def calcular_posicoes(self, no, profundidade=0, posicao=0, posicoes=None, deslocamento=1.5):

        # Se 'posicoes' não foi inicializado (ou seja, é None), 
        # inicia como um dicionário vazio. 
        # 'posicoes' armazenará as coordenadas x, y de cada nó.
        if posicoes is None:
            posicoes = {}

        # Se o nó atual não está vazio.
        if no:

            # Atribui a posição (x, y) do nó atual.
            # A posição y é negativa para mover os nós descendentes para baixo na visualização.
            posicoes[no.valor] = (posicao, -profundidade)

            # Calcula o tamanho da subárvore esquerda do nó atual. 
            # Isso ajudará a determinar quanto espaço é necessário para a subárvore à esquerda.
            deslocamento_esquerdo = self.tamanho_da_subarvore(no.esquerdo)

            # Calcula o tamanho da subárvore direita do nó atual.
            deslocamento_direito = self.tamanho_da_subarvore(no.direito)

            # Se o nó atual possui um filho à esquerda.
            if no.esquerdo:

                # Calcula as posições para a subárvore esquerda usando uma chamada recursiva.
                # Aumenta a profundidade (para mover para o próximo nível da árvore) e ajusta a posição x.
                posicoes = self.calcular_posicoes(no.esquerdo, profundidade+1, posicao-deslocamento*(deslocamento_direito+1), posicoes)

            # Se o nó atual possui um filho à direita.
            if no.direito:

                # Calcula as posições para a subárvore direita usando uma chamada recursiva.
                # Ajusta a posição x para garantir que a subárvore direita esteja posicionada corretamente.
                posicoes = self.calcular_posicoes(no.direito, profundidade+1, posicao+deslocamento*(deslocamento_esquerdo+1), posicoes)

        # Retorna o dicionário contendo as posições dos nós.
        return posicoes


            
    # Define um método para criar um grafo direcionado representando a árvore.
    def criar_grafo(self, no_atual=None, G=None):

        # Se o grafo 'G' não foi inicializado (ou seja, é None), 
        # cria uma nova instância do grafo direcionado usando a biblioteca NetworkX.
        if G is None:
            G = nx.DiGraph()

        # Se o nó atual não está vazio.
        if no_atual:

            # Se o nó atual possui um filho à esquerda.
            if no_atual.esquerdo:

                # Adiciona uma aresta ao grafo entre o nó atual e seu filho esquerdo.
                G.add_edge(no_atual.valor, no_atual.esquerdo.valor)

                # Chamada recursiva para adicionar nós e arestas da subárvore esquerda ao grafo.
                self.criar_grafo(no_atual.esquerdo, G)

            # Se o nó atual possui um filho à direita.
            if no_atual.direito:

                # Adiciona uma aresta ao grafo entre o nó atual e seu filho direito.
                G.add_edge(no_atual.valor, no_atual.direito.valor)

                # Chamada recursiva para adicionar nós e arestas da subárvore direita ao grafo.
                self.criar_grafo(no_atual.direito, G)

        # Retorna o grafo preenchido.
        return G
    

    # Define um método para excluir um nó com um determinado valor da árvore.
    def excluir(self, valor):

        # Verifica se a raiz da árvore não está vazia.
        if self.raiz:

            # Chama o método _excluir_recursivo, passando a raiz da árvore e o valor a ser excluído.
            # O resultado dessa chamada (que pode ser uma árvore atualizada ou a mesma 
            # árvore se o valor não for encontrado)
            # é atribuído de volta à raiz da árvore.
            self.raiz = self._excluir_recursivo(self.raiz, valor)
    
       
    # Define um método privado para exclusão recursiva de um nó da árvore.
    def _excluir_recursivo(self, no_atual, valor):

        # Caso base: se o nó atual é None (não existe), ele é retornado como está.
        if not no_atual:
            return no_atual

        # Se o valor a ser excluído é menor que o valor do nó atual,
        # o nó a ser excluído estará na subárvore esquerda.
        if valor < no_atual.valor:
            no_atual.esquerdo = self._excluir_recursivo(no_atual.esquerdo, valor)

        # Se o valor a ser excluído é maior que o valor do nó atual,
        # o nó a ser excluído estará na subárvore direita.
        elif valor > no_atual.valor:
            no_atual.direito = self._excluir_recursivo(no_atual.direito, valor)

        # Se o valor do nó atual é o valor a ser excluído, este é o nó a ser removido.
        else:

            # Se o nó atual não tem filho esquerdo, retorna o filho direito.
            # Isso cobre o caso onde o nó tem apenas um filho (o direito) ou nenhum filho.
            if not no_atual.esquerdo:
                return no_atual.direito

            # Se o nó atual não tem filho direito, retorna o filho esquerdo.
            # Isso cobre o caso onde o nó tem apenas um filho (o esquerdo).
            elif not no_atual.direito:
                return no_atual.esquerdo

            # Se o nó tem ambos os filhos, a estratégia é encontrar o menor valor da subárvore direita
            # (ou seja, o sucessor in-order) e substituir o valor do nó atual por ele.
            # Em seguida, exclua o sucessor in-order da subárvore direita.
            no_atual.valor = self._valor_minimo(no_atual.direito)
            no_atual.direito = self._excluir_recursivo(no_atual.direito, no_atual.valor)

        # Retorna o nó atual após realizar as operações de exclusão apropriadas.
        return no_atual
    
    
    # Define um método privado para encontrar o menor valor em uma subárvore.
    def _valor_minimo(self, no):
        
        # Inicializa o valor atual com o valor do nó fornecido.
        valor_atual = no.valor

        # Enquanto houver um filho à esquerda (nós à esquerda contêm valores menores),
        # atualiza o valor atual e avança para a esquerda.
        while no.esquerdo:
            valor_atual = no.esquerdo.valor
            no = no.esquerdo

        # Retorna o menor valor encontrado.
        return valor_atual
    
    
    # Define o método para atualizar um valor na árvore.
    def atualizar(self, valor_antigo, valor_novo):
        
        # Primeiro, exclui o valor antigo da árvore.
        self.excluir(valor_antigo)
        
        # Em seguida, insere o novo valor na árvore.
        self.inserir(valor_novo)
        
    
    # Define o método para buscar um valor na árvore.
    def buscar(self, valor):
        
        # Inicia a busca recursiva a partir da raiz da árvore.
        return self._buscar_recursivo(self.raiz, valor)
    
    
    # Define um método privado para buscar um valor na árvore de forma recursiva.
    def _buscar_recursivo(self, no_atual, valor):
        
        # Se o nó atual for None (ou seja, se alcançarmos uma folha da árvore sem encontrar o valor),
        # o valor não está presente na árvore e, portanto, retorna False.
        if no_atual is None:
            return False

        # Se o valor do nó atual for igual ao valor que estamos buscando,
        # encontramos o valor na árvore e, portanto, retorna True.
        if no_atual.valor == valor:
            return True

        # Se o valor que estamos buscando for menor que o valor do nó atual,
        # continue a busca recursivamente no subárvore à esquerda.
        if valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerdo, valor)

        # Se o valor que estamos buscando for maior que o valor do nó atual,
        # continue a busca recursivamente no subárvore à direita.
        return self._buscar_recursivo(no_atual.direito, valor)
    
                
# Define uma classe para criar uma interface gráfica para uma 
# Árvore Binária de Busca (ABB).
class InterfaceABB:
    
    # Método inicializador da classe.
    def __init__(self, janela_principal):
        
        # Atribui a janela principal passada como argumento para o atributo da classe 'janela'.
        self.janela = janela_principal
        
        # Define o título da janela principal.
        self.janela.title("Interface Gráfica para ABB")

        # Cria uma nova instância da Árvore Binária de Busca (ABB) que será usada na interface.
        self.arvore = ABB()

        # Cria um frame (quadro/contêiner) para conter os widgets relacionados à 
        # inserção, exclusão e atualização de nós.
        frame_entrada = ttk.Frame(janela_principal)
        
        # Posiciona o frame na janela principal com um espaçamento (padding) de 20 pixels verticalmente e horizontalmente.
        # O frame expandirá na direção horizontal para preencher o espaço disponível (fill=tk.X).
        frame_entrada.pack(pady=20, padx=20, fill=tk.X)
        
        # Seção para criar e posicionar componentes relacionados à inserção na interface.

        # Cria uma label (etiqueta) com o texto "Valor:" no frame de entrada.
        ttk.Label(frame_entrada, text="Valor:", font="Arial 16").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        
        # Cria um campo de entrada (Entry) onde os usuários podem inserir valores e o atribui ao atributo 'campo_valor'.
        self.campo_valor = ttk.Entry(frame_entrada, font="Arial 16")
        
        # Posiciona o campo de entrada na primeira linha e segunda coluna do layout grid do frame de entrada.
        self.campo_valor.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)
        
        # Cria um botão com o texto "Inserir", que quando pressionado, chama o método 'adicionar_valor'.
        self.botao_inserir = ttk.Button(frame_entrada,
                                        text="Inserir", 
                                        command=self.adicionar_valor)
        
        # Posiciona o botão na primeira linha e terceira coluna do layout grid do frame de entrada.
        self.botao_inserir.grid(row=0, column=2, padx=10, pady=5)
        
        
        
        # Seção para criar e posicionar componentes relacionados à exclusão na interface.

        # Cria um botão com o texto "Excluir", que quando pressionado, chama o método 'excluir_valor'.
        self.botao_excluir = ttk.Button(frame_entrada, 
                                        text="Excluir", 
                                        command=self.excluir_valor)
        
        # Posiciona o botão na primeira linha e quarta coluna do layout grid do frame de entrada.
        self.botao_excluir.grid(row=0, column=3, padx=10, pady=5)
        
        
        # Seção para criar e posicionar componentes relacionados à atualização na interface.

        # Cria uma label (etiqueta) com o texto "Atualizar:" no frame de entrada.
        ttk.Label(frame_entrada, 
                  text="Atualizar:", font="Arial 16").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        
        # Cria um campo de entrada (Entry) onde os usuários podem inserir o valor antigo que desejam atualizar.
        # Atribui este campo ao atributo 'campo_valor_antigo'.
        self.campo_valor_antigo = ttk.Entry(frame_entrada, font="Arial 16")
        
        # Posiciona o campo de entrada na segunda linha e segunda coluna do layout grid do frame de entrada.
        self.campo_valor_antigo.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)
        
        
        # Cria uma label com o texto "para" no frame de entrada, indicando 
        # que o valor antigo será atualizado para um novo valor.
        ttk.Label(frame_entrada, text="para:", font="Arial 16").grid(row=1, column=2, padx=10, pady=5)
       
        
        # Cria um campo de entrada (Entry) onde os usuários podem inserir o novo valor.
        # Atribui este campo ao atributo 'campo_valor_novo'.
        self.campo_valor_novo = ttk.Entry(frame_entrada, font="Arial 16")
        
        # Posiciona o campo de entrada na segunda linha e quarta coluna do layout grid do frame de entrada.
        self.campo_valor_novo.grid(row=1, column=3, padx=10, pady=5, sticky=tk.EW)
        
        
        # Cria um botão com o texto "Atualizar", que quando pressionado, chama o método 'atualizar_valor'.
        self.botao_atualizar = ttk.Button(frame_entrada, 
                                          text="Atualizar", 
                                          command=self.atualizar_valor)
        
        # Posiciona o botão na segunda linha e quinta coluna do layout grid do frame de entrada.
        self.botao_atualizar.grid(row=1, column=4, padx=10, pady=5)
        
        
        
        # Seção para ajustar o layout da interface.

        # Ajusta a configuração das colunas no frame 'frame_entrada' para permitir 
        # que os widgets contidos nas colunas especificadas
        # (coluna 1 e coluna 3) se expandam horizontalmente quando a janela for redimensionada.
        # O 'weight' controla como o espaço extra é alocado entre
        # colunas (ou linhas) em um layout de grid.
        frame_entrada.columnconfigure(1, weight=1)
        frame_entrada.columnconfigure(3, weight=1)
  
        
        # Seção para configurar a área de desenho do Matplotlib.

        # Cria uma figura e eixo do Matplotlib com um tamanho especificado.
        # Esta será a área onde a Árvore Binária de Busca será desenhada.
        self.figura, self.eixo = plt.subplots(figsize=(10, 8))
        
        # Cria um canvas (área de desenho) do Matplotlib para ser incorporado na janela principal do tkinter.
        # 'FigureCanvasTkAgg' é a classe que permite a integração do Matplotlib com o tkinter.
        self.canvas = FigureCanvasTkAgg(self.figura, janela_principal)
        
        # Incorpora o canvas criado na janela principal do tkinter, garantindo que ele seja apresentado ao usuário.
        # Ajusta o padding vertical para 10 pixels.
        self.canvas.get_tk_widget().pack(pady=10)
        
        
        # Seção para criar componentes de busca na interface.

        # Cria um rótulo "Buscar:" e o posiciona na linha 2, coluna 0 do frame 'frame_entrada'. 
        # 'sticky=tk.W' garante que o rótulo esteja alinhado à esquerda (oeste). 
        # 'padx' e 'pady' são usados para definir o espaçamento ao redor do rótulo.
        ttk.Label(frame_entrada, text="Buscar:", font="Arial 16").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        
        # Cria um campo de entrada onde o usuário pode digitar um valor para buscar na árvore e o posiciona na linha 2, coluna 1.
        # 'sticky=tk.EW' faz com que o campo de entrada se expanda horizontalmente conforme o frame é redimensionado.
        self.campo_busca = ttk.Entry(frame_entrada)
        self.campo_busca.grid(row=2, column=1, padx=10, pady=5, sticky=tk.EW)
        
        
        # Cria um botão "Buscar", que quando clicado, invoca a função 'self.buscar_valor'.
        # Este botão é posicionado na linha 2, coluna 2.
        self.botao_buscar = ttk.Button(frame_entrada, 
                                       text="Buscar", 
                                       command=self.buscar_valor)
        self.botao_buscar.grid(row=2, column=2, padx=10, pady=5)
        
        
        
    # Início da definição da função que manipula a adição de um valor à árvore.
    def adicionar_valor(self):
        

        # Tentativa de executar o bloco de código a seguir.
        try:
            
            # Obtém o valor digitado pelo usuário no campo 'campo_valor', tenta convertê-lo em um inteiro 
            # e atribui à variável 'valor'.
            valor = int(self.campo_valor.get())

            # Usa o método 'inserir' da árvore (instância da classe ABB) para inserir o valor obtido.
            self.arvore.inserir(valor)

            # Atualiza a representação visual da árvore.
            self.atualizar_desenho()

            # Limpa o campo de entrada 'campo_valor', removendo todo o conteúdo que o usuário digitou.
            self.campo_valor.delete(0, tk.END)
            

        # Caso ocorra um erro ao tentar converter o valor digitado em um número inteiro (ValueError).
        except ValueError:
            
            # Exibe uma janela de erro com o título "Erro" e a mensagem "Por favor, insira um número válido."
            messagebox.showerror("Erro", "Por favor, insira um número válido.")
            
            
    # Início da definição da função que manipula a exclusão de um valor da árvore.
    def excluir_valor(self):

        # Tenta executar o bloco de código a seguir.
        try:
            
            # Obtém o valor digitado pelo usuário no campo 'campo_valor', tenta convertê-lo em um inteiro 
            # e atribui à variável 'valor'.
            valor = int(self.campo_valor.get())

            # Usa o método 'excluir' da árvore (instância da classe ABB) para remover o valor obtido.
            self.arvore.excluir(valor)

            # Atualiza a representação visual da árvore após a exclusão.
            self.atualizar_desenho()

            # Limpa o campo de entrada 'campo_valor', removendo todo o conteúdo que o usuário digitou.
            self.campo_valor.delete(0, tk.END)

        # Caso ocorra um erro ao tentar converter o valor digitado em um número inteiro (ValueError).
        except ValueError:
            
            # Exibe uma janela de erro com o título "Erro" e a mensagem "Por favor, insira um número válido."
            messagebox.showerror("Erro", "Por favor, insira um número válido.")
            
    
    # Início da definição da função que manipula a atualização de um valor na árvore.
    def atualizar_valor(self):        

        # Tenta executar o bloco de código a seguir.
        try:
            
            # Obtém o valor digitado pelo usuário no campo 'campo_valor_antigo', tenta convertê-lo em um inteiro 
            # e atribui à variável 'valor_antigo'.
            valor_antigo = int(self.campo_valor_antigo.get())

            # Da mesma forma, obtém o valor digitado pelo usuário no campo 'campo_valor_novo', tenta convertê-lo 
            # em um inteiro e atribui à variável 'valor_novo'.
            valor_novo = int(self.campo_valor_novo.get())

            # Usa o método 'atualizar' da árvore (instância da classe ABB) para atualizar o 'valor_antigo' para 
            # 'valor_novo' na estrutura da árvore.
            self.arvore.atualizar(valor_antigo, valor_novo)

            # Atualiza a representação visual da árvore após a operação de atualização.
            self.atualizar_desenho()

            # Limpa o campo de entrada 'campo_valor_antigo', removendo todo o conteúdo que o usuário digitou.
            self.campo_valor_antigo.delete(0, tk.END)

            # Limpa o campo de entrada 'campo_valor_novo', removendo todo o conteúdo que o usuário digitou.
            self.campo_valor_novo.delete(0, tk.END)

        # Caso ocorra um erro ao tentar converter os valores digitados em números inteiros (ValueError).
        except ValueError:
            
            # Exibe uma janela de erro com o título "Erro" e a mensagem "Por favor, insira números válidos."
            messagebox.showerror("Erro", "Por favor, insira números válidos.")
            
            
    # Início da definição da função responsável por atualizar o desenho da
    # Árvore Binária de Busca (ABB) na interface.
    def atualizar_desenho(self):

        # Limpa o conteúdo atual do eixo. Essa ação é necessária para 
        # garantir que desenhos anteriores da árvore sejam removidos 
        # e possamos começar a desenhar a árvore atualizada a partir de uma tela em branco.
        self.eixo.clear()

        # Chama a função 'criar_grafo' da instância da classe ABB (representando 
        # a árvore) com a raiz da árvore como argumento. 
        # Esta função transforma a árvore em um grafo que pode ser desenhado.
        grafo = self.arvore.criar_grafo(self.arvore.raiz)

        # Chama a função 'calcular_posicoes' da instância da classe ABB 
        # para determinar as posições onde os nós da árvore 
        # devem ser desenhados. Esta função retorna um dicionário
        # mapeando cada nó para sua posição.
        posicoes = self.arvore.calcular_posicoes(self.arvore.raiz)

        # Utiliza a função 'draw' do pacote NetworkX para desenhar o grafo (representando
        # a ABB) nas posições calculadas.
        # Algumas características de como o grafo será desenhado são
        # definidas pelos argumentos, tais como:
        # - 'with_labels=True': Mostra os rótulos (valores) nos nós.
        # - 'arrows=False': Não mostra setas (pois é uma ABB e não um grafo direcionado padrão).
        # - 'node_size=2000': Define o tamanho dos nós.
        # - 'node_color='skyblue'': Define a cor dos nós como azul celeste.
        # - 'ax=self.eixo': Determina que o desenho será feito no eixo atual.
        nx.draw(grafo, posicoes, with_labels=True, arrows=False, node_size=2000, node_color='skyblue', ax=self.eixo)

        # Atualiza o canvas (área de desenho) para refletir as mudanças feitas no eixo.
        self.canvas.draw()
        
        
    # Início da definição da função que é responsável por buscar um valor na 
    # Árvore Binária de Busca (ABB) através da interface.
    def buscar_valor(self):
    

        try:
            
            # Tenta converter o valor inserido no campo de busca para um inteiro. 
            # Isso é necessário porque a entrada da interface gráfica retorna texto, e queremos buscar um número.
            valor = int(self.campo_busca.get())

            # Chama a função 'buscar' da instância da classe ABB (representando a árvore) com o valor a ser buscado como argumento.
            # A função retorna True se o valor está presente na árvore e False caso contrário.
            existe = self.arvore.buscar(valor)

            # Dependendo se o valor existe ou não na árvore, exibe uma mensagem adequada para o usuário.
            if existe:
                
                # Se o valor estiver presente na árvore, mostra uma mensagem informando que ele foi encontrado.
                messagebox.showinfo("Resultado", f"O valor {valor} está presente na árvore.")
            else:
                
                # Se o valor não estiver presente na árvore, mostra uma mensagem informando que ele não foi encontrado.
                messagebox.showwarning("Resultado", f"O valor {valor} não foi encontrado na árvore.")

            # Limpa o campo de busca após a busca ser realizada, para que o usuário possa inserir um novo valor facilmente.
            self.campo_busca.delete(0, tk.END)
            

        except ValueError:
            
            # Se ocorrer um erro ao tentar converter o valor inserido para um inteiro (por exemplo, se o usuário inserir texto),
            # mostra uma mensagem de erro informando ao usuário para inserir um número válido.
            messagebox.showerror("Erro", "Por favor, insira um número válido.")
            
            

# Verifica se este script está sendo executado diretamente (não importado como um módulo).
if __name__ == "__main__":

    # Cria uma instância da janela principal da biblioteca tkinter.
    janela = tk.Tk()

    # Cria uma instância da classe InterfaceABB, passando a janela recém-criada como argumento.
    # Isso inicializa a interface da Árvore Binária de Busca (ABB) dentro da janela.
    app = InterfaceABB(janela)

    # Inicia o loop principal da janela tkinter.
    # Isso fará com que a janela continue rodando e respondendo a eventos até que o usuário a feche.
    janela.mainloop()