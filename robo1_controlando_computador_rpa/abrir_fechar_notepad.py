import pyautogui as posicaoAbreArquivos

#O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
#Nesse caso é a mesma coisa que precionar Windows + R
posicaoAbreArquivos.hotkey('win', 'r')

#Tempo de espera para o computador pensar
posicaoAbreArquivos.sleep(2)

#Digitamos a palavra Notepad
posicaoAbreArquivos.typewrite('notepad')

#Tempo de espera para o computador pensar
posicaoAbreArquivos.sleep(2)

#Apertamos a tecla enter
posicaoAbreArquivos.press('enter')

#Tempo de espera para o computador pensar
posicaoAbreArquivos.sleep(3)

#Digitamos a frase
posicaoAbreArquivos.typewrite('Abrimos o Notepad com um robô ou Script')

#Tempo de espera para o computador pensar
posicaoAbreArquivos.sleep(2)

#O getActive Windows permite pega a janela que está ativa
fecharJanelaNotepad = posicaoAbreArquivos.getActiveWindow()

#Tempo de espera para o computador pensar
posicaoAbreArquivos.sleep(2)

#Aciona para fechar a janela ativa
fecharJanelaNotepad.close()

#Tempo de espera para o computador pensar
posicaoAbreArquivos.sleep(2)

#Precionamos a tecla TAB
posicaoAbreArquivos.press('tab')


#Tempo de espera para o computador pensar
posicaoAbreArquivos.sleep(2)

#Apertamos a tecla enter
posicaoAbreArquivos.press('enter')