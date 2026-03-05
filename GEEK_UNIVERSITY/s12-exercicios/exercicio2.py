"""
2. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela
quantas letras são vogais e quantas são consoantes.
"""

vogais: int = 0
consoantes: int = 0
arquivo: str = input('Informe o nome do arquivo para abrir: ')

with open(arquivo, 'r') as arq:
    linhas = arq.readlines()


for linha in linhas:
    if linha.replace('\n', '').lower() in ['a', 'e', 'i', 'o', 'u']:
        vogais = vogais + 1
    else:
        consoantes = consoantes + 1


if vogais > 0:
    print(f'Existe(m) {vogais} vogais no arquivo.')
else:
    print('Nao existem vogais no arquivo.')

if consoantes > 0:
    print(f'Existe(m) {consoantes} consoantes no arquivo.')
else:
    print('Nao existem consoantes no arquivo.')
