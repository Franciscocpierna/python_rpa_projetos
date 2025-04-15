"""
29. Exercício: "Criptografia de Substituição"

Descrição: Neste exercício, o jogador deve decifrar uma mensagem criptografada 
        usando uma substituição de letras. O programa gera uma mensagem oculta, 
        onde cada letra foi substituída por outra letra. 
        
O jogador deve tentar adivinhar qual é a substituição correta, letra por letra, 
        para revelar a mensagem original. A cada tentativa, o programa revela as 
        letras corretas ou informa se o jogador errou.

Regras:

- O jogador recebe uma mensagem criptografada com substituição de 
        letras (exemplo: 'A' foi substituído por 'X', 'B' por 'Y', etc.).
- O jogador deve tentar adivinhar a correspondência entre as letras.
- O programa verifica a resposta e atualiza a mensagem com as 
        letras corretas a cada tentativa.
- O jogo termina quando a mensagem inteira for decifrada.
"""

# Importa os módulos necessários para o jogo.
import random
import string

# Função para criar um mapa de substituição de letras aleatórias.
def gerar_criptografia():
    
    """
    Esta função gera um dicionário de substituição de letras, 
            onde cada letra do alfabeto é mapeada para outra letra aleatória, 
            sem repetições, efetivamente criando uma cifra de 
            substituição monoalfabética.
    """

    # Gera uma lista das letras do alfabeto em minúscula.
    # 'string.ascii_lowercase' é uma string pré-definida em 
            # Python que contém todas as letras de 'a' a 'z'.
    # Ao converter essa string para uma lista, cada letra se 
            # torna um elemento separado da lista.
    letras = list(string.ascii_lowercase)
    
    # Embaralha a lista de letras para criar uma sequência aleatória.
    # 'random.shuffle' recebe uma lista e reorganiza seus 
            # elementos em ordem aleatória.
    # Isso é crucial para garantir que a cifra de 
            # substituição não seja previsível.
    random.shuffle(letras)
    
    # Cria um dicionário que mapeia cada letra do alfabeto a 
            # uma letra embaralhada.
    # Este dicionário é criado usando compreensão de dicionário, 
            # que é uma forma concisa de construir dicionários em Python.
    # 'chr(i + 97)' converte um inteiro em um caractere, 
            # onde 97 é o código ASCII para 'a'.
    # O loop 'for i in range(26)' itera 26 vezes, 
            # correspondendo às 26 letras do alfabeto.
    # Para cada iteração, uma letra do alfabeto (a partir de 'a') é 
            # associada a uma letra na lista embaralhada.
    substituicao = {chr(i + 97): letras[i] for i in range(26)}
    
    # Retorna o dicionário de substituição.
    # Este dicionário será usado para substituir as letras na 
            # mensagem original durante a criptografia.
    return substituicao


# Função para criptografar uma mensagem usando o mapa de substituição.
def criptografar_mensagem(mensagem, substituicao):
    
    """
    Esta função aceita uma 'mensagem' (string) e um 'substituicao' (dicionário) 
            que contém o mapa de substituição de letras.
    Retorna a mensagem criptografada onde cada letra é substituída 
            por sua correspondente no dicionário.
    """

    # A função utiliza uma compreensão de lista para iterar sobre 
            # cada caractere 'c' na 'mensagem'.
    # O método 'substituicao.get(c, c)' tenta obter a substituição 
            # para o caractere 'c'.
    # Se 'c' é uma chave no dicionário 'substituicao', retorna o 
            # valor correspondente (letra substituta).
    # Se 'c' não é uma chave no dicionário (como no caso de espaços, 
            # pontuação ou caracteres que não foram mapeados),
    # retorna 'c' como está, mantendo o caractere original na 
            # mensagem criptografada.
    # 'join' é usado para concatenar todos os caracteres 
            # processados de volta em uma única string.
    return ''.join(substituicao.get(c, c) for c in mensagem)


