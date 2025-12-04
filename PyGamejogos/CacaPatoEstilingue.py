# Importa o módulo Pygame, usado para gráficos e 
        # controle de eventos do jogo
import pygame

# Importa o módulo random, usado para gerar números
        # aleatórios, como a posição inicial do pato
import random

# Importa o módulo sys, necessário para encerrar o
        # jogo corretamente ao fechar a janela
import sys

# Importa o módulo math, usado para cálculos matemáticos, 
        # como a potência do lançamento da bola
import math

# Inicializando o Pygame
# Esta linha inicia todos os módulos do Pygame, 
        # preparando o ambiente para o jogo
pygame.init()

# Configurações da tela
# Define a largura e altura da tela do jogo
LARGURA, ALTURA = 400, 600

# Cria a tela de jogo com as dimensões definidas (LARGURA x ALTURA)
# 'pygame.display.set_mode' cria a superfície
        # onde o jogo será renderizado
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela do jogo
pygame.display.set_caption("Caça ao Pato com Estilingue")

# Carregando a imagem do fundo
# Carrega a imagem de fundo a partir do arquivo 'fundo.png'
imagem_fundo = pygame.image.load('fundo.png')  # Plano de fundo do jogo

# Redimensiona a imagem de fundo para que ocupe toda a tela
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

# Carregando as imagens do pato e da bola
# Carrega a primeira imagem do pato voando (para 
        # simular o bater de asas)
imagem_pato1 = pygame.image.load('pato_voando1.png')

# Redimensiona a imagem do pato para 60x60 pixels
imagem_pato1 = pygame.transform.scale(imagem_pato1, (60, 60))

# Carrega a segunda imagem do pato (para alternar entre as 
        # imagens e criar um efeito de asas batendo)
imagem_pato2 = pygame.image.load('pato_voando2.png')

# Redimensiona a segunda imagem do pato para 60x60 pixels
imagem_pato2 = pygame.transform.scale(imagem_pato2, (60, 60))

# Carrega a imagem da bola do estilingue
imagem_bola = pygame.image.load('bola.png')

# Redimensiona a imagem da bola para 40x40 pixels
imagem_bola = pygame.transform.scale(imagem_bola, (40, 40))

# Cores
# Define a cor preta para uso em textos e elementos visuais
PRETO = (0, 0, 0)

# Define a cor vermelha para uso no estilingue e 
        # outras indicações visuais
VERMELHO = (255, 0, 0)

# Fonte
# Define a fonte padrão para o texto com tamanho 30
fonte = pygame.font.Font(None, 30)

# Define a fonte para o texto do menu com tamanho 40
fonte_menu = pygame.font.Font(None, 40)

# Variáveis do jogo
# Define a posição inicial do pato à direita da tela, 
        # com altura aleatória
# O pato começa na borda direita e em uma altura aleatória
        # entre 50 e metade da altura da tela
