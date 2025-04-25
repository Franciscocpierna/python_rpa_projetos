#Importamos o selenium para trabalhar com as páginas da web
from selenium import webdriver as opcoes_selenium_aula
from selenium.webdriver.common.keys import Keys

#Importando a biblioteca do pyautogui para trabalhar com o tempo e teclas teclado
import pyautogui as tempoPausaComputador

#Usando o By para trabalhar com as atualizações mais recentes
from selenium.webdriver.common.by import By

#Passamos autorização ao acesso as configurações do Chrome
meuNavegador = opcoes_selenium_aula.Chrome()
meuNavegador.get("https://www.google.com.br/")

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Procurando pelo elemento NAME e quando encontrar vou escrever Dolar hoje
meuNavegador.find_element(By.NAME, "q").send_keys("Dolar hoje")

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Retorna para o campo name q
#Faz a busca do valor que está digitado no campo NAME q
meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#No resultado da pesquisa pegamo o XPATH e no meios pegamos o primeiro elemento da lista
valorDolarPeloGoogle = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

print(valorDolarPeloGoogle)
#//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]
#//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]