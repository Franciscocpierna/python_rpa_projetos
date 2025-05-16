from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

#Abre o navegador da Web do Google Chrome
navegador = opcoesSelenium.Chrome()
navegador.get("https://rpachallengeocr.azurewebsites.net/")

#Copia o XPATH da tabela
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

#Pega Linhas e Colunas
linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

linha = 1
tempoEspera.sleep(3)
for linhaAtual in linhas:

    print(linhaAtual.text)
    linha = linha + 1
    

