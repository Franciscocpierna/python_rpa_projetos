# Importa o módulo pygame, que fornece funcionalidades para criar jogos.
import pygame

# Importa o módulo sys, usado para acessar funções e
        # variáveis do sistema operacional.
import sys

# Importa o módulo random, utilizado para gerar 
        # números aleatórios.
import random

# Importa o módulo os, usado para interagir com o 
        # sistema operacional.
import os

# Chama a função init() do pygame para inicializar todos os
        # módulos necessários para o pygame.
pygame.init()

# Define a largura da tela do jogo como 400 pixels.
LARGURA_TELA = 400

# Define a altura da tela do jogo como 600 pixels.
ALTURA_TELA = 600

# Cria uma janela ou tela para exibir o jogo, usando
        # as dimensões especificadas.
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Define o título da janela do jogo como 'Flappy Bird'.
pygame.display.set_caption('Flappy Bird')

# Carrega a imagem de fundo do jogo do arquivo 'fundo.png' e a 
        # converte para o formato de pixel interno usado pelo Pygame
        # para otimizar o desempenho.
fundo = pygame.image.load('fundo.png').convert()

# Carrega a imagem do pássaro do jogo do arquivo 'passaro.png' e 
        # utiliza convert_alpha para manter informações de transparência.
passaro_imagem = pygame.image.load('passaro.png').convert_alpha()

# Carrega a imagem do cano do jogo do arquivo 'cano.png' e também utiliza 
        # convert_alpha para manter transparência.
cano_imagem = pygame.image.load('cano.png').convert_alpha()

# Redimensiona a imagem de fundo para cobrir exatamente a tela do jogo.
fundo = pygame.transform.scale(fundo, (LARGURA_TELA, ALTURA_TELA))

# Redimensiona a imagem do pássaro para as dimensões especificadas (34x24 pixels).
passaro_imagem = pygame.transform.scale(passaro_imagem, (34, 24))

# Redimensiona a imagem do cano para as dimensões especificadas (52x320 pixels).
cano_imagem = pygame.transform.scale(cano_imagem, (52, 320))

# Define a gravidade inicial do jogo como 0.2, que afeta o
        # movimento de queda do pássaro.
GRAVIDADE_INICIAL = 0.2

# Define a gravidade atual do jogo igual à gravidade inicial.
gravidade = GRAVIDADE_INICIAL

# Inicializa a variável que controla o movimento 
        # vertical do pássaro como 0.
movimento_passaro = 0

# Define a variável de controle do estado do jogo como False, 
        # indicando que o jogo começa na tela do menu, e não em execução.
jogo_ativo = False

# Inicializa a pontuação do jogador como 0.
pontuacao = 0

# Define a velocidade inicial dos canos como 2, que influencia a
        # rapidez com que os canos se movem na tela.
VELOCIDADE_INICIAL_CANOS = 2

# Define a velocidade atual dos canos igual à velocidade inicial.
velocidade_canos = VELOCIDADE_INICIAL_CANOS

# Define um limiar de pontuação (5 pontos) após o
        # qual a dificuldade do jogo aumenta.
limitacao_pontuacao = 5

# Verifica se o arquivo 'pontuacao_maxima.txt' existe no diretório atual.
if os.path.exists('pontuacao_maxima.txt'):
    
    # Abre o arquivo de pontuação máxima para leitura.
    with open('pontuacao_maxima.txt', 'r') as arquivo:
        
        # Lê a pontuação máxima do arquivo e converte para float.
        pontuacao_maxima = float(arquivo.read())
        
else:
    
    # Se o arquivo não existir, define a pontuação 
            # máxima como 0.
    pontuacao_maxima = 0

# Cria uma fonte para o jogo usando a fonte padrão do 
        # sistema com tamanho 40.
fonte_jogo = pygame.font.Font(None, 40)

