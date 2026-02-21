"""
2. Faça um programa que leia um número inteiro fornecido pelo usuário.
Se esse número for positivo, calcule a raiz quadrada do número e apresente-a.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""

from math import sqrt


numero: int = int(input("Informe um numero inteiro: "))


if numero > 0:
    print(f"A raiz quadrada de {numero} eh {sqrt(numero)}")
else:
    print(f"O numero {numero} eh invalido.")
