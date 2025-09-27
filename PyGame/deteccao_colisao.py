"""
Lógica de Jogo

    - Detecção de Colisão: Conceitos e implementação.
    
    
Neste exemplo, criaremos uma tela de jogo com um retângulo azul 
representando um obstáculo e um retângulo verde que representa o 
jogador. O jogador pode se mover com as teclas direcionais. 

Se o jogador colide com o obstáculo, uma mensagem de "Colisão detectada!" é 
impressa no console e o jogo termina.

A detecção de colisão é realizada pela função colliderect() da classe 
Rect do Pygame, que retorna True se dois retângulos se sobrepuserem.

Este exemplo é simplificado para focar apenas na detecção de colisão, 
mas pode ser expandido para lidar com a resposta à colisão de várias 
maneiras, como parar o movimento do jogador, diminuir a vida do jogador, etc.
"""

# A linha abaixo importa o módulo pygame, que é uma
# biblioteca de código aberto usada para desenvolver jogos. 
# Ela fornece módulos que permitem criar jogos e conteúdos multimídia em Python.
import pygame

# Este import traz o módulo sys, que fornece acesso a 
# algumas variáveis e funções que têm forte interação com o interpretador Python.
# Será usado mais adiante para encerrar o programa.
import sys

# A função init() é chamada para inicializar todos os módulos importados no pygame. 
# É uma etapa necessária para fazer qualquer coisa no pygame e deve ser
# chamada após a importação do pygame e antes de qualquer outra operação relacionada ao pygame.
pygame.init()

# A variável PRETO é definida como uma tupla contendo três inteiros, que representam as cores no formato RGB (Red, Green, Blue). 
# Aqui, (0, 0, 0) significa que todas as cores estão no valor mínimo, produzindo a cor preta.
PRETO = (0, 0, 0)

# Similarmente, a variável VERMELHO é definida como uma tupla RGB. 
# O valor (255, 0, 0) significa que o vermelho está no valor máximo 
# e as outras cores (verde e azul) estão no mínimo, resultando em puro vermelho.
VERMELHO = (255, 0, 0)

# A variável VERDE é definida. Aqui, (0, 255, 0) significa que apenas
# o verde está no valor máximo enquanto as outras estão no mínimo, produzindo a cor verde.
VERDE = (0, 255, 0)

# Por fim, a variável AZUL é atribuída com (0, 0, 255), que é o valor
# onde apenas o azul está no valor máximo e as outras cores no mínimo, resultando em puro azul.
AZUL = (0, 0, 255)


# Estas duas linhas definem as variáveis LARGURA e ALTURA
# com os valores 800 e 600, respectivamente.
# Estes valores são usados para definir a dimensão da janela do jogo em pixels.
LARGURA = 800
ALTURA = 600

# A função 'set_mode' do módulo display do pygame é chamada com uma
# tupla contendo as variáveis LARGURA e ALTURA.
# Isso inicia e abre uma janela (ou tela) com a largura de 800 pixels
# e altura de 600 pixels para o jogo.
# A variável 'tela' armazena a superfície de desenho retornada, que 
# será usada para fazer operações de desenho posteriores.
tela = pygame.display.set_mode((LARGURA, ALTURA))

# 'set_caption' é uma função do módulo display que define o título da janela do jogo.
# Aqui, o título 'Detecção de Colisão' é definido para a janela do jogo.
pygame.display.set_caption('Detecção de Colisão')

# As seguintes linhas definem as variáveis para o jogador.
# 'x_jogador' e 'y_jogador' são inicializadas para começar no
# centro da tela, utilizando a divisão inteira (//) de LARGURA e ALTURA por 2.
# Isso coloca a posição inicial do jogador no meio da tela horizontalmente e verticalmente.
x_jogador = LARGURA // 2
y_jogador = ALTURA // 2

# 'largura_jogador' e 'altura_jogador' são as dimensões do
# retângulo que representa o jogador na tela.
# Aqui, são atribuídos os valores 50 pixels para a largura
# e altura, definindo o tamanho do jogador.
largura_jogador = 50
altura_jogador = 50

# 'velocidade_jogador' é a variável que define a velocidade
# com a qual o jogador pode se mover na tela.
# Neste caso, é definido o valor 5, que pode representar a 
# quantidade de pixels que o jogador se move a cada atualização 
# de frame quando uma tecla é pressionada.
velocidade_jogador = 5


# Aqui, estão sendo definidas as variáveis relacionadas 
# ao objeto estático, que neste contexto podemos chamar de obstáculo.
# 'x_obstaculo' é a posição horizontal do obstáculo na tela, que é 
# definida como um quarto da largura da tela.
x_obstaculo = LARGURA // 4

# 'y_obstaculo' é a posição vertical do obstáculo na tela, definida
# como um terço da altura da tela.
y_obstaculo = ALTURA // 3

# 'largura_obstaculo' define a largura do obstáculo, neste caso, definido em 200 pixels.
largura_obstaculo = 200

# 'altura_obstaculo' define a altura do obstáculo, que é definida como 100 pixels.
altura_obstaculo = 100