# Cria um retângulo de detecção de colisão para o pássaro, 
        # centralizando-o na posição inicial (100, metade da altura da tela).
passaro_rect = passaro_imagem.get_rect(center=(100, ALTURA_TELA / 2))

# Inicializa uma lista vazia para armazenar os 
        # canos gerados no jogo.
lista_de_canos = []

# Define um evento personalizado no Pygame para a 
        # geração de novos canos.
GERAR_CANO = pygame.USEREVENT

# Configura um temporizador para disparar o evento de geração de
        # canos a cada 1500 milissegundos (1,5 segundos).
pygame.time.set_timer(GERAR_CANO, 1500)

# Define o tamanho do espaço entre os canos superiores e
        # inferiores como 150 pixels.
TAMANHO_GAP = 150


def criar_canos():
    
    # Escolhe um ponto aleatório para a abertura entre dois canos. 
    # O intervalo garante que a abertura não esteja
    # demasiado perto do topo ou do fundo da tela, evitando que o 
            # jogo se torne impossivelmente difícil.
    posicao_gap = random.randint(100, ALTURA_TELA - 100 - TAMANHO_GAP)

    # Define a altura do cano que aparece no topo da tela. 
            # O cano terminará onde o gap começa.
    altura_cano_cima = posicao_gap

    # Define a altura do cano que aparece no fundo da tela. 
    # O cano começa onde o gap termina e se estende até a 
            # parte inferior da tela.
    altura_cano_baixo = ALTURA_TELA - posicao_gap - TAMANHO_GAP

    # Adapta a imagem do cano para a altura do cano superior.
    # Isso assegura que o cano pareça natural e mantenha sua largura original.
    cano_cima_imagem = pygame.transform.scale(cano_imagem, (cano_imagem.get_width(), altura_cano_cima))
    
    # Inverte a imagem do cano superior para que ele esteja
            # orientado corretamente, com a abertura voltada para baixo.
    cano_cima_imagem = pygame.transform.flip(cano_cima_imagem, False, True)
    
    # Cria um retângulo de colisão para o cano superior. Isso é 
            # usado para detectar colisões com o pássaro.
    cano_cima_rect = cano_cima_imagem.get_rect(midbottom=(LARGURA_TELA + 50, posicao_gap))

    # Adapta a imagem do cano para a altura do cano inferior, 
            # mantendo a largura e ajustando a altura conforme necessário.
    cano_baixo_imagem = pygame.transform.scale(cano_imagem, (cano_imagem.get_width(), altura_cano_baixo))
    
    # Cria um retângulo de colisão para o cano inferior. A posição do
            # retângulo é definida para começar onde o gap termina.
    cano_baixo_rect = cano_baixo_imagem.get_rect(midtop=(LARGURA_TELA + 50, posicao_gap + TAMANHO_GAP))

    # Retorna uma lista contendo pares de imagens e seus respectivos 
            # retângulos para os canos superior e inferior.
    # Esses pares serão usados para desenhar os canos na tela e para 
            # verificar colisões com o pássaro.
    return [(cano_cima_imagem, cano_cima_rect), (cano_baixo_imagem, cano_baixo_rect)]


# Define a função 'mover_canos' que é responsável por 
            # atualizar a posição dos canos no jogo.
def mover_canos(canos):
    
    # Cria uma lista vazia para armazenar os novos canos que
            # ainda estão visíveis na tela.
    novos_canos = []
    
    # Itera sobre cada cano na lista de canos passada para a função.
    for cano in canos:
    
        # Extrai a imagem do cano e o retângulo associado (que 
                # define a posição e dimensões do cano).
        imagem_cano, cano_rect = cano
        
        # Move o cano para a esquerda diminuindo sua posição central
                # no eixo X pela velocidade dos canos.
        cano_rect.centerx -= velocidade_canos
        
        # Verifica se o cano ainda está parcialmente visível na tela,
                # verificando se o lado direito do cano
                # ainda não passou completamente pelo lado esquerdo
                # da tela (a 50 pixels além da borda esquerda).
        if cano_rect.right > -50:
        
            # Se o cano ainda está parcialmente visível, adiciona-o
                    # à lista de novos canos.
            novos_canos.append((imagem_cano, cano_rect))
            
    # Retorna a lista de canos que ainda devem ser mostrados na tela.
    return novos_canos


