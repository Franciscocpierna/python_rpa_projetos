#Entry - Campo de entrada de dados
from tkinter import *

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("950x200")

#Altera o título da tela
janela.title("Entry - Campo de entrada de dados")

#grid - Divide a tela em grades / parte
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
nome = Label(text = "Nome: ", font = "Arial 40")
nome.grid(row=1, column=0, stick="W")

#Entry - Campo de entrada de dados
campoDigitavelNome = Entry(font = "Arial 40")
campoDigitavelNome.grid(row=1, column=1, stick="W")

#Label
sobrenome = Label(text = "Sobrenome: ", font = "Arial 40")
sobrenome.grid(row=2, column=0, stick="W")

#Entry - Campo de entrada de dados
campoDigitavelSobrenome = Entry(font = "Arial 40")
campoDigitavelSobrenome.grid(row=2, column=1, stick="W")


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()