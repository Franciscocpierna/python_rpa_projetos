#pandas utilizada para manipulação de dados em formato de tabela
import pandas as pd

#Utlizada para operações númericas complexas
import numpy as np

#Utilizada para criação de gráficos estatisticos
import seaborn as sns

#Utilizada para criação de gráficos em geral
import matplotlib.pyplot as plt

#Classe utilizada para permitir a exibição de graficos em um Interface Gráfica
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Ulizada para criação de interface gráfica em Python
from tkinter import *

#Módulo do Tkinter que contem widgets adicionais e visuais melhorados
from tkinter import ttk

#Utilizada para criar caixa de seleção
from tkinter.ttk import Combobox

#Utilizada para exibição de mensagens e caixa de dialogo
from tkinter import filedialog, messagebox, simpledialog

#Utilizadas para manipulação de imagens
from PIL import ImageTk, Image

#Uitlizada para fazer capturas da tela
from PIL import ImageGrab

#Utilizada para criar pastas e arquivos
import os

#Cria uma classe "Application" que herda da classe "Frame"
class Application(Frame):
    
    # Cria o método "__init__" que recebe o argumento "master" e o inicializa como atributo da classe
    #master / pai / mestre
    def __init__(self, master=None):
        
        # Chama o construtor da superclasse
        super().__init__(master)
        
        # Define o atributo "master" como o argumento passado
        self.master = master
        
        # Define o título da janela principal
        self.master.title("Análise de Dados")
        
        # Chama o método "create_widgets"
        self.create_widgets()
        
        # Define a largura da coluna que contém o widget do gráfico como "1"
        self.master.columnconfigure(1, weight=1)
    
    def create_widgets(self):
        
        self.menu_bar = Menu(self.master) #Cria o menu_bar
        self.master.config(menu=self.menu_bar) #Define o menu
        self.arquivo_menu = Menu(self.menu_bar) #Cria o menu Arquivo
        self.menu_bar.add_cascade(label="Arquivo", menu=self.arquivo_menu) #Adicionando o menu "Arquivo" ao menu bar
        self.arquivo_menu.add_command(label="Abrir", command=self.abrir_arquivo) #Adiciona o comando Sair ao menu
        self.arquivo_menu.add_command(label="Sair", command=self.master.destroy) #Adiciona o comando Sair ao menu
        
        #row - linha
        #column - coluna
        #padx - espaço nas laterais
        #pady - espaço em cima e em baixo
        #stick="NSEW" - Estica para preencher os espaços
        #stick="NSEW" - Norte, Sul, Leste e Oeste
        self.frame_relatorios = Frame(self.master) #Cria o Frame de relatórios
        self.frame_relatorios.grid(row=0, column=0, columnspan=2, padx=10, pady=10, stick="NSEW")
        
        self.btn_dash1 = Button(self.frame_relatorios, text="Dashboard 1", font="Arial 16")
        self.btn_dash1.grid(row=0, column=0, padx=10, pady=10, stick="NSEW")
        
        self.btn_dash2 = Button(self.frame_relatorios, text="Dashboard 2", font="Arial 16")
        self.btn_dash2.grid(row=0, column=1, padx=10, pady=10, stick="NSEW")

        self.btn_editar_dados = Button(self.frame_relatorios, text="Editar Dados", font="Arial 16", command=self.abrir_janela_editar_dados)
        self.btn_editar_dados.grid(row=0, column=2, padx=10, pady=10, stick="NSEW")
        
        #----------------------------------------------------
        
        #row - linha
        #column - coluna
        #padx - espaço nas laterais
        #pady - espaço em cima e em baixo
        #stick="NSEW" - Estica para preencher os espaços
        #stick="NSEW" - Norte, Sul, Leste e Oeste
        self.frame_botoes = Frame(self.master) #Cria o Frame de botoes
        self.frame_botoes.grid(row=1, column=0, padx=10, pady=10, stick=N+S)
        
        #Cria o botão para abrir o gráfico de colunas
        self.btn_colunas = Button(self.frame_botoes, text="Gráfico de Colunas", font="Arial 16", command=self.abrir_janela_colunas)
        self.btn_colunas.grid(row=1, column=0, padx=10, pady=10, stick="NSEW")

        #Cria o botão para abrir o gráfico de pizza
        self.btn_pizza = Button(self.frame_botoes, text="Gráfico de Pizza", font="Arial 16", command=self.abrir_janela_pizza)
        self.btn_pizza.grid(row=2, column=0, padx=10, pady=10, stick="NSEW")

        #Cria o botão para abrir o gráfico de linhas
        self.btn_linha = Button(self.frame_botoes, text="Gráfico de Linha", font="Arial 16", command=self.abrir_janela_linhas)
        self.btn_linha.grid(row=3, column=0, padx=10, pady=10, stick="NSEW")

        #Cria o botão para abrir o gráfico de área
        self.btn_area = Button(self.frame_botoes, text="Gráfico de Área", font="Arial 16", command=self.abrir_janela_area)
        self.btn_area.grid(row=4, column=0, padx=10, pady=10, stick="NSEW")

        #Cria o botão para abrir o gráfico de colunas
        self.btn_funil = Button(self.frame_botoes, text="Gráfico de Funil", font="Arial 16", command=self.abrir_janela_funil)
        self.btn_funil.grid(row=5, column=0, padx=10, pady=10, stick="NSEW")

        #matplotlib - plt
        #Cria uma figura com tamanho 6 x 8 polegadas e resolução de 100 dpi
        self.fig = plt.Figure(figsize=(4,6), dpi=100)
        
        # Adiciona um subplot (gráfico) na figura criada, com posição (1, 1, 1) 
        # - um subplot único em uma matriz de um por um.
        self.ax = self.fig.add_subplot(111)
        
        # Cria um canvas (uma área retangular para desenhar) e adiciona a figura criada a ele
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        
        # Define a posição do canvas na janela principal, na segunda linha (row=1) e segunda coluna (column=1)
        # Adiciona margem de 10 pixels na horizontal e vertical e expande em todas as direções (sticky=N+S+E+W)
        self.canvas.get_tk_widget().grid(row=1, column=1, padx=10, pady=10, stick=N+S+E+W)
        
    def abrir_arquivo(self):
        
        #Abrir o arquivo de excel
        caminho_arquivo = filedialog.askopenfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        
        #Verifica se o arquivo foi selecionado
        if caminho_arquivo:
            
            try:
                
                
                #Le o arquivo de Excel e cria um DataFrame
                self.df = pd.read_excel(caminho_arquivo)
                
                #Exibir mensagem de sucesso caso o arquivo tenha sido aberto corretamente
                messagebox.showinfo("Sucesso:", "Arquivo aberto com sucesso!")
        
                
            except Exception as e:
                
                #Exibir mensagem de erro caso ocorra uma exceção ao abrir o arquivo
                messagebox.showerror("Erro:", f"Não foi possível abrir o arquivo: {e}")
                
    
    def abrir_janela_colunas(self):
        
        # Abrir janela para seleção de colunas
        # Criando uma nova janela com título, dimensões e colocando em foco
        self.janela_colunas = Toplevel(self.master)
        self.janela_colunas.title("Gráfico Colunas")
        self.janela_colunas.geometry("500x500")
        self.janela_colunas.grab_set() #Bloqueia todas as outras janelas
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo X" e adicionando a janela
        self.lb_eixo_x = Label(self.janela_colunas,
                                  font="Arial 22", 
                                  text="Eixo X:")
        self.lb_eixo_x.pack(pady=5)
        
        # Criando comboboxes para seleção de colunas
        # Criando um Combobox com as colunas do DataFrame como valores para a escolha do usuário e adicionando a janela
        #columns.tolist() é um método do pandas que retorna uma lista contendo os nomes das colunas de um DataFrame.
        self.cb_eixo_x = Combobox(self.janela_colunas,
                                  font="Arial 22", 
                                  values=self.df.columns.tolist())
        self.cb_eixo_x.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo Y" e adicionando a janela
        self.lb_eixo_y = Label(self.janela_colunas,
                                  font="Arial 22", 
                                  text="Eixo Y:")
        self.lb_eixo_y.pack(pady=5)
        
        # Criando comboboxes para seleção de colunas
        # Criando um Combobox com as colunas do DataFrame como valores para a escolha do usuário e adicionando a janela
        #columns.tolist() é um método do pandas que retorna uma lista contendo os nomes das colunas de um DataFrame.
        self.cb_eixo_y = Combobox(self.janela_colunas,
                                  font="Arial 22", 
                                  values=self.df.columns.tolist())
        self.cb_eixo_y.pack(pady=5)
        
        #--------------------------------------------------------------------
        # Criando uma Label com o texto "Eixo Y" e adicionando a janela
        self.lb_titulo = Label(self.janela_colunas,
                                  font="Arial 22", 
                                  text="Título:")
        self.lb_titulo.pack(pady=5)
        
        # Criando um campo de entrada de dados para inserir um titulo
        self.entry_titulo = Entry(self.janela_colunas,
                                  font="Arial 22")
        self.entry_titulo.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo X" e adicionando a janela
        self.lb_imagem = Label(self.janela_colunas, text="Imagem:",
                                  font="Arial 22",)
        self.lb_imagem.pack(pady=5)
        
        # Criando comboboxes para seleção do número da imagem
        self.cb_imagem = Combobox(self.janela_colunas,
                                  font="Arial 22",
                                  values=["image1", "image2", "image3", "image4", "image5", "image6", "image7", "image8"])
        self.cb_imagem.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        #Cria o botão para gerar o gráfico 1
        self.btn_gerar_grafico_colunas_1 = Button(self.janela_colunas,
                                               text= "Gráfico 1",
                                               font="Arial 26",
                                               command = self.gerar_grafico_colunas)
        self.btn_gerar_grafico_colunas_1.pack(side=LEFT, padx=5, pady=5)
        
        #--------------------------------------------------------------------
        
        #Cria o botão para gerar o gráfico 2
        self.btn_gerar_grafico_colunas_2 = Button(self.janela_colunas,
                                               text= "Gráfico 2",
                                               font="Arial 26",
                                               command = self.gerar_grafico_colunas_2)
        self.btn_gerar_grafico_colunas_2.pack(side=LEFT, padx=5, pady=5)
        
        
    def gerar_grafico_colunas(self):
        
        #Limpa o grafico anterior
        self.ax.clear()
        
        #Obtem as colunas selecionadas na combobox
        col_x = self.cb_eixo_x.get()
        col_y = self.cb_eixo_y.get()
        
        #Agrupa valores de col_y (coluna com os números)
        #col_x - Coluna com os itens (textos) eu agrupo para deixar valores únicos
        df_agrupado = self.df.groupby(col_x).sum()[col_y]
        
        #Pega o titulo do gráfico digitado pelo usuário
        titulo_grafico = self.entry_titulo.get()
        
        # Plotar gráfico de barras com os valores somados
        # Plotar - "Plotar" é um termo usado em programação e em análise de dados para descrever a criação de um gráfico
        self.ax.bar(df_agrupado.index, df_agrupado.values)
        self.ax.set_xlabel(col_x) #Define o titulo do eixo x
        self.ax.set_ylabel(col_y) #Define o titulo do eixo y
        self.ax.set_title(titulo_grafico)
        
        # Adicionar valores acima de cada barra
        """
         adicionar um rótulo para cada barra no gráfico de colunas gerado.

        O método enumerate é usado para criar um loop através do índice e valor de 
        cada elemento de df_agrupado.values. O valor do índice i é usado para determinar 
        a posição horizontal do rótulo em relação à barra correspondente, enquanto 
        o valor v é usado como a posição vertical.

        O método annotate é usado para adicionar um texto de rótulo em cada barra. 
        O argumento str(v) é o texto a ser exibido no rótulo e xy=(i, v) especifica as 
        coordenadas (x, y) do rótulo em relação à barra. Os argumentos ha='center' e 
        va='bottom' são usados para alinhar o rótulo horizontal e verticalmente, 
        respectivamente, ao centro e na parte inferior da barra.
        """
        for i, v in enumerate(df_agrupado.values):
            
            #"{:,.0f}".format(v) - coloca o separados de milhares e elimina as casas decimais
            self.ax.annotate("{:,.0f}".format(v), xy=(i, v), ha="center", va="bottom")
        
        #Rotacionando o eixo x para ser possivel visualizar no grafico
        #self.ax.set_xticklabels(df_agrupado.index, rotation=45, ha="right")
        
        #Limpa o texto do titulo dos eixos x e y e oculta para remover os espaços em branco
        self.ax.xaxis.set_label_text("")
        self.ax.xaxis.get_label().set_visible(False)
        
        self.ax.yaxis.set_label_text("")
        self.ax.yaxis.get_label().set_visible(False)
        
        #Expande as laterais para que o gráfico oculpe toda a área
        self.fig.tight_layout()
        
        self.canvas.draw() #Atualizo a visualização do canvas
        
        #Pego o número da imagem salvar o gráfico
        nome_imagem = self.cb_imagem.get()
        caminho_nome_imagem = f"{nome_imagem}.png"
        
        #getcwd - Retorno o diretório pasta atual do arquivo
        #path.join - Junta o diretorio com o nome da imagem
        caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
        
        """
        Essa linha de código salva o gráfico atualmente criado na figura associada 
        ao objeto ax em um arquivo de imagem especificado por caminho_imagem. A imagem é 
        salva em um formato definido pela extensão do arquivo nome_imagem e com uma resolução 
        de 80 pontos por polegada (dpi).

        O método savefig() é fornecido pela biblioteca matplotlib e é usado para salvar a 
        figura atual em um arquivo. O parâmetro caminho_imagem especifica o caminho completo e 
        o nome do arquivo a ser salvo. O parâmetro dpi especifica a resolução da imagem em 
        pontos por polegada (dots per inch).
        """
        self.ax.figure.savefig(caminho_imagem, dpi=80)
        
        #Fecha a janela
        self.janela_colunas.destroy()
        
    def gerar_grafico_colunas_2(self):
        
        #Limpa o grafico anterior
        self.ax.clear()
        
        #Obtem as colunas selecionadas na combobox
        col_x = self.cb_eixo_x.get()
        col_y = self.cb_eixo_y.get()
        
        #Agrupa valores de col_y (coluna com os números)
        #col_x - Coluna com os itens (textos) eu agrupo para deixar valores únicos
        df_agrupado = self.df.groupby(col_x).sum()[col_y]
        
        #Pega o titulo do gráfico digitado pelo usuário
        titulo_grafico = self.entry_titulo.get()
        
        # Plotar gráfico de barras com os valores somados
        # Plotar - "Plotar" é um termo usado em programação e em análise de dados para descrever a criação de um gráfico
        self.ax.bar(df_agrupado.index, df_agrupado.values)
        self.ax.set_xlabel(col_x) #Define o titulo do eixo x
        self.ax.set_ylabel(col_y) #Define o titulo do eixo y
        self.ax.set_title(titulo_grafico)
        self.ax.set_xticks(range(len(df_agrupado.index))) #Transforma em uma lista de inteiros
        self.ax.set_xticklabels(df_agrupado.index, rotation=45, ha="right") #Rotaciona o eixo x
        self.ax.grid(True, axis="y") #Adiciona grade no eixo y
        self.ax.figure.set_size_inches(10,6) #Define tamanho da figura do gráfico
        
        
        # Adicionar valores acima de cada barra
        """
         adicionar um rótulo para cada barra no gráfico de colunas gerado.

        O método enumerate é usado para criar um loop através do índice e valor de 
        cada elemento de df_agrupado.values. O valor do índice i é usado para determinar 
        a posição horizontal do rótulo em relação à barra correspondente, enquanto 
        o valor v é usado como a posição vertical.

        O método annotate é usado para adicionar um texto de rótulo em cada barra. 
        O argumento str(v) é o texto a ser exibido no rótulo e xy=(i, v) especifica as 
        coordenadas (x, y) do rótulo em relação à barra. Os argumentos ha='center' e 
        va='bottom' são usados para alinhar o rótulo horizontal e verticalmente, 
        respectivamente, ao centro e na parte inferior da barra.
        """
        for i, v in enumerate(df_agrupado.values):
            
            #"{:,.0f}".format(v) - coloca o separados de milhares e elimina as casas decimais
            self.ax.annotate("{:,.0f}".format(v), xy=(i, v), ha="center", va="bottom")
        
        #Rotacionando o eixo x para ser possivel visualizar no grafico
        #self.ax.set_xticklabels(df_agrupado.index, rotation=45, ha="right")
        
        #Limpa o texto do titulo dos eixos x e y e oculta para remover os espaços em branco
        self.ax.xaxis.set_label_text("")
        self.ax.xaxis.get_label().set_visible(False)
        
        self.ax.yaxis.set_label_text("")
        self.ax.yaxis.get_label().set_visible(False)
        
        #Expande as laterais para que o gráfico oculpe toda a área
        self.fig.tight_layout()
        
        self.canvas.draw() #Atualizo a visualização do canvas
        
        #Pego o número da imagem salvar o gráfico
        nome_imagem = self.cb_imagem.get()
        caminho_nome_imagem = f"{nome_imagem}.png"
        
        #getcwd - Retorno o diretório pasta atual do arquivo
        #path.join - Junta o diretorio com o nome da imagem
        caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
        
        """
        Essa linha de código salva o gráfico atualmente criado na figura associada 
        ao objeto ax em um arquivo de imagem especificado por caminho_imagem. A imagem é 
        salva em um formato definido pela extensão do arquivo nome_imagem e com uma resolução 
        de 80 pontos por polegada (dpi).

        O método savefig() é fornecido pela biblioteca matplotlib e é usado para salvar a 
        figura atual em um arquivo. O parâmetro caminho_imagem especifica o caminho completo e 
        o nome do arquivo a ser salvo. O parâmetro dpi especifica a resolução da imagem em 
        pontos por polegada (dots per inch).
        """
        self.ax.figure.savefig(caminho_imagem, dpi=80)
        
        #Fecha a janela
        self.janela_colunas.destroy()
        
    def abrir_janela_pizza(self):
        
        # Abrir janela para seleção de colunas
        # Criando uma nova janela com título, dimensões e colocando em foco
        self.janela_pizza = Toplevel(self.master)
        self.janela_pizza.title("Gráfico Pizza")
        self.janela_pizza.geometry("500x500")
        self.janela_pizza.grab_set() #Bloqueia todas as outras janelas
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo X" e adicionando a janela
        self.lb_eixo_x = Label(self.janela_pizza,
                                  font="Arial 22", 
                                  text="Eixo X:")
        self.lb_eixo_x.pack(pady=5)
        
        # Criando comboboxes para seleção de colunas
        # Criando um Combobox com as colunas do DataFrame como valores para a escolha do usuário e adicionando a janela
        #columns.tolist() é um método do pandas que retorna uma lista contendo os nomes das colunas de um DataFrame.
        self.cb_eixo_x = Combobox(self.janela_pizza,
                                  font="Arial 22", 
                                  values=self.df.columns.tolist())
        self.cb_eixo_x.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo Y" e adicionando a janela
        self.lb_eixo_y = Label(self.janela_pizza,
                                  font="Arial 22", 
                                  text="Eixo Y:")
        self.lb_eixo_y.pack(pady=5)
        
        # Criando comboboxes para seleção de colunas
        # Criando um Combobox com as colunas do DataFrame como valores para a escolha do usuário e adicionando a janela
        #columns.tolist() é um método do pandas que retorna uma lista contendo os nomes das colunas de um DataFrame.
        self.cb_eixo_y = Combobox(self.janela_pizza,
                                  font="Arial 22", 
                                  values=self.df.columns.tolist())
        self.cb_eixo_y.pack(pady=5)
        
        #--------------------------------------------------------------------
        # Criando uma Label com o texto "Eixo Y" e adicionando a janela
        self.lb_titulo = Label(self.janela_pizza,
                                  font="Arial 22", 
                                  text="Título:")
        self.lb_titulo.pack(pady=5)
        
        # Criando um campo de entrada de dados para inserir um titulo
        self.entry_titulo = Entry(self.janela_pizza,
                                  font="Arial 22")
        self.entry_titulo.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo X" e adicionando a janela
        self.lb_imagem = Label(self.janela_pizza, text="Imagem:",
                                  font="Arial 22",)
        self.lb_imagem.pack(pady=5)
        
        # Criando comboboxes para seleção do número da imagem
        self.cb_imagem = Combobox(self.janela_pizza,
                                  font="Arial 22",
                                  values=["image1", "image2", "image3", "image4", "image5", "image6", "image7", "image8"])
        self.cb_imagem.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        #Cria o botão para gerar o gráfico 1
        self.btn_gerar_grafico_1 = Button(self.janela_pizza,
                                               text= "Gráfico 1",
                                               font="Arial 26",
                                               command = self.gerar_grafico_pizza)
        self.btn_gerar_grafico_1.pack(side=LEFT, padx=5, pady=5)
        
        #--------------------------------------------------------------------
        
        #Cria o botão para gerar o gráfico 2
        self.btn_gerar_grafico_2 = Button(self.janela_pizza,
                                               text= "Gráfico 2",
                                               font="Arial 26",
                                               command = self.gerar_grafico_pizza_2)
        self.btn_gerar_grafico_2.pack(side=LEFT, padx=5, pady=5)
        
    def gerar_grafico_pizza(self):
        
        #Limpa o grafico anterior
        self.ax.clear()
        
        #Obtem as colunas selecionadas na combobox
        col_x = self.cb_eixo_x.get()
        col_y = self.cb_eixo_y.get()
        
        #Agrupa valores de col_y (coluna com os números)
        #col_x - Coluna com os itens (textos) eu agrupo para deixar valores únicos
        df_agrupado = self.df.groupby(col_x).sum()[col_y]
        
        #Pega o titulo do gráfico digitado pelo usuário
        titulo_grafico = self.entry_titulo.get()
        
        total = df_agrupado.sum() # obtem a soma dos valores agrupados da coluna y
        pedacos = [(v / total) * 100  for v in df_agrupado.values] # calcular a porcentagem de cada valor em relação ao total
        
        # Plotar gráfico de pizza com os valores somados e totais de cada pedaço
        self.ax.pie(df_agrupado.values, labels=[f"{label} ({pedaco:.1f}%)"
                                                # plotar o gráfico de pizza com os valores agrupados e suas respectivas porcentagens
                                                for label, pedaco in zip(df_agrupado.index, pedacos)])
        self.ax.set_title(titulo_grafico)
        
        # Adicionar valores acima de cada barra
        """
         adicionar um rótulo para cada barra no gráfico de colunas gerado.

        O método enumerate é usado para criar um loop através do índice e valor de 
        cada elemento de df_agrupado.values. O valor do índice i é usado para determinar 
        a posição horizontal do rótulo em relação à barra correspondente, enquanto 
        o valor v é usado como a posição vertical.

        O método annotate é usado para adicionar um texto de rótulo em cada barra. 
        O argumento str(v) é o texto a ser exibido no rótulo e xy=(i, v) especifica as 
        coordenadas (x, y) do rótulo em relação à barra. Os argumentos ha='center' e 
        va='bottom' são usados para alinhar o rótulo horizontal e verticalmente, 
        respectivamente, ao centro e na parte inferior da barra.
        """
        for i, v in enumerate(df_agrupado.values):
            
            #"{:,.0f}".format(v) - coloca o separados de milhares e elimina as casas decimais
            self.ax.annotate("{:,.0f}".format(v), xy=(i, v), ha="center", va="bottom")
        
        #Rotacionando o eixo x para ser possivel visualizar no grafico
        #self.ax.set_xticklabels(df_agrupado.index, rotation=45, ha="right")
        
        self.canvas.draw() #Atualizo a visualização do canvas
        
        #Pego o número da imagem salvar o gráfico
        nome_imagem = self.cb_imagem.get()
        caminho_nome_imagem = f"{nome_imagem}.png"
        
        #getcwd - Retorno o diretório pasta atual do arquivo
        #path.join - Junta o diretorio com o nome da imagem
        caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
        
        """
        Essa linha de código salva o gráfico atualmente criado na figura associada 
        ao objeto ax em um arquivo de imagem especificado por caminho_imagem. A imagem é 
        salva em um formato definido pela extensão do arquivo nome_imagem e com uma resolução 
        de 80 pontos por polegada (dpi).

        O método savefig() é fornecido pela biblioteca matplotlib e é usado para salvar a 
        figura atual em um arquivo. O parâmetro caminho_imagem especifica o caminho completo e 
        o nome do arquivo a ser salvo. O parâmetro dpi especifica a resolução da imagem em 
        pontos por polegada (dots per inch).
        """
        self.ax.figure.savefig(caminho_imagem, dpi=80)
        
        #Fecha a janela
        #self.janela_colunas.destroy()
        
    def gerar_grafico_pizza_2(self):
        
        #Limpa o grafico anterior
        self.ax.clear()
        
        #Obtem as colunas selecionadas na combobox
        col_x = self.cb_eixo_x.get()
        col_y = self.cb_eixo_y.get()
        
        #Agrupa valores de col_y (coluna com os números)
        #col_x - Coluna com os itens (textos) eu agrupo para deixar valores únicos
        df_agrupado = self.df.groupby(col_x).sum()[col_y]
        
        #Pega o titulo do gráfico digitado pelo usuário
        titulo_grafico = self.entry_titulo.get()
        
        #Calcula o total de cada pedaço
        total = df_agrupado.sum() # obtem a soma dos valores agrupados da coluna y
        #pedacos = [(v / total) * 100  for v in df_agrupado.values] # calcular a porcentagem de cada valor em relação ao total
        
        # Plotar gráfico de pizza com os valores somados e totais de cada pedaço
        """
        Esta linha de código cria os rótulos das fatias do gráfico de pizza com 
        os valores absolutos de cada pedaço.

        O zip é uma função que cria um iterador que combina as informações 
        de duas listas. Neste caso, ele combina os valores do índice de 
        df_agrupado com os valores da coluna col_y.

        Na lista por compreensão, a variável label representa cada valor do 
        índice de df_agrupado, enquanto value representa cada valor da coluna 
        col_y.

        A expressão f"{label} ({value:.0f})" cria uma string que combina o valor 
        do índice (representado pela variável label) com o valor absoluto da 
        coluna col_y (representado pela variável value). O :.0f na expressão 
        significa que a string deve conter apenas números inteiros.

        Portanto, a linha de código cria uma lista de strings com o rótulo de 
        cada fatia do gráfico de pizza, no formato "valor (valor_absoluto)".
        """
        self.ax.pie(df_agrupado.values, labels=[f"{label} ({value:.0f})"
                                                # plotar o gráfico de pizza com os valores agrupados e suas respectivas porcentagens
                                                for label, value in zip(df_agrupado.index, df_agrupado.values)],
                                                autopct="%1.0f%%") #Define que cada fatia da pizza deve ter um percentual
        self.ax.set_title(titulo_grafico)
        
        # Adicionar valores acima de cada barra
        """
         adicionar um rótulo para cada barra no gráfico de colunas gerado.

        O método enumerate é usado para criar um loop através do índice e valor de 
        cada elemento de df_agrupado.values. O valor do índice i é usado para determinar 
        a posição horizontal do rótulo em relação à barra correspondente, enquanto 
        o valor v é usado como a posição vertical.

        O método annotate é usado para adicionar um texto de rótulo em cada barra. 
        O argumento str(v) é o texto a ser exibido no rótulo e xy=(i, v) especifica as 
        coordenadas (x, y) do rótulo em relação à barra. Os argumentos ha='center' e 
        va='bottom' são usados para alinhar o rótulo horizontal e verticalmente, 
        respectivamente, ao centro e na parte inferior da barra.
        """
        for i, v in enumerate(df_agrupado.values):
            
            #"{:,.0f}".format(v) - coloca o separados de milhares e elimina as casas decimais
            self.ax.annotate("{:,.0f}".format(v), xy=(i, v), ha="center", va="bottom")
        
        #Rotacionando o eixo x para ser possivel visualizar no grafico
        #self.ax.set_xticklabels(df_agrupado.index, rotation=45, ha="right")
        
        self.canvas.draw() #Atualizo a visualização do canvas
        
        #Pego o número da imagem salvar o gráfico
        nome_imagem = self.cb_imagem.get()
        caminho_nome_imagem = f"{nome_imagem}.png"
        
        #getcwd - Retorno o diretório pasta atual do arquivo
        #path.join - Junta o diretorio com o nome da imagem
        caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
        
        """
        Essa linha de código salva o gráfico atualmente criado na figura associada 
        ao objeto ax em um arquivo de imagem especificado por caminho_imagem. A imagem é 
        salva em um formato definido pela extensão do arquivo nome_imagem e com uma resolução 
        de 80 pontos por polegada (dpi).

        O método savefig() é fornecido pela biblioteca matplotlib e é usado para salvar a 
        figura atual em um arquivo. O parâmetro caminho_imagem especifica o caminho completo e 
        o nome do arquivo a ser salvo. O parâmetro dpi especifica a resolução da imagem em 
        pontos por polegada (dots per inch).
        """
        self.ax.figure.savefig(caminho_imagem, dpi=80)
        
        #Fecha a janela
        #self.janela_colunas.destroy()
        
    def abrir_janela_linhas(self):
        
        # Abrir janela para seleção de colunas
        # Criando uma nova janela com título, dimensões e colocando em foco
        self.janela_linhas = Toplevel(self.master)
        self.janela_linhas.title("Gráfico Linhas")
        self.janela_linhas.geometry("500x500")
        self.janela_linhas.grab_set() #Bloqueia todas as outras janelas
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo X" e adicionando a janela
        self.lb_eixo_x = Label(self.janela_linhas,
                                  font="Arial 22", 
                                  text="Eixo X:")
        self.lb_eixo_x.pack(pady=5)
        
        # Criando comboboxes para seleção de colunas
        # Criando um Combobox com as colunas do DataFrame como valores para a escolha do usuário e adicionando a janela
        #columns.tolist() é um método do pandas que retorna uma lista contendo os nomes das colunas de um DataFrame.
        self.cb_eixo_x = Combobox(self.janela_linhas,
                                  font="Arial 22", 
                                  values=self.df.columns.tolist())
        self.cb_eixo_x.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo Y" e adicionando a janela
        self.lb_eixo_y = Label(self.janela_linhas,
                                  font="Arial 22", 
                                  text="Eixo Y:")
        self.lb_eixo_y.pack(pady=5)
        
        # Criando comboboxes para seleção de colunas
        # Criando um Combobox com as colunas do DataFrame como valores para a escolha do usuário e adicionando a janela
        #columns.tolist() é um método do pandas que retorna uma lista contendo os nomes das colunas de um DataFrame.
        self.cb_eixo_y = Combobox(self.janela_linhas,
                                  font="Arial 22", 
                                  values=self.df.columns.tolist())
        self.cb_eixo_y.pack(pady=5)
        
        #--------------------------------------------------------------------
        # Criando uma Label com o texto "Eixo Y" e adicionando a janela
        self.lb_titulo = Label(self.janela_linhas,
                                  font="Arial 22", 
                                  text="Título:")
        self.lb_titulo.pack(pady=5)
        
        # Criando um campo de entrada de dados para inserir um titulo
        self.entry_titulo = Entry(self.janela_linhas,
                                  font="Arial 22")
        self.entry_titulo.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo X" e adicionando a janela
        self.lb_imagem = Label(self.janela_linhas, text="Imagem:",
                                  font="Arial 22",)
        self.lb_imagem.pack(pady=5)
        
        # Criando comboboxes para seleção do número da imagem
        self.cb_imagem = Combobox(self.janela_linhas,
                                  font="Arial 22",
                                  values=["image1", "image2", "image3", "image4", "image5", "image6", "image7", "image8"])
        self.cb_imagem.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        #Cria o botão para gerar o gráfico 1
        self.btn_gerar_grafico_1 = Button(self.janela_linhas,
                                               text= "Gráfico 1",
                                               font="Arial 26",
                                               command = self.gerar_grafico_linhas)
        self.btn_gerar_grafico_1.pack(side=LEFT, padx=5, pady=5)
        
        #--------------------------------------------------------------------
        
        #Cria o botão para gerar o gráfico 2
        self.btn_gerar_grafico_2 = Button(self.janela_linhas,
                                               text= "Gráfico 2",
                                               font="Arial 26",
                                               command = self.gerar_grafico_linhas_2)
        self.btn_gerar_grafico_2.pack(side=LEFT, padx=5, pady=5)
        
    def gerar_grafico_linhas(self):
        
        #Limpa o grafico anterior
        self.ax.clear()
        
        #Obtem as colunas selecionadas na combobox
        col_x = self.cb_eixo_x.get()
        col_y = self.cb_eixo_y.get()
        
        #Agrupa valores de col_y (coluna com os números)
        #col_x - Coluna com os itens (textos) eu agrupo para deixar valores únicos
        df_agrupado = self.df.groupby(col_x).sum()[col_y]
        
        #Pega o titulo do gráfico digitado pelo usuário
        titulo_grafico = self.entry_titulo.get()
        
        # Plotar gráfico de linhas com os valores somados
        # Plotar - "Plotar" é um termo usado em programação e em análise de dados para descrever a criação de um gráfico
        self.ax.plot(df_agrupado.index, df_agrupado.values)
        self.ax.set_xlabel(col_x) #Define o titulo do eixo x
        self.ax.set_ylabel(col_y) #Define o titulo do eixo y
        self.ax.set_title(titulo_grafico)
        
        # Adicionar valores acima de cada barra
        """
            adiciona anotações aos pontos do gráfico de linhas com os valores de y 
            correspondentes.

            A função annotate é usada para adicionar texto em um gráfico do Matplotlib 
            e aceita vários argumentos para personalizar a posição, o estilo e o formato 
            do texto. Na linha em questão, os argumentos são:

            str(v): converte o valor de y (representado pela variável v) em uma string 
            para ser exibida como texto no gráfico.
            
            xy=(df_agrupado.index[i], df_agrupado.values[i]): especifica a posição da 
            anotação no gráfico, que é definida pelas coordenadas x e y do ponto 
            correspondente. No caso, x é o valor da coluna x agrupado pelo 
            índice i (representado por df_agrupado.index[i]) e y é o valor da coluna y 
            correspondente ao índice i (representado por df_agrupado.values[i]).
            
            ha='center': define a posição horizontal do texto em relação ao ponto 
            de referência (no caso, o ponto do gráfico), que é o centro do texto.
            
            va='bottom': define a posição vertical do texto em relação ao ponto de 
            referência, que é a base do texto (ou seja, o texto é alinhado na parte inferior).
        """

        for i, v in enumerate(df_agrupado.values):
            
            #"{:,.0f}".format(v) - coloca o separados de milhares e elimina as casas decimais
            self.ax.annotate("{:,.0f}".format(v), xy=(df_agrupado.index[i], df_agrupado.values[i]), ha="center", va="bottom")
        
        #Rotacionando o eixo x para ser possivel visualizar no grafico
        #self.ax.set_xticklabels(df_agrupado.index, rotation=45, ha="right")
        
        #Limpa o texto do titulo dos eixos x e y e oculta para remover os espaços em branco
        self.ax.xaxis.set_label_text("")
        self.ax.xaxis.get_label().set_visible(False)
        
        self.ax.yaxis.set_label_text("")
        self.ax.yaxis.get_label().set_visible(False)
        
        #Expande as laterais para que o gráfico oculpe toda a área
        self.fig.tight_layout()
        
        self.canvas.draw() #Atualizo a visualização do canvas
        
        #Pego o número da imagem salvar o gráfico
        nome_imagem = self.cb_imagem.get()
        caminho_nome_imagem = f"{nome_imagem}.png"
        
        #getcwd - Retorno o diretório pasta atual do arquivo
        #path.join - Junta o diretorio com o nome da imagem
        caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
        
        """
        Essa linha de código salva o gráfico atualmente criado na figura associada 
        ao objeto ax em um arquivo de imagem especificado por caminho_imagem. A imagem é 
        salva em um formato definido pela extensão do arquivo nome_imagem e com uma resolução 
        de 80 pontos por polegada (dpi).

        O método savefig() é fornecido pela biblioteca matplotlib e é usado para salvar a 
        figura atual em um arquivo. O parâmetro caminho_imagem especifica o caminho completo e 
        o nome do arquivo a ser salvo. O parâmetro dpi especifica a resolução da imagem em 
        pontos por polegada (dots per inch).
        """
        self.ax.figure.savefig(caminho_imagem, dpi=80)
        
        #Fecha a janela
        self.janela_linhas.destroy()
        
    def gerar_grafico_linhas_2(self):
        
        #Limpa o grafico anterior
        self.ax.clear()
        
        #Obtem as colunas selecionadas na combobox
        col_x = self.cb_eixo_x.get()
        col_y = self.cb_eixo_y.get()
        
        #Agrupa valores de col_y (coluna com os números)
        #col_x - Coluna com os itens (textos) eu agrupo para deixar valores únicos
        df_agrupado = self.df.groupby(col_x).sum()[col_y]
        
        #Pega o titulo do gráfico digitado pelo usuário
        titulo_grafico = self.entry_titulo.get()
        
        # Plotar gráfico de linhas com os valores somados
        """
        self.ax é o objeto que representa o eixo do gráfico;
        
        df_agrupado.index e df_agrupado.values são os dados que serão plotados nos 
        eixos x e y, respectivamente;
        
        '-o' é um parâmetro que especifica que os pontos devem ser marcados com círculos;
        color='mediumseagreen' é um parâmetro que define a cor das linhas e dos pontos 
        do gráfico;
        
        linewidth=2 é um parâmetro que define a espessura da linha do gráfico;
        
        markersize=8 é um parâmetro que define o tamanho dos pontos do gráfico.
        """
        self.ax.plot(df_agrupado.index, df_agrupado.values,
                    '-o', color="mediumseagreen",
                    linewidth=2,
                    markersize=8)
        self.ax.set_xlabel(col_x) #Define o titulo do eixo x
        self.ax.set_ylabel(col_y) #Define o titulo do eixo y
        self.ax.set_title(titulo_grafico)
        
        # Adicionar valores acima de cada barra
        """
            adiciona anotações aos pontos do gráfico de linhas com os valores de y 
            correspondentes.

            A função annotate é usada para adicionar texto em um gráfico do Matplotlib 
            e aceita vários argumentos para personalizar a posição, o estilo e o formato 
            do texto. Na linha em questão, os argumentos são:

            str(v): converte o valor de y (representado pela variável v) em uma string 
            para ser exibida como texto no gráfico.
            
            xy=(df_agrupado.index[i], df_agrupado.values[i]): especifica a posição da 
            anotação no gráfico, que é definida pelas coordenadas x e y do ponto 
            correspondente. No caso, x é o valor da coluna x agrupado pelo 
            índice i (representado por df_agrupado.index[i]) e y é o valor da coluna y 
            correspondente ao índice i (representado por df_agrupado.values[i]).
            
            ha='center': define a posição horizontal do texto em relação ao ponto 
            de referência (no caso, o ponto do gráfico), que é o centro do texto.
            
            va='bottom': define a posição vertical do texto em relação ao ponto de 
            referência, que é a base do texto (ou seja, o texto é alinhado na parte inferior).
        """

        for i, v in enumerate(df_agrupado.values):
            
            #"{:,.0f}".format(v) - coloca o separados de milhares e elimina as casas decimais
            valor_formatado = "{:,.0f}".format(v)
            
            """
            adiciona rótulos com os valores de v em cada ponto do gráfico.

            self.ax.annotate() é um método que adiciona uma anotação no gráfico;
            
            xy=(df_agrupado.index[i], df_agrupado.values[i]) é um parâmetro que especifica
            a posição da anotação no gráfico;
            
            ha='center' é um parâmetro que alinha horizontalmente o texto da anotação 
            ao centro;
            
            va='bottom' é um parâmetro que alinha verticalmente o texto da anotação 
            na parte inferior;
            
            fontsize=10 é um parâmetro que define o tamanho da fonte do texto da anotação.
            """                             
            self.ax.annotate(valor_formatado, 
                             xy=(df_agrupado.index[i], 
                                 df_agrupado.values[i]), 
                                 ha="center", 
                                 va="bottom",
                                 fontsize=10)
            
        #Configur funo branco para o gráfico
        self.ax.set_facecolor("white")
        self.ax.grid(color="lightgray", linestyle="-", linewidth=0.5)
        
        #Rotaciona o eixo x
        self.ax.set_xticks(range(len(df_agrupado.index))) #Transforma em uma lista de inteiros
        self.ax.set_xticklabels(df_agrupado.index, rotation=40)
        
        #Limpa o texto do titulo dos eixos x e y e oculta para remover os espaços em branco
        self.ax.xaxis.set_label_text("")
        self.ax.xaxis.get_label().set_visible(False)
        
        self.ax.yaxis.set_label_text("")
        self.ax.yaxis.get_label().set_visible(False)
        
        #Expande as laterais para que o gráfico oculpe toda a área
        self.fig.tight_layout()
        
        self.canvas.draw() #Atualizo a visualização do canvas
        
        #Pego o número da imagem salvar o gráfico
        nome_imagem = self.cb_imagem.get()
        caminho_nome_imagem = f"{nome_imagem}.png"
        
        #getcwd - Retorno o diretório pasta atual do arquivo
        #path.join - Junta o diretorio com o nome da imagem
        caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
        
        """
        Essa linha de código salva o gráfico atualmente criado na figura associada 
        ao objeto ax em um arquivo de imagem especificado por caminho_imagem. A imagem é 
        salva em um formato definido pela extensão do arquivo nome_imagem e com uma resolução 
        de 80 pontos por polegada (dpi).

        O método savefig() é fornecido pela biblioteca matplotlib e é usado para salvar a 
        figura atual em um arquivo. O parâmetro caminho_imagem especifica o caminho completo e 
        o nome do arquivo a ser salvo. O parâmetro dpi especifica a resolução da imagem em 
        pontos por polegada (dots per inch).
        """
        self.ax.figure.savefig(caminho_imagem, dpi=80)
        
        #Fecha a janela
        self.janela_linhas.destroy()
        
    def abrir_janela_area(self):
        
        # Abrir janela para seleção de colunas
        # Criando uma nova janela com título, dimensões e colocando em foco
        self.janela_area = Toplevel(self.master)
        self.janela_area.title("Gráfico Área")
        self.janela_area.geometry("500x500")
        self.janela_area.grab_set() #Bloqueia todas as outras janelas
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo X" e adicionando a janela
        self.lb_eixo_x = Label(self.janela_area,
                                  font="Arial 22", 
                                  text="Eixo X:")
        self.lb_eixo_x.pack(pady=5)
        
        # Criando comboboxes para seleção de colunas
        # Criando um Combobox com as colunas do DataFrame como valores para a escolha do usuário e adicionando a janela
        #columns.tolist() é um método do pandas que retorna uma lista contendo os nomes das colunas de um DataFrame.
        self.cb_eixo_x = Combobox(self.janela_area,
                                  font="Arial 22", 
                                  values=self.df.columns.tolist())
        self.cb_eixo_x.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo Y" e adicionando a janela
        self.lb_eixo_y = Label(self.janela_area,
                                  font="Arial 22", 
                                  text="Eixo Y:")
        self.lb_eixo_y.pack(pady=5)
        
        # Criando comboboxes para seleção de colunas
        # Criando um Combobox com as colunas do DataFrame como valores para a escolha do usuário e adicionando a janela
        #columns.tolist() é um método do pandas que retorna uma lista contendo os nomes das colunas de um DataFrame.
        self.cb_eixo_y = Combobox(self.janela_area,
                                  font="Arial 22", 
                                  values=self.df.columns.tolist())
        self.cb_eixo_y.pack(pady=5)
        
        #--------------------------------------------------------------------
        # Criando uma Label com o texto "Eixo Y" e adicionando a janela
        self.lb_titulo = Label(self.janela_area,
                                  font="Arial 22", 
                                  text="Título:")
        self.lb_titulo.pack(pady=5)
        
        # Criando um campo de entrada de dados para inserir um titulo
        self.entry_titulo = Entry(self.janela_area,
                                  font="Arial 22")
        self.entry_titulo.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo X" e adicionando a janela
        self.lb_imagem = Label(self.janela_area, text="Imagem:",
                                  font="Arial 22",)
        self.lb_imagem.pack(pady=5)
        
        # Criando comboboxes para seleção do número da imagem
        self.cb_imagem = Combobox(self.janela_area,
                                  font="Arial 22",
                                  values=["image1", "image2", "image3", "image4", "image5", "image6", "image7", "image8"])
        self.cb_imagem.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        #Cria o botão para gerar o gráfico 1
        self.btn_gerar_grafico_1 = Button(self.janela_area,
                                               text= "Gráfico 1",
                                               font="Arial 26",
                                               command = self.gerar_grafico_area)
        self.btn_gerar_grafico_1.pack(side=LEFT, padx=5, pady=5)
        
        #--------------------------------------------------------------------
        
        #Cria o botão para gerar o gráfico 2
        self.btn_gerar_grafico_2 = Button(self.janela_area,
                                               text= "Gráfico 2",
                                               font="Arial 26",
                                               command = self.gerar_grafico_area_2)
        self.btn_gerar_grafico_2.pack(side=LEFT, padx=5, pady=5)
        
        
    def gerar_grafico_area(self):
        
        #Limpa o grafico anterior
        self.ax.clear()
        
        #Obtem as colunas selecionadas na combobox
        col_x = self.cb_eixo_x.get()
        col_y = self.cb_eixo_y.get()
        
        #Agrupa valores de col_y (coluna com os números)
        #col_x - Coluna com os itens (textos) eu agrupo para deixar valores únicos
        df_agrupado = self.df.groupby(col_x).sum()[col_y]
        
        #Pega o titulo do gráfico digitado pelo usuário
        titulo_grafico = self.entry_titulo.get()
        
        """
        cria uma área preenchida entre o eixo x e a linha do gráfico de áreas. 
        Os parâmetros passados são:

        df_agrupado.index: os valores do eixo x.
        df_agrupado.values: os valores do eixo y.
        color='blue': define a cor azul para a área preenchida.
        alpha=0.2: define a transparência da área preenchida como 20%, ou seja, 
        a área preenchida é semi-transparente.
        """
        self.ax.fill_between(df_agrupado.index,
                            df_agrupado.values,
                            color="blue",
                            alpha=0.2)
        
        """
        plota uma linha em um gráfico de área, usando os valores do eixo X e Y 
        a partir do DataFrame agrupado.

        df_agrupado.index é uma série Pandas contendo as categorias do 
        eixo X (coluna selecionada em self.cb_eixo_x), e é usada como os valores do 
        eixo X no gráfico.
        
        df_agrupado.values é uma série Pandas contendo os valores agrupados do 
        eixo Y (coluna selecionada em self.cb_eixo_y), e é usada como os valores do 
        eixo Y no gráfico.
        
        color='blue' define a cor da linha como azul.

        Dessa forma, o método plot() é usado para plotar a linha com base nos valores 
        do eixo X e Y.
        """
        self.ax.plot(df_agrupado.index, 
                     df_agrupado.values,
                    color="blue")
        self.ax.set_xlabel(col_x) #Define o titulo do eixo x
        self.ax.set_ylabel(col_y) #Define o titulo do eixo y
        self.ax.set_title(titulo_grafico)
        
        """
            adiciona um rótulo com o valor de cada ponto no gráfico de áreas. 
            O método annotate adiciona texto em um ponto específico do gráfico. 
            O argumento str(v) converte o valor do ponto para uma string. 
            O argumento xy define a posição do rótulo no gráfico, que é o ponto em 
            que as coordenadas x e y são especificadas por (df_agrupado.index[i],
            df_agrupado.values[i]). O argumento ha configura a alinhamento horizontal 
            do rótulo (horizontal alignment) para 'center', ou seja, alinhado ao 
            centro do ponto. O argumento va configura o alinhamento vertical do 
            rótulo (vertical alignment) para 'bottom', ou seja, alinhado à base do ponto.
            
            """

        for i, v in enumerate(df_agrupado.values):
            
            #"{:,.0f}".format(v) - coloca o separados de milhares e elimina as casas decimais
            self.ax.annotate("{:,.0f}".format(v), 
                             xy=(df_agrupado.index[i], 
                                 df_agrupado.values[i]),
                                 ha='center', va='bottom')
        
        #Rotaciona o eixo x
        self.ax.set_xticks(range(len(df_agrupado.index))) #Transforma em uma lista de inteiros
        self.ax.set_xticklabels(df_agrupado.index, rotation=40)
        
        #Limpa o texto do titulo dos eixos x e y e oculta para remover os espaços em branco
        self.ax.xaxis.set_label_text("")
        self.ax.xaxis.get_label().set_visible(False)
        
        self.ax.yaxis.set_label_text("")
        self.ax.yaxis.get_label().set_visible(False)
        
        #Expande as laterais para que o gráfico oculpe toda a área
        self.fig.tight_layout()
        
        self.canvas.draw() #Atualizo a visualização do canvas
        
        #Pego o número da imagem salvar o gráfico
        nome_imagem = self.cb_imagem.get()
        caminho_nome_imagem = f"{nome_imagem}.png"
        
        #getcwd - Retorno o diretório pasta atual do arquivo
        #path.join - Junta o diretorio com o nome da imagem
        caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
        
        """
        Essa linha de código salva o gráfico atualmente criado na figura associada 
        ao objeto ax em um arquivo de imagem especificado por caminho_imagem. A imagem é 
        salva em um formato definido pela extensão do arquivo nome_imagem e com uma resolução 
        de 80 pontos por polegada (dpi).

        O método savefig() é fornecido pela biblioteca matplotlib e é usado para salvar a 
        figura atual em um arquivo. O parâmetro caminho_imagem especifica o caminho completo e 
        o nome do arquivo a ser salvo. O parâmetro dpi especifica a resolução da imagem em 
        pontos por polegada (dots per inch).
        """
        self.ax.figure.savefig(caminho_imagem, dpi=80)
        
        #Fecha a janela
        self.janela_area.destroy()
        
        
    def gerar_grafico_area_2(self):
        
        #Limpa o grafico anterior
        self.ax.clear()
        
        #Obtem as colunas selecionadas na combobox
        col_x = self.cb_eixo_x.get()
        col_y = self.cb_eixo_y.get()
        
        #Agrupa valores de col_y (coluna com os números)
        #col_x - Coluna com os itens (textos) eu agrupo para deixar valores únicos
        df_agrupado = self.df.groupby(col_x).sum()[col_y]
        
        #Pega o titulo do gráfico digitado pelo usuário
        titulo_grafico = self.entry_titulo.get()
        
        """
        cria uma área preenchida entre o eixo x e a linha do gráfico de áreas. 
        Os parâmetros passados são:

        df_agrupado.index: os valores do eixo x.
        df_agrupado.values: os valores do eixo y.
        color='blue': define a cor azul para a área preenchida.
        alpha=0.2: define a transparência da área preenchida como 20%, ou seja, 
        a área preenchida é semi-transparente.
        label - Rótulo para a legenda do grafico do eixo x
        """
        self.ax.fill_between(df_agrupado.index,
                            df_agrupado.values,
                            color="blue",
                            alpha=0.2,
                            label=col_y)
        
        """
        plota uma linha em um gráfico de área, usando os valores do eixo X e Y 
        a partir do DataFrame agrupado.

        df_agrupado.index é uma série Pandas contendo as categorias do 
        eixo X (coluna selecionada em self.cb_eixo_x), e é usada como os valores do 
        eixo X no gráfico.
        
        df_agrupado.values é uma série Pandas contendo os valores agrupados do 
        eixo Y (coluna selecionada em self.cb_eixo_y), e é usada como os valores do 
        eixo Y no gráfico.
        
        color='blue' define a cor da linha como azul.

        Dessa forma, o método plot() é usado para plotar a linha com base nos valores 
        do eixo X e Y.
        """
        self.ax.plot(df_agrupado.index, 
                     df_agrupado.values,
                    color="red",
                    label=f"{col_y} (linha)")
        self.ax.set_xlabel(col_x) #Define o titulo do eixo x
        self.ax.set_ylabel("Soma de " + col_y) #Define o titulo do eixo y
        self.ax.set_title(titulo_grafico)
        self.ax.legend()
        
        self.ax.grid(True)
        
        """
            adiciona um rótulo com o valor de cada ponto no gráfico de áreas. 
            O método annotate adiciona texto em um ponto específico do gráfico. 
            O argumento str(v) converte o valor do ponto para uma string. 
            O argumento xy define a posição do rótulo no gráfico, que é o ponto em 
            que as coordenadas x e y são especificadas por (df_agrupado.index[i],
            df_agrupado.values[i]). O argumento ha configura a alinhamento horizontal 
            do rótulo (horizontal alignment) para 'center', ou seja, alinhado ao 
            centro do ponto. O argumento va configura o alinhamento vertical do 
            rótulo (vertical alignment) para 'bottom', ou seja, alinhado à base do ponto.
            
            """

        for i, v in enumerate(df_agrupado.values):
            
            #"{:,.0f}".format(v) - coloca o separados de milhares e elimina as casas decimais
            self.ax.annotate("{:,.0f}".format(v), 
                             xy=(df_agrupado.index[i], 
                                 df_agrupado.values[i]),
                                 ha='center', va='bottom')
        
        #Rotaciona o eixo x
        self.ax.set_xticks(range(len(df_agrupado.index))) #Transforma em uma lista de inteiros
        self.ax.set_xticklabels(df_agrupado.index, rotation=40)
        
        #Limpa o texto do titulo dos eixos x e y e oculta para remover os espaços em branco
        self.ax.xaxis.set_label_text("")
        self.ax.xaxis.get_label().set_visible(False)
        
        self.ax.yaxis.set_label_text("")
        self.ax.yaxis.get_label().set_visible(False)
        
        #Expande as laterais para que o gráfico oculpe toda a área
        self.fig.tight_layout()
        
        self.canvas.draw() #Atualizo a visualização do canvas
        
        #Pego o número da imagem salvar o gráfico
        nome_imagem = self.cb_imagem.get()
        caminho_nome_imagem = f"{nome_imagem}.png"
        
        #getcwd - Retorno o diretório pasta atual do arquivo
        #path.join - Junta o diretorio com o nome da imagem
        caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
        
        """
        Essa linha de código salva o gráfico atualmente criado na figura associada 
        ao objeto ax em um arquivo de imagem especificado por caminho_imagem. A imagem é 
        salva em um formato definido pela extensão do arquivo nome_imagem e com uma resolução 
        de 80 pontos por polegada (dpi).

        O método savefig() é fornecido pela biblioteca matplotlib e é usado para salvar a 
        figura atual em um arquivo. O parâmetro caminho_imagem especifica o caminho completo e 
        o nome do arquivo a ser salvo. O parâmetro dpi especifica a resolução da imagem em 
        pontos por polegada (dots per inch).
        """
        self.ax.figure.savefig(caminho_imagem, dpi=80)
        
        #Fecha a janela
        self.janela_area.destroy()
        
    def abrir_janela_funil(self):
        
        # Abrir janela para seleção de colunas
        # Criando uma nova janela com título, dimensões e colocando em foco
        self.janela_funil = Toplevel(self.master)
        self.janela_funil.title("Gráfico Funil")
        self.janela_funil.geometry("500x500")
        self.janela_funil.grab_set() #Bloqueia todas as outras janelas
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo X" e adicionando a janela
        self.lb_eixo_x = Label(self.janela_funil,
                                  font="Arial 22", 
                                  text="Eixo X:")
        self.lb_eixo_x.pack(pady=5)
        
        # Criando comboboxes para seleção de colunas
        # Criando um Combobox com as colunas do DataFrame como valores para a escolha do usuário e adicionando a janela
        #columns.tolist() é um método do pandas que retorna uma lista contendo os nomes das colunas de um DataFrame.
        self.cb_eixo_x = Combobox(self.janela_funil,
                                  font="Arial 22", 
                                  values=self.df.columns.tolist())
        self.cb_eixo_x.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo Y" e adicionando a janela
        self.lb_eixo_y = Label(self.janela_funil,
                                  font="Arial 22", 
                                  text="Eixo Y:")
        self.lb_eixo_y.pack(pady=5)
        
        # Criando comboboxes para seleção de colunas
        # Criando um Combobox com as colunas do DataFrame como valores para a escolha do usuário e adicionando a janela
        #columns.tolist() é um método do pandas que retorna uma lista contendo os nomes das colunas de um DataFrame.
        self.cb_eixo_y = Combobox(self.janela_funil,
                                  font="Arial 22", 
                                  values=self.df.columns.tolist())
        self.cb_eixo_y.pack(pady=5)
        
        #--------------------------------------------------------------------
        # Criando uma Label com o texto "Eixo Y" e adicionando a janela
        self.lb_titulo = Label(self.janela_funil,
                                  font="Arial 22", 
                                  text="Título:")
        self.lb_titulo.pack(pady=5)
        
        # Criando um campo de entrada de dados para inserir um titulo
        self.entry_titulo = Entry(self.janela_funil,
                                  font="Arial 22")
        self.entry_titulo.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        # Criando uma Label com o texto "Eixo X" e adicionando a janela
        self.lb_imagem = Label(self.janela_funil, text="Imagem:",
                                  font="Arial 22",)
        self.lb_imagem.pack(pady=5)
        
        # Criando comboboxes para seleção do número da imagem
        self.cb_imagem = Combobox(self.janela_funil,
                                  font="Arial 22",
                                  values=["image1", "image2", "image3", "image4", "image5", "image6", "image7", "image8"])
        self.cb_imagem.pack(pady=5)
        
        #--------------------------------------------------------------------
        
        #Cria o botão para gerar o gráfico 1
        self.btn_gerar_grafico_1 = Button(self.janela_funil,
                                               text= "Gráfico 1",
                                               font="Arial 40",
                                               command = self.gerar_grafico_funil)
        self.btn_gerar_grafico_1.pack(side=LEFT, padx=5, pady=5)
        
    def gerar_grafico_funil(self):
        
        #Limpa o grafico anterior
        self.ax.clear()
        
        #Obtem as colunas selecionadas na combobox
        col_x = self.cb_eixo_x.get()
        col_y = self.cb_eixo_y.get()
        
        #Agrupa valores de col_y (coluna com os números)
        #col_x - Coluna com os itens (textos) eu agrupo para deixar valores únicos
        df_agrupado = self.df.groupby(col_x).sum()[col_y]
        
        #Pega o titulo do gráfico digitado pelo usuário
        titulo_grafico = self.entry_titulo.get()
        
        #Ordena os valores em ordem descrecente
        df_agrupado = df_agrupado.sort_values(ascending=True)
        
        #cumsum() - Função do pandas retorna uma série contendo a soma cumulativa
        perc_acumuladas = (df_agrupado.cumsum() / df_agrupado.sum()) * 100 #Calcula o percentual
        
        #Calcular a altura das barras do funil
        """
        Vamos entender como a lista alturas é construída:

        alturas = [perc_acumuladas.iloc[0]]: O primeiro elemento da lista alturas 
        é a porcentagem acumulada do primeiro item da coluna col_y, armazenada em 
        perc_acumuladas.iloc[0]. Ou seja, o primeiro elemento da lista alturas 
        corresponde à altura da primeira barra do gráfico de funil.

        [perc_acumuladas.iloc[i] - perc_acumuladas.iloc[i-1] 
        for i in range(1, len(perc_acumuladas))]: Para os demais elementos da 
        lista alturas, é feito um laço que percorre todos os elementos da coluna col_y, 
        exceto o primeiro (que já foi incluído na lista alturas na primeira parte da 
        linha de código). Para cada elemento da coluna col_y, é calculada a diferença 
        entre a sua porcentagem acumulada e a porcentagem acumulada do elemento anterior. 
        Essa diferença é então incluída na lista alturas. Portanto, o elemento i da 
        lista alturas corresponde à altura da barra i do gráfico de funil.

        Em resumo, a linha de código cria uma lista alturas com as alturas de todas as 
        barras do gráfico de funil, onde a altura de cada barra é proporcional à diferença 
        entre as porcentagens acumuladas dos elementos da coluna col_y.
        """
        alturas = [perc_acumuladas[0]] + [perc_acumuladas.iloc[i] - perc_acumuladas[i-1] for i in range(1, len(perc_acumuladas))]
        
        #lista de cores hexadecimal para a barra do funil
        """
        criando uma lista chamada cores com 9 elementos, onde cada elemento é uma 
        string representando uma cor em formato hexadecimal.

        Essas cores podem ser utilizadas para colorir as barras do gráfico de funil, 
        criado posteriormente. As cores escolhidas são:

            "#3366cc": um tom de azul claro;
            "#dc3912": um tom de vermelho escuro;
            "#ff9900": um tom de laranja;
            "#109618": um tom de verde;
            "#990099": um tom de roxo escuro;
            "#0099c6": um tom de azul turquesa;
            "#dd4477": um tom de rosa;
            "#66aa00": um tom de verde claro;
            "#b82e2e": um tom de vermelho.

        Cada cor pode ser referenciada posteriormente pelo seu índice na lista cores.
        """
        cores = ["#3366cc", "#dc3912", "#ff9900", "#109618", "#990099", "#0099c6", "#dd4477", "#66aa00", "#b82e2e"]

        """
        gera uma sequência de cores a serem usadas para colorir as barras do 
        gráfico de funil.

        A função get_cmap da biblioteca matplotlib retorna um mapa de cores, que é uma 
        função que transforma valores numéricos em cores. 
        
        O argumento 'tab10' especifica qual mapa de cores será utilizado 
        (no caso, a paleta de cores "tab10" com 10 cores). 
        
        O segundo argumento len(df_agrupado) define o número de cores a serem geradas, 
        que é igual ao número de barras no gráfico.

        Em seguida, a função arange da biblioteca numpy cria uma sequência de números 
        inteiros que varia de 0 a len(df_agrupado) - 1. Essa sequência de números é 
        passada como argumento para a função retornada pelo get_cmap, que retorna uma 
        lista de cores correspondente à sequência de números. Essa lista de cores é 
        armazenada na variável cores e é utilizada na criação das barras do gráfico.
        """
        cores = plt.get_cmap('tab10', len(df_agrupado))(np.arange(len(df_agrupado)))
        
        nome = []
        
        #Cria as barras do funil com os respectivos rótulos
        """
        Essa linha é um loop for que itera sobre o objeto df_agrupado retornado 
        pelo método groupby do pandas.

        O enumerate é uma função que retorna uma tupla contendo um contador e o 
        valor do elemento atual da sequência em cada iteração. Neste caso, ele é 
        usado para gerar uma sequência de índices i e seus respectivos valores indice 
        e valor da coluna col_x (os itens textuais) e col_y (os valores numéricos agregados) 
        do DataFrame df_agrupado.

        Assim, a cada iteração, o loop atualiza as variáveis i, indice e valor com o 
        índice, rótulo e valor do próximo item de df_agrupado.

        """
        #iteritems() obsoleto use items() instead
        for i, (indice, valor) in enumerate(df_agrupado.items()):
            
            """
            Essa linha está dentro do loop que itera sobre cada barra do gráfico de 
            funil e calcula a posição horizontal da barra.

            A variável "esquerda" é a posição horizontal esquerda da barra, ou seja, 
            a distância da borda esquerda do gráfico até a borda esquerda da barra. 
            Essa distância é calculada como metade da diferença entre a altura máxima 
            do gráfico (100, já que é um gráfico de porcentagens) e a altura da barra 
            atual (alturas[i]), o que garante que a barra esteja centralizada verticalmente 
            no gráfico.

            O valor 100 representa a altura máxima do gráfico, já que o funil começa com 
            100% na base e diminui à medida que os dados são filtrados. A fórmula
            (100 - alturas[i]) / 2 calcula a distância da borda esquerda da barra até 
            a borda esquerda do gráfico, deixando a barra centralizada verticalmente. 
            O resultado é armazenado na variável "esquerda".
            """
            esquerda = (100 - alturas[i]) / 2
            
            """
            Essa linha cria uma barra horizontal no objeto do tipo Axes da biblioteca 
            matplotlib (armazenado em self.ax) em um gráfico de funil. A barra é 
            posicionada na posição vertical i, tem altura alturas[i], começa na posição 
            horizontal esquerda, tem cor cores[i] e tem transparência alpha=0.7. 
            Além disso, suas bordas são destacadas com a cor branca (edgecolor="white").

            i é a posição atual na lista de alturas, e alturas[i] é a altura correspondente 
            à barra que está sendo criada. O parâmetro left especifica a posição horizontal 
            da borda esquerda da barra. A variável esquerda é calculada como a diferença 
            entre 100 e a altura da barra, dividida por 2. Isso garante que a barra 
            esteja centralizada em relação à largura do gráfico de funil.

            O parâmetro color define a cor da barra. Nesse caso, a cor é obtida da 
            lista cores na posição i, que contém uma lista de cores em código hexadecimal, 
            criada anteriormente. O parâmetro alpha define a transparência da barra, 
            variando de 0 a 1. Neste caso, o valor é 0,7, o que significa que a barra 
            é parcialmente transparente. O parâmetro edgecolor define a cor da borda da barra. 
            Neste caso, a borda é branca.
            """
            self.ax.barh(i, alturas[i], left=esquerda, 
                         color=cores[i],
                         alpha=0.7,
                         edgecolor="white")
            label = f"{indice}: {int(valor):,d}"
            largura_barra = alturas[i]
            centraliza_barra = esquerda + largura_barra / 2
            
            """
            adiciona o texto das etiquetas das barras do gráfico de funil.

            centraliza_barra é a posição horizontal onde o texto deve ser centralizado. 
            Como as barras são deslocadas para a direita para que o funil pareça mais 
            atraente, a posição horizontal central é calculada subtraindo a largura da 
            barra do ponto médio da base da barra.

            i é a posição vertical onde o texto deve ser colocado, que corresponde à posição 
            da barra no gráfico.

            label é a etiqueta associada a essa barra, que será exibida como texto. Ela é 
            obtida a partir da série df_agrupado, que contém os valores que são exibidos no 
            gráfico de funil.

            color é a cor do texto.

            fontsize é o tamanho da fonte do texto.

            ha é o alinhamento horizontal do texto. Nesse caso, é definido como 'center', 
            para que o texto seja centralizado na posição horizontal.

            va é o alinhamento vertical do texto. Nesse caso, é definido como 'center', 
            para que o texto seja centralizado na posição vertical.
            """
            self.ax.text(centraliza_barra,
                        i,
                        label,
                        color="black",
                        fontsize=10,
                        ha='center',
                        va='center')
            
        #Ordena o eixo x
        df_agrupado = df_agrupado.sort_index()
            
        #Remove os eixos do gráfico x e y
        fig, ax = plt.subplots()
        ax.set_axis_off()
        self.ax.axis("off")
        
        #--------------------------------
        
        self.canvas.draw() #Atualizo a visualização do canvas
        
        #Pego o número da imagem salvar o gráfico
        nome_imagem = self.cb_imagem.get()
        caminho_nome_imagem = f"{nome_imagem}.png"
        
        #getcwd - Retorno o diretório pasta atual do arquivo
        #path.join - Junta o diretorio com o nome da imagem
        caminho_imagem = os.path.join(os.getcwd(), caminho_nome_imagem)
        
        """
        Essa linha de código salva o gráfico atualmente criado na figura associada 
        ao objeto ax em um arquivo de imagem especificado por caminho_imagem. A imagem é 
        salva em um formato definido pela extensão do arquivo nome_imagem e com uma resolução 
        de 80 pontos por polegada (dpi).

        O método savefig() é fornecido pela biblioteca matplotlib e é usado para salvar a 
        figura atual em um arquivo. O parâmetro caminho_imagem especifica o caminho completo e 
        o nome do arquivo a ser salvo. O parâmetro dpi especifica a resolução da imagem em 
        pontos por polegada (dots per inch).
        """
        self.ax.figure.savefig(caminho_imagem, dpi=80)
        
        #Fecha a janela
        self.janela_funil.destroy()
        
    def abrir_janela_editar_dados(self):
        
        self.editar_dados = Toplevel(self.master)
        self.editar_dados.title("Editar Dados")
        
        #Criando o menu editar
        menu_editar = Menu(self.editar_dados, tearoff=0)
        self.editar_dados.config(menu=menu_editar)
        
        #Criando o menu Salvar
        menu_salvar = Menu(self.editar_dados, tearoff=0)
        menu_editar.add_cascade(label="Formatar", menu=menu_salvar)
        
        menu_salvar.add_command(label="Renomear Coluna", command=self.renomear_coluna)
        menu_salvar.add_command(label="Remover Coluna", command=self.remover_coluna)
        menu_salvar.add_command(label="Remover Linhas em Branco", command=self.editar_dados.destroy)
        menu_salvar.add_command(label="Remover linhas alternadas", command=self.remove_algumas_linhas)
        menu_salvar.add_command(label="Remover duplicados", command=self.editar_dados.destroy)
        
        titulo = Label(self.editar_dados,
                      text="Edite seus dados : {}".format(",".join(self.df.columns)))
        titulo.grid(row=1, column=0, columnspan=2)
        
        #Cria a treeview com os cabeçalhos das colunas
        self.tree = ttk.Treeview(self.editar_dados,
                                columns=list(self.df.columns), show="headings")
        
        #for - para        
        for col in self.df.columns:
            
            self.tree.heading(col, text=col)
            
        #Insere os dados do dataframe / tabela na treeview
        for i, row in self.df.iterrows():
            
            self.tree.insert("", "end", values=list(row))
            
        #Adiciona a treeview na janela
        self.tree.grid(row=2, column=0, columnspan=2)
        
        
        #Cria a janela em segundo plano
        self.editar_dados.mainloop()
        
    def renomear_coluna(self):
        
        janela_renomear_coluna = Toplevel(self.editar_dados)
        janela_renomear_coluna.title("Renomear Coluna")
        
        #Define a largura e altura da janela
        largura_janela = 400
        altura_janela = 250
        
        #Obtem a largura e altura da tela do computador
        largura_tela = janela_renomear_coluna.winfo_screenwidth()
        altura_tela = janela_renomear_coluna.winfo_screenheight()
        
        #Calcula a posição da janela para centralizar
        pos_x = (largura_tela // 2) - (largura_janela // 2)
        pos_y = (altura_tela // 2) - (altura_janela // 2)
        
        #Definindo a posição da janela
        janela_renomear_coluna.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
        
        #Define a cor de fundo da janela
        janela_renomear_coluna.configure(bg="#FFFFFF")
        
        #Informação para o usuário
        label_coluna = Label(janela_renomear_coluna, 
                            text="Selecione a coluna para renomear:",
                            bg="#FFFFFF")
        label_coluna.pack(pady=10)
        
        #Campo de entrada de dados para digitarmos
        entry_coluna = Entry(janela_renomear_coluna,
                            width=30,
                            font=("Arial 12"))
        entry_coluna.pack(pady=10)
        
        #Informação para o usuário
        label_novo_nome = Label(janela_renomear_coluna, 
                            text="Digite o novo nome:",
                            bg="#FFFFFF")
        label_novo_nome.pack(pady=10)
        
        #Campo de entrada de dados para digitarmos
        entry_novo_nome = Entry(janela_renomear_coluna,
                            width=30,
                            font=("Arial 12"))
        entry_novo_nome.pack(pady=10)
        
        botao_renomear = Button(janela_renomear_coluna,
                               text="Renomear",
                               font=("Arial 12"),
                               command=lambda: self.renomear_coluna_funcao(entry_coluna.get(),
                                                                          entry_novo_nome.get(),
                                                                          janela_renomear_coluna))
        botao_renomear.pack(pady=20)
        
        
    def renomear_coluna_funcao(self, coluna, nome_nome, janela_renomear_coluna):
    
        #Renomeia o nome da coluna
        self.df = self.df.rename(columns={coluna: nome_nome})
        
        #Atualizar a treeview para refletir as alterações na tela
        self.atualiza_treeview()
        
        #Fecha a janela secundária
        janela_renomear_coluna.destroy()
        
    def atualiza_treeview(self):
        
        #Apagar todos os dados da treeview
        self.tree.delete(*self.tree.get_children())
        
        #Define as colunas da treeview com base nas colunas do df
        self.tree["columns"] = list(self.df.columns)
        
        for coluna in self.df.columns:
            
            #Difine o texto do cabeçalho de cada coluna
            self.tree.heading(coluna, text=coluna)
            
        for i, row in self.df.iterrows():
            
            #Converte a linha do df em uma lista e adiciona na variavel
            values = list(row)
            
            #Converter valores do tipo numpy para python
            for j, value in enumerate(values):
                
                if isinstance(value, np.generic):
                    
                    values[j] = np.asscalar(value)
            
            #Adiona valores na treeview
            self.tree.insert("", END, values=values)
            
    def remover_coluna(self):
        
        janela_remover_coluna = Toplevel(self.editar_dados)
        janela_remover_coluna.title("Remover Coluna")
        
        #Define a largura e altura da janela
        largura_janela = 400
        altura_janela = 250
        
        #Obtem a largura e altura da tela do computador
        largura_tela = janela_remover_coluna.winfo_screenwidth()
        altura_tela = janela_remover_coluna.winfo_screenheight()
        
        #Calcula a posição da janela para centralizar
        pos_x = (largura_tela // 2) - (largura_janela // 2)
        pos_y = (altura_tela // 2) - (altura_janela // 2)
        
        #Definindo a posição da janela
        janela_remover_coluna.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")
        
        #Define a cor de fundo da janela
        janela_remover_coluna.configure(bg="#FFFFFF")
        
        #Informação para o usuário
        label_coluna = Label(janela_remover_coluna, 
                            text="Digite o nome da coluna que quer remover:",
                            bg="#FFFFFF")
        label_coluna.pack(pady=10)
        
        #Campo de entrada de dados para digitarmos
        entry_coluna = Entry(janela_remover_coluna,
                            width=30,
                            font=("Arial 12"))
        entry_coluna.pack(pady=10)
        
        
        
        botao_remover = Button(janela_remover_coluna,
                               text="Remover",
                               font=("Arial 12"),
                               command=lambda: self.remover_coluna_funcao(entry_coluna.get(),
                                                                          janela_remover_coluna))
        botao_remover.pack(pady=20)
        
        
    def remover_coluna_funcao(self, coluna, janela_remover_coluna):
    
        if coluna:
            
            #Remove a coluna do Dataframe
            self.df = self.df.drop(columns=coluna)
            
        #Atualizar a treeview para refletir as alterações na tela
        self.atualiza_treeview()
        
        #Fecha a janela secundária
        janela_remover_coluna.destroy()
        
    
    def remove_algumas_linhas(self, linha_inicio=None, linha_fim=None):
        
            
            linha_inicio = int(simpledialog.askstring("Remover linhas",
                                                     "Digite o número da primeira linha a ser removida"))
        
            linha_fim = int(simpledialog.askstring("Remover linhas",
                                                     "Digite o número da última linha a ser removida"))
            
            #Mensagem de pergunta sim e não
            resposta = messagebox.askyesno("Remover linhas",
                                          f"Tem certeza que deseja deletar as linhas {linha_inicio} até {linha_fim}")
            
            if resposta:
                
                #Remove o intervalo de linhas especificado
                self.df = self.df.drop(self.df.index[linha_inicio-1:linha_fim])
                
            #Atualizar a treeview para refletir as alterações na tela
            self.atualiza_treeview()
        
#Cria uma instancia da classe tk para criar a janela principal
tela = Tk()

#Cria a instancia da classe Application com a janela principal como master
app = Application(master=tela)

#Define a posição da tela
#row - linha
#column - coluna
#padx - espaço nas laterais
#pady - espaço em cima e em baixo
app.grid(row=0, column=0, padx=10, pady=10)

#Inicia o loop
tela.mainloop()