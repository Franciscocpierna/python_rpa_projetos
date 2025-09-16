"""
Exercício - Convertendo Códigos Secretos em Mensagens

Dado um código numérico e um mapeamento de caracteres para números, sua 
tarefa é transformar o código numérico de volta em uma mensagem legível. O mapeamento 
é definido da seguinte forma:

    Letras maiúsculas de 'A' a 'Z' são mapeadas para números de '1' a '26' respectivamente.
    Letras minúsculas de 'a' a 'z' são mapeadas para números de '27' a '52' respectivamente.
    O espaço é mapeado para '53'.

Objetivo: Escreva uma função converter_codigo_para_mensagem(codigo) que receba 
o código numérico como uma string e retorne a mensagem original.

"""

# Solução

# Criação do dicionário 'mapeamento_inverso' para mapear números para caracteres.
# Este dicionário vai conter pares de chave-valor onde cada chave é uma string representando
# um número e cada valor é um caractere correspondente.

# A expressão compreende uma compreensão de dicionário, que é uma forma concisa de construir
# um dicionário em Python. Este loop especificamente cria pares de mapeamento para letras maiúsculas.
mapeamento_inverso = {
    
    # O loop 'for' itera através de uma sequência de números ASCII das letras maiúsculas.
    # 'ord('A')' é o valor ASCII para 'A', e 'ord('Z') + 1' é o valor ASCII para 'Z' mais um,
    # garantindo que o loop inclua a letra 'Z'.
    str(i - ord('A') + 1):  # Calcula o número correspondente a cada letra maiúscula.
                            # Por exemplo, para 'A', isso seria 1 (65 - 64).
                            # O resultado é convertido em string para ser usado como chave no dicionário.
    chr(i)                 # Converte o número ASCII 'i' de volta para o caractere alfabético correspondente.
                            # 'chr' é uma função que faz a conversão de um número ASCII em seu caractere.
    for i in range(ord('A'), ord('Z') + 1)  # Define o intervalo do loop para incluir todas as letras maiúsculas.
}

# Atualiza o dicionário 'mapeamento_inverso' com mapeamentos para letras minúsculas.
# Isso é feito para incluir todos os caracteres alfabéticos no mapeamento.
mapeamento_inverso.update({
    
    # O loop 'for' itera através de uma sequência de números ASCII das letras minúsculas.
    # 'ord('a')' é o valor ASCII para 'a', e 'ord('z') + 1' garante que o loop inclua a letra 'z'.
    str(i - ord('a') + 27):  # Calcula o número correspondente a cada letra minúscula.
                             # Por exemplo, para 'a', isso seria 27 (97 - 70).
                             # O resultado é convertido em string para ser usado como chave no dicionário.
    chr(i)                  # Converte o número ASCII 'i' para o caractere alfabético correspondente.
                             # Neste caso, converte para letras minúsculas.
    for i in range(ord('a'), ord('z') + 1)  # Define o intervalo do loop para incluir todas as letras minúsculas.
})

# Adiciona um mapeamento específico para o espaço em branco.
# O número '53' é usado para representar um espaço na codificação.
mapeamento_inverso['53'] = ' '  # A chave '53' é mapeada para o caractere de espaço (' ').


