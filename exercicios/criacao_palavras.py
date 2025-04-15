"""
32. Exercício: "Jogo de Criação de Palavras"

Descrição: Neste jogo, o jogador recebe várias letras aleatórias e precisa 
        formar a maior quantidade de palavras possível a partir dessas letras. 
        
O jogador tem um limite de tempo para formar as palavras e ganha pontos 
        por cada palavra válida. O jogo termina quando o tempo acaba, e a 
        pontuação final é calculada com base no número de palavras formadas.

Regras:

- O jogador recebe 4 letras aleatórias.
- O jogador tem 60 segundos para formar quantas palavras 
            puder com essas letras.
- Cada palavra formada corretamente dá pontos ao jogador.
"""

import random
import time

# Importa o módulo threading para utilizar temporizadores.
import threading  

# Dicionário simples de palavras válidas usado no jogo.
dicionario_palavras = ["rato", "esto", "ator", "tora", "rosa", "arte", "teor", "rota", "ser", "seta"]

# Função para gerar um conjunto de letras aleatórias a 
        # partir das palavras disponíveis no dicionário.
def gerar_letras_validas(dicionario):
    
    """
    Esta função gera um conjunto de letras únicas que podem ser 
            usadas para formar palavras válidas.
    Ela escolhe uma palavra aleatoriamente do dicionário 
            fornecido e extrai letras únicas dessa palavra,
            garantindo que o jogador tenha a chance de formar 
            pelo menos uma palavra válida completa.
    """

    todas_letras = []  # Lista para armazenar todas as letras das palavras escolhidas.
    
    # Seleciona uma palavra aleatória do dicionário.
    # 'random.choice' é usado para escolher um item 
            # aleatório de uma lista.
    palavra = random.choice(dicionario)
    
    # Adiciona cada letra da palavra escolhida à lista 'todas_letras'.
    # 'list(palavra)' converte a string da palavra em 
            # uma lista de caracteres.
    todas_letras.extend(list(palavra))
    
    # Cria uma lista de letras únicas a partir de 'todas_letras'.
    # 'set(todas_letras)' converte a lista em um conjunto, 
            # que automaticamente remove quaisquer duplicatas.
    letras_unicas = list(set(todas_letras))
    
    # Retorna uma amostra das letras únicas.
    # 'random.sample' é usado para selecionar uma quantidade 
            # específica de itens de uma lista sem repetição.
    # 'min(6, len(letras_unicas))' garante que o número de letras 
            # escolhidas não exceda o número de letras únicas 
            # disponíveis ou seis.
    return random.sample(letras_unicas, min(6, len(letras_unicas)))


# Função para verificar se uma palavra pode ser formada 
        # com as letras disponíveis.
def palavra_valida(palavra, letras_disponiveis):
    
    """
    Esta função determina se a palavra fornecida pelo jogador 
            pode ser formada usando as letras disponíveis.
    Ela verifica cada letra na palavra para garantir que a quantidade 
            dessa letra na palavra não exceda
            a quantidade dessa mesma letra nas letras disponíveis.
    """

    # A função 'all()' verifica se todos os elementos de um 
            # iterável são verdadeiros.
    # A expressão interna 'palavra.count(letra) <= letras_disponiveis.count(letra)' é uma comparação
            # que conta quantas vezes uma letra ocorre na 'palavra' e 
            # compara isso com o número de vezes
            # que a mesma letra ocorre nas 'letras_disponiveis'.
    # O loop 'for letra in palavra' percorre cada letra na 
            # palavra proposta pelo jogador.
    # Se todas as comparações são verdadeiras (i.e., se a 
            # palavra pode ser formada com as letras disponíveis),
            # a função retorna True. Se qualquer letra na 
            # palavra excede a quantidade disponível, retorna False.
    return all(palavra.count(letra) <= letras_disponiveis.count(letra) for letra in palavra)


# Função para encerrar o jogo após o tempo limite.
def encerrar_jogo():
    
    """
    Esta função é chamada quando o temporizador do jogo expira.
    Ela define a variável global 'jogo_ativo' como False, o que é 
            verificado no loop principal do jogo
            para encerrar a sessão de jogo.
    """

    # Declara que a função modificará a variável global 'jogo_ativo'.
    global jogo_ativo  

    # Altera o valor de 'jogo_ativo' para False, indicando 
            # que o jogo terminou.
    jogo_ativo = False  




