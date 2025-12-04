# Importa o módulo Pygame para gráficos, eventos e manipulação de imagens.
import pygame

# Importa o módulo random para gerar números aleatórios.
import random

# Importa o módulo sys para sair do programa de forma segura.
import sys

# Importa o módulo time para controlar o tempo no jogo.
import time

# Inicializando o Pygame
# Esta linha inicializa todos os módulos do Pygame, 
        # preparando-o para uso.
pygame.init()

# Configurações da tela (largura ajustada para 400 pixels)
# Define as dimensões da tela do jogo: largura de 400 
        # pixels e altura de 600 pixels.
LARGURA, ALTURA = 400, 600

# Cria a janela de exibição com as dimensões definidas (LARGURA x ALTURA).
# Esse será o espaço onde todos os elementos do jogo serão desenhados.
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela do jogo que será exibido na barra da janela.
pygame.display.set_caption("Jogo do Pássaro")

# Carregando a imagem do fundo
# Carrega a imagem de fundo a partir do arquivo 'fundo.png'.
# Essa imagem será usada como plano de fundo do jogo.
imagem_fundo = pygame.image.load('fundo.png') 

# Redimensiona a imagem de fundo para cobrir toda a tela.
# Adapta a imagem ao tamanho da tela definido 
        # anteriormente (LARGURA, ALTURA).
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA, ALTURA))

# Carregando as imagens do pássaro
# Carrega a primeira imagem do pássaro enquanto ele está "voando".
imagem_passaro1 = pygame.image.load('passaro_voando1.png')

# Redimensiona a primeira imagem do pássaro para um
        # tamanho de 50x50 pixels.
# Esse tamanho é adequado ao espaço do jogo.
imagem_passaro1 = pygame.transform.scale(imagem_passaro1, (50, 50))

# Carrega a segunda imagem do pássaro, que será 
        # alternada para simular o bater de asas.
imagem_passaro2 = pygame.image.load('passaro_voando2.png')

# Redimensiona a segunda imagem do pássaro para o 
        # mesmo tamanho de 50x50 pixels.
imagem_passaro2 = pygame.transform.scale(imagem_passaro2, (50, 50))

# Carrega a imagem do pássaro enquanto ele está 
        # caindo após ser acertado.
imagem_passaro_caindo = pygame.image.load('passaro_caindo.png')

# Redimensiona a imagem do pássaro caindo para 50x50 pixels.
imagem_passaro_caindo = pygame.transform.scale(imagem_passaro_caindo, (50, 50))

# Cores
# Define a cor branca usando valores RGB (255, 255, 255).
BRANCO = (255, 255, 255)

# Define a cor preta usando valores RGB (0, 0, 0).
PRETO = (0, 0, 0)

# Fonte
# Define a fonte padrão para o texto do jogo 
        # com tamanho 30 pixels.
fonte = pygame.font.Font(None, 30)

# Define uma fonte maior para o menu, com tamanho 40 pixels.
fonte_menu = pygame.font.Font(None, 40)

# Variáveis do jogo
# Define a posição inicial do pássaro com uma 
        # posição aleatória na tela.
# Garante que o pássaro não ultrapasse as bordas da 
        # tela usando o tamanho da imagem (50x50).
posicao_passaro = [random.randint(0, LARGURA - 50), random.randint(0, ALTURA - 50)]

# Define a direção inicial do pássaro, que pode ser
        # para a esquerda/direita e para cima/baixo.
# A direção é escolhida aleatoriamente entre -1 e 1 para cada eixo (x e y).
direcao_passaro = [random.choice([-1, 1]), random.choice([-1, 1])]

# Define a velocidade inicial do pássaro em 2 pixels por movimento.
# Aumenta à medida que o jogador acerta o 
        # pássaro, dificultando o jogo.
velocidade = 2

# Armazena a pontuação atual do jogador (número de
        # vezes que acertou o pássaro).
pontuacao = 0

# Armazena a pontuação acumulada ao longo das partidas,
        # carregada de um arquivo.
pontuacao_acumulada = 0  # Pontuação acumulada ao longo dos jogos

# Indica se o jogador clicou fora do pássaro; True 
        # significa que o jogador errou o clique.
clicado_incorretamente = False

# Indica se o pássaro foi atingido (acertado pelo 
        # clique do jogador); True se o pássaro foi acertado.
