"""
Gráficos em PyGame

    - Animações: Mover objetos, animação de quadros (sprites).
"""

# Pygame para a parte gráfica e de animação 
import pygame

# Inicializamos o pygame
pygame.init()

# Definimos as dimensões da janela
largura_tela, altura_tela = 800, 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Definimos as cores
PRETO = (0, 0, 0)

# Bloco de configurações da animação do sprite

# Define o tamanho de cada quadro (frame) do sprite como uma largura
# de 64 pixels e altura de 64 pixels.
tamanho_quadro = (64, 64) 

# Caminho do arquivo para o primeiro quadro da animação do sprite. 
# Substitua 'Passaro1.png' pelo caminho correto onde a primeira imagem
# do sprite está armazenada.
caminho_imagem_1 = 'Passaro1.png'

# Caminho do arquivo para o segundo quadro da animação do sprite. 
# Substitua 'Passaro2.png' pelo caminho correto onde a segunda imagem 
# do sprite está armazenada.
caminho_imagem_2 = 'Passaro2.png'

# Carrega o primeiro quadro da imagem, redimensionando-o para o tamanho de quadro especificado acima.
quadro_1 = pygame.transform.scale(pygame.image.load(caminho_imagem_1), tamanho_quadro)

# Carrega o segundo quadro da imagem, também redimensionando-o para o mesmo tamanho de quadro.
quadro_2 = pygame.transform.scale(pygame.image.load(caminho_imagem_2), tamanho_quadro)

# Cria uma lista contendo ambos os quadros carregados e redimensionados 
# para facilitar a alternância entre eles durante a animação.
quadros = [quadro_1, quadro_2]

# Inicializa o índice do quadro atual como 0, o que indica que o primeiro 
# quadro na lista `quadros` será exibido primeiro.
indice_quadro_atual = 0

# Define o intervalo de tempo em milissegundos que cada quadro permanecerá 
# visível antes de alternar para o próximo.
tempo_mudanca_quadro = 500

# Armazena o tempo atual em milissegundos desde que o pygame foi 
# inicializado, usado para controlar quando os quadros devem ser alternados.
ultimo_mudanca = pygame.time.get_ticks()


# Posição inicial do sprite
# Define um vetor com duas posições, onde '100' é a posição
# horizontal (eixo x) e '300' é a posição vertical (eixo y).
sprite_posicao = [100, 300]

# Definimos uma velocidade para o movimento do sprite
# Define um vetor de velocidade, onde '2' é a velocidade 
# horizontal (movimento ao longo do eixo x) e '0' é a velocidade 
# vertical (sem movimento no eixo y).
sprite_velocidade = [2, 0]

# Inicializa o loop principal do jogo
# Define a variável 'executando' como True para iniciar o loop do jogo.
executando = True

