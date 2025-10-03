# Importa o módulo pygame, que é uma biblioteca usada 
# para criar jogos e interfaces gráficas.
import pygame

# Importa o módulo random, que fornece funções para gerar números aleatórios.
import random

# Importa o módulo sys, que fornece acesso a algumas variáveis
# e funções que interagem fortemente com o interpretador Python.
import sys

# Inicializa todos os módulos importados do pygame. É necessário 
# para preparar a infraestrutura do Pygame antes de usar qualquer 
# outra funcionalidade dele.
pygame.init()

# Define a largura da janela do jogo em pixels. É uma variável
# que armazena o valor da largura da janela do jogo.
largura_tela = 800

# Define a altura da janela do jogo em pixels. É uma variável 
# que armazena o valor da altura da janela do jogo.
altura_tela = 600

# Cria uma janela ou tela para o jogo com as dimensões especificadas
# pelas variáveis largura_tela e altura_tela.
# set_mode() é uma função do Pygame que inicializa uma janela ou tela para exibição.
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Define o título da janela do jogo. A função set_caption() é usada para
# definir o título da janela.
# "Jogo de Carrinho" é o título que aparecerá na barra de título da janela do jogo.
pygame.display.set_caption("Jogo de Carrinho")


# Define a largura do carro do jogador em pixels. 
# É uma variável que armazena o valor da largura do sprite do carro
# que será usado para o jogador.
largura_carro = 60

# Define a altura do carro do jogador em pixels. 
# Semelhante à largura_carro, armazena o valor da altura do sprite do carro do jogador.
altura_carro = 120  

# Define a velocidade de movimento dos carros inimigos na tela. 
# É uma variável que controla a rapidez com que os carros inimigos se 
# movem verticalmente na tela.
velocidade_carro = 5

# Define a velocidade de mudança das imagens de fundo para criar um efeito de movimento. 
# Um valor menor faz com que o fundo se mova mais lentamente, dando uma 
# sensação de profundidade.
velocidade_fundo = 0.1  

# Define o número de pistas no jogo. 
# Esta variável é usada para calcular a largura de cada pista e posicionar
# os carros inimigos.
num_pistas = 4

# Calcula a largura de cada pista dividindo a largura total da tela pelo número de pistas.
# Usa a divisão inteira para garantir que o valor seja um inteiro.
largura_pista = largura_tela // num_pistas

# Define o limite esquerdo da área de movimento do carro do jogador. 
# O carro não pode se mover para a esquerda além deste ponto.
limite_esquerda = 110

# Define o limite direito da área de movimento do carro do jogador. 
# Calcula-se subtraindo a margem direita e a largura do carro da largura total da tela.
# O carro não pode se mover para a direita além deste ponto.
limite_direita = largura_tela - 10 - largura_carro

# Define a velocidade de movimento do carro do jogador. 
# É a velocidade com que o carro do jogador se move em resposta às entradas do usuário.
velocidade_jogador = 15

# Inicia pontuação com 0
pontuacao = 0


# Carrega a imagem do carro do jogador do arquivo "jogador.png".
# A função load() é usada para carregar uma imagem de um arquivo.
imagem_carro = pygame.image.load("car.png")

# Redimensiona a imagem do carro do jogador para as dimensões definidas
# por largura_carro e altura_carro.
# A função scale() redimensiona uma superfície para um novo tamanho.
imagem_carro = pygame.transform.scale(imagem_carro, (largura_carro, altura_carro))

# Carrega e armazena uma lista de imagens de fundo a partir de arquivos.
# Cada elemento da lista é uma imagem de fundo diferente para o jogo.
imagens_fundo = [pygame.image.load("background1.png"),
                 pygame.image.load("background2.png"),
                 pygame.image.load("background3.png"),
                 pygame.image.load("background4.png")]


# Este loop percorre a lista de imagens de fundo.
# 'len(imagens_fundo)' retorna o número de imagens na lista.
# 'range(len(imagens_fundo))' gera uma sequência de números de 0 até 
# o número de imagens - 1.
for i in range(len(imagens_fundo)):
    
    # Redimensiona cada imagem de fundo na lista para as dimensões da tela.
    # 'imagens_fundo[i]' acessa a i-ésima imagem na lista.
    # 'pygame.transform.scale()' redimensiona a imagem para as dimensões especificadas.
    # '(largura_tela, altura_tela)' são as novas dimensões para as imagens de fundo.
    imagens_fundo[i] = pygame.transform.scale(imagens_fundo[i], (largura_tela, altura_tela))
    
    
