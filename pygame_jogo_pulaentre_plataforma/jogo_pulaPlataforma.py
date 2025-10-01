
# Importa o módulo pygame, que é usado para escrever jogos em Python.
import pygame

# Importa o módulo random, que contém funções para gerar números aleatórios.
import random

# A função 'pygame.init()' é chamada para inicializar todos 
# os módulos importados da biblioteca pygame necessários para o jogo.
# Isso prepara a biblioteca pygame para ser usada, inicializando os módulos de vídeo e eventos.
pygame.init()

# A função 'pygame.mixer.init()' inicializa o módulo de mixer de áudio do pygame.
# Isso é necessário para carregar e reproduzir sons durante o jogo.
pygame.mixer.init()

# As próximas três linhas definem as dimensões da janela do jogo.
# 'largura_tela' e 'altura_tela' são variáveis que armazenam valores
# inteiros representando a largura e altura da janela do jogo, respectivamente.
largura_tela = 800
altura_tela = 600

# 'pygame.display.set_mode()' cria a janela do jogo com as
# dimensões especificadas pelas variáveis 'largura_tela' e 'altura_tela'.
# O resultado é armazenado na variável 'tela', que será usada para 
# desenhar elementos do jogo e atualizar a tela.
tela = pygame.display.set_mode((largura_tela, altura_tela))

# 'pygame.display.set_caption()' define o título da janela do 
# jogo que aparece na barra de título da janela.
pygame.display.set_caption('Jogo de Plataforma')

# Aqui são definidas constantes para cores usando o modelo de 
# cores RGB, onde cada cor é uma tupla contendo três inteiros entre 0 e 255.
# Estas cores serão usadas para desenhar elementos na tela.
# 'BRANCO' é definido como uma mistura completa de vermelho, verde e azul, resultando em branco.
BRANCO = (255, 255, 255)

# 'PRETO' é a ausência de cor, portanto, todos os valores são definidos como 0.
PRETO = (0, 0, 0)

# 'AMARELO' é definido com a máxima intensidade de vermelho 
# e verde, mas sem azul, resultando em amarelo.
AMARELO = (255, 255, 0)

# 'pygame.image.load' é uma função que carrega uma imagem do disco para a memória. 
# A string 'boneco.png' é o caminho para o arquivo de imagem do personagem que se deseja carregar.
# O resultado desta operação de carregamento é armazenado na variável 'personagem'.
personagem = pygame.image.load('boneco.png')

# 'pygame.transform.scale' é uma função que redimensiona uma 
# superfície (neste caso, a imagem do personagem) para um novo tamanho.
# O parâmetro (50, 50) define as novas dimensões da imagem do personagem, tornando-a um quadrado de 50x50 pixels.
# Isso pode ser necessário para garantir que o personagem se ajuste corretamente à escala do jogo.
personagem = pygame.transform.scale(personagem, (50, 50))

# 'get_rect()' é um método que retorna um novo objeto Rect que encapsula a imagem com as dimensões especificadas.
# Este objeto Rect, armazenado em 'rect_personagem', será usado 
# para controlar a posição e detectar colisões para o personagem no jogo.
rect_personagem = personagem.get_rect()

# 'rect_personagem.x' e 'rect_personagem.y' são atributos do 
# objeto Rect que definem a posição do retângulo no eixo x (horizontal) e y (vertical), respectivamente.
# Aqui, eles são definidos para posicionar o personagem em (50, 300) na
# tela, o que geralmente é uma posição inicial adequada em muitos jogos de plataforma.
rect_personagem.x = 50  # Posição horizontal inicial do personagem.
rect_personagem.y = 300  # Posição vertical inicial, possivelmente situando o personagem no chão ou em uma plataforma.


# As próximas três variáveis definem a física do pulo do personagem.
# 'gravidade' define a força constante que puxa o personagem para baixo.
gravidade = 2

# 'velocidade_pulo_curto' define a velocidade inicial
# negativa (para cima na tela) de um pulo curto.
velocidade_pulo_curto = -15

# 'velocidade_pulo_longo' tem um valor negativo maior que 
# 'velocidade_pulo_curto', resultando em um pulo mais alto.
velocidade_pulo_longo = -20

# 'pulo' é um booleano que rastreia se o personagem está atualmente pulando.
pulo = False

# 'plataformas' é uma lista que será preenchida com objetos Rect representando plataformas no jogo.
# Cada plataforma é um retângulo onde o personagem pode pousar.
plataformas = []


# Inimigos
# 'inimigos' é uma lista que irá armazenar os objetos que representam os inimigos no jogo.
inimigos = []

# 'pygame.image.load' é usado para carregar a imagem 'inimigo.png' do sistema de arquivos.
# Esta imagem será usada como a representação gráfica dos inimigos no jogo.
inimigo_imagem = pygame.image.load('aviao.png')

# 'pygame.transform.scale' é uma função que redimensiona a imagem carregada para as dimensões fornecidas.
# Aqui, a imagem do inimigo é redimensionada para ter 50 pixels de largura e 50 pixels de altura.
# Isso garante que a imagem do inimigo se encaixe na estética do jogo e tenha um tamanho apropriado para a tela.
inimigo_imagem = pygame.transform.scale(inimigo_imagem, (100, 100))


# A lista 'tiros_inimigos' é inicializada.
# Ela será usada para armazenar e rastrear os projéteis disparados pelos inimigos no jogo.
tiros_inimigos = []

