#Importanto as bibliotecas do selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Importanto as bibliotecas do pyautogui
import pyautogui as tempoEspera
import pyautogui as teclasTeclado

#By para trabalhar com os computadores mais recentes
from selenium.webdriver.common.by import By

#Importanto a biblioteca do openpyxl para trabalhar com o Excel
from openpyxl import load_workbook

#Pegamos o caminho do arquivo + nome do arquivo que está no computador
nome_arquivo_contatos = "C:\\python_projetos\\python_rpa_projetos\\Python_WhatsApp\\watsapp\\Contatos.xlsx"
planilhaDadosContato = load_workbook(nome_arquivo_contatos)

#Selecionamos a sheet de Dados
sheet_selecionada = planilhaDadosContato['Dados']

#Emulando o navegador do Chrome
navegadorChrome = webdriver.Chrome()

#Passando e abrindo a pagina da web que devemos abrir
navegadorChrome.get("https://web.whatsapp.com/")

#Aguarda até encontrar o ID side
#Enquanto o tamanho da lista for menor do que 1 fica tentando logar
while len(navegadorChrome.find_elements(By.ID, 'side')) < 1:
    #Aguarda 3 segundos para ver se o Whatsapp Web logou
    tempoEspera.sleep(3)
    
#Aguarda 3 segundos para dar tempo do site processas as informações 
tempoEspera.sleep(3)

#For = Para
for linha in range(2, len(sheet_selecionada['A']) + 1):
    
    #Criamos as variaveis nome e mensagem
    nomeContato = sheet_selecionada['A%s' % linha].value
    mensagemContato = sheet_selecionada['B%s' % linha].value
    
    #Busca pelo XPATH e escreve o nomeContato no campo pesquisa do WhatsApp Web
    navegadorChrome.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]').send_keys(nomeContato)
    
    #Aguarda 3 segundos para dar tempo do site processas as informações 
    tempoEspera.sleep(3)
    
    #Apertar a tecla enter do teclado
    teclasTeclado.press('enter')
    
    #Aguarda 3 segundos para dar tempo do site processas as informações 
    tempoEspera.sleep(3)
    
    #Busca pelo XPATH o campo onde escreve a mensagem e envia
    navegadorChrome.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(mensagemContato)
    
    #Aguarda 3 segundos para dar tempo do site processas as informações 
    tempoEspera.sleep(3)
    
    #Apertar a tecla enter do teclado para enviar a mensagem
    teclasTeclado.press('enter')
    
    #Aguarda 3 segundos para dar tempo do site processas as informações 
    tempoEspera.sleep(3)