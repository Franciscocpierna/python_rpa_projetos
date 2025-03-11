quadrado_impares = [i**2 for i in range(1, 10) if i % 2 != 0]
print(quadrado_impares)
# Output: [1, 9, 25, 49, 81]
quadrado_impares = []
for i in range(1, 10):
    if i % 2 != 0:
        quadrado_impares.append(i**2)
print(quadrado_impares) 
print("#############################################")
numero = int(input("Digite um número: "))
fatorial = 1
for i in range(numero, 0, -1):
    fatorial *= i
    print(i, end=" ")#end=" " para imprimir na mesma linha
print(f"O fatorial de {numero} é {fatorial}")
print()
print("#############################################")
texto = "Hello World!"
for letra in texto:
    print(letra)
print()
print("#############################################")    

consoantes = [letra for letra in texto if letra.lower() not in "aeiou !"]
print(consoantes) 
    
    