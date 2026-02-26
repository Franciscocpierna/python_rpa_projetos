numeros= [1,2,3,4,5,6,7,8,9,10] 
lista_pares = [numero for numero in numeros if numero % 2 == 0]
print(lista_pares) 
lista_impares = [numero for numero in numeros if numero % 2 != 0]
print(lista_impares) 

palavra = 'francisco carlos' 
resultado_direto = palavra.title()
print('resultado direto', resultado_direto) 

palavra1 = ['francisco carlos', 'maria', 'jose', 'antonio']
resultado_indireto = [p.capitalize() for p in palavra1]
print('resultado_indireto ',resultado_indireto  ) 

resultado_indireto = [p.capitalize() for p in palavra.split()]
print('resultado_indireto ',resultado_indireto  ) 