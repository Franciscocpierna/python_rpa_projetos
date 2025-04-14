
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
# Define a função chamada 'eh_primo', que recebe um parâmetro 'numero'.
# Esta função verifica se um número é primo.
def eh_primo(numero):
    
    # Primeiro, verifica se o número é menor que 2.
    # Por definição, números menores que 2 não são primos.
    if numero < 2:
        return False
    
    # Inicia um laço que vai de 2 até o número-1.
    # O laço testa se o número pode ser dividido de forma 
            # igual por algum número nesse intervalo.
    for i in range(2, numero):
        print("i", i)  # Imprime o valor de 'i' a cada iteração.
        # Se o número for divisível por algum 'i', ele não é primo.
        if numero % i == 0:
            return False
    
    # Se o laço terminar sem encontrar nenhum 
            # divisor, o número é primo.
    return True

# Chama a função 'eh_primo' com o número 7.
# Armazena o resultado retornado pela função 
        # na variável 'resultado'.
resultado = eh_primo(2)

# Imprime o resultado da função.
# A f-string é usada para incluir o resultado da 
        # verificação na mensagem exibida.
print(f"É primo? {resultado}")