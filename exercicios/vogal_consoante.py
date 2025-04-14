"""
1 - Faça um Programa que verifique se uma letra digitada é uma vogal ou consoante.

O programa deverá seguir as seguintes regras:

- Solicitar ao usuário que insira uma letra.
- Verificar se o caractere inserido é uma letra do alfabeto.
- Caso o usuário tenha inserido um caractere válido (ou seja, uma 
            letra do alfabeto), o programa deverá identificar e informar 
            se essa letra é uma vogal ou uma consoante.
- Caso o usuário insira um valor inválido (como números, símbolos ou 
            mais de um caractere), o programa deverá exibir uma mensagem de 
            erro, informando que a entrada é inválida e pedindo para que 
            ele insira apenas uma letra.
"""

# Define uma função 'verificar_letra' que recebe 'letra' 
        # como parâmetro.
# O propósito desta função é determinar se uma entrada 
        # única é uma vogal ou consoante,
        # e garantir que a entrada seja um caractere alfabético válido.
def verificar_letra(letra):
    
    # Cria uma lista contendo todas as vogais do alfabeto, 
            # tanto em caixa alta quanto baixa.
    # Isso permite que a função verifique de maneira eficaz e 
            # sem distinção de maiúsculas ou minúsculas.
    #vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vogais="aeiouAEIOU"
    # Primeiro, verifica se a entrada é um caractere alfabético e 
            # se consiste em apenas um caractere.
    # Utiliza 'letra.isalpha()' para garantir que a entrada 
            # seja alfabética, evitando números ou símbolos.
    # Utiliza 'len(letra) == 1' para assegurar que a entrada 
            # seja apenas um único caractere,
            # o que é essencial para a validação de vogal ou consoante.
    if letra.isalpha() and len(letra) == 1:
        
        # Se a letra está contida na lista de vogais definida, 
                # então é identificada como vogal.
        # A comparação 'letra in vogais' efetua uma busca na 
                # lista 'vogais' para verificar se a 'letra'
                # corresponde a qualquer elemento na lista.
        if letra in vogais:
            return f"A letra '{letra}' é uma vogal."
            
        # Caso a letra não esteja na lista de vogais, por 
                # eliminação, é uma consoante.
        # Isso ocorre apenas se a letra é alfabética e não é 
                # uma das vogais listadas anteriormente.
        else:
            return f"A letra '{letra}' é uma consoante."
            
    # Se a entrada não satisfizer as condições de ser 
            # alfabética e de ter apenas um caractere,
    # a função retorna uma mensagem de erro, pedindo 
            # uma entrada válida.
    else:
        return "Entrada inválida! Por favor, insira apenas uma letra."

# Solicita ao usuário que insira uma letra do 
        # alfabeto para verificação.
# Esta etapa interage diretamente com o usuário, 
        # pedindo uma entrada simples de texto.
letra_digitada = input("Digite uma letra: ")

# A função 'verificar_letra' é chamada com a entrada do 
        # usuário, e o resultado é armazenado em 'resultado'.
# Este resultado determinará se a entrada é uma vogal, 
        # consoante ou se foi inválida.
resultado = verificar_letra(letra_digitada)

# O resultado da verificação é impresso, mostrando ao 
        # usuário se a letra inserida é uma vogal, consoante
        # ou se a entrada foi inválida.
print(resultado)