passaro_atingido = False

# Armazena a imagem atual do pássaro para simular o bater de asas.
# A imagem inicial é 'imagem_passaro1'.
imagem_atual = imagem_passaro1

# Controla o tempo para alternar a imagem do pássaro e
        # simular o bater de asas.
contador_asa = 0

# Função para exibir texto
# Esta função exibe uma mensagem de texto na tela, 
        # com a fonte, cor e posição especificadas.
def mostrar_texto(texto, fonte, cor, x, y):
    
    # Renderiza o texto em uma superfície com a
            # fonte e cor especificadas.
    # O segundo parâmetro define se o texto é renderizado
            # com antialiasing (suavização de bordas).
    superficie_texto = fonte.render(texto, True, cor)
    
    # Desenha a superfície do texto (superficie_texto) 
            # na tela principal (tela)
            # nas coordenadas especificadas (x, y).
    tela.blit(superficie_texto, (x, y))

# Função para carregar a pontuação acumulada
# Esta função lê a pontuação acumulada de jogos
        # anteriores a partir de um arquivo de texto.
def carregar_pontuacao_acumulada():
    
    try:
        
        # Tenta abrir o arquivo 'pontuacao.txt' em modo de leitura.
        with open("pontuacao.txt", "r") as arquivo:
            
            # Lê a primeira linha do arquivo, remove
                    # espaços em branco e novas linhas
                    # e converte o valor para um número
                    # inteiro, que é a pontuação acumulada.
            return int(arquivo.readline().strip())
            
    except:
        
        # Se houver qualquer erro ao abrir ou ler o 
                # arquivo (como se o arquivo não existir),
                # retorna 0, indicando que a pontuação 
                # acumulada começa em zero.
        return 0

# Função para salvar pontuação acumulada
# Esta função atualiza a pontuação acumulada, somando a 
        # pontuação da partida atual e salvando o resultado no arquivo.
def salvar_pontuacao_acumulada(pontuacao):
    
    # Declara a variável global 'pontuacao_acumulada' 
            # para que possa ser modificada nesta função.
    global pontuacao_acumulada
    
    # Adiciona a pontuação da partida atual à pontuação acumulada.
    pontuacao_acumulada += pontuacao
    
    # Abre o arquivo 'pontuacao.txt' em modo de escrita
            # para salvar a pontuação atualizada.
    # Se o arquivo já existir, ele será substituído;
            # caso contrário, será criado.
    with open("pontuacao.txt", "w") as arquivo:
        
        # Converte a pontuação acumulada para string e
                # escreve no arquivo.
        arquivo.write(str(pontuacao_acumulada))


# Tela inicial aprimorada com texto ajustado
# Esta função exibe a tela inicial do jogo, com o plano 
        # de fundo e instruções para o jogador.
