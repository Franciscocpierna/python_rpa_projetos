#Messagebox
from tkinter import *
from tkinter import messagebox


#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("500x500")

#Altera o título da tela
janela.title("Messagebox")

informacao = Label(janela, text="Mensagens", font = 50)
informacao.pack() #pack cria e centraliza e deixa um em baixo do outro

messagebox.showinfo("Informação", "Bem vindo(a) ao curso de Tkinter")
messagebox.showwarning("Aviso", "Você está aprendendo TKinter")
messagebox.showerror("Erro", "Erro ao carregar o sistema")
messagebox.askquestion("Questão", "Tkinter é com Python?")
messagebox.askokcancel("Ok ou Cancelar", "Deseja continuar?")
messagebox.askyesno("Sim ou Não", "Que procurar o valor?")
messagebox.askretrycancel("Repetir ou Cancelar", "Que tentar novamente?")

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()