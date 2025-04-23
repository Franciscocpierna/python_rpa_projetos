import pyautogui as posicaoMouse
posicaoMouse.sleep(2)  # Espera 2 segundos para o usuário se preparar

#parte comentada abre o adobe reader
'''posicaoMouse.moveTo(x=27, y=749)  # Move o mouse para a posição (27, 749)
posicaoMouse.click(x=27, y=749)  # Clica na posição atual do mouse
posicaoMouse.sleep(4) # Espera 2 segundos
#posicaoMouse.typewrite('excel')  # Digita "Olá, mundo!" na posição atual do mouse
posicaoMouse.moveTo(x=148, y=265)  # Move o mouse para a posição (148, 265)
posicaoMouse.sleep(2)  # Espera 2 segundos
posicaoMouse.click(x=148, y=265)  # Clica na posição (148, 265) abre adobe
'''
# abre a calculadora do windows na barra de tarefas
print(posicaoMouse.position())  # Imprime a posição atual do mouse
posicaoMouse.moveTo(x=404, y=745)
posicaoMouse.sleep(2)  # Espera 2 segundos
posicaoMouse.click(x=404, y=745)  # Clica na posição (404, 745) abre calculadora