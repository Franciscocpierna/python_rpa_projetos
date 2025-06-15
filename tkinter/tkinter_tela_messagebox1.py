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


#Função
def mensagemInformacao():
    messagebox.showinfo("Informação", "Bem vindo(a) ao curso de Tkinter")

def mensagemAviso():
    messagebox.showwarning("Aviso", "Você está aprendendo TKinter")

def mensagemErro():
    messagebox.showerror("Erro", "Erro ao carregar o sistema")

def mensagemQuestao():
    messagebox.askquestion("Questão", "Tkinter é com Python?")

def mensagemOkouCancelar():
    messagebox.askokcancel("Ok ou Cancelar", "Deseja continuar?")

def mensagemSimouNao():
    messagebox.askyesno("Sim ou Não", "Que procurar o valor?")

def mensagemRepetirouCancelar():   
    messagebox.askretrycancel("Repetir ou Cancelar", "Que tentar novamente?")

botaoInformacao = Button(text="Informação", 
                         font = "Arial 20",
                        command = mensagemInformacao).pack() #pack cria e centraliza e deixa um em baixo do outro

botaoAviso = Button(text="Aviso", 
                         font = "Arial 20",
                        command = mensagemAviso).pack() #pack cria e centraliza e deixa um em baixo do outro

botaoErro = Button(text="Erro", 
                         font = "Arial 20",
                        command = mensagemErro).pack() #pack cria e centraliza e deixa um em baixo do outro

botaoQuestao = Button(text="Questão", 
                         font = "Arial 20",
                        command = mensagemQuestao).pack() #pack cria e centraliza e deixa um em baixo do outro

botaoOkouCancelar = Button(text="Ok ou Cancelar", 
                         font = "Arial 20",
                        command = mensagemOkouCancelar).pack() #pack cria e centraliza e deixa um em baixo do outro

botaoSimouNao = Button(text="Sim ou Não", 
                         font = "Arial 20",
                        command = mensagemSimouNao).pack() #pack cria e centraliza e deixa um em baixo do outro

botaoRepetirouCancelar = Button(text="Repetir ou Cancelar", 
                         font = "Arial 20",
                        command = mensagemRepetirouCancelar).pack() #pack cria e centraliza e deixa um em baixo do outro

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()