# Define uma função para desenhar os canos na tela do jogo.
def desenhar_canos(canos):
    
    # Itera sobre cada cano na lista de canos.
    for cano in canos:
    
        # Extrai a imagem do cano e o retângulo 
                # associado (definindo a posição do cano).
        imagem_cano, cano_rect = cano
        
        # Desenha a imagem do cano na tela na posição 
                # especificada pelo retângulo do cano.
        tela.blit(imagem_cano, cano_rect)


# Define uma função para verificar se ocorre alguma
        # colisão entre o pássaro e os canos.
def verificar_colisoes(canos):

    # Declara que a função modificará a variável global 'jogo_ativo'.
    global jogo_ativo
    
    # Itera sobre cada cano na lista para verificar colisões.
    for cano in canos:
    
        # Extrai a imagem do cano e o retângulo associado.
        imagem_cano, cano_rect = cano
        
        # Verifica se o retângulo do pássaro intersecta o
                # retângulo do cano.
        if passaro_rect.colliderect(cano_rect):
        
            # Se houver colisão, o jogo é finalizado 
                    # (jogo_ativo se torna False).
            jogo_ativo = False
            
    # Verifica também se o pássaro voou muito alto ou caiu demais.
    if passaro_rect.top <= -50 or passaro_rect.bottom >= ALTURA_TELA:
        
        # Finaliza o jogo se o pássaro sair dos limites
                # verticais da tela.
        jogo_ativo = False


# Define uma função para rotacionar a imagem do pássaro 
        # baseada em seu movimento vertical.
def rotacionar_passaro(passaro):
    
    # Rotaciona o pássaro. O ângulo de rotação é baseado no movimento
            # vertical do pássaro, multiplicado por -3 para ajustar a sensibilidade.
    novo_passaro = pygame.transform.rotozoom(passaro, -movimento_passaro * 3, 1)
    
    # Retorna a nova imagem do pássaro rotacionada.
    return novo_passaro


# Define uma função para exibir a pontuação, aceitando um 
        # parâmetro que indica o estado atual do
        # jogo ('jogo' ou 'menu').
def exibir_pontuacao(estado_jogo):
    
    # Verifica se o estado atual é 'jogo', o que significa 
            # que o jogo está ativo.
    if estado_jogo == 'jogo':
    
        # Renderiza o texto da pontuação usando a fonte 
                # definida anteriormente.
        # 'True' ativa o anti-aliasing do texto, fazendo-o mais
                # suave, e a cor do texto é branca (255, 255, 255).
        texto_pontuacao = fonte_jogo.render(f'Pontuação: {int(pontuacao)}', True, (255, 255, 255))
        
        # Obtém um retângulo que envolve o texto da pontuação, 
                # posicionando-o no centro da tela na parte superior.
        rect_pontuacao = texto_pontuacao.get_rect(center=(LARGURA_TELA / 2, 50))
        
        # Desenha o texto da pontuação na tela na posição 
                # especificada pelo retângulo.
        tela.blit(texto_pontuacao, rect_pontuacao)

    # Verifica se o estado atual é 'menu', o que significa que o 
            # jogo está no menu inicial ou final.
    if estado_jogo == 'menu':
        
        # Renderiza o texto da pontuação máxima alcançada no jogo,
                # também em branco com anti-aliasing.
        texto_pontuacao_maxima = fonte_jogo.render(f'Recorde: {int(pontuacao_maxima)}', True, (255, 255, 255))
        
        # Obtém um retângulo que envolve o texto da pontuação 
                # máxima, centralizando-o na tela um pouco abaixo 
                # do centro vertical.
        rect_pontuacao_maxima = texto_pontuacao_maxima.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 - 50))
        
        # Desenha o texto da pontuação máxima na tela na posição
                # especificada pelo retângulo.
        tela.blit(texto_pontuacao_maxima, rect_pontuacao_maxima)


