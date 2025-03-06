import random


print(random.randint(1, 100))
print(random.randrange(1, 5))
print(random.random())

frutas = ["maçã", "banana", "laranja", "pera"]
print(random.choice(frutas))
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros) # embaralha a lista
print(numeros)
#print(random.choice(numeros)) # escolhe um número aleatório da lista
print(random.uniform(5.5, 9.5)) # gera um número real aleatório entre 1 e 10
print(random.sample(range(100), 10)) # gera uma lista de 10 números aleatórios entre 0 e 100