# Define a largura dos carros inimigos em pixels. 
# Armazena o valor da largura dos sprites dos carros inimigos.
largura_carro_inimigo = 60  

# Define a altura dos carros inimigos em pixels.
# Armazena o valor da altura dos sprites dos carros inimigos.
altura_carro_inimigo = 120  

# Carrega a imagem do primeiro carro inimigo do arquivo "carro1.png".
carro1 = pygame.image.load("carro1.png")

# Redimensiona a imagem do primeiro carro inimigo para as dimensões
# definidas por largura_carro_inimigo e altura_carro_inimigo.
carro1 = pygame.transform.scale(carro1, (largura_carro_inimigo, altura_carro_inimigo))

# Carrega a imagem do segundo carro inimigo do arquivo "carro2.png".
carro2 = pygame.image.load("carro2.png")

# Redimensiona a imagem do segundo carro inimigo. 
# Aqui, a largura do carro é especificada como 120 pixels, 
# diferente da largura_carro_inimigo.
carro2 = pygame.transform.scale(carro2, (120, altura_carro_inimigo))

# Carrega a imagem do terceiro carro inimigo do arquivo "carro3.png".
carro3 = pygame.image.load("carro3.png")

# Redimensiona a imagem do terceiro carro inimigo para a mesma largura do 
# segundo carro, mas mantendo a mesma altura dos outros carros inimigos.
carro3 = pygame.transform.scale(carro3, (120, altura_carro_inimigo))

# Carrega a imagem do quarto carro inimigo do arquivo "carro4.png".
carro4 = pygame.image.load("carro4.png")

# Redimensiona a imagem do quarto carro inimigo para as dimensões
# definidas por largura_carro_inimigo e altura_carro_inimigo.
carro4 = pygame.transform.scale(carro4, (largura_carro_inimigo, altura_carro_inimigo))


# Classe para o carro do jogador
# Definição da classe CarroJogador
class CarroJogador:
    
    # Método construtor da classe. É chamado automaticamente quando uma instância da classe é criada.
    def __init__(self):
        
        # Atribui à variável 'self.imagem' a imagem do carro do jogador carregada anteriormente.
        self.imagem = imagem_carro

        # Cria um retângulo (objeto Rect) a partir da imagem do carro. 
        # Este retângulo é usado para posicionar a imagem na tela e para detecção de colisões.
        self.retangulo = self.imagem.get_rect()

        # Define a posição horizontal do centro do retângulo para ser o centro da tela.
        # 'largura_tela // 2' calcula o ponto central horizontal da tela.
        self.retangulo.centerx = largura_tela // 2

        # Define a posição vertical do fundo do retângulo para ser um pouco acima do fundo da tela.
        # 'altura_tela - 20' posiciona o carro um pouco acima do limite inferior da tela.
        self.retangulo.bottom = altura_tela - 20

    # Método para mover o carro do jogador.
    # 'direcao' é um parâmetro que indica para onde o carro deve se mover.
    def mover(self, direcao):
        
        # Se a direção for esquerda e o carro não tiver atingido o limite esquerdo, 
        # move o carro para a esquerda.
        if direcao == "esquerda" and self.retangulo.left > limite_esquerda:
            self.retangulo.x -= velocidade_jogador

        # Se a direção for direita e o carro não tiver atingido o limite direito, 
        # move o carro para a direita.
        elif direcao == "direita" and self.retangulo.right < limite_direita:
            self.retangulo.x += velocidade_jogador

        # Se a direção for cima e o carro não estiver na parte superior da tela, 
        # move o carro para cima.
        elif direcao == "cima" and self.retangulo.top > 0:
            self.retangulo.y -= velocidade_jogador

        # Se a direção for baixo e o carro não estiver na parte inferior da tela, 
        # move o carro para baixo.
        elif direcao == "baixo" and self.retangulo.bottom < altura_tela:
            self.retangulo.y += velocidade_jogador

    # Método para desenhar o carro do jogador na tela.
    def desenhar(self):
        
        # Desenha a imagem do carro na tela na posição
        # definida pelo retângulo.
        # 'tela.blit()' é usado para desenhar uma superfície
        # (neste caso, a imagem do carro) em outra superfície (a tela).
        tela.blit(self.imagem, self.retangulo)


