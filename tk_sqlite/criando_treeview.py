#Importa o modulo pyodbc para conexão com bando de dados
import pyodbc

#Importa o módulo tkinter para construção de interfaces gráficas
from tkinter import *

#Importa a classe ttk do módulo tkinter
from tkinter import ttk

#Driver - Drive
#Server - Servidor
#Database - Nome do Banco de Dados
dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db")

#UID - Login
#PWD - Senha

#Criando a conexao
conexao = pyodbc.connect(dadosConexao)

#Cria um objeto cursor para executar os comandos SQL no banco de dados
cursor = conexao.cursor()

#Executa um comando SQL para selecionar todos os valores da tabela de Produtos
conexao.execute("Select * From Produtos")

print("Conectado com sucesso!")

#Criando uma janela tkinter com o título "Cadastro de Produtos"
janela = Tk()
janela.title("Cadastro de Produtos")

#Definindo a cor de fundo para a janela
janela.configure(bg="#F5F5F5")

#Deixando a janela em tela cheia
janela.attributes("-fullscreen", True)

#Função para cadastrar o produto
def cadastrar():
    
    #Cria uma nova janela para cadastrar o produto
    janela_cadastrar = Toplevel(janela)
    janela_cadastrar.title("Cadastrar Produto")
    
    #bg - background (cor do fundo)
    #Definindo a cor de fundo da janela
    janela_cadastrar.configure(bg="#FFFFFF")

    #Define a largura e altura da janela
    largura_janela = 450
    altura_janela = 230

    #Obtem a largura e altura da tela computador
    largura_tela = janela_cadastrar.winfo_screenwidth()
    altura_tela = janela_cadastrar.winfo_screenheight()


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
    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    #Define a posição da janela
    """
    define a geometria da janela principal, especificando a 
    largura e altura da janela, bem como a posição onde a janela 
    será exibida na tela, usando as variáveis previamente definidas 
    para a posição x e y da janela. O formato utilizado é uma string 
    que contém os valores de largura, altura, posição x e posição y da 
    janela separados por "x" e "+" e passados ​​como argumentos para o m
    étodo geometry() da janela principal.

    O formato '{}'x'{}'+'{}'+'{}' é uma string de formatação que espera
    quatro valores, que correspondem à largura da janela, altura da janela, 
    posição x da janela e posição y da janela, respectivamente.

    Esses valores são passados na ordem especificada para a string de formatação e, 
    em seguida, são utilizados para definir a geometria da janela através do 
    método geometry do objeto janela_principal.
    """
    janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y ))
    
    
    for i in range(5):
        janela_cadastrar.grid_rowconfigure(i, weight=1)

    
    for i in range(2):
        janela_cadastrar.grid_columnconfigure(i, weight=1)
    
    #Adiciona bordas para cada campo de entrada
    estilo_borda = {"borderwidth": 2, "relief": "groove"}
    
    #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
    #fg - foreground (cor da letra)
    #row - linha
    #column - coluna
    #pady - espaço
    Label(janela_cadastrar, text="Nome do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, stick="W")
    nome_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
    nome_produto_cadastrar.grid(row=0, column=1, padx=10, pady=10)
    
    Label(janela_cadastrar, text="Descrição do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, stick="W")
    descricao_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
    descricao_produto_cadastrar.grid(row=1, column=1, padx=10, pady=10)
    
    Label(janela_cadastrar, text="Preço do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, stick="W")
    preco_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
    preco_produto_cadastrar.grid(row=2, column=1, padx=10, pady=10)
    
    #Cria uma função para salvar os dados no banco de dados
    def salvar_dados():
        
        #Cria uma tupla com os valores dos campos de texto
        novo_produto_cadastrar = (nome_produto_cadastrar.get(), descricao_produto_cadastrar.get(), preco_produto_cadastrar.get())
        
        #Executa um comando SQL para inserir os dados na tabela Produtos no banco de dados
        cursor.execute("INSERT INTO Produtos (NomeProduto, Descricao, Preco) Values (?, ?, ?)", novo_produto_cadastrar)
        conexao.commit() #Gravando no BD

        print("Dados cadastrados com sucesso!")
        
        
        #Fecha a janela de cadastro
        janela_cadastrar.destroy()
        
        
        
    #columnspan - quantas colunas vai ocupar no grid   
    #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
    botao_salvar_dados = Button(janela_cadastrar, text="Salvar", font=("Arial", 12), command=salvar_dados)
    botao_salvar_dados.grid(row=3, column=0, columnspan=2, padx=10, pady=10, stick="NSEW")
    
    #columnspan - quantas colunas vai ocupar no grid   
    #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
    botao_cancelar = Button(janela_cadastrar, text="Cancelar", font=("Arial", 12), command=janela_cadastrar.destroy)
    botao_cancelar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, stick="NSEW")

#Define o estilo da Treeview
style = ttk.Style(janela)

#Criando a Treeview
treeview = ttk.Treeview(janela, style="mystyle.Treeview")

style.theme_use("default")

#Configurando
style.configure("mystyle.Treeview", font=("Arial", 14))

treeview = ttk.Treeview(janela, style="mystyle.Treeview", columns=("ID", "NomeProduto", "Descricao", "Preco"), show="headings", height=20)

treeview.heading("ID", text="ID")
treeview.heading("NomeProduto", text="Nome do Produto")
treeview.heading("Descricao", text="Descrição do Produto")
treeview.heading("Preco", text="Preço do Produto")
#A primeira coluna, identificada como "#0"
#A opção "stretch=NO" indica que a coluna não deve esticar para preencher o espaço disponível.
treeview.column("#0", width=0, stretch=NO)
treeview.column("ID", width=100)
treeview.column("NomeProduto", width=300)
treeview.column("Descricao", width=500)
treeview.column("Preco", width=200)

#columnspan - quantas colunas vai ocupar no grid   
#stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
treeview.grid(row=3, column=0, columnspan=10, stick="NSEW")


#Configura a janela para utilizar a barra de menus criada
menu_barra = Menu(janela)
janela.configure(menu=menu_barra)

#Cria o menu chamado Arquivo
"""
O parâmetro "tearoff=0" é utilizado no tkinter para controlar 
a exibição de uma linha pontilhada no início de menus cascata. 
Ao definir "tearoff=0", a linha pontilhada não será exibida e o 
menu cascata ficará fixo na janela, não podendo ser destacado 
ou movido para outra posição.
"""
menu_arquivo = Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)

#Cria uma opção no menu "Arquivo" chamada "Cadastrar"
menu_arquivo.add_command(label="Cadastrar", command=cadastrar)

#Cria uma opção no menu "Arquivo" chamada "Sair"
menu_arquivo.add_command(label="Sair", command=janela.destroy)


#Inicia a janela Tkinter
janela.mainloop()

#Fechar o cursor e a conexao
cursor.close()
conexao.close()