posicao_pato = [LARGURA, random.randint(50, ALTURA // 2)]

# Define a direção do pato como -1, movendo-o da 
        # direita para a esquerda
direcao_pato = -1

# Define a velocidade do pato para 3 pixels por frame,
        # controlando a rapidez com que ele voa
velocidade_pato = 3

# Define a imagem atual do pato, inicializada com a 
        # primeira imagem
imagem_atual_pato = imagem_pato1

# Inicializa o contador de asas do pato, usado para
        # alternar entre as imagens e simular o bater de asas
contador_asa = 0  # Controla o bater de asas do pato

# Variáveis da bola
# Cria uma lista para armazenar as bolas 
        # disparadas pelo estilingue
bolas = []

# Define a posição inicial da bola no centro horizontal
        # da tela, com altura ajustada para o estilingue
posicao_inicial_bola = (LARGURA // 2, ALTURA - 140)

# Variável para controlar se o jogador está puxando o
        # estilingue (definindo potência de lançamento)
carregando_potencia = False

# Inicializa a direção do lançamento da bola como uma 
        # lista [0, 0], que será calculada posteriormente
direcao_lancamento = [0, 0]  # Direção calculada do lançamento

# Pontuação
# Inicializa a pontuação atual do jogador com zero
pontuacao = 0

# Inicializa a pontuação acumulada, que mantém o total 
        # de pontos ao longo dos jogos
pontuacao_acumulada = 0  # Pontuação acumulada ao longo dos jogos

# Variável para verificar se o jogador clicou errado (não 
        # acertou o pato), usada para determinar o fim do jogo
clicou_errado = False

# Função para exibir texto
# Esta função renderiza e exibe o texto na tela
        # do jogo, em uma posição específica.
# É usada para mostrar informações como
        # pontuação e instruções ao jogador.
def mostrar_texto(texto, fonte, cor, x, y):
    
    # Renderiza o texto, criando uma superfície de 
            # texto que pode ser desenhada na tela.
    # - 'texto' é o conteúdo textual que será exibido.
    # - 'True' ativa o antialiasing (suavização das bordas do texto).
    # - 'cor' define a cor do texto.
    superficie_texto = fonte.render(texto, True, cor)
    
    # Desenha a superfície de texto na tela, na
            # posição (x, y) especificada.
    # Isso torna o texto visível no local desejado.
    tela.blit(superficie_texto, (x, y))

# Função para carregar a pontuação acumulada
# Esta função lê a pontuação acumulada do jogador a 
        # partir de um arquivo.
# A pontuação acumulada permite ao jogador acompanhar
        # seu progresso ao longo das partidas.
def carregar_pontuacao_acumulada():
    
    # Tenta abrir o arquivo 'pontuacao.txt' em modo de 
            # leitura para obter a pontuação anterior.
    try:
        
        with open("pontuacao.txt", "r") as arquivo:
            
            # Lê a primeira linha do arquivo, remove espaços
                    # extras e converte para um número inteiro.
            # Retorna a pontuação lida para uso no jogo.
            return int(arquivo.readline().strip())
            
    # Se houver qualquer erro (por exemplo, o arquivo não 
            # existir), retorna 0 como pontuação inicial.
    except:
        return 0

# Função para salvar pontuação acumulada
# Esta função salva a pontuação acumulada no arquivo, 
        # somando a nova pontuação à pontuação total.
def salvar_pontuacao_acumulada(pontuacao):
    
    # Declara a variável 'pontuacao_acumulada' como 
            # global para que possamos modificá-la.
    global pontuacao_acumulada
    
    # Adiciona a pontuação atual à pontuação acumulada, 
            # atualizando o total de pontos.
    pontuacao_acumulada += pontuacao
    
    # Abre o arquivo 'pontuacao.txt' em modo de escrita, 
            # para salvar a pontuação atualizada.
    with open("pontuacao.txt", "w") as arquivo:
        
        # Escreve a pontuação acumulada no arquivo como uma string.
        arquivo.write(str(pontuacao_acumulada))


# Tela inicial com instruções e pontuação
# Esta função exibe a tela inicial do jogo, mostrando o
                # título, instruções, e a pontuação acumulada.
# O jogo só começa quando o jogador clica na tela.
def tela_inicial():
    
    # Desenha a imagem de fundo na tela, preenchendo a
            # área visível com a imagem.
    tela.blit(imagem_fundo, (0, 0))
    
    # Exibe o título do jogo, "Caça ao Pato!", no
            # centro da tela.
    # A posição é calculada para centralizar o texto 
            # horizontalmente e posicioná-lo no terço superior.
    mostrar_texto("Caça ao Pato!", fonte_menu, PRETO, LARGURA // 2 - 150, ALTURA // 2 - 150)
    
    # Exibe a pontuação acumulada na tela, mostrando o total de
            # pontos que o jogador acumulou em todas as partidas.
    mostrar_texto(f"Pontuação Acumulada: {pontuacao_acumulada}", fonte, PRETO, LARGURA // 2 - 120, ALTURA // 2 - 100)
    
    # Exibe uma instrução sobre o uso do estilingue para lançar a bola.
    mostrar_texto("Use o estilingue para lançar.", fonte, PRETO, LARGURA // 2 - 120, ALTURA // 2 - 50)
    
    # Exibe o texto "Clique para iniciar", instruindo o
            # jogador a clicar para começar o jogo.
    mostrar_texto("Clique para iniciar", fonte_menu, PRETO, LARGURA // 2 - 90, ALTURA // 2 + 80)
    
    # Atualiza a tela para exibir todas as mudanças 
            # feitas (fundo, título, pontuação, instruções).
    pygame.display.flip()
    
    # Define a variável 'aguardando' como True para iniciar o loop de espera.
    # Este loop fica ativo até que o jogador clique para iniciar o jogo.
    aguardando = True
    while aguardando:
        
        # Percorre todos os eventos do Pygame, verificando 
                # as ações do jogador.
        for evento in pygame.event.get():
            
            # Verifica se o jogador fechou a janela do jogo.
            if evento.type == pygame.QUIT:
                
                pygame.quit()  # Encerra o Pygame
                sys.exit()     # Encerra o programa completamente
            
            # Verifica se o jogador clicou com o mouse.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Se o mouse foi clicado, define 'aguardando' 
                        # como False, saindo do loop.
                # Isso permite que o jogo comece após o clique.
                aguardando = False


# Função para movimentar o pato e alternar asas
# Esta função move o pato para a esquerda e alterna a 
        # imagem do pato para simular o movimento das asas.
def mover_pato():
    
    # Declara as variáveis como globais para que possam ser
            # modificadas dentro da função.
    # 'posicao_pato' controla a posição do pato,
    # 'imagem_atual_pato' armazena a imagem do pato atualmente exibida,
    # 'contador_asa' conta os frames para alternar as asas.
    global posicao_pato, imagem_atual_pato, contador_asa

    # Atualiza a posição horizontal do pato (posicao_pato[0])
            # multiplicando a direção (-1) pela velocidade do 
            # pato (velocidade_pato). A cada frame, o pato se move para a esquerda.
    posicao_pato[0] += direcao_pato * velocidade_pato
    
    # Alternar imagem do pato para bater asas a cada 15 frames
    # Incrementa o contador de asas em 1 a cada frame para 
            # contar o tempo de alternância das asas.
    contador_asa += 1
    
    # Verifica se o contador de asas atingiu 15, o que controla a
            # frequência da troca de imagens.
    # A cada 15 frames, a imagem do pato é alternada para
            # criar o efeito de asas batendo.
    if contador_asa >= 15:  # Ajuste o valor para controlar a
                            # velocidade do bater de asas
        
        # Alterna a imagem do pato: se a imagem atual é 'imagem_pato1', 
                # muda para 'imagem_pato2', e vice-versa.
        # Isso cria o efeito de "bater asas".
        imagem_atual_pato = imagem_pato1 if imagem_atual_pato == imagem_pato2 else imagem_pato2
        
        # Reseta o contador de asas para 0, para que a
                # contagem de 15 frames reinicie.
        contador_asa = 0
    
    # Resetar a posição do pato se sair da tela
    # Verifica se o pato saiu da tela pela esquerda, ou seja, 
            # se a posição X dele é menor que -60 pixels.
    # O valor -60 é usado porque o pato tem largura 60, então 
            # ele é considerado "fora da tela" ao passar por -60.
    if posicao_pato[0] < -60:
        
        # Redefine a posição X do pato para o lado direito da
                # tela (LARGURA), fazendo-o reaparecer na direita.
        posicao_pato[0] = LARGURA
        
        # Define uma nova posição Y aleatória para o pato,
                # entre 50 e metade da altura da tela,
                # fazendo com que ele reapareça em uma altura 
                # diferente quando volta pela direita.
        posicao_pato[1] = random.randint(50, ALTURA // 2)


# Função para atualizar e lançar bolas
# Esta função atualiza a posição das bolas lançadas, 
        # verifica colisões com o pato,
        # e gerencia a pontuação e o estado do
        # jogo se a bola acertar ou errar o alvo.
def atualizar_bolas():
    
    # Declara as variáveis 'pontuacao' e 'clicou_errado' como globais,
    # pois elas serão atualizadas dentro da função.
    global pontuacao, clicou_errado
    
    # Cria um retângulo para o pato com base na sua 
            # posição e no tamanho da imagem (60x60).
    # Isso é feito para facilitar a verificação de
            # colisão com as bolas.
    retangulo_pato = pygame.Rect(posicao_pato[0], posicao_pato[1], 60, 60)
    
    # Percorre a lista 'bolas' para atualizar a posição 
            # de cada bola e verificar colisões.
    # 'bolas[:]' cria uma cópia da lista, permitindo a
            # remoção segura de itens enquanto itera.
    for bola in bolas[:]:
        
        # Atualiza a posição X da bola com base em sua 
                # velocidade horizontal (bola[2]),
                # movendo a bola em direção ao alvo.
        bola[0] += bola[2]
        
        # Atualiza a posição Y da bola com base em sua 
                # velocidade vertical (bola[3]),
                # permitindo que a bola siga uma 
                # trajetória específica.
        bola[1] += bola[3]
        
        # Cria um retângulo ao redor da bola para facilitar a
                # verificação de colisão com o pato.
        # O retângulo tem o tamanho da bola (40x40), 
                # baseado em sua posição atual.
        retangulo_bola = pygame.Rect(bola[0], bola[1], 40, 40)
        
        # Verificar se a bola colidiu com o pato
        # 'colliderect' retorna True se o retângulo do 
                # pato colide com o retângulo da bola.
        if retangulo_pato.colliderect(retangulo_bola):
            
            # Aumenta a pontuação em 1 ao acertar o pato.
            pontuacao += 1
            
            # Chama a função para salvar a pontuação acumulada, 
                    # somando 1 ao total.
            salvar_pontuacao_acumulada(1)
            
            # Remove a bola da lista, pois ela já atingiu o alvo e
                    # não precisa mais ser renderizada.
            bolas.remove(bola)
            
            # Reinicia a posição do pato fora da tela, à direita,
                    # para que ele reapareça como novo alvo.
            posicao_pato[0] = LARGURA
            
            # Define uma nova posição Y aleatória para o pato, 
                    # variando entre 50 e metade da altura da tela.
            # Isso cria um novo desafio, pois o pato reaparece 
                    # em uma altura diferente.
            posicao_pato[1] = random.randint(50, ALTURA // 2)
        
        # Remover bola se sair da tela
        # Verifica se a bola ultrapassou os limites da tela. Se sair 
                # pelos lados ou pela parte superior/inferior:
        elif bola[0] < 0 or bola[0] > LARGURA or bola[1] < 0 or bola[1] > ALTURA:
            
            # Remove a bola da lista, pois ela saiu da área de jogo.
            bolas.remove(bola)
            
            # Define 'clicou_errado' como True, indicando que o 
                    # jogador errou o alvo,
            # o que pode levar ao fim do jogo dependendo da lógica geral.
            clicou_errado = True  # Errou o tiro e perde o jogo


# Função principal do jogo
# Esta função controla o loop principal do jogo, incluindo o
        # movimento do pato, o lançamento das bolas,
        # a exibição da pontuação e o desenho de elementos
        # visuais, como o estilingue e a bola.
def jogo():
    
    # Declaração das variáveis como globais para que possam
            # ser modificadas dentro da função.
    # 'posicao_pato' controla a posição do pato.
    # 'pontuacao' armazena a pontuação atual do jogador.
    # 'clicou_errado' sinaliza se o jogador errou um tiro.
    # 'carregando_potencia' controla o estado do estilingue (puxando ou não).
    # 'direcao_lancamento' define a direção do lançamento da bola.
    global posicao_pato, pontuacao, clicou_errado, carregando_potencia, direcao_lancamento
    
    # Define a variável 'rodando' como True para manter o 
            # loop principal do jogo ativo.
    rodando = True
    
    # Loop principal do jogo
    # Este loop continua enquanto 'rodando' for True, atualizando e
            # desenhando todos os elementos do jogo.
    while rodando:
        
        # Desenha a imagem de fundo na tela, cobrindo tudo o que
                # foi desenhado anteriormente.
        # Isso cria uma nova tela "limpa" para o próximo quadro do jogo.
        tela.blit(imagem_fundo, (0, 0))
        
        # Exibindo a pontuação
        # Chama a função 'mostrar_texto' para exibir a pontuação
                # atual no canto superior esquerdo da tela.
        mostrar_texto(f"Pontuação: {pontuacao}", fonte, PRETO, 10, 10)
        
        # Movimentação do pato e bolas
        # Chama a função 'mover_pato' para atualizar a posição do
                # pato e alternar a imagem dele.
        mover_pato()
        
        # Desenha a imagem atual do pato na tela na
                # posição especificada.
        # 'imagem_atual_pato' alterna entre as duas imagens, 
                # simulando o movimento de bater asas.
        tela.blit(imagem_atual_pato, posicao_pato)
        
        # Percorre cada bola na lista 'bolas' e desenha na 
                # tela nas coordenadas (x, y) da bola.
        # 'bola[:2]' extrai as duas primeiras coordenadas da 
                # bola (x e y) para posicioná-la corretamente.
        for bola in bolas:

            # Desenhar a bola nas posições x, y
            tela.blit(imagem_bola, bola[:2])  
        
        # Chama a função 'atualizar_bolas' para atualizar a 
                # posição das bolas e verificar colisões com o pato.
        atualizar_bolas()

        # Desenhar linha do estilingue quando o jogador está puxando
        # Verifica se o jogador está puxando o estilingue para 
                # carregar o lançamento da bola.
        if carregando_potencia:
            
            # Obtém a posição atual do mouse para desenhar a
                    # linha do estilingue.
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            # Desenha uma linha vermelha entre a posição inicial 
                    # da bola e a posição atual do mouse,
            # representando a direção e a potência do lançamento.
            pygame.draw.line(tela, VERMELHO, posicao_inicial_bola, (mouse_x, mouse_y), 5)
        
        # Desenhar a bola na posição inicial
        # Desenha a bola na posição inicial do estilingue, 
                # independentemente de estar sendo puxada ou não.
        # Isso exibe a bola pronta para ser lançada antes do 
                # jogador puxar o estilingue.
        tela.blit(imagem_bola, posicao_inicial_bola)


        # Loop de eventos
        # Este loop captura e processa todos os eventos de entrada do 
                # usuário, como clicar ou soltar o mouse.
        for evento in pygame.event.get():
            
            # Verifica se o jogador fechou a janela do jogo.
            if evento.type == pygame.QUIT:
                
                # Encerra o Pygame e fecha o programa.
                pygame.quit()
                sys.exit()
            
            # Verifica se o jogador pressionou o botão do 
                    # mouse (início do estilingue).
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Define 'carregando_potencia' como True, indicando que o
                        # jogador está puxando o estilingue
                        # para lançar a bola com uma certa potência.
                carregando_potencia = True
            
            # Verifica se o jogador soltou o botão do
                    # mouse (lançamento do estilingue).
            elif evento.type == pygame.MOUSEBUTTONUP:
                
                # Verifica se o estilingue estava sendo carregado 
                        # quando o botão foi solto.
                if carregando_potencia:
                    
                    # Obtém a posição atual do mouse (posição 
                            # onde o botão foi solto).
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    # Calcula a diferença horizontal (dx) e vertical (dy)
                            # entre a posição inicial da bola
                            # e a posição onde o botão do mouse foi solto.
                    dx = posicao_inicial_bola[0] - mouse_x
                    dy = posicao_inicial_bola[1] - mouse_y
                    
                    # Calcula a distância entre a posição inicial da 
                            # bola e a posição onde o mouse foi solto.
                    # A distância é usada para determinar a potência do lançamento.
                    distancia = math.sqrt(dx**2 + dy**2)
                    
                    # Define a potência do lançamento dividindo a distância por 10.
                    # A função min() limita a potência máxima a 20 para 
                            # evitar lançamentos muito fortes.
                    potencia = min(distancia / 10, 20)
                    
                    # Calcula a direção horizontal (direcao_x) da bola, 
                            # ajustada pela potência.
                    direcao_x = (dx / distancia) * potencia
                    
                    # Calcula a direção vertical (direcao_y) da bola,
                            # ajustada pela potência.
                    direcao_y = (dy / distancia) * potencia
                    
                    # Adiciona a bola à lista 'bolas' com as coordenadas 
                            # iniciais e a direção calculada.
                    # A bola agora tem uma posição e uma velocidade (direção)
                            # que a moverá a cada frame.
                    bolas.append([posicao_inicial_bola[0], posicao_inicial_bola[1], direcao_x, direcao_y])
                    
                    # Define 'carregando_potencia' como False, pois a bola
                            # foi lançada e o estilingue está "livre".
                    carregando_potencia = False

        # Verifica se o jogador errou o alvo (clicou_errado é True).
        # Se 'clicou_errado' for verdadeiro, define 'rodando'
                # como False, encerrando o jogo.
        if clicou_errado:
            rodando = False
        
        # Atualiza a tela, aplicando todas as mudanças feitas 
                # durante o ciclo atual do loop.
        pygame.display.flip()
        
        # Atraso de 30 milissegundos entre cada frame para 
                # controlar a velocidade do jogo.
        pygame.time.delay(30)


# Tela de Game Over com opção de reiniciar
# Esta função exibe a tela de "Game Over" ao jogador 
        # quando o jogo termina.
# Mostra a pontuação final e instrui o jogador a clicar 
        # para voltar ao menu principal.
def tela_game_over():
    
    # Declara as variáveis 'pontuacao' e 'clicou_errado' 
            # como globais para que possam ser alteradas.
    # 'pontuacao' armazena a pontuação final a ser exibida,
            # e 'clicou_errado' será resetado para permitir que o 
            # jogo reinicie corretamente.
    global pontuacao, clicou_errado
    
    # Desenha a imagem de fundo, cobrindo a tela inteira.
    tela.blit(imagem_fundo, (0, 0))
    
    # Exibe o texto "Game Over!" na tela, no centro 
            # superior da área visível.
    # Usa 'fonte_menu' para um texto maior e mais visível.
    mostrar_texto("Game Over!", fonte_menu, PRETO, LARGURA // 2 - 80, ALTURA // 2 - 50)
    
    # Exibe a pontuação final do jogador, logo abaixo do
            # texto "Game Over!".
    # Usa a fonte padrão ('fonte') para um texto menor.
    mostrar_texto(f"Pontuação Final: {pontuacao}", fonte, PRETO, LARGURA // 2 - 80, ALTURA // 2 + 10)
    
    # Exibe uma mensagem instruindo o jogador a 
            # clicar para voltar ao menu.
    # Esta mensagem aparece logo abaixo da pontuação final.
    mostrar_texto("Clique para voltar ao menu", fonte, PRETO, LARGURA // 2 - 110, ALTURA // 2 + 60)
    
    # Atualiza a tela para mostrar o fundo, o texto 
            # de "Game Over" e a pontuação final.
    pygame.display.flip()
    
    # Pausa de 1 segundo para dar tempo ao jogador de 
            # ver a mensagem antes de reiniciar.
    pygame.time.delay(1000)
    
    # Variável 'aguardando' controla o loop de espera 
            # até o jogador clicar para continuar.
    aguardando = True
    while aguardando:
        
        # Verifica todos os eventos enquanto o jogo 
                # aguarda o clique do jogador.
        for evento in pygame.event.get():
            
            # Se o jogador fecha a janela, encerra o jogo.
            if evento.type == pygame.QUIT:
                
                pygame.quit()  # Encerra o Pygame
                sys.exit()     # Encerra o programa completamente
            
            # Se o jogador clica com o mouse, reinicia o jogo.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Reseta a pontuação para 0, preparando 
                        # para uma nova partida.
                pontuacao = 0
                
                # Reseta 'clicou_errado' para False, permitindo 
                        # que o jogo continue sem fim imediato.
                clicou_errado = False
                
                # Define 'aguardando' como False, saindo do loop 
                        # de espera e voltando ao menu principal.
                aguardando = False


# Carregar pontuação acumulada ao iniciar
# Chama a função 'carregar_pontuacao_acumulada' para ler a 
        # pontuação acumulada de jogos anteriores.
# Essa pontuação é exibida na tela inicial e
        # atualizada ao longo das partidas.
pontuacao_acumulada = carregar_pontuacao_acumulada()

# Loop principal
# Este é o loop principal do programa, que alterna entre a
        # tela de jogo, a tela inicial e a tela de Game Over.
# Ele continua indefinidamente até que o jogador 
        # feche a janela do jogo.
while True:
    
    # Verifica se o jogador errou um tiro ('clicou_errado' é True).
    # Se 'clicou_errado' for verdadeiro, exibe a tela de Game Over.
    if clicou_errado:
        
        # Chama a função 'tela_game_over' para mostrar a
                # pontuação final e reiniciar o jogo.
        tela_game_over()
    
    # Se 'clicou_errado' for False, o jogo pode continuar.
    else:
        
        # Exibe a tela inicial do jogo, com instruções e
                # pontuação acumulada.
        tela_inicial()
        
        # Inicia o loop principal do jogo, que inclui o movimento
                # do pato, o lançamento de bolas
                # e o controle da pontuação enquanto o
                # jogo estiver rodando.
        jogo()