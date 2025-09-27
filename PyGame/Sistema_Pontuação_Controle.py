"""
Lógica de Jogo

https://www.clipartmax.com/so/player/

    - Tempo e Pontuação - Implementação de um sistema de pontuação e controle de tempo.
        
Exemplo simples onde você controla um quadrado que deve coletar 
itens para ganhar pontos. O jogo terá uma contagem regressiva, e quando 
o tempo acabar, o jogo exibirá a pontuação final. 


Neste jogo:

    - A tela é inicializada com tamanho de 800x600 pixels.
    - Um jogador é desenhado na tela e pode se mover com as setas do teclado.
    - Itens azuis (pontos) são espalhados aleatoriamente pela tela.
    - O jogador ganha 10 pontos cada vez que coleta um item.
    - Um temporizador conta 30 segundos até o final do jogo.
    - A pontuação e o tempo restante são mostrados no canto superior
        esquerdo e direito da tela, respectivamente.
    - Quando o tempo acaba, o jogo imprime a pontuação no console e 
        aguarda por 2 segundos antes de fechar.

Isso fornece uma base sólida para um jogo simples com pontuação e controle 
de tempo que você pode expandir e modificar conforme necessário.

"""

# Importação de bibliotecas necessárias para o jogo:
import pygame  # pygame é uma biblioteca de jogos que fornece funcionalidades para criar jogos em 2D.
import sys  # sys é uma biblioteca que fornece acesso a algumas variáveis e funções que interagem com o interpretador Python.
import random  # random é uma biblioteca que gera números aleatórios, útil para adicionar imprevisibilidade ao jogo.

# Inicialização do Pygame:
pygame.init()  # Inicializa todos os módulos incluídos no pacote Pygame, necessário para usar as funcionalidades da biblioteca.

# Definição de cores básicas que serão usadas para desenhar na tela do jogo:
# As cores são definidas como tuplas de três elementos, representando os valores de Vermelho, Verde e Azul (RGB),
# onde cada valor pode ir de 0 (nenhum) a 255 (máximo).
PRETO = (0, 0, 0)  # Define a cor preta (ausência de cor em RGB).
VERMELHO = (255, 0, 0)  # Define a cor vermelha (máximo de vermelho, sem verde e azul).
VERDE = (0, 255, 0)  # Define a cor verde (sem vermelho, máximo de verde, sem azul).
AZUL = (0, 0, 255)  # Define a cor azul (sem vermelho, sem verde, máximo de azul).
BRANCO = (255, 255, 255)  # Define a cor branca (máximo de todas as cores, resultando em branco).

# Configurações da tela do jogo:
LARGURA = 800  # Define a largura da tela do jogo em pixels.
ALTURA = 600  # Define a altura da tela do jogo em pixels.

# Cria uma janela para o jogo com as dimensões especificadas, retornando uma superfície que representa a tela visível.
# A função set_mode() aceita uma tupla ou lista com a largura e a altura da tela.
tela = pygame.display.set_mode((LARGURA, ALTURA))  # Esta superfície é onde todos os elementos gráficos do jogo serão desenhados.


# Definindo o título da janela do jogo:
pygame.display.set_caption('Tempo e Pontuação') 


# Definição das variáveis relacionadas ao jogador:
# A variável x_jogador armazena a posição horizontal do jogador.
# Usamos a divisão inteira (//) para posicionar o jogador no meio da largura da tela.
x_jogador = LARGURA // 2  

# A variável y_jogador armazena a posição vertical do jogador.
# Da mesma forma, usamos a divisão inteira para posicionar o jogador no meio da altura da tela.
y_jogador = ALTURA // 2  

# Define a largura do jogador. Neste caso, o jogador terá 50 pixels de largura.
largura_jogador = 50  

# Define a altura do jogador. Neste caso, o jogador terá 50 pixels de altura.
altura_jogador = 50  

# Define a velocidade do jogador. Este valor é usado para determinar quantos pixels
# o jogador se move a cada atualização de quadro quando uma tecla é pressionada.
velocidade_jogador = 5  


# Inicialização da lista dos itens que serão coletados no jogo:
# Cria uma lista vazia chamada 'itens'. 
# Esta lista será posteriormente preenchida com os retângulos representando os itens a serem coletados no jogo.
itens = []  


# Loop que irá rodar 10 vezes para criar 10 itens no jogo.
for _ in range(10):
    
    # 'pygame.Rect' cria um retângulo que será usado para representar um item.
    # 'random.randint(0, LARGURA - 20)' gera uma posição aleatória para o eixo x dentro da tela,
    # subtraindo 20 para garantir que o item não seja criado fora da tela.
    # 'random.randint(0, ALTURA - 20)' faz o mesmo para a posição y.
    # '20, 20' define a largura e altura do item, que são 20 pixels cada.
    itens.append(pygame.Rect(random.randint(0, LARGURA - 20), random.randint(0, ALTURA - 20), 20, 20))

