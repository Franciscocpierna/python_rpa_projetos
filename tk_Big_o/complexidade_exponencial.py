"""
Big-O - 2^n Exponential

A complexidade exponencial O(2n) refere-se a algoritmos cujo tempo de
execução dobra com cada elemento adicional na entrada. Algoritmos com 
complexidade exponencial tendem a ser impraticáveis para entradas 
maiores, pois o tempo de execução cresce muito rapidamente.

Exemplo Prático: Gerar todas as combinações possíveis de uma string

Imagine que você queira gerar todas as combinações possíveis de uma
string. Por exemplo, para a string "AB", as combinações 
são "", "A", "B" e "AB". O número de combinações possíveis é 2n, onde n é 
o comprimento da string.

Aqui está um exemplo:
"""

# Define a função 'gerar_combinacoes' que toma 
# uma string 's' como argumento.
def gerar_combinacoes(s):
    
    # Caso base: Se a string está vazia, retorne uma lista 
    # com uma string vazia.
    if len(s) == 0:
        return ['']
    
    # Inicializa uma lista vazia chamada 'combinacoes' para armazenar 
    # todas as combinações geradas.
    combinacoes = []
    
    # Pega a primeira letra da string 's' e armazena na variável 'primeira_letra'.
    primeira_letra = s[0]
    
    # Chama a função recursivamente para o restante da string e armazena 
    # as combinações retornadas em 'combinacoes_restantes'.
    combinacoes_restantes = gerar_combinacoes(s[1:])
    
    # Loop através de cada combinação em 'combinacoes_restantes'.
    for combinacao in combinacoes_restantes:
        
        # Adiciona a combinação original (sem a primeira letra) à 
        # lista 'combinacoes'.
        combinacoes.append(combinacao)
        
        # Adiciona uma nova combinação que é a concatenação da 
        # 'primeira_letra' com a combinação original.
        combinacoes.append(primeira_letra + combinacao)
    
    # Retorna a lista completa de combinações.
    return combinacoes


# Demonstração do uso da função 'gerar_combinacoes'

# Define uma string 'string' que contém os caracteres "AB"
string = "AB"

# Chama a função 'gerar_combinacoes' com a string "AB" como argumento
# e armazena o resultado retornado na variável 'resultado'.
resultado = gerar_combinacoes(string)

# Exibe as combinações geradas no console.
# A função 'print' é usada para imprimir a lista 'resultado', 
# que contém todas as combinações da string "AB".
print("Combinações:", resultado)


"""
Neste exemplo, para gerar combinações, pegamos a primeira letra 
da string e, recursivamente, geramos combinações para o restante da 
string. Depois, para cada combinação gerada a partir da substring 
restante, criamos duas novas combinações: uma sem a primeira letra e 
outra com ela.

Dado que cada caracter da string pode estar presente ou ausente em uma
combinação, temos 2 opções para cada caractere, resultando em 2n
combinações possíveis, o que nos dá a complexidade exponencial.
"""
print()