# A função 'desenhar' é definida abaixo. Esta função será chamada
# para atualizar o visual da tela a cada frame do jogo.
def desenhar():
    
    # 'tela.fill(PRETO)' é um comando que preenche toda a superfície da tela com a cor preta.
    # Este passo é importante para limpar qualquer desenho anterior antes de
    # começar a desenhar o estado atual da tela.
    tela.fill(PRETO)

    # 'pygame.draw.rect' é uma função que desenha um retângulo na superfície dada (neste caso, a 'tela').
    # A cor do retângulo será VERDE, e a posição e tamanho são dados pela 
    # tupla (x_jogador, y_jogador, largura_jogador, altura_jogador).
    # Isso desenha o jogador na tela.
    pygame.draw.rect(tela, VERDE, (x_jogador, y_jogador, largura_jogador, altura_jogador))

    # Um segundo retângulo é desenhado, desta vez na cor AZUL, na
    # posição e com o tamanho definido pelas variáveis do obstáculo.
    # Este retângulo representa o obstáculo estático na tela.
    pygame.draw.rect(tela, AZUL, (x_obstaculo, y_obstaculo, largura_obstaculo, altura_obstaculo))

    # 'pygame.display.update()' é uma função que atualiza a tela inteira se chamada sem argumentos.
    # Isso fará com que tudo que foi desenhado anteriormente com os comandos 'pygame.draw.rect' apareça na tela.
    pygame.display.update()
    
    

# Loop principal
# A variável 'executando' é inicializada com o valor True. Esta variável 
# controla o loop principal do jogo.
# Enquanto 'executando' for True, o jogo continuará a rodar.
executando = True

# Este é o loop principal do jogo. A cada iteração, ele verifica 
# eventos, atualiza o estado do jogo e redesenha a tela.
while executando:
    
    # O método 'pygame.event.get()' captura todos os eventos que 
    # aconteceram desde a última vez que foi chamado.
    # Isso inclui teclas pressionadas, movimentos do mouse, etc.
    for evento in pygame.event.get():
        
        # Aqui é verificado se algum dos eventos capturados é do 
        # tipo QUIT, que ocorre, por exemplo, quando
        # o usuário clica no botão de fechar a janela do jogo.
        if evento.type == pygame.QUIT:
            
            # 'pygame.quit()' é chamado para finalizar todos os módulos
            # do pygame de forma limpa.
            pygame.quit()
            
            # 'sys.exit()' é utilizado para encerrar o programa completamente.
            sys.exit()
            
    # A função 'pygame.key.get_pressed()' obtém o estado de todas as teclas do teclado.
    # Ela retorna uma sequência de booleanos representando o estado de cada tecla.
    teclas = pygame.key.get_pressed()

    # Abaixo, as teclas de seta do teclado são verificadas para atualizar a posição do jogador.
    # Se a tecla da seta para esquerda (K_LEFT) está pressionada, então a posição x do jogador é decrementada,
    # movendo o jogador para a esquerda na tela.
    if teclas[pygame.K_LEFT]:
        x_jogador -= velocidade_jogador

    # Se a tecla da seta para direita (K_RIGHT) está pressionada, a posição x do jogador é incrementada,
    # movendo o jogador para a direita.
    if teclas[pygame.K_RIGHT]:
        x_jogador += velocidade_jogador

    # Se a tecla da seta para cima (K_UP) está pressionada, a posição y do jogador é decrementada,
    # movendo o jogador para cima na tela.
    if teclas[pygame.K_UP]:
        y_jogador -= velocidade_jogador

    # Se a tecla da seta para baixo (K_DOWN) está pressionada, a posição y do jogador é incrementada,
    # movendo o jogador para baixo na tela.
    if teclas[pygame.K_DOWN]:
        y_jogador += velocidade_jogador
        
    
    # Verifica colisão
    
    # Cria um retângulo que representa a posição e dimensão do jogador utilizando a classe Rect do pygame.
    # Os parâmetros passados são as coordenadas do canto superior esquerdo e as dimensões do retângulo.
    jogador_rect = pygame.Rect(x_jogador, y_jogador, largura_jogador, altura_jogador)

    # Cria um retângulo que representa a posição e dimensão do obstáculo de maneira similar ao retângulo do jogador.
    obstaculo_rect = pygame.Rect(x_obstaculo, y_obstaculo, largura_obstaculo, altura_obstaculo)

    # Verifica se os retângulos do jogador e do obstáculo estão se sobrepondo, o que indicaria uma colisão.
    if jogador_rect.colliderect(obstaculo_rect):
        
        # Se uma colisão for detectada, imprime uma mensagem no console para informar o usuário.
        print("Colisão detectada!")
        
        # A variável 'executando' é configurada como False para sair do loop principal e terminar o jogo.
        executando = False

    # Desenha os elementos na tela
    # Chama a função 'desenhar', que atualiza a visualização do jogo na tela.
    # Esta função é responsável por desenhar o jogador, o obstáculo e qualquer outro elemento gráfico do jogo.
    desenhar()

    # Limita o número de quadros por segundo (fps)
    # Cria um objeto Clock que pode ser usado para rastrear o tempo.
    # O método 'tick' é chamado com o valor 30, o que limita o jogo a no máximo 30 quadros por segundo.
    pygame.time.Clock().tick(30)
        
        
        
# Espera um pouco antes de encerrar após a colisão
# Depois que o jogo detecta uma colisão e a variável 'executando' é definida como False,
# o programa aguarda 2000 milissegundos (ou 2 segundos) antes de prosseguir para dar ao jogador
# um momento para perceber a colisão.
pygame.time.delay(2000)

# Finaliza o pygame
# Depois do atraso, a função 'pygame.quit()' é chamada para encerrar todos os módulos do pygame
# de forma adequada, permitindo que o programa seja encerrado sem deixar processos pendentes.
pygame.quit()