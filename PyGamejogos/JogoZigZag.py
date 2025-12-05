# Importa a biblioteca Pygame, essencial para 
        # gráficos e criação de jogos
import pygame

# Importa a biblioteca Random para gerar valores aleatórios, usada 
        # para criar variações na pista e na posição das moedas
import random

# Importa a biblioteca Sys para operações de sistema, 
        # como finalizar o jogo
import sys

# Importa a biblioteca Math para funções matemáticas, como 
        # cálculo de distância entre objetos (bola e moedas)
import math

# Importa a biblioteca Os para manipulação de arquivos e sistema,
        # usada para ler e escrever o arquivo de pontuação
import os

# Inicializa todos os módulos do Pygame para preparar o ambiente do jogo
pygame.init()

# Configurações da tela do jogo
LARGURA_TELA = 800

# Define a altura da tela em pixels
ALTURA_TELA = 600

# Cria a tela do jogo com as dimensões especificadas
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Define o título da janela do jogo que aparece na barra superior
pygame.display.set_caption("Jogo ZigZag")

# Configurações da bola do jogo
bola_raio = 10

# Define a velocidade inicial horizontal da
        # bola (velocidade ao se mover para os lados)
velocidade_bola = 1

# Define a posição inicial horizontal da bola no centro da tela
bola_x = LARGURA_TELA // 2

# Define a posição inicial vertical da bola 
        # ajustando-a acima do centro da tela
bola_y = ALTURA_TELA // 2 - 100

# Inicializa a variável indicando que a bola não está caindo
caindo = False

# Configurações da pista do jogo
largura_pista = 100

# Define a altura de cada segmento da pista
altura_segmento = 50

# Define a velocidade inicial da pista, que se moverá 
        # para dar a impressão de movimento
velocidade_pista_inicial = 1

# Define a velocidade atual da pista, começando 
        # pela velocidade inicial
velocidade_pista = velocidade_pista_inicial

# Define o valor de aceleração da pista para tornar o 
        # jogo mais difícil com o tempo
aceleracao_pista = 0.001

# Cria uma lista vazia que armazenará todos os 
        # segmentos da pista
segmentos = []

# Configurações das moedas do jogo
moedas = []

# Define o raio de cada moeda para representar seu tamanho
raio_moeda = 8

# Define a margem para garantir que a moeda fique dentro da pista
margem_moeda = 10

# Definição das cores utilizadas no jogo
AZUL_CLARO = (100, 149, 237)

# Cor alternativa da pista
AZUL_ESCURO = (65, 105, 225)

# Cor da bola e do texto de pontuação
PRETO = (0, 0, 0)

# Cor de fundo da tela
BRANCO = (255, 255, 255)

# Cor das moedas
AMARELO = (255, 223, 0)

# Configuração das fontes para pontuação e texto de menu
fonte_pontuacao = pygame.font.SysFont(None, 36)

# Define o tamanho da fonte para o menu principal
fonte_menu = pygame.font.SysFont(None, 48)

# Caminho para o arquivo que salva a pontuação mais alta
caminho_score = "score.txt"

# Variável para controle do movimento horizontal da bola
movimento_horizontal = 0


# Função para criar o próximo segmento da pista em ziguezague
# Esta função é responsável por adicionar um novo pedaço da pista,
# que se move para a direita ou esquerda, 
        # criando o efeito de ziguezague.
