#Trabalhando com Botões
from tkinter import *
from tkinter import messagebox

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()

#Altera o título da tela
janela.title("Tela Botões")



#bg - background / Cor do Fundo
#fg - foreground / Cord da Letra
#pack - TOP, BOTTOM, LEFT, RIGTH
botaoVerde = Button(janela, text = "VERDE", fg="white", bg="green") 
botaoVerde.pack(side = LEFT) #pack cria no lado esquerdo

#bg - background / Cor do Fundo
#fg - foreground / Cord da Letra
botaoAmarelo = Button(janela, text = "AMARELO", fg="black", bg="yellow") 
botaoAmarelo.pack(side = TOP) #pack cria no lado esquerdo

#bg - background / Cor do Fundo
#fg - foreground / Cord da Letra
botaoAzul = Button(janela, text = "AZUL", fg="white", bg="blue") 
botaoAzul.pack(side = LEFT) #pack cria no lado esquerdo



#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()