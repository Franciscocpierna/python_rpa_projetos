#Entry - Campo de entrada de dados
from tkinter import *
from tkinter import messagebox

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("950x400")

#Altera o título da tela
janela.title("Entry - Campo de entrada de dados")

#grid - Divide a tela em grades / parte
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
usuario = Label(text = "Usuário: ", font = "Arial 40")
usuario.grid(row=1, column=0, stick="W")

#Entry - Campo de entrada de dados
campoDigitavelUsuario = Entry(font = "Arial 40")
campoDigitavelUsuario.grid(row=1, column=1, stick="W")

#Label
senha = Label(text = "Senha: ", font = "Arial 40")
senha.grid(row=2, column=0, stick="W")

#Entry - Campo de entrada de dados
#show - Substitui o que está digitado por *
campoDigitavelSenha = Entry(font = "Arial 40", show="*")
campoDigitavelSenha.grid(row=2, column=1, stick="W")

#Criando a função para logar
def logar():
    
    #pegando o texto que foi digitado no campo campoDigitavelUsuario
    nome = str(campoDigitavelUsuario.get())
    
    #pegando o texto que foi digitado no campo campoDigitavelUsuario
    senha = str(campoDigitavelSenha.get())
    
    #if - se
    #and - e
    if nome == "steven" and senha == "555":
        
        messagebox.showinfo("Messagem", "Bem vindo(a) ao sistema!" )
        
    else:
        
        messagebox.showinfo("Messagem", "Usuário ou senha inválidos!" )

botao = Button(text = "ENTRAR", font = "Arial 40", 
              command=logar)

#columnspan - Colocamos para dizer quantas colunas do grid o item vai oculpar
botao.grid(row=3, column=0, columnspan=2, stick="NSEW")


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()