from tkinter import Tk
from tkinter import *
#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
tela = Tk()
tela.title("Interface Gráfica / Label")
#relief - Relevo - Borda decorativa ao redor do rótulo
#bg - background / Cor do Fundo
#fg - foreground / Cord da Letra
#https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
#borderwidth - Especura da borda
rotulo1 = Label(tela, text = "Python", relief=FLAT, bg="green", fg="white" )
rotulo2 = Label(tela, text = "Python", relief=FLAT, bg="blue", fg="white", font="Mangal 40" )
rotulo3 = Label(tela, text = "Python", relief=GROOVE, bg="green", fg="white", font="Mangal 40", borderwidth=25 )

#pack() - Coloca o objeto dentro da Janela / Tela
rotulo1.pack() #pack centraliza e deixa um em baixo do outro
rotulo2.pack()
rotulo3.pack()


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
tela.mainloop()