from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By 
opcoes = Options()
opcoes.add_argument("--disable-blink-features=AutomationControlled")
opcoes.add_experimental_option("excludeSwitches", ["enable-automation"])
opcoes.add_experimental_option('useAutomationExtension', False)
 
navegador = webdriver.Chrome(options=opcoes)
navegador.get("https://www.google.com/")
time.sleep(3)
navegador.find_element("name", "q").send_keys("Dólar hoje", Keys.RETURN)
time.sleep(4)

#No resultado da pesquisa pegamo o XPATH e no meios pegamos o primeiro elemento da lista
valorDolarPeloGoogle = navegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

#Aguarda 4 segundo para dar tempo do computador processar as informações
time.sleep(4)

print(valorDolarPeloGoogle)

'''
A classe Options() no Selenium é usada para configurar opções específicas para o navegador antes de inicializá-lo. No caso do código fornecido, ela está sendo usada para personalizar o comportamento do navegador Chrome.

Aqui está o que cada configuração faz no seu código:

opcoes.add_argument("--disable-blink-features=AutomationControlled"):

Remove a detecção de automação do navegador, dificultando que sites detectem que o navegador está sendo controlado por um script.
opcoes.add_experimental_option("excludeSwitches", ["enable-automation"]):

Remove a mensagem "Chrome está sendo controlado por um software de automação" que aparece no navegador.
opcoes.add_experimental_option('useAutomationExtension', False):

Desativa a extensão de automação padrão do ChromeDriver, que também pode ser usada para detectar automação.
Essas configurações são úteis para evitar que sites detectem que o navegador está sendo controlado por um script automatizado, o que pode ser importante em tarefas de RPA (Automação de Processos Robóticos).
'''