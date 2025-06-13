#Imagem plano de fundo
from tkinter import *

#pillow também é conhecido como PIL
from PIL import ImageTk, Image

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("460x260")

#Altera o título da tela
janela.title("Imagem plano de fundo")

#Configurando o caminho e a imagem
caminhoImagem = ImageTk.PhotoImage(Image.open("C:\\python_projetos\\python_rpa_projetos\\tkinter\\imagem\\plano_fundo.png"))

labelParaFundo = Label(image = caminhoImagem)
labelParaFundo.place(x=0, y=0)

#relief - Relevo - Borda decorativa ao redor do rótulo
#bg - background / Cor do Fundo
#fg - foreground / Cord da Letra
#https://stackoverflow.com/questions/39614027/list-available-font-families-in-tkinter
#borderwidth - Especura da borda
rotulo1 = Label(janela, text = "Python", relief=FLAT, bg="green", fg="white" )
rotulo2 = Label(janela, text = "Python", relief=FLAT, bg="blue", fg="white", font="Mangal 20" )
rotulo3 = Label(janela, text = "Python", relief=GROOVE, bg="green", fg="white", font="Mangal 20", borderwidth=25 )

#pack() - Coloca o objeto dentro da Janela / Tela
rotulo1.pack() #pack centraliza e deixa um em baixo do outro
rotulo2.pack()
rotulo3.pack()

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()