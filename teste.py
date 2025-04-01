
def calcula_fatorial(n):
 
    if n == 0:
        return 1
    return n*calcula_fatorial(n-1)
  

print(calcula_fatorial(5))  # Saída: 120
palavras = ['Olá,', 'como', 'vai', 'você?']
print(palavras)
frase = ' '.join(palavras)
print(frase)
espaco=[" "," "," "]
nova = '|'.join(espaco)
print(nova)