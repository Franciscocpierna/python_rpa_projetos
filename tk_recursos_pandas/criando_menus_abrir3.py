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
        
        menu_de_arquivos.add_command(label="Abrir", command=self.carregar_excel)
        menu_de_arquivos.add_separator()
        menu_de_arquivos.add_command(label="Salvar Como", command=janela.destroy)
        menu_de_arquivos.add_separator()
        menu_de_arquivos.add_command(label="Sair", command=janela.destroy)
        
        #Adiciona o menu Arquivo a barra de menus
        menu_bar.add_cascade(label="Arquivo", menu=menu_de_arquivos)
        
        #------------------------------------------------
        
        # Cria o menu "Editar"
        #O tearoff=0 é uma configuração de menu que, quando definida como 0, desativa a função de arrastar
        menu_edicao = tk.Menu(menu_bar, tearoff=0)
        
        menu_edicao.add_command(label="Renomear Coluna", command=janela.destroy)
        menu_edicao.add_command(label="Remover Coluna", command=janela.destroy)
        menu_edicao.add_command(label="Filtrar", command=janela.destroy)
        menu_edicao.add_command(label="Pivot", command=janela.destroy)
        menu_edicao.add_command(label="Group", command=janela.destroy)
        menu_edicao.add_command(label="Remover linhas em branco", command=janela.destroy)
        menu_edicao.add_command(label="Remover linhas alternadas", command=janela.destroy)
        menu_edicao.add_command(label="Remover Duplicados", command=janela.destroy)
        
        #Adiciona o menu Arquivo a barra de menus
        menu_bar.add_cascade(label="Editar", menu=menu_edicao)
        
        #------------------------------------------------
        
        # Cria o menu "Merge"
        #O tearoff=0 é uma configuração de menu que, quando definida como 0, desativa a função de arrastar
        merge_menu = tk.Menu(menu_bar, tearoff=0)
        
        merge_menu.add_command(label="Inner Join", command=janela.destroy)
        merge_menu.add_command(label="Join Full", command=janela.destroy)
        merge_menu.add_command(label="Left Join", command=janela.destroy)
        merge_menu.add_command(label="Merge Outer", command=janela.destroy)
        
        #Adiciona o menu Arquivo a barra de menus
        menu_bar.add_cascade(label="Merge", menu=merge_menu)
        
        #------------------------------------------------
        
        # Cria o menu "Reletórios"
        #O tearoff=0 é uma configuração de menu que, quando definida como 0, desativa a função de arrastar
        relatorio_menu = tk.Menu(menu_bar, tearoff=0)
        
        relatorio_menu.add_command(label="Consolidar", command=janela.destroy)
        relatorio_menu.add_command(label="Quebra", command=janela.destroy)
        
        #Adiciona o menu Arquivo a barra de menus
        menu_bar.add_cascade(label="Relatório", menu=relatorio_menu)        
        
        
        # Define a barra de menu como uma barra de menu da janela principal 
        self.janela_principal.config(menu=menu_bar)
        
        #Criando a Treeview
        self.tree = tk.ttk.Treeview(self.janela_principal)
        
        # Coloca o widget de árvore na janela principal
        self.tree.pack(expand=False)
        
        
    def carregar_excel(self):
        
        # Define os tipos de arquivos que podem ser abertos
        tipo_de_arquivo = (("Excel files", "*.xlsx;*.xls"), ("All files", "*.*"))
        
        # Abre a janela para selecionar o arquivo e armazena o caminho na variável "tipo_de_arquivo"
        self.nome_do_arquivo = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=tipo_de_arquivo)
        
        try:
            
            # Lê o arquivo excel com a biblioteca Pandas e armazena o conteúdo na variável "df"
            self.df = pd.read_excel(self.nome_do_arquivo)
            
            # Atualiza a árvore (treeview) com o conteúdo do arquivo
            self.atualiza_treeview()
            
        except Exception as e:
            
            # Exibe mensagem de erro caso não seja possível abrir o arquivo
            messagebox.showerror("Erro", f"Não foi possível abrir o arquivo: {e}")
    
    def atualiza_treeview(self):
        
        print("Carregando dados")

editor = ExcelEditor(janela)


janela.mainloop()