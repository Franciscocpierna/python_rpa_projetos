"""
Entrada do Usuário

    - Eventos: Teclado, mouse.
    
As teclas W, A, S, D são usadas para mover o retângulo na tela.
    
"""

# Primeiro, importamos o módulo pygame, que é uma biblioteca
# usada para criar jogos e outras aplicações multimídia em Python.
import pygame

# Em seguida, importamos o módulo random, que nos permite 
# gerar números aleatórios.
import random

# Aqui, iniciamos o pygame, que é necessário para configurar 
# internamente os módulos que vamos usar.
pygame.init()

# Definimos as variáveis 'largura_tela' e 'altura_tela', que vão
# determinar o tamanho da janela do jogo em pixels.
# Estabelecemos a largura como 800 pixels e a altura como 600 pixels.
largura_tela, altura_tela = 800, 600

# Criamos a tela do jogo chamando 'pygame.display.set_mode' e passando 
# uma tupla com a largura e altura definidas anteriormente.
# Esta tela será a superfície de desenho onde elementos gráficos do jogo serão exibidos.
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Definimos duas cores em formato RGB (Red, Green, Blue), onde cada cor 
# pode ter um valor de 0 a 255.
# 'PRETO' é definido como a ausência de cor, portanto, todos os valores são 0.
PRETO = (0, 0, 0)

# 'BRANCO' é definido como a presença total de todas as cores, então todos os valores são 255.
BRANCO = (255, 255, 255)


# Definimos as variáveis referentes ao retângulo que será controlado pelo
# jogador ou pela lógica do jogo.

# As variáveis 'x' e 'y' representam a posição do retângulo
# na tela. A operação de divisão inteira '//' garante que os valores
# sejam inteiros. Iniciamos o retângulo no centro da tela dividindo a
# largura e a altura da tela por 2.
x, y = largura_tela // 2, altura_tela // 2

# As variáveis 'largura_retangulo' e 'altura_retangulo' definem as dimensões do retângulo.
# Neste caso, ambos são definidos como 50 pixels.
largura_retangulo, altura_retangulo = 50, 50

# A variável 'velocidade' determina quão rápido o retângulo se
# moverá na tela. O valor é em pixels por ciclo do loop do jogo.
# Aumentar este número fará com que o retângulo se mova mais rápido.
velocidade = 5

# A variável 'cor_retangulo' armazena a cor atual do 
# retângulo. Iniciamos com a cor BRANCO definida anteriormente.
# Esta cor pode ser alterada durante a execução do jogo, por 
# exemplo, em resposta a eventos do usuário.
cor_retangulo = BRANCO

# Loop principal do jogo
# A variável 'executando' é uma flag (sinalizador) que controla a execução do loop principal do jogo. 
# Quando 'executando' é True, o jogo continua rodando. Se for definida como False, o loop termina e o jogo é fechado.
executando = True

