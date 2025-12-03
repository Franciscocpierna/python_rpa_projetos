# Importa a biblioteca Pygame, que é usada para criar jogos em Python.
import pygame

# Importa a biblioteca sys, que fornece funções e variáveis usadas 
        # para manipular diferentes partes do ambiente de execução do Python.
import sys

# Importa a biblioteca random, que contém funções para gerar números aleatórios.
import random

# Importa a biblioteca os, que fornece uma maneira portátil de usar 
        # funcionalidades dependentes de sistema operacional, como 
        # ler ou escrever arquivos.
import os

# Inicializa o Pygame, o que é necessário para usar qualquer
        # uma das funcionalidades do Pygame.
pygame.init()

# Define variáveis para a largura e a altura da tela do jogo.
LARGURA_TELA = 800
ALTURA_TELA = 600

# Cria a tela do jogo com as dimensões especificadas (largura e altura).
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Define o título da janela do jogo.
pygame.display.set_caption('Space Invaders')

# Carrega a imagem da nave a partir de um arquivo no diretório 'assets', e
        # permite a manipulação de pixels com transparência.
#imagem_nave_original = pygame.image.load(os.path.join('assets', 'nave.png')).convert_alpha()
imagem_nave_original = pygame.image.load(os.path.join('nave.png')).convert_alpha()

# Redimensiona a imagem da nave para as dimensões (50, 40) pixels.
imagem_nave = pygame.transform.scale(imagem_nave_original, (50, 40))

# Carrega e converte a imagem do inimigo, similarmente ao 
        # processo feito com a nave.
imagem_inimigo_original = pygame.image.load(os.path.join('inimigo.png')).convert_alpha()
imagem_inimigo = pygame.transform.scale(imagem_inimigo_original, (40, 30))

# Carrega e converte a imagem do chefe do jogo, também 
        # permitindo transparência.
imagem_chefe_original = pygame.image.load(os.path.join('chefe.png')).convert_alpha()

# Redimensiona a imagem do chefe para as dimensões (200, 100) pixels.
imagem_chefe = pygame.transform.scale(imagem_chefe_original, (200, 100))

# Carrega um arquivo de som de tiro, que será usado quando o
        # jogador ou inimigo atirar.
som_tiro = pygame.mixer.Sound(os.path.join('tiro.mp3'))

# Define uma fonte para a pontuação, usando a fonte 'arial' de tamanho 24.
fonte_pontuacao = pygame.font.SysFont('arial', 24)

# Define uma fonte maior para a mensagem de game over, usando a
        # mesma fonte 'arial' mas com tamanho 48.
fonte_game_over = pygame.font.SysFont('arial', 48)


# Define uma classe chamada Jogador que herda de pygame.sprite.Sprite,
        # que é uma classe base para objetos visuais em jogos feitos com Pygame.
class Jogador(pygame.sprite.Sprite):
    
    # Método construtor que é chamado ao criar uma instância da classe Jogador.
    def __init__(self):
        
        # Chama o método construtor da classe pai (pygame.sprite.Sprite) 
                # para garantir que a inicialização da superclasse aconteça corretamente.
        super().__init__()
        
        # Atribui a imagem carregada anteriormente para a nave ao sprite do jogador.
        self.image = imagem_nave
        
        # Obtem um objeto rect (retângulo) que representa as dimensões da
                # imagem e permite manipular sua posição.
        self.rect = self.image.get_rect()
        
        # Define a posição horizontal do centro do sprite para o meio da tela.
        self.rect.centerx = LARGURA_TELA / 2
        
        # Define a posição vertical do fundo do sprite para 10 pixels
                # acima do fundo da tela.
        self.rect.bottom = ALTURA_TELA - 10
        
        # Inicializa a velocidade horizontal do sprite como 0 (o 
                # sprite está parado horizontalmente no início).
        self.velocidade_x = 0
        
        # Define o número de vidas que o jogador tem no início do jogo.
        self.vidas = 3

    # Método que atualiza o estado do sprite do jogador a cada frame do jogo.
    def update(self):
        
        # Move o sprite horizontalmente de acordo com sua velocidade atual.
        self.rect.x += self.velocidade_x
        
        # Verifica se o sprite está saindo da tela pelo lado esquerdo.
                # Se sim, mantém ele dentro da tela.
        if self.rect.left < 0:
            self.rect.left = 0
        
        # Verifica se o sprite está saindo da tela pelo lado direito. 
        # Se sim, mantém ele dentro da tela.
        if self.rect.right > LARGURA_TELA:
            self.rect.right = LARGURA_TELA

    # Método para o jogador atirar balas.
    def atirar(self):
        
        # Verifica se o número de balas do jogador na tela é menor que 3.
        if len(balas_jogador) < 3:
            
            # Cria uma nova bala na posição central superior do jogador.
            bala = Bala(self.rect.centerx, self.rect.top)
            
            # Adiciona a bala ao grupo de todas as sprites para que ela
                    # seja processada e desenhada.
            todas_as_sprites.add(bala)
            
            # Adiciona a bala ao grupo específico de balas do jogador para
                    # poder gerenciar colisões e outros comportamentos.
            balas_jogador.add(bala)
            
            # Reproduz o som de tiro.
            som_tiro.play()


