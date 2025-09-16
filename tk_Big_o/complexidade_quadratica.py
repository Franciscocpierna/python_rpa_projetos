"""
Big-O - n^2 Quadratic


A complexidade quadrática O(n2) refere-se a algoritmos cujo tempo
de execução cresce proporcionalmente ao quadrado do tamanho da 
entrada. Um dos exemplos clássicos de algoritmos com complexidade O(n2) é 
a ordenação por seleção (selection sort).

Exemplo Prático: Ordenação por Seleção (Selection Sort)

A ordenação por seleção funciona da seguinte forma:

    - Encontre o menor elemento da lista e troque-o com o primeiro elemento.
    - Encontre o segundo menor elemento da lista (ignorando o primeiro) e 
        troque-o com o segundo elemento.
    - Continue este processo até que a lista inteira esteja ordenada.

Vamos ver um exemplo:
"""

# Define a função 'ordenacao_por_selecao' que aceita uma lista como parâmetro.
def ordenacao_por_selecao(lista):
    
    # Obtemos o tamanho da lista e armazenamos na variável 'n'.
    n = len(lista)
    
    # O loop externo itera sobre cada elemento da lista. 'i' é o índice do elemento atual.
    for i in range(n):
        
        # Assume-se inicialmente que o elemento mais à esquerda (elemento atual) é o menor.
        # A variável 'indice_menor' guarda o índice do menor elemento encontrado até agora.
        indice_menor = i
        
        # O loop interno começa do elemento à direita do atual (i+1) e vai até
        # o último elemento da lista.
        for j in range(i+1, n):
            
            # Verifica se o elemento na posição 'j' é menor que o elemento na
            # posição 'indice_menor'.
            if lista[j] < lista[indice_menor]:
                
                # Atualiza 'indice_menor' se encontrarmos um elemento menor.
                indice_menor = j
        
        # Após o loop interno, trocamos o elemento mínimo encontrado pelo elemento atual.
        # Isso coloca o menor elemento não ordenado na sua posição correta.
        # lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
        
        # Cria uma variável temporária para guardar o valor de lista[i]
        temp = lista[i]

        # Atribui o valor de lista[indice_menor] para lista[i]
        lista[i] = lista[indice_menor]

        # Atribui o valor temporário (original lista[i]) para lista[indice_menor]
        lista[indice_menor] = temp


# Lista de números a serem ordenados.
lista_numeros = [64, 25, 12, 22, 11]

# Chama a função 'ordenacao_por_selecao' para ordenar 'lista_numeros'.
ordenacao_por_selecao(lista_numeros)

# Exibe a lista ordenada.
print("Lista ordenada:", lista_numeros)

"""
No algoritmo de ordenação por seleção, o loop externo percorre cada
elemento da lista, e o loop interno compara o elemento atual com todos
os outros elementos subsequentes para encontrar o menor. Por causa destes 
dois loops aninhados, ambos percorrendo a lista, a complexidade de tempo deste
algoritmo é O(n2).
"""
print()