# Similarmente, 'tiros_jogador' é uma lista destinada a rastrear os projéteis disparados pelo jogador.
# Durante o jogo, quando o jogador atira, os projéteis serão adicionados a esta lista.
tiros_jogador = []

# 'vidas' é uma variável que armazena o número de vidas que o personagem do jogador tem.
# O jogador começa com 3 vidas, e este valor será decrementado cada vez que
# o personagem for atingido por um inimigo ou projétil.
vidas = 3


# A variável 'pontuacao' é inicializada com o valor 0.
# Esta variável será usada para rastrear a pontuação do jogador 
# ao longo do jogo, aumentando quando certos eventos ocorrerem, como derrotar inimigos.
pontuacao = 0

# 'pygame.font.SysFont' cria um objeto de fonte que pode ser usado para renderizar texto na tela.
# 'None' significa que será usada a fonte padrão do sistema.
# O número '36' é o tamanho da fonte.
# Este objeto de fonte será usado para desenhar a pontuação do jogador na tela.
fonte = pygame.font.SysFont(None, 36)

# A variável 'tempo_ultimo_tiro' armazena o número de milissegundos desde que o pygame foi inicializado.
# Isso é usado para controlar quando os inimigos podem disparar novamente.
tempo_ultimo_tiro = pygame.time.get_ticks()

# 'tempo_entre_tiros' é definido como 5000 milissegundos (ou 5 segundos), que
# é o intervalo de tempo que deve passar antes que os inimigos possam atirar novamente.
tempo_entre_tiros = 5000

# 'pygame.mixer.Sound' carrega um arquivo de som que será usado para o efeito sonoro de tiro no jogo.
# O arquivo 'tiro.mp3' é passado como argumento, mas pode ser substituído pelo nome de qualquer arquivo de som válido.
som_tiro = pygame.mixer.Sound('tiro.mp3')

# 'rodando' é uma variável booleana que controla o loop principal do jogo.
# Enquanto 'rodando' for True, o loop do jogo continua executando.
rodando = True

# 'primeiro_pulo' é uma variável booleana usada para verificar se o personagem do jogador já executou seu primeiro pulo.
# Isso pode ser usado para impedir que o jogador pule novamente enquanto ainda está no ar.
primeiro_pulo = False

# 'tiro_disparado' é uma variável booleana que rastreia se um tiro foi disparado.
# Isso pode ser usado para controlar a lógica de disparo, como limitar a frequência dos tiros.
tiro_disparado = False

# O arquivo de imagem 'fundo_lava.jpg' é carregado usando 'pygame.image.load'.
# Este será o plano de fundo do jogo, dando um contexto visual para o ambiente do jogo.
imagem_fundo = pygame.image.load('fundo_lava.jpg')

# A imagem de fundo é redimensionada para preencher a tela inteira usando 'pygame.transform.scale'.
# A imagem é dimensionada para corresponder à 'largura_tela' e 'altura_tela' definidas anteriormente.
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura_tela, altura_tela))


# Este é um loop 'for' que irá iterar cinco vezes, com a variável 'i' começando de 0 e indo até 4.
# O propósito deste loop é criar cinco plataformas que serão usadas no jogo.
for i in range(5):
    
    # 'plataforma_x' é uma variável que calcula a posição horizontal 'x' para cada plataforma.
    # Cada plataforma é posicionada a 250 pixels de distância uma da outra no eixo x.
    # O valor é calculado multiplicando o índice 'i' do loop por 250.
    # Isso espaça as plataformas uniformemente ao longo do eixo horizontal.
    plataforma_x = i * 250

    # 'plataforma_y' é uma variável que armazena um valor 
    # aleatório para a posição vertical 'y' de cada plataforma.
    # O valor é escolhido aleatoriamente entre 300 e 500 pixels.
    # Isso significa que cada plataforma terá uma altura diferente dentro desse intervalo.
    plataforma_y = random.randint(300, 500)

    # 'pygame.Rect' é uma função que cria um objeto retangular que representa a plataforma.
    # Os argumentos são as posições x e y calculadas acima, seguidas pela 
    # largura (100 pixels) e altura (10 pixels) da plataforma.
    # Este objeto retangular é usado para desenhar a plataforma na tela e para a detecção de colisão.
    plataforma = pygame.Rect(plataforma_x, plataforma_y, 100, 10)

    # 'plataformas.append(plataforma)' adiciona o objeto retangular criado à lista 'plataformas'.
    # Isso é feito para cada uma das cinco iterações do loop, resultando em cinco plataformas com posições x e y diferentes.
    plataformas.append(plataforma)
    

    
