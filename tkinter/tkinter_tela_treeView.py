#TreeView
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("750x350")

#Altera o título da tela
janela.title("TreeView")
# Define o tema visual dos widgets ttk como "alt"
#theme_use - alt, default, classic
#Configurando o título e o stilo
estiloDaTreeview = ttk.Style()
estiloDaTreeview.theme_use("alt")
# Configura a fonte padrão dos widgets para Arial tamanho 14
estiloDaTreeview.configure(".", font = "Arial 14")

#column - criando 4 colunas
treeViewDados = ttk.Treeview(janela, column=(1, 2, 3, 4), show="headings")

treeViewDados.column("1", anchor= CENTER) #centralizo a coluna
treeViewDados.heading("1", text= "ID" ) #Coloco o titulo da coluna
# Configura a coluna 2 para centralizar o texto
treeViewDados.column("2", anchor= CENTER) #centralizo a coluna
treeViewDados.heading("2", text= "Nome" ) #Coloco o titulo da coluna

treeViewDados.column("3", anchor= CENTER) #centralizo a coluna
treeViewDados.heading("3", text= "Idade" ) #Coloco o titulo da coluna

treeViewDados.column("4", anchor= CENTER) #centralizo a coluna
treeViewDados.heading("4", text= "Sexo" ) #Coloco o titulo da coluna

#Inserindo dados na treeview
# Insere uma linha na Treeview com os valores: ID, Nome, Idade, Sexo
treeViewDados.insert("", "end", text="1", values=("1", "Allan", 29, "Masculino"))
treeViewDados.insert("", "end", text="2", values=("2", "Ana", 41, "Feminino"))
treeViewDados.insert("", "end", text="3", values=("3", "Berenice", 50, "Feminino"))
treeViewDados.insert("", "end", text="4", values=("4", "Roger", 19, "Masculino"))
treeViewDados.insert("", "end", text="5", values=("5", "Pedro", 25, "Masculino"))


treeViewDados.pack() #pack cria e centraliza e deixa um em baixo do outro
#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()
