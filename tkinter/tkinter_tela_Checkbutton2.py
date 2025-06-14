#Checkbutton
from tkinter import *


#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("950x400")

#Altera o título da tela
janela.title("Checkbutton")

#fg - cor da letra
#fg - foreground / Cord da Letra
informacao = Label(janela, text = "Selecione a opção desejada",
                  fg="blue", font="Arial 20")

informacao.pack() #pack centraliza e deixa um em baixo do outro

total = 0
valorAntigo = 0

#Funções
def soma():
    global total
    global valorAntigo
    
    valorAntigo = total
    #total = total + int(varNumero.get())
    total += int(varNumero5.get()) + int(varNumero10.get()) + int(varNumero15.get())
    
    print(valorAntigo, " + ", total)
    

    
#Criando as variáveis que vão armazenar os textos
varNumero5 = IntVar()
varNumero10 = IntVar()
varNumero15 = IntVar()

checkNumero5 = Checkbutton(janela, text = "5",
                       variable = varNumero5,
                       onvalue = 5,
                       font="Arial 20",
                       offvalue = 0,
                       height = 2, #altura
                       width = 10, #largura
                       command=soma) 

checkNumero10 = Checkbutton(janela, text = "10",
                       variable = varNumero10,
                       onvalue = 10,
                       font="Arial 20",
                       offvalue = 0,
                       height = 2, #altura
                       width = 10, #largura
                       command=soma)

checkNumero15 = Checkbutton(janela, text = "15",
                       variable = varNumero15,
                       onvalue = 15,
                       font="Arial 20",
                       offvalue = 0,
                       height = 2, #altura
                       width = 10, #largura
                       command=soma)

checkNumero5.pack() #pack centraliza e deixa um em baixo do outro
checkNumero10.pack() #pack centraliza e deixa um em baixo do outro
checkNumero15.pack() #pack centraliza e deixa um em baixo do outro

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()

