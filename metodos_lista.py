
"""
Métodos de Listas
        sort(): ordena a lista in-place.
        reverse(): inverte a ordem dos elementos in-place.
        count(): conta o número de ocorrências de um elemento.
        index(): retorna o índice da primeira ocorrência de um elemento.
"""



print("O método sort() ordena os itens da lista em uma ordem crescente por ")
print("padrão. Para números, isso é uma ordem numérica e para strings, é uma ordem alfabética")

numeros = [23, 1, 45, 6, 12]
frutas = ["banana", "maçã", "banana", "cereja", "maçã", "damasco"]
numeros.sort()
print(numeros)
print()
frutas.sort()
print(frutas)

print("count(): conta o número de ocorrências de um elemento.")
numeros = [23, 1, 45, 6, 12]
frutas = ["banana", "maçã", "banana", "cereja", "maçã", "damasco"]
print(numeros.count(6))
print(frutas.count("maçã"))
ocorrencias_banana = frutas.count("banana")
print(ocorrencias_banana) # Saída 2
print()
print(" index(): retorna o índice da primeira ocorrência de um elemento.")
indice_maca = frutas.index("maçã")
print(indice_maca)  # Saída: 4 (pois nós invertemos a lista anteriormente com reverse())

indice_23 = numeros.index(6)
print(indice_23) #Saída: 3
print("Para ordenar em ordem decrescente, podemos usar o argumento reverse=True:")
numeros = [23, 1, 45, 6, 12]
frutas = ["banana", "maçã", "banana", "cereja", "maçã", "damasco"]
numeros.sort(reverse=True) #ordem decrescente
print(numeros)  # Saída: [45, 23, 12, 6, 1]
numeros.sort(reverse=False) #ordem crescente
print(numeros)  # Saída: [45, 23, 12, 6, 1]

frutas.sort(reverse=True)
print(frutas)
print()
print("O método reverse() simplesmente inverte a ordem dos elementos da lista.")
print(numeros)
print(frutas)
numeros.reverse() #inverte a lista
print(numeros) 
numeros.reverse() #inverte a lista
print(numeros) 
numeros.reverse() #inverte a lista
print(numeros) 
frutas.reverse()
print(frutas)
frutas.reverse()
print(frutas)