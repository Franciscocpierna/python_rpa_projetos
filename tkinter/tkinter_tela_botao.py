#Trabalhando com Botões
from tkinter import *
from tkinter import messagebox

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()

#Altera o título da tela
janela.title("Tela Botões")

#def - criarmos funções
def exibirMensagem():
    messagebox.showinfo("Titulo Mensagem", "Olá, mundo!")

#command - Executa uma ação nesse caso chamou e executou uma função
botao = Button(janela, text = "Clique aqui", command = exibirMensagem)

botao.pack() #pack cria e centraliza e deixa um em baixo do outro


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()