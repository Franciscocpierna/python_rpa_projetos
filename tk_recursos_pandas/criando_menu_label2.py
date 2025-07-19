#Importando a biblioteca para tratalhar com a Interface Gráfica
import tkinter as tk
from tkinter import *

#Importanda classes do Tkinter
from tkinter import filedialog, messagebox, simpledialog

#Importa a classe pandas como pd e a numpy como np
import pandas as pd
import numpy as np

#importando a classe Table
from pandastable import Table

# Cria uma janela principal com o título "Editor de Excel", 
#cria um objeto da classe "ExcelEditor" passando a janela como parâmetro, 
#e inicia o loop principal do tkinter
janela = Tk()
janela.title("Editor de Excel com Pandas")
janela.attributes("-fullscreen", True)

class ExcelEditor:
    
    #__init__ é um método especial chamado construtor, 
    #que é usado para inicializar um novo objeto. 
    #Definindo um construtor para uma classe chamada self, com um parâmetro janela_principal. 
    #Esse janela_principal pode ser qualquer objeto que será passado como argumento
    #janela_principal - Master
    def __init__(self, janela_principal):
    
        #Inicializa a classe com uma instancia da janela principal
        self.janela_principal = janela_principal
        
        #self é uma palavra-chave especial em Python que utilizada para acessar um objeto dentro de sua própria definição.
        self.resultado_label = Label(self.janela_principal, text="Total: ", font="Arial 16", bg="#F5F5F5")
        self.resultado_label.pack(side=TOP, padx=10, pady=10)
        
        #Cria um dataframe vazio
        self.df = pd.DataFrame()
        
        #Incializa as variaveis
        self.tree = None
        self.table = None
        self.filename = ""
        
        #Criando os widgets
        self.cria_widgets()
        
    #Widgets são widgets de interface de usuário em Python. 
    #Eles são usados para construir interface
    def cria_widgets(self):
    
        #Cria a janela de menu
        menu_bar = tk.Menu(self.janela_principal)
        
        # Cria o menu "Arquivo"
        #O tearoff=0 é uma configuração de menu que, quando definida como 0, desativa a função de arrastar
        menu_de_arquivos = tk.Menu(menu_bar, tearoff=0)
        
        menu_de_arquivos.add_command(label="Abrir", command=janela.destroy)
        menu_de_arquivos.add_separator()
        menu_de_arquivos.add_command(label="Salvar Como", command=janela.destroy)
        menu_de_arquivos.add_separator()
        menu_de_arquivos.add_command(label="Sair", command=janela.destroy)
        
        #Adiciona o menu Arquivo a barra de menus
        menu_bar.add_cascade(label="Arquivo", menu=menu_de_arquivos)
        
        # Define a barra de menu como uma barra de menu da janela principal 
        self.janela_principal.config(menu=menu_bar)
    

editor = ExcelEditor(janela)


janela.mainloop()