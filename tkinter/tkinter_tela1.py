#Trabalhando com Label
from tkinter import *

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()

#Altera o título da tela
janela.title("Interface Gráfica / Label")

texto = """Curso de Tkinter
Aprendendo como criar
Interface gráfica com
Python
"""

formato = Label(janela,
               font = "Arial 40 bold",
               text = texto).pack() #pack cria e centraliza e deixa um em baixo do outro

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()