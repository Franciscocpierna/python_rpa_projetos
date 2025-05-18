#Mercado Livre

from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

#Abre o navegador da Web do Google Chrome
navegador = opcoesSelenium.Chrome()
navegador.get("https://www.mercadolivre.com.br/")

#Procura o campo Name, digita a palavra que queremos procurar e cola
#navegador.find_element(By.NAME, "as_word").send_keys("carteira")
tempoEspera.sleep(2)
navegador.find_element(By.NAME, "as_word").send_keys("carteira" + Keys.ENTER)
#Aguarda 2 segundos
#tempoEspera.sleep(2)

#Procura o botão com o XPATH e clica no botão para pesquisar
#navegador.find_element(By.XPATH, "/html/body/header/div/form/button").click()
#navegador.find_element(By.XPATH, "/html/body/header/div/div[2]/form/button[2]").click()



#Aguarda 6 segundos
tempoEspera.sleep(6)

dadosProduto = navegador.find_elements(By.CLASS_NAME, "ui-search-layout__item")


linha = 2
for informacoes in dadosProduto:
   
    nomeProduto = informacoes.find_element(By.CLASS_NAME, "poly-component__title").text
    
    
    #precoProduto = informacoes.find_element(By.CLASS_NAME, "price-tag-fraction").text
    #precoProduto = informacoes.find_element(By.CLASS_NAME, "poly-component__price").text
    precoProduto = informacoes.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
    
    
    try:
        centavosProduto = informacoes.find_element(By.CLASS_NAME, "price-tag-cents").text
    except:
        centavosProduto = "0"
    
    urlProduto = informacoes.find_element(By.TAG_NAME, "a").get_attribute("href")
    
    print(nomeProduto + " - " + precoProduto + "," + centavosProduto + " - " + urlProduto)
    
   