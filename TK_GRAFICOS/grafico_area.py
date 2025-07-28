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

        self.btn_editar_dados = Button(self.frame_relatorios, text="Editar Dados", font="Arial 16")
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
        self.btn_funil = Button(self.frame_botoes, text="Gráfico de Funil", font="Arial 16")
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
                                               command = self.gerar_grafico_linhas_2)
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