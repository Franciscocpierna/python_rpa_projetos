# Importa a biblioteca pygame, usada para criar 
        # jogos e interfaces gráficas
import pygame

# Importa a biblioteca random, que inclui funções para
        # gerar números aleatórios
import random

# Importa a biblioteca sys, utilizada para acessar funções e
        # objetos que interagem com o ambiente do Python
import sys

# Importa a biblioteca os, que fornece funções para interagir
        # com o sistema operacional
import os

# Inicializa todos os módulos importados do pygame, 
        # necessários para a configuração inicial
pygame.init()

# Define uma cor usando uma tupla com valores RGB para amarelo
AMARELO = (255, 223, 90)

# Define uma cor usando uma tupla com valores RGB para preto
PRETO = (0, 0, 0)

# Define as dimensões da janela do jogo
LARGURA, ALTURA = 400, 600

# Cria uma tela com as dimensões especificadas
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela do jogo
pygame.display.set_caption("Bee Honey")

# Carrega uma fonte padrão do sistema com tamanho 48 para o título
fonte_titulo = pygame.font.Font(None, 48)

# Carrega uma fonte padrão do sistema com tamanho 36 para a pontuação
fonte_pontuacao = pygame.font.Font(None, 36)

# Carrega a imagem da abelha do arquivo especificado
abelha_imagem = pygame.image.load("abelha.png")

# Redimensiona a imagem da abelha para 50x50 pixels
abelha_imagem = pygame.transform.scale(abelha_imagem, (50, 50))

# Carrega a imagem da aranha do arquivo especificado
aranha_imagem = pygame.image.load("aranha.png")

# Redimensiona a imagem da aranha para 60x60 pixels
aranha_imagem = pygame.transform.scale(aranha_imagem, (60, 60))

# Carrega a imagem da fruta do arquivo especificado
fruta_imagem = pygame.image.load("fruta.png")

# Redimensiona a imagem da fruta para 20x20 pixels
fruta_imagem = pygame.transform.scale(fruta_imagem, (20, 20))

# Define o nome do arquivo onde a pontuação será salva
ARQUIVO_PONTUACAO = "pontuacao.txt"

# Define a velocidade inicial da abelha
velocidade_abelha = 5

# Define a velocidade inicial base para as aranhas
velocidade_aranha_base = 2

# Define a posição inicial X da abelha (no centro da tela)
abelha_x = LARGURA // 2

# Define a posição inicial Y da abelha (80 pixels 
        # acima da parte inferior da tela)
abelha_y = ALTURA - 80

# Inicializa a pontuação como zero
pontuacao = 0

# Define o estado inicial do jogo como não jogando
jogando = False

# Define o número máximo de aranhas na tela ao mesmo tempo
max_aranhas = 5

# Cria uma lista vazia para armazenar as aranhas
aranhas = []

# Cria uma lista vazia para armazenar as frutas
frutas = []


# Define a função 'carregar_pontuacao' para carregar a 
        # pontuação a partir de um arquivo de texto.
def carregar_pontuacao():
    
    # Utiliza 'global' para modificar a variável 'pontuacao' 
            # que foi definida fora do escopo local da função.
    global pontuacao
    
    # Verifica se o arquivo de pontuação existe no 
            # diretório atual do script.
    if os.path.exists(ARQUIVO_PONTUACAO):
    
        # Abre o arquivo de pontuação em modo de leitura ('r').
        with open(ARQUIVO_PONTUACAO, "r") as arquivo:
        
            # Tenta executar o bloco de código dentro do 'try'.
            try:
            
                # Lê a pontuação do arquivo, remove quaisquer vírgulas (para
                        # tratar números formatados) e converte para inteiro.
                pontuacao = int(arquivo.read().replace(",", ""))
            
            # Captura o erro 'ValueError' que ocorre se a conversão para inteiro 
                    # falhar (por exemplo, se o arquivo estiver vazio ou 
                    # contiver texto não numérico).
            except ValueError:
            
                # Se um erro de valor ocorrer, define a pontuação como 0.
                pontuacao = 0


# Define a função 'salvar_pontuacao' que é responsável por 
        # gravar a pontuação atual no arquivo.
