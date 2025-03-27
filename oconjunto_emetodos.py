print("Outras Funções e Métodos")
"""
Outras Funções e Métodos
        len(): Retorna o número de elementos no conjunto.
        in: Verifica a existência de um elemento no conjunto.
        copy(): Retorna uma cópia do conjunto.
"""
#Conjunto de Amostra

#Vamos considerar um conjunto chamado frutas que contém os nomes de algumas frutas:
frutas = {"maça", "banana", "laranja", "uva", "manga"}

#1. len():

#Usar len() para obter o número de frutas no conjunto:
numero_de_frutas = len(frutas)
print(f"O conjunto tem {numero_de_frutas} frutas.") 
# Saída: O conjunto tem 5 frutas.
#2. in:

#Verificar se uma fruta específica está no conjunto:
fruta_desejada = "maça"
if fruta_desejada in frutas:
    print(f"{fruta_desejada} está no conjunto de frutas.")
else:
    print(f"{fruta_desejada} não está no conjunto de frutas.")
# Saída: maçã está no conjunto de frutas.
#3. copy():

#Copiar o conjunto de frutas para outro conjunto:
frutas_copia = frutas.copy()
print(frutas_copia)
# Saída: {'banana', 'maça', 'manga', 'uva', 'laranja'}

# Verificando se os conjuntos são realmente diferentes em memória:
print(frutas is frutas_copia)  # Saída: False

"""
3. Verificação de Elemento:
        Escreva uma função chamada verificar_animal que aceite um nome de animal como argumento.
        A função deve verificar se o animal especificado existe no conjunto animais usando o operador in.
        Se o animal estiver no conjunto, a função deve imprimir: "[Nome do animal] está no conjunto de animais!".
        Caso contrário, deve imprimir: "[Nome do animal] não está no conjunto de animais!".
        Teste a função com os nomes "gato" e "elefante".
"""
animais = {"cachorro", "gato", "pássaro", "peixe", "coelho"}

print(animais)
print()
def verificar_animal(nome):
    
    if nome in animais:
        
        print(f"{nome} está no conjunto de animais!")
        
    else:
        
        print(f"{nome} não está no conjunto de animais!")

verificar_animal("gato")
verificar_animal("elefante")
"""
4. Cópia do Conjunto:
        Crie uma cópia do conjunto animais e armazene-a em uma variável chamada animais_copia.
        Use a função copy() para isso.
        Verifique e imprima se animais e animais_copia são o mesmo objeto em memória.
        Adicione um novo animal, "tartaruga", apenas ao conjunto animais_copia.
        Imprima ambos os conjuntos para verificar se o conjunto original animais permaneceu inalterado.
"""

animais_copia = animais.copy()
print(animais is animais_copia)

animais_copia.add("tartaruga")
print(animais)
print(animais_copia)
