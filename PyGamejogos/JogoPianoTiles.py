# Importa a biblioteca pygame, que é usada para criar
        # jogos e interfaces gráficas.
import pygame

# Importa a biblioteca random para geração de números aleatórios.
import random

# Importa a biblioteca sys para interagir com o sistema,
        # permitindo manipular a execução do programa.
import sys

# Importa a biblioteca os para interação com o sistema 
        # operacional, como manipular arquivos e diretórios.
import os

# Inicializa todos os módulos importados de pygame, 
        # necessários para o funcionamento dos jogos.
pygame.init()

# Define a largura da tela do jogo.
LARGURA_TELA = 400

# Define a altura da tela do jogo.
ALTURA_TELA = 600

# Define o tamanho de cada tile (quadrado clicável) no jogo.
TAMANHO_TILE = 100

# Define a velocidade com que os tiles se movem na tela.
VELOCIDADE_TILE = 5

# Define a cor branca no formato RGB.
BRANCO = (255, 255, 255)

# Define a cor preta no formato RGB.
PRETO = (0, 0, 0)

# Define a cor verde no formato RGB.
VERDE = (0, 255, 0)

# Define a cor vermelha no formato RGB.
VERMELHO = (255, 0, 0)

# Configura a tela de display do jogo usando as dimensões 
        # especificadas e armazena essa configuração na variável 'tela'.
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Define o título da janela do jogo que aparece na 
        # barra de título da janela.
pygame.display.set_caption("Piano Tiles")

# Cria um objeto de fonte para uso no jogo, especificando o
        # estilo e tamanho da fonte para pontuação.
fonte = pygame.font.Font(None, 36)

# Cria um objeto de fonte maior para uso nos títulos de menu no jogo.
fonte_menu = pygame.font.Font(None, 48)

# Inicializa a variável que guarda a pontuação atual do jogador.
pontuacao = 0

# Inicializa a variável que guarda a pontuação acumulada
        # do jogador ao longo das sessões.
pontuacao_acumulada = 0

# Inicializa a lista que armazenará os tiles 
        # criados durante o jogo.
tiles = []

# Define o intervalo de tempo em milissegundos
        # entre a criação de cada tile.
tempo_tile = 1000

# Armazena o momento da última criação de um tile 
        # para controlar a criação de novos tiles.
ultima_criacao_tile = pygame.time.get_ticks()

# Inicializa a variável que define o modo de jogo, 
        # que pode ser alterado no menu.
modo_jogo = None

# Inicializa a variável que armazena o próximo número a 
        # ser tocado no modo de jogo 'sequencia'.
proximo_numero_sequencia = 1

# Define o nome do arquivo usado para salvar a pontuação acumulada.
ARQUIVO_PONTUACAO = "pontuacao_acumulada.txt"


# Define a função para carregar a pontuação acumulada 
        # de sessões anteriores do jogo
def carregar_pontuacao():
    
    # Declara que a variável 'pontuacao_acumulada' será 
            # utilizada como uma variável global dentro desta função
    global pontuacao_acumulada
    
    # Verifica se o arquivo de pontuação existe no diretório atual
    if os.path.exists(ARQUIVO_PONTUACAO):
    
        # Abre o arquivo de pontuação em modo leitura
        with open(ARQUIVO_PONTUACAO, "r") as arquivo:
        
            # Tenta ler e converter o conteúdo do arquivo para inteiro e
                    # armazenar na variável 'pontuacao_acumulada'
            try:
                pontuacao_acumulada = int(arquivo.read())
            
            # Caso haja um erro na conversão devido ao conteúdo não 
                    # ser um inteiro válido
            except ValueError:
            
                # Define a pontuação acumulada como 0 se o conteúdo do
                        # arquivo não puder ser convertido em um inteiro
                pontuacao_acumulada = 0



# Define a função para salvar a pontuação acumulada 
        # do jogo em um arquivo de texto
