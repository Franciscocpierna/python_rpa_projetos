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
senha_usuario_entry = Entry(janela_principal, font="Arial 14")
senha_usuario_entry.grid(row=2, column=1, pady=10 )

#stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
entrar_btn = Button(janela_principal, text="Entrar", font="Arial 14", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, stick="NSEW")

#stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
sair_btn = Button(janela_principal, text="Sair", font="Arial 14", command=janela_principal.destroy)
sair_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, stick="NSEW")

#Inicia a janela Tkinter
janela_principal.mainloop()