# Define a função que atualiza a pontuação máxima com base
        # na pontuação atual do jogo.
def atualizar_pontuacao(pontuacao, pontuacao_maxima):
    
    # Compara a pontuação atual com a pontuação máxima 
            # anteriormente registrada.
    if pontuacao > pontuacao_maxima:
    
        # Se a pontuação atual for maior, atualiza a pontuação 
                # máxima para o valor da pontuação atual.
        pontuacao_maxima = pontuacao
        
        # Abre (ou cria, se não existir) um arquivo de texto 
                # chamado 'pontuacao_maxima.txt' no modo de escrita.
        with open('pontuacao_maxima.txt', 'w') as arquivo:
        
            # Converte a pontuação máxima de um número para 
                    # uma string e escreve no arquivo.
            arquivo.write(str(pontuacao_maxima))
    
    # Retorna o valor atualizado da pontuação máxima, 
            # seja ela alterada ou não.
    return pontuacao_maxima


def desenhar_botao_comecar():
    
    # Usa a fonte definida para criar uma superfície 
            # com o texto 'Começar'.
    # O segundo parâmetro 'True' ativa o anti-aliasing, que 
            # suaviza as bordas do texto para uma apresentação visual melhor.
    # O terceiro parâmetro especifica a cor do texto em RGB, 
            # onde (255, 255, 255) representa a cor branca.
    texto_botao = fonte_jogo.render('Começar', True, (255, 255, 255))
    
    # Cria um objeto retângulo (pygame.Rect) que é usado 
            # para posicionar o texto na tela.
    # A função get_rect() calcula o tamanho necessário para o
            # texto e permite definir sua posição com o parâmetro 'center'.
    # Aqui, o texto é centralizado horizontalmente e posicionado 
            # um pouco abaixo da metade vertical da tela.
    rect_botao = texto_botao.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 + 50))
    
    # Desenha um retângulo preto ao redor do local onde o 
            # texto será exibido.
    # A função draw.rect() requer a superfície onde desenhar, a
            # cor em formato RGB e o retângulo.
    # O método inflate() é usado para aumentar as dimensões do 
            # retângulo do texto, adicionando 20 pixels na
            # largura e 10 pixels na altura,
    # criando assim uma margem ao redor do texto para que o 
            # botão pareça mais claro e fácil de pressionar.
    pygame.draw.rect(tela, (0, 0, 0), rect_botao.inflate(20, 10))
    
    # Coloca o texto na tela na posição definida pelo retângulo.
    # O método blit() da superfície 'tela' é usado para desenhar a
            # superfície do texto 'texto_botao' na posição
            # especificada por 'rect_botao'.
    tela.blit(texto_botao, rect_botao)
    
    # Retorna o retângulo que contém o texto. Isso é útil 
            # para posterior detecção de cliques,
            # pois permite verificar se o clique do mouse ocorreu
            # dentro das dimensões do retângulo.
    return rect_botao


