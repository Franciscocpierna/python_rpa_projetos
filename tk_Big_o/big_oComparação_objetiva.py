"""
Comparação objetiva entre dois algoritmos

Vamos realizar uma comparação objetiva entre dois algoritmos de busca: a busca 
linear e a busca binária.

Busca Linear:

Complexidade: O(n)

Esta busca verifica cada elemento da lista sequencialmente até encontrar
o elemento desejado ou concluir que o elemento não está na lista.
"""

# Definindo uma função chamada 'busca_linear' que recebe dois argumentos: 'lista' e 'alvo'.
def busca_linear(lista, alvo):
    
    # Usando a função 'enumerate', nós iteramos sobre cada 'item' da 'lista' 
    # e também obtemos o índice atual desse item, que é armazenado na variável 'i'.
    for i, item in enumerate(lista):
        
        # Verificando se o 'item' atual é igual ao 'alvo' especificado.
        if item == alvo:
            
            # Se o 'item' for igual ao 'alvo', retornamos o índice 'i' 
            # onde o 'alvo' foi encontrado.
            return i
        
    # Se terminarmos de iterar sobre a lista inteira e o 'alvo' não for encontrado,
    # retornamos -1 para indicar que o 'alvo' não está presente na 'lista'.
    return -1


"""
Busca Binária:

Complexidade: O(log⁡n)

Esta busca assume que a lista está ordenada. Ela divide repetidamente a 
lista pela metade até que o alvo seja encontrado ou até que a sublista se
torne muito pequena.
"""

# Definindo uma função chamada 'busca_binaria' que recebe dois 
# argumentos: 'lista' e 'alvo'.
def busca_binaria(lista, alvo):
    
    # Inicializando duas variáveis: 'esquerda' e 'direita'. 'esquerda' 
    # começa no índice 0 (início da lista) 
    # e 'direita' começa no último índice da 'lista'.
    esquerda, direita = 0, len(lista) - 1
    
    # Enquanto o valor de 'esquerda' for menor ou igual a 'direita', 
    # continuamos procurando.
    # Isso garante que ainda temos uma sublista para pesquisar.
    while esquerda <= direita:
        
        # Calculando o índice 'meio' da sublista atual.
        # Usamos a divisão inteira '//' para obter um número inteiro.
        meio = (esquerda + direita) // 2
        
        # Verificando se o elemento no índice 'meio' é igual ao 'alvo'.
        if lista[meio] == alvo:
            
            # Se for, retornamos o índice 'meio' onde o 'alvo' foi encontrado.
            return meio
        
        # Se o elemento no índice 'meio' for menor que o 'alvo',
        # significa que o 'alvo' está à direita do 'meio'.
        elif lista[meio] < alvo:
            
            # Assim, atualizamos 'esquerda' para ser 'meio + 1', reduzindo 
            # a sublista para a parte direita.
            esquerda = meio + 1
            
        # Caso contrário, o 'alvo' está à esquerda do 'meio'.
        else:
            
            # Assim, atualizamos 'direita' para ser 'meio - 1', reduzindo 
            # a sublista para a parte esquerda.
            direita = meio - 1

    # Se terminarmos o loop 'while' e o 'alvo' não for encontrado,
    # retornamos -1 para indicar que o 'alvo' não está presente na 'lista'.
    return -1
        
        

"""
Comparação Objetiva:

Vamos comparar o tempo que cada algoritmo leva para buscar um 
elemento em uma lista de tamanho n.
"""

# Importando o módulo 'time' para medir o tempo de execução das funções.
import time

# Importando o módulo 'random' para gerar números aleatórios.
import random

# Criando uma lista chamada 'lista' contendo números 
# inteiros em ordem crescente de 0 até 999999.
# A função 'range(1000000)' gera uma sequência de 
# números de 0 até 999999, e 'list()' a converte em uma lista.
lista = list(range(1000000))

# Gerando um número aleatório entre 0 e 999999 e armazenando-o na variável 'alvo'.
# O número gerado será o valor que tentaremos encontrar nas funções de busca.
alvo = random.randint(0, 999999)

# Iniciando o processo de medição de tempo para a busca linear.
# Capturando o tempo atual e armazenando-o na variável 'inicio'.
inicio = time.time()

# Chamando a função 'busca_linear' com a 'lista' e 'alvo' como argumentos.
# Estamos buscando o 'alvo' dentro da 'lista' usando o método de busca linear.
busca_linear(lista, alvo)

# Capturando o tempo novamente após a execução da função 'busca_linear' e
# armazenando-o na variável 'fim'.
fim = time.time()

# Calculando a diferença entre 'fim' e 'inicio' para obter o tempo 
# total de execução da função 'busca_linear'.
# Imprimindo o resultado com uma precisão de 6 casas decimais.
print(f"Busca Linear: {fim - inicio:.6f} segundos")


# Iniciando o processo de medição de tempo para a busca binária.

# Capturando o tempo atual em segundos desde a "época" (geralmente 1 de janeiro de 1970)
# e armazenando-o na variável 'inicio'.
inicio = time.time()

# Chamando a função 'busca_binaria' com a 'lista' e 'alvo' como argumentos.
# A função busca_binaria tentará encontrar a posição (índice) do 'alvo' dentro da 'lista'.
# Esta função utiliza o método de busca binária, que é mais eficiente do que a busca linear
# para listas ordenadas, pois divide a lista em duas metades em cada iteração.
busca_binaria(lista, alvo)

# Capturando o tempo atual novamente após a execução da função 
# 'busca_binaria' e armazenando-o na variável 'fim'.
fim = time.time()

# Calculando a diferença entre 'fim' e 'inicio' para obter o tempo
# total de execução da função 'busca_binaria'.
# Imprimindo o resultado com uma precisão de 6 casas decimais.
print(f"Busca Binária: {fim - inicio:.6f} segundos")


"""
ao executar este código, você perceberá que a busca binária é 
significativamente mais rápida que a busca linear, especialmente para 
listas grandes. Isso se deve às suas respectivas complexidades: O(n)
para a busca linear e O(log⁡n) para a busca binária.

Este é apenas um exemplo para ilustrar a diferença prática nas complexidades 
Big O entre dois algoritmos. Em situações do mundo real, outras considerações, 
como o uso de memória, também são importantes ao avaliar a eficiência de um algoritmo.
"""
print()