# Classe Bala herda de pygame.sprite.Sprite para fazer uso das
        # funcionalidades de sprites do Pygame.
class Bala(pygame.sprite.Sprite):
    
    # Método construtor com parâmetros x e y, que são as coordenadas 
            # onde a bala será criada.
    def __init__(self, x, y):
        
        # Chama o construtor da classe base para garantir que o sprite
                # seja inicializado corretamente.
        super().__init__()
        
        # Cria uma superfície de 4 pixels de largura por 10 pixels de
                # altura que será a imagem da bala.
        self.image = pygame.Surface((4, 10))
        
        # Preenche a imagem com a cor vermelha (255, 0, 0) em RGB, 
                # onde 255 é o máximo de vermelho, e 0 para verde e azul.
        self.image.fill((255, 0, 0))
        
        # Obtém o retângulo (rect) que representa as bordas da superfície da bala. 
        # Este retângulo é usado para posicionamento e detecção de colisão.
        self.rect = self.image.get_rect()
        
        # Define a posição horizontal central da bala para a
                # coordenada x passada ao criar a bala.
        self.rect.centerx = x
        
        # Define a posição vertical inferior da bala para a coordenada y
                # passada, fazendo a bala começar de onde o jogador está.
        self.rect.bottom = y
        
        # Define a velocidade vertical da bala como -5, indicando 
                # que a bala se move para cima na tela.
        self.velocidade_y = -5

    # Método update que é chamado a cada frame para atualizar a posição da bala.
    def update(self):
        
        # Atualiza a posição vertical da bala, movendo-a de 
                # acordo com sua velocidade.
        # Como a velocidade_y é -5, a bala se move 5 pixels para
                # cima a cada frame.
        self.rect.y += self.velocidade_y
        
        # Verifica se a parte inferior da bala saiu da parte superior 
                # da tela (posição y menor que 0).
        # Se verdadeiro, o método self.kill() é chamado para remover a
                # bala do grupo de sprites, garantindo que ela não 
                # seja mais processada ou desenhada.
        if self.rect.bottom < 0:
            self.kill()


# Classe BalaInimigo herda de pygame.sprite.Sprite, o que a integra ao 
        # sistema de sprites do Pygame, facilitando gerenciamento 
        # de renderização e colisões.
class BalaInimigo(pygame.sprite.Sprite):
    
    # Método construtor com parâmetros x e y, que determinam a 
            # posição inicial da bala na tela.
    def __init__(self, x, y):
        
        # Inicializa a classe pai (pygame.sprite.Sprite) para garantir
                # que o sprite seja configurado corretamente.
        super().__init__()
        
        # Cria uma superfície retangular para a imagem da bala. As dimensões
                # são 4 pixels de largura por 10 pixels de altura.
        self.image = pygame.Surface((4, 10))
        
        # Preenche a superfície criada com a cor azul (0, 0, 255 em RGB), 
                # diferenciando visualmente das balas do jogador.
        self.image.fill((0, 0, 255))
        
        # Cria um retângulo (rect) que delimita a bala, usado para 
                # detectar colisões e posicionar a bala.
        self.rect = self.image.get_rect()
        
        # Define a posição horizontal central da bala conforme o parâmetro x recebido.
        self.rect.centerx = x
        
        # Define a posição vertical superior da bala conforme o parâmetro y 
                # recebido, que é geralmente a posição do inimigo que dispara a bala.
        self.rect.top = y
        
        # Define a velocidade vertical da bala como 4, o que indica que 
                # ela se move para baixo na tela, em direção ao jogador.
        self.velocidade_y = 4

    # Método update que é chamado a cada frame para 
            # atualizar o estado do sprite.
    def update(self):
        
        # Atualiza a posição vertical da bala, incrementando seu
                # valor y pela velocidade_y. A bala desce na tela a cada frame.
        self.rect.y += self.velocidade_y
        
        # Verifica se a parte superior da bala ultrapassou a altura da tela, 
                # indicando que a bala saiu da área visível.
        if self.rect.top > ALTURA_TELA:
            
            # Chama o método kill para remover a bala do grupo de sprites ao
                    # qual pertence, cessando seu processamento e renderização.
            self.kill()