def salvar_pontuacao():
    
    # Abre (ou cria, se não existir) o arquivo especificado 
            # no modo de escrita
    with open(ARQUIVO_PONTUACAO, "w") as arquivo:
        
        # Escreve a pontuação acumulada no arquivo, 
                # convertendo-a primeiro para string
        arquivo.write(str(pontuacao_acumulada))



# Define a função responsável por criar um novo tile (quadrado) no jogo
def criar_tile():
    
    # Calcula uma posição 'x' aleatória para o novo tile, escolhendo 
            # entre 0 e 3, multiplicado pelo tamanho do tile,
            # garantindo que o tile apareça em uma das quatro 
            # colunas possíveis na tela.
    x = random.randint(0, 3) * TAMANHO_TILE
    
    # Verifica se o modo de jogo atual é "sequencia", um modo 
            # onde os tiles devem ser tocados em uma ordem numérica crescente
    if modo_jogo == "sequencia":
    
        # Determina o número que aparecerá no tile, com uma probabilidade
                # de 70% de ser o próximo número sequencial esperado
        # Essa alta probabilidade ajuda a manter o desafio focado em
                # seguir a sequência corretamente.
        if random.random() < 0.7:
        
            # Atribui ao tile o próximo número na sequência
                    # que o jogador deve tocar
            numero = proximo_numero_sequencia
        
        else:
        
            # Atribui um número aleatório dentro de um intervalo de 10 
                    # números acima do próximo esperado,
                    # introduzindo uma variação e dificuldade
                    # adicional ao jogo.
            numero = random.randint(proximo_numero_sequencia, proximo_numero_sequencia + 10)
        
        # Cria um objeto rect (retângulo) do Pygame na posição x calculada, 
                # no topo da tela, com largura e altura definidas por TAMANHO_TILE
        tile = pygame.Rect(x, 0, TAMANHO_TILE, TAMANHO_TILE)
        
        # Adiciona o novo tile à lista de tiles, junto com suas propriedades
                # de cor (PRETO) e o número designado.
        # O último valor 'numero' é uma redundância para facilitar a 
                # verificação de jogo ou futuras extensões de lógica.
        tiles.append((tile, PRETO, numero, numero))


    # Verifica se o modo de jogo atual é "pares", onde o jogador 
            # deve tocar apenas em tiles que mostram números pares.
    elif modo_jogo == "pares":

        # Gera um número aleatório entre 1 e 100 para ser exibido no tile.
        numero = random.randint(1, 100)

        # Cria um objeto rect (retângulo) do Pygame na posição x calculada, 
                # no topo da tela, com largura e altura definidas por TAMANHO_TILE.
        tile = pygame.Rect(x, 0, TAMANHO_TILE, TAMANHO_TILE)

        # Adiciona o novo tile à lista de tiles com suas propriedades: posição, 
                # cor (PRETO), número gerado, e o número repetido para consistência.
        tiles.append((tile, PRETO, numero, numero))
    
    # Verifica se o modo de jogo atual é "cores", onde os tiles devem ser
            # identificados e tocados com base na cor do texto e fundo.
    elif modo_jogo == "cores":

        # Define uma lista de tuplas contendo nomes de cores e seus 
                # respectivos valores RGB.
        cores = [("Verde", VERDE), ("Vermelho", VERMELHO)]

        # Escolhe aleatoriamente uma das tuplas de cores para 
                # determinar a cor de fundo do tile.
        nome_cor_fundo, cor_fundo = random.choice(cores)

        # Escolhe aleatoriamente uma das cores para o texto do tile. 
        # Aqui, a escolha é restrita a "Verde" ou "Vermelho".
        nome_cor_texto = random.choice(["Verde", "Vermelho"])
        
        # Cria um objeto rect (retângulo) do Pygame na posição x calculada, 
                # no topo da tela, com largura e altura definidas por TAMANHO_TILE.
        tile = pygame.Rect(x, 0, TAMANHO_TILE, TAMANHO_TILE)

        # Adiciona o novo tile à lista de tiles com suas propriedades: posição,
                # cor de fundo escolhida, nome da cor do texto, e None,
                # pois não há número associado.
        tiles.append((tile, cor_fundo, nome_cor_texto, None))


    # Este bloco else trata dos modos de jogo "normal" e "verde". Se não for um 
            # dos modos específicos anteriores, ele executa este código.
    else:
        
        # Define a cor do tile baseada no modo de jogo. No modo "verde", há 
                # uma chance de 30% de que o tile seja verde, caso contrário será preto.
        # Essa probabilidade é controlada pela função random.random() que gera
                # um número entre 0 e 1, e se for menor que 0.3, o tile será verde.
        cor_tile = VERDE if modo_jogo == "verde" and random.random() < 0.3 else PRETO
    
        # Cria um objeto rect (retângulo) do Pygame. O retângulo é 
                # posicionado na coordenada x calculada anteriormente,
                # começa no topo da tela (y = 0), e tem a largura e
                # altura definidas por TAMANHO_TILE.
        tile = pygame.Rect(x, 0, TAMANHO_TILE, TAMANHO_TILE)
    
        # Adiciona o novo tile à lista de tiles. No modo "normal" ou
                # quando o modo "verde" não gera um tile verde,
        # o tile terá cor preta. Neste caso, o conteúdo do tile (número
                # ou texto) é definido como None,
                # pois não há informação específica a ser exibida 
                # no tile além da cor.
        tiles.append((tile, cor_tile, None, None))



