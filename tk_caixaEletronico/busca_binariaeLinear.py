"""
 Big-O - lon(n) Logarithmic
 
A complexidade logarítmica O(log⁡n) é frequentemente observada 
em algoritmos que dividem a entrada pela metade (ou por um fator 
constante) em cada etapa de sua execução. Uma das aplicações mais 
clássicas da complexidade O(log⁡n) é a busca binária.

Exemplo Prático: Busca Binária

A busca binária é um algoritmo que encontra a posição de um valor 
específico dentro de uma lista ordenada. Ele funciona dividindo 
repetidamente a lista ao meio até encontrar o valor desejado ou até 
que o subconjunto se torne pequeno demais para continuar.

Aqui está um exemplo em Python:
"""

# Definindo a função busca_binaria que recebe uma lista e um valor como parâmetros.
def busca_binaria(lista, valor):
    
    """
    Esta função retorna o índice do valor na lista se ele estiver presente.
    Se o valor não estiver presente, a função retorna -1.
    """
    
    # Definindo a variável 'inicio' para marcar o início do 
    # intervalo de busca. Inicialmente, é 0.
    inicio = 0
    
    # Definindo a variável 'fim' para marcar o final do intervalo 
    # de busca. É o último índice da lista.
    fim = len(lista) - 1  # Subtrai 1 porque a lista é indexada a partir de 0.
    
    # O loop while executará enquanto 'inicio' for menor ou igual a 'fim'.
    while inicio <= fim:
        
        # Calculando o índice do meio do intervalo atual.
        # Utilizamos a divisão inteira '//' para garantir que o resultado seja um inteiro.
        meio = (inicio + fim) // 2

        # Verificando se o valor no índice 'meio' é igual ao valor que estamos procurando.
        if lista[meio] == valor:
            
            return meio  # Se sim, retornamos o índice 'meio'.

        # Verificando se o valor no índice 'meio' é menor que o valor que estamos procurando.
        elif lista[meio] < valor:
            
            # Se sim, ajustamos 'inicio' para ser 'meio + 1'.
            # Ignoramos a primeira metade da lista, pois o valor que 
            # estamos procurando deve estar na segunda metade.
            inicio = meio + 1

        # Se o código chegar aqui, significa que lista[meio] > valor.
        else:
            
            # Ajustamos 'fim' para ser 'meio - 1'.
            # Ignoramos a segunda metade da lista, pois o valor que estamos procurando deve estar na primeira metade.
            fim = meio - 1

    # Se o loop termina e não retornamos um índice, então o valor não está presente na lista.
    return -1  # Retornamos -1 para indicar que o valor não foi encontrado.


# Criamos uma lista chamada 'lista_numeros' que contém números inteiros ordenados.
lista_numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Definimos o 'numero_procurado' que desejamos encontrar na lista.
numero_procurado = 15

# Chamamos a função 'busca_binaria' e passamos 
# 'lista_numeros' e 'numero_procurado' como argumentos.
# O resultado será armazenado na variável 'resultado'.
resultado = busca_binaria(lista_numeros, numero_procurado)

# Verificamos se o resultado é diferente de -1.
# Se for diferente de -1, então o número foi encontrado na lista.
if resultado != -1:
    
    # Exibimos uma mensagem indicando que o 'numero_procurado' foi 
    # encontrado e em qual posição (índice).
    print(f"O elemento {numero_procurado} está presente na posição {resultado}.")
    
# Se o resultado for -1, o número não foi encontrado na lista.
else:
    
    # Exibimos uma mensagem indicando que o 'numero_procurado' não foi encontrado na lista.
    print(f"O elemento {numero_procurado} não está presente na lista.")



"""
Neste exemplo, a lista é dividida pela metade em cada iteração do loop
while, o que resulta em uma complexidade logarítmica O(log⁡n). Portanto, 
mesmo que a lista tenha 1.024 elementos, precisaríamos de, no máximo, 10 etapas
para encontrar o elemento desejado (ou determinar que ele não está presente), pois
log⁡2(1024)=10.
"""
print()

print("--------------------------------------------------") 


print()



"""
Big-O - n Linear
 
A complexidade linear O(n) ocorre quando o tempo de execução 
do algoritmo aumenta linearmente com o tamanho da entrada. Uma das 
aplicações mais simples e diretas dessa complexidade é a busca linear.

Exemplo Prático: Busca Linear

A busca linear, também conhecida como busca sequencial, é um método
para encontrar um elemento dentro de uma lista. Ele faz isso percorrendo 
cada elemento da lista, um por um, até encontrar o elemento desejado ou até 
chegar ao fim da lista.

Vamos ver um exemplo:
"""

# Definição da função 'busca_linear', que recebe uma 
# lista e um valor que estamos procurando.
# A função retorna o índice desse valor na lista, se 
# ele existir; caso contrário, retorna -1.
def busca_linear(lista, valor_procurado):
    
    """
    Retorna o índice do valor_procurado na lista se estiver presente, caso contrário retorna -1
    """
    
    # Utilizamos um loop for para percorrer a lista. 
    # A função 'enumerate' nos dá tanto o índice (indice) quanto
    # o valor (valor) de cada elemento da lista.
    for indice, valor in enumerate(lista):
        
        # Verificamos se o valor atual (valor) é igual ao valor
        # que estamos procurando (valor_procurado).
        if valor == valor_procurado:
            
            # Se for igual, retornamos o índice desse valor.
            return indice
    
    # Se o loop terminar sem encontrar o valor, retornamos -1.
    return -1

# Criamos uma lista chamada 'lista_numeros' contendo números inteiros.
lista_numeros = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]

# Definimos o 'numero_procurado' que desejamos encontrar na lista.
numero_procurado = 77

# Chamamos a função 'busca_linear' e passamos 'lista_numeros' 
# e 'numero_procurado' como argumentos.
# O resultado será armazenado na variável 'resultado'.
resultado = busca_linear(lista_numeros, numero_procurado)

# Verificamos se o resultado é diferente de -1.
# Se for diferente de -1, então o número foi encontrado na lista.
if resultado != -1:
    
    # Exibimos uma mensagem indicando que o 'numero_procurado' 
    # foi encontrado e em qual posição (índice).
    print(f"O elemento {numero_procurado} está presente na posição {resultado}.")
    
# Se o resultado for -1, o número não foi encontrado na lista.
else:
    
    # Exibimos uma mensagem indicando que o 'numero_procurado'
    # não foi encontrado na lista.
    print(f"O elemento {numero_procurado} não está presente na lista.")

    
"""
Neste exemplo, a função busca_linear percorre cada elemento da lista 
até encontrar o valor_procurado. A complexidade de tempo dessa função 
é O(n) porque, no pior cenário (quando o elemento não está presente ou
é o último da lista), ela terá que percorrer todos os n elementos da lista.
"""
print()