def aumentar_dificuldade():
    
    # Declara que a função modificará as variáveis globais 
            # 'velocidade_canos', 'gravidade' e 'limitacao_pontuacao'.
    global velocidade_canos, gravidade, limitacao_pontuacao
    
    # Verifica se a pontuação atual do jogador atingiu ou 
            # excedeu o limiar definido para aumentar a dificuldade.
    if pontuacao >= limitacao_pontuacao:
        
        # Aumenta a velocidade dos canos que se movem na tela,
                # fazendo com que os canos se desloquem mais rapidamente.
        # Isso exige reações mais rápidas do jogador para 
                # evitar colisões.
        velocidade_canos += 0.1  
        
        # Aumenta a gravidade que afeta o pássaro, fazendo com que 
                # ele caia mais rapidamente quando o jogador
                # não está pressionando o botão para voar. 
        # Isso adiciona um desafio ao controle do pássaro.
        gravidade += 0.01
        
        # Ajusta o limiar de pontuação para o próximo nível de 
                # dificuldade, aumentando-o em 5 pontos.
        # Isso significa que a dificuldade será novamente aumentada 
                # quando o jogador atingir este novo limiar.
        limitacao_pontuacao += 5


# Loop principal do jogo
relogio = pygame.time.Clock()

# Inicia um loop infinito que continuará executando 
        # até que o jogo seja fechado.