# Este é o loop principal do jogo, que continuará executando
# enquanto a variável 'executando' for verdadeira.
while executando:
    
    # Verifica a fila de eventos do pygame
    # Percorre todos os eventos que o pygame detectou, como
    # pressionamentos de tecla, movimentos do mouse, etc.
    for evento in pygame.event.get():
        
        # Verifica se o evento atual é um pedido para sair do jogo
        # Se o evento for do tipo QUIT (geralmente o evento de fechar
        # a janela), então define a variável 'executando' como False.
        if evento.type == pygame.QUIT:
            
            # Sai do loop, efetivamente terminando o jogo.
            executando = False


    # Atualiza a posição do sprite
    # Adiciona a velocidade horizontal atual (sprite_velocidade[0]) à
    # posição horizontal do sprite (sprite_posicao[0]), o que causa o 
    # movimento do sprite na tela.
    sprite_posicao[0] += sprite_velocidade[0]

    # Condicional que verifica se o sprite atingiu os limites horizontais da tela
    """
        - sprite_posicao[0]: Este é um acesso ao primeiro elemento da lista 
        sprite_posicao, que representa a coordenada x (horizontal) da 
        posição atual do sprite na tela.

        - <= 0: Esta expressão verifica se a coordenada x do sprite
        é menor ou igual a zero. Se for, significa que o sprite atingiu
        ou ultrapassou a borda esquerda da janela do jogo.

        - or: É um operador lógico que permite combinar duas expressões
        booleanas. Se pelo menos uma das expressões for verdadeira, toda a
        condição avaliada pelo if será considerada verdadeira.

        - sprite_posicao[0] + tamanho_quadro[0]: Aqui adiciona-se a 
        largura do sprite (primeiro elemento da tupla tamanho_quadro, que
        guarda a largura e altura do sprite) à sua posição x atual. Isso representa o ponto mais à direita do sprite.

        - >= largura_tela: Esta expressão verifica se o ponto mais à 
        direita do sprite é maior ou igual à largura total da 
        tela (ou janela do jogo). Se for, significa que o sprite atingiu
        ou ultrapassou a borda direita da janela do jogo.
    """
    if sprite_posicao[0] <= 0 or sprite_posicao[0] + tamanho_quadro[0] >= largura_tela:
        sprite_velocidade[0] *= -1  # Multiplica a velocidade horizontal por -1, invertendo a direção do movimento do sprite.

    # Atualiza o quadro do sprite baseado no tempo
    # Obtém o tempo atual em milissegundos desde que o pygame foi inicializado com pygame.time.get_ticks().
    tempo_atual = pygame.time.get_ticks()

    # Verifica se o tempo transcorrido desde a última mudança de 
    # quadro (último_mudanca) é maior que o tempo definido para mudar de quadro (tempo_mudanca_quadro).
    # Se sim, significa que é hora de mudar para o próximo quadro da animação do sprite.
    if tempo_atual - ultimo_mudanca > tempo_mudanca_quadro:
        
        # Atualiza o índice para o próximo quadro. O operador % (módulo) garante 
        # que o índice volte a 0 após atingir o fim da lista de quadros,
        # criando um loop contínuo na animação do sprite.
        indice_quadro_atual = (indice_quadro_atual + 1) % len(quadros)
        
        # Atualiza o momento da última mudança de quadro para o tempo atual, para
        # que o intervalo possa ser verificado novamente a partir de agora.
        ultimo_mudanca = tempo_atual


    # Preenche toda a tela com a cor preta, que é definida pela constante PRETO.
    # Este preenchimento é feito para "limpar" a tela antes de desenhar a próxima cena.
    # Isso evita o rastro de imagens anteriores permanecendo na tela.
    tela.fill(PRETO)

    # Desenha o quadro atual do sprite na posição especificada pela lista sprite_posicao.
    # tela.blit() é uma função que desenha uma imagem sobre outra.
    # quadros[indice_quadro_atual] acessa a lista de quadros do sprite e obtém o quadro atual,
    # o qual é determinado pela variável indice_quadro_atual.
    # sprite_posicao é uma lista que contém as coordenadas x e y onde o sprite será desenhado.
    tela.blit(quadros[indice_quadro_atual], sprite_posicao)

    # Atualiza o conteúdo da tela inteira.
    # pygame.display.flip() muda os buffers, o que significa que tudo o que foi desenhado
    # desde a última chamada será exibido na tela.
    # Isso é o que efetivamente faz as imagens aparecerem na tela.
    pygame.display.flip()

    # Limita a taxa de atualização do jogo a 60 quadros por segundo (fps).
    # pygame.time.Clock().tick(60) é usado para garantir que o jogo não execute mais rápido
    # do que 60 quadros por segundo. Isso é importante para manter o jogo rodando
    # de maneira consistente em diferentes sistemas e também ajuda a controlar a física do jogo,
    # caso ela dependa da taxa de quadros para os cálculos.
    pygame.time.Clock().tick(60)


# Encerra o pygame
pygame.quit()