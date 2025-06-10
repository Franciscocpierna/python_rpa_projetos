from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
import pyautogui as tempoEspera

from selenium.webdriver.common.by import By

#Abre o navegador do Google Chrome
navegador = opcoesSelenium.Chrome()
navegador.get("https://rpachallenge.com/")

#Aguarda 3 segundos para dar tempo do computador processar informações
tempoEspera.sleep(3)

#Localiza o First Name e envia o texto 
#//*[]
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys("Cristina")

#Aguarda 2 segundos para dar tempo do computador processar informações
tempoEspera.sleep(2)

#Localiza o LastName e envia o texto 
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys("Silva")

#Aguarda 2 segundos para dar tempo do computador processar informações
tempoEspera.sleep(2)

#Localiza o CompanyName e envia o texto 
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys("Cursos Online")

#Aguarda 2 segundos para dar tempo do computador processar informações
tempoEspera.sleep(2)

#Localiza o Role / Função e envia o texto 
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys("Gerente Sênior")

#Aguarda 2 segundos para dar tempo do computador processar informações
tempoEspera.sleep(2)

#Localiza o Address / Endereço e envia o texto 
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys("Rua Alvarez de Souza 50")

#Aguarda 2 segundos para dar tempo do computador processar informações
tempoEspera.sleep(2)

#Localiza o Email e envia o texto 
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys("cristina@gmail.com")

#Aguarda 2 segundos para dar tempo do computador processar informações
tempoEspera.sleep(2)

#Localiza o Phone / Telefone e envia o texto 
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys("91111 - 1111")

#Aguarda 2 segundos para dar tempo do computador processar informações
tempoEspera.sleep(2)

#Clicando no botão para enviar as informações preenchidas
navegador.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

print("Dados enviados com sucesso!")