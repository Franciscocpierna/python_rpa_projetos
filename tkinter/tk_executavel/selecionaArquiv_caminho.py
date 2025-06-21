#Selecionar um arquivo e imprimir o caminho do arquivo
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#tk - Biblioteca do Tkinter
#tk - Janela / Tela
janela = Tk()

#Tamanho da tela
janela.geometry("800x200")
janela.title("Abrir arquivo")

#grid - Divide a tela em grades / parte
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
caminhoArquivo = Label(text = "Caminho: ", font = "Arial 20")
caminhoArquivo.grid(row = 1, column = 0, stick = "W")

#Campo para digitar a informação
campoRecebeCaminhoArquivo = Entry(font = "Arial 20")
campoRecebeCaminhoArquivo.grid(row = 1, column = 1, columnspan = 6, stick = "W")

def abrirArquivo():
    
    #Abre a caixa do dialog e permite selecionar o arquivo e retorna o caminho
    caminhoArquivo = filedialog.askopenfilename()
    
    campoRecebeCaminhoArquivo.insert("insert", caminhoArquivo)

#bg - background / Cor do Fundo
#fg - foreground / Cord da Letra
botao = Button(text = "Selecionar", font = "Arial 12",
              command = abrirArquivo, 
              bg = "blue",
              fg = "white")

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
botao.grid(row = 1, column = 7, columnspan = 4, stick = "NSEW")


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()