# Função para decifrar a mensagem com as letras adivinhadas pelo usuário.
def decifrar_mensagem(mensagem, mapeamento_usuario):
    
    """
    Esta função decifra a mensagem criptografada usando as 
            adivinhações do usuário armazenadas em 'mapeamento_usuario'.
    Cada letra criptografada é substituída pela letra adivinhada 
            correspondente ou, se não adivinhada, por '*'.
    """

    # A função também usa uma compreensão de lista para processar 
            # cada caractere 'c' na 'mensagem'.
    # 'mapeamento_usuario.get(c, '*')' tenta obter a letra 
            # adivinhada para o caractere 'c'.
    # Se 'c' é uma letra e está no 'mapeamento_usuario', 
            # retorna a letra adivinhada.
    # Se 'c' não foi adivinhado ou não é uma letra (como espaços 
            # ou pontuação), verifica-se com 'c.isalpha()'.
    # Se 'c.isalpha()' for False, o caractere 'c' é retornado como está.
    # Caso contrário, se não houver adivinhação para 'c', retorna '*' 
            # para indicar que a letra ainda precisa ser adivinhada.
    return ''.join(mapeamento_usuario.get(c, '*') if c.isalpha() else c for c in mensagem)


# Função principal que organiza a lógica do jogo de criptografia.
def jogo_criptografia():
    
    """
    Esta função coordena o fluxo do jogo de criptografia, 
            onde uma mensagem é criptografada
            e o jogador deve adivinhar a substituição 
            de letras para decifrá-la.
    """

    # Define a mensagem original que será criptografada.
    # Neste exemplo, a mensagem é uma string simples 
            # para facilitar o entendimento.
    mensagem_original = "este e um teste"
    
    # Gera o mapa de substituição de letras utilizando a 
            # função definida anteriormente.
    # Esta função cria um mapeamento aleatório de cada letra 
            # do alfabeto para outra letra.
    substituicao = gerar_criptografia()
    
    # Criptografa a mensagem original usando o mapa de 
            # substituição gerado.
    # A mensagem resultante será uma versão da mensagem original 
            # onde cada letra foi substituída
            # conforme o mapeamento definido em 'substituicao'.
    mensagem_criptografada = criptografar_mensagem(mensagem_original, substituicao)

    # Exibe a mensagem criptografada para o jogador, dando a 
            # ele o ponto de partida para decifrar.
    print(f"Mensagem criptografada: {mensagem_criptografada}")
    
    # Inicializa um dicionário para armazenar as adivinhações do 
            # usuário sobre a substituição de letras.
    mapeamento_usuario = {}

    # Decifra inicialmente a mensagem criptografada 
            # substituindo letras conhecidas pelo usuário
    # e marcando letras desconhecidas com '*' para indicar 
            # que ainda não foram decifradas.
    mensagem_decifrada = decifrar_mensagem(mensagem_criptografada, mapeamento_usuario)
    print(f"Mensagem decifrada até agora: {mensagem_decifrada}\n")

    # Loop de adivinhação onde o usuário tenta identificar 
            # as substituições corretas.
    while True:
        
        # Solicita ao usuário que digite a letra criptografada 
                # que deseja substituir.
        letra_criptografada = input("Digite a letra criptografada que você quer decifrar: ").lower()
        
        # Solicita ao usuário a letra que ele acredita ser a 
                # original correspondente à criptografada.
        letra_real = input(f"Qual é a letra original correspondente a '{letra_criptografada}'?: ").lower()

        # Adiciona a correspondência entre a letra criptografada e a 
                # suposta letra real ao mapeamento do usuário.
        mapeamento_usuario[letra_criptografada] = letra_real

        # Atualiza a mensagem decifrada com as novas 
                # adivinhações do usuário.
        mensagem_decifrada = decifrar_mensagem(mensagem_criptografada, mapeamento_usuario)
        print(f"\nMensagem decifrada até agora: {mensagem_decifrada}\n")

        # Verifica se a mensagem foi completamente decifrada, ou 
                # seja, se não contém mais o caractere '*'.
        if '*' not in mensagem_decifrada:
            
            # Se a mensagem está completamente decifrada, exibe uma 
                    # mensagem de parabéns e termina o loop.
            print("Parabéns! Você decifrou a mensagem completa!")
            break

# Chamada da função para iniciar o jogo.
jogo_criptografia()