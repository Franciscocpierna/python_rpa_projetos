"""
3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
"""

numero: int = int(input("Informe um numero inteiro: "))

if numero % 2 == 0:
    print(f"O numero {numero} eh par.")
else:
    print(f"O numero {numero} eh impar.")
