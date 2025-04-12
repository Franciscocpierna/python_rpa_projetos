"""
6. Peça ao usuário uma lista de palavras separadas por 
        vírgulas e mostre a lista com as palavras invertidas.

Objetivo: Manipular strings e listas, reverter listas.
"""

# Solicita ao usuário que digite uma série de palavras, 
        # separadas por vírgulas.
# A entrada do usuário é capturada como uma string.
palavras = input("Digite palavras separadas por vírgulas: ").split(',')

# O método .split(',') é usado para dividir a string de 
        # entrada em uma lista de palavras,
        # onde cada palavra é separada pelo delimitador vírgula (,).
# Isso transforma a string contínua em uma lista 
        # de strings individuais.

# Utiliza o fatiamento de lista [::-1] para inverter a 
        # ordem dos elementos na lista 'palavras'.
# [::-1] é uma sintaxe que começa do final até o início 
        # da lista, movendo-se com um passo de -1 (inverso).
palavras_invertidas = palavras[::-1]

# Imprime a lista de palavras invertida.
# Mostra as palavras na ordem em que foram inseridas, 
        # mas agora em ordem reversa.
print("Lista com palavras invertidas:", palavras_invertidas)
