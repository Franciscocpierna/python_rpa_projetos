# Importa o módulo 'pygame' para desenvolver jogos e
        # interfaces gráficas em Python.
import pygame

# Importa o módulo 'sys' que provê acesso a algumas variáveis e 
        # funções que interagem com o interpretador Python.
import sys

# Importa o módulo 'random' que contém funções para geração 
        # de números aleatórios.
import random

# Importa o módulo 'os' que fornece uma forma portável de usar 
        # funcionalidades dependentes do sistema operacional.
import os

# A função 'pygame.init()' inicializa todos os módulos incluídos no 
        # pygame, preparando a biblioteca para seu uso.
pygame.init()

# Define as dimensões da janela do jogo em pixels. Aqui, definimos as
        # dimensões comuns para um jogo estilo Pac-Man.
LARGURA, ALTURA = 448, 496

# 'pygame.display.set_mode()' configura a janela do display e retorna
        # uma superfície que representa a janela visível.
# A variável 'tela' agora representa essa superfície.
tela = pygame.display.set_mode((LARGURA, ALTURA))

# 'pygame.display.set_caption()' define o título da janela do
        # jogo, que aparece na barra de título da janela.
pygame.display.set_caption("Pac-Man")

# 'pygame.time.Clock()' cria um objeto relógio que pode ser usado
        # para controlar a taxa de atualizações do jogo,
        # também conhecido como quadros por segundo (FPS).
relogio = pygame.time.Clock()

# Define cores usando o modelo RGB, onde cada cor é uma tupla
        # de três valores (R, G, B) que representam,
        # respectivamente, a intensidade do vermelho, verde e azul.
PRETO = (0, 0, 0)       # Cor preta, ausência de cor em RGB.
AZUL = (33, 33, 255)     # Cor azul com máxima intensidade de azul e um pouco de vermelho e verde.
AMARELO = (255, 255, 0)  # Cor amarela, máxima intensidade de vermelho e verde, sem azul.
BRANCO = (255, 255, 255) # Cor branca, máxima intensidade de vermelho, verde e azul.
VERMELHO = (255, 0, 0)   # Cor vermelha, máxima intensidade de vermelho.
ROSA = (255, 182, 193)   # Cor rosa, com intensidades específicas de vermelho, verde e azul.
CIANO = (0, 255, 255)    # Cor ciano, máxima intensidade de verde e azul.
LARANJA = (255, 165, 0)  # Cor laranja, alta intensidade de vermelho com um pouco de verde.

# Carrega uma fonte do sistema para usar no jogo. 'SysFont' pega 
        # uma fonte do sistema e define o tamanho da fonte.
# Aqui, 'arial' é o tipo de fonte escolhida e 24 é o tamanho da fonte.
fonte = pygame.font.SysFont('arial', 24)


# Labirintos para cada fase
labirintos = [
    [
        # Cada string representa uma linha do labirinto na fase 1.
        # 'X' representa paredes que o Pac-Man não pode atravessar.
        # '.' representa os pequenos pontos que o Pac-Man coleta
                # para ganhar pontos.
        # 'o' representa as pastilhas energéticas que permitem ao Pac-Man
                # comer os fantasmas temporariamente.
        # '@' pode representar a localização inicial dos fantasmas ou um 
                # lugar especial no labirinto (não utilizado em todos os jogos).
        # ' ' (espaço em branco) é o caminho por onde o Pac-Man e os
                # fantasmas podem se mover.
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X............XX............X",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "X............XX............X",
        "X.XXXX.XX.XXXXXXXX.XX.XXXX.X",
        "X.XXXX.XX.XXXXXXXX.XX.XXXX.X",
        "X......XX....XX....XX......X",
        "XXXXXX.XXXXX XX XXXXX.XXXXXX",
        "     X.XXXXX XX XXXXX.X     ",
        "     X.XX          XX.X     ",
        "     X.XX XXX--XXX XX.X     ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "      .   X      X   .      ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "     X.XX XXX--XXX XX.X     ",
        "     X.XX          XX.X     ",
        "     X.XX XXXXXXXX XX.X     ",
        "XXXXXX.XX XXXXXXXX XX.XXXXXX",
        "X............XX............X",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "X...XX................XX...X",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "X......XX....XX....XX......X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X............@@............X",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ],
    # Fase 2
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X............XX............X",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "X.XXXX................XXXX.X",
        "X............XX............X",
        "X.XXXX.XX.XXXXXXXX.XX.XXXX.X",
        "X......XX....XX....XX......X",
        "XXXXXX.XXXXX.XX.XXXXX.XXXXXX",
        "     X.XXXXX XX XXXXX.X     ",
        "     X.XX          XX.X     ",
        "     X.XX XXX--XXX XX.X     ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "      .   X      X   .      ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "     X.XX XXX--XXX XX.X     ",
        "     X.XX          XX.X     ",
        "X....X.XX XXXXXXXX XX.X....X",
        "XoXX.X.XX XXXXXXXX XX.X.XXoX",
        "XoXX....................XXoX",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "XoXX....................XXoX",
        "X...XX................XX...X",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "X......XX....XX....XX......X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X............@@............X",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ],
    # Fase 3
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "X............XX............X",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "XoXXXX................XXXXoX",
        "X.XXXX.XXXXX.XX.XXXXX.XXXX.X",
        "X............XX............X",
        "X.XXXX.XX.XXXXXXXX.XX.XXXX.X",
        "X......XX....XX....XX......X",
        "XXXXXX.XXXXX.XX.XXXXX.XXXXXX",
        "     X.XXXXX XX XXXXX.X     ",
        "     X.XX          XX.X     ",
        "     X.XX XXX--XXX XX.X     ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "      .   X      X   .      ",
        "XXXXXX.XX X      X XX.XXXXXX",
        "     X.XX XXX--XXX XX.X     ",
        "     X.XX          XX.X     ",
        "X....X.XX XXXXXXXX XX.X....X",
        "XoXX.X.XX XXXXXXXX XX.X.XXoX",
        "XoXX....................XXoX",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "XoXXXX.XXXXX.XX.XXXXX.XXXXoX",
        "XoXX....................XXoX",
        "X...XX................XX...X",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "XXX.XX.XX.XXXXXXXX.XX.XX.XXX",
        "X......XX....XX....XX......X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X.XXXXXXXXXX.XX.XXXXXXXXXX.X",
        "X............@@............X",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]
]

