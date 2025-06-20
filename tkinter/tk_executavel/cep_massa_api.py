#Configuramos o selenium e chrome

import pyautogui as tempoEspera
import requests
from tkinter import *
from tkinter import messagebox

#tk - Biblioteca do tkinter
#Tk - Janela / Tela
janela = Tk()

#Tamanho da tela
janela.geometry("1200x650")

#grid - Divide a tela em grades / partes
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
instrucao = Label(text = "Clique no botão para pesquisar: ", font = "Arial 40")
instrucao.grid(row = 1, column = 0, stick="W")

contador = 0
#Função que pesquisa o CEP e extrai o endereço
def pesquisaCEP():
    global contador
    contador += 1
    print(f"Contador = {contador}")  
    
    # Obtem o CEP digitado e remove espaços
    cep = "23548057"  # Exemplo de CEP fixo 
    #Caminho para abrir o arquivo de texto
    try:
      resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
      dados = resposta.json()
     # Verifica se ocorreu erro na resposta
      if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado.")
            return
 
      # Atualiza os labels com os dados retornados
      #Pego a rua do site do busca através do XPATH
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

      #Pego a cep do site do busca através do XPATH
      cep = dados.get('cep', '-')
      print(cep)

      #Aguarda 1 segundos par a computador processar as informações
      tempoEspera.sleep(1)
      
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    
    try:
      arquivo = open("C:\\python_projetos\\python_rpa_projetos\\tkinter\\tk_executavel\\CEP.txt")
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

                #Pego a cep do site do busca através do XPATH
                cep = dados.get('cep', '-')
                print(cep)

                #Aguarda 1 segundos par a computador processar as informações
                tempoEspera.sleep(1)
                     
                
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
                    
        
           

            
    
    print("Pronto!")
    print("")
    
    print(f"Total Contador = {contador}")  
    print("") 

#bg - Background cor do fundo
#fg - Cor da letra
botaoPesquisar = Button(text = "Pesquisar", font = "Arial 40",
                        bg= "blue",
                        fg = "white",
                        command = pesquisaCEP)

#columnspan - Colocamos para dizer quantas colunas do grid o item vai oculpar
botaoPesquisar.grid(row = 2, column = 0, columnspan = 2, stick="NSEW")




#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()
