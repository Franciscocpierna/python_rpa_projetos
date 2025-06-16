#Combobox pega Item Selecionado
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("700x200")

#Altera o título da tela
janela.title("Combobox pega Item Selecionado")

#Criando um campo Label para informar o usuário
Label(janela, text = "Selecione um mês:",
     font = ("Arial 18")).grid(row = 1, column=0)

#Criando a bombobox
mesSelecionado = ttk.Combobox(janela, font = ("Arial 20")) 

mesSelecionado["values"] = ("Janeiro",
                           "Fevereiro",
                           "Março",
                           "Abril",
                           "Maio",
                           "Junho",
                           "Julho",
                           "Agosto",
                           "Setembro",
                           "Outubro",
                           "Novembro",
                           "Dezembro"
                           )

#grid - é uma tabela / Pedaço da tabela
mesSelecionado.grid(row = 1, column=1)
mesSelecionado.current(5) #Deixo um mês selecionado

#criando a função que imprime o item selecionado
def itemSelecionado():
    print(str(mesSelecionado.get()))

botaoSelecionar = Button(text="Item selecionado",
                        font = "Arial 20",
                        command=itemSelecionado)

#columnspan - Oculpa o espaço de uma ou mais colunas dependendo do número
#stick - Estica o campo para oculpar todos o espaço em branco na tela
#NSEW - Norte, Sul, Leste e Oeste
botaoSelecionar.grid(row = 2, column=0, columnspan=2, stick="NSEW")

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()