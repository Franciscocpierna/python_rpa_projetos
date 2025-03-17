"""
Operações Básicas com Listas
        Adicionar elementos: append(), insert()
        Remover elementos: remove(), pop()
        Concatenar listas: +, extend()
        Repetir listas: *
        Verificar se um item está na lista: in
"""


#a. append() - Adiciona um item ao final da lista:
frutas = ["maçã", "banana"]
frutas.append("cereja")
print(frutas)  # Saída: ['maçã', 'banana', 'cereja']

#b. insert() - Insere um item em uma posição específica:
frutas = ["maçã", "banana", "cereja"]
frutas.insert(1, "abacate")  # Insere "abacate" na posição de índice 1
print(frutas)  # Saída: ['maçã', 'abacate', 'banana', 'cereja']

print("2. Remover elementos")

#a. remove() - Remove o primeiro item da lista que tem o valor especificado:
frutas = ["maçã", "banana", "cereja"]
frutas.remove("banana")
print(frutas)  # Saída: ['maçã', 'cereja']

print("b. pop() - Remove o item da posição especificada (ou o último item, se o índice não for especificado")
#item, se o índice não for especificado):
frutas = ["maçã", "banana", "cereja"]
frutas.pop(1)  # Remove o item de índice 1
print(frutas)  # Saída: ['maçã', 'cereja']
frutas = ["maçã", "banana", "cereja"]

frutas.pop(1)  # Remove o item de índice 1
print(frutas)  # Saída: ['maçã', 'cereja']

frutas = ["maçã", "banana", "cereja"]
frutas.pop()  # Remove o último item
print(frutas)  # Saída: ["maça","banana"]

print("3. Concatenar listas")
#a. + - Une duas listas:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
uniao = lista1 + lista2
print(uniao)  # Saída: [1, 2, 3, 4, 5, 6]

print("b. extend() - Adiciona os elementos de uma lista (ou qualquer iterável) ao final da lista atual:")
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)  # Saída: [1, 2, 3, 4, 5, 6]

print("4. Repetir listas * - Repete a lista um número específico de vezes:")
repeticao = ["a", "b"] * 3
print(repeticao)  # Saída: ['a', 'b', 'a', 'b', 'a', 'b']

print("#5.  Verificar se um item está na lista #in - Retorna True se um elemento está presente na lista,#caso contrário retorna False:")

frutas = ["maçã", "banana", "cereja"]
print("banana" in frutas)  # Saída: True
print("uva" in frutas)     # Saída: False
print()


