"""
Complexidade Computacional
        Notação Big O
        
        
A complexidade computacional e a notação Big O são ferramentas essenciais 
na ciência da computação para descrever a eficiência de algoritmos em 
termos de tempo e espaço. Vamos discutir isso com exemplos práticos:


Como comparar 2 algoritmos:

Vamos usar um exemplo simples: encontrar o maior número em uma lista.

Algoritmo 1: Uso de Loop

    - Vamos percorrer cada número da lista e encontrar o maior número.
    - Algoritmo 2: Uso da Função Nativa max()

Python tem uma função nativa chamada max() que retorna o maior item de uma lista.

Implementação dos Algoritmos:
"""


# Algoritmo 1: Uso de Loop

# Define a função 'encontrar_maior_loop' que aceita uma lista como argumento.
def encontrar_maior_loop(lista):

    # Inicialmente, assume-se que o primeiro elemento da lista é o maior.
    # 'maior' é inicializado com o primeiro elemento da lista.
    maior = lista[0]

    # O loop 'for' itera sobre cada elemento (referido como 'num') na lista.
    for num in lista:

        # Verifica se o número atual (num) da iteração é maior que o valor
        # armazenado em 'maior'.
        if num > maior:

            # Se o número atual (num) for maior, atualize a variável 'maior' com esse valor.
            maior = num

    # Depois de verificar todos os elementos da lista, retorne o valor armazenado 
    # em 'maior', que é o maior número da lista.
    return maior

# Algoritmo 2: Uso da Função Nativa max()

# Define a função 'encontrar_maior_max' que aceita uma lista como argumento.
def encontrar_maior_max(lista):

    # Retorna o maior elemento da lista usando a função nativa 'max()'.
    # A função 'max()' examina todos os elementos da lista e retorna o maior valor.
    return max(lista)



# Teste de Desempenho:

# Importa o módulo 'time' que fornece várias funções relacionadas ao tempo.
# Neste caso, estamos interessados na função 'time()', que retorna o tempo 
# atual em segundos desde a época (normalmente 1 de janeiro de 1970).
import time

# Uma lista de números é definida para ser usada como entrada para o teste de desempenho.
lista = [3, 5, 2, 8, 7, 9, 1]

# Medindo o tempo de execução do Algoritmo 1 (encontrar_maior_loop):

# Captura o tempo atual em segundos e o armazena na variável 'inicio'.
# Este é o ponto de partida para medir quanto tempo o algoritmo leva para executar.
inicio = time.time()

# Chama a função 'encontrar_maior_loop' com a lista de números e imprime o 
# resultado (o maior número da lista).
print(encontrar_maior_loop(lista))

# Captura o tempo novamente, após a execução da função, e o armazena na variável 'fim'.
fim = time.time()

# Calcula a diferença entre 'fim' e 'inicio' para determinar quanto 
# tempo o algoritmo levou para executar.
# Imprime essa diferença formatada com 5 casas decimais, indicando o 
# tempo de execução em segundos.
print(f"Tempo do Algoritmo 1 (Loop): {fim - inicio:.50f} segundos")


# Medindo o tempo de execução do Algoritmo 2 (encontrar_maior_max):

# Captura o tempo atual em segundos e o armazena na variável 'inicio'.
# Este é o ponto de partida para medir quanto tempo o algoritmo leva para executar.
inicio = time.time()

# Chama a função 'encontrar_maior_max' com a lista de números e 
# imprime o resultado (o maior número da lista).
# 'encontrar_maior_max' usa a função nativa 'max()' para encontrar o maior número.
print(encontrar_maior_max(lista))

# Captura o tempo novamente, após a execução da função, e o armazena na variável 'fim'.
fim = time.time()

# Calcula a diferença entre 'fim' e 'inicio' para determinar quanto
# tempo o algoritmo levou para executar.
# Imprime essa diferença formatada com 5 casas decimais, indicando o 
# tempo de execução em segundos.
print(f"Tempo do Algoritmo 2 (max()): {fim - inicio:.50f} segundos")



"""
Análise de Big O:

    Algoritmo 1 (Uso de Loop): O(n) - porque verifica cada número uma vez.
    Algoritmo 2 (Uso da Função Nativa max()): O(n) - apesar de ser uma função nativa, 
        ela ainda precisa verificar cada número uma vez.

Conclusão:

Ambos os algoritmos têm a mesma complexidade de tempo, O(n). No entanto, ao 
rodar o código, você pode observar que a função nativa max() pode ser ligeiramente 
mais rápida porque está otimizada em nível de implementação do Python. Este exemplo 
mostra que, mesmo com a mesma complexidade de Big O, o tempo de execução real pode 
variar com base na implementação específica e otimizações.
"""
print()