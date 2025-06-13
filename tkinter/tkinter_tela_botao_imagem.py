#Botões com Imagem
from tkinter import *

#pillow também é conhecido como PIL
from PIL import ImageTk, Image

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()

#Altera o título da tela
janela.title("Botões com Imagem")

Label(janela, text = "Imagem", 
     font = ("Verdana 15")).pack()  #pack cria e centraliza e deixa um em baixo do outro

#Configurando o caminho e a imagem
caminhoImagem = ImageTk.PhotoImage(Image.open("C:\\python_projetos\\python_rpa_projetos\\tkinter\\imagem\\sair.jpg"))

#Criamos o botão e colocamos a imagem no botão
botaoComImagem = Button(image = caminhoImagem, command=janela.destroy)
botaoComImagem.pack()#pack cria e centraliza e deixa um em baixo do outro

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()