# Define a classe Inimigo, que herda de pygame.sprite.Sprite. Isso permite 
        # que objetos desta classe utilizem todas as funcionalidades de 
        # manipulação de sprites oferecidas pelo Pygame, incluindo 
        # renderização e detecção de colisões.
class Inimigo(pygame.sprite.Sprite):
    
    # Método construtor com parâmetros x e y, que são as coordenadas 
            # iniciais onde o inimigo será posicionado no jogo.
    def __init__(self, x, y):
    
        # Chama o construtor da classe pai (pygame.sprite.Sprite) para 
                # garantir que a inicialização da superclasse aconteça 
                # corretamente, preparando o sprite para uso.
        super().__init__()
        
        # Atribui a imagem previamente carregada para o inimigo (definida 
                # fora desta classe) ao sprite do inimigo.
        # Esta imagem é a representação visual do inimigo no jogo.
        self.image = imagem_inimigo
        
        # Obtem um objeto rect (retângulo) que representa as
                # dimensões e posição da imagem do inimigo.
        # Este retângulo é fundamental para posicionamento e
                # detecção de colisão no jogo.
        self.rect = self.image.get_rect()
        
        # Define a posição horizontal (x) do retângulo do inimigo. Isso
                # posiciona o inimigo horizontalmente na tela conforme
                # a coordenada x fornecida.
        self.rect.x = x
        
        # Define a posição vertical (y) do retângulo do inimigo. Isso
                # posiciona o inimigo verticalmente na tela
                # conforme a coordenada y fornecida.
        self.rect.y = y
        
        # Inicializa a velocidade horizontal do inimigo. Neste caso, a
                # velocidade é configurada como 1, o que significa que o 
                # inimigo se moverá horizontalmente a uma velocidade
                # constante de 1 pixel por atualização de frame.
        self.velocidade_x = 1


    def update(self):
    
        # Atualiza a posição horizontal do inimigo multiplicando 
                # sua velocidade pela direção.
        # A direção pode ser 1 (movendo para a direita) ou -1 (movendo 
                # para a esquerda), permitindo que o inimigo mude de direção.
        self.rect.x += self.velocidade_x * direcao_inimigos
    
        # Verifica se o inimigo atingiu as bordas da tela. 
        # Se o lado direito do inimigo é maior ou igual à largura da
                # tela ou se o lado esquerdo é menor ou igual a zero,
        # a função `alterar_direcao_inimigos()` é chamada para 
                # mudar a direção de todos os inimigos.
        if self.rect.right >= LARGURA_TELA or self.rect.left <= 0:
            alterar_direcao_inimigos()
    
        # Inimigos atiram de forma aleatória. A função `random.random()`
                # gera um número entre 0 e 1.
        # Se esse número for menor que 0.002, o inimigo atira. 
                # Esta condição limita a frequência de tiros.
        if random.random() < 0.002:
            self.atirar()
    
        # Verifica se o inimigo atingiu o chão, ou seja, se a parte
                # inferior do inimigo é maior ou igual à altura da tela.
        if self.rect.bottom >= ALTURA_TELA:

            # Se verdadeiro, o inimigo é removido do jogo com `self.kill()`.
            self.kill()
            
            # Diminui uma vida do jogador.
            jogador.vidas -= 1
            
            # Se as vidas do jogador chegam a zero, define a variável 
                    # global `jogo_rodando` como False,
                    # o que eventualmente interrompe o loop principal
                    # do jogo, terminando o jogo.
            if jogador.vidas <= 0:
                global jogo_rodando
                jogo_rodando = False


    def atirar(self):
    
        # Cria uma nova bala do tipo 'BalaInimigo'. A bala é posicionada 
                # de modo que seu centro horizontal (centerx) alinhe-se 
                # com o centro horizontal do inimigo.
        # O topo da bala (bottom) é posicionado na parte inferior do
                # inimigo (rect.bottom), fazendo com que a bala 
                # pareça ser disparada de baixo do inimigo.
        bala = BalaInimigo(self.rect.centerx, self.rect.bottom)
    
        # Adiciona a bala recém-criada ao grupo geral de
                # sprites chamado 'todas_as_sprites'.
        # Este grupo é usado para gerenciar a renderização e
                # atualização de todos os sprites no jogo.
        todas_as_sprites.add(bala)
    
        # Adiciona a bala ao grupo específico 'balas_inimigo'. 
        # Este grupo pode ser usado para gerenciar colisões e outros
                # comportamentos específicos das balas disparadas pelos 
                # inimigos, diferenciando-as das balas do jogador.
        balas_inimigo.add(bala)