def salvar_pontuacao():
    
    # Abre o arquivo definido pela constante 'ARQUIVO_PONTUACAO' 
            # em modo de escrita ('w'),
            # que limpa o conteúdo existente do arquivo 
            # antes de escrever novos dados.
    with open(ARQUIVO_PONTUACAO, "w") as arquivo:
        
        # Escreve a pontuação atual no arquivo, formatando-a 
                # com vírgulas para milhares.
        # O uso de ':' dentro das chaves é uma funcionalidade de 
                # formatação do Python que adiciona separadores de milhar.
        arquivo.write(f"{pontuacao:,}")

# Chama a função 'carregar_pontuacao' para ler a pontuação 
        # salva do arquivo no início do programa.
# Isso garante que a pontuação mais recente seja carregada quando o
        # jogo for iniciado, permitindo a continuidade do 
        # progresso do jogador.
carregar_pontuacao()


# Define a função 'nova_aranha' para adicionar uma nova
        # aranha à lista de aranhas no jogo.
def nova_aranha():
    
    # Verifica se o número atual de aranhas é menor que o 
            # limite máximo permitido.
    if len(aranhas) < max_aranhas:
        
        # Gera uma posição aleatória no eixo X dentro da largura da tela,
                # subtraindo a largura da imagem da aranha para evitar que 
                # parte dela fique fora da tela.
        x = random.randint(0, LARGURA - aranha_imagem.get_width())
        
        # Define a posição inicial no eixo Y da aranha como um valor negativo 
                # igual à altura da imagem, fazendo com que ela comece fora da 
                # tela e "desça" para dentro dela.
        y = -aranha_imagem.get_height()
        
        # Define a velocidade no eixo Y da aranha, que aumenta conforme a pontuação
                # do jogador. A divisão por 10 faz com que o aumento da
                # velocidade ocorra de forma gradativa.
        velocidade_y = velocidade_aranha_base + pontuacao // 10
        
        # Escolhe aleatoriamente uma direção horizontal (esquerda ou direita)
                # e uma velocidade horizontal entre 1 e 3.
        velocidade_x = random.choice([-1, 1]) * random.randint(1, 3)
        
        # Adiciona a nova aranha à lista de aranhas, utilizando um dicionário 
                # para armazenar suas propriedades como posição e velocidade.
        aranhas.append({"x": x, "y": y, "velocidade_y": velocidade_y, "velocidade_x": velocidade_x})


# Define a função 'nova_fruta' que é responsável por adicionar
        # uma nova fruta ao jogo.
def nova_fruta():
    
    # Gera uma posição aleatória para a fruta no eixo X dentro
            # dos limites da tela,
    # subtraindo a largura da imagem da fruta para garantir
            # que ela fique completamente visível.
    x = random.randint(0, LARGURA - fruta_imagem.get_width())
    
    # Define a posição inicial Y da fruta como um valor negativo
            # igual à altura da imagem,
    # fazendo com que a fruta comece fora da tela e "caia" 
            # para dentro dela.
    y = -fruta_imagem.get_height()
    
    # Adiciona a nova fruta à lista de frutas, armazenando suas 
            # coordenadas (x, y) em um dicionário.
    frutas.append({"x": x, "y": y})


# Define a função 'exibir_pontuacao' que é responsável por
        # renderizar e mostrar a pontuação do jogador na tela.
def exibir_pontuacao():
    
    # Renderiza o texto da pontuação usando a fonte de pontuação 
            # definida, formatando o número com separadores de milhar.
    # O segundo argumento 'True' habilita o anti-aliasing do 
            # texto, e 'PRETO' define a cor do texto.
    texto = fonte_pontuacao.render(f"Pontuação: {pontuacao:,}", True, PRETO)
    
    # Desenha o texto renderizado na tela na posição (10, 10), 
            # que é próxima ao canto superior esquerdo.
    tela.blit(texto, (10, 10))


# Define a função 'colisao' que recebe dois dicionários representando
        # objetos do jogo (como frutas e aranhas) e verifica se
        # eles se sobrepõem.
def colisao(obj1, obj2):
    
    # Retorna True se e somente se todas as seguintes 
            # condições forem verdadeiras:
    return (
        
        # A borda esquerda de obj1 está à esquerda da 
                # borda direita de obj2.
        obj1["x"] < obj2["x"] + obj2["largura"] and
        
        # A borda direita de obj1 está à direita da borda
                # esquerda de obj2.
        obj1["x"] + obj1["largura"] > obj2["x"] and
        
        # A borda superior de obj1 está acima da borda
                # inferior de obj2.
        obj1["y"] < obj2["y"] + obj2["altura"] and
        
        # A borda inferior de obj1 está abaixo da borda
                # superior de obj2.
        obj1["y"] + obj1["altura"] > obj2["y"]
    )