while True:
    
    # Itera sobre cada evento na fila de eventos do Pygame.
    for evento in pygame.event.get():
    
        # Verifica se o tipo do evento é QUIT, o que ocorre quando o
                # usuário clica no botão de fechar a janela do jogo.
        if evento.type == pygame.QUIT:
        
            # Encerra o Pygame, finalizando todos os módulos inicializados.
            pygame.quit()
            
            # Encerra o script do Python, garantindo que o 
                    # jogo feche corretamente.
            sys.exit()

        # Verifica se foi pressionada alguma tecla.
        if evento.type == pygame.KEYDOWN:
            
            # Checa se a tecla pressionada foi a barra de espaço e 
                    # se o jogo está atualmente ativo.
            if evento.key == pygame.K_SPACE and jogo_ativo:
            
                # Reseta o movimento vertical do pássaro para 0 para
                        # iniciar um novo movimento de subida.
                movimento_passaro = 0
                
                # Diminui o valor de movimento do pássaro, fazendo com 
                        # que ele 'salte' para cima na tela.
                # O valor 6 é subtraído para criar um impulso 
                        # significativo para cima.
                movimento_passaro -= 6


        # Verifica se houve um clique do mouse e se o jogo
                # não está ativo no momento.
        if evento.type == pygame.MOUSEBUTTONDOWN and not jogo_ativo:
        
            # Obtém a posição atual do mouse como uma tupla (x, y).
            posicao_mouse = pygame.mouse.get_pos()
            
            # Verifica se o clique do mouse foi dentro do retângulo 
                    # do botão "Começar".
            if rect_botao.collidepoint(posicao_mouse):
                
                # Se o clique foi no botão "Começar", reinicia variáveis e 
                        # estados do jogo para começar uma nova partida.
                
                # Define o jogo como ativo, permitindo que o loop do jogo 
                        # comece a processar os movimentos e lógicas do jogo.
                jogo_ativo = True
            
                # Limpa a lista de canos existentes para começar o
                        # jogo com uma tela limpa.
                lista_de_canos.clear()
                
                # Posiciona o pássaro no centro da tela na horizontal e 
                        # na metade da tela na vertical.
                passaro_rect.center = (100, ALTURA_TELA / 2)
                
                # Reseta o movimento vertical do pássaro para 0 para 
                        # que ele não tenha impulso inicial.
                movimento_passaro = 0
                
                # Zera a pontuação do jogador para o novo jogo.
                pontuacao = 0
                
                # Restaura a velocidade inicial dos canos para o 
                        # valor padrão definido.
                velocidade_canos = VELOCIDADE_INICIAL_CANOS
                
                # Restaura a gravidade para o valor inicial para que o 
                        # pássaro tenha o comportamento padrão ao saltar.
                gravidade = GRAVIDADE_INICIAL
                
                # Restabelece o limiar de dificuldade inicial, para aumentar a
                        # dificuldade à medida que o jogador alcança pontos específicos.
                limitacao_pontuacao = 5
        
        # Verifica se o evento de gerar cano foi disparado e 
                # se o jogo está ativo.
        if evento.type == GERAR_CANO and jogo_ativo:
            
            # Adiciona novos canos à lista de canos. A função 'criar_canos' é
                    # chamada para gerar um novo conjunto de canos,
                    # que são então adicionados à lista de canos que 
                    # serão gerenciados e movimentados na tela.
            lista_de_canos.extend(criar_canos())


    # Desenha a imagem de fundo na tela, começando no canto 
            # superior esquerdo (0, 0).
    tela.blit(fundo, (0, 0))
    
    # Verifica se o jogo está ativo. Se sim, processa a lógica de jogo.
    if jogo_ativo:
        
        # Aplica a gravidade ao movimento vertical do pássaro, 
                # aumentando-a a cada ciclo do loop,
                # o que faz o pássaro cair progressivamente mais rápido.
        movimento_passaro += gravidade
    
        # Rotaciona a imagem do pássaro com base em seu movimento vertical.
        # Isso dá ao jogador uma resposta visual sobre o comportamento
                # do pássaro (subindo ou descendo).
        passaro_rotacionado = rotacionar_passaro(passaro_imagem)
    
        # Atualiza a posição vertical do pássaro no jogo 
                # usando o movimento calculado.
        passaro_rect.centery += movimento_passaro
    
        # Desenha o pássaro rotacionado na posição atualizada na tela.
        tela.blit(passaro_rotacionado, passaro_rect)
    
        # Atualiza a posição dos canos, movendo-os 
                # para a esquerda na tela.
        lista_de_canos = mover_canos(lista_de_canos)
    
        # Desenha os canos atualizados na tela.
        desenhar_canos(lista_de_canos)
    
        # Verifica se houve alguma colisão do pássaro com os
                # canos ou com os limites da tela.
        verificar_colisoes(lista_de_canos)
    
        # Incrementa a pontuação baseado no tempo de jogo e 
                # exibe a pontuação atualizada.
        pontuacao += 0.01
        exibir_pontuacao('jogo')
    
        # Aumenta a dificuldade do jogo incrementando a velocidade
                # dos canos e a gravidade,
                # e ajusta o limiar para futuros aumentos de dificuldade
                # baseado na pontuação alcançada.
        aumentar_dificuldade()


    else:
   
        # Se o jogo não está ativo, exibe a pontuação no menu, 
                # mostrando a pontuação máxima alcançada.
        exibir_pontuacao('menu')
    
        # Verifica se a pontuação do jogo que acabou de terminar é maior 
                # que zero para mostrar a mensagem de Game Over.
        if pontuacao > 0:
            
            # Renderiza a mensagem 'Game Over' com anti-aliasing 
                    # ativado em branco (255, 255, 255).
            texto_game_over = fonte_jogo.render('Game Over', True, (255, 255, 255))
            
            # Cria um retângulo para posicionar o texto 'Game Over' no 
                    # centro da tela, ajustado para cima.
            rect_game_over = texto_game_over.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 - 100))
            
            # Desenha o texto 'Game Over' na tela usando as coordenadas
                    # definidas no retângulo.
            tela.blit(texto_game_over, rect_game_over)
    
            # Atualiza e salva a pontuação máxima se a pontuação atual 
                    # for maior que a pontuação máxima anterior.
            pontuacao_maxima = atualizar_pontuacao(pontuacao, pontuacao_maxima)
    
        # Chama a função para desenhar o botão 'Começar' na tela, permitindo
                # ao jogador iniciar um novo jogo.
        rect_botao = desenhar_botao_comecar()


    # Atualiza a tela inteira para refletir quaisquer mudanças feitas na
            # superfície de desenho durante o ciclo do loop.
    pygame.display.update()

    # Mantém o jogo rodando a uma taxa de 120 quadros por segundo (fps), o 
            # que garante uma jogabilidade suave e responsiva.
    relogio.tick(120)