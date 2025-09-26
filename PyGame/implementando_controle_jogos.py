"""
Entrada do Usuário

    Controles: Implementação de controles para jogos.
    
Vamos criar um exemplo de implementação de controles para um jogo simples 
usando Pygame. No jogo, o jogador controlará um quadrado que pode se
mover em todas as quatro direções com as teclas do teclado e atirará 
em direção ao cursor do mouse quando o botão esquerdo for pressionado.

Neste exemplo, incluiremos:

    - Controle do quadrado com as teclas W, A, S, D.
    - O quadrado atira em direção ao cursor do mouse ao clicar com o botão esquerdo do mouse.
    - Os projéteis se movem em direção à posição onde o cursor estava no momento do clique.
"""

# Importa o módulo pygame, que é uma biblioteca 
# usada para desenvolver jogos.
import pygame

# Importa o módulo math, que fornece acesso a funções matemáticas.
import math

# Chama a função init do módulo pygame, que é necessária para inicializar
# os módulos internos do pygame.
pygame.init()

# Define as variáveis `largura_tela` e `altura_tela` que determinam
# o tamanho da janela do jogo.
largura_tela, altura_tela = 800, 600

# Cria a janela do jogo usando as dimensões fornecidas e armazena na variável `tela`.
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Define três tuplas que representam as cores em RGB (Red, Green, Blue).
# PRETO é definido como cor com todos os componentes RGB definidos para 0.
PRETO = (0, 0, 0)

# VERMELHO é definido como cor com o componente
# vermelho máximo e verde e azul como 0.
VERMELHO = (255, 0, 0)

# BRANCO é definido como cor com todos os componentes
# RGB definidos para o valor máximo, 255.
BRANCO = (255, 255, 255)

# Define as variáveis `x_jogador` e `y_jogador` para armazenar
# a posição inicial do jogador na tela.
# O jogador é colocado no centro da tela usando a divisão
# inteira da largura e altura da tela por 2.
x_jogador, y_jogador = largura_tela // 2, altura_tela // 2

# Define as variáveis `largura_jogador` e `altura_jogador`
# para determinar o tamanho do retângulo do jogador.
largura_jogador, altura_jogador = 50, 50

# Define a variável `velocidade_jogador` que determina 
# a rapidez com que o jogador pode se mover.
velocidade_jogador = 5


# A lista `projeteis` é inicializada vazia. Ela armazenará a
# posição e a velocidade de cada projétil disparado pelo jogador.
projeteis = []

# `velocidade_projétil` é uma variável que define a velocidade 
# constante de todos os projéteis atirados no jogo.
velocidade_projétil = 10


# Aqui é definida a função `atirar`, que é responsável por criar um projétil.
# Ela recebe quatro argumentos: `x` e `y` são as coordenadas do jogador (ou da origem do tiro),
# e `mx` e `my` são as coordenadas do mouse no momento do clique, ou seja, o
# alvo para onde o projétil será direcionado.
def atirar(x, y, mx, my):
    
    # Calcula o ângulo do tiro baseado na posição do alvo (mx, my) e a
    # posição atual do jogador (x, y).
    # A função `atan2` retorna o ângulo entre o eixo x e o vetor que
    # vai do jogador ao ponto de mira,
    # o resultado está em radianos.
    angulo = math.atan2(my-y, mx-x)
    
    # Calcula a velocidade horizontal do projétil (`vx`) com base no cosseno do ângulo.
    # Multiplica-se o cosseno do ângulo pela `velocidade_projétil` para manter a magnitude constante da velocidade,
    # independente da direção. Isso assegura que o projétil se mova a uma velocidade constante em qualquer direção.
    vx = math.cos(angulo) * velocidade_projétil
    
    # Calcula a velocidade vertical do projétil (`vy`) com base no seno do ângulo.
    # Multiplica-se o seno do ângulo pela `velocidade_projétil` pelo mesmo motivo explicado acima.
    vy = math.sin(angulo) * velocidade_projétil
    
    # Adiciona o projétil recém-criado à lista `projeteis`. Cada projétil é representado por uma lista
    # contendo sua posição atual (x, y) e sua velocidade (vx, vy).
    projeteis.append([x, y, vx, vy])


