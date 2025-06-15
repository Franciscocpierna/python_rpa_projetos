#Radiobutton
from tkinter import *


#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("500x500")

#Altera o título da tela
janela.title("Radiobutton")

#Criando a variavel
variavelOpcaoSelecionada = StringVar(janela, "0")

def imprimirItemSelecionado():
    labelResutado.config(text="Você selecionou a letra " + variavelOpcaoSelecionada.get())
    

listaNomes = {"Letra A" : "A",
          "Letra B" : "B",
          "Letra C" : "C",
          "Letra D" : "D",
          "Letra E" : "E",
          "Letra F" : "F",
          "Letra G" : "G",
          "Letra H" : "H",
          "Letra I" : "I",
    
}

#for - para
for(textoColuna0, textoColuna1) in listaNomes.items():
                Radiobutton(janela,
                text=textoColuna0,
                variable=variavelOpcaoSelecionada,
                value=textoColuna1,
                font=30,
                command=imprimirItemSelecionado).pack() #pack cria e centraliza e deixa um em baixo do outro

labelResutado = Label(janela, text="", font=30)
labelResutado.pack() #pack cria e centraliza e deixa um em baixo do outro


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()