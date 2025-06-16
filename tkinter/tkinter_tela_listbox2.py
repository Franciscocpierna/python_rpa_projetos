#Listbox
from tkinter import *
from tkinter import messagebox


#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("500x600")

#Altera o título da tela
janela.title("Listbox")

textoDiaSemana = Label(janela, 
                       text="Dia da Semana",
                       font="Arial 40")
textoDiaSemana.pack() #pack cria e centraliza e deixa um em baixo do outro

#Criando a lista de nomes
listaNomes = ("Ana", "Amanda", "Cesar")

#Cria a variavel que contem todos os nomes
variavelNomes = Variable(value=listaNomes)

#selectmode - BROWSE, SINGLE, MULTIPLE, EXTENDED
listboxExemplo = Listbox(janela, 
                         listvariable = variavelNomes, #Recebe a lista dos nomes
                         height = 6, #Altura
                         font="Arial 40",
                         selectmode = SINGLE) #Determina o número de itens que podem ser selecionados

#expand - Centraliza
#Fill  - Expande
listboxExemplo.pack(expand=True, fill=BOTH) #pack cria e centraliza e deixa um em baixo do outro

#Criando a função que pega e exibe o item selecionado
def itemSelecionado(evento):
    
    #Retorno todos os indices / Posições selecionadas
    indiceSelecionado = listboxExemplo.curselection()
    
    #for - para
    #join - Junta todos os itens que estão selecionados na lista
    #get - pega os itens selecionados
    item = ",".join([listboxExemplo.get(posicao) for posicao in indiceSelecionado])
    mensagem = "Você selecionou: " + item
    messagebox.showinfo(title="Atenção!", message=mensagem)

#Para executar uma função quando selecionar um item
#Vinculamos a função a um evento: ListboxSelect
listboxExemplo.bind("<<ListboxSelect>>", itemSelecionado)

#Criando um campo digitavel
textoParaAdicionar = Entry(font = "Arial 40")
textoParaAdicionar.pack() #pack cria e centraliza e deixa um em baixo do outro


#Criando a função
def adicionarItem():
    
    #Adiciono o item no final da listboxExemplo
    listboxExemplo.insert(END, str(textoParaAdicionar.get()))

#Criando o botão para adiciona o novo item
botaoAdicionar = Button(text="Adicionar Item Na Lista", 
                        font = "Arial 20",
                       command = adicionarItem)

botaoAdicionar.pack() #pack cria e centraliza e deixa um em baixo do outro

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()