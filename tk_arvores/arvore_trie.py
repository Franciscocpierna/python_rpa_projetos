"""
Estruturas de Dados Não-Lineares
    
        Árvores
            
            Trie
            
 Uma Trie é uma árvore de prefixos, onde cada caminho da raiz
 a um nó representa um prefixo da coleção de palavras. Se duas 
 palavras possuem um prefixo comum, elas compartilharão o mesmo
 caminho na Trie até o fim desse prefixo.

Por exemplo, se inserirmos as palavras "carro" e "casa" 
na Trie, a estrutura da Trie será:

raiz
 |
 c
 |
 a
 |\
 | s
 |  \
 r   a
 |
 r
 |
 o


"""

# Importando a biblioteca tkinter, que é usada para criar interfaces gráficas.
import tkinter as tk

# Importando o módulo ttk do tkinter, que fornece acesso a um conjunto de widgets temáticos.
from tkinter import ttk

# Importando a biblioteca networkx, que é usada para criar, manipular 
# e estudar a estrutura e funções de grafos complexos.
import networkx as nx

# Importando a biblioteca matplotlib, que é uma biblioteca de plotagem 2D em Python.
import matplotlib.pyplot as plt

# Importando FigureCanvasTkAgg do backend do matplotlib para integrar gráficos 
# do matplotlib em aplicações Tkinter.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Definindo uma classe chamada NoTrie para representar um nó na Trie.
class NoTrie:
    
    # O construtor da classe, que é chamado quando um novo objeto NoTrie é criado.
    def __init__(self):
        
        # Inicializando um dicionário para os filhos do nó. Cada chave é um 
        # caractere e o valor é outro NoTrie.
        self.filhos = {}
        
        # Inicializando uma variável booleana para verificar se o nó atual 
        # marca o fim de uma palavra na Trie.
        self.eh_fim_palavra = False
        

# Definindo uma classe chamada Trie para representar a estrutura de dados Trie.
class Trie:
    
    # O construtor da classe, que é chamado quando um novo objeto Trie é criado.
    def __init__(self):
        
        # Inicializando a raiz da Trie com um novo nó NoTrie.
        # A raiz da Trie é um nó especial que não contém nenhum caractere/palavra.
        self.raiz = NoTrie()

    # Método para inserir uma palavra na Trie.
    def inserir(self, palavra):
        
        # Começando da raiz da Trie.
        no = self.raiz
        
        # Iterando sobre cada caractere da palavra.
        for char in palavra:
            
            # Verificando se o caractere atual não é um filho do nó atual.
            # Se não for, criamos um novo nó NoTrie e o adicionamos ao 
            # dicionário de filhos.
            if char not in no.filhos:
                no.filhos[char] = NoTrie()
            
            # Movendo para o próximo nó (ou seja, o filho que representa
            # o caractere atual).
            no = no.filhos[char]
        
        # Após iterar por todos os caracteres, marcamos o último nó 
        # como o fim da palavra.
        no.eh_fim_palavra = True
        
        