# Definição da função 'converter_codigo_para_mensagem' que aceita um argumento 'codigo'.
# Esta função é responsável por decodificar uma mensagem codificada numericamente
# de volta para uma mensagem de texto legível.
def converter_codigo_para_mensagem(codigo):
    
    # Inicialização de uma variável 'mensagem' como uma string vazia.
    # Esta variável será usada para acumular a mensagem decodificada à medida
    # que o código é processado.
    mensagem = ""

    # Inicialização da variável 'i', que servirá como um índice para percorrer
    # a string 'codigo'. O índice 'i' começará em 0, que é a posição do primeiro
    # caractere na string.
    i = 0

    # Início de um loop 'while' que continuará executando enquanto 'i' for menor
    # que o comprimento da string 'codigo'. Isso garante que cada parte do código
    # seja verificada.
    while i < len(codigo):
        
        # Verificação se os dois próximos dígitos na string 'codigo' são iguais a '53'.
        # O fatiamento 'codigo[i:i+2]' extrai uma subcadeia da string 'codigo',
        # começando no índice 'i' e terminando antes de 'i+2', ou seja, pegando
        # dois caracteres a partir de 'i'.
        # Essa subcadeia é então comparada com a string '53' para verificar
        # se representa um espaço.
        if codigo[i:i+2] == '53':

            # Se a condição 'if' for verdadeira, significa que a subcadeia atual representa
            # um espaço na mensagem original.
            # Portanto, um espaço (' ') é adicionado à string 'mensagem'.
            # 'mapeamento_inverso['53']' é usado para obter o caractere correspondente ao código '53',
            # que é um espaço.
            mensagem += mapeamento_inverso['53']

            # Como a subcadeia '53' tem dois caracteres e já foi processada,
            # o índice 'i' é incrementado em 2 para mover para a próxima parte
            # do código que ainda não foi decodificada.
            # Isso é necessário para não reprocessar os mesmos dígitos.
            i += 2



        # Esta linha verifica se a subcadeia de dois dígitos da string 'codigo' (extraída por fatiamento)
        # corresponde a algum caractere no dicionário 'mapeamento_inverso'.
        # O fatiamento 'codigo[i:i+2]' extrai dois caracteres, começando no índice 'i' e terminando antes de 'i+2'.
        # Esse fragmento é então verificado contra o dicionário 'mapeamento_inverso' para ver se ele
        # representa um caractere válido.
        elif codigo[i:i+2] in mapeamento_inverso:

            # Se a condição 'elif' for verdadeira, isso indica que a subcadeia atual (dois dígitos) no código
            # representa um único caractere alfabético, seja letra maiúscula ou minúscula.
            # O método 'mapeamento_inverso[codigo[i:i+2]]' é usado para acessar o caractere correspondente
            # a esses dois dígitos no dicionário 'mapeamento_inverso'.
            # Esse caractere é então adicionado à string 'mensagem', que está sendo construída
            # para formar a mensagem decodificada.
            mensagem += mapeamento_inverso[codigo[i:i+2]]

            # Incrementa o índice 'i' por 2. Isso é feito porque os dois dígitos já foram processados
            # e representam um único caractere. O incremento permite que o loop avance para o próximo conjunto
            # de dígitos ou dígito único no código.
            i += 2

        # Este bloco 'else' é executado se a subcadeia atual não corresponder a '53' (espaço)
        # nem a um par de dígitos que representam um caractere.
        # Isso implica que a subcadeia é um código de um único dígito, representando uma letra maiúscula.
        else:

            # Aqui, o caractere correspondente ao dígito único em 'codigo[i]' é acessado
            # no dicionário 'mapeamento_inverso'. Isso é feito porque, após verificar as outras condições,
            # o único caso restante é um dígito único que mapeia diretamente para uma letra maiúscula.
            # O caractere obtido é então adicionado à string 'mensagem'.
            mensagem += mapeamento_inverso[codigo[i]]

            # Incrementa 'i' por 1, pois apenas um dígito foi processado.
            # Isso permite avançar para o próximo caractere ou par de caracteres
            # na string 'codigo', continuando o processo de decodificação.
            i += 1


    # Esta parte do código é executada após o término do loop 'while'.
    # Neste ponto, todos os caracteres da string 'codigo' foram percorridos e processados.
    # O loop 'while' é usado para decodificar cada parte do código numérico e construir
    # a mensagem decodificada caractere por caractere.
    
    # A variável 'mensagem' agora contém a mensagem decodificada completa.
    # Durante o loop, cada caractere decodificado foi adicionado sequencialmente a 'mensagem'.
    # Portanto, 'mensagem' agora é a representação em texto da string de código numérico original.
    return mensagem  # A função retorna a variável 'mensagem', que é a saída desejada da função.

# Após definir a função, o código abaixo é usado para demonstrar sua funcionalidade.

# Uma string 'codigo' é definida com um valor numérico específico.
# Este código é um exemplo que será usado para testar a função de decodificação.
# Cada número nesta string representa um caractere, conforme o mapeamento definido anteriormente.
codigo = "84136315331454641475327424431403041533947354641"


# A função 'converter_codigo_para_mensagem' é chamada, passando a string 'codigo' como argumento.
# A função processa essa string e retorna a mensagem decodificada correspondente.
# O resultado da função (mensagem decodificada) é então impresso no console.
print(converter_codigo_para_mensagem(codigo))  # A saída esperada é a mensagem "Hoje estou aprendo muito".