def criar_segmento():
    
    """
    Cria um novo segmento de pista na direção atual.
    """
    
    # Verifica se ainda não existe nenhum segmento criado na pista
    if len(segmentos) == 0:
        
        # Inicializa o primeiro segmento da pista e o 
                # posiciona no centro da tela
        novo_segmento = {
            
            # Define a posição horizontal (x) do segmento 
                    # como o centro da tela
            "x": LARGURA_TELA // 2,
            
            # Define a posição vertical (y) do segmento no meio da tela
            "y": ALTURA_TELA // 2,
            
            # Define a largura do segmento com base no valor 
                    # configurado para a pista
            "largura": largura_pista,
            
            # Define a direção do segmento aleatoriamente, 
                    # escolhendo entre -1 (esquerda) e 1 (direita)
            "direcao": random.choice([-1, 1])
        }
        
        # Adiciona este primeiro segmento à lista que 
                # armazena todos os segmentos da pista
        segmentos.append(novo_segmento)
    
    # Caso já existam segmentos na pista
    else:
        
        # Seleciona o último segmento criado para usá-lo 
                # como base para o próximo segmento
        ultimo_segmento = segmentos[-1]
        
        # Calcula a posição horizontal (x) do novo segmento com 
                # base na posição e direção do último segmento
        # Multiplica a direção (esquerda ou direita) pela metade da 
                # largura da pista para posicionamento
        novo_x = ultimo_segmento["x"] + ultimo_segmento["direcao"] * (largura_pista // 2)
        
        # Ajusta o novo segmento para que ele não ultrapasse os limites da tela
        # Garante que o segmento não vá muito para a esquerda ou para a direita
        novo_x = max(largura_pista // 2, min(LARGURA_TELA - largura_pista // 2, novo_x))
        
        # Cria o novo segmento baseado nas coordenadas calculadas e
                # uma nova direção aleatória
        novo_segmento = {
            
            # Define a posição horizontal (x) ajustada do novo segmento
            "x": novo_x,
            
            # Define a posição vertical (y) logo acima do último
                    # segmento, para continuação da pista
            "y": ultimo_segmento["y"] - altura_segmento,
            
            # Define a largura do novo segmento, mantendo a largura da pista
            "largura": largura_pista,
            
            # Escolhe aleatoriamente uma nova direção para o próximo 
                    # segmento, esquerda (-1) ou direita (1)
            "direcao": random.choice([-1, 1])
        }
        
        # Adiciona o novo segmento criado à lista de segmentos da 
                # pista para que ele seja exibido no jogo
        segmentos.append(novo_segmento)


    
    # Adiciona uma moeda aleatoriamente ao novo segmento da pista, 
            # desde que dentro dos limites da pista
    # Usa uma condição de 30% de chance para gerar uma 
            # moeda neste segmento
    if random.random() < 0.3:  
    
        # Calcula a posição horizontal da moeda (moeda_x) baseada 
                # na posição do segmento atual,
        # garantindo que a moeda fique dentro da largura da 
                # pista e respeitando uma margem de segurança
        moeda_x = novo_segmento["x"] + random.randint(
            -novo_segmento["largura"] // 3 + margem_moeda, 
            novo_segmento["largura"] // 3 - margem_moeda
        )
        
        # Calcula a posição vertical da moeda (moeda_y) para
                # que ela fique no meio do segmento verticalmente,
                # também com uma margem para evitar que fique
                # muito próxima das bordas
        moeda_y = novo_segmento["y"] - altura_segmento // 2 + margem_moeda
        
        # Adiciona a moeda na lista de moedas, salvando
                # suas coordenadas x e y
        moedas.append({"x": moeda_x, "y": moeda_y})


# Função para desenhar a pista com uma perspectiva 2D simulando 3D
# Esta função usa segmentos sobrepostos em formato de 
        # trapézio para dar um efeito de profundidade
def desenhar_pista():
    
    # Loop para percorrer todos os segmentos da pista, exceto o
            # último, que não tem um próximo segmento
    for i in range(len(segmentos) - 1):
        
        # Define o segmento atual como o segmento na posição i da lista
        segmento_atual = segmentos[i]
        
        # Define o próximo segmento como o segmento na posição i+1 da lista
        proximo_segmento = segmentos[i + 1]

        # Desenha o segmento da pista como um trapézio para 
                # simular perspectiva
        # O trapézio é desenhado entre as coordenadas dos 
                # segmentos atual e próximo,
                # criando um efeito de profundidade
        pygame.draw.polygon(
            
            tela,  # Desenha na tela principal do jogo
            AZUL_CLARO,  # Usa a cor definida para o trapézio (AZUL_CLARO)
            [
                # Ponto superior esquerdo do trapézio, calculado a
                        # partir do centro do segmento atual
                (segmento_atual["x"] - segmento_atual["largura"] // 2, segmento_atual["y"]),
                
                # Ponto superior direito do trapézio, calculado a 
                        # partir do centro do segmento atual
                (segmento_atual["x"] + segmento_atual["largura"] // 2, segmento_atual["y"]),
                
                # Ponto inferior direito do trapézio, calculado a 
                        # partir do centro do próximo segmento
                (proximo_segmento["x"] + proximo_segmento["largura"] // 2, proximo_segmento["y"]),
                
                # Ponto inferior esquerdo do trapézio, calculado a 
                        # partir do centro do próximo segmento
                (proximo_segmento["x"] - proximo_segmento["largura"] // 2, proximo_segmento["y"]),
                
            ]
        )


# Função para desenhar as moedas
# Esta função desenha cada moeda na tela, representando-as 
        # como pequenos círculos
def desenhar_moedas():
    
    # Loop para percorrer cada moeda presente na lista de moedas
    for moeda in moedas:
        
        # Desenha a moeda como um círculo na posição (x, y) da moeda
        # "tela" é onde o círculo será desenhado
        # "AMARELO" define a cor da moeda
        # "(int(moeda['x']), int(moeda['y']))" define a posição da 
                # moeda (convertida para números inteiros)
        # "raio_moeda" define o tamanho do círculo, que 
                # representa o tamanho da moeda
        pygame.draw.circle(tela, AMARELO, (int(moeda["x"]), int(moeda["y"])), raio_moeda)


# Função para reiniciar o jogo
# Esta função redefine as variáveis do jogo e recria os 
        # elementos principais para um novo início
def reiniciar_jogo():
    
    # Declara as variáveis globais para que possamos modificar os 
            # valores dentro da função
    global bola_x, bola_y, caindo, segmentos, moedas, pontuacao, velocidade_pista, velocidade_bola, movimento_horizontal
    
    # Limpa a lista de segmentos da pista, removendo
            # todos os segmentos existentes
    segmentos.clear()
    
    # Limpa a lista de moedas, removendo todas as moedas existentes
    moedas.clear()
    
    # Reinicia a pontuação para zero
    pontuacao = 0
    
    # Redefine a velocidade da pista para o valor inicial,
            # como se o jogo estivesse começando
    velocidade_pista = velocidade_pista_inicial
    
    # Redefine a velocidade da bola para o valor inicial
    velocidade_bola = 1

    # Reinicia o movimento horizontal da bola, fazendo 
            # com que ela comece parada
    movimento_horizontal = 0

    # Calcula o número de segmentos necessários para cobrir 
            # toda a altura da tela
    # Adiciona mais dois segmentos para garantir que a 
            # pista cubra toda a tela
    numero_segmentos = (ALTURA_TELA // altura_segmento) + 2
    
    # Cria os segmentos da pista necessários para cobrir a 
            # tela no início do jogo
    for _ in range(numero_segmentos):
        criar_segmento()
    
    # Define a posição inicial da bola no topo do primeiro segmento
    primeiro_segmento = segmentos[0]  # Primeiro segmento criado
    
    # Define a posição horizontal (x) da bola no centro 
            # do primeiro segmento
    bola_x = primeiro_segmento["x"]
    
    # Define a posição vertical (y) da bola logo acima do primeiro
            # segmento, com um pequeno espaço
    # 5 pixels acima para uma leve separação visual
    bola_y = primeiro_segmento["y"] - bola_raio - 5  
    
    # Define a variável 'caindo' como False, indicando que a
            # bola está no início sobre a pista
    caindo = False


# Função para mover a bola e verificar se ela saiu da pista
# Esta função atualiza a posição horizontal da bola e 
        # verifica se ela ainda está sobre a pista
def mover_bola():
    
    # Define as variáveis globais que precisam ser atualizadas
    global bola_x, bola_y, caindo

    # Atualiza a posição da bola na direção horizontal (esquerda ou direita)
    # Multiplica o movimento pela velocidade da bola 
            # para ajustar a distância que ela percorre
    bola_x += movimento_horizontal * velocidade_bola

    # Limita a posição horizontal da bola para que ela não saia da tela
    # "max" garante que a bola não vá além do limite esquerdo (0 + bola_raio)
    # "min" garante que a bola não vá além do limite direito (LARGURA_TELA - bola_raio)
    bola_x = max(bola_raio, min(LARGURA_TELA - bola_raio, bola_x))

    # Inicializa a variável que indica se a bola está sobre a pista
    sobre_segmento = False
    
    # Verifica se a bola está em cima de algum dos segmentos da pista
    for segmento in segmentos:
        
        # Calcula a distância vertical entre a bola e o segmento
        # Confere se a bola está na altura do segmento, considerando a
                # altura da bola e do segmento
        if abs(bola_y - segmento["y"]) <= bola_raio + altura_segmento // 2:
            
            # Verifica se a posição horizontal da bola está dentro 
                    # dos limites do segmento
            if segmento["x"] - segmento["largura"] // 2 <= bola_x <= segmento["x"] + segmento["largura"] // 2:
                
                # Define que a bola está sobre o segmento e 
                        # encerra a verificação
                sobre_segmento = True
                break

    # Se a bola não está sobre nenhum segmento, 
            # ativa o modo de queda
    if not sobre_segmento:
        caindo = True


# Função para verificar colisão com as moedas
# Esta função verifica se a bola encostou em alguma moeda, usando a 
        # distância entre elas para detectar a colisão
def verificar_colisao_moedas():
    
    # Declara as variáveis globais que serão 
            # modificadas (moedas e pontuação)
    global moedas, pontuacao
    
    # Itera sobre cada moeda na lista de moedas (a lista é copiada
            # com [:] para evitar erros ao modificar durante a iteração)
    for moeda in moedas[:]:
        
        # Calcula a distância entre a posição da bola e a posição da moeda
        # math.hypot calcula a distância usando o teorema de
                # Pitágoras (distância euclidiana)
        distancia = math.hypot(bola_x - moeda["x"], bola_y - moeda["y"])
        
        # Verifica se a distância entre a bola e a moeda é
                # menor que a soma dos raios
        # Isso significa que a bola "encostou" na moeda, 
                # indicando uma colisão
        if distancia < bola_raio + raio_moeda:
            
            # Remove a moeda da lista, pois ela foi coletada pela bola
            moedas.remove(moeda)
            
            # Incrementa a pontuação em 10 pontos ao coletar a moeda
            pontuacao += 10


# Função para ler a pontuação mais alta do arquivo
# Esta função verifica se existe um arquivo de pontuação e, 
        # se existir, lê a pontuação mais alta armazenada
def ler_pontuacao():
    
    # Verifica se o arquivo de pontuação existe no sistema
    if os.path.exists(caminho_score):
        
        # Abre o arquivo de pontuação no modo de leitura ("r") se ele existir
        with open(caminho_score, "r") as f:
            
            # Tenta ler o conteúdo do arquivo e converter para um número inteiro
            try:
                return int(f.read())
            
            # Se ocorrer algum erro (por exemplo, se o arquivo estiver
                    # vazio ou contiver dados inválidos).
            # Retorna 0 como valor padrão da pontuação.
            except:
                return 0
    
    # Se o arquivo não existir, retorna 0 como pontuação padrão
    else:
        return 0


# Função para salvar a pontuação mais alta no arquivo
# Esta função verifica se a pontuação atual é maior do 
        # que a pontuação mais alta salva.
# Caso seja, substitui a pontuação mais alta pelo novo 
        # valor e salva no arquivo.
def salvar_pontuacao(nova_pontuacao):
    
    # Chama a função 'ler_pontuacao' para obter a pontuação 
            # mais alta registrada no arquivo
    pontuacao_mais_alta = ler_pontuacao()
    
    # Compara a nova pontuação com a pontuação mais alta existente
    # Se a nova pontuação é maior, ela se torna a nova 
            # pontuação mais alta
    if nova_pontuacao > pontuacao_mais_alta:
        
        # Abre o arquivo de pontuação no modo de escrita ("w") para atualizar o valor
        # Se o arquivo já existia, ele será substituído pelo novo conteúdo;
        # se não existia, será criado um novo arquivo com esse nome
        with open(caminho_score, "w") as f:
            
            # Converte a nova pontuação para uma string e 
                    # escreve no arquivo
            f.write(str(nova_pontuacao))
            # Isso sobrescreve qualquer pontuação anterior
                    # com a nova pontuação mais alta


# Função principal do jogo
# Esta função é responsável por executar o loop principal do jogo, 
        # onde todas as ações do jogo acontecem, 
        # como atualização de posições, verificações de eventos e
        # desenho dos elementos na tela.
def jogo():
    
    # Declara variáveis globais que precisam ser atualizadas 
            # no loop principal
    global movimento_horizontal, caindo, bola_y, pontuacao, velocidade_pista, velocidade_bola
    
    # Define uma variável que controla se o jogo está rodando
    rodando = True
    
    # Cria um objeto para controlar o tempo e a taxa de atualização 
            # do jogo (frames por segundo - FPS)
    relogio = pygame.time.Clock()

    # Reinicia todas as variáveis e elementos do jogo, 
            # preparando para um novo início
    reiniciar_jogo()

    # Loop principal do jogo, que continua enquanto 'rodando' for True
    while rodando:
        
        # Preenche a tela com a cor branca para limpar os 
                # elementos desenhados anteriormente
        tela.fill(BRANCO)

        # Captura todos os eventos (ações) que ocorrem durante o 
                # jogo, como teclas pressionadas e fechamento da janela
        for evento in pygame.event.get():
            
            # Se o evento for de saída (fechamento da janela), encerra o jogo
            if evento.type == pygame.QUIT:
                pygame.quit()  # Finaliza o Pygame
                sys.exit()  # Encerra o programa
                
            # Verifica se uma tecla foi pressionada
            if evento.type == pygame.KEYDOWN:
                
                # Se a tecla pressionada for a seta para a esquerda, 
                        # define o movimento horizontal para -1 (esquerda)
                if evento.key == pygame.K_LEFT:
                    movimento_horizontal = -1
                    
                # Se a tecla pressionada for a seta para a direita, 
                        # define o movimento horizontal para 1 (direita)
                elif evento.key == pygame.K_RIGHT:
                    movimento_horizontal = 1
                    
            # Verifica se uma tecla foi liberada
            if evento.type == pygame.KEYUP:
                
                # Se a tecla liberada for a seta para a esquerda ou 
                        # para a direita, para o movimento horizontal
                if evento.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    movimento_horizontal = 0  # Para o movimento horizontal

        # Chama a função para desenhar a pista na tela
        desenhar_pista()

        # Chama a função para desenhar todas as moedas na tela
        desenhar_moedas()

        # Desenha a bola na tela, verificando se ela está 
                # em estado de queda ou não
        if not caindo:
            
            # Desenha a bola como um círculo preenchido em preto
                    # na tela, se não estiver caindo
            # "tela" é onde o círculo será desenhado (a janela principal do jogo)
            # "PRETO" define a cor do círculo (cor da bola)
            # "(int(bola_x), int(bola_y))" define a posição central
                    # do círculo (coordenadas da bola)
            # "bola_raio" define o tamanho do círculo, que representa a bola
            pygame.draw.circle(tela, PRETO, (int(bola_x), int(bola_y)), bola_raio)
        
        else:
            
            # Se a bola estiver em estado de queda (fora da pista), faz 
                    # com que ela caia verticalmente
            # Adiciona 20 unidades à posição vertical da 
                    # bola (eixo Y), simulando a gravidade
            bola_y += 20  
            
            # Desenha a bola novamente na nova posição (mais baixa), 
                    # para que o movimento de queda seja visível
            pygame.draw.circle(tela, PRETO, (int(bola_x), int(bola_y)), bola_raio)
            
            # Verifica se a bola caiu completamente fora da tela (além 
                    # da altura da tela + o raio da bola)
            if bola_y > ALTURA_TELA + bola_raio:
                
                # Salva a pontuação atual, pois o jogo terminou (a 
                        # bola caiu fora da tela)
                salvar_pontuacao(pontuacao)
                
                # Define 'rodando' como False para encerrar o loop 
                        # principal do jogo, voltando ao menu
                rodando = False

        # Movimenta a bola horizontalmente e verifica 
                # se ela saiu da pista
        mover_bola()

        # Se a bola não está em queda, verifica se houve colisão
                # entre a bola e as moedas
        if not caindo:
            
            # Chama a função para verificar colisão entre a bola e as moedas
            # Se houver colisão, a moeda é removida e a pontuação aumenta
            verificar_colisao_moedas()

        # Move os segmentos da pista automaticamente para simular
                # que a pista está se movendo para baixo
        # Isso cria a ilusão de que a bola está avançando pela pista
        for segmento in segmentos:
            
            # Aumenta a posição Y de cada segmento de acordo 
                    # com a velocidade da pista
            # Assim, os segmentos da pista se movem para baixo
            segmento["y"] += velocidade_pista

        # Move as moedas automaticamente para baixo, junto com a pista
        for moeda in moedas:
            
            # Aumenta a posição Y de cada moeda de acordo com a velocidade da pista,
            # para que as moedas se movam junto com os segmentos da pista
            moeda["y"] += velocidade_pista

        # Remove os segmentos que saíram da tela para otimizar a memória e processamento
        # Filtra apenas os segmentos que ainda estão dentro dos limites da tela
        segmentos[:] = [segmento for segmento in segmentos if segmento["y"] < ALTURA_TELA]

        # Remove as moedas que saíram da tela (não são mais 
                # visíveis nem precisam ser processadas)
        # Filtra apenas as moedas que ainda estão dentro dos limites da tela
        moedas[:] = [moeda for moeda in moedas if moeda["y"] < ALTURA_TELA]


        # Adicionar novos segmentos de pista conforme a direção
        # Este loop cria segmentos adicionais no topo da pista 
                # conforme ela se move para baixo,
                # garantindo que a pista continue na tela
        while len(segmentos) < (ALTURA_TELA // altura_segmento) + 2:
            
            # Chama a função para criar um novo segmento de 
                    # pista no topo da lista
            criar_segmento()

        # Aceleração gradual da pista
        # Incrementa a velocidade da pista em cada ciclo do loop, 
                # tornando o jogo gradualmente mais rápido
        velocidade_pista += aceleracao_pista
        
        # Aumenta também a velocidade da bola para 
                # acompanhar a aceleração da pista
        velocidade_bola += 0.001

        # Exibir a pontuação do jogador na tela
        # Cria um texto renderizado com a pontuação atual usando a
                # fonte de pontuação configurada
        # "f" antes da string permite incorporar a variável 
                # pontuacao diretamente no texto exibido
        texto_pontuacao = fonte_pontuacao.render(f"Pontuação: {pontuacao}", True, PRETO)
        
        # Desenha (blit) o texto de pontuação na tela, na 
                # posição superior esquerda (10, 10)
        tela.blit(texto_pontuacao, (10, 10))

        # Atualização da tela e controle de FPS (Frames por Segundo)
        # Atualiza a tela, exibindo todas as mudanças feitas 
                # desde a última atualização
        pygame.display.flip()
        
        # Define a taxa de atualização para 60 FPS, limitando o 
                # jogo a essa velocidade
        # Isso proporciona uma jogabilidade mais suave e constante
        relogio.tick(60)


    # Após perder, salva a pontuação e retorna ao menu
    salvar_pontuacao(pontuacao)

# Tela de Menu
# Esta função exibe o menu principal do jogo, incluindo o título, um 
        # botão de instrução e a pontuação mais alta.
def mostrar_menu():
    
    # Lê a pontuação mais alta a partir do arquivo e a
            # armazena em uma variável
    pontuacao_mais_alta = ler_pontuacao()
    
    # Define a fonte do título do menu com tamanho 72
    font_titulo = pygame.font.SysFont(None, 72)
    
    # Define a fonte do botão de instrução com tamanho 48
    font_botao = pygame.font.SysFont(None, 48)
    
    # Renderiza o texto do título do jogo na fonte 'font_titulo'
    # "Jogo ZigZag" é o texto exibido, 'True' permite 
            # antialiasing (suavização), 'PRETO' define a cor
    titulo = font_titulo.render("Jogo ZigZag", True, PRETO)
    
    # Renderiza o texto do botão de instrução, indicando que o
            # jogador deve pressionar "ESPAÇO" para começar o jogo
    botao_jogar = font_botao.render("Pressione ESPAÇO para Jogar", True, PRETO)
    
    # Renderiza o texto da pontuação mais alta obtida, usando a 
            # fonte de pontuação configurada
    # Exibe a pontuação mais alta com o texto "Pontuação Mais Alta:"
    texto_pontuacao = fonte_pontuacao.render(f"Pontuação Mais Alta: {pontuacao_mais_alta}", True, PRETO)

    # Preenche a tela com a cor branca para limpar qualquer
            # conteúdo anterior
    tela.fill(BRANCO)
    
    # Desenha o título na tela centralizado horizontalmente e
            # posicionado no quarto superior da tela
    # LARGURA_TELA // 2 centraliza o texto horizontalmente, 
            # ajustado pelo meio do comprimento do título
    tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, ALTURA_TELA // 4))
    
    # Desenha o botão de instrução na tela, centralizado 
            # horizontalmente e posicionado no meio da tela
    tela.blit(botao_jogar, (LARGURA_TELA // 2 - botao_jogar.get_width() // 2, ALTURA_TELA // 2))
    
    # Desenha o texto da pontuação mais alta na tela, centralizado
            # horizontalmente, abaixo do botão de instrução
    tela.blit(texto_pontuacao, (LARGURA_TELA // 2 - texto_pontuacao.get_width() // 2, ALTURA_TELA // 2 + 60))
    
    # Atualiza a tela para exibir o menu com 
            # todas as alterações feitas
    pygame.display.flip()


# Função para limpar o arquivo de pontuação (opcional)
# Esta função redefine a pontuação mais alta para zero 
        # no arquivo de pontuação.
# Pode ser usada para reiniciar a pontuação mais alta 
        # caso o jogador queira começar do zero.
def limpar_pontuacao():
    
    # Abre o arquivo de pontuação no modo de escrita ("w"), o
            # que apaga o conteúdo existente
            # e permite reescrever no arquivo. Se o 
            # arquivo não existir, ele será criado.
    with open(caminho_score, "w") as f:
        
        # Escreve "0" no arquivo, redefinindo a pontuação mais alta para zero
        f.write("0")


# Loop principal do programa
# Este loop controla o fluxo principal do jogo, começando 
        # pelo menu e aguardando a ação do jogador
while True:
    
    # Exibe o menu principal, onde o jogador pode ver o título, 
            # instruções e a pontuação mais alta
    mostrar_menu()

    # Variável de controle que define se o programa está aguardando a 
            # ação do jogador para iniciar o jogo
    esperando = True
    
    # Loop que permanece enquanto o jogador não pressionar a
            # tecla de início (ESPAÇO)
    while esperando:
        
        # Captura e processa todos os eventos que ocorrem, como
                # fechamento da janela e pressionamento de teclas
        for evento in pygame.event.get():
            
            # Verifica se o evento é o fechamento da janela (clique no "X")
            # Se for, encerra o Pygame e o programa
            if evento.type == pygame.QUIT:
                
                pygame.quit()  # Finaliza o Pygame
                sys.exit()  # Encerra o programa

            # Verifica se uma tecla foi pressionada e se 
                    # essa tecla é a ESPAÇO
            # Se for, define 'esperando' como False para sair
                    # do loop e iniciar o jogo
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                esperando = False  # Inicia o jogo quando ESPAÇO é pressionado

    # Chama a função principal do jogo, que 
            # contém o loop de jogabilidade
    jogo()