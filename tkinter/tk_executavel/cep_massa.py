#Configuramos o selenium e chrome
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as tempoEspera

from selenium.webdriver.common.by import By

options = opcoesSelenium.ChromeOptions()
options.add_argument("--healess")

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


#Função que pesquisa o CEP e extrai o endereço
def pesquisaCEP():
    
    #Instanciando da classe Options para configurar o headless Chrome
    options = Options()
    
    #False - VISIVEL - que vemos a tela do Chrome trabalhando
    #True - OCULTO - que não vemos a tela do Chrome
    options.headless = True
    
    #Inicializa
    navegador = opcoesSelenium.Chrome(options = options)
    
    #Aguarda 1 segundo par a computador processar as informações
    tempoEspera.sleep(1)
    
    navegador.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

    #Aguarda 3 segundos par a computador processar as informações
    tempoEspera.sleep(3)
    
    #Imprime o CEP no campo do CEP no site
    navegador.find_element(By.NAME, "endereco").send_keys("23548057")
    #navegador.find_element(By.ID, "endereco").send_keys(cep)
    #navegador.find_element(By.XPATH, '//*[@id="endereco"]').send_keys(cep)
    
    #Aguarda 3 segundos par a computador processar as informações
    tempoEspera.sleep(3)
    
    #Clica no botão de pesquisar para busca o endereço do CEP procurado
    navegador.find_element(By.NAME, "btn_pesquisar").click()
    
    #Aguarda 3 segundos par a computador processar as informações
    tempoEspera.sleep(3)
    
    #Caminho para abrir o arquivo de texto
    arquivo = open("C:\\Users\\55119\\Desktop\\TKinter Arquivos\\CEP.txt")
    arquivoBlocoDeNotas = arquivo.readlines()

    #for - para
    for linha in arquivoBlocoDeNotas:

        #Remove a quebra de linhas
        linha = linha.rstrip("\n")
        
        #if - se
        if linha == "CEP":
            
            print(linha)
            
        else:
            
            #Aguarda 3 segundos par a computador processar as informações
            tempoEspera.sleep(3)
            
            #Clica no botão para volta e poder fazer uma nova busca
            navegador.find_element(By.ID, "btn_nbusca").click()
            
            #-------------------------------------------------------
            
            #Aguarda 3 segundos par a computador processar as informações
            tempoEspera.sleep(3)
            
            #Pego o cep que está na linha corrente
            cepLinha = linha

            #Imprime o CEP no campo do CEP no site
            navegador.find_element(By.NAME, "endereco").send_keys(cepLinha)
            #navegador.find_element(By.ID, "endereco").send_keys(cep)
            #navegador.find_element(By.XPATH, '//*[@id="endereco"]').send_keys(cep)

            #Aguarda 3 segundos par a computador processar as informações
            tempoEspera.sleep(3)

            #Clica no botão de pesquisar para busca o endereço do CEP
            navegador.find_element(By.NAME, "btn_pesquisar").click()

            #Aguarda 3 segundos par a computador processar as informações
            tempoEspera.sleep(3)
    
            #Pego a rua do site do busca através do XPATH
            rua = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
            print(rua)

            #Aguarda 1 segundos par a computador processar as informações
            tempoEspera.sleep(1)

            #Pego a bairro do site do busca através do XPATH
            bairro = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
            print(bairro)

            #Aguarda 1 segundos par a computador processar as informações
            tempoEspera.sleep(1)

            #Pego a cidade do site do busca através do XPATH
            cidade = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
            print(cidade)

            #Aguarda 1 segundos par a computador processar as informações
            tempoEspera.sleep(1)

            #Pego a cep do site do busca através do XPATH
            cep = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
            print(cep)

            #Aguarda 1 segundos par a computador processar as informações
            tempoEspera.sleep(1)
    
    print("Pronto!")
    

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
