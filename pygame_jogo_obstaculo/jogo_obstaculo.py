# Importa o módulo pygame que é utilizado para criar jogos e interfaces gráficas
import pygame

# Importa o módulo random que permite a geração de números aleatórios
import random

# Importa o módulo sys que fornece acesso a algumas variáveis e funções
# que têm forte interação com o interpretador Python
import sys

# Inicializa todos os módulos importados do pygame, o que é
# necessário para começar a trabalhar com a biblioteca
pygame.init()

# Define a largura e altura da tela do jogo
largura_tela, altura_tela = 800, 600

# Cria uma janela ou tela para exibição com as dimensões especificadas acima
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Define o título da janela do jogo
pygame.display.set_caption("Jogo do Pulo")


# Definição de cores usando o modelo RGB onde cada cor é uma tupla contendo três valores (R, G, B),
# que representam respectivamente a intensidade de Vermelho, Verde e Azul. Cada valor pode ir de 0 a 255.
branco = (255, 255, 255)  # Cor branca: todas as componentes de cor no máximo.
preto = (0, 0, 0)         # Cor preta: todas as componentes de cor no mínimo.
vermelho = (255, 0, 0)    # Cor vermelha: apenas a componente vermelha no máximo.
verde = (0, 255, 0)       # Cor verde: apenas a componente verde no máximo.
azul = (0, 0, 255)        # Cor azul: apenas a componente azul no máximo.
cinza = (128, 128, 128)   # Cor cinza: as três componentes têm a mesma intensidade, não no máximo nem no mínimo.

# Define a altura do chão no jogo.
# Esta é uma medida em pixels a partir da parte inferior da tela que 
# indica onde a linha do chão é desenhada.
# O chão é importante para aterrisar o boneco após um pulo 
# e para posicionar obstáculos sobre ele.
altura_chao = 10

# Carrega uma imagem de plano de fundo do sistema de arquivos.
# A função 'pygame.image.load()' é usada para carregar imagens. 
# A imagem deve estar no mesmo diretório que este script Python, a 
# menos que um caminho diferente seja especificado.
# O nome do arquivo indica que é uma imagem '.jpg'.
imagem_plano_de_fundo = pygame.image.load('plano_de_fundo.jpg')

# Redimensiona a imagem carregada para o tamanho da tela do jogo. 
# 'pygame.transform.scale()' é uma função que redimensiona uma superfície (no caso, uma imagem).
# Os parâmetros passados são a superfície a ser redimensionada e as novas dimensões desejadas, 
# que aqui são as mesmas da tela do jogo.
imagem_plano_de_fundo = pygame.transform.scale(imagem_plano_de_fundo, (largura_tela, altura_tela))



# Carrega a imagem que será usada para o boneco no jogo.
# A função 'pygame.image.load()' é utilizada para carregar a imagem do boneco a partir do 
# arquivo 'boneco.png'.
# Este arquivo deve estar localizado no mesmo diretório
# do script Python, a menos que um caminho seja especificado.
imagem_boneco = pygame.image.load('boneco.png')

# A imagem do boneco é redimensionada para um tamanho de 100x100 pixels.
# Isso é feito através da função 'pygame.transform.scale()', que altera o
# tamanho da imagem original para as dimensões desejadas.
imagem_boneco = pygame.transform.scale(imagem_boneco, (100, 100))

# Define as coordenadas iniciais do boneco na tela.
# O boneco é posicionado horizontalmente no centro da tela ('largura_tela // 2'),
# e verticalmente, ele é colocado acima da linha do chão ('altura_tela - imagem_boneco.get_height() - altura_chao').
# O operador '//' é a divisão inteira, que descarta a parte fracionária do resultado.
# 'imagem_boneco.get_height()' obtém a altura da imagem do boneco, que é usada para posicionar o boneco acima do chão.
x_boneco, y_boneco = largura_tela // 2, altura_tela - imagem_boneco.get_height() - altura_chao

