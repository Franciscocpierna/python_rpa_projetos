#Trabalhando com Botões
from tkinter import *
from tkinter import messagebox

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()

#Altera o título da tela
janela.title("Tela Botões")

#def - criarmos funções
def mensagem():
    #print("Curso de Tkinter!")
    messagebox.showinfo("Titulo Mensagem", "curso de Tkinter!")

#command - Executa uma ação
botaoSair = Button(janela, 
                   text = "Sair", 
                   command = janela.destroy) #Fecha a tela do Tkinter

#command - Executa uma ação nesse caso chamou e executou uma função
botaoEntrar = Button(janela, 
                   text = "Entrar", 
                   command = mensagem) #Fecha a tela do Tkinter

botaoSair.pack() #pack cria e centraliza e deixa um em baixo do outro
botaoEntrar.pack(side = LEFT) #Criando do lado esquerdo


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()