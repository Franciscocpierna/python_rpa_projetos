from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

#Abre o navegador da Web do Google Chrome
navegador = opcoesSelenium.Chrome()
navegador.get("https://rpachallengeocr.azurewebsites.net/")



linha = 1

i = 1
#Enquanto o i for menor do que 4
while i < 4:

    #Copia o XPATH da tabela
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    #Pega Linhas e Colunas
    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

    #Para cada
    for linhaAtual in linhas:

        print(linhaAtual.text)
        linha = linha + 1
        
    i += 1
    #Aguarda 2 segundos para o computador ou site processar as informações
    tempoEspera.sleep(2)
    
    #Encontra o XPATH do botão Next e clica
    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    
    #Aguarda 2 segundos para o computador ou site processar as informações
    tempoEspera.sleep(2)
    
        
else:
    
    print("Pronto!")