# Inicializa o mixer do pygame, que é responsável por carregar e reproduzir sons.
pygame.mixer.init()

# Carrega o som que será reproduzido quando o boneco pular.
# A função 'pygame.mixer.Sound()' é usada para carregar um objeto de 
# som a partir do arquivo 'som_espaco.mp3'.
som_pulo = pygame.mixer.Sound('som_espaco.mp3')

# Carrega o som que será reproduzido quando o jogo terminar, por exemplo, quando o jogador perder.
# Assim como o som de pulo, um objeto de som é carregado a partir de 'som_encerramento.mp3'.
som_perda = pygame.mixer.Sound('som_encerramento.mp3')


# Define a velocidade inicial do pulo como 0. 
# Essa variável será utilizada para controlar o impulso vertical do boneco quando ele pular.
velocidade_pulo = 0

# Define a gravidade que será aplicada ao boneco. 
# A gravidade é usada para trazer o boneco de volta ao chão após um pulo
# e para dar uma sensação de peso ao pulo.
# Um valor de 1 significa que a cada quadro do jogo (frame), a velocidade
# vertical do boneco aumentará em 1 na direção do chão.
gravidade = 1

# Define a velocidade com que o boneco pode se mover horizontalmente.
# Esse valor é usado para incrementar ou decrementar a posição horizontal
# do boneco quando as teclas de movimento são pressionadas.
velocidade_horizontal = 5

# Inicializa uma lista vazia que será usada para armazenar os obstáculos no jogo.
# Cada obstáculo será uma lista contendo as coordenadas x e y, largura, altura e cor.
obstaculos = []

# Define a posição inicial do primeiro obstáculo.
# Isso determina onde na tela o primeiro obstáculo aparecerá.
# Aqui está definido para aparecer na borda direita da tela.
espaco_inicial = largura_tela

# Define a distância mínima horizontal entre obstáculos consecutivos.
# Isso ajuda a garantir que há espaço suficiente para o boneco passar entre os obstáculos sem colidir.
espaco_minimo = 400


# Inicia um loop que irá iterar 4 vezes, criando assim 4 obstáculos.
# A variável 'i' será utilizada para espaçar horizontalmente os obstáculos.
for i in range(4):
    
    # Gera uma largura aleatória para o obstáculo, entre 40 e 70 pixels.
    largura_obstaculo = random.randint(40, 70)
    
    # Gera uma altura aleatória para o obstáculo, entre 20 e 150 pixels.
    altura_obstaculo = random.randint(20, 150)
    
    # Define a posição 'x' do obstáculo. O primeiro obstáculo é colocado na 'espaco_inicial' 
    # e cada obstáculo subsequente é espaçado por 'espaco_minimo' pixels.
    x_obstaculo = espaco_inicial + i * espaco_minimo
    
    # Define a posição 'y' do obstáculo de modo que esteja localizado sobre o chão.
    # Isso é calculado subtraindo a 'altura_obstaculo' e 'altura_chao' da 'altura_tela', 
    # garantindo que a base do obstáculo esteja alinhada com o chão.
    y_obstaculo = altura_tela - altura_obstaculo - altura_chao
    
    # Escolhe uma cor aleatoriamente para o obstáculo dentre as opções vermelho, verde e azul.
    cor = random.choice([vermelho, verde, azul])
    
    # Adiciona o obstáculo criado à lista de 'obstaculos'. Cada obstáculo é representado 
    # por uma lista contendo sua posição 'x' e 'y', largura, altura e cor.
    obstaculos.append([x_obstaculo, y_obstaculo, largura_obstaculo, altura_obstaculo, cor])
    
    
# Pontuação
# Inicia a variável 'pontos' com o valor 0, que será usada para 
# manter a contagem da pontuação do jogador.
pontos = 0

# Cria um objeto de fonte usando a fonte padrão do sistema com 
# tamanho de 35 para exibir textos na tela, como a pontuação.
fonte = pygame.font.SysFont(None, 35)

