# Importa o módulo pygame, que é uma biblioteca usada para 
        # criar jogos e outras aplicações multimídia.
import pygame

# Importa o módulo random, que fornece funções para gerar
        # números aleatórios, essencial para dinâmicas de jogo variadas.
import random

# Importa o módulo sys, utilizado para manipular diferentes 
        # partes do ambiente de execução do Python, como a saída do sistema.
import sys

# Importa o módulo os, que fornece uma maneira portátil de usar
        # funcionalidades dependentes do sistema operacional,
        # como ler ou escrever arquivos.
import os

# Inicializa todos os módulos necessários para o Pygame
        # funcionar corretamente.
pygame.init()

# Define constantes para a largura e altura da tela do jogo, 
        # usadas para configurar a janela de exibição.
LARGURA_TELA = 400
ALTURA_TELA = 600

# Cria uma janela ou tela para exibição com as dimensões especificadas acima.
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Define o título que aparecerá na barra de título da janela do jogo.
pygame.display.set_caption("Desvie dos Obstáculos")

# Define a cor BRANCO como uma tupla contendo os valores RGB (255, 255, 255).
BRANCO = (255, 255, 255)

# Define a cor LARANJA como uma tupla contendo os valores RGB (255, 140, 0).
LARANJA = (255, 140, 0)

# Cria uma fonte do Pygame para desenhar texto na tela. 
        # O 'None' especifica o uso da fonte padrão, e
        # '40' é o tamanho da fonte.
fonte = pygame.font.SysFont(None, 40)

# Carrega imagens dos arquivos especificados, que serão usadas 
        # para o fundo, o jogador e os obstáculos no jogo.
imagem_fundo = pygame.image.load("fundo.png")
imagem_jogador = pygame.image.load("jogador.png")
imagem_obstaculo = pygame.image.load("obstaculo.png")

# Redimensiona as imagens carregadas para se ajustarem às necessidades
        # específicas do jogo, como dimensões específicas na tela.
imagem_fundo = pygame.transform.scale(imagem_fundo, (LARGURA_TELA, ALTURA_TELA))
imagem_jogador = pygame.transform.scale(imagem_jogador, (50, 50))
imagem_obstaculo = pygame.transform.scale(imagem_obstaculo, (50, 50))

# Define a posição inicial do jogador no meio da largura da tela e 
        # ajustado para ficar acima do chão da tela.
pos_x_jogador = LARGURA_TELA // 2 - imagem_jogador.get_width() // 2
pos_y_jogador = ALTURA_TELA - imagem_jogador.get_height() - 85

# Define a velocidade de movimento do jogador.
velocidade_jogador = 7

# Define a velocidade de movimento dos obstáculos 
        # que aparecerão na tela.
velocidade_obstaculo = 5

# Define o intervalo de tempo entre o surgimento de cada obstáculo.
intervalo_obstaculos = 30

# Inicializa uma lista vazia para armazenar os retângulos que 
        # representam os obstáculos que serão criados.
obstaculos = []

# Inicializa a variável de pontos acumulados pelo jogador a zero.
pontos = 0

# Inicializa a variável que controla o tempo de jogo.
tempo_jogo = 0

# Inicializa uma variável booleana que indica se o jogo está em execução.
jogo_rodando = False


# Define uma função chamada 'carregar_pontuacao' que não
        # recebe nenhum argumento e retorna o total de pontos acumulados.
def carregar_pontuacao():
    
    # Verifica se o arquivo 'pontuacao.txt' existe no diretório
            # atual usando a função 'exists' do módulo 'os.path'.
    if os.path.exists("pontuacao.txt"):
    
        # Abre o arquivo 'pontuacao.txt' no modo de leitura ('r') como 'arquivo'.
        with open("pontuacao.txt", "r") as arquivo:
        
            # Lê o conteúdo completo do arquivo, remove espaços em branco e
                    # novas linhas extras no início e no fim com 'strip()'.
            conteudo = arquivo.read().strip()
            
            # Tenta realizar as operações dentro do bloco 'try'.
            try:
            
                # Divide o conteúdo pela string ": ", pega o segundo elemento da 
                        # lista resultante (índice 1), e tenta converter para inteiro.
                total_pontos = int(conteudo.split(": ")[1])
            
            # Captura erros de 'IndexError' (índice não encontrado) ou 
                    # 'ValueError' (conversão para inteiro falha).
            except (IndexError, ValueError):
            
                # Se ocorrer algum dos erros acima, define 'total_pontos' como 0.
                total_pontos = 0
            
            # Retorna o valor de 'total_pontos' que pode ser o 
                    # convertido ou zero em caso de erro.
            return total_pontos
    
    # Se o arquivo 'pontuacao.txt' não existir, retorna 0.
    else:
        return 0


