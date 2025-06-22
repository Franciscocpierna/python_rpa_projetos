#Configuramos o selenium e chrome
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as tempoEspera

from selenium.webdriver.common.by import By

options = opcoesSelenium.ChromeOptions()
options.add_argument("--healess")

#Selecionar um arquivo e imprimir os dados
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#tk - Biblioteca do Tkinter
#tk - Janela / Tela
janela = Tk()

#Tamanho da tela
janela.geometry("800x200")
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


#Função que pesquisa o CEP e extrai o endereço
def pesquisaCEP():
    
    #Abre a caixa do dialog e permite selecionar o arquivo e retorna o caminho
    caminhoArquivo = filedialog.askopenfilename()
    
    #Imprimo o caminho no campo digitavel
    campoRecebeCaminhoArquivo.insert("insert", caminhoArquivo)
    
    #abrir o arquivo
    arquivo = open(caminhoArquivo)
    
    #ler os dados
    arquivoBlocoDeNotas = arquivo.readlines()
    
    
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
    
    #Aguarda 2 segundos par a computador processar as informações
    tempoEspera.sleep(2)
    
    #Clica no botão de pesquisar para busca o endereço do CEP procurado
    navegador.find_element(By.NAME, "btn_pesquisar").click()
    
    #Aguarda 3 segundos par a computador processar as informações
    tempoEspera.sleep(3)
    
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
        

#bg - background / Cor do Fundo
#fg - foreground / Cord da Letra
botao = Button(text = "Selecionar", font = "Arial 12",
              command = pesquisaCEP, 
              bg = "blue",
              fg = "white")

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
botao.grid(row = 1, column = 7, columnspan = 4, stick = "NSEW")


#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()