# Constante que define o tamanho de cada bloco do labirinto em pixels. 
# Essa medida é utilizada para dimensionar paredes e caminhos no jogo.
TAMANHO_BLOCO = 16

# Variável global para manter a pontuação total do jogador durante o jogo.
pontuacao_total = 0

# Define uma função chamada 'carregar_pontuacao_acumulada' 
        # que não recebe parâmetros.
def carregar_pontuacao_acumulada():
    
    # Checa se um arquivo chamado 'pontuacoes.txt' existe no 
            # mesmo diretório do script.
    if os.path.exists("pontuacoes.txt"):
    
        # Abre o arquivo 'pontuacoes.txt' no modo de leitura ('r') e o
                # associa a uma variável chamada 'arquivo'.
        with open("pontuacoes.txt", "r") as arquivo:
        
            # Lê todas as linhas do arquivo e as armazena na lista 'linhas'.
            linhas = arquivo.readlines()
            
            # Inicializa uma variável 'total' com 0, que será usada para
                    # somar todas as pontuações.
            total = 0
            
            # Itera sobre cada 'linha' na lista 'linhas'.
            for linha in linhas:
                
                try:
                    
                    # Tenta executar o código dentro do bloco 'try'.
                    # Remove espaços em branco do começo e fim da string e
                            # divide a string pelo caractere ':'.
                    # Pega o segundo elemento resultante dessa divisão (índice 1), 
                            # que deve ser a pontuação,
                            # e converte esse elemento para inteiro.
                    pontos = int(linha.strip().split(":")[1])
                    
                    # Adiciona o valor convertido para inteiro à variável 'total'.
                    total += pontos
                    
                except:
                    
                    # Se ocorrer algum erro durante a tentativa, o bloco 'except' é executado,
                            # e o 'continue' faz com que o laço pule para a próxima iteração.
                    continue
                    
            # Retorna o valor de 'total' após terminar o loop.
            return total
            
    else:
        
        # Se o arquivo 'pontuacoes.txt' não existir, retorna 0.
        return 0


# Define a função 'mostrar_menu', que exibe o menu inicial do jogo e
        # aceita a pontuação acumulada como argumento.
