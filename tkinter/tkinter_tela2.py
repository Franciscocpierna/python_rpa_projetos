#Trabalhando com Label
from tkinter import *

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()

#Altera o título da tela
janela.title("Tela 3 x 3")

#for - para
for linha in range(5):
    
    for coluna in range(3):
        
        #relief - Relevo - Borda decorativa ao redor do rótulo
        #master: Mestre - Representa a Janela PAI
        tabela = Frame(
            master = janela,
            relief = RAISED,
            borderwidth = 1
        )
        #padx - Espaçamento entre colunas
        #pady - Espaçamento entre linhas
        tabela.grid(row=linha, column=coluna, padx=50, pady=50)
        label = Label(master=tabela, text = f"Linha {linha}\n Coluna {coluna}")
        label.pack() #pack cria e centraliza e deixa um em baixo do outro


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()