# Inicializa a pontuação do jogador como 0.
pontuacao = 0

# 'tempo_inicio' armazena o tempo total do jogo em segundos, que é definido como 30 segundos.
tempo_inicio = 30

# 'tempo_final' calcula o momento (em milissegundos) em que o jogo deve terminar.
# 'pygame.time.get_ticks()' retorna o número de milissegundos desde que 'pygame.init()' foi chamado.
# Multiplicando 'tempo_inicio' por 1000 converte os segundos em milissegundos.
# Somando isso ao tempo atual, temos o momento exato no futuro quando o tempo do jogo acaba.
tempo_final = pygame.time.get_ticks() + tempo_inicio * 1000

# 'fonte' é uma variável que armazena a fonte que será usada para renderizar texto.
# 'pygame.font.SysFont(None, 55)' cria uma fonte do sistema com tamanho 55.
# Se o primeiro argumento é 'None', o Pygame usará a fonte padrão.
fonte = pygame.font.SysFont(None, 55)


# Define a função 'desenhar', que será responsável por atualizar a 
# tela do jogo com todos os elementos gráficos.
def desenhar():
    
    # Preenche toda a tela com a cor preta. 'tela.fill(PRETO)' é usado 
    # para limpar a tela e definir uma cor de fundo.
    tela.fill(PRETO)

    # Desenha o retângulo que representa o jogador na tela.
    # 'pygame.draw.rect' é a função que desenha um retângulo.
    # 'tela' é a superfície onde o retângulo será desenhado.
    # 'VERDE' é a cor do retângulo do jogador.
    # A tupla '(x_jogador, y_jogador, largura_jogador, altura_jogador)' define a
    # posição e tamanho do retângulo do jogador.
    pygame.draw.rect(tela, VERDE, (x_jogador, y_jogador, largura_jogador, altura_jogador))

    # Inicia um loop para desenhar cada item na lista de itens.
    for item in itens:
        
        # 'pygame.draw.ellipse' é a função que desenha uma elipse ou um
        # círculo se a altura e largura forem iguais.
        # 'tela' é onde a elipse será desenhada.
        # 'AZUL' define a cor da elipse.
        # 'item' é a posição e tamanho da elipse, que é definida por um objeto 'pygame.Rect'.
        pygame.draw.ellipse(tela, AZUL, item)

    # Renderiza o texto da pontuação usando a fonte definida anteriormente.
    # 'fonte.render' cria uma imagem do texto.
    # 'f'Pontuação: {pontuacao}'' é uma string formatada que exibe a 
    # palavra 'Pontuação' seguida pelo valor atual da pontuação do jogador.
    # 'True' habilita o anti-aliasing do texto, que é um recurso para suavizar as
    # bordas das letras.
    # 'BRANCO' é a cor do texto.
    texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, BRANCO)

    # 'tela.blit' desenha a imagem do texto na tela.
    # '(10, 10)' é a posição onde o texto será colocado na tela, neste caso, no
    # canto superior esquerdo com uma pequena margem.
    tela.blit(texto_pontuacao, (10, 10))

    # Calcula o tempo restante do jogo subtraindo o tempo atual do 
    # 'tempo_final' e convertendo de milissegundos para segundos.
    tempo_atual = (tempo_final - pygame.time.get_ticks()) // 1000

    # Renderiza o texto do tempo restante e o desenha na tela.
    # 'f'Tempo: {tempo_atual}'' exibe a palavra 'Tempo' seguida pelo tempo restante calculado.
    texto_tempo = fonte.render(f'Tempo: {tempo_atual}', True, BRANCO)

    # Desenha o texto do tempo no canto superior direito da tela, subtraindo
    # 200 pixels da largura total para dar margem.
    tela.blit(texto_tempo, (LARGURA - 200, 10))

    # 'pygame.display.flip()' atualiza a tela inteira com tudo que foi 
    # desenhado. É o que efetivamente faz os desenhos aparecerem.
    pygame.display.flip()
    
    
# A variável 'executando' é definida como True, o que indica que 
# o loop principal do jogo está ativo.
executando = True