# A função 'criar_inimigo' é definida com três parâmetros: 'inimigo_imagem', que é esperado ser um objeto de imagem do Pygame
# representando o gráfico do inimigo; 'largura_tela', a largura total da janela do jogo; e 'altura_tela', a altura total da janela do jogo.
# Esta função é chamada para criar uma nova entidade de inimigo com uma posição inicial aleatória e velocidade.
def criar_inimigo(inimigo_imagem, largura_tela, altura_tela):
    
    # 'inimigo_imagem.copy()' cria uma cópia independente da imagem original do inimigo. Isso é feito para evitar modificar
    # a imagem original quando forem feitas alterações no inimigo, como movê-lo pela tela ou aplicar efeitos gráficos.
    inimigo = inimigo_imagem.copy()
    
    # 'get_rect()' é um método que cria um novo objeto Rect (que é essencialmente um retângulo) com as mesmas proporções da imagem.
    # Este objeto Rect é crucial porque oferece uma maneira de controlar a posição do inimigo na tela e é amplamente utilizado para
    # detecção de colisão no Pygame. O Rect contém propriedades como 'x', 'y', 'width', 'height' que definem sua posição e tamanho.
    inimigo_rect = inimigo.get_rect()
    
    # 'inimigo_rect.x' é a propriedade que determina a posição horizontal do retângulo (e, consequentemente, da imagem do inimigo) na tela.
    # Aqui, ele é definido para um valor que é a largura total da tela mais um número aleatório entre 100 e 200 pixels.
    # Isso significa que o inimigo será posicionado fora da tela para a direita, de forma que ele possa se mover para a esquerda e entrar na área visível.
    inimigo_rect.x = largura_tela + random.randint(100, 200)
    
    # 'inimigo_rect.y' é a propriedade que determina a posição vertical do retângulo na tela. Definir esta posição para um número aleatório
    # entre 100 e 'altura_tela - 100' assegura que o inimigo apareça em um local vertical aleatório, mas dentro dos limites da tela, evitando
    # que seja desenhado muito perto das bordas superior e inferior.
    inimigo_rect.y = random.randint(100, altura_tela - 100)
    
    # 'velocidade_inimigo' é uma variável que armazena um número inteiro aleatório entre 2 e 5. Este valor é usado para determinar
    # quão rápido o inimigo se move pela tela. Um valor maior resultará em um inimigo mais rápido.
    velocidade_inimigo = random.randint(2, 5)
    
    # A função retorna um tuplo com três elementos: 'inimigo', que é a cópia da imagem do inimigo; 'inimigo_rect', o objeto Rect que 
    # será usado para gerenciar a posição e colisão do inimigo na tela; e 'velocidade_inimigo', o valor que define a velocidade de movimento.
    return inimigo, inimigo_rect, velocidade_inimigo



# Este bloco de código está configurando inimigos para o jogo.
# Um loop 'for' é utilizado para criar três inimigos, o que é indicado pelo 'range(3)'.
# O caractere '_' é usado como uma variável temporária ou de descarte, que não será usada no bloco do loop.
for _ in range(3):
    
    # A função 'criar_inimigo' é chamada com a imagem do inimigo, a largura e a altura da tela como argumentos.
    # Essa função retorna três valores: a cópia da imagem do inimigo, o objeto Rect 
    # associado para detecção de colisões e a velocidade do inimigo.
    inimigo, inimigo_rect, velocidade_inimigo = criar_inimigo(inimigo_imagem, largura_tela, altura_tela)

    # O trio retornado pela função 'criar_inimigo' é adicionado à lista 'inimigos'.
    # Isso permite que o jogo mantenha um registro de todos os inimigos criados
    # para processamento posterior, como movimento e renderização.
    inimigos.append((inimigo, inimigo_rect, velocidade_inimigo))

    # A posição x do retângulo do inimigo é ajustada para espaçar os inimigos horizontalmente.
    # O valor é incrementado multiplicando o índice atual do loop por 150.
    # Isso significa que cada inimigo subsequente será posicionado 150 pixels mais à direita do que o anterior.
    inimigo_rect.x += _ * 150
   
    
    