# A classe AppTrie é uma extensão de tk.Tk, que é a janela principal do Tkinter.
# Isso significa que nossa classe AppTrie não é apenas um aplicativo padrão, mas
# também uma janela principal do Tkinter,
# com todos os recursos e funcionalidades de uma janela Tkinter.
class AppTrie(tk.Tk):
    
    # O método __init__ é o construtor da classe. Ele é chamado 
    # automaticamente quando um objeto da classe é criado.
    def __init__(self):
        
        # A função super() retorna um objeto temporário da classe 
        # base, que neste caso é tk.Tk.
        # Estamos chamando o método __init__ da classe base para 
        # garantir que a janela principal do Tkinter seja inicializada corretamente.
        super().__init__()

        # Criamos uma instância da estrutura de dados Trie, que será 
        # usada para inserir e consultar palavras.
        self.trie = Trie()
        
        # O método title() é usado para definir o título da janela. Neste caso, 
        # a janela terá o título "Árvore Trie".
        self.title("Árvore Trie")

        # ttk.Entry é um widget que permite ao usuário inserir uma única linha de texto.
        # Estamos criando uma caixa de entrada e associando-a à janela principal (self).
        self.entrada = ttk.Entry(self, font=("Arial 20"))
        
        # O método pack() é usado para organizar widgets na janela. 
        # pady=20 adiciona um espaço vertical de 20 pixels acima e abaixo 
        # da caixa de entrada.
        self.entrada.pack(pady=20)
        
        # ttk.Button é um widget que cria um botão. 
        # O texto no botão é "Inserir" e, quando o botão for 
        # clicado, a função self.inserir_e_mostrar será executada.
        self.botao_inserir = ttk.Button(self, 
                                        text="Inserir", 
                                        command=self.inserir_e_mostrar)
        
        # Organizamos o botão na janela, assim como fizemos com a caixa de entrada.
        self.botao_inserir.pack(pady=20)
        
        
        # ttk.Frame cria um container retangular que pode conter outros widgets.
        # Estamos criando esse frame para posteriormente adicionar um gráfico visual da Trie.
        self.canvas_frame = ttk.Frame(self)
        
        # Adicionando o frame à janela principal. 
        # fill=tk.BOTH faz com que o frame se expanda tanto vertical 
        # quanto horizontalmente para preencher qualquer espaço disponível.
        # expand=True garante que, se a janela principal for redimensionada, 
        # o frame também será, ocupando todo o espaço disponível.
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        
    # Definindo o método 'inserir_e_mostrar' para a classe 'AppTrie'.
    # Este método é responsável por pegar a palavra inserida pelo usuário e, 
    # em seguida, inseri-la na Trie e visualizá-la.
    def inserir_e_mostrar(self):
        
        # Usando o método 'get' do widget 'Entry' para obter a palavra/string 
        # que o usuário digitou na caixa de entrada.
        palavra = self.entrada.get()
        
        # Verificando se a palavra obtida não está vazia. 
        # Se a caixa de entrada estiver vazia, 'palavra' será uma string vazia, 
        # que é avaliada como 'False' em uma condição.
        if palavra:
            
            # Chamando o método 'inserir' da instância 'trie' para adicionar
            # a palavra à Trie.
            self.trie.inserir(palavra)
            
            # Chamando o método 'mostrar_arvore' para atualizar a visualização 
            # gráfica da Trie.
            self.mostrar_arvore()
            
    # Definindo o método 'mostrar_arvore' para a classe 'AppTrie'.
    # Este método é responsável por criar uma visualização gráfica da Trie.
    def mostrar_arvore(self):
        
        # Criando um grafo direcionado usando a biblioteca 'networkx'.
        # A Trie é uma forma de árvore/grafos, e 'DiGraph' representa 
        # um grafo direcionado.
        G = nx.DiGraph()
        
        # Inicializando um dicionário vazio para armazenar os rótulos dos nós.
        # Cada nó terá um rótulo, que é o caractere da Trie que ele representa.
        labels = {}
        
        # Inicializando um dicionário vazio para armazenar as posições dos 
        # nós quando desenharmos o grafo.
        posicoes = {}
        
        # Inicializando um dicionário vazio para armazenar os nós por nível.
        # Isso nos ajudará a determinar a posição y de cada nó.
        niveis = {}

        # Definindo uma função interna chamada 'visitar_no' para percorrer a Trie.
        # Esta função será chamada recursivamente para cada nó da Trie.
        def visitar_no(no, parent_name, caminho_atual, nivel):
            
            # Iterando sobre cada filho do nó atual.
            for char, filho_no in no.filhos.items():
                
                # Criando um nome único para o nó com base no caminho da raiz até ele.
                nome_no = caminho_atual + char
                
                # Adicionando uma aresta ao grafo do nó pai para o nó filho.
                G.add_edge(parent_name, nome_no)
                
                # Definindo o rótulo do nó filho como o caractere que ele representa.
                labels[nome_no] = char
                
                # Verificando se o nível atual já tem uma entrada no dicionário de níveis.
                if nivel not in niveis:
                    niveis[nivel] = []
                
                # Adicionando o nome do nó à lista de nós no nível atual.
                niveis[nivel].append(nome_no)
                
                # Chamando a função 'visitar_no' recursivamente para o nó filho.
                # Isso percorrerá todos os descendentes do nó filho.
                visitar_no(filho_no, nome_no, nome_no, nivel + 1)
                
        
        # Chamando a função interna 'visitar_no' para iniciar a travessia da Trie.
        # Começamos com a raiz da Trie e definimos os valores 
        # iniciais para 'parent_name', 'caminho_atual' e 'nivel'.
        # 'parent_name' e 'caminho_atual' são strings vazias porque estamos no início.
        # 'nivel' é definido como 1 porque estamos começando da raiz.
        visitar_no(self.trie.raiz, "", "", 1)
        
        
        # Iterando sobre cada nível e seus respectivos nós, armazenados no dicionário 'niveis'.
        for nivel, nos in niveis.items():
            
            # Calculando o total de nós no nível atual.
            total_nos = len(nos)
            
            # Iterando sobre cada nó no nível atual.
            # A função 'enumerate' retorna o índice (idx) e o valor (no) do item enquanto itera.
            for idx, no in enumerate(nos):
                
                # Calculando a posição x do nó.
                # A ideia é distribuir os nós uniformemente ao longo do eixo x.
                # 'idx - total_nos / 2' assegura que os nós sejam centralizados em torno de x=0.
                x = idx - total_nos / 2
                
                # A posição y é simplesmente o negativo do nível, para que os nós 
                # sejam desenhados de cima para baixo.
                y = -nivel
                
                # Armazenando a posição (x, y) do nó no dicionário 'posicoes'.
                posicoes[no] = (x, y)
                
        
        # Verificando se o nó com nome vazio (""), que representa a 
        # raiz, está presente no grafo 'G'.
        # A raiz não possui um valor de caractere associado, então usamos uma 
        # string vazia para representá-la.
        if "" in G:
            
            # Se o nó raiz estiver presente no grafo, removemos esse nó.
            # Isso é feito porque, geralmente, não queremos mostrar a raiz 
            # na visualização, pois ela não tem um valor significativo em si.
            G.remove_node("")
                
        
        # Acessando todos os widgets (elementos gráficos) que são filhos do 'canvas_frame'.
        # 'canvas_frame' é onde colocamos nossa visualização gráfica, e queremos 
        # limpar qualquer visualização anterior antes de desenhar uma nova.
        for widget in self.canvas_frame.winfo_children():
            
            # Destruindo (removendo) cada widget filho do 'canvas_frame'.
            # Isso garante que, quando desenharmos uma nova visualização, a 
            # visualização anterior seja removida e não haja sobreposição.
            widget.destroy()
        
        # Criando uma nova figura usando a biblioteca matplotlib com um tamanho
        # específico de 10x6 polegadas.
        plt.figure(figsize=(10, 6))
        
        # Usando a função 'draw' da biblioteca networkx para desenhar o grafo 'G'.
        # - 'pos=posicoes': define as posições dos nós conforme calculado anteriormente.
        # - 'labels=labels': define os rótulos dos nós conforme determinado anteriormente.
        # - 'with_labels=True': instrui a função a realmente mostrar os rótulos dos nós.
        # - 'node_size=3000': define o tamanho dos nós.
        # - 'node_color='skyblue'': define a cor dos nós.
        # - 'font_size=15': define o tamanho da fonte dos rótulos.
        nx.draw(G, 
                pos=posicoes, 
                labels=labels, 
                with_labels=True, 
                node_size=3000, 
                node_color='skyblue', 
                font_size=15)
        
        # Criando um 'canvas' (área de desenho) para a figura atual do matplotlib na interface do Tkinter.
        # 'plt.gcf()' retorna a figura atual do matplotlib.
        # 'self.canvas_frame' é o widget Tkinter onde queremos exibir o gráfico.
        canvas = FigureCanvasTkAgg(plt.gcf(), self.canvas_frame)
        
        # Desenhando a figura no canvas.
        canvas.draw()
        
        # Integrando o canvas com a interface do Tkinter.
        # 'get_tk_widget()' retorna o widget Tkinter associado ao canvas.
        # 'pack' organiza o widget na janela. 'side=tk.TOP' coloca o widget no topo da janela.
        # 'fill=tk.BOTH' e 'expand=True' garantem que o widget ocupe todo o espaço disponível.
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        
# Criando uma instância da classe 'AppTrie', o que inicia a interface gráfica.
app = AppTrie()

# Executando o loop principal do Tkinter. 
# 'mainloop()' mantém a janela aberta e escuta eventos, como cliques de botão.
app.mainloop()
        