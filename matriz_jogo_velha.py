"""
Exercício - Jogo da Velha com Matriz

Objetivo: Implementar o jogo da velha usando uma matriz 3x3 e permitir que dois jogadores joguem um contra o outro.

Instruções:

    Inicialize uma matriz 3x3 com espaços em branco para representar o tabuleiro do jogo da velha.
    Crie uma função para exibir o tabuleiro atualizado a cada jogada.
    Crie uma função para verificar se há um vencedor.
    Implemente um loop que alterna entre os jogadores (X e O) e permite que eles escolham uma posição no tabuleiro.
    Após cada jogada, verifique se há um vencedor ou se o tabuleiro está cheio.
    Se houver um vencedor ou o tabuleiro estiver cheio, termine o jogo e exiba o resultado.

Dicas:

    Lembre-se de verificar as linhas, colunas e diagonais ao procurar por um vencedor.
    Certifique-se de que os jogadores não possam escolher uma posição que já foi ocupada.
    Use funções para organizar seu código e torná-lo mais legível.

"""

#Solução:

# Inicializa o tabuleiro
# tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

# Inicializa o tabuleiro como uma lista vazia
tabuleiro = []

# Loop para adicionar 3 linhas ao tabuleiro
for i in range(3):
    
    # Cria uma linha vazia
    linha = []
    
    # Loop para adicionar 3 espaços em branco a cada linha
    for j in range(3):
        
        # Adiciona um espaço em branco à linha
        linha.append(' ')
        
    # Adiciona a linha completa ao tabuleiro
    tabuleiro.append(linha)
    
def exibir_tabuleiro():
    
    """Exibe o tabuleiro atual."""
    
    # Loop para percorrer cada linha do tabuleiro
    for linha in tabuleiro:
        
        # Imprime a linha atual do tabuleiro, separando cada célula por "|"
        print("|".join(linha))
        
        # Imprime um separador para visualizar melhor as linhas do tabuleiro
        print("-" * 5)
    
    
def verificar_vencedor(jogador):
    
    """Verifica se o jogador atual é o vencedor."""
    
    # Loop para percorrer as linhas e colunas do tabuleiro
    for i in range(3):
        
        # Inicializa variáveis para verificar se todas as células são iguais ao jogador
        todas_celulas_linha = True
        todas_celulas_coluna = True
        
        # Loop para percorrer cada  coluna(j) da linha atual (i)
        for j in range(3):

            # Verifica se a célula atual na linha (i) e coluna (j) é diferente do jogador
            # Se for diferente, atualiza a variável 'todas_celulas_linha' para False
            if tabuleiro[i][j] != jogador:
                todas_celulas_linha = False

            # Verifica se a célula atual na coluna (i) e linha (j) é diferente do jogador
            # Se for diferente, atualiza a variável 'todas_celulas_coluna' para False
            if tabuleiro[j][i] != jogador:
                todas_celulas_coluna = False
                
        """
        Parte onde é verificado se um jogador venceu o jogo:

        Verificação de Linhas e Colunas:
        As variáveis todas_celulas_linha e todas_celulas_coluna são inicializadas como 
        True para cada iteração do loop que percorre as linhas e colunas do tabuleiro. Isso 
        acontece para cada valor de i, que representa o índice da linha atual. O loop interno 
        percorre as colunas (índices de j) para cada linha. Durante a iteração, se uma célula na 
        linha i e coluna j não contiver o símbolo do jogador atual, a respectiva variável todas_celulas_linha 
        ou todas_celulas_coluna é definida como False. Isso acontece para garantir que todas as células em uma 
        linha ou coluna sejam do mesmo jogador.

        Se, após as iterações do loop, todas_celulas_linha ou todas_celulas_coluna forem True, isso significa 
        que todas as células na linha ou coluna contêm o símbolo do jogador atual, o que resulta em uma vitória.

        Verificação de Diagonais:
        As duas diagonais do tabuleiro são verificadas separadamente. A primeira diagonal (de cima à esquerda 
        para baixo à direita) é verificada comparando os elementos das células (0, 0), (1, 1) e (2, 2) com o 
        símbolo do jogador atual. A segunda diagonal (de cima à direita para baixo à esquerda) é verificada comparando 
        os elementos das células (0, 2), (1, 1) e (2, 0).

        Se uma das diagonais contiver apenas o símbolo do jogador atual, isso indica uma vitória.

        Retorno de Resultado:
        Se qualquer uma das condições acima for verdadeira (ou seja, uma linha, coluna ou diagonal contém apenas
        o símbolo do jogador atual), a função retorna True, indicando que o jogador venceu. Se nenhuma das condições 
        for atendida, isso significa que não há vencedor e a função retorna False.

        Essa estratégia verifica todas as possibilidades onde um jogador pode ganhar o jogo: todas as linhas, 
        colunas e diagonais. Se alguma dessas condições for atendida, a função verificar_vencedor retorna True, caso 
        contrário, retorna False.
        """
                
        # Se todas as células em uma linha ou coluna são iguais ao jogador
        if todas_celulas_linha or todas_celulas_coluna:
            return True
        
        # Verifica a diagonal principal (de cima à esquerda para baixo à direita)
        if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
            return True

        # Verifica a diagonal secundária (de cima à direita para baixo à esquerda)
        if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
            return True

        # Se nenhuma das condições acima for atendida, retorna False (não há vencedor)
        return False