# Definição da classe CarroInimigo.
class CarroInimigo:
    
    # Método construtor da classe, chamado ao criar uma instância da classe.
    # 'pista' é o parâmetro que indica em qual pista o carro inimigo aparecerá.
    def __init__(self, pista):
        
        # Escolhe aleatoriamente uma imagem para o carro inimigo de uma lista de imagens.
        # 'random.choice()' seleciona um elemento aleatório de uma lista.
        self.imagem = random.choice([carro1, carro2, carro3, carro4])

        # Cria um retângulo (objeto Rect) a partir da imagem do carro inimigo.
        # Este retângulo é usado para posicionar a imagem na tela e para detecção de colisões.
        self.retangulo = self.imagem.get_rect()

        # Posiciona o centro horizontal do retângulo com base na pista dada.
        # 'pista * largura_pista' calcula o início da pista.
        # '(largura_pista // 2)' calcula o ponto central da pista.
        # Os valores adicionados (70, 60, 40) são ajustes para posicionar corretamente o carro na pista.
        if pista == 0:
            self.retangulo.centerx = pista * largura_pista + (largura_pista // 2) + 70
        elif pista == 1:
            self.retangulo.centerx = pista * largura_pista + (largura_pista // 2) + 60
        elif pista == 2:
            self.retangulo.centerx = pista * largura_pista + (largura_pista // 2) + 40
        else:  # Para qualquer outra pista
            self.retangulo.centerx = pista * largura_pista + largura_pista // 2

        # Define a posição vertical inicial do carro inimigo fora da tela.
        # 'random.randint(-200, -100)' gera um número aleatório entre -200 e -100.
        # Isso faz com que o carro inimigo comece em uma posição acima da área visível da tela.
        self.retangulo.y = random.randint(-200, -100)
        
    # Método para mover o carro inimigo.
    def mover(self):
        
        # Incrementa a posição vertical do retângulo pelo valor da 'velocidade_carro'.
        # Isso faz com que o carro inimigo se mova para baixo na tela.
        self.retangulo.y += velocidade_carro

    # Método para desenhar o carro inimigo na tela.
    def desenhar(self):
        
        # Desenha a imagem do carro inimigo na tela na posição definida pelo retângulo.
        # 'tela.blit()' é usado para desenhar uma superfície (a imagem do 
        # carro) em outra superfície (a tela).
        tela.blit(self.imagem, self.retangulo)
        
        
        
# Inicialização do jogador e carros inimigos

# Cria uma instância da classe CarroJogador chamada 'jogador'.
# Isso inicializa o carro do jogador com as propriedades definidas na classe CarroJogador.
jogador = CarroJogador()

# Cria uma lista vazia chamada 'inimigos' para armazenar os objetos CarroInimigo que serão gerados.
# Esta lista será usada para manter o controle de todos os carros inimigos no jogo.
inimigos = []

# Definição da função gerar_inimigos.
# Esta função é responsável por criar novos carros inimigos e adicioná-los à lista 'inimigos'.
def gerar_inimigos():
    
    # Escolhe um número aleatório de pistas, entre 1 e 3, e seleciona aleatoriamente essas pistas.
    # 'range(num_pistas)' cria uma sequência de números que representa cada pista.
    # 'random.sample()' seleciona aleatoriamente um subconjunto das pistas.
    pistas = random.sample(range(num_pistas), random.randint(1, 3))

    # Percorre cada pista selecionada.
    for pista in pistas:
        
        # Cria um novo objeto CarroInimigo para a pista atual.
        # Passa 'pista' como argumento para o construtor de CarroInimigo.
        inimigo = CarroInimigo(pista)

        # Adiciona o objeto CarroInimigo recém-criado à lista 'inimigos'.
        # Isso permite que o jogo rastreie e gerencie todos os carros inimigos.
        inimigos.append(inimigo)
        
        

# Função para verificar colisões entre o carro do jogador e os carros inimigos.
def verificar_colisoes():
    
    # Itera sobre cada carro inimigo na lista 'inimigos'.
    for inimigo in inimigos:
        
        # Verifica se o retângulo do jogador colide com o retângulo do inimigo.
        # 'jogador.retangulo.colliderect()' verifica se dois retângulos se sobrepõem.
        # Se houver uma colisão, a função retorna True, indicando que o jogo deve terminar.
        if jogador.retangulo.colliderect(inimigo.retangulo):
            return True
        
    # Se o loop terminar sem encontrar nenhuma colisão, retorna False.
    # Isso indica que o jogo pode continuar.
    return False


# Definição da função 'renderizar_pontuacao'.
# Esta função é responsável por desenhar o texto da pontuação na tela do jogo.
# 'pontuacao' é o parâmetro que recebe o valor atual da pontuação do jogador.
def renderizar_pontuacao(pontuacao):
    
    # Cria um objeto de texto (Surface) com a pontuação atual.
    # 'fonte.render()' é usado para criar um objeto de texto.
    # O primeiro argumento é o texto a ser renderizado.
    # 'True' habilita o anti-aliasing do texto, tornando-o mais suave.
    # '(255, 255, 255)' define a cor do texto em RGB, que neste caso é branco.
    texto = fonte.render(f'Pontuação: {pontuacao}', True, (255, 255, 255))

    # Desenha o texto na tela.
    # 'tela.blit()' é usado para desenhar uma superfície (texto) em outra superfície (tela).
    # '(10, 10)' são as coordenadas (x, y) na tela onde o texto será desenhado.
    tela.blit(texto, (10, 10))
        
        
# Loop principal do jogo

# Variável de controle para manter o jogo em execução.
# Enquanto 'executando' for True, o loop do jogo continuará rodando.
executando = True

# Variável para controlar qual imagem de fundo será exibida.
# É usada para criar um efeito de movimento no fundo do jogo.
indice_fundo = 0

# Cria um objeto Clock para controlar a taxa de atualização do jogo.
# 'pygame.time.Clock()' é usado para garantir que o jogo seja
# executado na mesma velocidade em diferentes máquinas.
relogio = pygame.time.Clock()

# Variável para controlar a geração de carros inimigos.
# Será incrementada a cada iteração do loop e usada para determinar
# quando gerar novos inimigos.
temporizador_geracao = 0

# Define a fonte e o tamanho do texto
fonte = pygame.font.Font(None, 36)


# Loop principal do jogo. Este loop é executado enquanto 'executando' for True.
while executando:
    
    # Itera sobre todos os eventos que ocorreram.
    # 'pygame.event.get()' retorna uma lista de todos os eventos que 
    # ocorreram desde a última vez que foi chamado.
    for evento in pygame.event.get():
        
        # Verifica se o tipo do evento é QUIT, que é acionado 
        # quando a janela do jogo é fechada.
        if evento.type == pygame.QUIT:
            
            # Se o evento for QUIT, altera a variável 'executando' para False.
            # Isso fará com que o loop principal do jogo pare de executar.
            executando = False

    # Captura o estado atual de todas as teclas do teclado.
    # 'pygame.key.get_pressed()' retorna uma lista representando 
    # o estado de cada tecla.
    teclas = pygame.key.get_pressed()

    # Verifica se a tecla esquerda está pressionada.
    # 'pygame.K_LEFT' representa a tecla de seta para a esquerda no teclado.
    # Se a tecla esquerda estiver pressionada, move o carro do jogador para a esquerda.
    if teclas[pygame.K_LEFT]:
        jogador.mover("esquerda")

    # Verifica se a tecla direita está pressionada.
    # 'pygame.K_RIGHT' representa a tecla de seta para a direita no teclado.
    # Se a tecla direita estiver pressionada, move o carro do jogador para a direita.
    if teclas[pygame.K_RIGHT]:
        jogador.mover("direita")

    # Verifica se a tecla para cima está pressionada.
    # 'pygame.K_UP' representa a tecla de seta para cima no teclado.
    # Se a tecla para cima estiver pressionada, move o carro do jogador para cima.
    if teclas[pygame.K_UP]:
        jogador.mover("cima")

    # Verifica se a tecla para baixo está pressionada.
    # 'pygame.K_DOWN' representa a tecla de seta para baixo no teclado.
    # Se a tecla para baixo estiver pressionada, move o carro do jogador para baixo.
    if teclas[pygame.K_DOWN]:
        jogador.mover("baixo")
   
    
    # Atualizar a posição do carro do jogador

    # Atualização do fundo em movimento
    # Incrementa 'indice_fundo' pela 'velocidade_fundo'.
    # Isso muda qual imagem de fundo será exibida para criar um efeito de movimento.
    indice_fundo = (indice_fundo + velocidade_fundo) % len(imagens_fundo)

    # Desenha a imagem de fundo atual na tela.
    # 'int(indice_fundo)' é usado para obter o índice inteiro da imagem de fundo.
    # '(0, 0)' é a posição na tela onde a imagem de fundo será desenhada.
    tela.blit(imagens_fundo[int(indice_fundo)], (0, 0))

    # Geração de novos carros inimigos
    # Incrementa 'temporizador_geracao' a cada iteração do loop.
    temporizador_geracao += 1

    # Verifica se 'temporizador_geracao' alcançou 100.
    # Este valor controla a frequência com que novos carros inimigos são gerados.
    if temporizador_geracao == 100:
        
        # Chama a função 'gerar_inimigos' para criar novos carros inimigos.
        gerar_inimigos()

        # Reinicia o temporizador para começar a contagem
        # para a próxima geração de inimigos.
        temporizador_geracao = 0

    # Movimentação e renderização dos carros inimigos
    # Itera sobre cada carro inimigo na lista 'inimigos'.
    for inimigo in inimigos:
        
        # Chama o método 'mover' para atualizar a 
        # posição do carro inimigo.
        inimigo.mover()

        # Chama o método 'desenhar' para renderizar o 
        # carro inimigo na tela.
        inimigo.desenhar()
        
        
    # Itera sobre uma cópia da lista de carros inimigos.
    # A cópia é necessária porque estamos modificando a 
    # lista 'inimigos' durante a iteração.
    # Modificar uma lista enquanto a iteramos pode causar erros
    # ou comportamentos inesperados.
    for inimigo in inimigos.copy():
        
        # Chama o método 'mover' do carro inimigo, atualizando
        # sua posição na tela.
        inimigo.mover()

        # Verifica se o carro inimigo saiu da tela (ou seja, se 
        # moveu além do limite inferior da tela).
        # 'inimigo.retangulo.top > altura_tela' verifica se a parte
        # superior do carro está abaixo do limite inferior da tela.
        if inimigo.retangulo.top > altura_tela:
            
            # Remove o carro inimigo da lista 'inimigos'.
            # Isso é feito porque o carro não é mais visível na 
            # tela e não precisa ser processado.
            inimigos.remove(inimigo)

            # Incrementa a pontuação do jogador.
            # Cada vez que um carro inimigo sai da tela, o jogador ganha um ponto.
            # Isso serve como uma recompensa por evitar colisões com os carros inimigos.
            pontuacao += 1



    # Verificação de colisões
    # Chama a função 'verificar_colisoes'.
    # Se houver uma colisão, 'executando' é definido como False, 
    # encerrando o loop do jogo.
    if verificar_colisoes():
        executando = False

    # Renderização do carro do jogador
    # Chama o método 'desenhar' do objeto 'jogador' para
    # renderizar o carro do jogador na tela.
    jogador.desenhar()
    
    # Chame a função para renderizar a pontuação
    renderizar_pontuacao(pontuacao)
        
        
        
    # Atualiza a tela inteira
    # 'pygame.display.update()' atualiza a tela
    # inteira com tudo que foi desenhado desde a última atualização.
    pygame.display.update()

    # Controla a taxa de quadros por segundo (FPS)
    # 'relogio.tick(60)' garante que o jogo não execute
    # a mais de 60 quadros por segundo.
    relogio.tick(60)


# Encerra todos os módulos do Pygame.
# 'pygame.quit()' é usado para desligar corretamente a biblioteca Pygame.
# Isso é importante para liberar recursos e evitar problemas 
# quando o programa é fechado.
pygame.quit()

# Sai do programa.
# 'sys.exit()' é uma maneira de encerrar o programa Python.
# Isso informa ao ambiente de execução do Python que o 
# programa está pronto para terminar.
sys.exit()
        
        