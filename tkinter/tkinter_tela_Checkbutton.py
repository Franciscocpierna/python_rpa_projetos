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

#Funções
def azulClicado():
    print(varAzul.get())
    
def amareloClicado():
    print(varAmarelo.get())
    
def verdeClicado():
    print(varVerde.get())
    
#  A linha varAzul = StringVar() cria uma variável especial do tipo StringVar, que é usada no Tkinter (biblioteca de interface gráfica do Python) para armazenar e gerenciar valores de texto de widgets, como Entry, Label ou OptionMenu. Ela permite que o valor do widget seja atualizado automaticamente na interface sempre que o valor da variável muda, e vice-versa.   
    
#Criando as variáveis que vão armazenar os textos
# Cria uma variável do tipo StringVar para uso em widgets do Tkinter (interface gráfica)
# varAzul = StringVar()
varAzul = StringVar()
varAmarelo = StringVar()
varVerde = StringVar()

checkAzul = Checkbutton(janela, text = "Azul",
                       variable = varAzul,
                       onvalue = "Clicou na cor Azul",
                       font="Arial 20",
                       offvalue = "",
                       height = 2, #altura
                       width = 10, #largura
                       command=azulClicado) 

checkAmarelo = Checkbutton(janela, text = "Amarelo",
                       variable = varAmarelo,
                       onvalue = "Clicou na cor Amarelo",
                       font="Arial 20",
                       offvalue = "",
                       height = 2, #altura
                       width = 10, #largura
                       command=amareloClicado)

checkVerde = Checkbutton(janela, text = "Verde",
                       variable = varVerde,
                       onvalue = "Clicou na cor Verde",
                       font="Arial 20",
                       offvalue = "",
                       height = 2, #altura
                       width = 10, #largura
                       command=verdeClicado)

checkAzul.pack() #pack centraliza e deixa um em baixo do outro
checkAmarelo.pack() #pack centraliza e deixa um em baixo do outro
checkVerde.pack() #pack centraliza e deixa um em baixo do outro

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()