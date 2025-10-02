# Importa o módulo pygame, uma biblioteca para criar jogos e interfaces gráficas em Python.
import pygame

# Importa o módulo random, usado para gerar números aleatórios, útil para escolher peças aleatórias no Tetris.
import random

# Importa o módulo time, que fornece funções relacionadas ao tempo, como pausas (sleep) durante o jogo.
import time

# Importa o módulo sys, que fornece acesso a algumas variáveis e funções usadas pelo interpretador Python.
import sys

# Importa o módulo os, usado para interagir com o sistema operacional. Neste caso, pode ser útil para manipular arquivos e diretórios.
import os

# Importa o módulo mixer do pygame, que é usado para carregar e reproduzir sons, como efeitos sonoros no jogo.
import pygame.mixer

# Define as configurações básicas do jogo.
LARGURA, ALTURA = 300, 600  # Define a largura e a altura da janela do jogo em pixels.
TAMANHO_GRADE = 30          # Define o tamanho de cada célula da grade do jogo, também em pixels.
COLUNAS_GRADE = LARGURA // TAMANHO_GRADE  # Calcula o número de colunas na grade baseado na largura e no tamanho da célula.
LINHAS_GRADE = ALTURA // TAMANHO_GRADE    # Calcula o número de linhas na grade baseado na altura e no tamanho da célula.

# Define cores que serão usadas no jogo. Cada cor é definida como uma tupla de três valores (R, G, B), 
# representando os componentes de cor vermelha, verde e azul.
BRANCO = (255, 255, 255)  # Define a cor branca.
PRETO = (0, 0, 0)         # Define a cor preta.

# Inicializa o sistema de fontes do pygame, que é necessário para renderizar textos.
pygame.font.init()

# Define a fonte que será usada para exibir textos no
# jogo, como a pontuação. A fonte padrão é selecionada e seu 
# tamanho é definido como 36.
FONT = pygame.font.SysFont(None, 36)

# Define um array de cores que serão usadas para as diferentes peças do Tetris.
# Cada cor é uma tupla (R, G, B).
CORES = [
    
    # Preto
    # R = 0, G = 0, B = 0
    # Geralmente usado para representar espaços vazios na grade do jogo.
    (0, 0, 0),

    # Vermelho
    # R = 255, G = 0, B = 0
    # Máximo de vermelho com ausência de verde e azul. Cor brilhante e chamativa.
    (255, 0, 0),

    # Verde
    # R = 0, G = 255, B = 0
    # Máximo de verde sem vermelho e azul. Cor vibrante que se destaca bem.
    (0, 255, 0),

    # Azul
    # R = 0, G = 0, B = 255
    # Máximo de azul com ausência de vermelho e verde. Uma cor primária forte.
    (0, 0, 255),

    # Amarelo
    # R = 255, G = 255, B = 0
    # Combinação máxima de vermelho e verde, sem azul. Resulta em um amarelo brilhante.
    (255, 255, 0),

    # Magenta
    # R = 255, G = 0, B = 255
    # Combinação máxima de vermelho e azul, sem verde. Uma cor vibrante que 
    # combina características do vermelho e do azul.
    (255, 0, 255),

    # Ciano
    # R = 0, G = 255, B = 255
    # Combinação máxima de verde e azul, sem vermelho. Uma 
    # cor refrescante que lembra a água.
    (0, 255, 255),

    # Cinza médio
    # R = 128, G = 128, B = 128
    # Igual proporção de vermelho, verde e azul, resultando
    # em um cinza médio.
    # Não tão escuro como o preto, mas ainda assim neutro e discreto.
    (128, 128, 128)
]


# Formas das peças do Tetris
FORMAS = [
    
    # Representa a peça "T".
    # A matriz é 3x2 onde a primeira linha tem três blocos (1s) e a 
    # segunda linha tem um bloco no meio.
    # Representação visual:
    # 111
    # 010
    [[1, 1, 1],
     [0, 1, 0]],

    # Representa a peça "O".
    # Uma matriz 2x2 completamente preenchida (todos 1s), formando um quadrado.
    # Representação visual:
    # 11
    # 11
    [[1, 1],
     [1, 1]],

    # Representa a peça "L".
    # Uma matriz 1x4, representando uma linha reta de quatro blocos.
    # Representação visual:
    # 1111
    [[1, 1, 1, 1]],

    # Representa a peça "L".
    # A matriz é 3x2 com três blocos na primeira linha e um bloco no início da segunda linha.
    # Representação visual:
    # 111
    # 100
    [[1, 1, 1],
     [1, 0, 0]],

    # Representa a peça "J".
    # A matriz é 3x2 com três blocos na primeira linha e um bloco no final da segunda linha.
    # Representação visual:
    # 111
    # 001
    [[1, 1, 1],
     [0, 0, 1]],

    # Representa outra variação da peça "T".
    # Semelhante à primeira peça "T", mas a posição dos blocos pode variar
    # na implementação do jogo.
    # Representação visual:
    # 111
    # 010
    [[1, 1, 1],
     [0, 1, 0]],

    # Representa a peça "S".
    # A matriz é 2x3 com dois blocos deslocados na primeira linha e dois
    # blocos deslocados na segunda linha.
    # Representação visual:
    # 011
    # 110
    [[0, 1, 1],
     [1, 1, 0]]
]

