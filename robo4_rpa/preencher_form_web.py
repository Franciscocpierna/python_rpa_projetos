# Importa a classe 'webdriver' do módulo 'selenium' e a renomeia para 'opcoesSelenium'.
# Isso é útil para controlar navegadores de forma programática.
from selenium import webdriver as opcoesSelenium

# Importa a classe 'By' do módulo 'selenium.webdriver.common.by'.
# 'By' é usado para definir os métodos de localização de elementos em uma página web.
from selenium.webdriver.common.by import By

# Importa a classe 'Keys' do módulo 'selenium.webdriver.common.keys'.
# 'Keys' é usado para enviar comandos do teclado, como Enter, Escape, etc.
from selenium.webdriver.common.keys import Keys

# Importa o módulo 'pyautogui' e o renomeia para 'tempoEspera'.
# 'pyautogui' é uma biblioteca para automação de interface gráfica do usuário, aqui usada para criar pausas.
import pyautogui as tempoEspera

# Inicializa uma instância do navegador Chrome e a atribui à variável 'navegadorFormulario'.
navegadorFormulario = opcoesSelenium.Chrome()

# Navega para a URL especificada.
navegadorFormulario.get("https://pt.surveymonkey.com/r/WLXYDX2")


# Pausa a execução do script por 6 segundos para permitir
# que a página seja carregada completamente.
tempoEspera.sleep(6)

# Localiza um elemento no navegador pelo seu nome ('name') e o atribui à variável 'nome'.
nome = navegadorFormulario.find_element(By.NAME, "166517069")

# Pausa a execução do script por 1 segundo após preencher o campo.
tempoEspera.sleep(1)

# Envia o texto 'Amanda Martins' para o campo identificado acima.
nome.send_keys("Eduardo Borges Alves")

# Pausa a execução do script por 1 segundo após preencher o campo.
tempoEspera.sleep(1)


# --------------


# Similar ao anterior, localiza o campo de e-mail pelo NAME e atribui à variável 'email'.
email = navegadorFormulario.find_element(By.NAME, "166517072")

# Pausa a execução do script por 1 segundo.
tempoEspera.sleep(1)

# Envia o texto 'amanda.martins2024@gmail.com' para o campo de e-mail.
email.send_keys("edu.b_alves@gmail.com")

# Pausa a execução do script por 1 segundo.
tempoEspera.sleep(1)


# --------------


# Localiza o campo de telefone pelo nome e atribui à variável 'telefone'.
telefone = navegadorFormulario.find_element(By.NAME, "166517070")

# Pausa a execução do script por 1 segundo.
tempoEspera.sleep(1)

# Envia o número de telefone para o campo correspondente.
telefone.send_keys("(99) 6666 - 5555")

# Pausa a execução do script por 1 segundo.
tempoEspera.sleep(1)


# --------------


# Localiza o campo 'Sobre' pelo nome e atribui à variável 'sobre'.
sobre = navegadorFormulario.find_element(By.NAME, "166517073")

# Pausa a execução do script por 1 segundo.
tempoEspera.sleep(1)

# Envia o texto 'Sei automatizar processos e planilhas com Python' para o campo 'Sobre'.
sobre.send_keys("Sei automatizar processos e planilhas com Python")

# Pausa a execução do script por 1 segundo.
tempoEspera.sleep(1)

# Localiza um botão de rádio pelo seu ID e o atribui à variável 'radio_button'.
radio_button = navegadorFormulario.find_element(By.ID, "166517071_1215509813_label")

# Pausa a execução do script por 1 segundo.
tempoEspera.sleep(1)

# Clica no botão de rádio.
radio_button.click()

# Pausa a execução do script por 2 segundos.
tempoEspera.sleep(2)

# Localiza o botão de envio do formulário pelo seu XPath e o atribui à variável 'enviar'.
enviar = navegadorFormulario.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button')

# Clica no botão de envio do formulário.
# enviar.click()