# Define a classe Chefe, que é uma subclasse de pygame.sprite.Sprite, 
        # facilitando o uso de imagens, detecção de colisão e grupos de sprites.
class Chefe(pygame.sprite.Sprite):
    
    # Método construtor que aceita dois parâmetros opcionais: vidas e 
            # velocidade_x. 
    # Estes parâmetros são usados para configurar a saúde e
            # a velocidade horizontal do chefe.
    def __init__(self, vidas=100, velocidade_x=2):
        
        # Chama o construtor da classe base para garantir a
                # correta inicialização do sprite.
        super().__init__()
        
        # Atribui a imagem previamente carregada do chefe ao sprite.
        # Esta imagem define a aparência do chefe no jogo.
        self.image = imagem_chefe
        
        # Cria um retângulo para o sprite que facilita a manipulação 
                # de sua posição e a detecção de colisão.
        self.rect = self.image.get_rect()
        
        # Centraliza horizontalmente o chefe na tela.
        self.rect.centerx = LARGURA_TELA / 2
        
        # Posiciona o topo do chefe um pouco abaixo do topo
                # da tela (10 pixels abaixo).
        self.rect.top = 10
        
        # Define a velocidade horizontal do chefe usando o parâmetro fornecido.
        self.velocidade_x = velocidade_x
        
        # Define a quantidade de vidas do chefe usando o parâmetro fornecido.
        # Isso determina quantos colisoes ele pode receber antes de ser destruído.
        self.vidas = vidas

    # Método update é chamado a cada frame do jogo para atualizar a
            # posição do chefe e verificar se ele deve atirar.
    def update(self):
        
        # Move o chefe horizontalmente baseado em sua velocidade e direção.
        self.rect.x += self.velocidade_x * direcao_chefe
        
        # Verifica se o chefe atingiu as bordas da tela para alterar sua direção.
        if self.rect.right >= LARGURA_TELA or self.rect.left <= 0:
            
            # Chama função para mudar a direção horizontal do chefe.
            alterar_direcao_chefe()
        
        # Determina aleatoriamente se o chefe vai atirar, 
                # baseado em uma probabilidade de 2%.
        if random.random() < 0.02:
            self.atirar()

    # Método para o chefe atirar.
    def atirar(self):
        
        # Cria uma nova bala inimiga na posição atual do chefe.
        bala = BalaInimigo(self.rect.centerx, self.rect.bottom)
        
        # Adiciona a nova bala ao grupo geral de todas as
                # sprites para ser processada e renderizada.
        todas_as_sprites.add(bala)
        
        # Adiciona a bala ao grupo específico das balas de
                # inimigo para facilitar a gestão de colisões.
        balas_inimigo.add(bala)


# Define uma função chamada 'alterar_direcao_inimigos' 
        # que não recebe parâmetros.
def alterar_direcao_inimigos():
    
    # Declara que a variável 'direcao_inimigos' é global, o que 
            # significa que ela referencia a variável definida fora 
            # da função, no escopo global.
    global direcao_inimigos
    
    # Multiplica a direção atual dos inimigos por -1, o que efetivamente 
            # inverte a direção.
    # Se os inimigos estavam se movendo para a direita (direcao_inimigos = 1), 
            # agora se moverão para a esquerda (direcao_inimigos = -1), e vice-versa.
    direcao_inimigos *= -1
    
    # Itera sobre cada inimigo presente no grupo 'inimigos'.
    for inimigo in inimigos:
        
        # Move cada inimigo verticalmente para baixo em 10 pixels.
        # Este ajuste vertical cada vez que a direção é alterada cria um
                # efeito onde os inimigos descem um pouco mais perto do 
                # jogador cada vez que atingem uma borda da tela.
        inimigo.rect.y += 10


# Define a função que altera a direção horizontal na qual o chefe se move.
def alterar_direcao_chefe():
    
    # Utiliza a palavra-chave 'global' para modificar a variável 'direcao_chefe', 
            # que está definida no escopo global.
    global direcao_chefe
    
    # Multiplica a direção atual do chefe por -1 para inverter sua direção.
    # Isso faz com que se ele estiver se movendo para a direita (direcao_chefe = 1), 
            # passe a se mover para a esquerda (direcao_chefe = -1), e vice-versa.
    direcao_chefe *= -1