# Define a função 'salvar_pontuacao' para gravar o total de
            # pontos acumulados no arquivo.
def salvar_pontuacao():
    
    # Chama a função 'carregar_pontuacao' para obter o total de 
            # pontos acumulados e soma com a variável global 'pontos'.
    total_pontos = carregar_pontuacao() + pontos
    
    # Abre (ou cria) o arquivo 'pontuacao.txt' no modo de 
            # escrita ('w'), que sobrescreve o conteúdo existente.
    with open("pontuacao.txt", "w") as arquivo:
        
        # Escreve a string formatada "Pontos: " seguida do 
                # valor de 'total_pontos' no arquivo.
        arquivo.write(f"Pontos: {total_pontos}")

# Define a função 'exibir_pontuacao' para mostrar a 
        # pontuação atual na tela do jogo.
def exibir_pontuacao():
    
    # Usa a 'fonte' definida anteriormente para renderizar o texto da 
            # pontuação atual, com antialiasing (True) e na cor LARANJA.
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, LARANJA)
    
    # Desenha o texto renderizado na tela na posição (10, 10)
            # do canto superior esquerdo.
    tela.blit(texto_pontos, (10, 10))


# Define uma função chamada 'criar_obstaculo' para 
        # adicionar obstáculos ao jogo.
def criar_obstaculo():
    
    # Gera uma coordenada x aleatória. A função 'randint' do 
            # módulo 'random' escolhe um número inteiro aleatoriamente
            # entre 0 e a largura da tela menos a largura do obstáculo. 
    # Isso garante que o obstáculo seja totalmente visível na tela,
            # evitando que parte dele fique fora da área visível horizontalmente.
    x = random.randint(0, LARGURA_TELA - imagem_obstaculo.get_width())
    
    # Define a coordenada y inicial do obstáculo como negativa, 
            # exatamente acima do topo da tela.
    # A altura do obstáculo é subtraída da posição y, fazendo
            # com que ele comece fora da tela (acima do limite superior),
            # permitindo que desça para a tela, o que cria 
            # uma animação de 'cair' do topo.
    y = -imagem_obstaculo.get_height()
    
    # Adiciona um novo retângulo à lista 'obstaculos'. 
    # A função 'pygame.Rect' cria um retângulo que é usado para representar
            # o obstáculo. Os parâmetros são (x, y, largura, altura), 
            # onde 'x' e 'y' são as coordenadas definidas acima, e
            # 'imagem_obstaculo.get_width()' e 'imagem_obstaculo.get_height()' 
            # são a largura e a altura do obstáculo, respectivamente.
    # Este retângulo é usado para posicionar o obstáculo na tela e 
            # para detectar colisões com o jogador.
    obstaculos.append(pygame.Rect(x, y, imagem_obstaculo.get_width(), imagem_obstaculo.get_height()))


# Define uma função chamada 'atualizar_obstaculos' que recebe 
            # um retângulo do Pygame representando o jogador.
def atualizar_obstaculos(jogador):
    
    # Declaração 'global' para modificar variáveis globais dentro da função.
    global pontos, velocidade_obstaculo, jogo_rodando
    
    # Inicia um loop para iterar sobre cada obstáculo na lista 'obstaculos'.
    for obstaculo in obstaculos:
        
        # Aumenta a posição y do obstáculo, fazendo-o descer na tela.
        # A quantidade de incremento é determinada pela 'velocidade_obstaculo'.
        obstaculo.y += velocidade_obstaculo
        
        # Checa se o retângulo do obstáculo colide com o retângulo 
                # do jogador usando o método 'colliderect'.
        # Se houver uma colisão, define a variável 'jogo_rodando' 
                # como False, o que pode ser usado para interromper o jogo.
        if obstaculo.colliderect(jogador):

            # Define o estado do jogo para falso, indicando o fim 
                    # do jogo devido à colisão.
            jogo_rodando = False  
        
        # Verifica se o obstáculo passou do limite inferior da 
                # tela (sua posição y é maior que a altura da tela).
        if obstaculo.y > ALTURA_TELA:
            
            # Remove o obstáculo da lista 'obstaculos', pois ele não 
                    # precisa mais ser processado ou desenhado.
            obstaculos.remove(obstaculo)
            
            # Incrementa a variável 'pontos' em 1, pois o jogador 
                    # conseguiu evitar o obstáculo com sucesso.
            pontos += 1
            
            # Aumenta a 'velocidade_obstaculo' em 0.5 para tornar o jogo 
                    # progressivamente mais difícil à medida que mais 
                    # obstáculos são evitados.
            velocidade_obstaculo += 0.5


