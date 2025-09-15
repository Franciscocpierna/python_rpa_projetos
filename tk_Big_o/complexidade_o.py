"""
 Big-O - Complexidade O(1)
 
 
 A Complexidade O(1), também conhecida como complexidade constante, 
 refere-se a uma situação em que o tempo de execução (ou outro recurso) de 
 uma operação ou algoritmo não depende do tamanho da entrada. Em outras
 palavras, independentemente de quão grande ou pequena seja a entrada, a
 operação ou algoritmo levará aproximadamente o mesmo tempo para ser 
 executado.

A notação O(1) não significa necessariamente que a operação é "rápida"
em termos absolutos; ela simplesmente indica que o tempo de execução não 
varia com o tamanho da entrada. Uma operação O(1) pode, de fato, ser mais 
lenta do que uma operação O(n) para valores pequenos de n, mas a diferença 
chave é que, enquanto a operação O(n) se tornará mais lenta à medida que n
aumenta, a operação O(1) permanecerá constante.


Exemplo Prático: Acessar um elemento em um array (ou lista em Python)

Em linguagens de programação que usam arrays ou listas, acessar um elemento por 
seu índice tem uma complexidade de tempo constante O(1).

A justificativa para isso é que, quando sabemos o índice do elemento, podemos 
acessar diretamente o elemento sem ter que verificar os outros elementos da 
lista. Independentemente de onde o elemento esteja (no início, meio ou fim da
lista) ou de quão grande seja a lista, o tempo necessário para acessar um 
elemento específico é o mesmo.
"""

# Definindo uma função chamada 'acessar_elemento'.
# A função aceita dois argumentos: uma 'lista' e um 'indice'. 
# Seu objetivo é retornar o elemento da 'lista' localizado 
# na posição especificada pelo 'indice'.
def acessar_elemento(lista, indice):
    return lista[indice]  # Retorna o elemento da 'lista' que está na posição 'indice'.

# Criando uma lista (ou array) chamada 'meu_array' que contém alguns números inteiros.
meu_array = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]

# Usando a função 'acessar_elemento' para acessar e 
# imprimir o primeiro elemento da 'meu_array'.
# Como as listas em Python são baseadas em índice zero, o 
# índice 0 refere-se ao primeiro elemento da lista.
print(acessar_elemento(meu_array, 0))  # Saída esperada é 2, pois é o primeiro elemento da lista.

# Usando a função 'acessar_elemento' para acessar e 
# imprimir o sexto elemento da 'meu_array'.
# O índice 5 refere-se ao sexto elemento, pois 0 é o 
# índice do primeiro elemento, 1 é o índice do segundo, e assim por diante.
print(acessar_elemento(meu_array, 5))  # Saída esperada é 23, pois é o sexto elemento da lista.

# Usando a função 'acessar_elemento' para acessar e imprimir o 
# décimo primeiro (e último) elemento da 'meu_array'.
# O índice 10 refere-se ao décimo primeiro elemento.
print(acessar_elemento(meu_array, 10))  # Saída esperada é 91, pois é o último elemento da lista.

"""
Neste exemplo, o tempo que leva para acessar um elemento em meu_array
é constante, independentemente de qual elemento estamos acessando. O 
tamanho da lista não afeta o tempo necessário para acessar um elemento 
específico, e é por isso que dizemos que essa operação tem uma complexidade
de tempo O(1).
"""
print()