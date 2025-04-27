#Importamos o selenium para trabalhar com as páginas da web
from selenium.webdriver.chrome.options import Options
from selenium import webdriver as opcoes_selenium_aula
from selenium.webdriver.common.keys import Keys

#Importando a biblioteca do pyautogui para trabalhar com o tempo e teclas teclado
import pyautogui as tempoPausaComputador

#Usando o pyautogui para controlar as teclas do teclado
import pyautogui as teclasAtalhoTeclado

#Usando o By para trabalhar com as atualizações mais recentes
from selenium.webdriver.common.by import By
# configurando o Chrome para não ser detectado como um robô
opcoes = Options()
opcoes.add_argument("--disable-blink-features=AutomationControlled")
opcoes.add_experimental_option("excludeSwitches", ["enable-automation"])
opcoes.add_experimental_option('useAutomationExtension', False)
meuNavegador = opcoes_selenium_aula.Chrome(options=opcoes)
#
#Passamos autorização ao acesso as configurações do Chrome
#meuNavegador = opcoes_selenium_aula.Chrome()
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

#-----------------------------------------------------------------

#Aguarda 2 segundo para dar tempo do computador processar as informações
#tempoPausaComputador.sleep(2)

#Retorna para o campo name q
#Faz a busca do valor que está digitado no campo NAME q
#meuNavegador.find_element(By.NAME, "q").send_keys("")

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Estamos usando o pyautogui para apertar a tecla TAB
#teclasAtalhoTeclado.press('tab') 
# Limpa o campo de pesquisa diretamente
meuNavegador.find_element(By.NAME, "q").clear()

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Estamos usando o pyautogui para apertar a tecla enter
#Enter para limpar o campo de pesquisa
#teclasAtalhoTeclado.press('enter')

#Aguarda 4 segundo para dar tempo do computador processar as informações
#tempoPausaComputador.sleep(4)

#Procurando pelo elemento NAME e quando encontrar vou escrever Dolar hoje
meuNavegador.find_element(By.NAME, "q").send_keys("Euro")

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#Retorna para o campo name q
#Faz a busca do valor que está digitado no campo NAME q
meuNavegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

#No resultado da pesquisa pegamo o XPATH e no meios pegamos o primeiro elemento da lista
valorEuroPeloGoogle = meuNavegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text

#Aguarda 4 segundo para dar tempo do computador processar as informações
tempoPausaComputador.sleep(4)

print(valorEuroPeloGoogle)

#-------------------------------------

#import xlsxwriter
import os
import xlwt

nomeCaminhoArquivo = "C:\\python_projetos\\python_rpa_projetos\\robo2_rpa\\Dolar+e+Euro+Google.xls"

#planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)
#sheet1 = planilhaCriada.add_worksheet()
# Criando o arquivo Excel
planilhaCriada = xlwt.Workbook()
sheet1 = planilhaCriada.add_sheet("Dados")


#Escrevendo nas células
#sheet1.write("A1", "Dolar")
#sheet1.write("B1", "Euro")
#sheet1.write("A2", valorDolarPeloGoogle)
#sheet1.write("B2", valorEuroPeloGoogle)
#
# Escrevendo nas células
sheet1.write(0, 0, "Dolar")  # Linha 0, Coluna 0
sheet1.write(0, 1, "Euro")  # Linha 0, Coluna 1
sheet1.write(1, 0, valorDolarPeloGoogle)  # Linha 1, Coluna 0
sheet1.write(1, 1, valorEuroPeloGoogle)  # Linha 1, Coluna 1


#

#Substituir a vírgula por ponto deixando 5,38 para 5.38
valorDolarPeloGoogle = valorDolarPeloGoogle.replace(',','.')
valorEuroPeloGoogle = valorEuroPeloGoogle.replace(',','.')

#Convertendo o valor do Dolar e Euro de String para Float
valor_Dolar_Tipo_Float = float(valorDolarPeloGoogle)
Valor_Euro_Tipo_Float = float(valorEuroPeloGoogle)

sheet1.write(2, 0, valor_Dolar_Tipo_Float)
sheet1.write(2, 1, Valor_Euro_Tipo_Float)
print(valor_Dolar_Tipo_Float)
print(Valor_Euro_Tipo_Float)        
#Fechando o arquivo do Excel que está em segundo plano
#planilhaCriada.close() 
planilhaCriada.save(nomeCaminhoArquivo)


#Abro o arquivo
os.startfile(nomeCaminhoArquivo)



# Caminho do arquivo Excel
#