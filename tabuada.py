
# Desenvolva um programa que leia um número inteiro e mostre a sua tabuada.
numero = 1
while numero!=0:
    print("Digite um número diferente de 0")
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    for i in range(1, 11):
      print(f"{numero} x {i} = {numero * i}")
    
    
       