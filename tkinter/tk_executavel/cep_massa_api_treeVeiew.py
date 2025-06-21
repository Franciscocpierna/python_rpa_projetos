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
janela.geometry("1050x850")

#grid - Divide a tela em grades / partes
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
instrucao = Label(text = "CEP: ", font = "Arial 40")
instrucao.grid(row = 1, column = 0, stick="W")

#Entry - Campo de entrada de dados
campoDigitavelCEP = Entry(font = "Arial 40")
campoDigitavelCEP.grid(row = 1, column = 1, stick="W")

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
    
    #Pega o CEP que digitamos para poder pesquisar
    cep = campoDigitavelCEP.get()
    
    #Aguarda 2 segundos par a computador processar as informações
    tempoEspera.sleep(2)
    
    #Imprime o CEP no campo do CEP no site
    navegador.find_element(By.NAME, "endereco").send_keys(cep)
    #navegador.find_element(By.ID, "endereco").send_keys(cep)
    #navegador.find_element(By.XPATH, '//*[@id="endereco"]').send_keys(cep)
    
    #Aguarda 3 segundos par a computador processar as informações
    tempoEspera.sleep(3)
    
    #Clica no botão de pesquisar para busca o endereço do CEP procurado
    navegador.find_element(By.NAME, "btn_pesquisar").click()
    
    #Aguarda 3 segundos par a computador processar as informações
    tempoEspera.sleep(3)
    
    #Pego a rua do site do busca através do XPATH
    rua = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
    lblRua.config(text = "Rua: " + rua)
    
    #Aguarda 1 segundos par a computador processar as informações
    tempoEspera.sleep(1)
    
    #Pego a bairro do site do busca através do XPATH
    bairro = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
    lblBairro.config(text = "Bairro: " + bairro)
    
    #Aguarda 1 segundos par a computador processar as informações
    tempoEspera.sleep(1)
    
    #Pego a cidade do site do busca através do XPATH
    cidade = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
    lblCidade.config(text = "Cidade: " + cidade)
    
    #Aguarda 1 segundos par a computador processar as informações
    tempoEspera.sleep(1)
    
    #Pego a cep do site do busca através do XPATH
    cep = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
    lblCEP.config(text = "CEP: " + cep)
    
    #Aguarda 3 segundos par a computador processar as informações
    tempoEspera.sleep(3)
    
    
    print("Pronto!")

botaoPesquisar = Button(text = "Pesquisar", font = "Arial 40",
                       command = pesquisaCEP)

#columnspan - Colocamos para dizer quantas colunas do grid o item vai oculpar
botaoPesquisar.grid(row = 2, column = 0, columnspan = 2, stick="NSEW")

lblRua = Label(text = "\nRua: -", font = "Arial 40")
lblRua.grid(row = 3, column = 0, columnspan = 2, stick="NSEW")

lblBairro = Label(text = "Bairro: -", font = "Arial 40")
lblBairro.grid(row = 4, column = 0, columnspan = 2, stick="NSEW")

lblCidade = Label(text = "Cidade: -", font = "Arial 40")
lblCidade.grid(row = 5, column = 0, columnspan = 2, stick="NSEW")

lblCEP = Label(text = "CEP: -", font = "Arial 40")
lblCEP.grid(row = 6, column = 0, columnspan = 2, stick="NSEW")

#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()
