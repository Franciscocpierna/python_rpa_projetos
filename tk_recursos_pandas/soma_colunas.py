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
        
        menu_edicao.add_command(label="Renomear Coluna", command=self.renomear_coluna)
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
       
    def soma_colunas_com_valor(self):
        
        resultados = []
        
        #for - para
        for coluna in self.df.columns:
            
            #if - se
            # Verifica se a coluna contém apenas números
            #A função "pd.api.types.is_numeric_dtype()" é uma função do pandas que retorna True 
            #se a coluna contém valores numéricos e False caso contrário.
            if pd.api.types.is_numeric_dtype(self.df[coluna]):
            
                #Seleciona apenas as linhas a partir da segunda linha da coluna
                #Exclui primeiro elemento da coluna. O motivo de excluir o primeiro elemento (índice [0])
                #é que muitas vezes a primeira linha de uma coluna de dados é usada para nomear a coluna
                #ou fornecer algum tipo de informação de cabeçalho que não é relevante para a análise dos dados.
                valores_numericos = self.df[coluna][1:]
                
                # Tenta converter os valores para numéricos
                # o argumento "errors='coerce'" permite que a função "pd.to_numeric()" 
                #lide com valores não numéricos na coluna e continue a converter os valores 
                #numéricos restantes, transformando os valores não numéricos em NaN.
                valores_numericos = pd.to_numeric(valores_numericos, errors='coerce')
                
                # Filtra os valores que são numéricos
                #a expressão "np.isnan(valores_numericos)" é usada para verificar quais valores da coluna "valores_numericos" são NaN (not a number). 
                #A função "np.isnan()" é da biblioteca NumPy e retorna "True" se o valor passado como argumento for NaN e "False"
                #caso contrário.

                #O símbolo "~" é usado para inverter os resultados retornados pela função "np.isnan()". 
                #Ou seja, "~np.isnan(valores_numericos)" retornará um array booleano com valores "True" 
                #para todos os elementos que não são NaN e "False" para todos os elementos que são NaN.
                valores_numericos = valores_numericos[~np.isnan(valores_numericos)]
                
                #Soma os valores números
                soma = valores_numericos.sum()
                
                resultado = f"A soma da coluna {coluna} é {soma}"
                
                #append - é um método usado para adicionar um elemento ao final de uma lista.
                resultados.append(resultado)
             
        # Configura o widget resultado_label com todos os resultados concatenados
        # "join" é um método usado para concatenar os elementos de uma lista em uma única string, separando cada elemento com um separador especificado.
        self.resultado_label.config(text="\n".join(resultados))
        
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
         
        #Calcula a soma das colunas com valores
        self.soma_colunas_com_valor()
    
    def atualiza_treeview(self):
        
        #Apaga todo o conteúdo da treeview
        self.tree.delete(*self.tree.get_children())
        
        #Define as colunas da treeview com base nas colunas do df (Dataframe)
        self.tree["columns"] = list(self.df.columns)
        
        #for - para
        for column in self.df.columns:
            
            #Define o texto do cabeçalho de cada coluna
            self.tree.heading(column, text=column)
            
        #O método iterrows é usado para percorrer cada linha do DataFrame, contém todas as colunas da linha atual
        for i, row in self.df.iterrows():
            
            # Converte a linha do dataframe em uma lista e adiciona à treeview
            values = list(row)
            
            # Converte valores de tipo numpy para python nativo
            #"enumerate()" permite que se tenha acesso tanto ao índice quanto ao valor correspondente
            #de cada elemento da lista em uma única instrução de loop "for". Isso pode ser útil em várias situações em que é necessário manter
            #o controle sobre a posição de um elemento em uma lista enquanto se itera sobre ela.
            for j, value in enumerate(values):
                
                """
                verificando se o tipo do objeto "value" é do tipo "np.generic", que é um tipo 
                de dados específico do NumPy que é retornado quando um array do NumPy é indexado
                ou fatiado. O objeto "value" pode ter esse tipo se a lista "values" contiver 
                valores que foram convertidos para o tipo "np.generic" em algum momento.

                Se o tipo do objeto "value" for "np.generic", o código usa a função 
                "np.asscalar()" para converter o valor para um tipo nativo Python. 
                Essa função é usada para converter um valor do tipo NumPy para um tipo 
                nativo do Python (por exemplo, de um tipo de número do NumPy para um tipo 
                de número do Python). A função "np.asscalar()" é usada para garantir que 
                os valores da lista "values" sejam todos do tipo nativo Python e, portanto, 
                possam ser usados com segurança em outras partes do código.

                O resultado da conversão é atribuído novamente à mesma posição da lista "values"
                usando a variável "j". Isso garante que a lista "values" seja atualizada com os 
                valores corrigidos antes de serem usados em outras partes do código.
                """
                if isinstance(value, np.generic):
                    
                    values[j] = np.asscalar(value)
                    
            self.tree.insert("", tk.END, values=values)
         
    #É a função para abrir a janela secundária para renomear uma coluna
    def renomear_coluna(self):
        
        #Cria uma tela em segundo plano em cima da tela principal
        janela_renomear_coluna = tk.Toplevel(self.janela_principal)
        janela_renomear_coluna.title("Renomear Coluna")
        
        largura_janela = 400
        altura_janela = 250
        
        #Define a cor de fundo da janela
        janela_renomear_coluna.configure(bg="#FFFFFF")
        
        label_coluna = tk.Label(janela_renomear_coluna, text="Digite o nome da coluna que quer renomear:", font=("Arial", 12), bg="#FFFFFF")
        label_coluna.pack(pady=10)
        entry_coluna = tk.Entry(janela_renomear_coluna, font=("Arial", 12))
        entry_coluna.pack()
        
        label_novo_nome = tk.Label(janela_renomear_coluna, text="Digite o novo nome:", font=("Arial", 12), bg="#FFFFFF")
        label_novo_nome.pack(pady=10)
        entry_novo_nome = tk.Entry(janela_renomear_coluna, font=("Arial", 12))
        entry_novo_nome.pack()
        
        #Cria o botão para renomear a coluna
        botao_renomear = tk.Button(janela_renomear_coluna, text="Renomear", font=("Arial", 12), command=lambda: self.funcao_renomear_coluna(entry_coluna.get(), entry_novo_nome.get(), janela_renomear_coluna))
        botao_renomear.pack(pady=20)
        
        #Cria / exie na tela
        janela_renomear_coluna.mainloop()
        
    def funcao_renomear_coluna(self, coluna, novo_nome, janela_renomear_coluna):
        
        if novo_nome:
            
            #Renomeia a coluna com o novo nome
            self.df = self.df.rename(columns={coluna: novo_nome})
            
            #Atualiza a Treeview
            self.atualiza_treeview()
            
            #Fecha a janela secundária
            janela_renomear_coluna.destroy()

editor = ExcelEditor(janela)


janela.mainloop()