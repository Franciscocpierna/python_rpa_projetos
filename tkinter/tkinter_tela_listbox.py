#Listbox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("500x500")

#Altera o título da tela
janela.title("Listbox")

textoDiaSemana = Label(janela, 
                       text="Dia da Semana",
                       font="Arial 40")
textoDiaSemana.pack() #pack cria e centraliza e deixa um em baixo do outro

listboxExemplo = Listbox(janela, font="Arial 40")

#insert - Inserindo o item dentro do listbox
listboxExemplo.insert(1, "Domingo")
listboxExemplo.insert(2, "Segunda-feira")
listboxExemplo.insert(3, "Terça-feira")
listboxExemplo.insert(4, "Quarta-feira")
listboxExemplo.insert(5, "Quinta-feira")
listboxExemplo.insert(6, "Sexta-feira")
listboxExemplo.insert(7, "Sábado")


listboxExemplo.pack() #pack cria e centraliza e deixa um em baixo do outro


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()