def jogada(jogador):
    
    """Permite ao jogador atual fazer uma jogada."""
    
    # Inicia um loop infinito para garantir que o jogador faça uma jogada válida
    while True:
        
        # Solicita ao jogador que insira a linha e a coluna onde deseja jogar
        jogada = input(f"Jogador {jogador}, escolha a linha e coluna (ex: 0 2): ")

        # Tenta converter a entrada do jogador em coordenadas de linha e coluna
        try:
            
            """
            jogada.split(): A função split() é um método de strings que divide uma string em 
            uma lista, usando espaços como delimitadores por padrão. Por exemplo, se jogada for 
            a string "1 2", então jogada.split() retornará a lista ['1', '2'].

            map(int, jogada.split()): A função map() aplica uma função a todos os itens em 
            uma entrada de lista (ou qualquer outro iterável). Neste caso, estamos aplicando a 
            função int a cada item da lista resultante de jogada.split(). Isso converte cada string 
            da lista em um número inteiro. Continuando com o exemplo anterior, isso transformaria ['1', '2'] em [1, 2].

            linha, coluna = ...: Isso é chamado de desempacotamento de lista. Estamos 
            atribuindo os valores da lista resultante às variáveis linha e coluna. No exemplo dado, 
            linha receberia o valor 1 e coluna receberia o valor 2
            """
            linha, coluna = map(int, jogada.split())
            
            # Verifica se a célula escolhida no tabuleiro está vazia (representada por um espaço em branco)
            if tabuleiro[linha][coluna] == ' ':

                # Se estiver vazia, atualiza a célula com o símbolo do jogador atual (X ou O)
                tabuleiro[linha][coluna] = jogador

                # Sai do loop, pois a jogada foi válida
                break

            # Se a célula já estiver ocupada (não estava vazia)
            else:

                # Informa ao jogador que a posição escolhida já está ocupada
                print("Posição já ocupada. Tente novamente.")


        # Se ocorrer um erro (entrada inválida ou fora do intervalo), informa ao jogador
        except:
            print("Entrada inválida. Tente novamente.")


# Loop principal do jogo
# Define o jogador inicial como 'X'
jogador_atual = 'X'

# Inicia um loop para as 9 possíveis jogadas no jogo da velha

"""
    range(9): A função range(9) retorna uma sequência de números, começando 
    de 0 e indo até 8 (um total de 9 números). Portanto, o loop irá iterar 9 vezes.

    for _ in ...: Aqui, estamos usando um loop for para iterar sobre cada número 
    na sequência retornada por range(9).

    _: O sublinhado (_) é uma convenção em Python que indica que a variável não será 
    usada dentro do loop. É uma maneira de dizer "estamos iterando 9 vezes, mas não nos 
    importamos com o valor específico em cada iteração". Em outras palavras, estamos 
    interessados apenas no número de iterações, e não no valor em cada iteração.

    Então, em resumo, a linha for _ in range(9): é uma maneira concisa de escrever
    um loop que se repete 9 vezes, sem se preocupar com o valor da variável de loop 
    em cada iteração.

"""
for _ in range(9):
    
    # Exibe o tabuleiro atualizado
    exibir_tabuleiro()
    
    # Permite que o jogador atual faça sua jogada
    jogada(jogador_atual)
    
    # Verifica se a jogada resultou em uma vitória para o jogador atual
    if verificar_vencedor(jogador_atual):
        
        # Exibe o tabuleiro final
        exibir_tabuleiro()
        
        # Informa que o jogador atual venceu o jogo
        print(f"Jogador {jogador_atual} venceu!")
        
        # Encerra o loop, pois o jogo terminou
        break
    
    # Alterna o jogador atual (de 'X' para 'O' ou vice-versa)
    jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Caso o loop termine sem encontrar um vencedor (todas as 9 jogadas foram feitas)
else:
    
    # Exibe o tabuleiro final
    exibir_tabuleiro()
    
    # Informa que o jogo terminou em empate
    print("Empate!")