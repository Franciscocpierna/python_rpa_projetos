"""
Big-O - n^3 Cubic

A complexidade cúbica O(n3) refere-se a algoritmos cujo tempo de 
execução cresce proporcionalmente ao cubo do tamanho da entrada. Embora
algoritmos com essa complexidade não sejam tão comuns quanto aqueles com 
complexidades mais baixas, eles ainda existem, especialmente em problemas 
combinatórios e em algoritmos de força bruta.

Exemplo Prático: Triplas que somam zero

Suponha que você tenha uma lista de números inteiros e queira encontrar
todas as triplas (três números) na lista que somam zero.

A abordagem cúbica é percorrer todos os conjuntos possíveis de três números 
na lista e verificar se a soma é zero.

Vamos ver um exemplo:
"""

# Define a função 'encontrar_triplos_soma_zero' que recebe uma lista como argumento.
def encontrar_triplos_soma_zero(lista):
    
    # Obtém o tamanho da lista e armazena na variável 'n'.
    n = len(lista)
    
    # Inicializa uma lista vazia 'triplas' para armazenar os conjuntos
    # de três números que somam zero.
    triplas = []
    
    # Primeiro loop: itera sobre cada elemento da lista, armazenando o
    # índice atual em 'i'.
    for i in range(n):
        
        # Segundo loop: começa de 'i+1' para evitar duplicatas e percorre
        # até o final da lista.
        for j in range(i + 1, n):
            
            # Terceiro loop: começa de 'j+1' para evitar duplicatas e 
            # percorre até o final da lista.
            for k in range(j + 1, n):
                
                # Verifica se a soma dos elementos nos índices i, j e k é igual a zero.
                if lista[i] + lista[j] + lista[k] == 0:
                    
                    # Se a soma é zero, adiciona uma tupla contendo os três 
                    # elementos à lista 'triplas'.
                    triplas.append((lista[i], lista[j], lista[k]))
    
    # Retorna a lista 'triplas' contendo todas as triplas que somam zero.
    return triplas


# Parte de Demonstração

# Inicializa uma lista de números, que contém números positivos, negativos e zero.
lista_numeros = [-1, 0, 1, 2, -1, -4]

# Chama a função 'encontrar_triplos_soma_zero' passando a lista de números como argumento.
# Armazena o resultado retornado pela função na variável 'resultado'.
resultado = encontrar_triplos_soma_zero(lista_numeros)

# Imprime as triplas encontradas que somam zero.
# O resultado é uma lista de tuplas, onde cada tupla contém três elementos que somam zero.
print("Triplas que somam zero:", resultado)


"""
No exemplo acima, temos três loops aninhados percorrendo a lista
de números. Isso resulta em uma complexidade de tempo O(n3). No entanto, 
vale observar que há maneiras mais eficientes de resolver esse problema 
específico, mas a abordagem acima serve para ilustrar a complexidade cúbica.


Triplas que somam zero: O problema

Dada uma lista de números, queremos encontrar todas as combinações de três
números cuja soma seja zero.


Dada a lista [-1, 0, 1, 2, -1, -4], as triplas que somam zero são:

    (-1, 0, 1)
    (-1, 2, -1)
    (0, 1, -1)

Para esclarecer:

    (-1, 0, 1): Usa o primeiro "-1" da lista, "0" e "1".
    (-1, 2, -1): Usa o primeiro "-1" da lista, "2" e o segundo "-1".
    (0, 1, -1): Usa "0", "1" e o segundo "-1" da lista.

Assim, todos os números da lista, exceto "-4", são usados em pelo menos uma 
das combinações que somam zero.

"""
print()