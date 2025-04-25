import pyautogui as posicaoAbrirGoogle

#Tempo de espera para o computador pensar
posicaoAbrirGoogle.sleep(4)

posicaoAbrirGoogle.doubleClick(x=1258, y=20) #minimiza a janela dev
posicaoAbrirGoogle.sleep(2)
 
#https://www.google.com/
# Dolar hoje
# no botão Start ou seja no botão do Windows

posicaoAbrirGoogle.hotkey('win', 'r')
posicaoAbrirGoogle.sleep(2)
#posicaoAbrirGoogle.doubleClick(x=187, y=526) # clica no google abrindo a janela do google
posicaoAbrirGoogle.typewrite('chrome')
posicaoAbrirGoogle.sleep(2)

posicaoAbrirGoogle.press('enter')

#Tempo de espera para o computador pensar
posicaoAbrirGoogle.sleep(4)

#Digitamos o site do google
posicaoAbrirGoogle.typewrite('https://www.google.com/') # digitamos o site do google
posicaoAbrirGoogle.sleep(3)
posicaoAbrirGoogle.press('enter')
posicaoAbrirGoogle.sleep(3)
#posicaoAbrirGoogle.click(x=1236, y=152) # maximiza a janela do google
#as tres linhas de baixo são para maximizar a janela do google
posicaoAbrirGoogle.hotkey('alt', 'space')  # Abre o menu da janela
posicaoAbrirGoogle.sleep(3)
posicaoAbrirGoogle.press('x')  # Seleciona a opção de maximizar

#Tempo de espera para o computador pensar
posicaoAbrirGoogle.sleep(4)

#Apertamos a tecla enter
posicaoAbrirGoogle.press('enter')

#Tempo de espera para o computador pensar
posicaoAbrirGoogle.sleep(7)

#Digitamos o site do google
posicaoAbrirGoogle.typewrite('Dolar hoje') # pesquisando o dolar hoje

#Tempo de espera para o computador https://www.google.com/

posicaoAbrirGoogle.sleep(3)

#Apertamos a tecla enter
posicaoAbrirGoogle.press('enter') # apertamos enter para pesquisar o dolar hoje

posicaoAbrirGoogle.sleep(2)
posicaoAbrirGoogle.doubleClick(x=321, y=344) # clica no dolar primeiro site


#as tres linhas de baixo são para fechar a janela do google
posicaoAbrirGoogle.sleep(7)
posicaoAbrirGoogle.hotkey('alt', 'space')  # Abre o menu da janela
posicaoAbrirGoogle.sleep(3)
posicaoAbrirGoogle.press('f')  # Seleciona a opção de maximizar

posicaoAbrirGoogle.sleep(3)
posicaoAbrirGoogle.click(x=803, y=748)

#print(posicaoAbrirGoogle.position())
