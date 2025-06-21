#Criando tela e exportando o endereço para o Treeview
#Configuramos o selenium e chrome
from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui as tempoEspera

from selenium.webdriver.common.by import By

options = opcoesSelenium.ChromeOptions()
options.add_argument("--healess")


from tkinter import *
from tkinter import ttk

#tk - Biblioteca do Tkinter
#tk - Janela / Tela
janela = Tk()

#Tamanho da tela
janela.geometry("950x350")
janela.title("Treeview")

#grid - Divide a tela em grades / parte
#stick - Usamos para preecher o item na tela ou seja
#stick - Esticamos o item para não ficar espaço vazio nas laterais
#stick - Norte, Sul, Leste e Oeste - (NSEW)
cep = Label(text = "CEP: ", font = "Arial 20")
cep.grid(row = 1, column = 0, stick = "W")

#Campo para digitar a informação
campoDigitavelCEP = Entry(font = "Arial 20")
campoDigitavelCEP.grid(row = 1, column = 1, columnspan = 3, stick = "W")


#Criando a função que busca o CEP
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
    
    #Aguarda 1 segundos par a computador processar as informações
    tempoEspera.sleep(1)
    
    #Pego a bairro do site do busca através do XPATH
    bairro = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]')[0].text
    
    #Aguarda 1 segundos par a computador processar as informações
    tempoEspera.sleep(1)
    
    #Pego a cidade do site do busca através do XPATH
    cidade = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]')[0].text
    
    #Aguarda 1 segundos par a computador processar as informações
    tempoEspera.sleep(1)
    
    #Pego a cep do site do busca através do XPATH
    cep = navegador.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
    
    #Aguarda 3 segundos par a computador processar as informações
    tempoEspera.sleep(3)
    
    #Inserindo os dados do endereço na Treeview
    treeviewDados.insert("", "end",
                        values=(rua, bairro, cidade, cep))
    
    
    print("Pronto!")


#bg - background / Cor do Fundo
#fg - foreground / Cord da Letra
botao = Button(text = "PESQUISAR", font = "Arial 12",
              command = pesquisaCEP, 
              bg = "blue",
              fg = "white")

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
botao.grid(row = 1, column = 4, columnspan = 4, stick = "NSEW")

#theme_use - alt, default, classic
#Configurando o título e o stilo
configuracoesTreeview = ttk.Style()
configuracoesTreeview.theme_use("alt")
configuracoesTreeview.configure(".", font = ("Arial", 12))

#column - criando 4 colunas
treeviewDados = ttk.Treeview(janela, column = (1, 2, 3, 4), show = "headings")

treeviewDados.column("1", anchor=CENTER) #centralizo a coluna
treeviewDados.heading("1", text = "Rua") #Coloco o titulo da coluna

treeviewDados.column("2", anchor=CENTER)
treeviewDados.heading("2", text = "Bairro")

treeviewDados.column("3", anchor=CENTER)
treeviewDados.heading("3", text = "Cidade")

treeviewDados.column("4", anchor=CENTER)
treeviewDados.heading("4", text = "CEP")

#columnspan - É a quantidade de colunas que o nosso campo vai oculpar na tela
treeviewDados.grid(row = 2, column = 0, columnspan = 8, stick = "NSEW")



#mainloop - Looping infinito, a janela do Python mostra um programa em funcionamento
janela.mainloop()