#While Usando uma Condição Complexa

# Definindo dois números secretos
numero_secreto1 = 7
numero_secreto2 = 3

# Definindo o número de tentativas
tentativas = 5

# Variáveis para rastrear se os números foram adivinhados
adivinhou1 = False
adivinhou2 = False

# O loop continuará enquanto ambas as condições forem verdadeiras: 
#tentativas restantes e pelo menos um número não adivinhado
while tentativas > 0 and (not adivinhou1 == True or not adivinhou2 == True):
    
    print(f"Tentantivas restantes: {tentativas}")
    
    palpite1 = int(input("Adivinhe o primeiro número secreto (1-10): "))
    palpite2 = int(input("Adivinhe o segundo número secreto (1-10): "))
    
    # Se palpite1 é igual ao numero_secreto1 imprime a mensagem
    if palpite1 == numero_secreto1:
        
        print("Você adivinhou o primeiro número!")
        
        adivinhou1 = True
        
    # Se palpite1 é igual ao numero_secreto1 imprime a mensagem
    if palpite2 == numero_secreto2:
        
        print("Você adivinhou o segundo número!")
        
        adivinhou2 = True
        
    # Se não adivinhou  exibe tente novamente
    if not adivinhou1 == True or not adivinhou2 == True:
        
        print("Tente novamente.")
        
        #Reduzindo as tentantivas restantes
        tentativas -= 1
        
if adivinhou1 == True and adivinhou2 == True:
    
    print("Parabéns! Você adivinhou ambos os números!")
    
else:
    
    print(f"Você não conseguiu adivinhar os números. Eles eram {numero_secreto1} e {numero_secreto2}")
    
print("Fim do jogo!")
print() 