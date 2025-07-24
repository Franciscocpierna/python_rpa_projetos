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
        #self.create_widgets()
        
        # Define a largura da coluna que contém o widget do gráfico como "1"
        self.master.columnconfigure(1, weight=1)
    
    


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