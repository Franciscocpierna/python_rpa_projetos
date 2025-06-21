#Criando a tela
from tkinter import *
from tkinter import ttk

#tk - Biblioteca do Tkinter
#tk - Janela / Tela
janela = Tk()

#Tamanho da tela
janela.geometry("950x350")
janela.title("Treeview")

#grid - Divide a tela em grades / parte
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
cep = Label(text = "CEP: ", font = "Arial 20")
cep.grid(row = 1, column = 0, stick = "W")

#Campo para digitar a informação
campoDigitavelCEP = Entry(font = "Arial 20")
campoDigitavelCEP.grid(row = 1, column = 1, columnspan = 3, stick = "W")


#Criando a função que busca o CEP
def pesquisaCEP():
    
    print("Pronto!")


#bg - background / Cor do Fundo
#fg - foreground / Cord da Letra
botao = Button(text = "PESQUISAR", font = "Arial 12",
              command = pesquisaCEP, 
              bg = "blue",
              fg = "white")

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
botao.grid(row = 1, column = 4, columnspan = 4, stick = "NSEW")

configuracoesTreeview = ttk.Style()
configuracoesTreeview.theme_use("alt")
configuracoesTreeview.configure(".", font = ("Arial", 20))

treeviewDados = ttk.Treeview(janela, column = (1, 2, 3, 4), show = "headings")

treeviewDados.column("1", anchor=CENTER)
treeviewDados.heading("1", text = "Rua")

treeviewDados.column("2", anchor=CENTER)
treeviewDados.heading("2", text = "Bairro")

treeviewDados.column("3", anchor=CENTER)
treeviewDados.heading("3", text = "Cidade")

treeviewDados.column("4", anchor=CENTER)
treeviewDados.heading("4", text = "CEP")

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
treeviewDados.grid(row = 2, column = 0, columnspan = 8, stick = "NSEW")



#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()