# Este é o loop principal do jogo, que continuará executando enquanto 'executando' for True.
while executando:
    
    # A função 'pygame.time.get_ticks()' retorna o número de
    # milissegundos desde que 'pygame.init()' foi chamado.
    # Compara se o tempo atual é maior que o 'tempo_final', que é quando o jogo deve terminar.
    if pygame.time.get_ticks() > tempo_final:
        
        # Se o tempo acabou, imprime a pontuação final do jogador no console.
        print(f'Seu jogo acabou! Sua pontuação foi: {pontuacao}')
        
        # 'pygame.time.delay(2000)' faz o programa esperar 2000 milissegundos
        # (ou seja, 2 segundos) antes de continuar.
        pygame.time.delay(2000)
        
        # Define 'executando' como False, o que causará a saída do 
        # loop principal e terminará o jogo.
        executando = False

    # Aqui inicia um loop que verifica todos os eventos que estão na fila de eventos do Pygame.
    for evento in pygame.event.get():
        
        # 'pygame.event.get()' retorna uma lista de todos os eventos que
        # aconteceram desde a última vez que a função foi chamada.
        # Verifica cada evento na fila para ver se o tipo do evento é 
        # 'pygame.QUIT', que é um evento gerado quando o usuário fecha a janela do jogo.
        if evento.type == pygame.QUIT:
            
            # Se o evento for do tipo QUIT, 'pygame.quit()' é chamado 
            # para terminar todos os módulos do Pygame.
            pygame.quit()
            
            # 'sys.exit()' é utilizado para sair do script Python.
            sys.exit()

    # Movimento do jogador
    
    # Captura o estado atual de todas as teclas.
    teclas = pygame.key.get_pressed()

    # Verifica se a tecla esquerda (K_LEFT) está pressionada.
    if teclas[pygame.K_LEFT]:
        
        # Se a tecla esquerda está pressionada, subtrai da coordenada x 
        # do jogador a quantidade definida pela 'velocidade_jogador'.
        # Isso move o jogador para a esquerda na tela.
        x_jogador -= velocidade_jogador

    # Verifica se a tecla direita (K_RIGHT) está pressionada.
    if teclas[pygame.K_RIGHT]:
        
        # Se a tecla direita está pressionada, adiciona à coordenada x
        # do jogador a quantidade definida pela 'velocidade_jogador'.
        # Isso move o jogador para a direita na tela.
        x_jogador += velocidade_jogador

    # Verifica se a tecla para cima (K_UP) está pressionada.
    if teclas[pygame.K_UP]:
        
        # Se a tecla para cima está pressionada, subtrai da coordenada y 
        # do jogador a quantidade definida pela 'velocidade_jogador'.
        # Isso move o jogador para cima na tela.
        # Em gráficos de computador, o topo da tela é geralmente a coordenada y 0, 
        # então subtrair da coordenada y move para cima.
        y_jogador -= velocidade_jogador

    # Verifica se a tecla para baixo (K_DOWN) está pressionada.
    if teclas[pygame.K_DOWN]:
        
        # Se a tecla para baixo está pressionada, adiciona à coordenada y do
        # jogador a quantidade definida pela 'velocidade_jogador'.
        # Isso move o jogador para baixo na tela.
        y_jogador += velocidade_jogador
        
        
    # Este bloco é responsável por verificar se ocorre alguma 
    # colisão entre o jogador e os itens coletáveis.
    jogador_rect = pygame.Rect(x_jogador, y_jogador, largura_jogador, altura_jogador)
    
    # Cria um retângulo para o jogador usando as coordenadas atuais e o tamanho do jogador.
    # Este retângulo será usado para detectar colisões.

    # Itera sobre uma cópia da lista de itens.
    # A cópia é criada usando a notação de fatia '[:]' para 
    # evitar modificar a lista enquanto a iteramos.
    for item in itens[:]:

        # Verifica se o retângulo do jogador colide com o retângulo do item atual.
        # A função 'colliderect' retorna True se houver uma colisão.
        if jogador_rect.colliderect(item):            

            # Se ocorrer uma colisão, remove o item da lista, representando que o
            # jogador coletou o item.
            itens.remove(item)
            
            # Incrementa a pontuação em 10 pontos para cada item coletado.
            pontuacao += 10

    # Após verificar colisões e atualizar a lista de itens e pontuação,
    # o próximo passo é desenhar a cena atualizada.

    # Chama a função 'desenhar' para desenhar todos os elementos na tela.
    # Isso incluirá o jogador, quaisquer itens restantes, e as atualizações
    # do placar e do temporizador.
    desenhar()

    # Este bloco é para controlar a taxa de atualização do jogo, também 
    # conhecida como quadros por segundo (fps).
    # Cria um objeto Clock e chama o método 'tick' com o valor 30.
    # Isso significa que o jogo vai tentar não rodar a mais de 30 quadros por segundo.
    # Controlar o fps é importante para garantir que o jogo funcione da mesma forma
    # em diferentes hardwares e que a mecânica do jogo não fique muito rápida ou lenta.
    pygame.time.Clock().tick(30)


# Pygame é encerrado com esta chamada.
pygame.quit()
        
        