# Define a função responsável por desenhar os elementos 
        # gráficos do jogo na tela
def desenhar_jogo():
    
    # Preenche a tela com a cor branca antes de desenhar qualquer coisa, 
            # garantindo que a tela esteja limpa a cada atualização.
    tela.fill(BRANCO)
    
    # Itera sobre a lista de tiles, onde cada tile é representado por uma
            # tupla contendo informações sobre sua forma, cor e conteúdo.
    for tile, cor, conteudo, resultado in tiles:
    
        # Desenha um retângulo (tile) na tela na posição especificada pelo 
                # objeto 'tile', preenchido com a 'cor' especificada.
        pygame.draw.rect(tela, cor, tile)
        
        # Verifica se o modo de jogo atual requer que algum conteúdo seja 
                # exibido nos tiles (números ou textos).
        if modo_jogo in ["sequencia", "pares", "cores"]:
        
            # Renderiza o texto a ser exibido no tile, configurando a cor do
                    # texto para branco a menos que a cor do tile seja
                    # branca, nesse caso, usa preto.
            texto_conteudo = fonte.render(str(conteudo), True, BRANCO if cor != BRANCO else PRETO)
            
            # Posiciona o texto renderizado no centro do tile, ajustando com
                    # base na largura e altura do texto.
            tela.blit(texto_conteudo, (tile.x + TAMANHO_TILE // 2 - texto_conteudo.get_width() // 2, tile.y + TAMANHO_TILE // 2 - texto_conteudo.get_height() // 2))
    
    # Renderiza o texto da pontuação atual do jogador, formatando o número 
            # com separadores de milhares e configurando a cor do texto para preto.
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao:,}", True, PRETO)
    
    # Renderiza o texto da pontuação acumulada do jogador,
            # similarmente formatada e colorida.
    texto_acumulada = fonte.render(f"Total: {pontuacao_acumulada:,}", True, PRETO)
    
    # Posiciona o texto da pontuação no canto superior 
            # esquerdo da tela.
    tela.blit(texto_pontuacao, (10, 10))
    
    # Posiciona o texto da pontuação acumulada um pouco 
            # abaixo do texto da pontuação atual.
    tela.blit(texto_acumulada, (10, 40))

    # Atualiza a tela inteira para refletir os novos desenhos feitos.
    pygame.display.flip()



# Define a função responsável por exibir o menu inicial do jogo.
def mostrar_menu():
    
    # Limpa a tela preenchendo-a com a cor branca para garantir que
            # nenhum gráfico anterior interfira na visualização do menu.
    tela.fill(BRANCO)
    
    # Renderiza o título do jogo "Piano Tiles" usando a fonte do menu, 
            # configurando a cor do texto para preto.
    titulo = fonte_menu.render("Piano Tiles", True, PRETO)
    
    # Posiciona o título no centro horizontal da tela e a 100 pixels do
            # topo, ajustando baseado na largura do texto renderizado.
    tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 100))
    
    # Renderiza a opção "1. Modo Normal" para seleção no menu, 
            # configurando a cor do texto para preto.
    opcao1 = fonte.render("1. Modo Normal", True, PRETO)
    
    # Posiciona essa opção no centro da tela e 200 pixels do topo, 
            # centralizando-a horizontalmente.
    tela.blit(opcao1, (LARGURA_TELA // 2 - opcao1.get_width() // 2, 200))
    
    # Renderiza a opção "2. Modo Apenas Verde", com texto em preto.
    opcao2 = fonte.render("2. Modo Apenas Verde", True, PRETO)
    
    # Posiciona esta opção 250 pixels do topo, alinhada
            # horizontalmente ao centro da tela.
    tela.blit(opcao2, (LARGURA_TELA // 2 - opcao2.get_width() // 2, 250))
    
    # Renderiza a opção "3. Modo Apenas Números Pares", com texto em preto.
    opcao3 = fonte.render("3. Modo Apenas Números Pares", True, PRETO)
    
    # Posiciona esta opção 300 pixels do topo, centralizando-a na tela.
    tela.blit(opcao3, (LARGURA_TELA // 2 - opcao3.get_width() // 2, 300))
    
    # Renderiza a opção "4. Modo Cores Corretas", com texto em preto.
    opcao4 = fonte.render("4. Modo Cores Corretas", True, PRETO)
    
    # Posiciona esta opção 350 pixels do topo, alinhada ao centro da tela.
    tela.blit(opcao4, (LARGURA_TELA // 2 - opcao4.get_width() // 2, 350))
    
    # Renderiza a opção "5. Modo Sequência Crescente", com texto em preto.
    opcao5 = fonte.render("5. Modo Sequência Crescente", True, PRETO)
    
    # Posiciona esta opção 400 pixels do topo, centralizando-a horizontalmente.
    tela.blit(opcao5, (LARGURA_TELA // 2 - opcao5.get_width() // 2, 400))
    
    # Atualiza a tela para exibir todas as opções do menu 
            # que foram renderizadas.
    pygame.display.flip()



# Define a função principal que gerencia o fluxo geral do jogo.
def main():
    
    # Declara que várias variáveis globais serão usadas e potencialmente
            # modificadas dentro desta função.
    global pontuacao, pontuacao_acumulada, VELOCIDADE_TILE, ultima_criacao_tile, modo_jogo, proximo_numero_sequencia
    
    # Chama a função para carregar a pontuação acumulada de 
            # sessões anteriores do jogo.
    carregar_pontuacao()

    # Inicia um loop infinito que mantém o jogo rodando até 
            # que o jogador decida sair.
    while True:
        
        # Inicializa a variável para controlar se o menu está sendo exibido.
        em_menu = True
        
        # Mantém o menu na tela enquanto o jogador não seleciona uma opção.
        while em_menu:
            
            # Chama a função para desenhar e exibir o menu de 
                    # opções do jogo na tela.
            mostrar_menu()
            
            # Processa todos os eventos de entrada (como cliques de
                    # teclado e fechamento da janela).
            for evento in pygame.event.get():
                
                # Verifica se o tipo do evento é QUIT, indicando que o
                        # jogador deseja fechar o jogo.
                if evento.type == pygame.QUIT:
                
                    # Salva a pontuação acumulada antes de sair.
                    salvar_pontuacao()
                    
                    # Encerra o Pygame para liberar recursos.
                    pygame.quit()
                    
                    # Sai do programa.
                    sys.exit()
                    
                # Verifica se uma tecla foi pressionada.
                elif evento.type == pygame.KEYDOWN:
                    
                    # Verifica se a tecla "1" foi pressionada.
                    if evento.key == pygame.K_1:
                        
                        # Define o modo de jogo como "normal".
                        modo_jogo = "normal"
                        
                        # Muda a variável 'em_menu' para False, saindo do loop do
                                # menu e iniciando o jogo no modo normal.
                        em_menu = False
                    
                    # Verifica se a tecla "2" foi pressionada.
                    elif evento.key == pygame.K_2:
                        
                        # Define o modo de jogo como "verde".
                        modo_jogo = "verde"
                        
                        # Muda a variável 'em_menu' para False, saindo do loop do
                                # menu e iniciando o jogo no modo verde.
                        em_menu = False
                    
                    # Verifica se a tecla "3" foi pressionada.
                    elif evento.key == pygame.K_3:
                        
                        # Define o modo de jogo como "pares".
                        modo_jogo = "pares"
                        
                        # Muda a variável 'em_menu' para False, saindo do loop do
                                # menu e iniciando o jogo no modo pares.
                        em_menu = False
                    
                    # Verifica se a tecla "4" foi pressionada.
                    elif evento.key == pygame.K_4:
                        
                        # Define o modo de jogo como "cores".
                        modo_jogo = "cores"
                        
                        # Muda a variável 'em_menu' para False, saindo do loop do
                                # menu e iniciando o jogo no modo cores.
                        em_menu = False
                    
                    # Verifica se a tecla "5" foi pressionada.
                    elif evento.key == pygame.K_5:
                        
                        # Define o modo de jogo como "sequencia".
                        modo_jogo = "sequencia"
                        
                        # Muda a variável 'em_menu' para False, indicando que o
                                # menu deve ser fechado.
                        em_menu = False
                        
                        # Reinicia o contador de sequência para o início (1), configurando o
                                # ambiente para o modo sequência.
                        proximo_numero_sequencia = 1



        # Reinicia a pontuação do jogador a cada novo jogo.
        pontuacao = 0
        
        # Define a velocidade inicial dos tiles que caem para 5. Esse valor 
                # pode ser ajustado conforme o jogador avança no jogo.
        VELOCIDADE_TILE = 5
        
        # Limpa a lista de tiles, removendo todos os tiles existentes 
                # para começar um novo jogo.
        tiles.clear()
        
        # Atualiza o tempo da última criação de tile para o momento atual, 
                # garantindo que a criação de novos tiles seja
                # sincronizada com o início do jogo.
        ultima_criacao_tile = pygame.time.get_ticks()
        
        # Inicia o loop principal do jogo, que continua até que a
                # variável 'rodando' seja False.
        rodando = True
        while rodando:
            
            # Cria um objeto Clock para controlar a taxa de atualizações do
                    # jogo, assegurando um jogo suave.
            relogio = pygame.time.Clock()
            
            # Limita a taxa de atualizações (frames por segundo) a 30 para 
                    # manter o jogo jogável e consistente em diferentes máquinas.
            relogio.tick(30)
            
            # Processa todos os eventos que ocorrem (como cliques e
                    # pressionamentos de teclas).
            for evento in pygame.event.get():
                
                # Verifica se o evento é do tipo QUIT, que ocorre quando o 
                        # usuário fecha a janela do jogo.
                if evento.type == pygame.QUIT:
                    
                    # Chama a função para salvar a pontuação atual antes de sair, 
                            # garantindo que o progresso não seja perdido.
                    salvar_pontuacao()
                    
                    # Encerra a biblioteca Pygame, liberando recursos do sistema.
                    pygame.quit()
                    
                    # Sai do programa, encerrando completamente o jogo.
                    sys.exit()

                # Verifica se o evento capturado é um clique do
                        # mouse (botão pressionado).
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    
                    # Obtém a posição atual do cursor do mouse na tela.
                    pos_mouse = pygame.mouse.get_pos()
                    
                    # Itera sobre a lista de tiles, considerando uma cópia da 
                            # lista para evitar modificações durante a iteração.
                    for tile, cor, conteudo, resultado in tiles[:]:
                        
                        # Verifica se o ponto onde o mouse foi clicado colide
                                # com algum dos tiles.
                        if tile.collidepoint(pos_mouse):
                            
                            # Verifica se o modo de jogo atual é "sequencia".
                            if modo_jogo == "sequencia":
                                
                                # No modo sequência, verifica se o número no tile clicado 
                                        # não é o número sequencial esperado.
                                if resultado != proximo_numero_sequencia:
                                    
                                    # Se o número não for o esperado, termina o loop de
                                            # jogo, finalizando a sessão atual.
                                    rodando = False
                                    
                                # Se o número for o correto na sequência,
                                else:
                                    
                                    # Remove o tile clicado da lista de tiles, pois 
                                            # foi corretamente selecionado.
                                    tiles.remove((tile, cor, conteudo, resultado))
                                    
                                    # Incrementa a pontuação do jogador em 1 ponto.
                                    pontuacao += 1
                                    
                                    # Aumenta a velocidade de queda dos tiles para aumentar a 
                                            # dificuldade do jogo progressivamente.
                                    VELOCIDADE_TILE += 0.3
                                    
                                    # Incrementa o próximo número esperado na sequência para o próximo tile.
                                    proximo_numero_sequencia += 1
                            
                            # Verifica se o modo de jogo atual é "pares", onde o jogador 
                                    # deve clicar apenas em tiles com números pares.
                            elif modo_jogo == "pares":

                                # Verifica se o número no tile clicado não é par.
                                if resultado % 2 != 0:
                                    
                                    # Se o número não é par, o jogo termina.                                    
                                    rodando = False
                                    
                                else:
                                    
                                    # Se o número é par, o tile é removido da lista, indicando
                                            # que foi corretamente selecionado.
                                    tiles.remove((tile, cor, conteudo, resultado))
                                    
                                    # Aumenta a pontuação do jogador em 1 ponto.
                                    pontuacao += 1
                                    
                                    # Incrementa levemente a velocidade dos tiles, 
                                            # aumentando a dificuldade do jogo.
                                    VELOCIDADE_TILE += 0.2
                            
                            # Verifica se o modo de jogo é "cores", onde o jogador deve 
                                    # clicar em tiles cuja cor do texto corresponda à cor de fundo.
                            elif modo_jogo == "cores":
                                
                                # Verifica se o nome da cor do conteúdo corresponde à
                                        # cor de fundo do tile.
                                if (conteudo == "Verde" and cor == VERDE) or (conteudo == "Vermelho" and cor == VERMELHO):
                                
                                    # Remove o tile correto da lista.
                                    tiles.remove((tile, cor, conteudo, resultado))
                                    
                                    # Aumenta a pontuação do jogador.
                                    pontuacao += 1
                                    
                                    # Aumenta a velocidade dos tiles sutilmente.
                                    VELOCIDADE_TILE += 0.1
                                    
                                else:
                                    
                                    # Se a cor não corresponde, o jogo termina.
                                    rodando = False
                            
                            # Verifica se o modo de jogo é "verde", onde o jogador deve 
                                    # clicar apenas em tiles verdes.
                            elif modo_jogo == "verde":
                                
                                # Verifica se a cor do tile clicado é verde.
                                if cor == VERDE:
                                
                                    # Remove o tile verde correto.
                                    tiles.remove((tile, cor, conteudo, resultado))
                                    
                                    # Aumenta a pontuação.
                                    pontuacao += 1
                                    
                                    # Aumenta significativamente a velocidade dos tiles, 
                                            # tornando o jogo mais desafiador.
                                    VELOCIDADE_TILE += 1
                                    
                                else:
                                    
                                    # Se o tile não é verde, o jogo termina.
                                    rodando = False
                            
                            # Verifica se o modo de jogo é "normal", onde todos os tiles 
                                    # são pretos e devem ser clicados.
                            elif modo_jogo == "normal" and cor == PRETO:
                                
                                # Remove o tile preto que foi clicado.
                                tiles.remove((tile, cor, conteudo, resultado))
                                
                                # Aumenta a pontuação.
                                pontuacao += 1
                                
                                # Aumenta moderadamente a velocidade dos tiles.
                                VELOCIDADE_TILE += 0.3


            # Itera sobre todos os tiles atualmente na lista de tiles.
            for tile, cor, conteudo, resultado in tiles:
                
                # Aumenta a posição vertical (y) do tile, fazendo-o "descer" na tela.
                        # A taxa de descida é determinada pela variável VELOCIDADE_TILE.
                tile.y += VELOCIDADE_TILE
            
            # Itera sobre uma cópia da lista de tiles para remover os tiles conforme 
                    # necessário sem alterar a lista durante a iteração.
            for tile, cor, conteudo, resultado in tiles[:]:
                
                # Verifica se o tile alcançou ou ultrapassou o limite inferior da tela,
                        # indicando que ele chegou ao final da tela.
                if tile.y >= ALTURA_TELA:
                
                    # Aplica lógicas específicas de cada modo de jogo para determinar se o 
                            # jogo deve terminar baseado no tile que chegou ao final.
                    # No modo "sequencia", verifica se o tile que chegou ao final é o
                            # próximo esperado na sequência.
                    if modo_jogo == "sequencia" and resultado == proximo_numero_sequencia:

                        # Termina o jogo se o tile esperado na sequência não foi acertado.
                        rodando = False  
                        
                    # No modo "pares", verifica se o tile que chegou ao final é um número par.
                    elif modo_jogo == "pares" and resultado % 2 == 0:

                        # Termina o jogo se um número par não foi acertado.
                        rodando = False  
                        
                    # No modo "cores", verifica se o tile que chegou ao final tem o texto 
                            # correspondente à sua cor de fundo.
                    elif modo_jogo == "cores" and ((conteudo == "Verde" and cor == VERDE) or (conteudo == "Vermelho" and cor == VERMELHO)):

                        # Termina o jogo se um tile de cor correta não foi acertado.
                        rodando = False  
                        
                    # No modo "verde", verifica se o tile que chegou ao final é verde.
                    elif modo_jogo == "verde" and cor == VERDE:

                        # Termina o jogo se um tile verde não foi acertado.
                        rodando = False  
                        
                    # No modo "normal", todos os tiles são pretos e devem ser acertados.
                    elif modo_jogo == "normal" and cor == PRETO:

                        # Termina o jogo se um tile preto não foi acertado.
                        rodando = False  
                        
                    # Remove o tile da lista, pois ele já passou pelo ponto de
                            # verificação (fim da tela).
                    tiles.remove((tile, cor, conteudo, resultado))

            
            # Obtem o tempo atual em milissegundos desde que o Pygame foi inicializado.
            agora = pygame.time.get_ticks()
            
            # Verifica se o tempo decorrido desde a última criação de um tile é 
                    # maior que o intervalo de tempo definido para criação de novos tiles.
            if agora - ultima_criacao_tile > tempo_tile:
            
                # Chama a função para criar um novo tile.
                criar_tile()
                
                # Atualiza a variável 'ultima_criacao_tile' com o tempo atual, 
                        # resetando o temporizador para a próxima criação de tile.
                ultima_criacao_tile = agora
            
            # Chama a função para desenhar os elementos do jogo na tela, 
                    # incluindo tiles e pontuação.
            desenhar_jogo()
            
        # Este bloco é executado quando o loop do jogo (variável 'rodando') é 
                # finalizado, indicando que o jogo terminou.
        # Adiciona a pontuação obtida na sessão atual à pontuação acumulada,
                # garantindo que o progresso do jogador seja salvo.
        pontuacao_acumulada += pontuacao
        
        # Chama a função para salvar a pontuação acumulada em um arquivo,
                # preservando os dados para futuras sessões.
        salvar_pontuacao()


# Chama a função para executar o jogo
main()