# Definição da função principal do jogo.
def jogo_criacao_palavras():
    
    """
    Gerencia o jogo de criação de palavras onde o jogador forma 
            palavras a partir de letras aleatórias.
    O jogador tem um tempo limitado para formar as palavras e 
            ganha pontos por cada palavra válida formada.
    """

    # Chama a função para gerar um conjunto de letras aleatórias que 
            # podem ser usadas para formar palavras.
    letras_disponiveis = gerar_letras_validas(dicionario_palavras)
    
    # Imprime uma mensagem de boas-vindas e as regras básicas do jogo.
    print("Bem-vindo ao Jogo de Criação de Palavras!")
    print("Você tem 60 segundos para formar palavras.")
    print(f"Letras disponíveis: {', '.join(letras_disponiveis).upper()}\n")

    # Define uma variável global 'jogo_ativo' para controlar o 
            # fluxo do jogo dentro do loop.
    global jogo_ativo

    # Inicializa o jogo como ativo.
    jogo_ativo = True  
    
    # Inicializa variáveis para rastrear a pontuação e as 
            # palavras que o jogador já formou.
    pontuacao = 0
    palavras_formadas = []

    # Configura um temporizador de 60 segundos que chamará a 
            # função 'encerrar_jogo' quando o tempo expirar.
    temporizador = threading.Timer(10, encerrar_jogo)

    # Ativa o temporizador para iniciar a contagem regressiva.
    temporizador.start()  

    # Loop principal do jogo que continua enquanto 'jogo_ativo' for True.
    while jogo_ativo:
        
        # Solicita ao jogador para inserir uma palavra 
                # usando as letras disponíveis.
        palavra = input("Digite uma palavra: ").lower()

        # Verifica se o temporizador já terminou para parar 
                # de aceitar novas entradas.
        if not jogo_ativo:
            break

        # Checa se a palavra inserida está no dicionário de palavras 
                # válidas e se pode ser formada com as letras disponíveis.
        if palavra in dicionario_palavras and palavra_valida(palavra, letras_disponiveis):
            
            # Confere se a palavra já foi formada anteriormente 
                    # para evitar duplicatas.
            if palavra not in palavras_formadas:

                # Adiciona a palavra válida à lista de palavras formadas.
                palavras_formadas.append(palavra)  
                
                # Adiciona pontos à pontuação do jogador.
                pontuacao += 10  
                print(f"Correto! +10 pontos.\n")
                
            else:
                
                # Informa ao jogador que a palavra já foi usada.
                print("Você já formou essa palavra.\n")
                
        else:
            
            # Informa ao jogador que a palavra é inválida.
            print("Incorreto! Essa palavra não pode ser formada com as letras disponíveis.\n")

    # Após o término do jogo, mostra as palavras possíveis 
            # que poderiam ter sido formadas.
    # Esta seção é executada depois que o temporizador 
            # termina e o loop do jogo é encerrado.
    palavras_possiveis = [

        # Itera sobre cada palavra no dicionário de 
                # palavras válido.
        palavra for palavra in dicionario_palavras  

        # Inclui a palavra na lista se ela pode ser formada 
                # com as letras disponíveis.
        if palavra_valida(palavra, letras_disponiveis)  
        
    ]
    
    # A lista 'palavras_possiveis' agora contém todas as palavras do 
            # dicionário que o jogador poderia ter formado
    # com as letras que foram dadas, considerando que elas atendem às 
            # regras de formação de palavras estabelecidas
            # pela função 'palavra_valida'. Esta função verifica se a 
            # quantidade de cada letra na palavra não excede
            # a quantidade dessa letra nas letras disponíveis.
    
    # Exibe o resultado final, incluindo o número total de 
            # palavras formadas e a pontuação.
    # A mensagem final fornece feedback ao jogador sobre seu 
            # desempenho e também oferece uma visão do que poderia
            # ter sido alcançado, o que pode ser motivador e educativo.
    print(f"\nVocê formou {len(palavras_formadas)} palavras e ganhou {pontuacao} pontos.")

    # Mostra a lista de palavras que o jogador poderia ter formado. 
    # Isso pode ajudar o jogador a aprender novas palavras
            # e a entender melhor como usar as letras de maneira eficaz.
    print(f"Palavras que poderiam ser formadas com as letras disponíveis: {', '.join(palavras_possiveis)}")


# ["rato", "esto", "ator", "tora", "rosa", "arte", "teor", "rota", "ser", "seta"]

# Inicia o jogo
jogo_criacao_palavras()