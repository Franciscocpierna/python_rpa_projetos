print("Listas Aninhadas (listas de listas)Criando e acessando listas dentro de listas.Utilizando loops aninhados para iterar sobre elas.")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("matriz[0][1]",matriz[0][1])

for linha in matriz:
    
    # Loop interno: itera sobre cada número (ou elemento) dentro da linha atual
    for numero in linha:
        
        # Imprime o número atual seguido por um espaço, sem mudar de linha devido ao parâmetro "end=' '"
        print(numero, end=' ')
    
    # Uma vez que todos os números de uma linha são impressos, esta linha imprime uma quebra de linha
    # para separar visualmente as linhas da matriz ao imprimir
    print()  


#4. Exemplo Prático:

#Vamos supor que queremos calcular a transposta dessa matriz. 
#A transposta de uma matriz é obtida trocando suas linhas por colunas:

# Inicializando uma lista vazia chamada "transposta"
transposta = []


# Loop através de cada coluna da matriz original
print("matriz[0]", matriz[0])
for i in range(len(matriz[0])):
    
    # Inicializa uma linha temporária para construir uma linha da matriz transposta
    linha_temporaria = []
    
    # Loop através de cada linha da matriz original
    for j in range(len(matriz)):
        
        # Adiciona o elemento da posição j,i (transposto) à linha temporária
        linha_temporaria.append(matriz[j][i])
        print("o i e j ", i,j)
        print("matriz[j][i]",matriz[j][i]) 
        
    # Adiciona a linha temporária completa à matriz transposta
    transposta.append(linha_temporaria)
    
   
print("transposta", transposta)

#1. Acesse e imprima o valor localizado na 
#segunda linha e terceira coluna (deve ser o número 6).

valor = matriz[1][2]

print(f"Valor na segunda linha e terceira coluna: {valor}") # Saída: 6

#2. Utilizando loops aninhados, calcule e imprima a soma de todos
#os valores presentes na matriz.

# Inicializando a variável "soma" com 0. Esta variável armazenará a soma total de todos os números na matriz.
soma = 0

# Loop externo: itera sobre cada linha da matriz
print("calcula a soma")
for linha in matriz:
    
    # Loop interno: itera sobre cada número (ou elemento) dentro da linha atual
    for numero in linha:
        
        # Adiciona o valor do número atual à variável "soma"
        #soma = soma + numero
        print("linha ",linha )
        print("numero = é somado ",numero)
        soma += numero
                

# Após a conclusão dos loops, a variável "soma" contém a soma total de todos os números da matriz.
print(f"Soma dos valores da matriz: {soma}")  # Saída: 45

print()


# Loop externo: itera sobre cada linha da matriz
print("Imprime o número atual seguido por uma tabulação representada por end=\ seguido de t")
for linha in matriz:

    # Loop interno: itera sobre cada número (ou elemento) dentro da linha atual
    for numero in linha:
    
        # Imprime o número atual seguido por uma tabulação (representada por "\t"), 
        # mantendo os números na mesma linha ao imprimir
        print(numero, end="\t")
    
    # Uma vez que todos os números de uma linha são impressos, 
    # esta linha imprime uma quebra de linha para separar as linhas da matriz visualmente ao imprimir
    print()  