# Aqui começa o loop principal do jogo. Dentro deste loop, todos
# os eventos são processados e o estado do jogo é atualizado.
while executando:
    
    # O 'pygame.event.get()' captura uma lista de todos os eventos que
    # ocorreram desde a última vez que foi chamado.
    # Isso inclui eventos de teclado, mouse e outros dispositivos de entrada.
    for evento in pygame.event.get():
        
        # A condição 'if evento.type == pygame.QUIT:' verifica se o evento
        # capturado é um evento do tipo QUIT,
        # o que ocorre, por exemplo, quando o usuário clica no botão 
        # de fechar a janela do jogo.
        if evento.type == pygame.QUIT:
            
            # Se um evento QUIT é capturado, definimos 'executando' como
            # False, o que terminará o loop do jogo.
            executando = False

        # 'if evento.type == pygame.KEYDOWN:' verifica se o evento é 
        # um pressionamento de tecla.
        if evento.type == pygame.KEYDOWN:
            
            # Dentro deste bloco, verificamos qual tecla foi pressionada.
            # 'if evento.key == pygame.K_ESCAPE:' verifica se a 
            # tecla ESC (Escape) foi pressionada.
            if evento.key == pygame.K_ESCAPE:
                
                # Se a tecla ESC for pressionada, 'executando' é definido
                # como False, o que terminará o loop do jogo,
                # permitindo ao usuário sair do jogo pressionando ESC.
                executando = False

        # Verifica se um evento do tipo 'MOUSEBUTTONDOWN' ocorreu - isto é, 
        # se um dos botões do mouse foi pressionado.
        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            # 'if evento.button == 1:' verifica se o botão pressionado foi o 
            # botão esquerdo do mouse.
            # O botão esquerdo é geralmente o botão principal e tem o valor 1.
            if evento.button == 1:
                
                # Se o botão esquerdo do mouse for pressionado, a cor do retângulo é alterada.
                # 'random.randint(0, 255)' gera um número inteiro aleatório entre 0 e 255, que são os valores possíveis
                # para um componente de cor em um sistema de cores RGB.
                # Assim, uma nova cor aleatória é gerada para o retângulo cada
                # vez que o botão esquerdo do mouse é pressionado.
                cor_retangulo = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
              
            
    # Captura de teclas pressionadas:
    # Esta linha chama a função 'get_pressed()', que retorna um 
    # dicionário com todos os estados das teclas: 
    # se uma tecla está sendo pressionada, o valor correspondente 
    # será True, se não, será False.
    teclas_pressionadas = pygame.key.get_pressed()

    # A seguir, temos uma série de condicionais que verificam se 
    # uma determinada tecla está pressionada.
    # Se a tecla 'W' (para cima) está pressionada, decrementamos o
    # valor de 'y' pela 'velocidade', 
    # fazendo o retângulo se mover para cima na tela.
    if teclas_pressionadas[pygame.K_w]:
        y -= velocidade            
        
        
    # Se a tecla 'S' (para baixo) está pressionada, incrementamos o
    # valor de 'y' pela 'velocidade',
    # fazendo o retângulo se mover para baixo na tela.
    if teclas_pressionadas[pygame.K_s]:
        y += velocidade

    # Se a tecla 'A' (esquerda) está pressionada, decrementamos o 
    # valor de 'x' pela 'velocidade',
    # fazendo o retângulo se mover para a esquerda na tela.
    if teclas_pressionadas[pygame.K_a]:
        x -= velocidade

    # Se a tecla 'D' (direita) está pressionada, incrementamos o valor de 'x' pela 'velocidade',
    # fazendo o retângulo se mover para a direita na tela.
    if teclas_pressionadas[pygame.K_d]:
        x += velocidade

    # Impedindo o retângulo de sair da tela:
    # Aqui aplicamos duas funções, 'max' e 'min', para garantir 
    # que o retângulo não saia dos limites da tela.
    # A função 'max' garante que o 'x' e o 'y' não sejam menores que 0, o 
    # que impediria o retângulo de ir além da borda superior e da esquerda da tela.
    # A função 'min' garante que o retângulo não vá além da largura da tela menos 
    # a largura do retângulo para 'x',
    # e não vá além da altura da tela menos a altura do retângulo
    # para 'y', impedindo que saia das bordas direita e inferior.
    x = max(0, min(x, largura_tela - largura_retangulo))
    y = max(0, min(y, altura_tela - altura_retangulo))


    # Atualizando a tela:
    # Esta linha preenche a tela inteira com a cor preta. 
    # O método 'fill()' é utilizado para preencher toda a 
    # superfície com uma cor uniforme, neste caso, PRETO, 
    # que é uma tupla RGB definida anteriormente no código.
    tela.fill(PRETO)  # Limpa a tela com a cor preta

    # Desenho do retângulo:
    # A função 'draw.rect()' é usada para desenhar um retângulo na superfície especificada. 
    # Neste caso, desenha-se na superfície 'tela', com a cor 
    # atual 'cor_retangulo' (que pode mudar com cliques do mouse),
    # e na posição e tamanho especificados pela tupla (x, y, largura_retangulo, altura_retangulo).
    pygame.draw.rect(tela, cor_retangulo, (x, y, largura_retangulo, altura_retangulo))  # Desenha o retângulo na tela

    # Atualização do frame da tela:
    # 'pygame.display.flip()' é um comando que atualiza todo o conteúdo da janela. 
    # Se você desenhou ou mudou algo na superfície que é exibida na tela
    # desde a última vez que a tela foi atualizada,
    # esta função fará com que essas mudanças sejam visíveis.
    pygame.display.flip()  # Atualiza o frame da tela para mostrar as novas mudanças

    # Controle do framerate do jogo:
    # Esta linha cria um novo objeto Clock e chama o método 'tick()', 
    # que faz com que o jogo aguarde o suficiente para rodar a uma velocidade de 60 quadros por segundo (fps).
    # Se o jogo estiver rodando mais rápido do que isso, o 'tick()' vai atrasar o loop por um tempo, 
    # de forma que não passe de 60 fps. Isso é útil para garantir que o jogo rode de
    # maneira suave e consistente em diferentes hardwares.
    pygame.time.Clock().tick(60)  # Limita o jogo a rodar a no máximo 60 quadros por segundo


# Finalizando o Pygame
pygame.quit()

                
    