# Define uma função para mostrar texto na tela do jogo.
def mostrar_texto(texto, tamanho, cor, x, y):
    
    # Cria uma fonte usando a família 'arial' e o tamanho especificado.
    fonte = pygame.font.SysFont('arial', tamanho)
    
    # Renderiza o texto fornecido na cor especificada. O parâmetro True
            # indica que o texto será renderizado com anti-aliasing, 
            # tornando as bordas do texto mais suaves.
    superficie_texto = fonte.render(texto, True, cor)
    
    # Obtém o retângulo que envolve o texto renderizado. Este retângulo é
            # usado para posicionar o texto na tela.
    rect_texto = superficie_texto.get_rect()
    
    # Define o centro do retângulo de texto nas coordenadas (x, y) fornecidas.
    # Isso centraliza o texto nas coordenadas especificadas, tornando 
            # mais fácil alinhar visualmente na interface do jogo.
    rect_texto.center = (x, y)
    
    # Desenha o texto renderizado na tela. 'blit' é um método que 
            # copia o conteúdo de uma superfície para outra.
    # Neste caso, copia a superfície do texto para a superfície da
            # tela principal do jogo na posição especificada pelo retângulo do texto.
    tela.blit(superficie_texto, rect_texto)


# Define uma função chamada 'criar_inimigos' que aceita dois 
        # parâmetros, 'linhas' e 'colunas', 
        # indicando o número de linhas e colunas de
        # inimigos que serão criados.
def criar_inimigos(linhas, colunas):
    
    # Utiliza um loop 'for' para iterar sobre o número de 
            # linhas especificado.
    for linha in range(linhas):
        
        # Dentro do loop de linhas, usa outro loop 'for' para
                # iterar sobre o número de colunas especificado.
        for coluna in range(colunas):
            
            # Calcula a posição 'x' do inimigo. 'offset_x' é uma 
                    # variável que define o deslocamento horizontal inicial
                    # e 'espacamento_x' é a distância horizontal entre cada
                    # inimigo. A posição x é incrementada para cada coluna.
            x = offset_x + coluna * espacamento_x
            
            # Calcula a posição 'y' do inimigo de maneira similar,
                    # usando 'offset_y' para o deslocamento vertical inicial
                    # e 'espacamento_y' para a distância vertical entre cada 
                    # linha de inimigos. A posição y é incrementada para cada linha.
            y = offset_y + linha * espacamento_y
            
            # Cria uma instância da classe 'Inimigo', passando as
                    # posições 'x' e 'y' calculadas.
            inimigo = Inimigo(x, y)
            
            # Adiciona o inimigo criado ao grupo 'todas_as_sprites', que é
                    # um pygame.sprite.Group. 
            # Isso permite que o inimigo seja automaticamente gerenciado 
                    # pelo Pygame (renderizado e atualizado).
            todas_as_sprites.add(inimigo)
            
            # Adiciona o inimigo ao grupo 'inimigos', que pode ser usado 
                    # para gerenciar especificamente os inimigos,
                    # como para detectar colisões ou implementar lógica
                    # de jogo específica para inimigos.
            inimigos.add(inimigo)



# Cria um grupo de sprites no Pygame que será usado para manter e 
        # gerenciar todos os sprites do jogo (inimigos, jogador, balas, etc.).
todas_as_sprites = pygame.sprite.Group()

# Instancia o jogador usando a classe Jogador definida anteriormente.
jogador = Jogador()

# Adiciona o objeto jogador ao grupo todas_as_sprites para que seja 
        # gerenciado pelo Pygame (atualizado e renderizado automaticamente).
todas_as_sprites.add(jogador)

# Cria um grupo separado apenas para os inimigos. Isso facilita a 
        # gestão de eventos e colisões específicas para inimigos.
inimigos = pygame.sprite.Group()

# Define o número de linhas e colunas de inimigos que 
        # serão criados na tela.
linhas_inimigos = 5
colunas_inimigos = 10

# Define a direção inicial de movimento dos inimigos. '1' significa 
        # que começarão se movendo para a direita.
direcao_inimigos = 1

# Define o espaço entre cada inimigo horizontalmente e verticalmente.
espacamento_x = 60
espacamento_y = 50

# Define os deslocamentos iniciais horizontal e vertical para 
        # onde o primeiro inimigo será colocado.
offset_x = 80
offset_y = 50

# Chama a função para criar inimigos nas posições definidas
        # pelas variáveis de linha, coluna, espaçamento e offset.
