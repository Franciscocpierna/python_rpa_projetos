#Configuramos o selenium e chrome

import pyautogui as tempoEspera
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()

janela.geometry("950x350")
janela.title("Treeview")

#grid - Divide a tela em grades / parte
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
cep = Label(text = "CEP: ", font = "Arial 20")
cep.grid(row = 1, column = 0, stick = "W")

#Campo para digitar a informação
campoDigitavelCEP = Entry(font = "Arial 20")
campoDigitavelCEP.grid(row = 1, column = 1, columnspan = 3, stick = "W")

#Função que pesquisa o CEP e extrai o endereço
def pesquisaCEP():
    
    cep = campoDigitavelCEP.get() 
    try:
      resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
      dados = resposta.json()
     # Verifica se ocorreu erro na resposta
      if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado.")
            return
 
      # Atualiza os labels com os dados retornados
      
      cep = dados.get('cep', '-')
      print(cep)
      rua =dados.get('logradouro', '-')
      print(rua)

      #Aguarda 1 segundos par a computador processar as informações
      tempoEspera.sleep(1)

      #Pego a bairro do site do busca através do XPATH
      bairro = dados.get('bairro', '-')
      print(bairro)

      #Aguarda 1 segundos par a computador processar as informações
      tempoEspera.sleep(1)
      #Pego a cidade do site do busca através do XPATH
      cidade = dados.get('localidade', '-')
      print(cidade)

      #Aguarda 1 segundos par a computador processar as informações
      tempoEspera.sleep(1)

      
      cep = dados.get('cep', '-')
      print(cep)

      #Aguarda 1 segundos par a computador processar as informações
      tempoEspera.sleep(1)
      
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    
    

    #Inserindo os dados do endereço na Treeview
    treeviewDados.insert("", "end",
                        values=(rua, bairro, cidade, cep))
    
    
print("Pronto!")
botao = Button(text = "PESQUISAR", font = "Arial 12",
              command = pesquisaCEP, 
              bg = "blue",
              fg = "white")

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
botao.grid(row = 1, column = 4, columnspan = 4, stick = "NSEW")

#theme_use - alt, default, classic
#Configurando o título e o stilo
configuracoesTreeview = ttk.Style()
configuracoesTreeview.theme_use("alt")
configuracoesTreeview.configure(".", font = ("Arial", 12))

#column - criando 4 colunas
treeviewDados = ttk.Treeview(janela, column = (1, 2, 3, 4), show = "headings")

treeviewDados.column("1", anchor=CENTER) #centralizo a coluna
treeviewDados.heading("1", text = "Rua") #Coloco o titulo da coluna

treeviewDados.column("2", anchor=CENTER)
treeviewDados.heading("2", text = "Bairro")

treeviewDados.column("3", anchor=CENTER)
treeviewDados.heading("3", text = "Cidade")

treeviewDados.column("4", anchor=CENTER)
treeviewDados.heading("4", text = "CEP")

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
treeviewDados.grid(row = 2, column = 0, columnspan = 8, stick = "NSEW")



#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()