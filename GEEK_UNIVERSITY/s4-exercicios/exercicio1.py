"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""

numero1: int = int(input("Informe o primeiro numero: "))
numero2: int = int(input("Informe o segundo numero: "))

if numero1 > numero2:
    print(f"O numero {numero1} eh maior que {numero2}")
elif numero1 == numero2:
    print(f"Os numeros {numero1} e {numero2} sao iguais.")
else:
    print(f"O numero {numero2} eh maior que {numero1}")