criar_inimigos(linhas_inimigos, colunas_inimigos)

# Cria grupos de sprites separados para as balas disparadas 
        # pelo jogador e pelos inimigos.
balas_jogador = pygame.sprite.Group()
balas_inimigo = pygame.sprite.Group()

# Define a variável chefe como None inicialmente, indicando 
        # que o chefe ainda não está presente no jogo.
chefe = None

# Define a direção inicial de movimento do chefe, similar 
        # ao dos inimigos comuns.
direcao_chefe = 1

# Variáveis do Jogo
# Define a pontuação inicial do jogador como 0.
pontuacao = 0

# Variável de controle para manter o jogo rodando. 
        # Se for False, o jogo termina.
jogo_rodando = True

# Cria um relógio para controlar a taxa de atualização do jogo, 
        # garantindo um jogo suave e consistente.
relogio = pygame.time.Clock()

# Define uma variável para rastrear a fase atual de inimigos no jogo.
fase = 1


# Este loop continua executando enquanto a variável 'jogo_rodando' for True.
while jogo_rodando:
    
    # Limita a taxa de frames do jogo a 60 frames por segundo para
            # garantir jogabilidade suave e consistente.
    relogio.tick(60)

    # Processa todos os eventos que aconteceram desde a última vez 
            # que este loop foi executado.
    for evento in pygame.event.get():
        
        # Verifica se o evento é do tipo QUIT, que ocorre geralmente
                # quando o jogador fecha a janela do jogo.
        if evento.type == pygame.QUIT:
            
            # Define 'jogo_rodando' como False para terminar o loop e encerrar o jogo.
            jogo_rodando = False
            
        # Verifica se uma tecla foi pressionada.
        elif evento.type == pygame.KEYDOWN:
            
            # Se a tecla pressionada for a seta para esquerda, ajusta a
                    # velocidade horizontal do jogador para -5 (movendo para esquerda).
            if evento.key == pygame.K_LEFT:
            
                jogador.velocidade_x = -5
            
            # Se a tecla pressionada for a seta para direita, ajusta a
                    # velocidade horizontal do jogador para 5 (movendo para direita).
            elif evento.key == pygame.K_RIGHT:
                
                jogador.velocidade_x = 5
                
            # Se a tecla pressionada for a barra de espaço, o jogador
                    # executa a ação de atirar.
            elif evento.key == pygame.K_SPACE:
                
                jogador.atirar()
                
        # Verifica se uma tecla foi solta.
        elif evento.type == pygame.KEYUP:
            
            # Se a tecla solta for a seta para esquerda e a velocidade
                    # horizontal do jogador for negativa, 
                    # zera a velocidade horizontal, parando o movimento para a esquerda.
            if evento.key == pygame.K_LEFT and jogador.velocidade_x < 0:
                
                jogador.velocidade_x = 0
                
            # Se a tecla solta for a seta para direita e a velocidade
                    # horizontal do jogador for positiva, 
                    # zera a velocidade horizontal, parando o movimento para a direita.
            elif evento.key == pygame.K_RIGHT and jogador.velocidade_x > 0:
                
                jogador.velocidade_x = 0


    # Atualiza todas as sprites gerenciadas pelo grupo 'todas_as_sprites'. 
    # Isso inclui jogadores, inimigos, balas e qualquer outro
            # sprite adicionado ao grupo. 
    # O método 'update' de cada sprite individual é chamado automaticamente.
    todas_as_sprites.update()
    
    # Detecta colisões entre dois grupos: inimigos e balas do jogador.
    # O primeiro argumento 'True' faz com que os inimigos que 
            # colidiram sejam automaticamente removidos do grupo,
            # o segundo 'True' faz o mesmo com as balas que colidiram.
    colisoes = pygame.sprite.groupcollide(inimigos, balas_jogador, True, True)
    
    # Para cada inimigo atingido (cada item em 'colisoes'), 
            # adiciona 10 pontos à pontuação do jogador.
    for colisao in colisoes:
        pontuacao += 10
    
    # Detecta colisões entre o jogador e as balas dos inimigos.
    # O jogador é representado pelo sprite 'jogador', e 'balas_inimigo' é 
            # o grupo contendo as balas disparadas pelos inimigos.
    # 'True' como terceiro argumento especifica que as balas que 
            # colidirem com o jogador devem ser removidas do grupo.
    colisoes = pygame.sprite.spritecollide(jogador, balas_inimigo, True)
    
    # Se houve colisão, isto é, se 'colisoes' não está vazio.
    if colisoes:
        
        # Reduz uma vida do jogador por cada bala que o atingiu.
        jogador.vidas -= 1
        
        # Verifica se as vidas do jogador chegaram a zero.
        if jogador.vidas <= 0:
            
            # Se sim, define 'jogo_rodando' como False, terminando o
                    # loop principal e, consequentemente, o jogo.
            jogo_rodando = False


    # Detecta colisões entre o jogador (sprite individual) e os
            # inimigos (grupo de sprites).
    # O primeiro argumento é o sprite do jogador, o segundo é o grupo 
            # de inimigos, e 'True' especifica que os inimigos que
            # colidirem devem ser removidos.
    colisoes = pygame.sprite.spritecollide(jogador, inimigos, True)
    
    # Verifica se houve alguma colisão detectada, ou seja, se a 
            # lista 'colisoes' não está vazia.
    if colisoes:
        
        # Diminui uma vida do jogador para cada colisão detectada.
        jogador.vidas -= 1
        
        # Verifica se as vidas do jogador esgotaram.
        if jogador.vidas <= 0:
            
            # Se sim, o jogo é encerrado definindo a variável 'jogo_rodando' como False.
            jogo_rodando = False
    
    # Verifica se todos os inimigos foram destruídos e se o chefe
            # ainda não está presente no jogo.
    if not inimigos and not chefe:
        
        # Cria uma instância do Chefe com vidas incrementadas por cada
                # fase passada e uma velocidade que também aumenta com as fases.
        chefe = Chefe(vidas=100 + (fase - 1) * 50, velocidade_x=2 + (fase - 1))
        
        # Adiciona o chefe ao grupo geral de sprites para que seja
                # gerenciado pelo Pygame (renderizado e atualizado).
        todas_as_sprites.add(chefe)


    # Verifica se o chefe está atualmente ativo no jogo
            # antes de verificar colisões.
    if chefe:
        
        # Detecta colisões entre o chefe e as balas do jogador.
        # A função spritecollide verifica se o sprite 'chefe' colidiu
                # com algum sprite no grupo 'balas_jogador'.
        # O argumento True indica que as balas do jogador que
                # colidirem com o chefe serão removidas do jogo.
        colisoes = pygame.sprite.spritecollide(chefe, balas_jogador, True)
    
        # Itera sobre cada colisão encontrada entre o chefe e as balas do jogador.
        for colisao in colisoes:
            
            # Diminui em 1 a vida do chefe para cada bala que o atinge.
            chefe.vidas -= 1
    
            # Verifica se as vidas do chefe são reduzidas a zero ou menos.
            if chefe.vidas <= 0:
                
                # Se as vidas do chefe acabarem, o sprite do chefe é 
                        # removido do jogo usando o método kill.
                chefe.kill()
    
                # Define o objeto chefe como None, indicando que não há 
                        # atualmente um chefe no jogo.
                chefe = None
    
                # Aumenta a pontuação do jogador em 100 pontos por derrotar o chefe.
                pontuacao += 100
    
                # Incrementa a variável 'fase', que rastreia o número de fases de 
                        # inimigos enfrentadas pelo jogador.
                fase += 1
    
                # Calcula o número de linhas de inimigos para a próxima fase.
                # A fórmula '5 + fase - 1' aumenta o número de linhas à medida que o 
                        # jogo avança (cada nova fase aumenta o número base de linhas).
                # Por exemplo, na primeira fase (fase = 1), o cálculo 
                        # seria 5 + 1 - 1 = 5 linhas de inimigos.
                # A função 'min' é usada para garantir que o número de linhas 
                        # não exceda o máximo estabelecido de 8.
                # Isso significa que, independentemente de quantas fases o 
                        # jogador avance, o número máximo de linhas será sempre 8.
                linhas_inimigos = min(5 + fase - 1, 8)
                
                # Calcula o número de colunas de inimigos para a próxima fase.
                # A fórmula '10 + (fase - 1) * 2' aumenta o número de colunas 
                        # adicionando 2 para cada fase subsequente.
                # Por exemplo, na primeira fase (fase = 1), o cálculo 
                        # seria 10 + (1 - 1) * 2 = 10 colunas de inimigos.
                # Na segunda fase (fase = 2), seria 10 + (2 - 1) * 2 = 12 
                        # colunas, e assim por diante.
                # A função 'min' novamente assegura que o número de colunas não 
                        # ultrapasse o limite máximo de 16.
                # Isso limita o layout dos inimigos para garantir que o jogo 
                        # permaneça jogável e os inimigos não sejam posicionados fora da tela.
                colunas_inimigos = min(10 + (fase - 1) * 2, 16)

    
                # Chama a função para criar uma nova fase de inimigos com os 
                        # valores atualizados de linhas e colunas.
                criar_inimigos(linhas_inimigos, colunas_inimigos)
    
                # Inicia um loop que percorre cada inimigo presente no grupo 'inimigos'.
                # Este grupo contém todos os inimigos atualmente ativos no jogo.
                for inimigo in inimigos:
                    
                    # Aumenta a velocidade horizontal (velocidade_x) de cada inimigo.
                    # O aumento é calculado como 0.2 vezes o número da
                            # fase atual menos um.
                    # Essa fórmula significa que na primeira fase (fase = 1), o 
                            # aumento será 0.2 * (1 - 1) = 0, ou seja, não há 
                            # aumento na primeira fase.
                    # Na segunda fase (fase = 2), o aumento será 0.2 * (2 - 1) = 0.2 unidades.
                    # Isso faz com que os inimigos se movam mais rapidamente à 
                            # medida que o jogador progride nas fases, adicionando um
                            # elemento de dificuldade crescente ao jogo.
                    inimigo.velocidade_x += 0.2 * (fase - 1)



    # Preenche toda a tela com a cor preta. Isso limpa a tela antes de 
            # desenhar o novo frame, removendo traços do frame anterior.
    # As cores são definidas em RGB, e (0, 0, 0) representa preto.
    tela.fill((0, 0, 0))
    
    # Desenha todos os sprites gerenciados pelo
            # grupo 'todas_as_sprites' na tela.
    # Isso inclui o jogador, inimigos, balas e quaisquer
            # outros sprites que foram adicionados ao grupo.
    todas_as_sprites.draw(tela)
    
    # Chama a função 'mostrar_texto' para desenhar na tela a 
            # pontuação atual do jogador.
    # 'Pontuação: {pontuacao}' forma uma string que inclui o 
            # valor atual da variável 'pontuacao'.
    # O tamanho da fonte é 24, a cor é branco (255, 255, 255 em RGB), e
            # a posição x é 70 e y é 20 pixels da borda superior esquerda.
    mostrar_texto(f'Pontuação: {pontuacao}', 24, (255, 255, 255), 70, 20)
    
    # Similarmente, desenha na tela a quantidade de vidas
            # restantes do jogador.
    # A posição x é ajustada para estar 70 pixels à esquerda da
            # borda direita da tela, utilizando 'LARGURA_TELA - 70'.
    mostrar_texto(f'Vidas: {jogador.vidas}', 24, (255, 255, 255), LARGURA_TELA - 70, 20)
    
    # Desenha na tela o número da fase atual do jogo.
    # A posição x é centrada na tela usando 'LARGURA_TELA / 2', e 
            # a posição y é 20, igual às outras informações.
    mostrar_texto(f'Fase: {fase}', 24, (255, 255, 255), LARGURA_TELA / 2, 20)
    
    # Atualiza a tela para mostrar tudo que foi desenhado. Esta 
            # função é essencial para tornar visíveis todas
            # as alterações visuais feitas.
    pygame.display.flip()


