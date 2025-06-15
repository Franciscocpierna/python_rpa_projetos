#Radiobutton
from tkinter import *


#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("500x300")

#Altera o título da tela
janela.title("Radiobutton")

#Criando a variavel
variavelOpcaoSelecionada = StringVar(janela, "0")

def imprimirItemSelecionado():
    labelResutado.config(text="Você selecionou a letra " + variavelOpcaoSelecionada.get())
    

radioButtonA = Radiobutton(janela, 
                          text="Letra A",
                          variable=variavelOpcaoSelecionada,
                          value="A",
                          font=30,
                          command=imprimirItemSelecionado)
radioButtonA.pack() #pack cria e centraliza e deixa um em baixo do outro

radioButtonB = Radiobutton(janela, 
                          text="Letra B",
                          variable=variavelOpcaoSelecionada,
                          value="B",
                          font=30,
                          command=imprimirItemSelecionado)
radioButtonB.pack() #pack cria e centraliza e deixa um em baixo do outro

radioButtonC = Radiobutton(janela, 
                          text="Letra C",
                          variable=variavelOpcaoSelecionada,
                          value="C",
                          font=30,
                          command=imprimirItemSelecionado)
radioButtonC.pack() #pack cria e centraliza e deixa um em baixo do outro


labelResutado = Label(janela, text="", font=30)
labelResutado.pack() #pack cria e centraliza e deixa um em baixo do outro


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()