#função lambda usando filter para filtrar os números pares de uma lista
print("numeros pares")
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda x: x % 2 == 0, numeros))#filter retorna um iterador, por isso é necessário converter para lista
print(pares) 
#função lambda usando filter para filtrar os números ímpares de uma lista
print("numeros impares")
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)
#função lambda usando filter para filtrar os números maiores que 5 de uma lista
print("numeros maiores que 5")
maiores_que_5 = list(filter(lambda x: x > 5, numeros))
print(maiores_que_5)
#função lambda usando filter para filtrar os números menores
#que 5 de uma lista
print("numeros menores que 5")
menores_que_5 = list(filter(lambda x: x < 5, numeros))
print(menores_que_5)

#função lambda usando filter para filtrar os números iguais a 5 de uma lista
print("numeros iguais a 5")
iguais_a_5 = list(filter(lambda x: x == 5, numeros))
print(iguais_a_5)
#lista com lista de strings retorna a letra "a"

print("letra a")
lista_strings = ["banana","maçã", "damasco","cereja"]
letra_a = list(filter(lambda x: "a" in x, lista_strings))
print(letra_a)

lista ="abcdefghijklmnopqrstuvwxyzmnopqrstuvwx"
print("vogais")
#lista com letras do alfabeto retorna as vogais
vogais = list(filter(lambda x: x in "aeiou", lista))
print(vogais)
print("consoantes")
#lista com letras do alfabeto retorna as consoantes
consoantes = list(filter(lambda x: x not in "aeiou", lista))
print(consoantes)
print("letras maiúsculas")
#lista com letras do alfabeto retorna as letras maiúsculas
letras_maiusculas = list(filter(lambda x: x.isupper(), lista))
print(letras_maiusculas)
print("letras minúsculas")
#lista com letras do alfabeto retorna as letras minúsculas
letras_minusculas = list(filter(lambda x: x.islower(), lista))
print(letras_minusculas)

nomes = ["Pedro", "Maria", "João", "Alan", "Ana","Maria"]
print("que começam com a letra 'A'")
#lista com nomes retorna os nomes que começam com a letra "A"
nomes_com_a = list(filter(lambda x: x.startswith("A"), nomes))#startswith verifica se a string começa com o argumento passado
print(nomes_com_a) 
print("que começam letra A")
#lista com nomes retorna os nomes que começam com a letra "A"
nomes_com_a = list(filter(lambda x: x[0] == "A", nomes))
print(nomes_com_a)
print("que terminam com a letra 'a'")
#lista com nomes retorna os nomes que terminam com a letra "a"
nomes_com_a = list(filter(lambda x: x.endswith("a"), nomes))#endswith verifica se a string termina com o argumento passado
print(nomes_com_a)
print("que terminam com a letra a")
#lista com nomes retorna os nomes que terminam com a letra "a"
nomes_com_a = list(filter(lambda x: x[-1] == "a", nomes))
print(nomes_com_a)

print("nomes = Maria") 
nomes_iguais = list(filter(lambda x: x == "Maria", nomes))    
print(nomes_iguais)    

print("Função Lambda com map retornando cada numero elevado ao quadrado")
numeros1 = [1,2,3,4,5]
quadrado = list(map(lambda x: x ** 2, numeros1))
print(quadrado)
print("Retorna o tamanho de cada palavra")
lista_frutas = ["banana","maçã", "damasco","cereja"]
print("lista_frutas")
frutas = list(map(lambda x: len(x), lista_frutas))
print(frutas)
print("Função Lambda com filter e map retornando cada numero impar elevado ao quadrado")
numeros1 = [1,2,3,4,5]
impares = list(filter(lambda x: x%2!=0, numeros1))
impares_quadrado = list(map(lambda x: x**2,impares))
print(impares)
print(impares_quadrado)

print("tentar outra forma")
      