# Este é o início do loop principal do jogo. O loop continuará enquanto a variável 'rodando' for True.
# 'rodando' é uma variável booleana que determina se o jogo está ativo. 
# Se 'rodando' for False, o loop e o jogo terminarão.
while rodando:

    # 'tela.blit' desenha a imagem de fundo na superfície da tela.
    # 'imagem_fundo' é o objeto de imagem que foi carregado e dimensionado 
    # anteriormente para se ajustar à tela.
    # O par de coordenadas (0, 0) especifica que a imagem de fundo
    # deve ser desenhada começando do canto superior esquerdo da tela.
    tela.blit(imagem_fundo, (0, 0))

    # Este é um loop 'for' que processa todos os eventos na fila de eventos do pygame.
    # 'pygame.event.get()' obtém todos os eventos da fila de eventos desde a
    # última vez que foi chamado.
    for evento in pygame.event.get():
        
        # 'if evento.type == pygame.QUIT:' verifica se o evento atual é 
        # do tipo QUIT, que ocorre quando o usuário fecha a janela do jogo.
        if evento.type == pygame.QUIT:
            
            # Se o evento for do tipo QUIT, 'rodando' é definido como
            # False, o que fará com que o loop principal pare.
            rodando = False
            
            
    # 'pygame.key.get_pressed()' obtém o estado de todas as teclas do teclado.
    # Isso retorna uma lista de booleanos representando o estado 
    # pressionado ou não de cada tecla.
    teclas = pygame.key.get_pressed()

    # As próximas duas condições verificam se a tecla para mover o 
    # personagem para a esquerda ou para a direita foi pressionada.
    # 'pygame.K_LEFT' e 'pygame.K_RIGHT' são constantes que representam 
    # as teclas de seta para esquerda e direita, respectivamente.
    
    # Se a tecla de seta para a esquerda for pressionada, o código move o 
    # personagem para a esquerda diminuindo o valor 'x' de 'rect_personagem'.
    if teclas[pygame.K_LEFT]:
        rect_personagem.x -= 5  # Subtrai 5 pixels da posição x, movendo o 
                                # personagem 5 pixels para a esquerda.
        
    # Se a tecla de seta para a direita for pressionada, o código move o
    # personagem para a direita aumentando o valor 'x' de 'rect_personagem'.
    if teclas[pygame.K_RIGHT]:
        rect_personagem.x += 5  # Adiciona 5 pixels à posição x, movendo o
                                # personagem 5 pixels para a direita.


    # Este comentário indica que o código a seguir implementa a
    # funcionalidade de pulo curto e longo para o personagem.
    # Pulo curto e longo
    # A condição verifica se a tecla de espaço ('pygame.K_SPACE') foi
    # pressionada e se o personagem não está atualmente em um pulo ('not pulo').
    if teclas[pygame.K_SPACE] and not pulo:
        
        # Se ambas as condições forem verdadeiras, a variável 'pulo' é 
        # definida como True, indicando que o personagem está no meio de um pulo.
        pulo = True
        
        # A variável 'velocidade_pulo' é definida como 'velocidade_pulo_curto', 
        # que é uma velocidade negativa que move o personagem para cima na tela.
        velocidade_pulo = velocidade_pulo_curto
        
        # 'primeiro_pulo' é definido como True para registrar que o
        # personagem realizou um pulo.
        primeiro_pulo = True  # marcar que o personagem já pulou

    # Uma condição similar verifica se a tecla para cima ('pygame.K_UP') foi
    # pressionada e se o personagem não está em um pulo.
    if teclas[pygame.K_UP] and not pulo:
        
        # Se essas condições forem verdadeiras, o personagem começa um pulo longo.
        pulo = True
        
        # A velocidade de pulo é definida como 'velocidade_pulo_longo', que é
        # uma velocidade de pulo mais alta (mais negativa) que a curta, resultando
        # em um pulo mais alto.
        velocidade_pulo = velocidade_pulo_longo  # pulo longo
        
        # Novamente, 'primeiro_pulo' é definido como True para registrar que um pulo foi feito.
        primeiro_pulo = True  # marcar que o personagem já pulou

        
    # Esta condição é verificada a cada iteração do loop para ver se o personagem
    # está no meio de um pulo.
    if pulo:
        
        # Se estiver pulando, a posição vertical 'y' do personagem é ajustada 
        # pela 'velocidade_pulo'.
        rect_personagem.y += velocidade_pulo
        
        # A 'velocidade_pulo' é incrementada em 1 a cada iteração para
        # simular a força da gravidade trazendo o personagem de volta para baixo.
        velocidade_pulo += 1  # ajustar a velocidade do pulo para simular a gravidade

    # Independentemente de o personagem estar pulando ou não, a gravidade é sempre aplicada.
    # Isso simula a gravidade puxando o personagem para baixo constantemente.
    # A posição vertical 'y' é ajustada pela variável 'gravidade' para que o
    # personagem caia ou desça gradualmente se estiver no ar.
    # Gravidade
    rect_personagem.y += gravidade


    # Esta condição é verificada para ver se o personagem caiu abaixo do
    # limite inferior da tela, o que indicaria que ele "caiu" e deveria perder uma vida.
    # 'rect_personagem.y' é a posição vertical do personagem e
    # 'rect_personagem.height' é a altura do personagem.
    # 'altura_tela' é a altura total da janela do jogo.
    if rect_personagem.y + rect_personagem.height > altura_tela and primeiro_pulo:
        
        # Se o personagem caiu abaixo da tela após ter pulado, uma vida é 
        # subtraída da contagem total de vidas do jogador.
        vidas -= 1  # Perde uma vida
        
        # Esta condição verifica se o número de vidas restantes é zero ou menor.
        if vidas <= 0:
            
            # Se não houver mais vidas, uma mensagem de "Fim de jogo" é 
            # exibida com a pontuação final.
            # A variável 'pontuacao' é usada para mostrar ao jogador sua
            # pontuação no final do jogo.
            print(f"Fim de jogo! Sua pontuação foi: {pontuacao}")
            
            # 'rodando' é definido como False, o que fará com que o loop
            # principal do jogo pare, terminando o jogo.
            rodando = False
            
        else:
            
            # Se ainda restarem vidas, o personagem é redefinido para a posição inicial na tela.
            # 'rect_personagem.x' é redefinido para 50, que é a posição horizontal inicial.
            # 'rect_personagem.y' é redefinido para 300, que é a posição vertical inicial acima do chão.
            rect_personagem.x = 50
            rect_personagem.y = 300
            
            # A variável 'pulo' é redefinida como False, indicando que o personagem
            # não está mais pulando e pode pular novamente.
            pulo = False
            
    
    # Este é um loop 'for' que percorre cada 'plat' na lista 'plataformas'.
    # 'plataformas' é uma lista de objetos Rect que representam as plataformas no jogo.
    for plat in plataformas:
        
        # 'rect_personagem.colliderect(plat)' verifica se o retângulo que representa o 
        # personagem ('rect_personagem') está colidindo
        # (ou seja, tem uma interseção) com o retângulo que representa uma plataforma ('plat').
        # Esta é uma forma de detectar colisões entre objetos no Pygame.
        if rect_personagem.colliderect(plat):
            
            # Se uma colisão for detectada, a posição vertical 'y' do
            # personagem é ajustada para que ele "pouse" na plataforma.
            # 'plat.y' é a posição vertical da borda superior da plataforma,
            # subtraindo 'rect_personagem.height' (a altura do personagem)
            # coloca o personagem diretamente em cima da plataforma, sem sobreposição.
            rect_personagem.y = plat.y - rect_personagem.height
            
            # Uma vez que o personagem colide com uma plataforma, 'pulo' é 
            # definido como False, indicando que o personagem não está mais no ar
            # e pode iniciar outro pulo.
            pulo = False
            
            # 'break' termina o loop 'for' antecipadamente uma vez
            # que a colisão com uma plataforma foi tratada.
            # Não é necessário verificar colisões com outras plataformas
            # até que o próximo frame do jogo seja processado.
            break
            
            
    # Este é um loop 'for' que itera sobre cada inimigo na lista 'inimigos'.
    # A função 'enumerate()' é usada para ter acesso tanto ao índice atual 'i' 
    # quanto ao conteúdo do item atual da lista 'inimigos'.
    # Cada item é um tuplo contendo a imagem do inimigo, o objeto Rect para
    # detecção de colisão ('inimigo_rect') e um valor descartado ('_').
    for i, (inimigo, inimigo_rect, _) in enumerate(inimigos):
        
        # 'rect_personagem.colliderect(inimigo_rect)' verifica se o 
        # retângulo ('Rect') do personagem está colidindo com o retângulo de algum inimigo.
        # Esta é a forma de detectar colisões entre o personagem e os inimigos no jogo.
        if rect_personagem.colliderect(inimigo_rect):
            
            # Se ocorrer uma colisão, uma vida é subtraída do total de vidas do personagem.
            vidas -= 1  # Perde uma vida
            
            # Se após perder uma vida, o número total de vidas restantes for
            # 0 ou menos, o jogo termina.
            if vidas <= 0:
                
                # Uma mensagem é impressa no console para informar o jogador que o 
                # jogo terminou e mostrar a pontuação alcançada.
                print(f"Fim de jogo! Sua pontuação foi: {pontuacao}")
                
                # A variável 'rodando' é definida como False para terminar o 
                # loop principal do jogo, efetivamente encerrando o jogo.
                rodando = False
                
            else:
                
                # Se o jogador ainda tiver vidas restantes, o personagem é 
                # reposicionado para a posição inicial.
                # Isso significa que 'rect_personagem.x' é definido para 50, que
                # é a posição inicial horizontal,
                # e 'rect_personagem.y' é definido para 300, que é a posição inicial
                # vertical acima do chão.
                rect_personagem.x = 50
                rect_personagem.y = 300
                
                # A variável 'pulo' é redefinida para False, o que permite
                # que o jogador faça um novo pulo.
                pulo = False
                
            # A instrução 'break' interrompe o loop 'for' assim que uma colisão é detectada e tratada.
            # Isso é eficiente porque, uma vez que o personagem colidiu com um
            # inimigo e as consequências foram aplicadas, não é necessário continuar
            # verificando colisões com outros inimigos até o próximo ciclo do loop.
            break
        
    
    # Este é um loop 'for' que percorre cada objeto Rect na lista 'plataformas'.
    # Cada 'plat' na lista representa uma plataforma no jogo.
    for plat in plataformas:
        
        # A posição horizontal 'x' da plataforma é decrementada por 5.
        # Isso move a plataforma para a esquerda na tela, criando um 
        # efeito de deslocamento do cenário que simula o movimento do personagem.
        plat.x -= 5
        
        # A condição verifica se a plataforma se moveu para além da borda esquerda da tela.
        # 'plat.x + plat.width' é o ponto mais à direita da plataforma; se 
        # esse valor for menor que 0, a plataforma saiu completamente da tela.
        if plat.x + plat.width < 0:
            
            # Se a plataforma saiu da tela, sua posição 'x' é redefinida para 'largura_tela', que é o lado direito da tela,
            # fazendo com que a plataforma reapareça do outro lado e continue seu movimento para a esquerda novamente.
            plat.x = largura_tela
            
            # A posição vertical 'y' da plataforma é redefinida para um valor aleatório entre 300 e 500,
            # o que dá à plataforma uma nova altura aleatória cada vez que ela é reposicionada.
            plat.y = random.randint(300, 500)
            
            # Quando uma plataforma é reposicionada, a pontuação do jogador é incrementada em 10.
            # Isso recompensa o jogador por permanecer no jogo por tempo 
            # suficiente para que as plataformas sejam recicladas.
            pontuacao += 10  # Aumenta a pontuação
            
            
    # Este é um loop 'for' que percorre a lista de 'inimigos'. A função 'enumerate' é
    # usada para obter tanto o índice (i) quanto o valor de cada item na lista.
    # Cada item na lista 'inimigos' é um tuplo contendo a imagem do inimigo, o 
    # objeto Rect associado a esse inimigo (para detecção de colisão e posicionamento),
    # e a velocidade desse inimigo.
    for i, (inimigo, inimigo_rect, velocidade_inimigo) in enumerate(inimigos):
        
        # O valor 'x' do retângulo do inimigo ('inimigo_rect') é decrementado pela 'velocidade_inimigo'.
        # Isso move o inimigo para a esquerda na tela a cada iteração do loop 
        # principal do jogo, com a velocidade determinada pelo valor 'velocidade_inimigo'.
        inimigo_rect.x -= velocidade_inimigo

        # Aqui, verificamos se a borda direita do retângulo do inimigo ('inimigo_rect.right') é menor que 0,
        # o que significaria que o inimigo se moveu completamente para fora da tela (além da borda esquerda).
        if inimigo_rect.right < 0:
            
            # Se o inimigo saiu da tela, ele é reposicionado chamando a função 'criar_inimigo'.
            # Essa função cria um novo inimigo com uma posição inicial aleatória 
            # fora da tela à direita e com uma velocidade aleatória.
            # O novo inimigo é então colocado de volta na lista 'inimigos' na
            # mesma posição do inimigo que saiu da tela,
            # substituindo-o efetivamente.
            inimigos[i] = criar_inimigo(inimigo_imagem, largura_tela, altura_tela)
            
            
    # 'random.random()' gera um número flutuante aleatório entre 0.0 e 1.0.
    # A condição verifica se este número aleatório é menor que 0.2, o que acontece 
    # aproximadamente 20% das vezes que o código é executado.
    # Além disso, verifica se a quantidade atual de inimigos ('len(inimigos)') é menor que 3.
    # Essas duas condições juntas limitam a frequência e o número de
    # inimigos que podem aparecer na tela ao mesmo tempo.
    if random.random() < 0.2 and len(inimigos) < 3:
        
        # Se as condições forem verdadeiras, um novo inimigo é criado chamando a função 'criar_inimigo'.
        # Esta função é definida em outro lugar no código e responsável por gerar um inimigo com uma posição e velocidade aleatórias.
        # A função retorna um tuplo contendo a imagem do inimigo, o objeto Rect para detecção de colisão, e a velocidade do inimigo.
        inimigo, inimigo_rect, velocidade_inimigo = criar_inimigo(inimigo_imagem, largura_tela, altura_tela)

        # O novo inimigo criado é então adicionado à lista 'inimigos' usando o método 'append'.
        # Isso aumenta o número de inimigos na tela, tornando o jogo mais desafiador.
        inimigos.append((inimigo, inimigo_rect, velocidade_inimigo))
        
        
    # Controle de tempo para os tiros dos inimigos
    # 'pygame.time.get_ticks()' retorna o número de milissegundos desde que o pygame foi inicializado.
    # Isso é armazenado na variável 'tempo_atual' e é usado para medir o tempo entre eventos, como os tiros dos inimigos.
    tempo_atual = pygame.time.get_ticks()

    # Esta condição verifica se o tempo decorrido desde o 'tempo_ultimo_tiro' (a última vez que um inimigo atirou) é maior do que
    # o 'tempo_entre_tiros', que é definido em milissegundos. Se sim, significa que é hora dos inimigos atirarem novamente.
    if tempo_atual - tempo_ultimo_tiro > tempo_entre_tiros:
        
        # Este é um loop 'for' que percorre a lista de 'inimigos'.
        # O caractere '_' é usado para ignorar os valores não utilizados no tuplo (neste caso, a imagem do inimigo e sua velocidade).
        for (_, inimigo_rect, _) in inimigos:
            
            # Um novo objeto Rect é criado com 'pygame.Rect'. Este objeto representa o tiro disparado pelo inimigo.
            # As coordenadas 'centerx' e 'centery' do retângulo do inimigo ('inimigo_rect') são usadas para posicionar o tiro
            # no centro do inimigo, e o tiro tem uma largura de 10 pixels e uma altura de 5 pixels.
            tiro_rect = pygame.Rect(inimigo_rect.centerx, inimigo_rect.centery, 10, 5)
            
            # O novo objeto Rect que representa o tiro é adicionado à lista 'tiros_inimigos'.
            # Isso permite que o jogo mantenha um registro dos tiros na tela e os mova adequadamente.
            tiros_inimigos.append(tiro_rect)
            
            # O método 'play' do objeto 'som_tiro' é chamado para reproduzir o som do tiro.
            # Isso adiciona uma resposta auditiva ao ato de atirar, melhorando a experiência do usuário.
            som_tiro.play()
            
        # Após os inimigos atirarem, 'tempo_ultimo_tiro' é atualizado para o 'tempo_atual'.
        # Isso reinicia o temporizador para o próximo tiro e garante que os tiros ocorram apenas em intervalos regulares.
        tempo_ultimo_tiro = tempo_atual
        
        
        
    # 'tiros_inimigos' é uma lista que contém os objetos Rect que 
    # representam os tiros dos inimigos.
    # Este é um loop 'for' que percorre cada 'tiro_rect' na lista 'tiros_inimigos'.
    for tiro_rect in tiros_inimigos:
        
        # A posição horizontal 'x' do tiro é decrementada por 5 pixels.
        # Isso move cada tiro para a esquerda na tela, simulando o 
        # disparo dos inimigos em direção ao personagem do jogador.
        tiro_rect.x -= 5

    # Após mover os tiros, um novo loop 'for' é iniciado para verificar 
    # se algum tiro colidiu com o personagem.
    for tiro_rect in tiros_inimigos:
        
        # 'rect_personagem.colliderect(tiro_rect)' verifica se o retângulo 
        # que representa o personagem está colidindo com o retângulo de um tiro.
        if rect_personagem.colliderect(tiro_rect):
            
            # Se ocorrer uma colisão, o personagem perde uma vida.
            vidas -= 1  # Subtrai 1 do total de vidas.
            
            # O tiro que colidiu com o personagem é removido da lista 'tiros_inimigos'.
            # Isso impede que o mesmo tiro seja contabilizado mais de uma vez e 
            # também remove o tiro da tela.
            tiros_inimigos.remove(tiro_rect)
            
            # Se o número de vidas restantes for igual ou menor que 0, o jogo termina.
            if vidas <= 0:
                
                # Uma mensagem de 'Fim de jogo' é exibida no console junto com a 
                # pontuação que o jogador conseguiu.
                print(f"Fim de jogo! Sua pontuação foi: {pontuacao}")
                
                # A variável 'rodando' é definida como False, o que causa a 
                # saída do loop principal do jogo, efetivamente terminando o jogo.
                rodando = False
                
            else:
                
                # Se ainda restarem vidas, o personagem é reposicionado para a
                # posição inicial no jogo.
                # A posição 'x' é definida como 50 e a posição 'y' como 300.
                rect_personagem.x = 50
                rect_personagem.y = 300
                
                # A variável 'pulo' é redefinida como False para indicar que 
                # o personagem não está pulando e pode iniciar outro pulo.
                pulo = False
                
            # A instrução 'break' é usada para sair do loop assim que uma colisão é tratada.
            # Isso evita que o personagem perca mais de uma vida por um único
            # tiro na mesma atualização do jogo.
            break
            
            
    # Inicia-se um loop 'for' que percorre todos os tiros do 
    # jogador, armazenados na lista 'tiros_jogador'.
    # Cada 'tiro_rect' é um objeto Rect que representa a posição e
    # tamanho de um tiro disparado pelo jogador.
    for tiro_rect in tiros_jogador:
        
        # Dentro do primeiro loop, inicia-se um segundo loop 'for' que
        # itera sobre a lista 'inimigos', usando a função 'enumerate' para acessar
        # tanto o índice 'i' quanto os valores (inimigo, inimigo_rect, _), onde
        # 'inimigo_rect' é um objeto Rect para cada inimigo.
        for i, (inimigo, inimigo_rect, _) in enumerate(inimigos):
            
            # 'tiro_rect.colliderect(inimigo_rect)' verifica se o Rect do
            # tiro está colidindo com o Rect de algum inimigo.
            # Essa é a maneira de detectar se um tiro do jogador atingiu um inimigo.
            if tiro_rect.colliderect(inimigo_rect):
                
                # Se uma colisão é detectada, o código entra neste bloco 
                # condicional onde duas ações são realizadas:
                # Primeiro, o inimigo atingido é removido da lista 'inimigos'. Isso é 
                # feito usando o método 'pop',
                # que remove o item na posição 'i', que é o índice do inimigo que foi atingido.
                inimigos.pop(i)
                
                # Segundo, o tiro que atingiu o inimigo é removido da lista 'tiros_jogador', 
                # garantindo que o mesmo tiro não possa atingir mais de um inimigo.
                tiros_jogador.remove(tiro_rect)
                
                # A pontuação do jogador é aumentada em 50 pontos para cada inimigo atingido.
                # Isso recompensa o jogador por acertar um inimigo.
                pontuacao += 50
                
                # A instrução 'break' é utilizada para sair do segundo loop 
                # assim que uma colisão é tratada e as ações correspondentes são executadas.
                # Isso previne que o índice 'i' seja usado após a modificação da
                # lista 'inimigos', o que poderia causar erros,
                # e também impede a verificação desnecessária de colisões após o 
                # tiro já ter atingido um inimigo.
                break
                
    # Este é um loop 'for' que itera por cada objeto Rect na lista 'tiros_jogador'.
    # Cada 'tiro_rect' representa um tiro disparado pelo jogador.
    for tiro_rect in tiros_jogador:
        
        # A posição horizontal 'x' do tiro é incrementada por 5 pixels.
        # Isso move cada tiro para a direita na tela, na direção dos inimigos.
        # O valor 5 determina a rapidez com que o tiro se move a cada 
        # atualização de frame do jogo.
        tiro_rect.x += 5

    # A variável 'delay_entre_tiros' define o tempo mínimo requerido entre os tiros disparados pelo jogador.
    # O valor é definido em milissegundos, então 500 milissegundos equivalem a meio segundo.
    # Isso significa que o jogador precisa esperar pelo menos meio segundo antes de poder disparar outro tiro.
    delay_entre_tiros = 500  # 500 milissegundos (0,5 segundos)



    # Atirar com a tecla "Z"
    # 'pygame.time.get_ticks()' é chamado novamente para obter o 
    # número atual de milissegundos desde que o pygame foi iniciado.
    # Esta informação é armazenada em 'tempo_atual' e é usada para 
    # controlar o tempo entre os tiros.
    tempo_atual = pygame.time.get_ticks()

    # Aqui é verificado se a tecla "Z" está pressionada e se o tempo 
    # decorrido desde o último tiro é maior ou igual ao 'delay_entre_tiros'.
    # 'pygame.K_z' é a constante do pygame para a tecla "Z".
    # 'tempo_atual - tempo_ultimo_tiro' calcula quanto tempo passou desde o último tiro.
    # 'delay_entre_tiros' é o tempo definido que deve passar entre os tiros, neste caso, 500 milissegundos.
    if teclas[pygame.K_z] and tempo_atual - tempo_ultimo_tiro >= delay_entre_tiros:
        
        # Se ambas as condições forem verdadeiras, um novo objeto Rect é criado para representar o tiro.
        # 'rect_personagem.right' é a posição x à direita do personagem, 
        # 'rect_personagem.centery - 2.5' é a posição central y do personagem ajustada um pouco,
        # para que o tiro pareça sair do centro do personagem. '10' e '5' são a 
        # largura e a altura do tiro, respectivamente.
        tiro_rect = pygame.Rect(rect_personagem.right, rect_personagem.centery - 2.5, 10, 5)

        # O novo tiro é adicionado à lista 'tiros_jogador', o que permite que o
        # jogo rastreie todos os tiros na tela e os mova adequadamente.
        tiros_jogador.append(tiro_rect)

        # O som do tiro é reproduzido usando 'som_tiro.play()'. Isto adiciona 
        # feedback auditivo à ação de atirar.
        som_tiro.play()

        # 'tempo_ultimo_tiro' é atualizado para 'tempo_atual', reiniciando o contador desde o último tiro.
        # Isso impede que um novo tiro seja disparado até que o 'delay_entre_tiros' tenha passado.
        tempo_ultimo_tiro = tempo_atual  # Atualize o tempo do último tiro

    
    # Exibe a pontuação e as vidas
    # A variável 'texto_pontuacao' armazena o objeto de texto que será renderizado na tela.
    # O método 'fonte.render' é usado para criar uma imagem do texto
    # que representa a pontuação do jogador.
    # O primeiro argumento é uma string formatada que exibirá o texto
    # "Pontuação: " seguido do valor atual da variável 'pontuacao'.
    # O segundo argumento é um valor booleano 'True', que indica que o 
    # texto será renderizado com anti-aliasing, tornando as bordas mais suaves.
    # O terceiro argumento é a cor do texto, que neste caso é definida como 'BRANCO'.
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, BRANCO)

    # A variável 'texto_vidas' armazena o objeto de texto que será 
    # renderizado na tela para mostrar as vidas restantes do jogador.
    # Da mesma forma que a pontuação, a 'fonte.render' é usada para criar a 
    # imagem do texto "Vidas: " seguido do valor atual da variável 'vidas'.
    # Novamente, 'True' para anti-aliasing e 'BRANCO' para a cor do texto.
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, BRANCO)

    # 'tela.blit' é usado para desenhar o objeto de texto 'texto_pontuacao' 
    # na tela na posição (10, 10).
    # Isso coloca o texto da pontuação no canto superior esquerdo da tela.
    tela.blit(texto_pontuacao, (10, 10))

    # 'tela.blit' é usado para desenhar o objeto de texto 'texto_vidas' na tela.
    # 'largura_tela - 100, 10' é a posição onde o texto será colocado, normalmente no
    # canto superior direito, dependendo da largura da tela.
    tela.blit(texto_vidas, (largura_tela - 100, 10))

    # Aqui o personagem é desenhado na tela. 'tela.blit' é usado 
    # para desenhar a imagem do personagem ('personagem')
    # na posição especificada pelo retângulo do personagem ('rect_personagem.x', 'rect_personagem.y').
    # Essas coordenadas determinam onde o personagem aparece na tela.
    tela.blit(personagem, (rect_personagem.x, rect_personagem.y))
    
            
    # Este é um loop 'for' que percorre cada objeto Rect na lista 'plataformas'.
    # Cada 'plat' é um objeto Rect que representa uma plataforma no jogo.
    for plat in plataformas:
        
        # 'pygame.draw.rect' é uma função que desenha um retângulo na superfície especificada.
        # O primeiro argumento 'tela' é a superfície na qual o retângulo será desenhado.
        # 'BRANCO' é a cor definida anteriormente no código que será usada para pintar o retângulo.
        # 'plat' é o objeto Rect que especifica a posição e dimensões da plataforma a ser desenhada.
        pygame.draw.rect(tela, BRANCO, plat)
        
        
    # Este é um loop 'for' que percorre cada inimigo na lista 'inimigos'.
    # Cada item é um tuplo contendo a imagem do inimigo, o objeto Rect associado e um valor descartado ('_').
    for inimigo, inimigo_rect, _ in inimigos:
        
        # 'tela.blit' é uma função que desenha uma imagem na tela.
        # 'inimigo' é a imagem que será desenhada, e 
        # 'inimigo_rect.topleft' é a posição na tela onde a imagem será colocada.
        # O método 'topleft' do objeto Rect retorna as coordenadas da 
        # parte superior esquerda do retângulo, que é onde a imagem do inimigo começará a ser desenhada.
        tela.blit(inimigo, inimigo_rect.topleft)

    # Este é um loop 'for' que percorre cada tiro dos inimigos na lista 'tiros_inimigos'.
    for tiro_rect in tiros_inimigos:
        
        # Da mesma forma que as plataformas, 'pygame.draw.rect' desenha o
        # retângulo que representa o tiro na tela.
        # Neste caso, a cor do tiro é definida como 'AMARELO'.
        pygame.draw.rect(tela, AMARELO, tiro_rect)

    # Este é um loop 'for' que percorre cada tiro do jogador na lista 'tiros_jogador'.
    for tiro_rect in tiros_jogador:
        
        # 'pygame.draw.rect' desenha o retângulo que representa o tiro do jogador na tela.
        # Os tiros do jogador também são desenhados na cor 'AMARELO'.
        pygame.draw.rect(tela, AMARELO, tiro_rect)
            
        
    # 'pygame.display.update()' é uma função que atualiza o conteúdo da tela inteira para o novo frame.
    # Isso fará com que tudo o que foi desenhado nos passos anteriores apareça na tela.
    pygame.display.update()

    # 'pygame.time.delay(30)' pausa o loop por 30 milissegundos.
    # Isso controla a taxa de atualização do jogo, dando-nos aproximadamente 
    # 33 frames por segundo (1000ms / 30ms por frame = ~33fps).
    pygame.time.delay(30)

# Finalmente, 'pygame.quit()' é chamado para encerrar o jogo
# corretamente quando o loop principal termina.
# Isso acontece quando a variável 'rodando' se torna False, geralmente
# como resultado de uma ação do jogador, como fechar a janela do jogo.
pygame.quit()