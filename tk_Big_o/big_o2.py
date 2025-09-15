"""
Exercício - Comparando Dois Métodos de Soma

Objetivo: Dados dois algoritmos diferentes para somar todos os números de
uma lista, seu objetivo é implementá-los, testá-los e analisar sua eficiência.

Instruções:

    Você tem a lista de 200 números: 
        lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200].

    - Implemente dois algoritmos para calcular a soma total dessa lista:

        a. Algoritmo 1: Soma Iterativa

            Utilize um loop para iterar sobre cada número da lista e somá-lo a um total.

        b. Algoritmo 2: Soma Recursiva

            Implemente uma função recursiva que somará o último número da lista 
            com a soma dos números restantes.

    - Execute ambos os algoritmos e imprima o resultado.

    - Calcule e compare o tempo de execução de ambos os algoritmos.

    Analise a complexidade de cada algoritmo em termos de notação Big O.

Dicas:

    Use o módulo time do Python para medir o tempo de execução.
    Lembre-se de que, para listas pequenas, as diferenças no tempo de execução podem não ser muito 
    perceptíveis. A análise de Big O é mais relevante quando consideramos tamanhos de entrada muito maiores.
"""

# Vamos resolver o exercício passo a passo:

"""
exemplo de como criar a lista:

lista_numeros = list(range(1, 201))
print(lista_numeros)
"""

"""
Você tem a lista de 200 números: 
        lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200].
"""

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]


# - Implemente dois algoritmos para calcular a soma total dessa lista:

"""
a. Algoritmo 1: Soma Iterativa

        Utilize um loop para iterar sobre cada número da lista e somá-lo a um total.
"""

# Define a função 'soma_iterativa', que recebe como argumento uma lista de números.
def soma_iterativa(lista):
    
    # Inicializa a variável 'total' com o valor 0. 
    # Esta variável será usada para acumular a soma de todos os números na lista.
    total = 0
    
    # O loop 'for' percorre cada número (denominado 'numero') na lista passada como argumento.
    for numero in lista:
        
        # Dentro do loop, cada 'numero' é adicionado ao 'total' acumulado.
        total += numero
        
    # Após o loop ter terminado de percorrer todos os números na lista, 
    # a função retorna o valor acumulado em 'total', que representa a soma 
    # de todos os números na lista.
    return total



"""
b. Algoritmo 2: Soma Recursiva

        Implemente uma função recursiva que somará o último número da lista 
        com a soma dos números restantes.
"""

# Define a função 'soma_recursiva', que recebe como argumento uma lista de números.
def soma_recursiva(lista):
    
    # Verifica se a lista está vazia.
    # A função 'not lista' retorna 'True' se a lista for vazia (ou seja, não tiver elementos).
    if not lista:  
        
        # Se a lista estiver vazia, a função retorna 0, pois a soma de uma lista vazia é 0.
        return 0
    
    # Se a lista não estiver vazia, a função retorna a soma do primeiro número da lista (lista[0])
    # com a soma dos números restantes (lista[1:]). Para calcular a soma dos números restantes,
    # a função chama a si mesma (soma_recursiva) com a sublista que começa do segundo elemento até o final.
    # Isso é um exemplo de recursão, onde uma função chama a si mesma.
    return lista[0] + soma_recursiva(lista[1:])


# - Execute ambos os algoritmos e imprima o resultado.

# Aqui, os algoritmos de soma são executados usando a lista 'lista_numeros' 
# (que foi definida anteriormente).
# Os resultados são impressos na tela.

# Executa a função 'soma_iterativa' e imprime o resultado.
print("Soma Iterativa:", soma_iterativa(lista_numeros))

# Executa a função 'soma_recursiva' e imprime o resultado.
print("Soma Recursiva:", soma_recursiva(lista_numeros))


# - Calcule e compare o tempo de execução de ambos os algoritmos.

# Importa o módulo 'time'. Este módulo fornece várias funções relacionadas ao tempo,
# incluindo a função 'time()', que retorna o tempo atual em segundos desde a "época".
import time

# Registra o tempo atual em segundos desde a "época" usando a função 'time()' do módulo 'time'.
# Este é o ponto de partida para medir quanto tempo o Algoritmo 1 levará para ser executado.
inicio = time.time()

# Chama a função 'soma_iterativa' para calcular a soma dos números na lista 'lista_numeros'.
soma_iterativa(lista_numeros)

# Registra o tempo atual novamente para determinar quando o Algoritmo 1 terminou.
fim = time.time()

# Calcula a diferença entre os tempos 'fim' e 'inicio' para determinar a 
# duração total da execução.
# Em seguida, imprime o tempo de execução do Algoritmo 1 (Soma Iterativa) em segundos.
print(f"Tempo do Algoritmo 1 (Soma Iterativa): {fim - inicio:.50f} segundos")

# Repete o processo para o Algoritmo 2 (Soma Recursiva):

# Registra o tempo atual para iniciar a medição do Algoritmo 2.
inicio = time.time()

# Chama a função 'soma_recursiva' para calcular a soma dos números na lista 'lista_numeros'.
soma_recursiva(lista_numeros)

# Registra o tempo atual para determinar quando o Algoritmo 2 terminou.
fim = time.time()

# Calcula e imprime o tempo de execução do Algoritmo 2 (Soma Recursiva).
print(f"Tempo do Algoritmo 2 (Soma Recursiva): {fim - inicio:.50f} segundos")



"""
    Análise da complexidade em termos de notação Big O:

    Algoritmo 1 (Soma Iterativa): O(n) - O algoritmo itera sobre cada 
        número da lista uma vez.

    Algoritmo 2 (Soma Recursiva): O(n) - Embora use recursividade, o 
        algoritmo ainda precisa processar cada número da lista uma vez.

Conclusão:

Ambos os algoritmos têm uma complexidade de tempo de O(n) e, portanto, são 
comparáveis em eficiência. A escolha entre eles dependerá principalmente de 
preferências de estilo e legibilidade. Para listas pequenas como a fornecida, a 
diferença no tempo de execução será mínima, mas é útil entender as implicações 
de eficiência para listas muito maiores.
"""

print()
