numero = 1     

# Continua o loop enquanto 'numero' for menor que 5
while numero < 5:
    
    # Imprime o valor atual de 'numero'
    print(numero)
    
    # Incrementa 'numero' em 1 para a próxima iteração
    #numero = numero + 1
    numero += 1


    
"""
Explicação:

    Definindo Variável: A variável numero é inicializada com o valor 1.

    Loop While: A estrutura while cria um loop que continuará executando enquanto 
    a condição especificada for verdadeira. Neste caso, o loop continuará enquanto 
    numero for menor que 5.

    Corpo do Loop: Dentro do loop, há uma instrução de impressão que imprime o valor """
    
contador = 4

# Enquanto a variável contador for maior ou igual a 1, o loop continuará
while contador >= 1:
        
        # Imprime o valor atual da variável contador
        print(contador)  
        
        # Decrementa o valor da variável contador em 1
        #contador = contador - 1
        contador -= 1
        
        
print()
contador = 0

# Continua o loop enquanto 'contador' for menor que 10
while contador < 10:
    
    # Incrementa 'contador' em 1 a cada iteração do loop
    contador += 1
    
    # Imprime a string "Número " seguida do valor atual de 'contador'
    print("Número ", contador)
    
else:
    
    # Imprime esta mensagem após o término do loop
    print("Números impressos com sucesso!")
print("while cntador > 10")
print()
 
contador = 20
while (contador > 10):
    print(contador)
    contador -= 1
print("terminou o loop")    
    