# Inicializa o módulo mixer do Pygame, que é necessário para carregar e reproduzir sons.
pygame.mixer.init()


# Carrega o som que será tocado quando a tecla de espaço for pressionada. 
# É necessário substituir 'som_espaco.mp3' pelo caminho correto do arquivo de som.
SOM_PONTO = pygame.mixer.Sound('ponto.mp3')

# Define o volume do som da tecla de espaço para 50%. O volume pode
# variar de 0.0 (silencioso) a 1.0 (volume máximo).
SOM_PONTO.set_volume(0.5)


# Define a classe Tetris, que representa o jogo.
class Tetris:
    
    # Método construtor da classe Tetris, responsável por 
    # inicializar uma nova instância do jogo.
    def __init__(self):
        
        # Inicializa todos os módulos internos do Pygame, preparando o 
        # sistema para uso de recursos de vídeo, som e eventos.
        pygame.init()

        # Cria e exibe a janela do jogo. A função 'set_mode' recebe uma 
        # tupla com largura e altura (definidas anteriormente),
        # estabelecendo assim as dimensões da janela de exibição do jogo.
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))

        # Define o título da janela do jogo para "Tetris". Isso 
        # aparecerá na barra de título da janela.
        pygame.display.set_caption("Tetris")

        # Cria a grade do jogo, que é uma lista de listas (matriz). A grade é usada para acompanhar a posição das peças.
        # Cada célula da grade pode ser 0 (espaço vazio) ou um número representando a cor da peça.
        # A grade tem o tamanho de 'LINHAS_GRADE' (número de linhas) por 'COLUNAS_GRADE' (número de colunas).
        # O uso de '[0] * COLUNAS_GRADE' cria uma linha com todas as células inicializadas como 0 (espaço vazio).
        # O loop 'for _ in range(LINHAS_GRADE)' repete essa operação para criar todas as linhas da grade.
        # self.grade = [[0] * COLUNAS_GRADE for _ in range(LINHAS_GRADE)]
        
        
        # Inicializa a variável 'grade' como uma lista vazia.
        # Esta variável 'grade' será usada para representar a grade do
        # jogo Tetris, onde as peças serão colocadas.
        self.grade = []

        # O loop 'for' irá iterar 'LINHAS_GRADE' vezes.
        # 'LINHAS_GRADE' é uma constante que define o número de linhas na grade do Tetris.
        for _ in range(LINHAS_GRADE):
            
            # Dentro do loop, 'self.grade.append(...)' é chamado para
            # adicionar uma nova linha à grade.
            # Cada linha da grade é representada por uma lista.

            # '[0] * COLUNAS_GRADE' cria uma lista contendo zeros.
            # 'COLUNAS_GRADE' é uma constante que define o número de colunas na grade do Tetris.
            # Multiplicar uma lista por um número (neste caso, 'COLUNAS_GRADE')
            # cria uma nova lista onde o conteúdo original é repetido.
            # Por exemplo, se 'COLUNAS_GRADE' é 10, '[0] * 10' resulta em [0, 0, 0, 0, 0, 0, 0, 0, 0, 0].
            # O resultado é que cada linha na grade contém 'COLUNAS_GRADE' zeros, 
            # representando espaços vazios onde ainda não há peças.
            self.grade.append([0] * COLUNAS_GRADE)

        
        # Inicializa a pontuação do jogo como 0. Este valor será atualizado
        # conforme o jogador completa linhas.
        self.pontuacao = 0

        # Define a velocidade de queda das peças. Um valor mais alto 
        # resulta em peças caindo mais rápido.
        # Este valor pode ser ajustado para aumentar a dificuldade à 
        # medida que o jogo avança.
        self.velocidade_queda = 0.5

        # Inicializa a variável que armazenará a peça atual controlada pelo jogador.
        # No início do jogo, não há peça atual, então é definida como None.
        self.peca_atual = None

        # Define um indicador de estado do jogo. 'fim_de_jogo' será True se o 
        # jogo terminar (quando as peças atingirem o topo da grade).
        self.fim_de_jogo = False

        # Controla se a tecla para mover a peça para baixo está sendo pressionada.
        # Isso permite implementar a funcionalidade de acelerar a queda da peça quando 
        # o jogador pressiona uma tecla específica.
        self.tecla_para_baixo_pressionada = False
        
        
    def nova_peca(self):
        
        # Escolhe aleatoriamente uma forma de peça do array 'FORMAS'.
        # 'random.choice' seleciona um elemento aleatório da lista fornecida, neste caso, 'FORMAS'.
        # Cada elemento em 'FORMAS' é uma matriz representando a forma de uma peça de Tetris.
        forma = random.choice(FORMAS)

        # Gera um número aleatório para a cor da peça.
        # 'random.randint' gera um número inteiro aleatório entre os dois argumentos inclusivos.
        # Aqui, escolhe-se um número entre 1 e o número de cores disponíveis em 'CORES' menos um.
        # O intervalo começa em 1 porque a cor na posição 0 é geralmente usada para espaços vazios.
        cor = random.randint(1, len(CORES) - 1)

        # Cria a peça atual com suas propriedades.
        # 'forma': A matriz da forma da peça escolhida.
        # 'cor': O índice da cor escolhida para a peça.
        # 'x': A posição inicial horizontal (coluna) da peça. 
        #      Calculado para colocar a peça aproximadamente no meio horizontal da grade.
        #      'COLUNAS_GRADE // 2' encontra o ponto médio da grade. 'len(forma[0]) // 2' encontra o meio da peça.
        #      Subtraindo um do outro, a peça é posicionada de forma que seu centro esteja perto do meio da grade.
        # 'y': A posição inicial vertical (linha) da peça. Começa em 0, que é a linha superior da grade.
        self.peca_atual = {'forma': forma, 
                           'cor': cor, 
                           'x': COLUNAS_GRADE // 2 - len(forma[0]) // 2, 
                           'y': 0}
        
        
    # Este método é responsável por verificar se ocorrerá uma colisão
    # caso a peça atual do jogo seja movida.
    # 'desloc_x' representa o deslocamento horizontal pretendido para a peça.
    # 'desloc_y' representa o deslocamento vertical pretendido para a peça.
    def verificar_colisao(self, desloc_x, desloc_y):
    
        
        # Itera sobre cada linha da matriz que representa a forma da peça atual.
        # A matriz da peça é uma lista de listas onde cada sublista representa uma linha da forma da peça.
        # 'len(self.peca_atual['forma'])' retorna o número de linhas na matriz da peça.
        # O loop 'for' percorre cada uma dessas linhas, representadas pelo índice 'linha'.
        for linha in range(len(self.peca_atual['forma'])):

            # Itera sobre cada coluna na linha atual da matriz da peça.
            # 'self.peca_atual['forma'][0]' é a primeira linha da matriz da peça, e 
            # sua extensão (len) indica o número de colunas.
            # O loop 'for' percorre cada uma dessas colunas na linha atual, 
            # representadas pelo índice 'coluna'.
            for coluna in range(len(self.peca_atual['forma'][0])):

                
                # Verifica se o elemento atual da matriz é um bloco da peça (representado por 1).
                # Dentro da matriz que representa a forma da peça, 
                # '1' indica um bloco ativo (parte da peça) e 
                # '0' indica um espaço vazio.
                if self.peca_atual['forma'][linha][coluna] == 1:
                    
                    # Se o valor na posição atual da matriz for '1', significa que é
                    # um bloco que precisa ser considerado na verificação de colisão.

                    # Calcula a posição 'x' (horizontal) real da peça na grade.
                    # 'self.peca_atual['x']' é a posição horizontal atual da peça na 
                    # grade do jogo, indicando em qual coluna a parte esquerda da peça está localizada.
                    # 'coluna' é o índice da coluna atual na matriz da peça, indicando a
                    # posição do bloco relativo ao lado esquerdo da peça.
                    # 'desloc_x' é o deslocamento horizontal que queremos verificar para a
                    # colisão. Pode ser positivo (para a direita), negativo (para a
                    # esquerda) ou zero (sem movimento horizontal).
                    # Ao somar esses três valores, obtemos a nova posição horizontal 
                    # proposta para este bloco da peça na grade.
                    x = int(self.peca_atual['x']) + coluna + desloc_x

                    # Calcula a posição 'y' (vertical) real da peça na grade.
                    # 'self.peca_atual['y']' é a posição vertical atual da peça na 
                    # grade do jogo, indicando em qual linha a parte superior da
                    # peça está localizada.
                    # 'linha' é o índice da linha atual na matriz da peça, indicando a 
                    # posição do bloco relativo ao topo da peça.
                    # 'desloc_y' é o deslocamento vertical que queremos verificar para 
                    # a colisão. Pode ser positivo (para baixo), negativo (para cima) ou zero (sem movimento vertical).
                    # Ao somar esses três valores, obtemos a nova posição vertical
                    # proposta para este bloco da peça na grade.
                    y = int(self.peca_atual['y']) + linha + desloc_y


                    # Verifica as condições de colisão:
                    # 1. Se 'x' é menor que 0, a peça sairia da grade à esquerda.
                    # 2. Se 'x' é maior ou igual a 'COLUNAS_GRADE', a peça sairia da grade à direita.
                    # 3. Se 'y' é maior ou igual a 'LINHAS_GRADE', a peça atingiria o fundo da grade.
                    # 4. Se 'y' é menor que 0, a peça estaria acima do topo da grade (geralmente
                    # permitido para o início da peça).
                    # 5. Se a posição (y, x) na grade já está ocupada por outra peça (não é 0), há uma colisão.
                    if (x < 0 or x >= COLUNAS_GRADE or
                        y >= LINHAS_GRADE or y < 0 or
                        (y >= 0 and self.grade[y][x] != 0)):
                        
                        # Se qualquer uma dessas condições for verdadeira, uma colisão ocorreu.
                        return True

        # Se o loop termina sem encontrar uma colisão, retorna 
        # False, indicando que não há colisão.
        return False
        
    
    def rotacionar_peca(self):
        
        # Cria uma nova matriz para a forma rotacionada da peça.
        # A nova matriz tem suas dimensões invertidas em relação à matriz original.
        # Se a peça original é 3x2 (3 linhas, 2 colunas), a nova será 2x3.
        # O loop 'for _ in range(len(self.peca_atual['forma'][0]))' determina o número de linhas da nova matriz,
        # que é igual ao número de colunas da matriz original.
        # Cada linha da nova matriz é inicializada com zeros, usando '[0] * len(self.peca_atual['forma'])'.
        # nova_forma = [[0] * len(self.peca_atual['forma']) for _ in range(len(self.peca_atual['forma'][0]))]
        
        # Inicializa 'nova_forma' como uma lista vazia.
        # Esta variável 'nova_forma' será usada para armazenar a forma da peça após ser rotacionada.
        nova_forma = []

        # O loop 'for' itera com base no número de colunas da forma atual da peça.
        # 'len(self.peca_atual['forma'][0])' retorna o número de colunas na primeira linha da forma atual da peça.
        # Isso é usado aqui porque, ao rotacionar a peça, as colunas se tornam linhas.
        for _ in range(len(self.peca_atual['forma'][0])):
            
            # 'nova_forma.append(...)' adiciona uma nova linha à matriz 'nova_forma'.
            # Cada linha é inicializada como uma lista de zeros.

            # '[0] * len(self.peca_atual['forma'])' cria uma lista de zeros.
            # 'len(self.peca_atual['forma'])' retorna o número de linhas na forma atual da peça.
            # Isso é usado aqui porque, ao rotacionar a peça, as linhas se tornam colunas.
            # Por exemplo, se a forma atual tem 3 linhas, isso resultará em 3 zeros em cada nova linha de 'nova_forma'.
            nova_forma.append([0] * len(self.peca_atual['forma']))

        
        # Itera sobre cada linha da matriz que representa a forma da peça atual.
        # Esta matriz é uma lista de listas, onde cada sublista representa uma linha da peça,
        # e cada elemento dentro da sublista representa um bloco (ou a ausência dele) naquela linha específica.
        # 'len(self.peca_atual['forma'])' retorna o número total de linhas na matriz da forma da peça.
        for linha in range(len(self.peca_atual['forma'])):
            
            # Neste loop, 'linha' é um índice que começa em 0 e vai até o número
            # total de linhas na peça, menos um.
            # Cada iteração deste loop representa uma linha diferente na matriz da peça.

            # Itera sobre cada coluna na linha atual da matriz da peça.
            # 'self.peca_atual['forma'][0]' é uma referência à primeira linha da matriz da peça,
            # e 'len(self.peca_atual['forma'][0])' retorna o número total de colunas nessa linha.
            # Supõe-se que todas as linhas na matriz da peça têm o mesmo número de colunas.
            for coluna in range(len(self.peca_atual['forma'][0])):
                
                # Neste loop interno, 'coluna' é um índice que começa em 0 
                
                # Preenche a nova matriz com os valores da matriz original, mas em posições rotacionadas.
                # A posição da linha na matriz original se torna a posição da coluna na nova matriz.
                # 'len(self.peca_atual['forma']) - linha - 1' inverte a ordem das linhas na nova matriz,
                # o que efetua a rotação da peça.
                # O bloco na posição (linha, coluna) na matriz original é movido para a posição
                # (coluna, len(self.peca_atual['forma']) - linha - 1) na nova matriz.
                nova_forma[coluna][len(self.peca_atual['forma']) - linha - 1] = self.peca_atual['forma'][linha][coluna]

        # Atualiza a forma da peça atual para a nova forma rotacionada.
        self.peca_atual['forma'] = nova_forma
        
        
    def desenhar_grade(self):
        
        # Itera sobre cada linha da grade do jogo.
        for linha in range(LINHAS_GRADE):
            
            # Itera sobre cada coluna dentro da linha atual.
            for coluna in range(COLUNAS_GRADE):
                
                # Seleciona a cor para a célula atual.
                # A cor é determinada pelo valor armazenado na grade na posição [linha][coluna].
                # Cada número na grade corresponde a um índice na lista 'CORES', que armazena
                # as cores das peças.
                cor = CORES[self.grade[linha][coluna]]

                # Desenha um retângulo na tela representando a célula da grade.
                # 'pygame.draw.rect' é usado para desenhar um retângulo.
                # 'self.tela' é a superfície na qual o retângulo será desenhado.
                # 'cor' é a cor do retângulo, determinada pela célula atual da grade.
                # O próximo argumento é um tuple que define a posição e o tamanho do retângulo:
                # (coluna * TAMANHO_GRADE, linha * TAMANHO_GRADE) define a posição x e y do retângulo na tela.
                # 'TAMANHO_GRADE' é tanto a largura quanto a altura do retângulo.
                # O último argumento '0' significa que o retângulo é preenchido com a cor.
                pygame.draw.rect(self.tela, cor, 
                                 (coluna * TAMANHO_GRADE, 
                                  linha * TAMANHO_GRADE, 
                                  TAMANHO_GRADE, 
                                  TAMANHO_GRADE), 0)

                # Desenha o contorno de cada célula da grade.
                # Novamente, usa 'pygame.draw.rect' para desenhar um retângulo, mas desta vez é apenas um contorno.
                # 'PRETO' é a cor do contorno.
                # Os argumentos para a posição e tamanho são os mesmos que o retângulo de preenchimento.
                # O último argumento '1' define a espessura da linha do contorno. Neste caso, uma linha de 1 pixel.
                pygame.draw.rect(self.tela, 
                                 PRETO, 
                                 (coluna * TAMANHO_GRADE, 
                                  linha * TAMANHO_GRADE, 
                                  TAMANHO_GRADE, TAMANHO_GRADE), 1)
    
    
    def desenhar_peca(self):
        
        # Itera sobre cada linha da matriz que representa a forma da peça atual.
        # 'self.peca_atual['forma']' é uma matriz de 0s e 1s onde 1 representa um bloco da peça.
        for linha in range(len(self.peca_atual['forma'])):
            
            # Itera sobre cada coluna na linha atual da matriz da peça.
            for coluna in range(len(self.peca_atual['forma'][0])):
                
                # Verifica se o elemento atual na matriz da peça é um bloco (valor 1).
                if self.peca_atual['forma'][linha][coluna] == 1:
                    
                    # Calcula a posição 'x' (horizontal) do bloco na tela.
                    # Comentários detalhados:
                    # 1. 'self.peca_atual['x']' representa a posição horizontal base da peça inteira na grade.
                    #    - É um valor que indica a posição da coluna mais à esquerda da matriz que representa a peça.
                    #    - Esse valor muda conforme o jogador move a peça para a esquerda ou para a direita.

                    # 2. 'coluna' é o índice da coluna atual dentro da matriz que representa a forma da peça.
                    #    - As peças do Tetris são representadas por matrizes de 0s e 1s, onde cada '1' é um bloco da peça.
                    #    - 'coluna' varia de 0 até o número de colunas da matriz da peça (menos 1).

                    # 3. Ao somar 'self.peca_atual['x']' com 'coluna', estamos calculando a posição horizontal exata do bloco na grade.
                    #    - Por exemplo, se a peça está na coluna 5 da grade ('self.peca_atual['x']' é 5) e estamos 
                    # olhando para o segundo bloco da peça ('coluna' é 1), então a posição 'x' do bloco na tela é 6
                    x = int(self.peca_atual['x']) + coluna

                    # Calcula a posição 'y' (vertical) do bloco na tela.
                    # 1. 'self.peca_atual['y']' representa a posição vertical base da peça inteira na grade.
                    #    - É um valor que indica a posição da linha mais alta da matriz que representa a peça.
                    #    - Esse valor aumenta à medida que a peça desce na grade.

                    # 2. 'linha' é o índice da linha atual dentro da matriz que representa a forma da peça.
                    #    - Como a peça é representada por uma matriz, 'linha' varia de 0 até o número de 
                    # linhas da matriz da peça (menos 1).

                    # 3. Ao somar 'self.peca_atual['y']' com 'linha', estamos calculando a posição 
                    # vertical exata do bloco na grade.
                    #    - Por exemplo, se a parte superior da peça está na linha 3 da 
                    # grade ('self.peca_atual['y']' é 3) e estamos olhando para o segundo bloco
                    # da peça ('linha' é 1), então a posição 'y' do bloco na tela é 4.
                    y = int(self.peca_atual['y']) + linha

                    # Seleciona a cor do bloco da peça.
                    # 'self.peca_atual['cor']' contém o índice da cor da peça na lista 'CORES'.
                    cor = CORES[self.peca_atual['cor']]

                    # Desenha o bloco da peça na tela.
                    # 'pygame.draw.rect' é usado para desenhar um retângulo (bloco).
                    # O primeiro argumento é a superfície onde desenhar (neste caso, 'self.tela').
                    # O segundo argumento é a cor do retângulo.
                    # O terceiro argumento é um tuple contendo a posição (x, y) e o tamanho (largura e altura) do retângulo.
                    # O último argumento '0' indica que o retângulo é completamente preenchido com a cor.
                    pygame.draw.rect(self.tela, 
                                     cor, 
                                     (x * TAMANHO_GRADE, 
                                      y * TAMANHO_GRADE, 
                                      TAMANHO_GRADE, 
                                      TAMANHO_GRADE), 0)

                    # Desenha o contorno do bloco.
                    # O contorno é desenhado sobre o retângulo preenchido para melhorar a visualização.
                    # 'PRETO' é a cor do contorno.
                    # Os parâmetros de posição e tamanho são os mesmos do retângulo preenchido.
                    # O último argumento '1' indica a espessura da linha do contorno (1 pixel).
                    pygame.draw.rect(self.tela, 
                                     PRETO, 
                                     (x * TAMANHO_GRADE, 
                                      y * TAMANHO_GRADE, 
                                      TAMANHO_GRADE, 
                                      TAMANHO_GRADE), 1)
                    
    def limpar_linhas(self):
        
        # Inicializa uma lista para armazenar os índices das linhas completas.
        linhas = []

        # Contador para o número de linhas completas encontradas.
        linhas_completas = 0

        # Itera sobre cada linha da grade do jogo.
        for linha in range(LINHAS_GRADE):
            
            # Verifica se todos os blocos na linha atual estão preenchidos (não são 0).
            # A função 'all()' retorna True se todos os elementos na linha são
            # verdadeiros (ou seja, diferentes de 0).
            if all(self.grade[linha]):
                
                # Adiciona o índice da linha completa à lista 'linhas'.
                linhas.append(linha)

                # Incrementa o contador de linhas completas.
                linhas_completas += 1

        # Verifica se alguma linha completa foi encontrada.
        # 'linhas_completas' é um contador que registra o número 
        # total de linhas completas encontradas na grade.
        if linhas_completas > 0:
            
            # Se uma ou mais linhas completas foram encontradas, o código 
            # dentro deste bloco é executado.

            # Reproduz um efeito sonoro para indicar que as linhas foram completadas.
            # 'pygame.mixer.Sound(SOM_PONTO).play()' toca o som armazenado na variável 'SOM_PONTO'.
            # Isso serve como feedback auditivo para o jogador, indicando que
            # ele completou uma ou mais linhas.
            pygame.mixer.Sound(SOM_PONTO).play()

            # Pausa brevemente o jogo para dar um feedback visual ao jogador.
            # 'time.sleep(0.2)' faz o programa esperar por 0.2 segundos (200 milissegundos) antes de continuar.
            # Isso dá ao jogador um momento para reconhecer que completou a(s) linha(s).
            time.sleep(0.2)

        # Itera sobre as linhas completas armazenadas na lista 'linhas'.
        # 'linhas' contém os índices das linhas na grade que foram completadas 
        # e precisam ser removidas.
        for linha in linhas:
            
            # Remove a linha completa da grade.
            # 'del self.grade[linha]' exclui a linha na posição 'linha' da grade.
            # Isso efetivamente remove a linha completa da grade do jogo.
            del self.grade[linha]

            # Insere uma nova linha no topo da grade.
            # 'self.grade.insert(0, [0] * COLUNAS_GRADE)' insere uma nova
            # lista de zeros na primeira posição (índice 0) da grade.
            # '[0] * COLUNAS_GRADE' cria uma lista contendo 'COLUNAS_GRADE' zeros, 
            # representando uma linha vazia.
            # Isso é necessário para manter o tamanho constante da grade após 
            # remover as linhas completas.
            self.grade.insert(0, [0] * COLUNAS_GRADE)

        # Atualiza a pontuação do jogador.
        # 'self.pontuacao += linhas_completas ** 2' aumenta a pontuação do jogador.
        # A pontuação aumenta de acordo com o quadrado do número de linhas completas,
        # incentivando o jogador a completar múltiplas linhas simultaneamente 
        # para obter uma pontuação mais alta.
        self.pontuacao += linhas_completas ** 2
        
        
    def verificar_fim_de_jogo(self):
        
        # Itera sobre cada coluna na primeira linha da grade.
        for coluna in range(COLUNAS_GRADE):
            
            # Verifica se algum bloco na primeira linha da grade (índice 0) não é vazio (diferente de 0).
            # Isso significa que uma nova peça não pode entrar na grade sem colidir com outra peça,
            # indicando o fim do jogo.
            if self.grade[0][coluna] != 0:
                
                # Se um bloco não vazio é encontrado, o jogo termina.
                self.fim_de_jogo = True
                
                # Sai do loop, pois não é necessário verificar mais colunas 
                # uma vez que o fim do jogo foi determinado.
                break
                
                
    def acelerar_queda(self):
        
        # Aumenta a velocidade de queda das peças.
        # Isso é utilizado para aumentar a dificuldade do jogo ou 
        # como uma ação de controle do jogador.
        # O valor 5.0 é significativamente maior que a velocidade
        # normal, fazendo com que as peças caiam mais rápido.
        self.velocidade_queda = 5.0


    def normalizar_queda(self):
        
        # Restaura a velocidade de queda das peças para o valor padrão.
        # Isso é usado para redefinir a velocidade de queda após a 
        # aceleração, mantendo o jogo jogável em um ritmo normal.
        # O valor 0.5 é a velocidade padrão de queda estabelecida no início do jogo.
        self.velocidade_queda = 0.5


    def desenhar_pontuacao(self):
        
        # Renderiza o texto da pontuação atual do jogador.
        # 'FONT.render' cria uma superfície de texto. O primeiro argumento é o texto a ser renderizado.
        # 'True' indica a utilização de anti-aliasing, tornando o texto mais suave.
        # 'BRANCO' é a cor do texto.
        texto = FONT.render(f'Pontuação: {self.pontuacao}', True, BRANCO)

        # Desenha o texto na tela.
        # 'self.tela.blit' desenha a superfície de texto na tela. 
        # O segundo argumento é a posição (x, y) onde o texto será colocado na tela.
        # Neste caso, é colocado próximo ao canto superior esquerdo.
        self.tela.blit(texto, (10, 10))
        
        
    def rodar(self):
        
        # Cria um objeto de relógio para controlar a taxa de 
        # atualizações (frames por segundo) do jogo.
        clock = pygame.time.Clock()

        # Gera uma nova peça no início do jogo.
        self.nova_peca()


        # Loop principal do jogo. Executa enquanto o jogo não 
        # terminar ('self.fim_de_jogo' é False).
        while not self.fim_de_jogo:

            # Itera sobre a fila de eventos do Pygame.
            for evento in pygame.event.get():

                # Verifica se o evento é do tipo QUIT (por exemplo, fechar a janela do jogo).
                if evento.type == pygame.QUIT:

                    # Fecha o Pygame de maneira adequada.
                    pygame.quit()

                    # Encerra o programa.
                    sys.exit()

                # Verifica se algum evento de teclado foi acionado.
                # 'pygame.KEYDOWN' é um tipo de evento que ocorre quando uma tecla é pressionada.
                if evento.type == pygame.KEYDOWN:
                    
                    # Se um evento de tecla pressionada é detectado, o código dentro deste bloco é executado.

                    # Verifica se a tecla pressionada é a seta para esquerda.
                    # 'pygame.K_LEFT' é uma constante no Pygame que representa a tecla de seta para esquerda.
                    if evento.key == pygame.K_LEFT:
                        
                        # Se a tecla de seta para esquerda foi pressionada, o código 
                        # dentro deste bloco é executado.

                        # Verifica se mover a peça para a esquerda (deslocamento horizontal de -1) 
                        # causaria uma colisão.
                        # 'self.verificar_colisao(-1, 0)' verifica se mover a peça uma posição para a
                        # esquerda (-1 no eixo x, 0 no eixo y)
                        # irá resultar em colidir com a borda da grade ou com outras peças já colocadas.
                        if not self.verificar_colisao(-1, 0):
                            
                            # Se não houver colisão ao mover a peça para a esquerda, então o
                            # código dentro deste bloco é executado.

                            # Move a peça atual uma posição para a esquerda.
                            # Decrementa o valor 'x' da posição da peça atual, efetivamente movendo a 
                            # peça uma coluna para a esquerda na grade.
                            # 'self.peca_atual['x']' representa a posição horizontal atual da peça na grade do jogo.
                            self.peca_atual['x'] -= 1


                    # Verifica se a tecla pressionada é a seta para direita.
                    # 'pygame.K_RIGHT' é uma constante no Pygame que representa a
                    # tecla de seta para direita.
                    elif evento.key == pygame.K_RIGHT:
                        
                        # Se a tecla de seta para direita foi pressionada, o código dentro
                        # deste bloco é executado.

                        # Verifica se mover a peça uma posição para a direita (deslocamento
                        # horizontal de 1) causaria uma colisão.
                        # 'self.verificar_colisao(1, 0)' verifica se mover a peça para a 
                        # direita resultará em colisão.
                        if not self.verificar_colisao(1, 0):
                            
                            # Se não houver colisão ao mover a peça para a direita, o 
                            # código dentro deste bloco é executado.

                            # Move a peça atual uma posição para a direita.
                            # Incrementa o valor 'x' da posição da peça atual, movendo-a 
                            # uma coluna para a direita na grade.
                            self.peca_atual['x'] += 1


                    # Verifica se a tecla pressionada é a seta para baixo.
                    # 'pygame.K_DOWN' é uma constante no Pygame que representa a 
                    # tecla de seta para baixo.
                    elif evento.key == pygame.K_DOWN:
                        
                        # Se a tecla de seta para baixo foi pressionada, o código 
                        # dentro deste bloco é executado.

                        # Enquanto mover a peça uma posição para baixo (deslocamento
                        # vertical de 1) não causar uma colisão.
                        # O loop continua movendo a peça para baixo até encontrar uma colisão.
                        while not self.verificar_colisao(0, 1):
                            
                            # Incrementa o valor 'y' da posição da peça atual, movendo-a 
                            # rapidamente para baixo na grade.
                            self.peca_atual['y'] += 1


                    # Verifica se a tecla pressionada é a seta para cima.
                    # 'pygame.K_UP' é uma constante no Pygame que representa a 
                    # tecla de seta para cima.
                    elif evento.key == pygame.K_UP:
                    
                        # Se a tecla de seta para cima foi pressionada, o código 
                        # dentro deste bloco é executado.

                        # Chama o método 'self.rotacionar_peca()' para rotacionar a peça atual.
                        # Este método altera a orientação da peça, o que é uma parte 
                        # fundamental da jogabilidade do Tetris.
                        self.rotacionar_peca()
                        
                        
            # Verifica se mover a peça atual uma posição para baixo na grade causaria uma colisão.
            # A função 'self.verificar_colisao(0, 1)' é chamada com dois 
            # parâmetros: deslocamento horizontal (0) e deslocamento vertical (1).
            # O deslocamento horizontal de '0' significa que não estamos movendo
            # a peça para a esquerda ou direita.
            # O deslocamento vertical de '1' significa que estamos tentando mover 
            # a peça uma posição para baixo na grade.
            # Esta função retorna True se tal movimento resultar em uma colisão 
            # com outras peças fixadas na grade ou com as bordas da grade.
            if not self.verificar_colisao(0, 1):
                
                # Se a função 'self.verificar_colisao' retornar False, significa que
                # não há colisão ao mover a peça para baixo.
                # Ou seja, é seguro mover a peça uma posição para baixo.

                # Aumenta a posição 'y' da peça atual.
                # 'self.peca_atual['y']' representa a posição vertical atual da peça na grade.
                # Ao incrementar 'self.peca_atual['y']', estamos movendo a peça uma posição 
                # para baixo na grade.
                self.peca_atual['y'] += 1

            else:
                
                # Se a função 'self.verificar_colisao' retornar True, significa que
                # há uma colisão ao tentar mover a peça para baixo.
                # Neste caso, o código que segue esse bloco será executado, 
                # geralmente tratando de fixar a peça na sua posição atual na grade
                # e gerando uma nova peça para continuar o jogo.


                # Se houver uma colisão ao tentar mover a peça para baixo, significa que a peça
                # atingiu o fundo da grade ou outra peça.
                # Neste caso, o código abaixo é executado para fixar a peça na grade.

                # Itera sobre cada linha da matriz que representa a forma da peça atual.
                # A matriz 'self.peca_atual['forma']' é uma lista de listas, onde cada 
                # sublista representa uma linha da peça,
                # e os elementos dentro de cada sublista representam os blocos ou 
                # espaços vazios dessa linha.
                for linha in range(len(self.peca_atual['forma'])):
                    
                    # 'linha' é o índice da linha atual na matriz da forma da peça.
                    # Este loop permite acessar cada linha da peça.

                    # Itera sobre cada coluna na linha atual da matriz da peça.
                    # 'len(self.peca_atual['forma'][0])' retorna o número de colunas na peça,
                    # assumindo que todas as linhas da peça têm o mesmo número de colunas.
                    for coluna in range(len(self.peca_atual['forma'][0])):
                        
                        # 'coluna' é o índice da coluna atual na linha da matriz da peça.
                        # Este loop interno permite acessar cada bloco (ou espaço vazio) na linha atual da peça.

                        # Verifica se o elemento atual na matriz da peça é um bloco (valor 1).
                        if self.peca_atual['forma'][linha][coluna] == 1:
                            
                            # Se o valor for 1, o código dentro deste bloco é executado,
                            # significando que esta posição na matriz é um bloco da peça e 
                            # precisa ser fixado na grade.

                            # Calcula a posição final 'x' e 'y' do bloco na grade.
                            # A posição 'x' é calculada somando a posição horizontal base da peça ('self.peca_atual['x']')
                            # com o índice da coluna atual. Similarmente, a posição 'y' é calculada somando a posição
                            # vertical base da peça ('self.peca_atual['y']') com o índice da linha atual.
                            x = int(self.peca_atual['x']) + coluna
                            y = int(self.peca_atual['y']) + linha

                            # Atualiza a célula correspondente na grade com o índice de cor da peça atual.
                            # 'self.grade[y][x] = self.peca_atual['cor']' coloca o índice de cor da peça na 
                            # posição calculada na grade,
                            # efetivamente fixando o bloco da peça naquela posição da grade.
                            self.grade[y][x] = self.peca_atual['cor']


                # Chama o método para verificar e limpar linhas completas.
                self.limpar_linhas()

                # Gera uma nova peça para continuar o jogo.
                self.nova_peca()

                # Verifica se a nova peça colide com blocos na posição inicial, o que

                # Verifica se o jogo terminou. Essa verificação ocorre após a
                # fixação de uma peça na grade.
                self.verificar_fim_de_jogo()

                # Verifica se há uma colisão na posição inicial da nova peça.
                # Isso acontece imediatamente após uma nova peça ser gerada.
                if self.verificar_colisao(0, 0):

                    # Se houver uma colisão na posição inicial, o jogo termina.
                    # Isso geralmente significa que não há mais espaço para novas peças, pois a grade está cheia.
                    self.fim_de_jogo = True                    
                        
                        
            # Preenche a tela com a cor branca.
            # Isso limpa a tela antes de desenhar os novos elementos do jogo,
            # evitando sobreposição de imagens.
            self.tela.fill(BRANCO)

            # Chama o método para desenhar a grade do jogo.
            # Esse método desenha as células da grade e as peças já fixadas nela.
            self.desenhar_grade()

            # Chama o método para desenhar a peça atual que está sendo controlada pelo jogador.
            self.desenhar_peca()

            # Chama o método para desenhar a pontuação atual do jogador na tela.
            self.desenhar_pontuacao()

            # Atualiza a tela inteira para refletir as mudanças feitas nos métodos de desenho.
            # Isso inclui a grade atualizada, a peça atual, e a pontuação.
            pygame.display.update()

            # Controla a velocidade do loop do jogo.
            # 'clock.tick(1)' limita o loop a rodar apenas 1 vez por segundo, o que 
            # controla a velocidade de queda das peças.
            clock.tick(1)

        # Fecha e limpa todos os módulos do Pygame.
        # É importante chamar esta função ao encerrar um programa Pygame para 
        # garantir que todos os recursos do Pygame sejam liberados corretamente.
        pygame.quit()

        # Encerra o programa.
        # 'sys.exit()' é usado para sair do programa de maneira limpa, encerrando o 
        # processo Python.
        sys.exit()
        
        
# Verifica se este script está sendo executado como o programa principal.
# '__name__' é uma variável especial em Python que é definida como '__main__' 
# quando o script é executado diretamente.
# Isso não acontecerá se o script for importado como um módulo em outro
# script. Nesse caso, '__name__' terá um valor diferente.
if __name__ == "__main__":
    
    # Este bloco de código só será executado se o script estiver sendo executado diretamente.
    # Isso é útil para prevenir a execução automática do jogo quando o script é importado como um módulo.

    # Cria uma instância da classe Tetris.
    # 'Tetris()' é o construtor da classe Tetris, que inicializa um novo jogo Tetris.
    # Isso inclui configurar a janela do jogo, inicializar variáveis, e preparar a grade de jogo.
    tetris = Tetris()

    # Chama o método 'rodar' do objeto 'tetris'.
    # Este método inicia o loop principal do jogo, onde toda a lógica do jogo acontece.
    # Isso inclui lidar com entrada do usuário, movimentar e rotacionar as
    # peças, verificar por linhas completas, e atualizar a tela.
    tetris.rodar()
    