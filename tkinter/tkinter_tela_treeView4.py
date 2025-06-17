#TreeView Cadastrar, Alterar, Deletar e contar Linhas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()


#Define o tamanho da janela
janela.geometry("950x350")

#Altera o título da tela
janela.title("TreeView Cadastrar, Alterar, Deletar e contar Linhas")

#grid - Divide a tela em grades / parte
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
id = Label(text = "ID", font = "Arial 12")
id.grid(row=1, column=0, stick="W")

#Campo para digitar a informação
campoDigitavelID = Entry(font = "Arial 12")
campoDigitavelID.grid(row=1, column=1, stick="W")

#-------------------------------------------------

#grid - Divide a tela em grades / parte
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
nome = Label(text = "Nome", font = "Arial 12")
nome.grid(row=1, column=2, stick="W")

#Campo para digitar a informação
campoDigitavelNome = Entry(font = "Arial 12")
campoDigitavelNome.grid(row=1, column=3, stick="W")

#-------------------------------------------------

#grid - Divide a tela em grades / parte
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
idade = Label(text = "Idade", font = "Arial 12")
idade.grid(row=1, column=4, stick="W")

#Campo para digitar a informação
campoDigitavelIdade = Entry(font = "Arial 12")
campoDigitavelIdade.grid(row=1, column=5, stick="W")

#-------------------------------------------------

#grid - Divide a tela em grades / parte
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
sexo = Label(text = "Sexo", font = "Arial 12")
sexo.grid(row=1, column=6, stick="W")

#Campo para digitar a informação
campoDigitavelSexo = Entry(font = "Arial 12")
campoDigitavelSexo.grid(row=1, column=7, stick="W")

#-------------------------------------------------

#Função que adiciona o item na Treeview
def addItemTreeview():
    
    #if - Se
    
    if str(campoDigitavelID.get()) == "":
        
        print("Digite algo no campo ID")
        
    elif str(campoDigitavelNome.get()) == "":
        
        print("Digite algo no campo Nome")
        
    elif str(campoDigitavelIdade.get()) == "":
        
        print("Digite algo no campo Idade")  
        
    elif str(campoDigitavelSexo.get()) == "":
        
        print("Digite algo no campo Sexo")
        
    else:
    
        treeViewDados.insert("", "end", 
                             values=(str(campoDigitavelID.get()),
                                    str(campoDigitavelNome.get()),
                                    str(campoDigitavelIdade.get()),
                                    str(campoDigitavelSexo.get())))

        #Limpando os campos
        campoDigitavelNome.delete(0, "end")
        campoDigitavelIdade.delete(0, "end")
        campoDigitavelSexo.delete(0, "end")
        campoDigitavelID.delete(0, "end")
        
    #Chamando a função que conta a quantidade de linhas
    contarNumeroLinhas()

botaoAdicionar = Button(text="Cadastrar",
                       font = "Arial 20",
                       command = addItemTreeview)

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
botaoAdicionar.grid(row=2, column=0, columnspan=2, stick="NSEW")

#theme_use - alt, default, classic
#Configurando o título e o stilo
estiloDaTreeview = ttk.Style()
estiloDaTreeview.theme_use("alt")
estiloDaTreeview.configure(".", font = "Arial 14")

#column - criando 4 colunas
treeViewDados = ttk.Treeview(janela, column=(1, 2, 3, 4), show="headings")

treeViewDados.column("1", anchor= CENTER) #centralizo a coluna
treeViewDados.heading("1", text= "ID" ) #Coloco o titulo da coluna

treeViewDados.column("2", anchor= CENTER) #centralizo a coluna
treeViewDados.heading("2", text= "Nome" ) #Coloco o titulo da coluna

treeViewDados.column("3", anchor= CENTER) #centralizo a coluna
treeViewDados.heading("3", text= "Idade" ) #Coloco o titulo da coluna

treeViewDados.column("4", anchor= CENTER) #centralizo a coluna
treeViewDados.heading("4", text= "Sexo" ) #Coloco o titulo da coluna

#Inserindo dados na treeview
treeViewDados.insert("", "end", text="1", values=("1", "Allan", 29, "Masculino"))
treeViewDados.insert("", "end", text="2", values=("2", "Ana", 41, "Feminino"))
treeViewDados.insert("", "end", text="3", values=("3", "Berenice", 50, "Feminino"))
treeViewDados.insert("", "end", text="4", values=("4", "Roger", 19, "Masculino"))
treeViewDados.insert("", "end", text="5", values=("5", "Pedro", 25, "Masculino"))

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
treeViewDados.grid(row=3, column=0, columnspan=8, stick="NSEW")

#Criando o Label que vai mostra o total de linhas
labelNumeroLinhas = Label(text = "Linhas: ", font = "Arial 20")
labelNumeroLinhas.grid(row=4, column=0, columnspan=8, stick="W")

def contarNumeroLinhas(item=""):
    
    numeroDeLinhas = 0
    
    #Pega a tabela
    linhas = treeViewDados.get_children(item)
    
    #for - para
    for linha in linhas:
        
        #numeroDeLinhas = numeroDeLinhas + 1
        numeroDeLinhas += 1
        
    labelNumeroLinhas.config(text="Linhas: " + str(numeroDeLinhas))
    

#Chamando a função que conta a quantidade de linhas
contarNumeroLinhas()
        

def deletarItemTreeview():
    
    #Selection - Pega o item selecionado
    itemSelecionado = treeViewDados.selection()
    
    #for - para
    for item in itemSelecionado:
        
        #Quando ele encontrar o item na treeview ele deleta o item
        treeViewDados.delete(item)
        
    #Chamando a função que conta a quantidade de linhas
    contarNumeroLinhas()


botaoDeletar = Button(text="Deletar",
                       font = "Arial 20",
                       command = deletarItemTreeview)

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
botaoDeletar.grid(row=2, column=2, columnspan=2, stick="NSEW")

def alterarItemTreeview():
    
    #if - Se
    
    if str(campoDigitavelID.get()) == "":
        
        print("Digite algo no campo ID")
        
    elif str(campoDigitavelNome.get()) == "":
        
        print("Digite algo no campo Nome")
        
    elif str(campoDigitavelIdade.get()) == "":
        
        print("Digite algo no campo Idade")  
        
    elif str(campoDigitavelSexo.get()) == "":
        
        print("Digite algo no campo Sexo")
        
    else:
    
        #selection()[0] - Pega a posição do item selecionado
        itemSelecionado = treeViewDados.selection()[0]

        #Substituir o item selecionado
        treeViewDados.item(itemSelecionado,
                            values=(str(campoDigitavelID.get()),
                                    str(campoDigitavelNome.get()),
                                    str(campoDigitavelIdade.get()),
                                    str(campoDigitavelSexo.get())))

        #Limpando os campos
        campoDigitavelNome.delete(0, "end")
        campoDigitavelIdade.delete(0, "end")
        campoDigitavelSexo.delete(0, "end")
        campoDigitavelID.delete(0, "end")
    

botaoAlterar = Button(text="Alterar",
                       font = "Arial 20",
                       command = alterarItemTreeview)

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
botaoAlterar.grid(row=2, column=4, columnspan=2, stick="NSEW")

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()