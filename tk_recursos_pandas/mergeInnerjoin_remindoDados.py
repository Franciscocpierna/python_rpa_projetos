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
        menu_edicao.add_command(label="Remover Coluna", command=self.remover_coluna)
        menu_edicao.add_command(label="Filtrar", command=self.filtrar)
        menu_edicao.add_command(label="Pivot", command=janela.destroy)
        menu_edicao.add_command(label="Group", command=self.group)
        menu_edicao.add_command(label="Remover linhas em branco", command=self.remover_linhas_em_branco)
        menu_edicao.add_command(label="Remover linhas alternadas", command=self.remove_algumas_linhas)
        menu_edicao.add_command(label="Remover Duplicados", command=self.remover_duplicados)
        
        #Adiciona o menu Arquivo a barra de menus
        menu_bar.add_cascade(label="Editar", menu=menu_edicao)
        
        #------------------------------------------------
        
        # Cria o menu "Merge"
        #O tearoff=0 é uma configuração de menu que, quando definida como 0, desativa a função de arrastar
        merge_menu = tk.Menu(menu_bar, tearoff=0)
        
        merge_menu.add_command(label="Inner Join", command=self.merge_inner_join)
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
                valores_numericos = self.df[coluna][0:]
                
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
        
        #Define a largura e altura da janela
        largura_janela = 400
        altura_janela = 250
        
        #Obtem a largura e da tela do computador
        largura_tela = janela_renomear_coluna.winfo_screenwidth()
        altura_tela = janela_renomear_coluna.winfo_screenheight()
        
        #Calcula a posição da janela para centraliza-la na tela
        """
        Essas linhas calculam a posição em que a janela deve ser
        exibida na tela do computador de forma centralizada. 
        A posição x é definida pela diferença entre a largura da tela
        e a largura da janela, dividida por 2. Já a posição y é definida
        pela diferença entre a altura da tela e a altura da janela, também
        dividida por 2. O operador "//" é utilizado para realizar a divisão
        inteira, ou seja, retornar apenas o resultado inteiro da divisão.
        """
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        #Define a posição da janela
        """
        define a geometria da janela principal, especificando a 
        largura e altura da janela, bem como a posição onde a janela 
        será exibida na tela, usando as variáveis previamente definidas 
        para a posição x e y da janela. O formato utilizado é uma string 
        que contém os valores de largura, altura, posição x e posição y da 
        janela separados por "x" e "+" e passados como argumentos para o 
        método geometry() da janela principal.

        O formato '{}'x'{}'+'{}'+'{}' é uma string de formatação que espera
        quatro valores, que correspondem à largura da janela, altura da janela, 
        posição x da janela e posição y da janela, respectivamente.

        Esses valores são passados na ordem especificada para a string de formatação e, 
        em seguida, são utilizados para definir a geometria da janela através do 
        método geometry do objeto janela_principal.
        """

        janela_renomear_coluna.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
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
            
    def remover_linhas_em_branco(self):
        
        #Solicita ao usuário se ele quer mesmo remover as linhas em branco
        reposta = messagebox.askyesno("Remover linhas em branco", "Tem certeza que deseja remover as linhas em branco?")
        
        #if - se
        #Verifica se a resposta é "sim"
        if reposta == 1:
            
            #Deleta as linhas com valores em branco
            self.df = self.df.dropna(axis=0)
            
            # Atualiza a árvore (treeview) com o conteúdo do arquivo
            self.atualiza_treeview()
            
            #Calcula a soma das colunas com valores
            self.soma_colunas_com_valor()
            
    #É a função para abrir a janela secundária para renomear uma coluna
    def remove_algumas_linhas(self):
        
        #Cria uma tela em segundo plano em cima da tela principal
        janela_remove_algumas_linhas = tk.Toplevel(self.janela_principal)
        janela_remove_algumas_linhas.title("Remover Algumas Linhas")
        
        #Define a largura e altura da janela
        largura_janela = 400
        altura_janela = 250
        
        #Obtem a largura e da tela do computador
        largura_tela = janela_remove_algumas_linhas.winfo_screenwidth()
        altura_tela = janela_remove_algumas_linhas.winfo_screenheight()
        
        #Calcula a posição da janela para centraliza-la na tela
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        #Define a posição da janela
        janela_remove_algumas_linhas.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        #Define a cor de fundo da janela
        janela_remove_algumas_linhas.configure(bg="#FFFFFF")
        
        label_linha_inicio = tk.Label(janela_remove_algumas_linhas, 
                                text="Digite o número da primeira linha a ser removida:", 
                                font=("Arial", 12), bg="#FFFFFF")
        label_linha_inicio.pack(pady=10)
        entry_linha_inicio = tk.Entry(janela_remove_algumas_linhas, 
                                      font=("Arial", 12))
        entry_linha_inicio.pack()
        
        label_linha_fim = tk.Label(janela_remove_algumas_linhas, 
                                   text="Digite o número da última linha a ser removida:", 
                                   font=("Arial", 12), bg="#FFFFFF")
        label_linha_fim.pack(pady=10)
        entry_linha_fim = tk.Entry(janela_remove_algumas_linhas, font=("Arial", 12))
        entry_linha_fim.pack()
        
        #Cria o botão para renomear a coluna
        botao_remover = tk.Button(janela_remove_algumas_linhas, 
                                  text="Remover", font=("Arial", 12), 
                                  command=lambda: self.funcao_remove_algumas_linhas(entry_linha_inicio.get(), 
                                                                              entry_linha_fim.get(), 
                                                                              janela_remove_algumas_linhas))
        botao_remover.pack(pady=20)
        
        #Cria / exie na tela
        janela_remove_algumas_linhas.mainloop()
        
    
    def funcao_remove_algumas_linhas(self, linha_inicio, linha_fim, janela_remove_algumas_linhas):
        
        #Convertendo de str - texto e int - inteiro
        primeira_linha = int(linha_inicio)
        ultima_linha = int(linha_fim)
        
        #if - se
        #Deleta as linhas em um intervalo
        self.df = self.df.drop(self.df.index[primeira_linha-1:ultima_linha])
            
        # Atualiza a árvore (treeview) com o conteúdo do arquivo
        self.atualiza_treeview()
            
        #Calcula a soma das colunas com valores
        self.soma_colunas_com_valor()
        
        #Fecha a janela secundária
        janela_remove_algumas_linhas.destroy()
        
    def remover_duplicados(self):
        
        #Cria uma tela em segundo plano em cima da tela principal
        janela_remover_duplicados = tk.Toplevel(self.janela_principal)
        janela_remover_duplicados.title("Remover Duplicados")
        
        #Define a largura e altura da janela
        largura_janela = 600
        altura_janela = 150
        
        #Obtem a largura e da tela do computador
        largura_tela = janela_remover_duplicados.winfo_screenwidth()
        altura_tela = janela_remover_duplicados.winfo_screenheight()
        
        #Calcula a posição da janela para centraliza-la na tela
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        #Define a posição da janela
        janela_remover_duplicados.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        #Define a cor de fundo da janela
        janela_remover_duplicados.configure(bg="#FFFFFF")
        
        label_coluna = tk.Label(janela_remover_duplicados, 
                                text="Digite o nome da coluna que quer remover os itens duplicados:", 
                                font=("Arial", 12), bg="#FFFFFF")
        label_coluna.pack(pady=10)
        entry_coluna = tk.Entry(janela_remover_duplicados, 
                                      font=("Arial", 12))
        entry_coluna.pack()
        
        
        
        #Cria o botão para renomear a coluna
        botao_remover = tk.Button(janela_remover_duplicados, 
                                  text="Remover", font=("Arial", 12), 
                                  command=lambda: self.funcao_remover_duplicados(entry_coluna.get(), 
                                                                              janela_remover_duplicados))
        botao_remover.pack(pady=20)
        
        #Cria / exie na tela
        janela_remover_duplicados.mainloop()
        
    
    def funcao_remover_duplicados(self, coluna, janela_remover_duplicados):
        
        
        #Verifica se o usuário digitou uma coluna
        if coluna:
            
            #Remove os itens duplicados na soluna, mantendo apenas a primeira ocorrencia
            #first - primeira ocorrencia
            #last - ultima
            self.df = self.df.drop_duplicates(subset=coluna, keep="first")
            
            
        # Atualiza a árvore (treeview) com o conteúdo do arquivo
        self.atualiza_treeview()
            
        #Calcula a soma das colunas com valores
        self.soma_colunas_com_valor()
        
        #Fecha a janela secundária
        janela_remover_duplicados.destroy()
        
    def remover_coluna(self):
        
        #Cria uma tela em segundo plano em cima da tela principal
        janela_remover_coluna = tk.Toplevel(self.janela_principal)
        janela_remover_coluna.title("Remover Coluna")
        
        #Define a largura e altura da janela
        largura_janela = 600
        altura_janela = 150
        
        #Obtem a largura e da tela do computador
        largura_tela = janela_remover_coluna.winfo_screenwidth()
        altura_tela = janela_remover_coluna.winfo_screenheight()
        
        #Calcula a posição da janela para centraliza-la na tela
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        #Define a posição da janela
        janela_remover_coluna.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        #Define a cor de fundo da janela
        janela_remover_coluna.configure(bg="#FFFFFF")
        
        label_coluna = tk.Label(janela_remover_coluna, 
                                text="Digite o nome da coluna que quer remover:", 
                                font=("Arial", 12), bg="#FFFFFF")
        label_coluna.pack(pady=10)
        entry_coluna = tk.Entry(janela_remover_coluna, 
                                      font=("Arial", 12))
        entry_coluna.pack()
        
        
        
        #Cria o botão para remover a coluna
        botao_remover = tk.Button(janela_remover_coluna, 
                                  text="Remover", font=("Arial", 12), 
                                  command=lambda: self.funcao_remover_coluna(entry_coluna.get(), 
                                                                              janela_remover_coluna))
        botao_remover.pack(pady=20)
        
        #Cria / exie na tela
        janela_remover_coluna.mainloop()
        
    
    def funcao_remover_coluna(self, coluna, janela_remover_coluna):
        
        
        #Verifica se o usuário digitou uma coluna
        if coluna: 
            
            #Remove a coluna selecionada
            self.df = self.df.drop(columns=coluna)
            
        # Atualiza a árvore (treeview) com o conteúdo do arquivo
        self.atualiza_treeview()
            
        #Calcula a soma das colunas com valores
        self.soma_colunas_com_valor()
        
        #Fecha a janela secundária
        janela_remover_coluna.destroy()
        
    def filtrar(self):
        
        #Cria uma tela em segundo plano em cima da tela principal
        janela_filtrar = tk.Toplevel(self.janela_principal)
        janela_filtrar.title("Filtrar")
        
        #Define a largura e altura da janela
        largura_janela = 600
        altura_janela = 250
        
        #Obtem a largura e da tela do computador
        largura_tela = janela_filtrar.winfo_screenwidth()
        altura_tela = janela_filtrar.winfo_screenheight()
        
        #Calcula a posição da janela para centraliza-la na tela
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        #Define a posição da janela
        janela_filtrar.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        #Define a cor de fundo da janela
        janela_filtrar.configure(bg="#FFFFFF")
        
        label_coluna = tk.Label(janela_filtrar, 
                                text="Digite o nome da coluna que quer filtrar:", 
                                font=("Arial", 12), bg="#FFFFFF")
        label_coluna.pack(pady=10)
        entry_coluna = tk.Entry(janela_filtrar, 
                                      font=("Arial", 12))
        entry_coluna.pack()
        
        
        label_valor = tk.Label(janela_filtrar, 
                                text="Digite o valor a ser filtrado:", 
                                font=("Arial", 12), bg="#FFFFFF")
        label_valor.pack(pady=10)
        entry_valor = tk.Entry(janela_filtrar, 
                                      font=("Arial", 12))
        entry_valor.pack()
        
        
        
        #Cria o botão para remover a coluna
        botao_filtrar = tk.Button(janela_filtrar, 
                                  text="Filtrar", font=("Arial", 12), 
                                  command=lambda: self.funcao_filtrar(entry_coluna.get(), 
                                                                      entry_valor.get(),
                                                                      janela_filtrar))
        botao_filtrar.pack(pady=20)
        
        #Cria / exie na tela
        janela_filtrar.mainloop()
        
    
    def funcao_filtrar(self, coluna, valor, janela_filtrar):
        
        
        #Verifica se o usuário digitou uma coluna
        if coluna: 
            
            #Verifica se o usuário digitou um valor
            if valor:
                
                #Filtra o dataframe com base na coluna e valor selecionados
                self.df = self.df[self.df[coluna] == valor]
                
            
        # Atualiza a árvore (treeview) com o conteúdo do arquivo
        self.atualiza_treeview()
            
        #Calcula a soma das colunas com valores
        self.soma_colunas_com_valor()
        
        #Fecha a janela secundária
        janela_filtrar.destroy()
        
    def group(self):
        
        #Cria uma tela em segundo plano em cima da tela principal
        janela_group = tk.Toplevel(self.janela_principal)
        janela_group.title("Agrupar")
        
        #Define a largura e altura da janela
        largura_janela = 600
        altura_janela = 250
        
        #Obtem a largura e da tela do computador
        largura_tela = janela_group.winfo_screenwidth()
        altura_tela = janela_group.winfo_screenheight()
        
        #Calcula a posição da janela para centraliza-la na tela
        posicao_x = (largura_tela // 2) - (largura_janela // 2)
        posicao_y = (altura_tela // 2) - (altura_janela // 2)
        
        #Define a posição da janela
        janela_group.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")
        
        #Define a cor de fundo da janela
        janela_group.configure(bg="#FFFFFF")
        
        label_coluna = tk.Label(janela_group, 
                                text="Digite o nome da coluna que quer agrupar:", 
                                font=("Arial", 12), bg="#FFFFFF")
        label_coluna.pack(pady=10)
        entry_coluna = tk.Entry(janela_group, 
                                      font=("Arial", 12))
        entry_coluna.pack()
        
        
               
        
        
        #Cria o botão para remover a coluna
        botao_filtrar = tk.Button(janela_group, 
                                  text="Agrupar", font=("Arial", 12), 
                                  command=lambda: self.funcao_agrupar(entry_coluna.get(),
                                                                      janela_group))
        botao_filtrar.pack(pady=20)
        
        #Cria / exie na tela
        janela_group.mainloop()
        
    
    def funcao_agrupar(self, coluna, janela_group):
        
        #Limpa os dados da treeview
        self.tree.delete(*self.tree.get_children())
        
        if coluna:
            
            # Agrupa os dados com base na coluna selecionada e calcula a soma dos valores de cada grupo
            dadosAgrupados = self.df.groupby(coluna).sum()
            
            #for - para
            # Insere cada grupo na Treeview como uma nova linha
            for i, linha in dadosAgrupados.iterrows():
                
                values = list(linha)
                
                # Converte valores do tipo numpy para o tipo nativo do Python
                for j, value in enumerate(values):
                    
                    """
                    verificam se a variável 'value' é um tipo genérico do NumPy (np.generic), ou seja,
                    se é um objeto que representa um tipo de dado numérico do NumPy, como um array ou 
                    um número.

                    Se 'value' for um objeto do tipo np.generic, a linha subsequente de código 
                    converte-o para um valor escalar NumPy usando a função np.asscalar(). 
                    A função np.asscalar() é usada para converter um array escalar NumPy em um 
                    valor Python escalar.

                    O valor escalar resultante é, então, atribuído à lista 'values' na 
                    posição 'j', substituindo o valor anterior que era do tipo np.generic.

                    Essa conversão é necessária porque algumas funções ou operações não suportam 
                    tipos genéricos do NumPy. Convertendo para um valor escalar, essas funções 
                    podem trabalhar com esses valores como se fossem 
                    valores regulares do Python.
                    """
                    if isinstance(value, np.generic):
                        
                        values[j] = np.asscalar(value)
                 
                #Inserindo a nova linha na treview
                self.tree.insert("", tk.END, values=[i] + values)
                
            #Fecha a janela secundária
            janela_group.destroy()
            
    def merge_inner_join(self):
        
        # Define os tipos de arquivos que podem ser abertos
        tipo_de_arquivo = (("Excel files", "*.xlsx;*.xls"), ("All files", "*.*"))
        
        # Abre a janela para selecionar o arquivo e armazena o caminho na variável
        nome_arquivo1 = filedialog.askopenfilename(title="Selecione o primeiro arquivo", filetypes=tipo_de_arquivo)
 
        # Abre a janela para selecionar o arquivo e armazena o caminho na variável
        nome_arquivo2 = filedialog.askopenfilename(title="Selecione o segundo arquivo", filetypes=tipo_de_arquivo)

        
        #Lê os arquivos em formato de excel
        arquivo1 = pd.read_excel(nome_arquivo1)
        arquivo2 = pd.read_excel(nome_arquivo2)
        
        #Pergunta ao usuário qual coluna deve ser utilizada no merge
        coluna_join = simpledialog.askstring("Coluna do Inner Join", "Digite o nome da coluna que será utilizada para o Inner Join:")
        
        #on - Qual coluna
        #how - Como
        #inner - Faz o merge entre as tabelas
        #Procura e exibe os vendedores ques estão em ambas as tabelas
        #self.df = pd.merge(arquivo1, arquivo2, on=coluna_join, how="inner")
        #suffixes - Muda o nome da coluna
        #self.df = pd.merge(arquivo1, arquivo2[["Vendedor", "Total Vendas"]], on=coluna_join, how="inner", suffixes=(" Loja 1", " Loja 2"))
        self.df = pd.merge(arquivo1, arquivo2[["Vendedor", "Total Vendas"]], on=coluna_join, how="inner", suffixes=(" Loja 1", " Loja 2"))
        
        #Resumindo os dados
        self.df = self.df[["Vendedor", "Total Vendas Loja 1", "Total Vendas Loja 2"]]
        
        #Atualiza a Treeview com o resultado do merge
        self.atualiza_treeview()
        

editor = ExcelEditor(janela)


janela.mainloop()




