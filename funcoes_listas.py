"""
 Utilidades e Funções com Listas
        len(): retorna o número de elementos na lista.
        max(): retorna o maior valor.
        min(): retorna o menor valor.
        sum(): retorna a soma dos elementos.

"""
print("Função len(valores) ")
valores = [23, 45, 67, 89, 12, 56, 78, 90, 34, 56]
print(valores)

numero_elementos = len(valores)
print(f"O número de elementos na lista de valores é: {numero_elementos}")

print("\npresente na lista usando as funções max() e min().")
maior_valor = max(valores)
menor_valor = min(valores)

print(f"O maior valor na lista de valores é: {maior_valor}")
print(f"O menor valor na lista de valores é: {menor_valor}")
print("\nusando a função sum() soma")
soma_valores = sum(valores)

print(f"A soma dos elementos da lista de valores é: {soma_valores}")

print("\nCalcule e imprima a média dos pesos usando as funções sum() e len()")
pesos = [58.5, 63.2, 71.3, 69.4, 68.2]

print(pesos)

media_pesos = sum(pesos) / len(pesos)

print(f"A média dos pesos é: {media_pesos:.2f}")

print("Usando o loop for para iterar sobre os valores da lista:")
frutas = ["maçã", "banana", "cereja", "damasco", "figo"]

for fruta in frutas:
    
    print(fruta)
    
#Usando enumerate() para obter índice e valor ao iterar:

#A função enumerate() retorna tanto o índice quanto o valor ao iterar 
#sobre uma lista. Isso é útil quando você quer saber a posição (índice) 
#de cada item na lista enquanto itera.

for indice, fruta in enumerate(frutas):
    print(f"Fruta no índice {indice} é {fruta}")

print("usando só sobre os itens")
nomes = ["Alice", "Bruno", "Clara", "Daniel", "Eduarda"]

print(nomes)

for nome in nomes:
    
    print(nome)
print("enumerate() para indice e valor") 
for  indice,nome in enumerate(nomes):
      print("indice e nome = ", indice,nome) 
      
for indice, nome in enumerate(nomes):
    
    print(f"{indice + 1}: {nome}")
    
    
notas = [85, 90, 78, 92, 88]

print()

print(notas)
print(nomes)

for indice, nome in enumerate(nomes):
    
    print(f"{nome} obteve nota {notas[indice]}")   
      
print("Ao usar a função list() em uma string, cada caractere da string será um elemento da lista resultante.")

s = "olá"
lista_s = list(s)
print(lista_s)  # Saída: ['o', 'l', 'á']

print("A função split() é usada para dividir uma string em uma lista com base em um delimitador especificado se não usa espaço")
frase = "Python é divertido"
palavras = frase.split()
print(palavras)  # Saída: ['Python', 'é', 'divertido']

data = "12/10/2023"
elementos_data = data.split("/")
print(elementos_data)#saída ['12', '10', '2023']
print("\nA função join() é usada para converter uma lista em uma string Ela une os elementos de uma lista em uma única string com base em um delimitador especificado")
lista_palavras = ['Python', 'é', 'incrível']
print("\n['Python', 'é', 'incrível']")
frase_juntada = ' '.join(lista_palavras)
print(frase_juntada)  # Saída: "Python é incrível"

print("\nlista_data = ['25', '12', '2023'] '/'.join(lista_data)")
lista_data = ["25", "12", "2023"]

print(lista_data)

data_juntada = '/'.join(lista_data)
print(data_juntada)
print("exercicios")

palavra = "Python"
print(palavra)
print("lista_palavra = list(palavra)")
lista_palavra = list(palavra)

print("Lista de caracteres:", lista_palavra)
print("\nusando split() ")
frase = "Aprendendo Python é divertido!"

print(frase)
lista_palavras = frase.split()

print("Lista de palavras:", lista_palavras)
print("reconstrução da frase")
frase_recontruida = " ".join(lista_palavras)

print("Frase resconstruída:", frase_recontruida)
print("Frase resconstruída usando join com virgula e espaço:string_itens = ", ".join(itens)")

itens = ["maçã", "banana", "cereja"]
print(itens)

string_itens = ", ".join(itens)

print("String de itens:", string_itens)