# Limpa a tela preenchendo-a com preto para preparar a tela 
        # para a exibição da mensagem de Game Over.
# Utiliza a cor preta (0, 0, 0 em RGB) para garantir
        # que o texto se destaque.
tela.fill((0, 0, 0))

# Define a mensagem de Game Over que será mostrada ao jogador.
mensagem = 'Você perdeu! Game Over'

# Chama a função 'mostrar_texto' para desenhar a mensagem
        # de Game Over na tela.
# O texto é configurado para ser grande e visível, com tamanho
        # de fonte 48 e cor branca (255, 255, 255 em RGB).
# O texto é centralizado na tela, usando metade da largura 
        # da tela (LARGURA_TELA / 2) e metade da altura da 
        # tela (ALTURA_TELA / 2) como coordenadas.
mostrar_texto(mensagem, 48, (255, 255, 255), LARGURA_TELA / 2, ALTURA_TELA / 2)

# Atualiza a tela para mostrar a mensagem de Game Over.
pygame.display.flip()

# Pausa o jogo por 5000 milissegundos (5 segundos), dando
        # tempo ao jogador para ler a mensagem de Game Over.
pygame.time.wait(5000)

# Fecha a janela do jogo e finaliza a biblioteca Pygame, 
        # liberando os recursos que foram utilizados.
pygame.quit()

# Encerra o script Python, garantindo que não haja processos
        # pendentes ou janelas abertas após o término do jogo.
sys.exit()