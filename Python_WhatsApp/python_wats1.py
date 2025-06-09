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

imagem = "C:\\python_projetos\\python_rpa_projetos\\Python_WhatsApp\\watsapp\\Boa_Noite.jpg"

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
    
    #Seletores CSS são usados para identificar um elemento que não possuem ID ou Nome
    #Estamos obtendo todos as tags span com o atributo data-icon com o "clip" dentro do valor
    navegadorChrome.find_elements(By.CSS_SELECTOR, "span[data-icon='clip']")
    
    #Aguarda 2 segundos para dar tempo do site processas as informações 
    tempoEspera.sleep(2)
    
    #Clico no icone do clip
    navegadorChrome.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
    
    #Clico no icone de imagens
    #Estamos obtendo todos as tags span com o atributo input com o "file" dentro do valor
    opcoesArquivosExternos = navegadorChrome.find_element(By.CSS_SELECTOR, "input[type='file']")
    
    #Aguarda 1 segundos para dar tempo do site processas as informações 
    tempoEspera.sleep(1)
    
    #Envia a imagem do computador para o WhatsApp WEB
    opcoesArquivosExternos.send_keys(imagem)
    
    #Aguarda 3 segundos para dar tempo do site processas as informações 
    tempoEspera.sleep(3)
    
    #Busca pelo XPATH o campo onde escreve a mensagem e envia
    navegadorChrome.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]').send_keys(mensagemContato)
    
    #Aguarda 3 segundos para dar tempo do site processas as informações 
    tempoEspera.sleep(3)
    
    #Apertar a tecla enter do teclado para enviar a mensagem
    teclasTeclado.press('enter')
    
    #Aguarda 3 segundos para dar tempo do site processas as informações 
    tempoEspera.sleep(3)
