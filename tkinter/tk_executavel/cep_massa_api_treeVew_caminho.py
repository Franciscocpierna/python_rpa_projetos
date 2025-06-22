#Configuramos o selenium e chrome

import pyautogui as tempoEspera
import requests
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog



#tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()

#Tamanho da tela
janela.geometry("800x300")
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

contador = 0
#Função que pesquisa o CEP e extrai o endereço
def pesquisaCEP():
    global contador
      
    
    
    #Caminho para abrir o arquivo de texto
    try:
        
        #Abre a caixa do dialog e permite selecionar o arquivo e retorna o caminho
        caminhoArquivo = filedialog.askopenfilename()
        
        #Imprimo o caminho no campo digitavel
        campoRecebeCaminhoArquivo.insert("insert", caminhoArquivo)
        
        #abrir o arquivo
        arquivo = open(caminhoArquivo)
        
        #ler os dados
        arquivoBlocoDeNotas = arquivo.readlines()
        
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")  

    #for - para
    for linha in arquivoBlocoDeNotas:
          
        #Remove a quebra de linhas
        linha = linha.rstrip("\n")
        #Pego o cep que está na linha corrente
        cepLinha = linha
        print("")
        print("")
        print("*"*50)
        #if - se
        if linha == "CEP":
            
            print(linha)
            
        else:
            try:
                contador += 1
                print(f"Contador = {contador}")  
                print("") 
                print("CEP:",cepLinha)
        
                resposta = requests.get(f"https://viacep.com.br/ws/{cepLinha}/json/")
                dados = resposta.json()
                
                    
                #Pego a rua do site do busca através do XPATH
                rua =dados.get('logradouro', '-')
                print(rua)

                #Aguarda 1 segundos par a computador processar as informações
                #tempoEspera.sleep(1)

                #Pego a bairro do site do busca através do XPATH
                bairro = dados.get('bairro', '-')
                print(bairro)

                #Aguarda 1 segundos par a computador processar as informações
                #tempoEspera.sleep(1)

                #Pego a cidade do site do busca através do XPATH
                cidade = dados.get('localidade', '-')
                print(cidade)

                #Aguarda 1 segundos par a computador processar as informações
                #tempoEspera.sleep(1)

                #Pego a cep do site do busca através do XPATH
                cep = dados.get('cep', '-')
                print(cep)

                #Aguarda 1 segundos par a computador processar as informações
                #tempoEspera.sleep(1)
                #Inserindo os dados do endereço na Treeview
                treeviewDados.insert("", "end",
                                values=(rua, bairro, cidade, cep)) 
                    
                
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
                    
        
           

            
   # treeviewDados.insert("", "end",
    #                            values=(contador))
    for _ in range(3):
      treeviewDados.insert('', 'end', values=("", "",  ""))  # Ajuste o número de colunas conforme necessário

    # Adiciona o contador
    #total_itens = len(treeviewDados.get_children())
    #treeviewDados.insert('', 'end', values=(f"Total de itens: {contador}", "", ""))  # Ajuste as colunas
    total_itens = len(treeviewDados.get_children()) - 3  # Subtrai as linhas vazias
    treeviewDados.insert('', 'end', values=("", "","", f"Total de itens: {total_itens}")) 
    # 
    #conforme necessário
    
    print("Pronto!")
    print("")
    
    print(f"Total Contador = {contador}")  
    print("") 
 
#bg - background / Cor do Fundo
#fg - foreground / Cord da Letra
botao = Button(text = "Selecionar", font = "Arial 12",
              command = pesquisaCEP, 
              bg = "blue",
              fg = "white")

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
botao.grid(row = 1, column = 7, columnspan = 4, stick = "NSEW")

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
treeviewDados.grid(row = 2, column = 0, columnspan = 11, stick = "NSEW")


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()