# Define a função 'mostrar_menu' para criar e exibir o menu inicial do jogo.
def mostrar_menu():
    
    # Desenha a imagem de fundo na tela. O método 'blit' é usado para 
            # desenhar uma superfície sobre outra, aqui posicionada no 
            # canto superior esquerdo (0, 0).
    tela.blit(imagem_fundo, (0, 0))
    
    # Renderiza o texto do título "Desvie dos Obstáculos" usando a fonte 
            # definida anteriormente, com antialiasing ativado (True) e a cor LARANJA.
    titulo = fonte.render("Desvie dos Obstáculos", True, LARANJA)
    
    # Desenha o título na tela. A posição x é calculada para centralizar o
            # título horizontalmente e a posição y é um quarto da altura da tela.
    tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, ALTURA_TELA // 4))

    # Chama a função 'carregar_pontuacao' para obter o total de
            # pontos acumulados do jogo.
    total_pontos = carregar_pontuacao()
    
    # Renderiza o texto do total acumulado de pontos, novamente 
            # com antialiasing e na cor LARANJA.
    texto_total = fonte.render(f"Total Acumulado: {total_pontos}", True, LARANJA)
    
    # Desenha o texto do total de pontos centralizado 
            # horizontalmente e um terço abaixo na tela.
    tela.blit(texto_total, (LARGURA_TELA // 2 - texto_total.get_width() // 2, ALTURA_TELA // 3))

    # Cria um retângulo que funcionará como botão de 'Jogar'. 
    # As coordenadas e dimensões são especificadas.
    botao_jogar = pygame.Rect(LARGURA_TELA // 2 - 60, ALTURA_TELA // 2, 120, 50)
    
    # Desenha o retângulo do botão na tela na cor LARANJA.
    pygame.draw.rect(tela, LARANJA, botao_jogar)
    
    # Renderiza o texto 'Jogar' na cor BRANCO, também com antialiasing.
    texto_jogar = fonte.render("Jogar", True, BRANCO)
    
    # Posiciona o texto 'Jogar' centralizado dentro do botão.
    tela.blit(texto_jogar, (botao_jogar.x + 25, botao_jogar.y + 10))
    
    # Atualiza a tela inteira para mostrar todos os elementos
            # desenhados, garantindo que tudo seja exibido simultaneamente.
    pygame.display.flip()
    
    # Retorna o retângulo do botão 'Jogar', que pode ser usado 
            # para detectar cliques do mouse posteriormente.
    return botao_jogar


# Define a função principal do jogo chamada 'jogo'.
def jogo():
    
    # Usa a palavra-chave 'global' para poder modificar 
            # variáveis globais dentro da função.
    global pos_x_jogador, tempo_jogo, jogo_rodando, pontos, velocidade_obstaculo, obstaculos

    # Reseta as variáveis do jogo para o estado inicial
            # para um novo jogo.

    # Zera os pontos do jogador.
    pontos = 0  

    # Define a velocidade inicial dos obstáculos.
    velocidade_obstaculo = 5

    # Limpa a lista de obstáculos, começando o jogo sem 
            # nenhum obstáculo na tela.
    obstaculos = []  

    # Cria o retângulo que representa o jogador no jogo. A função 'pygame.Rect' é 
            # usada para definir a posição e tamanho do jogador.
    # 'pos_x_jogador' e 'pos_y_jogador' são as coordenadas iniciais, e
            # 'imagem_jogador.get_width()' e 'imagem_jogador.get_height()'
            # são as dimensões do jogador baseadas na imagem carregada.
    jogador = pygame.Rect(pos_x_jogador, pos_y_jogador, imagem_jogador.get_width(), imagem_jogador.get_height())

    # Inicia o loop principal do jogo, que continuará 
            # enquanto 'jogo_rodando' for verdadeiro.
    while jogo_rodando:
        
        # Desenha a imagem de fundo na tela cada vez que o loop 
                # executa.
        # Isso garante que o fundo seja redesenhado para cobrir 
                # quaisquer imagens de obstáculos ou do jogador do frame anterior.
        tela.blit(imagem_fundo, (0, 0))

        # Processa todos os eventos da fila de eventos do Pygame.
        for evento in pygame.event.get():
        
            # Se o evento for do tipo QUIT (clicar no botão de fechar a
                    # janela), fecha o Pygame e termina o script.
            if evento.type == pygame.QUIT:

                # Desinicializa todos os módulos do Pygame.
                pygame.quit()

                # Sai do script, interrompendo o programa.
                sys.exit()  


        # Obtém o estado atual de todas as teclas.
        teclas = pygame.key.get_pressed()
        
        # Verifica se a tecla esquerda está pressionada e se o
                # jogador não está no limite esquerdo da tela.
        if teclas[pygame.K_LEFT] and pos_x_jogador > 0:
        
            # Move o jogador para a esquerda, subtraindo da posição x 
                    # do jogador a 'velocidade_jogador'.
            pos_x_jogador -= velocidade_jogador
        
        # Verifica se a tecla direita está pressionada e se o 
                # jogador não está no limite direito da tela.
        if teclas[pygame.K_RIGHT] and pos_x_jogador < LARGURA_TELA - imagem_jogador.get_width():
        
            # Move o jogador para a direita, adicionando à posição x 
                    # do jogador a 'velocidade_jogador'.
            pos_x_jogador += velocidade_jogador

        # Atualiza a posição x do retângulo do jogador para
                # refletir movimentos horizontais.
        jogador.x = pos_x_jogador
        
        # Mantém a posição y do jogador constante, já que ele 
                # se move apenas horizontalmente.
        jogador.y = pos_y_jogador

        # Verifica se o tempo de jogo é um múltiplo do intervalo
                # definido para a criação de obstáculos.
        if tempo_jogo % intervalo_obstaculos == 0:
        
            # Chama a função para criar um novo obstáculo.
            criar_obstaculo()

        # Chama a função para atualizar a posição e verificar
                # colisões dos obstáculos.
        atualizar_obstaculos(jogador)
        
        # Itera sobre cada obstáculo na lista para desenhá-los na tela.
        for obstaculo in obstaculos:
            
            # Desenha o obstáculo na tela na posição especificada
                    # pelo seu retângulo.
            tela.blit(imagem_obstaculo, obstaculo.topleft)

        # Desenha o jogador na tela na posição atual.
        tela.blit(imagem_jogador, (pos_x_jogador, pos_y_jogador))

        # Chama a função para exibir a pontuação atual na tela.
        exibir_pontuacao()

        # Incrementa o contador de tempo do jogo.
        tempo_jogo += 1

        # Atualiza a tela para mostrar o novo estado do jogo.
        pygame.display.flip()
        
        # Limita a taxa de atualização do jogo a 30 quadros por segundo.
        pygame.time.Clock().tick(30)


    # Salva a pontuação acumulada ao final do jogo
    salvar_pontuacao()

# Loop infinito para manter a exibição do menu e 
        # aguardar ações do usuário.
while True:
    
    # Preenche a tela com a cor branca antes de desenhar
            # os elementos do menu.
    tela.fill(BRANCO)
    
    # Chama a função 'mostrar_menu' que cria e exibe os elementos
            # do menu, incluindo o botão 'Jogar'.
    # 'botao_jogar' recebe o retângulo do botão 'Jogar' para
            # posterior detecção de cliques.
    botao_jogar = mostrar_menu()

    # Entra em um loop de eventos para processar todos os 
            # eventos na fila de eventos do Pygame.
    for evento in pygame.event.get():
    
        # Verifica se o evento é do tipo QUIT, o que ocorre quando o
                # usuário clica no botão de fechar a janela.
        if evento.type == pygame.QUIT:
            
            # Finaliza todos os módulos do Pygame, preparando 
                    # para a saída do programa.
            pygame.quit()
            
            # Encerra o programa, saindo completamente.
            sys.exit()
            
        # Verifica se um evento de clique do mouse foi registrado.
        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            # Verifica se a posição do clique colide com a área do botão 'Jogar'.
            if botao_jogar.collidepoint(evento.pos):
                
                # Define 'jogo_rodando' como True para iniciar o loop do jogo.
                jogo_rodando = True
                
                # Chama a função 'jogo', que inicia o loop principal do jogo.
                jogo()

    # Atualiza a tela para refletir quaisquer mudanças 
            # feitas ao desenhar o menu.
    pygame.display.flip()
    
    # Define a taxa de atualização da tela para 30 quadros por 
            # segundo, mantendo o jogo jogável e responsivo.
    pygame.time.Clock().tick(30)