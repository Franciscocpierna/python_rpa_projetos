altura  = 5
print()
for i in range(altura):
     espacos = altura - i - 1
     asteriscos = 2 * i + 1
    # print(f"numero de espaços = {espacos} e asteristicos {asteriscos} e i = {i}")
     print(" " * espacos + "*" * asteriscos)

print("#############################################")
for i in range(altura-1, -1, -1):
     espacos = altura - i - 1
     asteriscos = 2 * i + 1
    
         
     #print(f"numero de espaços = {espacos} e asteristicos {asteriscos} e i = {i}")
     print(" " * espacos + "*" * asteriscos)   
     
largura = 5  # Define a largura do retângulo
altura = 3   # Define a altura do retângulo

for i in range(altura):  # Loop para iterar pelas linhas do retângulo
    
    for j in range(largura):  # Loop para iterar pelas colunas do retângulo
    
        print("*", end=" ")  # Imprime o caractere "*" e um espaço na mesma linha
    
    print()  # Avança para a próxima linha após imprimir uma linha completa