def mostrar_menu(pontuacao_acumulada):
    
    # Inicia um loop infinito que continuará mostrando o menu até que
            # seja interrompido por uma ação (como pressionar uma tecla).
    while True:
    
        # Preenche toda a superfície da tela com a cor preta
                # para limpar a tela anterior.
        tela.fill(PRETO)
        
        # Renderiza o texto 'Pac-Man' usando a fonte previamente 
                # definida, com a cor amarela.
        titulo = fonte.render('Pac-Man', True, AMARELO)
        
        # Renderiza as instruções 'Pressione ESPAÇO para jogar' 
                # usando a fonte definida, com a cor branca.
        instrucoes = fonte.render('Pressione ESPAÇO para jogar', True, BRANCO)
        
        # Renderiza o texto mostrando a 'Pontuação Acumulada' do jogador, 
                # que é atualizada conforme o valor passado à função.
        pontuacao_texto = fonte.render(f'Pontuação Acumulada: {pontuacao_acumulada}', True, BRANCO)
        
        # Posiciona o texto do título no centro da tela, ajustado 
                # verticalmente para cima em 50 pixels da metade.
        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, ALTURA // 2 - 50))
        
        # Posiciona o texto de instruções exatamente no centro da tela.
        tela.blit(instrucoes, (LARGURA // 2 - instrucoes.get_width() // 2, ALTURA // 2))
        
        # Posiciona o texto de pontuação acumulada no centro da tela,
                # ajustado verticalmente para baixo em 50 pixels da metade.
        tela.blit(pontuacao_texto, (LARGURA // 2 - pontuacao_texto.get_width() // 2, ALTURA // 2 + 50))
        
        # Atualiza a tela para mostrar todas as novas informações renderizadas.
        pygame.display.flip()

        
        # Inicia um loop para processar eventos que são capturados pelo Pygame.
        for evento in pygame.event.get():
            
            # Verifica cada evento capturado na fila de eventos do Pygame.
            
            # Verifica se o tipo do evento é QUIT, que é disparado quando o 
                    # usuário clica no botão de fechar a janela.
            if evento.type == pygame.QUIT:
                
                # Chama pygame.quit() para finalizar todos os módulos do
                        # Pygame de maneira adequada.
                pygame.quit()
                
                # Chama sys.exit() para encerrar o programa.
                sys.exit()
            
            # Verifica se o tipo do evento é KEYDOWN, que verifica se 
                    # qualquer tecla foi pressionada.
            if evento.type == pygame.KEYDOWN:
                
                # Dentro do evento KEYDOWN, verifica se a tecla pressionada é 
                        # a barra de espaço (K_SPACE).
                if evento.key == pygame.K_SPACE:
                    
                    # Retorna do método ou função, efetivamente saindo do
                            # loop de menu ou de evento.
                    return


# Define uma classe chamada 'Jogador'.
class Jogador:
    
    # Método construtor que é chamado quando uma nova instância da classe é criada.
    def __init__(self, x, y):
    
        # A posição inicial do jogador é armazenada como uma lista 
                # de duas coordenadas: x e y.
        self.posicao = [x, y]
        
        # A direção atual do movimento do jogador é armazenada como uma lista.
        # Inicialmente, está definido para [0, 0], o que significa que o 
                # jogador não está se movendo.
        self.direcao = [0, 0]
        
        # A direção desejada é a direção para a qual o jogador quer se mover.
        # Isso pode mudar com base nas entradas do usuário (por exemplo,
                # pressionar uma tecla de seta).
        self.direcao_desejada = [0, 0]
        
        # Define a velocidade do jogador, que neste caso é um valor constante de 2.
        # Isso pode ser ajustado para tornar o jogo mais fácil ou mais difícil.
        self.velocidade = 2
        
        # Cria um objeto retângulo que representa a posição e 
                # tamanho do jogador na tela.
        # 'pygame.Rect' é usado para criar um retângulo onde 'x' e 'y'
                # são as coordenadas iniciais,
                # e 'TAMANHO_BLOCO' é a largura e altura do retângulo.
        self.retangulo = pygame.Rect(x, y, TAMANHO_BLOCO, TAMANHO_BLOCO)

    
    def mover(self, paredes):
        
        # Verifica se a direção que o jogador deseja seguir é
                # diferente da direção atual.
        if self.direcao_desejada != self.direcao:
            
            # Calcula qual seria a nova posição se o jogador seguir na direção desejada.
            nova_posicao = [self.posicao[0] + self.direcao_desejada[0] * self.velocidade,
                            self.posicao[1] + self.direcao_desejada[1] * self.velocidade]
            
            # Cria um retângulo de colisão na nova posição para 
                    # testar interseção com paredes.
            novo_retangulo = pygame.Rect(nova_posicao[0], nova_posicao[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
            
            # Testa se o novo retângulo colide com alguma das paredes do jogo.
            if not self.verificar_colisao(novo_retangulo, paredes):
                
                # Atualiza a direção atual do jogador para a direção 
                        # desejada, pois não há colisão.
                self.direcao = self.direcao_desejada
    
        # Calcula a nova posição do jogador baseando-se na direção atual.
        nova_posicao = [self.posicao[0] + self.direcao[0] * self.velocidade,
                        self.posicao[1] + self.direcao[1] * self.velocidade]
        
        # Cria outro retângulo de colisão para a nova posição calculada.
        novo_retangulo = pygame.Rect(nova_posicao[0], nova_posicao[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        
        # Verifica se o retângulo criado colide com qualquer parede.
        if not self.verificar_colisao(novo_retangulo, paredes):
            
            # Se não há colisão, atualiza a posição do jogador no jogo.
            self.posicao = nova_posicao
            
            # Atualiza o retângulo de colisão para a nova posição.
            self.retangulo = novo_retangulo
            
        else:
            
            # Se houver colisão, alinha o jogador ao bloco mais próximo 
                    # para evitar movimento parcial dentro das paredes.
            self.alinhar()
    
        # Verifica se o jogador atravessa os limites horizontais do
                # mapa para teletransporte.
        if self.posicao[0] < -TAMANHO_BLOCO:
            
            # Se o jogador sair pelo lado esquerdo, ele aparece no 
                    # lado direito da tela.
            self.posicao[0] = LARGURA
            
        elif self.posicao[0] > LARGURA:
            
            # Se o jogador sair pelo lado direito, ele aparece no
                    # lado esquerdo da tela.
            self.posicao[0] = -TAMANHO_BLOCO
    
        # Atualiza a posição do topo esquerdo do retângulo para
                # corresponder à nova posição do jogador.
        self.retangulo.topleft = self.posicao


    
    # Define o método 'verificar_colisao' na classe Jogador para
                # verificar colisões com as paredes.
    def verificar_colisao(self, retangulo, paredes):
        
        # Itera sobre a lista de paredes para verificar se há colisão 
                # entre o retângulo do jogador e qualquer parede.
        for parede in paredes:
            
            # Para cada parede na lista, verifica se o retângulo do 
                    # jogador intersecciona com a parede.
            if retangulo.colliderect(parede):
                
                # Se o retângulo do jogador intersecciona com alguma 
                        # das paredes, retorna True.
                return True
                
        # Se o loop terminar e nenhuma interseção for
                # detectada, retorna False.
        return False
    
    # Define o método 'alinhar' na classe Jogador para alinhar a
            # posição do jogador ao grid do labirinto.
    def alinhar(self):
        
        # Arredonda a posição x do jogador para o múltiplo mais
                # próximo de TAMANHO_BLOCO.
        self.posicao[0] = round(self.posicao[0] / TAMANHO_BLOCO) * TAMANHO_BLOCO
        
        # Arredonda a posição y do jogador para o múltiplo mais
                # próximo de TAMANHO_BLOCO.
        self.posicao[1] = round(self.posicao[1] / TAMANHO_BLOCO) * TAMANHO_BLOCO
        
        # Atualiza a posição do retângulo de colisão do jogador 
                # para refletir o alinhamento.
        self.retangulo.topleft = self.posicao


    # Método responsável por desenhar o jogador na superfície de jogo.
    def desenhar(self, superficie):
        
        # Desenha um círculo na superfície do jogo representando o jogador.
        # A cor do círculo é definida como AMARELO, e a posição é 
                # centralizada no bloco onde o jogador está.
        pygame.draw.circle(superficie, AMARELO, (int(self.posicao[0]) + TAMANHO_BLOCO // 2, int(self.posicao[1]) + TAMANHO_BLOCO // 2), TAMANHO_BLOCO // 2)
        
    # Método que permite ao jogador coletar pontos no jogo.
    def comer_ponto(self, pontos):
        
        # Itera sobre uma cópia da lista de pontos para permitir 
                # modificação durante a iteração.
        for ponto in pontos[:]:
            
            # Verifica se o retângulo do jogador colide com o 
                    # retângulo de um ponto.
            if self.retangulo.colliderect(ponto.retangulo):
                
                # Se colidir, o ponto é removido da lista de pontos.
                pontos.remove(ponto)
                
                # Retorna 1 para indicar que um ponto foi ganho.
                return 1
                
        # Se não houver colisão com nenhum ponto, retorna 0.
        return 0
    
    # Método que permite ao jogador coletar pastilhas no jogo.
    def comer_pastilha(self, pastilhas):
        
        # Itera sobre uma cópia da lista de pastilhas para 
                # permitir modificação durante a iteração.
        for pastilha in pastilhas[:]:
            
            # Verifica se o retângulo do jogador colide com o 
                    # retângulo de uma pastilha.
            if self.retangulo.colliderect(pastilha.retangulo):
                
                # Se colidir, a pastilha é removida da lista de pastilhas.
                pastilhas.remove(pastilha)
                
                # Retorna 50 para indicar que 50 pontos foram ganhos.
                return 50
                
        # Se não houver colisão com nenhuma pastilha, retorna 0.
        return 0


# Define a classe 'Ponto', que representa os pontos
        # coletáveis no jogo.
class Ponto:
    
    # Método construtor que inicializa um novo objeto Ponto com coordenadas x e y.
    def __init__(self, x, y):
        
        # Armazena a posição do ponto como uma lista de duas coordenadas [x, y].
        self.posicao = [x, y]
        
        # Cria um retângulo de colisão para o ponto. Este retângulo é
                # posicionado no centro do bloco
                # com um deslocamento para centralizar um círculo 
                # de 4 pixels de diâmetro (2 pixels de raio).
        self.retangulo = pygame.Rect(x + TAMANHO_BLOCO//2 - 2, y + TAMANHO_BLOCO//2 - 2, 4, 4)
    
    # Método para desenhar o ponto na superfície de jogo especificada.
    def desenhar(self, superficie):
        
        # Desenha um círculo branco na superfície de jogo que 
                # representa o ponto visualmente.
        # O círculo é desenhado no centro do bloco em que o 
                # ponto está posicionado.
        pygame.draw.circle(superficie, BRANCO, (self.posicao[0] + TAMANHO_BLOCO // 2, self.posicao[1] + TAMANHO_BLOCO // 2), 2)


# Define a classe 'Pastilha', que representa as pastilhas 
            # energéticas maiores que o jogador pode coletar no jogo.
class Pastilha:
    
    # Método construtor que inicializa uma nova pastilha com coordenadas x e y.
    def __init__(self, x, y):
    
        # Armazena a posição da pastilha como uma lista de
                # duas coordenadas [x, y].
        self.posicao = [x, y]
        
        # Cria um retângulo de colisão para a pastilha. 
        # Este retângulo é posicionado no centro do bloco
        # com um deslocamento para centralizar um círculo 
                # de 8 pixels de diâmetro (4 pixels de raio).
        self.retangulo = pygame.Rect(x + TAMANHO_BLOCO//2 - 4, y + TAMANHO_BLOCO//2 - 4, 8, 8)
    
    # Método para desenhar a pastilha na superfície de jogo especificada.
    def desenhar(self, superficie):
        
        # Desenha um círculo branco na superfície de jogo que
                # representa a pastilha visualmente.
        # O círculo é desenhado no centro do bloco em que a 
                # pastilha está posicionada, sendo maior que os pontos comuns.
        pygame.draw.circle(superficie, BRANCO, (self.posicao[0] + TAMANHO_BLOCO // 2, self.posicao[1] + TAMANHO_BLOCO // 2), 4)


# Define a classe 'Fantasma', que representa os inimigos no jogo.
class Fantasma:
    
    # Método construtor que inicializa um novo fantasma com
            # coordenadas x e y e uma cor específica.
    def __init__(self, x, y, cor):
    
        # Armazena a posição inicial do fantasma como uma lista
                # de duas coordenadas [x, y].
        self.posicao = [x, y]
        
        # Define a direção inicial do fantasma escolhendo aleatoriamente
                # entre as quatro possíveis direções.
        # Isso é feito usando 'random.choice', que seleciona um
                # item aleatório de uma lista.
        self.direcao = random.choice([[1,0], [-1,0], [0,1], [0,-1]])
        
        # Define a velocidade do fantasma. Neste caso, é um valor
                # constante de 2, igual à velocidade do jogador.
        self.velocidade = 2
        
        # Cria um retângulo de colisão para o fantasma. O retângulo é 
                # posicionado na localização inicial
                # e tem o tamanho de 'TAMANHO_BLOCO', que é o 
                # tamanho padrão para os elementos do jogo.
        self.retangulo = pygame.Rect(x, y, TAMANHO_BLOCO, TAMANHO_BLOCO)
        
        # Armazena a cor do fantasma, que é usada para desenhá-lo na
                # tela. A cor é passada como parâmetro.
        self.cor = cor

    
    def mover(self, paredes):
        
        # Calcula a nova posição do fantasma baseando-se na direção
                # atual e na velocidade.
        nova_posicao = [self.posicao[0] + self.direcao[0] * self.velocidade,
                        self.posicao[1] + self.direcao[1] * self.velocidade]
        
        # Cria um novo retângulo para essa posição, usado para 
                # detectar colisões com as paredes.
        novo_retangulo = pygame.Rect(nova_posicao[0], nova_posicao[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
        
        # Verifica se há colisão entre o novo retângulo e qualquer uma das paredes.
        if not self.verificar_colisao(novo_retangulo, paredes):
            
            # Se não houver colisão, atualiza a posição do 
                    # fantasma para a nova posição.
            self.posicao = nova_posicao
            
            # Atualiza o retângulo de colisão do fantasma para a nova posição.
            self.retangulo = novo_retangulo
            
        else:
            
            # Se houver colisão, o fantasma escolhe uma nova direção
                    # aleatoriamente para tentar evitar a parede.
            self.direcao = random.choice([[1,0], [-1,0], [0,1], [0,-1]])
    
        # Verifica se o fantasma passa pelos limites laterais do mapa,
                # permitindo "teletransporte" de um lado ao outro.
        if self.posicao[0] < -TAMANHO_BLOCO:
            
            # Se o fantasma sai pelo lado esquerdo da tela, ele 
                    # aparece no lado direito.
            self.posicao[0] = LARGURA
            
        elif self.posicao[0] > LARGURA:
            
            # Se o fantasma sai pelo lado direito da tela, ele 
                    # aparece no lado esquerdo.
            self.posicao[0] = -TAMANHO_BLOCO
    
        # Atualiza a posição do retângulo de colisão para estar 
                # alinhado com a nova posição do fantasma.
        self.retangulo.topleft = self.posicao

    
    # Define o método 'verificar_colisao' dentro da classe 'Fantasma'.
    def verificar_colisao(self, retangulo, paredes):
        
        # Este loop passa por cada 'parede' na lista 'paredes'.
        for parede in paredes:
        
            # Usa 'colliderect' para verificar se há uma interseção 
                    # entre o 'retangulo' do fantasma e qualquer 'parede'.
            if retangulo.colliderect(parede):
            
                # Retorna True se uma colisão for detectada, indicando 
                        # que o fantasma não pode mover para essa posição.
                return True
                
        # Retorna False se não houver colisões detectadas, permitindo 
                # que o fantasma continue seu movimento.
        return False
    
    # Define o método 'desenhar' dentro da classe 'Fantasma'.
    def desenhar(self, superficie):
        
        # Utiliza a função 'draw.rect' do pygame para desenhar o 
                # retângulo do fantasma na 'superficie' do jogo.
        pygame.draw.rect(superficie, self.cor, self.retangulo)
        # O retângulo é desenhado usando a cor armazenada em 'self.cor', e
                # as dimensões são definidas em 'self.retangulo'.

        
# Define a função 'main', que é o ponto de entrada principal do jogo.
def main():
    
    # Declara 'pontuacao_total' como uma variável global, permitindo
            # que ela seja modificada dentro da função.
    global pontuacao_total

    # Inicia um loop infinito que continuará rodando o jogo até
            # ser explicitamente encerrado.
    while True:
    
        # Chama a função 'carregar_pontuacao_acumulada' para obter a
                # pontuação acumulada de sessões anteriores.
        pontuacao_acumulada = carregar_pontuacao_acumulada()
        
        # Exibe o menu inicial do jogo, passando a pontuação 
                # acumulada para ser mostrada.
        mostrar_menu(pontuacao_acumulada)
        
        # Inicializa a variável 'fase_atual' com 0, indicando o
                # início do jogo na primeira fase.
        fase_atual = 0
        
        # Reinicializa 'pontuacao_total' com 0 para começar a contagem 
                # de pontos para a nova sessão de jogo.
        pontuacao_total = 0
        
        # Define 'vidas' com 5, dando ao jogador 5 vidas no início do jogo.
        vidas = 5


        # Inicia um loop que continua enquanto 'fase_atual' for menor 
                # que o número total de labirintos disponíveis.
        while fase_atual < len(labirintos):
            
            # Cria listas vazias para armazenar objetos de paredes, 
                    # pontos, pastilhas e fantasmas.
            paredes = []
            pontos = []
            pastilhas = []
            fantasmas = []
        
            # Seleciona o labirinto correspondente à fase atual 
                    # da lista de labirintos.
            labirinto = labirintos[fase_atual]
        
            # Determina o número de linhas no labirinto, que é o número de
                    # elementos na lista labirinto.
            LINHAS = len(labirinto)
            
            # Determina o número de colunas no labirinto, que é o comprimento do
                    # primeiro elemento (string) da lista labirinto.
            COLUNAS = len(labirinto[0])
        
            # Define a posição inicial do jogador dentro do labirinto.
            # Multiplica-se o número de bloco padrão pelo índice para centralizar o 
                    # jogador no meio do labirinto na vertical e próxima ao 
                    # centro na horizontal.
            jogador_posicao_inicial = (14 * TAMANHO_BLOCO, 23 * TAMANHO_BLOCO)
            
            # Cria uma instância do jogador na posição inicial definida.
            jogador = Jogador(*jogador_posicao_inicial)


            # Cria o labirinto iterando sobre cada linha e cada coluna dentro 
                    # do array de strings do labirinto.
            for linha in range(LINHAS):
                
                for coluna in range(COLUNAS):
                    
                    # Acessa o caractere específico no labirinto que indica o 
                            # tipo de bloco (parede, ponto, etc.)
                    bloco = labirinto[linha][coluna]
                    
                    # Calcula a posição x baseada na coluna atual, multiplicando
                            # pelo tamanho padrão do bloco.
                    x = coluna * TAMANHO_BLOCO
                    
                    # Calcula a posição y baseada na linha atual, também multiplicando
                            # pelo tamanho do bloco.
                    y = linha * TAMANHO_BLOCO
                    
                    # Verifica se o caractere no labirinto é 'X', o que
                            # indica uma parede.
                    if bloco == 'X':
                    
                        # Cria um retângulo na posição calculada que servirá 
                                # como uma parede no jogo.
                        parede = pygame.Rect(x, y, TAMANHO_BLOCO, TAMANHO_BLOCO)
                        
                        # Adiciona o retângulo criado à lista de paredes.
                        paredes.append(parede)
                        
                    # Verifica se o caractere é '.', indicando um ponto coletável.
                    elif bloco == '.':
                        
                        # Cria um objeto Ponto na posição calculada.
                        ponto = Ponto(x, y)
                        
                        # Adiciona o ponto à lista de pontos que o jogador pode coletar.
                        pontos.append(ponto)
                        
                    # Verifica se o caractere é 'o', indicando uma pastilha.
                    elif bloco == 'o':
                        
                        # Cria um objeto Pastilha na posição calculada.
                        pastilha = Pastilha(x, y)
                        
                        # Adiciona a pastilha à lista de pastilhas, que são 
                                # itens especiais no jogo.
                        pastilhas.append(pastilha)
                        
                    # Verifica se o caractere é '@', indicando a posição 
                            # inicial de um fantasma.
                    elif bloco == '@':
                        
                        # Cria um objeto Fantasma na posição calculada e
                                # define sua cor como vermelho.
                        fantasma = Fantasma(x, y, VERMELHO)
                        
                        # Adiciona o fantasma criado à lista de fantasmas 
                                # que irão perseguir o jogador.
                        fantasmas.append(fantasma)


            # Define a variável 'numero_de_fantasmas_extra' com 
                    # base no número da fase atual.
            # Multiplica o índice da fase atual por 2 para aumentar a
                    # dificuldade progressivamente:
            # Na primeira fase (índice 0), não adiciona fantasmas extras.
            # Na segunda fase (índice 1), adiciona 2 fantasmas 
                    # extras, e assim por diante.
            numero_de_fantasmas_extra = fase_atual * 2  # 0 na primeira fase, 2 na segunda, etc.
            
            # Lista das cores disponíveis para os fantasmas extras.
            # Isso permite variar visualmente os fantasmas e pode também 
                    # indicar diferentes comportamentos ou propriedades.
            cores_fantasmas = [VERMELHO, ROSA, CIANO, LARANJA]
            
            # Define posições iniciais para os fantasmas extras.
            # Essas posições são estrategicamente escolhidas para estar no
                    # centro do labirinto, facilitando a distribuição dos fantasmas.
            posicoes_fantasmas = [
                (14 * TAMANHO_BLOCO, 14 * TAMANHO_BLOCO),  # Posição central.
                (14 * TAMANHO_BLOCO, 15 * TAMANHO_BLOCO),  # Posição abaixo do centro.
                (13 * TAMANHO_BLOCO, 14 * TAMANHO_BLOCO),  # Posição à esquerda do centro.
                (15 * TAMANHO_BLOCO, 14 * TAMANHO_BLOCO)   # Posição à direita do centro.
            ]


            # Inicializa uma lista vazia para armazenar as posições
                    # iniciais dos fantasmas adicionais.
            fantasmas_posicoes_iniciais = []
            
            # Itera sobre o número de fantasmas extras determinado 
                    # pela fase atual do jogo.
            for i in range(numero_de_fantasmas_extra):
                
                # Seleciona a posição para o novo fantasma usando um padrão 
                        # circular com base no número total de posições disponíveis.
                # Isso assegura que a lista de posições não seja excedida,
                        # reutilizando posições conforme necessário.
                x, y = posicoes_fantasmas[i % len(posicoes_fantasmas)]
                
                # Seleciona a cor para o novo fantasma usando um padrão 
                        # circular semelhante ao das posições.
                # Isso garante variação nas cores dos fantasmas adicionais e
                        # evita exceder o número de cores disponíveis.
                cor = cores_fantasmas[i % len(cores_fantasmas)]
                
                # Cria uma nova instância do fantasma na posição e cor determinadas.
                fantasma = Fantasma(x, y, cor)
                
                # Adiciona o novo fantasma à lista de fantasmas ativos no jogo.
                fantasmas.append(fantasma)
                
                # Adiciona a posição inicial do novo fantasma à lista de posições iniciais.
                # Isso é útil para redefinir os fantasmas às suas posições
                        # originais se necessário, por exemplo, após o 
                        # jogador perder uma vida.
                fantasmas_posicoes_iniciais.append((x, y))


            # Inicializa ou reinicializa a lista que armazena as posições 
                    # iniciais de todos os fantasmas.
            # Isso inclui tanto os fantasmas adicionados na fase atual 
                    # quanto qualquer fantasma já existente.
            for fantasma in fantasmas:
                
                # Adiciona a posição atual de cada fantasma na 
                        # lista 'fantasmas_posicoes_iniciais'.
                # Isso é usado para redefinir a posição dos fantasmas caso o
                        # jogador perca uma vida ou reinicie a fase.
                fantasmas_posicoes_iniciais.append((fantasma.posicao[0], fantasma.posicao[1]))
            
            # Inicializa a pontuação da fase atual como zero.
            # Isso garante que a pontuação comece do zero a cada nova fase.
            pontuacao = 0
            
            # Define a variável 'rodando' como True para iniciar o loop 
                    # principal do jogo para a fase.
            # Essa variável controla se o loop de jogo continua executando, 
                    # sendo útil para terminar o jogo ou avançar de fase.
            rodando = True

            # Mantém o jogo executando enquanto a variável 'rodando'
                    # estiver definida como True.
            while rodando:
                
                # Define a taxa de quadros por segundo (FPS) para 60, o que 
                        # significa que o jogo tentará atualizar 60 vezes por segundo.
                relogio.tick(60)  # Limita a 60 FPS
                
                # Itera sobre todos os eventos que ocorreram desde a 
                        # última atualização.
                for evento in pygame.event.get():
                    
                    # Verifica se o evento é do tipo QUIT, que ocorre 
                            # quando o jogador fecha a janela do jogo.
                    if evento.type == pygame.QUIT:
                    
                        # Finaliza todos os módulos do Pygame de maneira adequada.
                        pygame.quit()
                        
                        # Sai do programa completamente.
                        sys.exit()
                    
                    # Verifica se algum evento de tecla pressionada foi capturado.
                    if evento.type == pygame.KEYDOWN:
                        
                        # Verifica se a tecla pressionada é a seta para esquerda.
                        if evento.key == pygame.K_LEFT:
                        
                            # Atualiza a direção desejada do jogador para esquerda.
                            jogador.direcao_desejada = [-1, 0]
                        
                        # Verifica se a tecla pressionada é a seta para direita.
                        elif evento.key == pygame.K_RIGHT:
                            
                            # Atualiza a direção desejada do jogador para direita.
                            jogador.direcao_desejada = [1, 0]
                            
                        # Verifica se a tecla pressionada é a seta para cima.
                        elif evento.key == pygame.K_UP:
                            
                            # Atualiza a direção desejada do jogador para cima.
                            jogador.direcao_desejada = [0, -1]
                            
                        # Verifica se a tecla pressionada é a seta para baixo.
                        elif evento.key == pygame.K_DOWN:
                            
                            # Atualiza a direção desejada do jogador para baixo.
                            jogador.direcao_desejada = [0, 1]


                # Chama o método 'mover' do objeto jogador, passando a 
                        # lista de paredes como argumento.
                # Este método atualiza a posição do jogador com base em sua
                        # direção desejada e verifica colisões.
                jogador.mover(paredes)
                
                # Chama o método 'comer_ponto' do jogador para verificar se o
                        # jogador coletou algum dos pontos no labirinto.
                # O método retorna a quantidade de pontos ganhos, que por
                        # padrão é 1 por ponto coletado.
                # A pontuação retornada é então adicionada à pontuação 
                        # total do jogador para esta fase.
                pontuacao += jogador.comer_ponto(pontos)
                
                # Similar ao método 'comer_ponto', o método 'comer_pastilha' 
                        # verifica se o jogador coletou alguma pastilha.
                # Cada pastilha coletada vale 50 pontos, e esse valor é 
                        # adicionado à pontuação total.
                # As pastilhas geralmente oferecem ao jogador vantagens 
                        # temporárias, como poder comer os fantasmas.
                pontuacao += jogador.comer_pastilha(pastilhas)


                # Itera sobre cada fantasma na lista de fantasmas para 
                        # mover e verificar colisões.
                for idx, fantasma in enumerate(fantasmas):
                    
                    # Chama o método 'mover' do objeto fantasma, passando a
                            # lista de paredes como argumento.
                    # Este método permite que o fantasma se mova dentro do labirinto e 
                            # mude de direção se necessário ao colidir com uma parede.
                    fantasma.mover(paredes)
                    
                    # Verifica se há colisão entre o retângulo de colisão do 
                            # fantasma e o retângulo do jogador.
                    if fantasma.retangulo.colliderect(jogador.retangulo):
                        
                        # Caso haja colisão, significa que o jogador foi "pego" pelo fantasma.
                        # Reduz o número de vidas do jogador em 1.
                        vidas -= 1
                        
                        # Verifica se o jogador ainda tem vidas restantes após ser pego.
                        if vidas > 0:
                            
                            # Se o jogador ainda tem vidas, reinicia a posição do 
                                    # jogador para a posição inicial da fase.
                            # Isso é feito para dar ao jogador a chance de continuar
                                    # jogando a partir de um ponto seguro.
                            jogador.posicao = list(jogador_posicao_inicial)
                            
                            # Reseta a direção atual e a direção desejada do jogador
                                    # para zero, parando seu movimento.
                            jogador.direcao = [0, 0]
                            jogador.direcao_desejada = [0, 0]
                            
                            # Atualiza a posição do retângulo de colisão do jogador para
                                    # corresponder à posição inicial.
                            jogador.retangulo.topleft = jogador.posicao

                            # Reinicia posições dos fantasmas
                            for idx, fantasma in enumerate(fantasmas):
                               
                                # Recupera as posições iniciais dos fantasmas da lista 
                                        # que armazena essas informações.
                                x, y = fantasmas_posicoes_iniciais[idx]
                                
                                # Redefine a posição do fantasma para a sua posição inicial.
                                fantasma.posicao = [x, y]
                                
                                # Atribui uma nova direção aleatória ao fantasma para
                                        # aumentar a imprevisibilidade após o reinício.
                                fantasma.direcao = random.choice([[1,0], [-1,0], [0,1], [0,-1]])
                                
                                # Atualiza o retângulo de colisão do fantasma para
                                        # corresponder à nova posição.
                                fantasma.retangulo.topleft = fantasma.posicao
                            
                            # Exibe mensagem de perda de vida
                            # Preenche toda a tela com a cor preta para limpar o 
                                        # conteúdo anterior.
                            tela.fill(PRETO)
                            
                            # Renderiza uma mensagem informando ao jogador que ele
                                    # perdeu uma vida e mostrando quantas vidas restam.
                            texto_vida = fonte.render(f'Você perdeu uma vida! Vidas restantes: {vidas}', True, BRANCO)
                            
                            # Posiciona a mensagem de perda de vida no centro da tela.
                            tela.blit(texto_vida, (LARGURA // 2 - texto_vida.get_width() // 2, ALTURA // 2))
                            
                            # Atualiza a tela para exibir a mensagem de perda de vida.
                            pygame.display.flip()
                            
                            # Pausa o jogo por 2000 milissegundos (2 segundos) para 
                                    # dar tempo ao jogador de ler a mensagem.
                            pygame.time.wait(2000)

                        else:
                            
                            # Este bloco é executado se o jogador não tiver mais vidas
                                    # restantes, indicando o fim do jogo.
                            
                            # Preenche toda a tela com a cor preta para preparar a 
                                    # exibição da mensagem de fim de jogo.
                            tela.fill(PRETO)
                            
                            # Renderiza a mensagem de fim de jogo usando a cor branca.
                            texto_fim = fonte.render('Você perdeu todas as vidas! Fim de Jogo!', True, BRANCO)
                            
                            # Posiciona a mensagem de fim de jogo no centro da tela.
                            tela.blit(texto_fim, (LARGURA // 2 - texto_fim.get_width() // 2, ALTURA // 2))
                            
                            # Atualiza a tela para exibir a mensagem de fim de jogo.
                            pygame.display.flip()
                            
                            # Pausa o jogo por 3000 milissegundos (3 segundos) para permitir 
                                    # que o jogador leia a mensagem de fim de jogo.
                            pygame.time.wait(3000)
                            
                            # Adiciona a pontuação obtida na fase atual à pontuação
                                    # total acumulada ao longo do jogo.
                            pontuacao_total += pontuacao
                            
                            # Chama a função para salvar a pontuação total no sistema de
                                    # arquivos ou base de dados conforme implementado.
                            salvar_pontuacao(pontuacao_total)
                            
                            # Define a variável 'rodando' como False para sair do
                                    # loop principal do jogo.
                            rodando = False
                            
                            # Utiliza 'break' para sair imediatamente do loop, retornando ao
                                    # menu principal ou encerrando a fase.
                            break


                # Verifica se a variável 'rodando' foi definida como False, o que 
                        # indica que o jogo deve parar.
                if not rodando:
                
                    # O jogador perdeu todas as vidas e a condição do jogo para 
                            # continuar rodando não é mais verdadeira,
                            # então o loop de jogo é interrompido e controla o
                            # retorno ao menu principal.
                    break
                
                # Verifica se todos os pontos e pastilhas no labirinto
                        # foram coletados pelo jogador.
                if not pontos and not pastilhas:
                    
                    # Adiciona a pontuação obtida na fase atual à
                            # pontuação total acumulada.
                    pontuacao_total += pontuacao
                    
                    # Incrementa a variável 'fase_atual' para mover o
                            # jogo para a próxima fase.
                    fase_atual += 1
                    
                    # Interrompe o loop atual para reiniciar o jogo com a próxima fase,
                    # permitindo que o setup inicial da nova fase seja processado.
                    break
                
                # Prepara a tela para a nova renderização, preenchendo-a com preto.
                # Isso limpa a tela de qualquer desenho anterior antes de
                        # começar a renderizar os novos elementos.
                tela.fill(PRETO)


                # Desenha o labirinto
                for parede in paredes:
                    
                    # Usa a função 'draw.rect' do Pygame para desenhar 
                            # cada parede na tela.
                    # As paredes são desenhadas na cor azul, e cada 'parede' é 
                            # um retângulo definido anteriormente.
                    pygame.draw.rect(tela, AZUL, parede)
                
                # Desenha os pontos
                for ponto in pontos:
                    
                    # Chama o método 'desenhar' da classe Ponto para cada
                            # ponto na lista de pontos.
                    # Este método é responsável por desenhar o ponto na
                            # tela, como definido na classe Ponto.
                    ponto.desenhar(tela)
                
                # Desenha as pastilhas
                for pastilha in pastilhas:
                    
                    # Chama o método 'desenhar' da classe Pastilha para cada
                            # pastilha na lista de pastilhas.
                    # Semelhante ao método da classe Ponto, ele desenha a 
                            # pastilha na tela na posição especificada.
                    pastilha.desenhar(tela)
                
                # Desenha o jogador
                # Chama o método 'desenhar' da classe Jogador para
                        # desenhar o jogador na tela.
                # Este método trata de renderizar o jogador na sua posição
                        # atual e com a aparência definida.
                jogador.desenhar(tela)


                # Desenha os fantasmas
                for fantasma in fantasmas:
                    
                    # Chama o método 'desenhar' da classe Fantasma para cada 
                            # fantasma na lista de fantasmas.
                    # Este método é responsável por renderizar o fantasma na tela, 
                            # utilizando as características definidas na classe Fantasma.
                    fantasma.desenhar(tela)
                
                # Desenha a pontuação
                # Renderiza o texto da pontuação usando a fonte definida, o valor é a 
                        # soma da pontuação total com a pontuação acumulada na fase atual.
                texto_pontuacao = fonte.render(f'Pontuação: {pontuacao_total + pontuacao}', True, BRANCO)

                # Posiciona o texto da pontuação na tela, especificamente no 
                        # canto superior esquerdo a 10 pixels das bordas.
                tela.blit(texto_pontuacao, (10, 10))
                
                # Desenha as vidas
                # Renderiza o texto das vidas restantes do jogador, também 
                        # usando a fonte definida.
                texto_vidas = fonte.render(f'Vidas: {vidas}', True, BRANCO)

                # Posiciona o texto das vidas no canto superior direito da tela, 
                        # ajustando para que não sobreponha a borda.
                tela.blit(texto_vidas, (LARGURA - texto_vidas.get_width() - 10, 10))
                
                # Atualiza a tela para exibir todos os elementos gráficos que 
                        # foram renderizados neste ciclo de jogo.
                pygame.display.flip()


            # Verifica se a variável 'rodando' está definida como False e
                        # se o jogador não possui mais vidas.
            if not rodando and vidas == 0:
                
                # Se ambas as condições forem verdadeiras, indica que o 
                        # jogador perdeu todas as vidas.
                # O loop das fases é interrompido, saindo assim do jogo 
                        # ou retornando ao menu inicial.
                break
            
            # Verifica se o índice da fase atual é menor que o número total de 
                    # labirintos e se o jogador ainda possui vidas.
            if fase_atual < len(labirintos) and vidas > 0:
                
                # Se o jogador concluiu a fase e ainda tem vidas, prepara a
                        # tela para a mensagem de conclusão.
                
                # Preenche a tela com preto para limpar qualquer conteúdo visual anterior.
                tela.fill(PRETO)
                
                # Renderiza o texto 'Fase Concluída!' usando a fonte definida, na cor branca.
                texto_fase = fonte.render('Fase Concluída!', True, BRANCO)
                
                # Posiciona o texto de conclusão da fase centralizado 
                        # horizontalmente e verticalmente na tela.
                tela.blit(texto_fase, (LARGURA // 2 - texto_fase.get_width() // 2, ALTURA // 2))
                
                # Atualiza a tela para mostrar a mensagem de conclusão da fase.
                pygame.display.flip()
                
                # Pausa o jogo por 2000 milissegundos (2 segundos) para
                        # permitir que o jogador leia a mensagem.
                pygame.time.wait(2000)


        else:
        
            # Esta condição é executada se o jogador completar
                    # todas as fases disponíveis no jogo.
            
            # Preenche a tela com preto para limpar qualquer conteúdo 
                    # visual anterior e preparar para a nova mensagem.
            tela.fill(PRETO)
            
            # Renderiza a mensagem de vitória usando a fonte definida, na cor branca.
            texto_vitoria = fonte.render('Parabéns! Você venceu!', True, BRANCO)
            
            # Renderiza a mensagem de pontuação final, mostrando a 
                    # pontuação total acumulada durante o jogo.
            pontuacao_final = fonte.render(f'Pontuação Total: {pontuacao_total}', True, BRANCO)
            
            # Posiciona o texto de vitória acima do centro
                    # horizontal e vertical da tela.
            tela.blit(texto_vitoria, (LARGURA // 2 - texto_vitoria.get_width() // 2, ALTURA // 2 - 20))
            
            # Posiciona o texto da pontuação final abaixo do centro
                    # horizontal e vertical da tela.
            tela.blit(pontuacao_final, (LARGURA // 2 - pontuacao_final.get_width() // 2, ALTURA // 2 + 20))
            
            # Atualiza a tela para mostrar as mensagens de vitória e
                    # de pontuação final.
            pygame.display.flip()
            
            # Pausa o jogo por 5000 milissegundos (5 segundos) para 
                    # permitir que o jogador leia as mensagens.
            pygame.time.wait(5000)
            
            # Chama a função para salvar a pontuação total no sistema de 
                    # arquivos ou base de dados conforme implementado.
            salvar_pontuacao(pontuacao_total)


# Define a função 'salvar_pontuacao' que recebe um 
        # argumento 'pontuacao'.
def salvar_pontuacao(pontuacao):
    
    # Abre ou cria um arquivo chamado 'pontuacoes.txt' no modo de adição ('a'),
    # que permite escrever no final do arquivo sem 
            # sobrescrever o conteúdo existente.
    with open("pontuacoes.txt", "a") as arquivo:
        
        # Escreve a pontuação recebida no arquivo, formatada 
                # com a etiqueta 'Pontuação: ',
                # seguida pelo valor da pontuação e uma quebra de
                # linha para separar entradas subsequentes.
        arquivo.write(f"Pontuação: {pontuacao}\n")

# Chama a função 'main' para iniciar o jogo.
# Esta é a entrada do programa que dispara a execução de
        # todas as lógicas do jogo.
main()