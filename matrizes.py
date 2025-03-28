"""
Matrizes:

        Inicializando as duas matrizes e a matriz resultado
        Usando loops for aninhados para subtrair elementos correspondentes
"""

#Exemplo Prático: Subtração de Matrizes 3x3 em Python

#A subtração de matrizes, assim como a adição, é uma operação elemento 
#a elemento. Para subtrair duas matrizes, elas devem ter as mesmas dimensões. 
#O resultado é uma nova matriz com a mesma dimensão, onde cada elemento é a diferença 
#dos elementos correspondentes das duas matrizes originais.

#Inicializando as duas matrizes e a matriz resultado:

# Inicializa a matriz A com valores pré-definidos
A = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
print(A)

# Imprime uma quebra de linha seguida de um título para a matriz A
print("\nImprimindo Matriz A")

# Imprime o título para a matriz A
print("Matriz A:\n")
# Inicia um loop para percorrer as linhas da matriz
for linha in range(3):  
    
    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(3):  
        
        # Imprime o valor do elemento atual da matriz seguido de dois espaços, sem quebrar a linha
        print(f"{A[linha][coluna]}", end="  ")  
        
    # Imprime uma quebra de linha após imprimir todos os elementos de uma linha completa da matriz
    print()  
# Inicializa a matriz B com valores pré-definidos
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Imprime uma quebra de linha seguida de um título para a matriz B
print("\nMatriz B:")

# Inicia um loop para percorrer as linhas da matriz
for linha in range(3):  
    
    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(3):  
        
        # Imprime o valor do elemento atual da matriz seguido de dois espaços, sem quebrar a linha
        print(f"{B[linha][coluna]}", end="  ") 
        
    # Imprime uma quebra de linha após imprimir todos os elementos de uma linha completa da matriz
    print()  
# Inicializa a matriz D com todos os elementos sendo zero
D = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]

# Imprime o título para a matriz D
print("\nMatriz D:")
# Inicia um loop para percorrer as linhas da matriz
for linha in range(3):
    
    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(3):
        
        # Imprime o valor do elemento atual da matriz seguido de dois espaços, sem quebrar a linha
        print(f"{D[linha][coluna]}", end="  ")
        
    # Imprime uma quebra de linha após imprimir todos os elementos de uma linha completa da matriz
    print()
print(" Subtração das matrizes A e B")

for linha in range(3):
    
    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(3):
        
        # Imprime o valor do elemento atual da matriz seguido de dois espaços, sem quebrar a linha
        D[linha][coluna] = A[linha][coluna]-B[linha][coluna]
        print(f"{D[linha][coluna]}", end="  ")
    # Imprime uma quebra de linha após imprimir todos os elementos de uma linha completa da matriz
    print()
print(" Soma das matrizes A e B") 
   
for linha in range(3):
    
    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(3):
        
        # Imprime o valor do elemento atual da matriz seguido de dois espaços, sem quebrar a linha
        D[linha][coluna] = A[linha][coluna]+B[linha][coluna]
        print(f"{D[linha][coluna]}", end="  ")
    # Imprime uma quebra de linha após imprimir todos os elementos de uma linha completa da matriz
    print()   
    
print("soma dos elementos da diagonal principal da matriz")   

soma_diagonal = 0

# Inicia um loop para percorrer os elementos da diagonal principal da matriz 3x3
for i in range(3):
    
    # Adiciona o valor do elemento atual da diagonal principal ao acumulador soma_diagonal
    #soma_diagonal = soma_diagonal + B[i][i]
    soma_diagonal += A[i][i]

# Imprime o resultado da soma dos elementos da diagonal principal
print(f"\nA soma dos elementos da diagonal da matriz A é: {soma_diagonal}")
"""
Exercício: Soma dos Números Pares em uma Matriz 4x4

Enunciado:

Dada a seguinte matriz 4x4:
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16

    - Escreva um programa em Python que percorre cada elemento da matriz.
    - Some todos os números pares presentes na matriz.
    - Imprima o resultado da soma.

Dica: Use loops for aninhados para percorrer cada linha e coluna da matriz. 
Utilize o operador % para verificar se um número é par.

Ao resolver o exercício, os alunos devem ser capazes de navegar pelos elementos 
da matriz, aplicar condições lógicas e acumular valores baseados em critérios específicos.
"""

#Solução:

# Dada matriz 4x4
M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(M)
# Inicializa o acumulador para armazenar a soma dos elementos pares da matriz
soma_pares = 0
for linha in range(4):
    
    # Inicia um loop interno para percorrer as colunas da matriz
    for coluna in range(4):
            if M[linha][coluna]%2 == 0: 
              soma_pares += M[linha][coluna]
        
print(f"A soma dos números pares é {soma_pares}")
print()   


print("somando a primeira coluna")
soma_coluna = 0
coluna_especifica = 0
for linha in range(4):
    
    soma_coluna += M[linha][coluna_especifica]
        
print(f"A soma da coluna {coluna_especifica} números somados {soma_coluna}")
print()   

"""
Exemplo de Matrizes e Média de Notas

Você foi contratado para desenvolver um sistema simples de registro de 
notas para uma escola. O professor possui 3 alunos e para cada um, ele 
deseja registrar 4 notas correspondentes aos bimestres do ano letivo.

Tarefas:

    - Solicite ao usuário o nome de cada aluno.
    - Para cada aluno, solicite as 4 notas correspondentes.
    - Armazene todas essas informações em uma matriz, onde cada 
        linha representa um aluno e as colunas contêm o nome do 
        aluno seguido por suas 4 notas.
    - Calcule a média das notas de cada aluno.
    - Imprima o nome, as notas e a média de cada aluno.

Dicas:

    Utilize loops for para percorrer os alunos e as notas.
    Lembre-se de que a média é a soma das notas dividida pelo número total de notas.
    Mantenha a organização do código para facilitar a leitura e a correção.
"""

# Inicializa uma matriz vazia para armazenar os nomes e as notas dos alunos
matriz_alunos = []

# Inicia um loop para coletar informações de 3 alunos
for i in range(3):
    
    # Solicita o nome do aluno atual
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    
    # Inicializa uma lista vazia para armazenar as notas do aluno atual
    notas = []
    
    # Inicia um loop para coletar as 4 notas do aluno atual
    for j in range(4):
        
        # Solicita a nota atual do aluno
        nota = float(input(f"Digite a nota {j + 1} do aluno {nome}: "))
        
        # Adiciona a nota coletada à lista de notas
        notas.append(nota)
        
    # Adiciona o nome do aluno e suas notas à matriz de alunos
    matriz_alunos.append([nome] + notas)
    

# Inicia um loop para imprimir as informações de cada aluno
for aluno in matriz_alunos:
    
    # Extrai o nome do aluno da lista atual
    nome = aluno[0]
    
    # Extrai as notas do aluno da lista atual
    notas = aluno[1:]
    
    # Calcula a média das notas do aluno
    media = sum(notas) / 4
    
    # Imprime as informações do aluno
    print("\n" + "-"*40)
    print(f"Nome: {nome}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")


    