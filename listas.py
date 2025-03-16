# Definindo uma lista de notas de um aluno
notas_aluno = [85, 90, 78, 92, 88]
print(notas_aluno)

print("List Comprehensions")
lista1= [x**2 for x in range(10) if x % 2 == 0]
print(lista1)

lista_numeros = [5, 10, 15]
print("lista_numeros",type(lista_numeros))
mensagem="olá"
print("mensagem= 'ola' ",type(mensagem))
print("lista de strings")

lista_strings = ["ola","tudo bem","com vc"]
print(type(lista_strings))
print("listas sao mutaveis")
lista_num= [1,2,3]
print("lista antes",lista_num)
lista_num[0]=100
print(lista_num)
print("lista depois lista_num[0]=100",lista_num)
print("tuplas sao imutaveis") 
tuplas = (1,2,3)
print("tuplas antes",tuplas)
print("tuplas tuplas[0]=100")
#tuplas[0]=100#da erro
print("lista mista")
lista_mista = [10,"ola",2.5,["a","b"],True]
print(lista_mista)
print("acesso aos elementos da lista")
frutas = ["maçã", "banana", "cereja", "damasco"]
print("frutas na posicao frutas[3]: ", frutas[3]) #damasco
print("frutas na posicao frutas[-1]: ", frutas[-1])#damasco
print("frutas na posicao : ", frutas[-2])#cereja
print("frutas na posicao  ", frutas[-3])#banana
print("frutas na posicao  ", frutas[-4])#maça