# A variável `executando` é usada como uma flag de controle para o loop principal do jogo.
# Enquanto `executando` for True, o loop continua executando. Esta variável pode ser alterada
# para False se o jogador decidir sair do jogo, o que encerrará o loop.
executando = True

# Este é o loop principal do jogo. Ele vai rodar repetidamente enquanto
# a variável `executando` for True.
while executando:
    
    # Este loop for percorre a fila de eventos do Pygame. O Pygame lida com todos os eventos
    # que vêm do sistema operacional, como teclas pressionadas, movimentos e cliques do mouse, etc.
    for evento in pygame.event.get():
        
        # Aqui é verificado se o evento atual é do tipo QUIT, que é um evento do Pygame
        # que ocorre quando o usuário fecha a janela do jogo. Se for o caso,
        # a flag `executando` é setada como False, saindo assim do loop principal
        # e fechando o jogo.
        if evento.type == pygame.QUIT:
            executando = False
        
        # Aqui é verificado se o evento atual é um clique de mouse com o botão para baixo.
        # O Pygame suporta diferentes botões do mouse, mas neste caso estamos apenas interessados
        # no botão esquerdo, que é representado pelo número 1.
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            # Verifica se o botão pressionado é o botão esquerdo do mouse.
            if evento.button == 1:
                
                # `pygame.mouse.get_pos()` obtém a posição atual do cursor do mouse como uma
                # tupla (x, y), que é armazenada nas variáveis `mx` e `my`.
                mx, my = pygame.mouse.get_pos()
                
                # Chama a função `atirar`, passando a posição central do jogador como ponto de origem
                # do projétil. A posição central é calculada adicionando metade da largura e metade da altura
                # às coordenadas x e y do jogador, permitindo que o projétil pareça sair do centro do jogador.
                atirar(x_jogador + largura_jogador / 2, y_jogador + altura_jogador / 2, mx, my)
                
                
    # Movimento do jogador

    # `pygame.key.get_pressed()` obtém o estado de todas as teclas do teclado.
    # O retorno é uma lista onde cada posição representa uma tecla e o valor é True se
    # a respectiva tecla está sendo pressionada no momento e False caso contrário.
    teclas = pygame.key.get_pressed()

    # Aqui verificamos se a tecla 'W' está pressionada, o que representa o movimento para cima.
    # Se a tecla 'W' estiver pressionada, subtraímos da posição 'y' do jogador a 'velocidade_jogador',
    # fazendo com que ele se mova para cima na tela.
    if teclas[pygame.K_w]:
        y_jogador -= velocidade_jogador
        
        
    # Aqui verificamos se a tecla 'S' está pressionada, o que representa o movimento para baixo.
    # Se a tecla 'S' estiver pressionada, adicionamos à posição 'y' do jogador a 'velocidade_jogador',
    # fazendo com que ele se mova para baixo na tela.
    if teclas[pygame.K_s]:
        y_jogador += velocidade_jogador

    # Aqui verificamos se a tecla 'A' está pressionada, o que representa o movimento para a esquerda.
    # Se a tecla 'A' estiver pressionada, subtraímos da posição 'x' do jogador a 'velocidade_jogador',
    # fazendo com que ele se mova para a esquerda na tela.
    if teclas[pygame.K_a]:
        x_jogador -= velocidade_jogador

    # Aqui verificamos se a tecla 'D' está pressionada, o que representa o movimento para a direita.
    # Se a tecla 'D' estiver pressionada, adicionamos à posição 'x' do jogador a 'velocidade_jogador',
    # fazendo com que ele se mova para a direita na tela.
    if teclas[pygame.K_d]:
        x_jogador += velocidade_jogador

    # Atualizar a posição dos projéteis
    
    # Este loop 'for' passa por cada projétil na lista de 'projeteis'.
    # Cada 'projétil' é uma lista contendo a posição 'x' (índice 0) e 'y' (índice 1) do projétil,
    # bem como as componentes de velocidade 'vx' (índice 2) e 'vy' (índice 3).
    for projétil in projeteis:
        
        # Atualizamos a posição 'x' do projétil ('projétil[0]') adicionando a sua velocidade horizontal ('projétil[2]').
        # Isso fará com que o projétil se mova na direção horizontal com base em sua velocidade.
        projétil[0] += projétil[2]

        # Atualizamos a posição 'y' do projétil ('projétil[1]') adicionando a sua velocidade vertical ('projétil[3]').
        # Isso fará com que o projétil se mova na direção vertical com base em sua velocidade.
        projétil[1] += projétil[3]


    # Remover projéteis que saíram da tela
    
    # Inicializa uma nova lista para os projéteis que permanecerão após o filtro.
    projeteis_filtrados = []

    # O loop for irá iterar sobre cada projétil existente na lista de projéteis.
    for projétil in projeteis:
        
        # Verifica se a posição x do projétil (projétil[0]) está dentro dos limites horizontais da tela.
        # Ou seja, maior que 0 e menor que a largura da tela (largura_tela).
        dentro_limites_horizontais = 0 < projétil[0] < largura_tela

        # Verifica se a posição y do projétil (projétil[1]) está dentro dos limites verticais da tela.
        # Ou seja, maior que 0 e menor que a altura da tela (altura_tela).
        dentro_limites_verticais = 0 < projétil[1] < altura_tela

        # Se o projétil está dentro dos limites tanto horizontais quanto verticais,
        # então ele é adicionado à nova lista de projéteis filtrados.
        if dentro_limites_horizontais and dentro_limites_verticais:
            projeteis_filtrados.append(projétil)

    # Após o loop, substituímos a lista antiga de projéteis pela nova lista filtrada.
    projeteis = projeteis_filtrados
    
    # Desenho
    # Preenche a tela com a cor preta.
    # O método fill() é usado para preencher toda a superfície com uma cor uniforme.
    # Neste caso, a cor preta (definida pela tupla PRETO) é usada para limpar o que estava
    # previamente desenhado na tela, efetivamente "reiniciando" a tela para o próximo frame.
    tela.fill(PRETO)

    # Desenha um retângulo representando o jogador.
    # pygame.draw.rect() é o método utilizado para desenhar um retângulo na superfície.
    # Os parâmetros são, respectivamente, a superfície onde desenhar, a cor do retângulo,
    # e um tuple contendo a posição x e y do retângulo e sua largura e altura.
    # A cor vermelha é definida pela tupla VERMELHO, e as variáveis x_jogador e y_jogador
    # determinam a posição do retângulo, enquanto largura_jogador e altura_jogador definem
    # suas dimensões.
    pygame.draw.rect(tela, VERMELHO, (x_jogador, y_jogador, largura_jogador, altura_jogador))

    # O loop for itera sobre cada projétil na lista de projéteis.
    # Para cada projétil, um círculo é desenhado representando o projétil na tela.
    for projétil in projeteis:
        
        # O método pygame.draw.circle() desenha um círculo na superfície.
        # Os parâmetros são a superfície onde desenhar, a cor do círculo,
        # a posição central do círculo (convertida para inteiros para evitar erros,
        # já que a posição do projétil pode ser um float), e o raio do círculo.
        # A cor branca é usada para o círculo, definida pela tupla BRANCO, e o raio
        # é definido como 5 pixels.
        pygame.draw.circle(tela, BRANCO, (int(projétil[0]), int(projétil[1])), 5)


    # Atualização da tela
    pygame.display.flip()

    # Controla o framerate do jogo
    pygame.time.Clock().tick(60)

# Finalizando o Pygame
pygame.quit()