# Define a função 'menu_inicial' que é usada para 
        # mostrar a tela de início do jogo.
def menu_inicial():
    
    # Preenche a tela inteira com a cor amarela definida anteriormente.
    tela.fill(AMARELO)
    
    # Chama a função 'exibir_texto' para renderizar e 
            # mostrar o título do jogo na tela.
    # O título "Bee Honey" é centralizado horizontalmente (LARGURA // 2) e 
            # colocado um quarto abaixo do topo da tela (ALTURA // 4).
    exibir_texto("Bee Honey", fonte_titulo, PRETO, LARGURA // 2, ALTURA // 4)
    
    # Chama a função 'exibir_texto' para mostrar a pontuação
            # atual no centro da tela.
    # A pontuação é centralizada horizontalmente e colocada
            # no meio da altura da tela (ALTURA // 2).
    exibir_texto(f"Pontuação: {pontuacao:,}", fonte_pontuacao, PRETO, LARGURA // 2, ALTURA // 2)
    
    # Chama a função 'exibir_texto' para exibir uma instrução 
            # para o jogador começar a jogar.
    # "Clique para Jogar" é mostrado centralizado horizontalmente e
            # um pouco mais abaixo do meio da tela (ALTURA // 1.5).
    exibir_texto("Clique para Jogar", fonte_pontuacao, PRETO, LARGURA // 2, ALTURA // 1.5)
    
    # Atualiza a tela para mostrar todos os elementos renderizados.
    pygame.display.flip()

    # Inicializa uma variável 'aguardando' como True, usada para
            # manter o menu ativo até que o jogador inicie o jogo.
    aguardando = True

    # Inicia um loop que continua enquanto a variável 'aguardando' for True.
    while aguardando:
        
        # Itera sobre a fila de eventos do Pygame para processar
                # cada evento ocorrido.
        for evento in pygame.event.get():
        
            # Verifica se o tipo do evento é QUIT, que ocorre, por exemplo, 
                    # quando o usuário clica no botão de fechar a janela.
            if evento.type == pygame.QUIT:
            
                # Chama a função 'pygame.quit()' para finalizar todos os 
                        # módulos do Pygame de forma limpa.
                pygame.quit()
                
                # Chama 'sys.exit()' para encerrar o script Python, garantindo 
                        # que nenhum processo fique pendente.
                sys.exit()
                
            # Verifica se o tipo do evento é MOUSEBUTTONDOWN, que ocorre 
                    # quando um botão do mouse é pressionado.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Altera o valor da variável 'aguardando' para False, 
                        # encerrando o loop e permitindo que o jogo prossiga.
                aguardando = False


# Define a função principal do jogo chamada 'jogo'.
def jogo():
    
    # Declara variáveis globais que serão modificadas 
            # dentro desta função.
    global abelha_x, abelha_y, pontuacao, jogando, velocidade_abelha, velocidade_aranha_base

    # Inicializa a velocidade da abelha no início do jogo.
    velocidade_abelha = 5
    
    # Inicializa a velocidade base das aranhas no início do jogo.
    velocidade_aranha_base = 2
    
    # Limpa a lista de aranhas para reiniciar o jogo sem 
            # nenhuma aranha na tela.
    aranhas.clear()
    
    # Limpa a lista de frutas para reiniciar o jogo sem
            # nenhuma fruta na tela.
    frutas.clear()

    # Inicializa um temporizador para o controle de
            # spawn de aranhas.
    aranha_timer = 0
    
    # Inicializa um temporizador para o controle de 
            # spawn de frutas.
    fruta_timer = 0
    
    # Cria um objeto de relógio para controlar a taxa
            # de atualização do jogo.
    clock = pygame.time.Clock()
    
    # Define a variável 'jogando' como True para iniciar o
            # loop principal do jogo.
    jogando = True


    # Inicia um loop que continua executando enquanto a 
            # variável 'jogando' for True.
    while jogando:
        
        # Preenche o fundo da tela com a cor amarela definida
                # anteriormente para limpar o quadro anterior.
        tela.fill(AMARELO)
    
        # Itera sobre todos os eventos capturados pelo Pygame para 
                # processar ações como fechar o jogo.
        for evento in pygame.event.get():
        
            # Verifica se o evento capturado é do tipo QUIT, que é 
                    # acionado quando o jogador tenta fechar a janela do jogo.
            if evento.type == pygame.QUIT:
            
                # Chama a função 'salvar_pontuacao' para gravar a 
                        # pontuação atual antes de fechar o jogo.
                salvar_pontuacao()
                
                # Finaliza todos os módulos do Pygame, preparando 
                        # para o fechamento do programa.
                pygame.quit()
                
                # Sai do programa utilizando 'sys.exit()' para
                        # encerrar completamente a execução.
                sys.exit()


        # Captura o estado atual de todas as teclas pressionadas.
        teclas = pygame.key.get_pressed()
        
        # Verifica se a tecla de seta para a esquerda está pressionada e
                # se a abelha não está na borda esquerda da tela.
        if teclas[pygame.K_LEFT] and abelha_x > 0:
        
            # Move a abelha para a esquerda diminuindo a coordenada X 
                    # pela velocidade definida.
            abelha_x -= velocidade_abelha
        
        # Verifica se a tecla de seta para a direita está pressionada e 
                # se a abelha não está na borda direita da tela.
        if teclas[pygame.K_RIGHT] and abelha_x < LARGURA - abelha_imagem.get_width():
        
            # Move a abelha para a direita aumentando a coordenada X 
                    # pela velocidade definida.
            abelha_x += velocidade_abelha
        
        # Verifica se a tecla de seta para cima está pressionada e se
                    # a abelha não está na borda superior da tela.
        if teclas[pygame.K_UP] and abelha_y > 0:
        
            # Move a abelha para cima diminuindo a coordenada Y 
                    # pela velocidade definida.
            abelha_y -= velocidade_abelha
        
        # Verifica se a tecla de seta para baixo está pressionada e
                # se a abelha não está na borda inferior da tela.
        if teclas[pygame.K_DOWN] and abelha_y < ALTURA - abelha_imagem.get_height():
        
            # Move a abelha para baixo aumentando a coordenada Y 
                    # pela velocidade definida.
            abelha_y += velocidade_abelha
        
        # Verifica se o temporizador de aranhas excedeu o 
                # limite de 100 ciclos.
        # Aumentar temporizador para reduzir a criação de aranhas
        if aranha_timer > 100:  
            
            # Gera uma nova aranha chamando a função específica.
            nova_aranha()
            
            # Reinicia o temporizador de aranhas após gerar uma nova.
            aranha_timer = 0
        
        # Incrementa o temporizador de aranhas a cada ciclo do jogo.
        aranha_timer += 1


        # Itera sobre a lista de aranhas criadas para
                # atualizar suas posições.
        # Utiliza uma cópia da lista para permitir 
                # modificações durante a iteração.
        for aranha in aranhas[:]:  
            
            # Atualiza a posição vertical da aranha de acordo 
                    # com sua velocidade vertical.
            aranha["y"] += aranha["velocidade_y"]
            
            # Atualiza a posição horizontal da aranha de acordo 
                    # com sua velocidade horizontal.
            aranha["x"] += aranha["velocidade_x"]
            
            # Verifica se a aranha atingiu os limites horizontais da tela.
            if aranha["x"] <= 0 or aranha["x"] >= LARGURA - aranha_imagem.get_width():
                
                # Inverte a direção horizontal da aranha ao
                        # atingir a borda da tela.
                aranha["velocidade_x"] *= -1
        
            # Verifica se a aranha ultrapassou a borda 
                    # inferior da tela.
            if aranha["y"] > ALTURA:
                
                # Remove a aranha da lista se ela sair da
                        # área visível da tela.
                aranhas.remove(aranha)
                
            # Checa se houve colisão entre a abelha e a aranha
                    # usando a função 'colisao'.
            elif colisao({"x": abelha_x, "y": abelha_y, "largura": abelha_imagem.get_width(), "altura": abelha_imagem.get_height()},
                         {"x": aranha["x"], "y": aranha["y"], "largura": aranha_imagem.get_width(), "altura": aranha_imagem.get_height()}):
                
                # Encerra o jogo ao detectar uma colisão entre a 
                        # abelha e uma aranha.
                jogando = False


        # Seção do código que gerencia o aparecimento e movimento das frutas.
        # Verifica se o temporizador de frutas excedeu 150 ciclos para 
                # limitar a frequência de criação de novas frutas.
        if fruta_timer > 150:  
            
            # Cria uma nova fruta chamando a função 'nova_fruta'.
            nova_fruta()
            
            # Reinicia o temporizador de frutas após criar uma nova fruta
                    # para manter o intervalo controlado.
            fruta_timer = 0
            
        # Incrementa o temporizador de frutas a cada ciclo do
                # loop principal do jogo.
        fruta_timer += 1
        
        # Itera sobre a lista de frutas para atualizar suas
                # posições e verificar colisões.
        # Faz uma cópia da lista para permitir modificação 
                # durante a iteração.
        for fruta in frutas[:]:  
            
            # Move a fruta para baixo aumentando a posição Y 
                    # em 3 unidades a cada ciclo.
            fruta["y"] += 3
            
            # Verifica se a fruta ultrapassou a borda inferior da tela.
            if fruta["y"] > ALTURA:
            
                # Remove a fruta da lista se ela sair da 
                        # área visível da tela.
                frutas.remove(fruta)
                
            # Utiliza a função 'colisao' para verificar se há
                    # colisão entre a abelha e a fruta.
            elif colisao({"x": abelha_x, "y": abelha_y, "largura": abelha_imagem.get_width(), "altura": abelha_imagem.get_height()},
                         {"x": fruta["x"], "y": fruta["y"], "largura": fruta_imagem.get_width(), "altura": fruta_imagem.get_height()}):
                
                # Remove a fruta da lista ao detectar uma colisão, significando
                        # que a abelha 'coletou' a fruta.
                frutas.remove(fruta)
                
                # Incrementa a pontuação do jogador ao coletar uma fruta.
                pontuacao += 1
                
                # Aumenta a velocidade da abelha para adicionar mais desafio 
                        # conforme o jogador coleta mais frutas.
                velocidade_abelha += 0.2
                
                # Aumenta a velocidade base das aranhas, tornando o jogo 
                        # progressivamente mais difícil.
                velocidade_aranha_base += 0.1


        # Desenha a abelha na tela usando a imagem carregada, nas 
                # coordenadas atualizadas de sua posição.
        tela.blit(abelha_imagem, (abelha_x, abelha_y))
        
        # Itera sobre a lista de aranhas para desenhar cada uma na tela.
        for aranha in aranhas:
            
            # Desenha cada aranha na tela usando sua imagem e 
                    # posição atual dentro da lista 'aranhas'.
            tela.blit(aranha_imagem, (aranha["x"], aranha["y"]))
        
        # Itera sobre a lista de frutas para desenhar cada uma na tela.
        for fruta in frutas:
            
            # Desenha cada fruta na tela usando sua imagem e 
                    # posição atual dentro da lista 'frutas'.
            tela.blit(fruta_imagem, (fruta["x"], fruta["y"]))
        
        # Chama a função 'exibir_pontuacao' para renderizar a 
                # pontuação atual na tela.
        exibir_pontuacao()
        
        # Atualiza o display inteiro; essa função deve ser chamada 
                # uma vez por frame para refletir as mudanças na tela.
        pygame.display.flip()
        
        # Controla a taxa de atualização do jogo, garantindo que 
                # ele não execute mais rápido do que 30 frames por segundo.
        clock.tick(30)


    # Salvar a pontuação ao final do jogo
    salvar_pontuacao()

# Define a função 'exibir_texto' que facilita a
        # renderização de texto na tela.
def exibir_texto(texto, fonte, cor, x, y):
    
    # Renderiza o texto usando a fonte e cor especificadas.
    # O segundo parâmetro 'True' ativa o anti-aliasing, 
            # tornando o texto mais suave.
    superficie = fonte.render(texto, True, cor)
    
    # Obtém um retângulo que envolve o texto renderizado e
            # define sua posição central com base em (x, y).
    rect = superficie.get_rect(center=(x, y))
    
    # Desenha o texto renderizado na tela na posição 
            # especificada pelo retângulo.
    tela.blit(superficie, rect)

# Inicia o loop infinito principal do jogo.
while True:
    
    # Chama a função 'menu_inicial' para exibir o menu de 
            # início e esperar até que o jogador decida iniciar o jogo.
    menu_inicial()
    
    # Chama a função 'jogo' para executar o ciclo principal do jogo 
            # até que um evento final (como perder o jogo) 
            # retorne ao menu inicial.
    jogo()