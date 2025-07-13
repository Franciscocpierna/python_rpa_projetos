#Importa o modulo pyodbc para conexão com bando de dados
import pyodbc

#Importa o módulo tkinter para construção de interfaces gráficas
from tkinter import *

#Importa a classe ttk do módulo tkinter
from tkinter import ttk

#Função que verifica se as credenciais do usuário estão corretas
def verifica_credenciais():
    
    #Driver - Drive
    #Server - Servidor
    #Database - Nome do Banco de Dados
    conexao = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db")

    #cursor - Ferramenta para exercutar os comandos em SQL
    cursor = conexao.cursor()
    
    #Executando uma query que seleniona os usuários que possuem o nome de usuário e senha inseridos pelo usuário
    cursor.execute("SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?", (nome_usuario_entry.get(), senha_usuario_entry.get()))
    
    #Recebendo o resultado da query
    usuario = cursor.fetchone()
    
    #if - se
    if usuario:
        
        #Destruindo / Fechando a janela de Login
        janela_principal.destroy()
        
        #Criando uma nova janela para a tela principal
        janela = Tk()
        janela.title("Tela Principal")
        
        #Fechar o cursor e a conexao
        cursor.close()
        conexao.close()
        
        
    else:
        
        mensagem_lbl = Label(janela_principal, text="Nome de usuário ou senha incorretos", fg="red")
        mensagem_lbl.grid(row=3, column=0, columnspan=2)

#Criando a janela principal para a tela de login
janela_principal = Tk()
janela_principal.title("Tela de Login")

#bg - background (cor do fundo)
#Definindo a cor de fundo da janela
janela_principal.configure(bg="#F5F5F5")

#Define a largura e altura da janela
largura_janela = 450
altura_janela = 300

#Obtem a largura e altura da tela computador
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()


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
janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y ))

#stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
#fg - foreground (cor da letra)
#row - linha
#column - coluna
#columnspan - quantas colunas vai ocupar no grid
#pady - espaço
titulo_lbl = Label(janela_principal, text="Tela de Login", font="Arial 20", fg="blue", bg="#F5F5F5")
titulo_lbl.grid(row=0, column=0, columnspan=2, pady=20)

#Campo label
nome_usuario_lbl = Label(janela_principal, text="Nome de Usuário", font="Arial 14 bold", bg="#F5F5F5")
nome_usuario_lbl.grid(row=1, column=0, stick="e") #NSEW

#Campo label
senha_usuario_lbl = Label(janela_principal, text="Senha", font="Arial 14 bold", bg="#F5F5F5")
senha_usuario_lbl.grid(row=2, column=0, stick="e") #NSEW

#Criando um entry para o campo Nome de Usuario com a fonte Arial tamanho 14
nome_usuario_entry = Entry(janela_principal, font="Arial 14")
nome_usuario_entry.grid(row=1, column=1, pady=10 )

#Criando um entry para o campo Nome de Usuario com a fonte Arial tamanho 14
senha_usuario_entry = Entry(janela_principal, show="*", font="Arial 14")
senha_usuario_entry.grid(row=2, column=1, pady=10 )

#stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
entrar_btn = Button(janela_principal, text="Entrar", font="Arial 14", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, stick="NSEW")

#stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
sair_btn = Button(janela_principal, text="Sair", font="Arial 14", command=janela_principal.destroy)
sair_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, stick="NSEW")

"""
Esse código está dentro de um laço "for" que executa 5 vezes
e serve para configurar o comportamento de uma grade (ou "grid") no tkinter.
A função "grid_rowconfigure()" permite definir a configuração de uma 
determinada linha na grade, com dois parâmetros: 
o índice da linha e um peso (ou "weight") que determina 
como essa linha deve se comportar em relação às outras linhas da grade.

No código em questão, o laço "for" está configurando as 5 linhas
da grade da janela_principal com um peso igual a 1. 
Isso significa que todas as linhas terão a mesma altura 
e que a altura da janela será dividida igualmente entre elas.
"""
for i in range(5):
    janela_principal.grid_rowconfigure(i, weight=1)

"""
Este código é usado para definir a configuração das colunas da grade
na janela principal. Ele utiliza um loop "for" para iterar através de 
duas colunas da grade e chama o método "grid_columnconfigure" do 
objeto "janela_principal" para definir o "weight" (peso) como 1.

O parâmetro "weight" é uma propriedade do gerenciador de layout do 
Tkinter que define a prioridade de expansão das colunas (ou linhas) 
quando a janela é redimensionada. Valores mais altos de "weight" significam
que a coluna irá expandir mais do que as outras colunas que possuem valores 
mais baixos de "weight". Ao configurar as colunas com um "weight" de 1, 
a janela principal será capaz de expandir uniformemente as colunas em toda 
a largura da janela quando ela for redimensionada.
"""
for i in range(2):
    janela_principal.grid_columnconfigure(i, weight=1)

#Inicia a janela Tkinter
janela_principal.mainloop()