# Controle do jogo
# Cria um objeto 'Clock' que pode ser usado para controlar o tempo de atualização do jogo, isto é,
# para garantir que o jogo rode a uma taxa de quadros por segundo (FPS) específica.
relogio = pygame.time.Clock()

# Define a variável 'fim_de_jogo' como False. Essa variável será utilizada para controlar
# se o jogo deve continuar rodando ou se chegou ao fim. Quando ela for True, o jogo irá terminar.
fim_de_jogo = False


# Inicia o loop principal do jogo. Este loop continuará executando até
# que a variável 'fim_de_jogo' seja True.
while not fim_de_jogo:
    
    # Desenha a imagem de plano de fundo na tela. O método 'blit' é 
    # utilizado para desenhar uma imagem sobre outra.
    # Neste caso, a imagem de plano de fundo é desenhada na 
    # posição (0, 0), que é o canto superior esquerdo da tela,
    # fazendo com que ela cubra toda a tela.
    tela.blit(imagem_plano_de_fundo, (0, 0))
    
    # Verifica a fila de eventos do Pygame para ver se algum evento
    # ocorreu. Por exemplo, um evento pode ser um clique do mouse
    # ou um pressionamento de tecla. Cada evento é representado por um 
    # objeto com um tipo de evento específico.
    for evento in pygame.event.get():
        
        # Se o tipo de evento for QUIT (como clicar no botão de 
        # fechar a janela do jogo), então define a variável 'fim_de_jogo' como True.
        # Isso fará com que o loop principal do jogo termine, pois a 
        # condição 'while not fim_de_jogo' deixará de ser verdadeira.
        if evento.type == pygame.QUIT:
            fim_de_jogo = True
            
            
    # Processamento da lógica de pulo e movimento horizontal do personagem.
    teclas = pygame.key.get_pressed()  # Detecta quais teclas estão sendo pressionadas no momento.
    
    
    # A condição verifica se o personagem está no chão, o que é feito
    # verificando se a posição vertical (y) do personagem
    # é igual à altura da tela menos a altura do personagem e a altura
    # do chão. Isso garante que o personagem só possa pular se estiver no chão.
    if y_boneco == altura_tela - imagem_boneco.get_height() - altura_chao:

        # Verifica se a tecla de espaço (K_SPACE) está pressionada.
        if teclas[pygame.K_SPACE]:
            
            # Se estiver, a velocidade de pulo é definida para um valor negativo para mover o personagem para cima.
            # Valores negativos de velocidade de pulo fazem o personagem subir (pulo).
            velocidade_pulo = -15
            
            # Toca o som de pulo quando o personagem pula.
            som_pulo.play()

        # Verifica se a tecla de seta para cima (K_UP) está pressionada.
        elif teclas[pygame.K_UP]:
            
            # Se estiver, a velocidade de pulo é definida para um valor mais negativo do que o pulo normal.
            # Isso dá ao personagem um pulo mais alto do que o pulo realizado com a tecla de espaço.
            velocidade_pulo = -22
            
            # Toca o som de pulo quando o personagem realiza um pulo alto.
            som_pulo.play()
        
        
    # Verifica se a tecla de seta para a esquerda (K_LEFT) está pressionada.
    if teclas[pygame.K_LEFT]:
        
        # Se a tecla de seta para a esquerda estiver pressionada, subtrai a
        # velocidade horizontal da posição 'x' do personagem.
        # Isso move o personagem para a esquerda na tela.
        x_boneco -= velocidade_horizontal

    # Verifica se a tecla de seta para a direita (K_RIGHT) está pressionada.
    if teclas[pygame.K_RIGHT]:
        
        # Se a tecla de seta para a direita estiver pressionada, adiciona a
        # velocidade horizontal à posição 'x' do personagem.
        # Isso move o personagem para a direita na tela.
        x_boneco += velocidade_horizontal


    # Atualiza a velocidade de pulo do personagem adicionando o valor da gravidade.
    # Isso simula o efeito da gravidade puxando o personagem para baixo ao longo do tempo.
    velocidade_pulo += gravidade

    # Atualiza a posição vertical (y) do personagem adicionando a velocidade de pulo atual.
    # Se a velocidade de pulo for negativa, o personagem se move para cima na tela; se for positiva, se move para baixo.
    y_boneco += velocidade_pulo

    # Verifica se o personagem está abaixo do ponto mais baixo permitido na tela (o chão),
    # o qual é calculado subtraindo a altura do chão e a altura do personagem da altura total da tela.
    if y_boneco > altura_tela - imagem_boneco.get_height() - altura_chao:
        
        # Se o personagem estiver abaixo do chão, ajusta sua posição para que ele não se mova abaixo do chão.
        y_boneco = altura_tela - imagem_boneco.get_height() - altura_chao

    # Desenha o personagem na tela na posição atualizada (x_boneco, y_boneco).
    # 'blit' é um método que desenha a imagem do personagem na superfície da tela.
    tela.blit(imagem_boneco, (x_boneco, y_boneco))

    # Desenha uma linha representando o chão na tela.
    # A linha é desenhada usando a cor cinza, começando do canto esquerdo até o canto direito da tela,
    # com a altura definida pela variável 'altura_chao'.
    pygame.draw.line(tela, cinza, (0, altura_tela - altura_chao), (largura_tela, altura_tela - altura_chao), altura_chao)
    
    
    # Itera sobre a lista de obstáculos.
    # Cada 'obs' é uma lista que contém as posições x e y do obstáculo, 
    # sua largura e altura, e sua cor.
    for obs in obstaculos:
        
        # Desenha o obstáculo na tela.
        # 'obs[4]' é a cor do obstáculo, e 'obs[:4]' são as coordenadas e
        # tamanho (x, y, largura, altura).
        pygame.draw.rect(tela, obs[4], obs[:4])

        # Move o obstáculo para a esquerda na tela, subtraindo 5 da posição x.
        # Isso faz com que o obstáculo se desloque horizontalmente ao longo do tempo.
        obs[0] -= 5

        # Verifica se o obstáculo saiu da tela pela esquerda.
        # 'obs[2]' é a largura do obstáculo, então '-obs[2]' é a posição fora da tela.
        if obs[0] < -obs[2]:
            
            # Se o obstáculo saiu da tela, reposiciona-o para o lado direito da tela,
            # para que ele possa entrar novamente como um novo obstáculo.
            obs[0] = largura_tela

            # Gera uma nova altura aleatória para o obstáculo, entre 100 e 150 pixels.
            nova_altura = random.randint(100, 150)

            # Reposiciona o obstáculo no eixo y para que ele esteja sobre o chão,
            # levando em consideração a nova altura do obstáculo.
            obs[1] = altura_tela - nova_altura - altura_chao

            # Gera uma nova largura aleatória para o obstáculo, entre 40 e 70 pixels.
            obs[2] = random.randint(40, 70)

            # Atualiza a altura do obstáculo para a nova altura gerada.
            obs[3] = nova_altura

            # Escolhe uma nova cor aleatoriamente para o obstáculo,
            # podendo ser vermelho, verde ou azul.
            obs[4] = random.choice([vermelho, verde, azul])

            # Incrementa a pontuação do jogador em 10 pontos.
            # Isso ocorre sempre que um obstáculo é reposicionado,
            # significando que o jogador conseguiu passar pelo obstáculo anterior.
            pontos += 10
        
    
    # Lógica de colisão
    # Este loop percorre cada obstáculo na lista de obstáculos.    
    for obs in obstaculos:
        
        # Verifica se há uma sobreposição horizontal entre o boneco e o obstáculo.
        # 'x_boneco + 50' é a posição frontal do boneco no eixo x, considerando sua largura.
        # 'obs[0]' é a posição do obstáculo no eixo x.
        # 'obs[0] + obs[2]' é a posição frontal do obstáculo no eixo x, considerando sua largura.
        # A primeira condição confirma se o boneco está à direita do lado esquerdo do obstáculo e
        # se a parte esquerda do boneco está à esquerda do lado direito do obstáculo.
        if x_boneco + 50 > obs[0] and x_boneco < obs[0] + obs[2]:
            
            # Verifica se há uma sobreposição vertical entre o boneco e o obstáculo.
            # 'y_boneco + 50' é a posição inferior do boneco no eixo y, considerando sua altura.
            # 'obs[1]' é a posição superior do obstáculo no eixo y.
            # Esta condição confirma se a parte inferior do boneco está abaixo do topo do obstáculo.
            if y_boneco + 50 > obs[1]:
                
                # Se ambas as condições forem verdadeiras, uma colisão ocorreu e o jogo termina.
                fim_de_jogo = True

                # Toca o som de perda, indicando que o jogador colidiu com um obstáculo e perdeu o jogo.
                som_perda.play()

                # Aguarda 3000 milissegundos (3 segundos), para que o som de perda possa ser ouvido.
                pygame.time.delay(3000)

                # Sai do loop 'for' imediatamente, pois não precisamos mais verificar
                # colisões com outros obstáculos.
                break

                # Encerra o Pygame. Esta linha nunca será alcançada devido ao 'break' acima.
                # Se a lógica de saída do jogo estiver após o loop 'for', você não precisa deste 'break'.
                pygame.quit()

                # Encerra o script Python completamente. Assim como 'pygame.quit()', esta linha
                # não será executada devido ao 'break'. Ela só seria necessária se o 'break' não existisse.
                sys.exit()
                
                
    # Exibe pontuação
    # Esta linha cria um objeto de texto com a pontuação atual do jogador.
    # 'fonte.render' cria uma imagem do texto que será exibida na tela.
    # O primeiro argumento é uma string formatada que exibe a 
    # palavra "Pontos:" seguida do valor da variável 'pontos'.
    # O segundo argumento 'True' indica que o texto será antialiasado (bordas suavizadas).
    # O terceiro argumento 'preto' define a cor do texto.
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, preto)

    # Esta linha 'blit' copia o conteúdo da superfície do texto para a 
    # superfície da tela na posição [10, 10].
    # As posições [10, 10] definem onde o canto superior esquerdo do
    # texto será posicionado na tela, neste caso, 10 pixels
    # para a direita e 10 pixels para baixo a partir do canto superior esquerdo da tela.
    tela.blit(texto_pontos, [10, 10])
    
    
    # Atualiza a tela inteira
    # 'pygame.display.update()' atualiza a tela com tudo que foi desenhado desde a última atualização.
    # Isso inclui o texto da pontuação, o boneco, os obstáculos, etc.
    pygame.display.update()

    # Controle de quadros por segundo
    # 'relogio.tick(30)' limita o jogo a no máximo 30 quadros por segundo.
    # Isso significa que independente da velocidade do computador, o jogo não rodará a mais de 30 FPS,
    # o que ajuda a manter a consistência na jogabilidade.
    relogio.tick(30)

# Encerra o Pygame
# 'pygame.mixer.music.stop()' interrompe qualquer música ou som que esteja tocando no momento.
# Isso é útil para garantir que não haja sons tocando após o encerramento do jogo.
pygame.mixer.music.stop()

# Fecha a janela do Pygame
# 'pygame.quit()' é usado para desinicializar todos os módulos do Pygame que foram inicializados.
# Isso irá fechar a janela do jogo e liberar os recursos que o Pygame estava utilizando.
pygame.quit()

# Encerra o script Python
# 'sys.exit()' é uma maneira de encerrar o script Python.
# Ele diz ao Python para parar a execução do programa.
# Isso é útil quando temos uma condição de encerramento do jogo e
# queremos fechar tudo imediatamente.
sys.exit()
            
    