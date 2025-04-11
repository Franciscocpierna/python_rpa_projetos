"""
Exercício 11: Converter decimal para binário

Peça ao usuário um número decimal e converta-o para binário usando o while.
"""

# Solicita ao usuário que insira um número decimal. A entrada é 
        # capturada como string e convertida para inteiro.
# Assume-se que o usuário inserirá um número decimal válido.
numero = int(input("Digite um número decimal: "))

# Inicializa a variável 'binario' como uma string vazia.
# Esta variável será usada para construir a representação 
        # binária do número a partir dos restos da divisão.
binario = ""

# Inicia um laço while que continuará enquanto 'numero' 
        # for maior que 0.
# O laço permite decompor o número em seus componentes 
        # binários através de divisões sucessivas por 2.
while numero > 0:
    
    # Calcula o resto da divisão do número por 2 (0 ou 1) e 
            # concatena esse valor ao início da string 'binario'.
    # O operador '%' é usado para obter o resto da divisão, 
            # que representa o bit menos significativo atual.
    binario = str(numero % 2) + binario
    print("Resto da divisão:", numero % 2)  # Imprime o resto da divisão atual.
    print("binario atual ", binario)  # Imprime o valor binário atual após cada iteração.
    ""
    # Utiliza a divisão inteira por 2 para reduzir o 'numero' 
            # pela metade, descartando o bit menos significativo já processado.
    # O operador '//=' é uma forma abreviada de 'numero = numero // 2'.
    numero //= 2 # Atualiza 'numero' para a próxima iteração.
    print("numero//=2 numero atualizado ", numero)  # Imprime o número atualizado após a divisão. 
# Após o término do laço (quando 'numero' é 0), imprime o 
        # resultado da conversão binária.
# Usa uma f-string para formatar a saída, incluindo a 
        # representação binária na mensagem final.
print(f"O número em binário é: {binario}")
numero=1
numero //=2
print("divisão 1/2, 1//=2) = ", numero)  # Imprime o resultado da divisão inteira por 2.