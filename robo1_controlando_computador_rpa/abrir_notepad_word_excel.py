import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm('Clique no botão desejado', buttons = ['Excel', 'Word', "Notepad"])

if opcao == "Excel":
    
    #O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
    #Nesse caso é a mesma coisa que precionar Windows + R
    escolha_opcao.hotkey('win', 'r')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    #Digitamos a palavra Excel
    escolha_opcao.typewrite('Excel')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    #Precionamos a tecla Enter
    escolha_opcao.press('Enter')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(4)
    
    #CLiquei na opção para abrir um excel em branco
    escolha_opcao.click(x=600, y=241)
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(3)
    
    escolha_opcao.typewrite('Escolhi abrir o Excel')
    
    #procedimento para fechar janela aplicativo ativo 
    escolha_opcao.sleep(7)
    escolha_opcao.hotkey('alt', 'space')  # Abre o menu da janela menu
    escolha_opcao.sleep(3)
    escolha_opcao.press('f')  # fecha a janela ativa
    escolha_opcao.sleep(2)

    #Precionamos a tecla TAB
    escolha_opcao.press('tab')


    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)

    #Apertamos a tecla enter
    escolha_opcao.press('enter')    
    
    
elif opcao == "Word":
    
    #O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
    #Nesse caso é a mesma coisa que precionar Windows + R
    escolha_opcao.hotkey('win', 'r')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    #Digitamos a palavra Excel
    escolha_opcao.typewrite('winword')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    #Precionamos a tecla Enter
    escolha_opcao.press('Enter')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(6)
    
    #CLiquei na opção para abrir um excel em branco
    escolha_opcao.click(x=447, y=334)
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(5)
    
    escolha_opcao.typewrite('Escolhi abrir o Word')
    
    #procedimento para fechar janela aplicativo ativo 
    escolha_opcao.sleep(7)
    escolha_opcao.hotkey('alt', 'space')  # Abre o menu da janela menu
    escolha_opcao.sleep(3)
    escolha_opcao.press('f')  # fecha a janela ativa
    escolha_opcao.sleep(2)

    #Precionamos a tecla TAB
    escolha_opcao.press('tab')


    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)

    #Apertamos a tecla enter
    escolha_opcao.press('enter')    
    
elif opcao == "Notepad":
    
    #O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
    #Nesse caso é a mesma coisa que precionar Windows + R
    escolha_opcao.hotkey('win', 'r')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    #Digitamos a palavra Excel
    escolha_opcao.typewrite('Notepad')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)
    
    #Precionamos a tecla Enter
    escolha_opcao.press('Enter')
    
    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(4)
    
    escolha_opcao.typewrite('Escolhi abrir o notepad')
    
    #procedimento para fechar janela aplicativo ativo 
    escolha_opcao.sleep(7)
    escolha_opcao.hotkey('alt', 'space')  # Abre o menu da janela menu
    escolha_opcao.sleep(3)
    escolha_opcao.press('f')  # fecha a janela ativa
    escolha_opcao.sleep(2)

    #Precionamos a tecla TAB
    escolha_opcao.press('tab')


    #Tempo de espera para o computador pensar
    escolha_opcao.sleep(2)

    #Apertamos a tecla enter
    escolha_opcao.press('enter')    
    #print(escolha_opcao.position())