def tela_inicial():
    
    # Desenha a imagem de fundo na tela, cobrindo toda a área de exibição.
    # Isso é feito para garantir que a tela comece com uma aparência "limpa".
    tela.blit(imagem_fundo, (0, 0))
    
    # Exibe a mensagem de boas-vindas "Bem-vindo ao Jogo!" no 
            # topo da tela, centralizada horizontalmente.
    mostrar_texto("Bem-vindo ao Jogo!", fonte_menu, PRETO, LARGURA // 2 - 150, ALTURA // 2 - 150)
    
    # Mostra a pontuação acumulada ao longo dos jogos, centralizada 
            # horizontalmente, logo abaixo do título.
    mostrar_texto(f"Pontuação Acumulada: {pontuacao_acumulada}", fonte, PRETO, LARGURA // 2 - 120, ALTURA // 2 - 100)
    
    # Instrui o jogador a clicar no pássaro, exibindo o texto
            # centralizado logo abaixo da pontuação.
    mostrar_texto("Clique no pássaro.", fonte, PRETO, LARGURA // 2 - 130, ALTURA // 2 - 50)
    
    # Exibe uma instrução adicional: "Se errar, você perde!" 
            # para reforçar as regras do jogo.
    mostrar_texto("Se errar, você perde!", fonte, PRETO, LARGURA // 2 - 110, ALTURA // 2)
    
    # Informa ao jogador que ele deve clicar para iniciar o jogo, 
            # centralizado e na parte inferior da tela inicial.
    mostrar_texto("Clique para iniciar", fonte_menu, PRETO, LARGURA // 2 - 90, ALTURA // 2 + 80)
    
    # Atualiza a tela com todos os textos e a imagem de fundo, 
            # mostrando a tela inicial completa ao jogador.
    pygame.display.flip()
    
    # Define uma variável 'aguardando' como True para manter o 
            # loop de espera até o jogador clicar.
    aguardando = True
    
    # Loop para aguardar o jogador iniciar o jogo clicando na tela.
    # Esse loop mantém a tela inicial visível até que o
            # jogador interaja com ela,
            # clicando para iniciar o jogo ou fechando a janela.
    while aguardando:
        
        # Captura eventos do Pygame, como cliques e o fechamento da janela.
        # Cada evento representa uma interação do usuário, e o
                # loop verifica se o jogador
                # realizou alguma ação específica, como um clique ou fechamento.
        for evento in pygame.event.get():
            
            # Se o evento capturado for o fechamento da janela (pygame.QUIT),
            # o programa encerra o Pygame e termina o script.
            if evento.type == pygame.QUIT:
                
                # pygame.quit() encerra todos os módulos do
                        # Pygame que estão em uso.
                pygame.quit()
                
                # sys.exit() interrompe a execução do script, 
                        # fechando o programa completamente.
                sys.exit()
            
            # Se o evento capturado for um clique do 
                    # mouse (pygame.MOUSEBUTTONDOWN),
                    # significa que o jogador deseja iniciar o jogo.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Define 'aguardando' como False para sair do loop e
                        # prosseguir para o jogo.
                # Isso interrompe o loop de espera e faz com que o
                        # programa avance para a próxima fase.
                aguardando = False



# Função para movimentar o pássaro de forma realista
# Esta função move o pássaro pela tela e alterna entre 
        # imagens para simular o bater de asas.
def mover_passaro():
    
    # Declara variáveis globais para que as alterações feitas
            # dentro da função afetem o jogo todo.
    # 'posicao_passaro' define a posição atual do pássaro, 
            # 'direcao_passaro' define a direção do movimento,
    # 'imagem_atual' armazena a imagem atual para simular o 
            # bater de asas, e 'contador_asa' controla a troca de imagens.
    global posicao_passaro, direcao_passaro, imagem_atual, contador_asa
    
    # Atualiza a posição horizontal do pássaro (eixo X) com 
            # base na direção e velocidade atuais.
    # Multiplica a direção (1 ou -1) pela velocidade para 
            # mover o pássaro para a direita ou esquerda.
    posicao_passaro[0] += direcao_passaro[0] * velocidade
    
    # Atualiza a posição vertical do pássaro (eixo Y) com 
            # base na direção e velocidade atuais.
    # Multiplica a direção (1 ou -1) pela velocidade para
            # mover o pássaro para cima ou para baixo.
    posicao_passaro[1] += direcao_passaro[1] * velocidade

    # Alternando a imagem para simular o bater de
            # asas a cada 10 frames
    # Incrementa 'contador_asa' a cada chamada para 
            # controlar a frequência da troca de imagem.
    contador_asa += 1
    
    # Se 'contador_asa' atinge 10, troca a imagem do 
            # pássaro e reinicia o contador.
    # Esse ajuste de valor controla a velocidade do
            # bater de asas, dando um efeito animado.
    if contador_asa >= 10:  
        
        # Verifica se a imagem atual é 'imagem_passaro1'. 
        # Se for, troca para 'imagem_passaro2'.
        if imagem_atual == imagem_passaro1:
            imagem_atual = imagem_passaro2
            
        else:
            
            # Caso contrário, volta para 'imagem_passaro1', 
                    # criando o efeito de alternância.
            imagem_atual = imagem_passaro1
        
        # Reinicia o contador para recomeçar a 
                # contagem de frames até a próxima troca.
        contador_asa = 0

    # Alterar direção quando o pássaro atinge a borda da tela
    # Verifica se o pássaro atingiu a borda esquerda (0) ou
            # direita (largura da tela - 50 pixels).
    # Se sim, inverte a direção horizontal multiplicando 
            # por -1, fazendo-o "quicar" para o lado oposto.
    if posicao_passaro[0] <= 0 or posicao_passaro[0] >= LARGURA - 50:
        direcao_passaro[0] *= -1
    
    # Verifica se o pássaro atingiu a borda superior (0) ou 
            # inferior (altura da tela - 50 pixels).
    # Se sim, inverte a direção vertical multiplicando 
            # por -1, fazendo-o "quicar" para o lado oposto.
    if posicao_passaro[1] <= 0 or posicao_passaro[1] >= ALTURA - 50:
        direcao_passaro[1] *= -1


# Função para animar a queda do pássaro após ser acertado
# Esta função simula a animação do pássaro caindo
        # após ser atingido,
        # criando um efeito de queda realista que dura até o 
        # pássaro alcançar a parte inferior da tela.
def animar_queda():
    
    # Declara a variável global 'posicao_passaro' para
            # modificar sua posição ao longo da animação.
    global posicao_passaro
    
    # Inicia um loop que continuará até o pássaro atingir o 
            # solo (ALTURA - 50 pixels).
    # A condição verifica se a posição vertical do pássaro 
            # (posicao_passaro[1]) é menor que o limite inferior.
    while posicao_passaro[1] < ALTURA - 50:
        
        # Redesenha a imagem de fundo na tela, cobrindo 
                # qualquer elemento anteriormente desenhado.
        # Isso garante que a tela seja "limpa" antes de desenhar a 
                # nova posição do pássaro em queda.
        tela.blit(imagem_fundo, (0, 0))
        
        # Incrementa a posição vertical do pássaro para 
                # simular a queda.
        # O valor 20 representa a velocidade da queda, 
                # controlando o quão rápido o pássaro cai.
        posicao_passaro[1] += 20 
        
        # Desenha a imagem do pássaro caindo na nova posição.
        # Como 'posicao_passaro[1]' aumenta a cada iteração, o
                # pássaro é desenhado mais para baixo a cada ciclo.
        tela.blit(imagem_passaro_caindo, posicao_passaro)
        
        # Atualiza a tela com as mudanças feitas (fundo e
                # nova posição do pássaro).
        pygame.display.flip()
        
        # Introduz uma pequena pausa de 30 milissegundos 
                # entre cada atualização da tela,
                # para controlar a velocidade da animação e
                # torná-la mais fluida.
        pygame.time.delay(30)


# Função principal do jogo
# Esta função executa o loop principal do jogo, onde o 
        # pássaro se move pela tela e o jogador tenta acertá-lo.
# Ela também exibe a pontuação atual e lida com o estado do
        # jogo, como verificar se o pássaro foi atingido.
def jogo():
    
    # Declara variáveis globais para que as mudanças nelas
            # feitas aqui afetem todo o jogo.
    # 'posicao_passaro' controla a posição do pássaro na tela,
    # 'pontuacao' armazena a pontuação do jogador,
    # 'velocidade' ajusta a velocidade de movimento do pássaro,
    # 'clicado_incorretamente' marca se o jogador errou um clique,
    # e 'passaro_atingido' indica se o pássaro foi atingido.
    global posicao_passaro, pontuacao, velocidade, clicado_incorretamente, passaro_atingido
    
    # Define a variável 'rodando' como True, para que o loop do 
            # jogo continue até que 'rodando' se torne False.
    rodando = True
    
    # Loop principal do jogo, que mantém o jogo ativo
            # até o jogador errar um clique.
    while rodando:
        
        # Desenha a imagem de fundo para limpar a tela e
                # preparar a visualização para a próxima atualização.
        tela.blit(imagem_fundo, (0, 0))
        
        # Exibindo a pontuação
        # Mostra a pontuação atual no canto superior esquerdo da tela.
        # A função 'mostrar_texto' é usada para renderizar o texto na tela.
        mostrar_texto(f"Pontuação: {pontuacao}", fonte, PRETO, 10, 10)
        
        # Movimentação do pássaro
        # Verifica se o pássaro ainda não foi atingido pelo jogador.
        if not passaro_atingido:
            
            # Chama a função 'mover_passaro' para atualizar a posição do pássaro.
            # Isso permite que o pássaro se mova automaticamente pela tela.
            mover_passaro()
            
            # Desenha a imagem atual do pássaro na nova posição.
            # A imagem alterna entre 'imagem_passaro1' e
                    # 'imagem_passaro2' para simular o bater de asas.
            tela.blit(imagem_atual, posicao_passaro)

        
        # Loop de eventos
        # Este loop captura e processa os eventos do Pygame,
                # como cliques do mouse e fechamento da janela.
                # Cada evento representa uma interação do 
                # jogador com a janela do jogo.
        for evento in pygame.event.get():
            
            # Verifica se o evento é de fechamento da janela (pygame.QUIT).
            # Isso acontece quando o jogador clica no botão de fechar.
            if evento.type == pygame.QUIT:
                
                # Encerra o Pygame, fechando todos os módulos em uso.
                pygame.quit()
                
                # Finaliza o programa completamente.
                sys.exit()
            
            # Verifica se o evento é um clique do mouse (pygame.MOUSEBUTTONDOWN).
            # Isso ocorre quando o jogador clica com o botão do 
                    # mouse na tela do jogo.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Captura as coordenadas do clique do mouse e
                        # armazena em 'x' e 'y'.
                # Essas coordenadas serão usadas para verificar 
                        # se o jogador clicou no pássaro.
                x, y = evento.pos
                
                # Verifica se o clique foi no pássaro
                # Esta condição verifica se o clique está dentro da 
                        # área ocupada pela imagem do pássaro.
                # A posição do pássaro é definida por 'posicao_passaro', e
                        # o tamanho da imagem é de 50x50 pixels.
                if (posicao_passaro[0] <= x <= posicao_passaro[0] + 50) and (posicao_passaro[1] <= y <= posicao_passaro[1] + 50):
                    
                    # Acertou o clique
                    # Se a condição acima for verdadeira, significa que o
                            # jogador acertou o pássaro.
                    
                    # Incrementa a pontuação em 1 ponto.
                    pontuacao += 1
                    
                    # Chama a função 'salvar_pontuacao_acumulada' 
                            # para atualizar a pontuação acumulada.
                    salvar_pontuacao_acumulada(1)
                    
                    # Aumenta a velocidade do pássaro, tornando o
                            # jogo mais desafiador.
                    velocidade += 1
                    
                    # Marca o pássaro como atingido, para que ele 
                            # comece a animação de queda.
                    passaro_atingido = True
                
                else:
                    
                    # Errou o clique
                    # Se o jogador clicou fora da área do pássaro, o
                            # clique é considerado incorreto.
                    
                    # Define 'clicado_incorretamente' como True para 
                            # indicar que o jogador errou o clique.
                    clicado_incorretamente = True
                    
                    # Define 'rodando' como False para encerrar o loop
                            # do jogo, finalizando esta partida.
                    rodando = False


        # Animação de queda quando o pássaro é atingido
        # Este bloco de código verifica se o pássaro foi atingido e, 
                # caso tenha sido, executa a animação de queda.
        if passaro_atingido:
            
            # Chama a função 'animar_queda' para simular a animação do
                    # pássaro caindo para o solo.
            # A função 'animar_queda' atualiza a posição vertical do
                    # pássaro, desenhando-o progressivamente
                    # mais próximo da base da tela para criar um efeito de queda.
            animar_queda()
            
            # Após a animação de queda, redefine a variável 'passaro_atingido' para False,
            # para que o pássaro volte a se mover normalmente na 
                    # próxima iteração do loop do jogo.
            passaro_atingido = False
            
            # Define uma nova posição para o pássaro após a 
                    # queda, de forma aleatória.
            # O pássaro é reposicionado em um ponto aleatório na tela 
                    # para que o jogador o encontre novamente.
            posicao_passaro = [random.randint(0, LARGURA - 50), random.randint(0, ALTURA - 50)]
        
        # Atualiza a tela com todas as mudanças feitas no 
                # quadro atual do loop,
        # incluindo a nova posição do pássaro e qualquer
                # alteração visual recente.
        pygame.display.flip()
        
        # Introduz uma pausa de 50 milissegundos entre 
                # cada iteração do loop,
        # controlando a velocidade do jogo e tornando a 
                # animação mais suave.
        pygame.time.delay(50)


# Tela de Game Over aprimorada
# Esta função exibe a tela de Game Over após o 
        # jogador cometer um erro.
# Ela mostra a pontuação final e uma mensagem para o 
        # jogador clicar para retornar ao menu principal.
def tela_game_over():
    
    # Declara as variáveis globais 'pontuacao',
            # 'velocidade' e 'clicado_incorretamente',
            # para que possamos redefinir esses valores 
            # quando o jogo recomeçar.
    global pontuacao, velocidade, clicado_incorretamente
    
    # Desenha a imagem de fundo na tela para limpar 
            # qualquer conteúdo anterior.
    tela.blit(imagem_fundo, (0, 0))
    
    # Exibe a mensagem "Game Over!" no centro da tela 
            # para indicar o fim do jogo.
    # O texto é centralizado horizontalmente ajustando a 
            # posição com base em sua largura.
    mostrar_texto("Game Over!", fonte_menu, PRETO, LARGURA // 2 - 80, ALTURA // 2 - 50)
    
    # Exibe a pontuação final do jogador logo abaixo da
            # mensagem de Game Over.
    # A pontuação é centralizada na tela para que o jogador
            # visualize seu desempenho.
    mostrar_texto(f"Pontuação Final: {pontuacao}", fonte, PRETO, LARGURA // 2 - 80, ALTURA // 2 + 10)
    
    # Exibe uma mensagem instruindo o jogador a clicar para 
            # retornar ao menu principal.
    # A mensagem é centralizada horizontalmente e posicionada 
            # abaixo da pontuação.
    mostrar_texto("Clique para voltar ao menu", fonte, PRETO, LARGURA // 2 - 110, ALTURA // 2 + 60)
    
    # Atualiza a tela para exibir todos os textos e a imagem de fundo.
    pygame.display.flip()
    
    # Introduz uma pausa de 1 segundo (1000 milissegundos)
            # para que o jogador tenha um momento para ver a 
            # tela de Game Over antes de poder clicar para retornar.
    pygame.time.delay(1000)
    
    # Define a variável 'aguardando' como True para
            # entrar no loop de espera.
    # Esse loop fica ativo até o jogador clicar
            # para voltar ao menu.
    aguardando = True
    
    # Loop de espera para aguardar o jogador clicar e
            # retornar ao menu principal.
    while aguardando:
        
        # Captura eventos do Pygame, como cliques do
                # mouse ou fechamento da janela.
        for evento in pygame.event.get():
            
            # Se o jogador fechar a janela, o Pygame e o 
                    # programa são encerrados.
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Se o jogador clicar com o mouse, o loop é 
                    # encerrado e o jogo retorna ao menu.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Redefine a pontuação para 0 para o início de um novo jogo.
                pontuacao = 0
                
                # Redefine a velocidade para o valor inicial,
                        # tornando o jogo mais fácil no reinício.
                velocidade = 2
                
                # Define 'clicado_incorretamente' como False, indicando
                        # que o jogador não errou no próximo jogo.
                clicado_incorretamente = False
                
                # Define 'aguardando' como False para sair do
                        # loop e voltar ao menu inicial.
                aguardando = False


# Carregar pontuação acumulada ao iniciar
# Esta linha chama a função 'carregar_pontuacao_acumulada' 
        # para obter a pontuação acumulada de jogos anteriores.
# A função tenta ler o valor de um arquivo e, se bem-sucedida,
        # armazena o valor na variável 'pontuacao_acumulada'.
pontuacao_acumulada = carregar_pontuacao_acumulada()

# Loop principal
# Este é o loop principal do programa, que mantém o jogo em
        # execução indefinidamente até que o jogador feche a janela.
while True:
    
    # Verifica se o jogador clicou incorretamente (ou seja,
            # errou ao tentar clicar no pássaro).
    # Se 'clicado_incorretamente' for True, chama a 
            # função 'tela_game_over', que mostra a 
            # tela de fim de jogo.
    if clicado_incorretamente:
        
        # Chama a função para exibir a tela de Game Over e
                # aguarda que o jogador clique para retornar ao menu.
        tela_game_over()
    
    else:
        
        # Se 'clicado_incorretamente' for False, significa 
                # que o jogador não cometeu um erro,
                # então o programa exibe a tela inicial e, em
                # seguida, inicia o jogo.
        
        # Chama a função 'tela_inicial' para mostrar as 
                # instruções e a pontuação acumulada.
        # A função 'tela_inicial' fica em um loop até que o 
                # jogador clique para iniciar o jogo.
        tela_inicial()
        
        # Inicia o loop do jogo chamando a função 'jogo'.
        # A função 'jogo' executa a lógica principal do jogo,
                # permitindo que o jogador interaja e acumule pontos.
        jogo()