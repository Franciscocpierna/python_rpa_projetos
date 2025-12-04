# Importa a biblioteca pygame, essencial para o desenvolvimento de 
        # jogos em Python, que lida com gráficos, áudio, e entrada do usuário.
import pygame

# Importa a biblioteca random para gerar números aleatórios, 
        # úteis para criação de variações como obstáculos e efeitos.
import random

# Importa a biblioteca sys para manipulação de sistema, 
        # permitindo encerrar o programa quando necessário.
import sys

# Importa a biblioteca math, que contém funções matemáticas 
        # avançadas, como seno e cosseno, para cálculos de movimento e ondulações.
import math

# Inicializa o Pygame e seus módulos para preparar o ambiente do jogo.
pygame.init()

# Configurações da Tela
# Define a largura da tela do jogo em pixels
LARGURA_TELA = 800

# Define a altura da tela do jogo em pixels
ALTURA_TELA = 600

# Cria a tela do jogo com as dimensões definidas, onde 
        # todos os elementos gráficos serão exibidos.
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Define o título da janela do jogo que será exibido na
        # barra de título da janela.
pygame.display.set_caption("Helicóptero no Túnel")

# Carregar imagem do helicóptero
# Carrega a imagem do helicóptero a partir do arquivo "jogador.png", 
        # que representa o personagem principal do jogo.
helicoptero_img = pygame.image.load("jogador.png")

# Define a largura da imagem do helicóptero em pixels, 
        # dimensionando o tamanho visual do helicóptero.
helicoptero_largura = 60

# Define a altura da imagem do helicóptero em pixels.
helicoptero_altura = 40

# Redimensiona a imagem do helicóptero para as dimensões 
        # especificadas de largura e altura, adequando a imagem ao jogo.
helicoptero_img = pygame.transform.scale(helicoptero_img, (helicoptero_largura, helicoptero_altura))

# Cores
# Define a cor verde em RGB para uso em elementos do
        # jogo, como o túnel.
VERDE = (0, 255, 0)

# Define a cor preta em RGB, usada como fundo da tela 
        # ou em outros elementos.
PRETO = (0, 0, 0)

# Define a cor branca em RGB, usada para textos e 
        # outros elementos gráficos.
BRANCO = (255, 255, 255)

# Define a cor cinza claro para efeitos de fumaça,
        # representando partículas de escape do helicóptero.
FUMAÇA = (150, 150, 150)

# Define a cor vermelha em RGB, usada em obstáculos 
        # ou para alertas visuais.
VERMELHO = (255, 0, 0)

# Define a cor amarela em RGB, usada para efeitos visuais, 
        # como projéteis disparados.
AMARELO = (255, 255, 0)

# Define a cor laranja em RGB, usada para efeitos de
        # destruição ou explosões.
LARANJA = (255, 165, 0)

# Configurações do Helicóptero
# Define a posição inicial do helicóptero no eixo X, 
        # fixando o ponto de partida na tela.
helicoptero_x = 100

# Define a velocidade inicial no eixo Y como zero, indicando 
        # que o helicóptero começa parado verticalmente.
velocidade_y = 0

# Define a velocidade de movimento do helicóptero no eixo X, 
        # determinando a velocidade horizontal constante.
velocidade_x = 5

# Define o limite da velocidade vertical, limitando a velocidade
        # para cima e para baixo, evitando movimentos abruptos.
velocidade_vertical_max = 5

# Define a aceleração vertical, indicando a taxa de aumento ou 
        # diminuição da velocidade quando teclas são pressionadas.
aceleracao_vertical = 0.5

# Cria uma lista para armazenar partículas de fumaça, que 
        # representam o efeito visual de movimento do helicóptero.
fumaça_lista = []

# Configurações do Jogo
# Define a pontuação inicial como zero, que aumenta
        # conforme o jogador avança.
pontuacao = 0

# Define a melhor pontuação alcançada, usada para 
        # registrar o recorde do jogador.
melhor_pontuacao = 0

# Define a velocidade do túnel, indicando a velocidade com 
        # que o cenário avança, criando a sensação de movimento.
velocidade_tunel = 5

# Variáveis para o túnel ondulado
# Define a amplitude da onda do túnel, que controla a altura 
        # máxima das ondulações nas paredes do túnel.
amplitude = 150

# Define o espaço entre o teto e o chão do túnel, criando uma
        # área segura para o helicóptero voar.
gap = 300

# Define a largura das seções das paredes do túnel, 
        # determinando o espaçamento das ondulações.
largura_parede = 20

# Define a frequência da onda do túnel, ajustando a suavidade 
        # das ondulações para um movimento mais natural.
frequencia = 500

# Define o deslocamento inicial do túnel como zero, que será
        # incrementado para simular o movimento do túnel.
tunnel_offset = 0

# Lista de obstáculos
# Cria uma lista para armazenar os obstáculos gerados no túnel,
        # que representam desafios para o jogador desviar.
obstaculos = []

# Define o temporizador para o próximo obstáculo, permitindo 
        # intervalos entre a geração de obstáculos.
tempo_para_proximo_obstaculo = 0

# Lista de projéteis
# Cria uma lista para armazenar projéteis disparados pelo
        # intervalos entre a geração de obstáculos.
        # helicóptero, usados para destruir obstáculos.
projetil_lista = []

# Lista de efeitos de destruição
# Cria uma lista para armazenar efeitos de destruição, como 
        # intervalos entre a geração de obstáculos.
        # explosões, ao colidir com obstáculos ou projéteis.
efeitos_destruicao = []

# Função para desenhar o túnel ondulado
# Essa função cria o túnel no qual o helicóptero deve passar.
# O túnel tem ondulações, como uma onda, para criar um
        # intervalos entre a geração de obstáculos.
        # desafio adicional ao jogador.
def desenhar_tunel():
    
    # Um laço que percorre a tela horizontalmente, dividindo o 
            # túnel em várias seções verticais.
    # O 'range' vai de -1 até um pouco além da largura da tela, 
            # para garantir que o túnel cubra toda a largura 
            # da tela, mesmo enquanto ele "se move" para a esquerda.
    for i in range(-1, LARGURA_TELA // largura_parede + 2):
        
        # Calcula a posição X da parede.
        # A variável 'parede_x' é a posição horizontal de cada seção do túnel.
        # Multiplicamos 'i' pela largura das paredes para espaçá-las adequadamente.
        # O 'tunnel_offset % largura_parede' faz com que as
                # seções pareçam "correr" para a esquerda,
                # dando uma impressão de movimento no túnel.
        parede_x = i * largura_parede - (tunnel_offset % largura_parede)
        
        # Calcula o deslocamento da onda, criando a ondulação do túnel.
        # O 'offset' ajusta a posição do túnel para simular o
                # movimento ondulado usando uma função seno.
        offset = (tunnel_offset + i * largura_parede) / frequencia
        
        # Usa a função seno para criar um valor que varia 
                # entre -1 e 1, o que cria a forma ondulada do túnel.
        sin_offset = math.sin(offset)
        
        # Define o centro do túnel com base na altura da 
                # tela e no valor do seno.
        # Multiplicamos o 'sin_offset' pela amplitude para
                # controlar o quanto o túnel sobe e desce.
        # Dessa forma, o túnel vai parecer que "sobe" e "desce" 
                # de acordo com a onda.
        centro_tunel = ALTURA_TELA / 2 + amplitude * sin_offset
        
        # Calcula a altura do teto do túnel com base no centro e 
                # no espaço entre o teto e o chão.
        # 'gap / 2' define o espaço seguro (abertura do túnel) 
                # para o helicóptero passar.
        altura_teto = centro_tunel - gap / 2
        
        # Calcula a altura do chão do túnel com base no 
                # centro e no espaço de segurança.
        altura_chao = centro_tunel + gap / 2
        
        # Desenha uma seção do teto do túnel como um 
                # retângulo verde, da posição (parede_x, 0)
                # até a altura do teto calculada.
        pygame.draw.rect(tela, VERDE, (parede_x, 0, largura_parede, altura_teto))  # Teto
        
        # Desenha uma seção do chão do túnel como um retângulo 
                # verde, da posição (parede_x, altura_chao)
                # até a parte inferior da tela. Isso cria o efeito 
                # visual de um túnel com teto e chão.
        pygame.draw.rect(tela, VERDE, (parede_x, altura_chao, largura_parede, ALTURA_TELA - altura_chao))  # Chão


# Função para gerar e atualizar partículas de fumaça
# Essa função cria partículas de fumaça que saem do 
        # helicóptero enquanto ele se move,
        # adicionando um efeito visual de movimento e "motor" ao jogo.
def gerar_fumaca():
    
    # Define a posição X da fumaça um pouco atrás do helicóptero.
    # Como o helicóptero está se movendo para a direita, isso 
            # cria uma trilha de fumaça atrás dele.
    # O valor "-10" move a fumaça para trás do helicóptero na tela.
    fumaça_x = helicoptero_x - 10
    
    # Define a posição Y da fumaça no centro vertical do helicóptero.
    # Isso faz com que a fumaça pareça sair do meio do 
            # helicóptero, alinhada verticalmente.
    # A divisão "// 2" pega o ponto médio da altura do helicóptero.
    fumaça_y = helicoptero_y + helicoptero_altura // 2
    
    # Adiciona uma nova partícula de fumaça na lista 'fumaça_lista'.
    # Cada partícula de fumaça é representada como um dicionário com:
    # - "x": posição horizontal da fumaça
    # - "y": posição vertical da fumaça
    # - "tamanho": tamanho inicial da partícula, gerado 
            # aleatoriamente entre 5 e 10.
    # O uso de random.randint cria tamanhos variados, dando um 
            # efeito mais natural e dinâmico à fumaça.
    fumaça_lista.append({"x": fumaça_x, "y": fumaça_y, "tamanho": random.randint(5, 10)})


# Função para desenhar e atualizar partículas de fumaça
# Esta função desenha as partículas de fumaça e atualiza
        # suas posições e tamanhos, simulando um efeito de 
        # movimento e dissipação conforme elas se afastam do helicóptero.
def desenhar_fumaca():
    
    # Laço que percorre cada partícula de fumaça na lista 'fumaça_lista'.
    # A lista é copiada usando '[:]' para evitar problemas ao 
            # remover partículas durante a iteração.
    for particula in fumaça_lista[:]:
        
        # Move a partícula de fumaça para a esquerda, 
                # acompanhando a velocidade do túnel.
        # Isso cria o efeito de que a fumaça está ficando para
                # trás enquanto o helicóptero avança.
        particula["x"] -= velocidade_tunel
        
        # Aumenta o tamanho da partícula de fumaça para simular o 
                # efeito de dissipação.
        # Cada iteração aumenta o tamanho em 0.2, fazendo a 
                # partícula parecer que se espalha.
        particula["tamanho"] += 0.2
        
        # Desenha a partícula de fumaça como um círculo na tela.
        # A cor é definida por 'FUMAÇA' e as coordenadas e tamanho 
                # da partícula são ajustados.
        # 'int()' é usado para converter para inteiros, pois as funções 
                # de desenho requerem valores inteiros.
        pygame.draw.circle(tela, FUMAÇA, (int(particula["x"]), int(particula["y"])), int(particula["tamanho"]))
        
        # Verifica se a partícula de fumaça saiu completamente da tela à esquerda.
        # Se 'particula["x"] < 0', significa que a partícula está fora da tela,
                # então ela é removida da lista 'fumaça_lista' para 
                # economizar memória e processamento.
        if particula["x"] < 0:
            fumaça_lista.remove(particula)


# Função para mostrar a pontuação atual e a melhor pontuação
# Esta função exibe a pontuação do jogador e a melhor 
        # pontuação registrada no jogo.
# Ambas as pontuações são desenhadas na tela em locais específicos.
def mostrar_pontuacao(pontuacao, melhor_pontuacao):
    
    # Define a fonte do texto para exibir a pontuação.
    # 'pygame.font.SysFont' cria uma fonte padrão do sistema.
    # 'None' significa que a fonte padrão do sistema será usada.
    # O número 36 representa o tamanho da fonte.
    font = pygame.font.SysFont(None, 36)
    
    # Renderiza o texto para a pontuação atual, convertendo o 
            # valor numérico em texto.
    # 'font.render' cria uma imagem de texto com os seguintes parâmetros:
    # - O texto é formatado para exibir "Distancia: <pontuação atual>".
    # - O segundo parâmetro, 'True', ativa a suavização das bordas do texto.
    # - A cor do texto é definida como 'BRANCO' para que ele
            # seja visível sobre fundos escuros.
    texto_distancia = font.render(f"Distancia: {pontuacao}", True, BRANCO)
    
    # Renderiza o texto para a melhor pontuação.
    # A melhor pontuação é exibida no formato "Melhor: <melhor pontuação>".
    # O processo é o mesmo do anterior, mas o texto contém a melhor pontuação.
    texto_melhor = font.render(f"Melhor: {melhor_pontuacao}", True, BRANCO)
    
    # Desenha o texto da pontuação atual na tela em uma 
            # posição fixa, no canto inferior esquerdo.
    # 'tela.blit' desenha o texto na tela:
    # - O primeiro parâmetro é o objeto de texto gerado.
    # - O segundo parâmetro define a posição (10 pixels da 
            # esquerda, 40 pixels acima da base da tela).
    tela.blit(texto_distancia, (10, ALTURA_TELA - 40))
    
    # Desenha o texto da melhor pontuação na tela no canto inferior direito.
    # Isso permite que o jogador veja seu progresso e a 
            # pontuação máxima alcançada.
    # 'LARGURA_TELA - 150' alinha o texto 150 pixels antes do final da tela, e
    # 'ALTURA_TELA - 40' posiciona o texto 40 pixels acima da borda inferior.
    tela.blit(texto_melhor, (LARGURA_TELA - 150, ALTURA_TELA - 40))


# Função para mostrar o menu inicial
# Esta função exibe o menu inicial com o título do jogo, uma
        # instrução para começar a jogar
        # e a melhor pontuação registrada, tudo centralizado na tela.
def mostrar_menu():
    
    # Define a fonte e o tamanho do texto para o título do jogo.
    # 'None' significa usar a fonte padrão do sistema e
            # '72' define o tamanho do texto do título.
    font_titulo = pygame.font.SysFont(None, 72)
    
    # Define a fonte e o tamanho do texto para o botão de
            # início e melhor pontuação.
    # Esse texto será menor que o título, com tamanho 48.
    font_botao = pygame.font.SysFont(None, 48)
    
    # Renderiza o texto do título "Helicóptero no Túnel".
    # O texto será suavizado (True) e de cor branca (BRANCO).
    # O objeto 'titulo' contém a imagem do texto renderizado 
            # que será exibida na tela.
    titulo = font_titulo.render("Helicóptero no Túnel", True, BRANCO)
    
    # Renderiza o texto do botão "Pressione ESPAÇO para Jogar".
    # Esse texto instrui o jogador a pressionar a 
            # tecla ESPAÇO para iniciar o jogo.
    botao_jogar = font_botao.render("Pressione ESPAÇO para Jogar", True, BRANCO)
    
    # Renderiza o texto da melhor pontuação, que mostra a
            # pontuação mais alta registrada.
    # A melhor pontuação é formatada como
            # "Melhor Pontuação: <melhor pontuação>".
    melhor_pontuacao_texto = font_botao.render(f"Melhor Pontuação: {melhor_pontuacao}", True, BRANCO)
    
    # Preenche a tela inteira com a cor preta, criando um
            # fundo limpo para o menu.
    tela.fill(PRETO)
    
    # Desenha o título na tela, centralizado horizontalmente e 
            # posicionado no terço superior da tela.
    # A posição horizontal é ajustada para que o centro do texto 
            # fique no meio da tela.
    tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, ALTURA_TELA // 3))
    
    # Desenha o texto do botão de início na tela, centralizado 
            # horizontalmente e na metade da altura da tela.
    # A posição horizontal centraliza o texto e a posição vertical 
            # coloca-o no meio da tela.
    tela.blit(botao_jogar, (LARGURA_TELA // 2 - botao_jogar.get_width() // 2, ALTURA_TELA // 2))
    
    # Desenha o texto da melhor pontuação na tela, centralizado 
            # horizontalmente e posicionado abaixo do botão de 
            # início (1.5 vezes a altura da tela), para exibir a
            # melhor pontuação ao jogador.
    tela.blit(melhor_pontuacao_texto, (LARGURA_TELA // 2 - melhor_pontuacao_texto.get_width() // 2, ALTURA_TELA // 1.5))
    
    # Atualiza a tela com o conteúdo desenhado, exibindo o 
            # menu para o jogador.
    pygame.display.flip()


# Função para gerar obstáculos usando um temporizador
# Esta função cria obstáculos no túnel em intervalos de
        # tempo regulares, adicionando
        # desafios para o jogador desviar enquanto o jogo progride.
def gerar_obstaculos(delta_time):
    
    # Declara a variável 'tempo_para_proximo_obstaculo' como
            # global para podermos alterá-la dentro da função.
    # Essa variável controla o tempo até o próximo obstáculo ser gerado.
    global tempo_para_proximo_obstaculo
    
    # Reduz o tempo restante para o próximo obstáculo com base 
            # no tempo decorrido (delta_time).
    # 'delta_time' representa o tempo entre cada quadro do 
            # jogo, garantindo que o temporizador
            # seja atualizado corretamente conforme o jogo avança.
    tempo_para_proximo_obstaculo -= delta_time
    
    # Verifica se o tempo para o próximo obstáculo já
            # chegou a zero ou menos.
    # Se for menor ou igual a zero, significa que é 
            # hora de gerar um novo obstáculo.
    if tempo_para_proximo_obstaculo <= 0:
        
        # Reinicia o temporizador para 5000 milissegundos (5 segundos),
        # determinando que o próximo obstáculo será gerado em 5 segundos.
        tempo_para_proximo_obstaculo = 5000
        
        # Define a posição X do obstáculo para fora da tela, à direita,
        # para que ele se mova da direita para a esquerda ao entrar na tela.
        obstaculo_x = LARGURA_TELA + 50
        
        # Calcula o deslocamento usando uma função seno para
                # gerar a ondulação do túnelm e garantir que os
                # obstáculos sigam o movimento ondulado do túnel.
        offset = (tunnel_offset + obstaculo_x) / frequencia
        sin_offset = math.sin(offset)
        
        # Define o centro do túnel verticalmente, somando a 
                # altura do seno ao centro da tela.
        # A amplitude controla o quanto o túnel oscila verticalmente.
        centro_tunel = ALTURA_TELA / 2 + amplitude * sin_offset
        
        # Define a altura do teto do túnel para que o obstáculo não
                # ultrapasse a área de segurança.
        # A altura do teto é calculada subtraindo metade do 
                # espaço seguro (gap) do centro do túnel.
        altura_teto = centro_tunel - gap / 2
        
        # Define a altura do chão do túnel, somando metade do
                # espaço seguro ao centro do túnel.
        # Isso garante que o túnel tenha um espaço definido 
                # onde o helicóptero pode passar.
        altura_chao = centro_tunel + gap / 2
        
        # Gera uma posição Y aleatória para o obstáculo dentro do 
                # espaço entre o teto e o chão,
                # garantindo que o obstáculo fique na área segura.
        # Subtrai 50 e 60 para evitar que o obstáculo toque no
                # teto ou no chão, deixando um espaço adicional.
        obstaculo_y = random.randint(int(altura_teto + 50), int(altura_chao - 50 - 60))
        
        # Define a largura do obstáculo como 30 pixels.
        obstaculo_largura = 30
        
        # Define a altura do obstáculo como 60 pixels.
        obstaculo_altura = 60
        
        # Adiciona o novo obstáculo à lista de obstáculos 
                # como um dicionário com as coordenadas e dimensões.
        # Isso permite que o obstáculo seja desenhado e movido no jogo.
        obstaculos.append({
            "x": obstaculo_x,
            "y": obstaculo_y,
            "largura": obstaculo_largura,
            "altura": obstaculo_altura
        })


# Função para desenhar e atualizar a posição dos obstáculos
# Esta função move os obstáculos para a esquerda e
        # os desenha na tela.
# Quando um obstáculo sai da tela (extrema esquerda), ele é
        # removido da lista de obstáculos.
def desenhar_obstaculos():
    
    # Laço que percorre cada obstáculo na lista 'obstaculos'.
    # A lista é copiada usando '[:]' para evitar problemas ao
            # remover obstáculos enquanto iteramos sobre eles.
    for obstaculo in obstaculos[:]:
        
        # Move o obstáculo para a esquerda, reduzindo seu valor
                # de 'x' com base na velocidade do túnel.
        # Isso cria a ilusão de que o helicóptero está avançando 
                # enquanto os obstáculos "se aproximam".
        obstaculo["x"] -= velocidade_tunel
        
        # Desenha o obstáculo na tela como um retângulo de cor
                # vermelha (VERMELHO).
        # 'pygame.draw.rect' recebe:
        # - 'tela': a superfície onde o retângulo será desenhado.
        # - 'VERMELHO': a cor do retângulo.
        # - A posição e dimensões do retângulo são extraídas do
                # dicionário 'obstaculo'.
        pygame.draw.rect(tela, VERMELHO, (obstaculo["x"], obstaculo["y"], obstaculo["largura"], obstaculo["altura"]))
        
        # Verifica se o obstáculo saiu completamente da tela pela esquerda.
        # Se a posição X do obstáculo somada à sua largura for menor que zero,
        # significa que ele está fora da tela.
        if obstaculo["x"] + obstaculo["largura"] < 0:
            
            # Remove o obstáculo da lista, economizando memória e
                    # melhorando o desempenho,
                    # pois ele não é mais necessário no jogo.
            obstaculos.remove(obstaculo)


# Função para gerar e atualizar projéteis
# Esta função cria projéteis que o helicóptero dispara para
        # frente, adicionando uma forma de
        # ataque contra os obstáculos.
def gerar_projetil():
    
    # Define a posição inicial do projétil no eixo X.
    # 'projetil_x' é definido na extremidade direita do 
            # helicóptero, na posição horizontal do helicóptero
            # mais a largura do helicóptero. Isso faz o projétil 
            # parecer que sai do helicóptero.
    projetil_x = helicoptero_x + helicoptero_largura
    
    # Define a posição inicial do projétil no eixo Y.
    # 'projetil_y' é colocado no centro vertical do helicóptero,
            # calculado pela posição Y do helicóptero somada à
            # metade da altura do helicóptero. Assim, o projétil
            # parece sair do centro.
    projetil_y = helicoptero_y + helicoptero_altura / 2
    
    # Define a velocidade do projétil em 10 pixels por frame,
            # para que ele se mova rapidamente para frente.
    # Isso cria um efeito visual de disparo rápido.
    projetil_velocidade = 10
    
    # Adiciona o projétil à lista 'projetil_lista' como um
            # dicionário com as informações:
    # - "x": posição inicial horizontal do projétil
    # - "y": posição inicial vertical do projétil
    # - "velocidade": velocidade com a qual o projétil se
            # moverá para frente
    # Essa lista será usada para desenhar e atualizar a 
            # posição de cada projétil no jogo.
    projetil_lista.append({"x": projetil_x, "y": projetil_y, "velocidade": projetil_velocidade})


# Função para desenhar e atualizar a posição dos projéteis
# Esta função move cada projétil para a direita e o desenha na tela.
# Quando um projétil sai da tela pela direita, ele é removido da lista.
def desenhar_projeteis():
    
    # Laço que percorre cada projétil na lista 'projetil_lista'.
    # A lista é copiada usando '[:]' para evitar problemas ao 
            # remover projéteis enquanto iteramos sobre eles.
    for projetil in projetil_lista[:]:
        
        # Move o projétil para a direita, aumentando seu valor 
                # de "x" com base na velocidade definida.
        # Isso cria o efeito de que o projétil está avançando 
                # rapidamente para frente (da esquerda para a direita).
        projetil["x"] += projetil["velocidade"]
        
        # Desenha o projétil na tela como um pequeno círculo amarelo (cor AMARELO).
        # 'pygame.draw.circle' desenha um círculo com:
        # - 'tela': a superfície onde o círculo será desenhado.
        # - 'AMARELO': a cor do círculo.
        # - A posição e o raio do círculo são definidos pela posição 
                # do projétil e o valor '5' para o raio.
        # A função 'int()' é usada para converter as coordenadas em 
                # inteiros, pois as funções de desenho
                # requerem valores inteiros.
        pygame.draw.circle(tela, AMARELO, (int(projetil["x"]), int(projetil["y"])), 5)
        
        # Verifica se o projétil saiu completamente da tela pela direita.
        # Se 'projetil["x"]' for maior que a largura da tela, 
                # significa que o projétil está fora da tela.
        if projetil["x"] > LARGURA_TELA:
            
            # Remove o projétil da lista, economizando memória e
                    # melhorando o desempenho,
                    # pois ele não é mais necessário no jogo.
            projetil_lista.remove(projetil)


# Função para atualizar e desenhar efeitos de destruição
# Esta função controla a duração e o visual dos efeitos de
        # destruição, como explosões,
        # para simular o impacto visual de projéteis
        # atingindo obstáculos.
def atualizar_destruicoes():
    
    # Laço que percorre cada efeito de destruição na
            # lista 'efeitos_destruicao'.
    # A lista é copiada usando '[:]' para evitar problemas ao 
            # remover efeitos enquanto iteramos sobre eles.
    for efeito in efeitos_destruicao[:]:
        
        # Reduz o tempo de vida do efeito, diminuindo o valor 
                # de "tempo" em 1 a cada chamada da função.
        # Isso faz o efeito durar apenas um certo número de
                # frames antes de desaparecer.
        efeito["tempo"] -= 1
        
        # Verifica se o tempo do efeito chegou a zero ou menos,
                # indicando que o efeito terminou.
        if efeito["tempo"] <= 0:
            
            # Remove o efeito de destruição da lista, pois ele 
                    # já "acabou" e não deve mais ser desenhado.
            efeitos_destruicao.remove(efeito)
            
        else:
            
            # Desenha o efeito de destruição como um círculo laranja, 
                    # representando uma explosão.
            # 'pygame.draw.circle' cria um círculo com:
            # - 'tela': a superfície onde o círculo será desenhado.
            # - 'LARANJA': a cor do círculo, representando uma
                    # explosão em tons de laranja.
            # - A posição 'x' e 'y' do efeito são convertidas em
                    # inteiros para a função de desenho.
            # - 'efeito["raio"]' define o tamanho do círculo, que 
                    # aumenta gradualmente.
            pygame.draw.circle(tela, LARANJA, (int(efeito["x"]), int(efeito["y"])), efeito["raio"])
            
            # Aumenta o raio do efeito de destruição em 2, simulando uma
                    # expansão, como uma explosão que se espalha para 
                    # fora a cada frame, criando um visual dinâmico.
            efeito["raio"] += 2


# Função principal do jogo
# Esta função contém a lógica central do jogo, gerenciando o
        # loop principal, a posição do helicóptero,
        # a geração de obstáculos e projéteis, a pontuação, e
        # a verificação de colisões.
def jogo():
    
    # Define algumas variáveis como globais para que possam ser 
            # modificadas dentro desta função.
    # Essas variáveis incluem a posição do helicóptero, a 
            # pontuação, a melhor pontuação, a velocidade vertical 
            # do helicóptero, o deslocamento do túnel e o 
            # temporizador do próximo obstáculo.
    global helicoptero_x, helicoptero_y, pontuacao, melhor_pontuacao, velocidade_y, tunnel_offset, tempo_para_proximo_obstaculo
    
    # Define o estado do jogo como ativo. Enquanto 'rodando' 
            # for True, o jogo continuará.
    rodando = True
    
    # Cria um objeto 'relogio' para controlar a taxa de
            # atualização do jogo.
    # Este relógio permite limitar a quantidade de frames 
            # por segundo (FPS) no jogo.
    relogio = pygame.time.Clock()
    
    # Inicializa a pontuação do jogador como zero no início do jogo.
    pontuacao = 0
    
    # Limpa as listas de fumaça, obstáculos, projéteis e 
            # efeitos de destruição, garantindo
            # que não haja partículas ou objetos indesejados 
            # quando o jogo recomeçar.
    fumaça_lista.clear()
    obstaculos.clear()
    projetil_lista.clear()
    efeitos_destruicao.clear()
    
    # Define a velocidade vertical inicial do helicóptero como
            # zero, ou seja, ele começa parado no eixo Y.
    velocidade_y = 0
    
    # Inicializa o deslocamento do túnel como zero, o que significa
            # que ele ainda não "começou a se mover".
    tunnel_offset = 0
    
    # Define o tempo para o próximo obstáculo como 3000 
            # milissegundos (3 segundos).
    # Isso permite que o jogador comece sem um obstáculo imediato.
    tempo_para_proximo_obstaculo = 3000  # Primeiro obstáculo em 3 segundos

    # Posições iniciais
    # Define a posição inicial do helicóptero no centro
            # vertical da tela.
    # A altura do helicóptero é subtraída pela metade para 
            # centralizar o helicóptero no meio da tela.
    helicoptero_y = ALTURA_TELA / 2 - helicoptero_altura / 2  # Centraliza o helicóptero verticalmente

    # Variáveis para controlar a taxa de disparo
    # 'a_pressed' é uma variável booleana que indica se a
            # tecla de disparo (a tecla "A") está pressionada.
    # Ela é usada para gerenciar o estado do disparo de projéteis.
    a_pressed = False
    
    # Define o tempo de recarga do próximo tiro (em milissegundos) 
            # para evitar disparos contínuos.
    # Inicialmente, o cooldown é zero, permitindo que o jogador dispare
            # imediatamente ao iniciar o jogo.
    cooldown_tiro = 0  # Tempo de recarga para o próximo tiro

    # Loop principal do jogo
    # Este loop controla o jogo enquanto a variável 'rodando' for True.
    # Ele atualiza o estado do jogo, gerencia eventos, desenha 
            # objetos na tela, e mantém o jogo funcionando.
    while rodando:
        
        # Calcula o tempo desde o último frame em milissegundos (delta_time).
        # 'relogio.tick(60)' limita a taxa de quadros para 60 FPS (frames por segundo),
        # mantendo o jogo fluido e a física consistente entre frames.
        delta_time = relogio.tick(60)
        
        # Preenche a tela com a cor preta, apagando tudo o que
                # foi desenhado no frame anterior.
        # Isso prepara a tela para o próximo frame,
                # evitando "rastros" de objetos.
        tela.fill(PRETO)

        # Eventos
        # Este bloco monitora os eventos do usuário, como fechar a 
                # janela ou pressionar teclas.
        for evento in pygame.event.get():
            
            # Verifica se o evento é 'QUIT' (fechar a janela).
            # Se sim, chama 'pygame.quit()' para encerrar o Pygame e
                    # 'sys.exit()' para fechar o programa.
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Verifica se uma tecla foi pressionada (evento de 
                    # pressionar tecla).
            elif evento.type == pygame.KEYDOWN:
                
                # Verifica se a tecla pressionada é "A" (disparo).
                # Se for, altera 'a_pressed' para True, permitindo que 
                        # projéteis sejam disparados.
                if evento.key == pygame.K_a:
                    a_pressed = True
            
            # Verifica se uma tecla foi solta (evento de soltar tecla).
            elif evento.type == pygame.KEYUP:
                
                # Verifica se a tecla solta é "A".
                # Se for, altera 'a_pressed' para False, interrompendo o
                        # disparo de projéteis.
                if evento.key == pygame.K_a:
                    a_pressed = False


        # Controle de teclas
        # Verifica continuamente o estado das teclas para controlar o
                # movimento vertical do helicóptero.
        
        # Captura o estado de todas as teclas e armazena em 'teclas'.
        # 'pygame.key.get_pressed()' retorna uma lista booleana 
                # onde cada posição indica
                # se uma tecla específica está pressionada (True) ou não (False).
        teclas = pygame.key.get_pressed()
        
        # Verifica se a tecla "UP" (seta para cima) está pressionada.
        if teclas[pygame.K_UP]:
            
            # Se a seta para cima está pressionada, diminui a
                    # velocidade vertical.
            # Isso faz o helicóptero subir, pois um valor de 
                    # velocidade negativo move para cima.
            velocidade_y -= aceleracao_vertical
            
            # Limita a velocidade máxima de subida para evitar que o
                    # helicóptero suba muito rápido.
            # Se a velocidade for menor que o limite negativo, ela é
                    # ajustada para o limite.
            if velocidade_y < -velocidade_vertical_max:
                velocidade_y = -velocidade_vertical_max
        
        # Verifica se a tecla "DOWN" (seta para baixo) está pressionada.
        elif teclas[pygame.K_DOWN]:
            
            # Se a seta para baixo está pressionada, aumenta a
                    # velocidade vertical.
            # Isso faz o helicóptero descer, pois um valor de velocidade 
                    # positivo move para baixo.
            velocidade_y += aceleracao_vertical
            
            # Limita a velocidade máxima de descida para evitar que o
                    # helicóptero desça muito rápido.
            # Se a velocidade for maior que o limite, ela é 
                    # ajustada para o limite.
            if velocidade_y > velocidade_vertical_max:
                velocidade_y = velocidade_vertical_max
        
        else:
            
            # Se nenhuma tecla para cima ou para baixo está pressionada,
                    # não altera a velocidade vertical.
            # Isso significa que o helicóptero continua no mesmo nível 
                    # vertical, mantendo a velocidade atual.
            pass


        # Movimento lateral
        # Controla o movimento horizontal do helicóptero com as 
                # teclas de seta para a esquerda e direita.

        # Verifica se a tecla "LEFT" (seta para esquerda) está pressionada
        # e se o helicóptero não está na borda esquerda da tela (x > 0).
        if teclas[pygame.K_LEFT] and helicoptero_x > 0:
            
            # Move o helicóptero para a esquerda diminuindo o valor de 'helicoptero_x'
            # com base na velocidade horizontal 'velocidade_x'.
            helicoptero_x -= velocidade_x  # Movimento para a esquerda

        # Verifica se a tecla "RIGHT" (seta para direita) está pressionada
        # e se o helicóptero não está na borda direita da 
                # tela (x < largura da tela - largura do helicóptero).
        if teclas[pygame.K_RIGHT] and helicoptero_x < LARGURA_TELA - helicoptero_largura:
            
            # Move o helicóptero para a direita aumentando o 
                    # valor de 'helicoptero_x'
            # com base na velocidade horizontal 'velocidade_x'.
            helicoptero_x += velocidade_x  # Movimento para a direita

        # Movimento do helicóptero
        # Atualiza a posição vertical do helicóptero de acordo 
                # com sua velocidade vertical.
        # Isso aplica a velocidade calculada para o movimento 
                # para cima ou para baixo.
        helicoptero_y += velocidade_y

        # Desenha a imagem do helicóptero na tela, na posição atualizada.
        # 'helicoptero_img' é desenhado na posição (helicoptero_x, helicoptero_y).
        tela.blit(helicoptero_img, (helicoptero_x, helicoptero_y))

        # Desenhar e mover o túnel
        # Chama a função para desenhar o túnel na tela, criando o
                # efeito de um túnel ondulado.
        desenhar_tunel()
        
        # Atualiza o deslocamento do túnel, fazendo o túnel parecer
                # que se move para a esquerda.
        # Isso cria a ilusão de que o helicóptero está avançando pelo túnel.
        tunnel_offset += velocidade_tunel  # Atualiza o deslocamento do túnel

        # Gerar e desenhar fumaça
        # Chama a função para gerar uma nova partícula de 
                # fumaça atrás do helicóptero.
        gerar_fumaca()
        
        # Chama a função para desenhar todas as partículas de fumaça na tela.
        desenhar_fumaca()

        # Gerar e desenhar obstáculos
        # Gera novos obstáculos no túnel com base em um temporizador.
        gerar_obstaculos(delta_time)
        
        # Desenha os obstáculos na tela e os move para a esquerda, 
                # criando um desafio para o jogador.
        desenhar_obstaculos()


        # Gerar e desenhar projéteis
        # Controla o disparo de projéteis pelo helicóptero, permitindo 
                # um intervalo entre os tiros.

        # Verifica se a tecla de disparo (variável 'a_pressed') está pressionada e
        # se o tempo de recarga (cooldown) chegou a zero, 
                # permitindo o disparo.
        if a_pressed and cooldown_tiro <= 0:
            
            # Chama a função para gerar um novo projétil na
                    # posição do helicóptero.
            gerar_projetil()
            
            # Define o tempo de recarga para 300 milissegundos,
                    # evitando disparos contínuos
            # e permitindo um intervalo entre os tiros.
            cooldown_tiro = 300  # Tempo de recarga de 300 ms
            
        else:
            
            # Se o projétil está em recarga, reduz o cooldown com 
                    # base no tempo decorrido (delta_time).
            # Isso permite que o cooldown diminua a cada quadro 
                    # até chegar a zero novamente.
            cooldown_tiro -= delta_time
        
        # Chama a função para desenhar todos os projéteis na tela e
                # movê-los para a direita.
        desenhar_projeteis()

        # Atualizar e desenhar efeitos de destruição
        # Chama a função para atualizar e desenhar os efeitos de
                # destruição (explosões).
        # Cada explosão expande e eventualmente desaparece, 
                # simulando um efeito de impacto.
        atualizar_destruicoes()

        # Limites do túnel (detecção de colisão)
        # Calcula a posição central do helicóptero no eixo X para 
                # comparar com os limites do túnel.
        helicoptero_centro_x = helicoptero_x + helicoptero_largura / 2
        
        # Calcula o deslocamento da posição central do helicóptero
                # dentro do túnel usando uma função seno.
        # Isso ajuda a alinhar a posição do helicóptero com o
                # formato ondulado do túnel.
        offset = (tunnel_offset + helicoptero_centro_x) / frequencia
        sin_offset = math.sin(offset)
        
        # Define o centro do túnel, onde a amplitude da onda determina o
                # movimento para cima e para baixo.
        # A altura do centro é ajustada com base na função seno 
                # para simular a forma do túnel.
        centro_tunel = ALTURA_TELA / 2 + amplitude * sin_offset
        
        # Calcula a altura do teto do túnel com base no centro e no
                # espaço de segurança (gap).
        # Isso define o limite superior que o helicóptero 
                # não deve ultrapassar.
        altura_teto = centro_tunel - gap / 2
        
        # Calcula a altura do chão do túnel com base no centro e 
                # no espaço de segurança.
        # Isso define o limite inferior que o helicóptero não
                # deve ultrapassar.
        altura_chao = centro_tunel + gap / 2

        # Verifica se o helicóptero colidiu com o teto ou o chão do túnel.
        # Se a posição Y do helicóptero é menor que o teto ou 
                # maior que o chão, o jogo termina.
        if helicoptero_y < altura_teto or helicoptero_y + helicoptero_altura > altura_chao:
            
            # Define 'rodando' como False para encerrar o loop e, portanto, o jogo.
            rodando = False  # Fim do jogo se colidir com o teto ou chão


        # Detecção de colisão com obstáculos
        # Verifica se o helicóptero colidiu com algum obstáculo, 
                # encerrando o jogo em caso de colisão.
        
        # Cria um retângulo ao redor do helicóptero para facilitar a 
                # detecção de colisão.
        # 'pygame.Rect' cria um retângulo a partir das coordenadas e 
                # dimensões do helicóptero,
        # permitindo uma comparação de colisão com outros objetos 
                # retangulares (obstáculos).
        helicoptero_rect = pygame.Rect(helicoptero_x, helicoptero_y, helicoptero_largura, helicoptero_altura)
        
        # Laço que percorre cada obstáculo na lista de 'obstaculos'.
        for obstaculo in obstaculos[:]:
            
            # Cria um retângulo ao redor do obstáculo atual, usando
                    # suas coordenadas e dimensões.
            obstaculo_rect = pygame.Rect(obstaculo["x"], obstaculo["y"], obstaculo["largura"], obstaculo["altura"])
            
            # Verifica se o retângulo do helicóptero colide com o 
                    # retângulo do obstáculo.
            # Se houver colisão, o jogo termina definindo 'rodando' como False.
            if helicoptero_rect.colliderect(obstaculo_rect):
                rodando = False  # Fim do jogo se colidir com um obstáculo

            # Verificar colisão com projéteis
            # Laço que percorre cada projétil na lista 'projetil_lista' 
                    # para verificar se algum projétil atingiu o obstáculo.
            for projetil in projetil_lista[:]:
                
                # Cria um pequeno retângulo ao redor do projétil para 
                        # detectar colisão.
                # As coordenadas do projétil são ajustadas para centralizar o
                        # retângulo e o tamanho é definido como 10x10.
                projetil_rect = pygame.Rect(projetil["x"] - 5, projetil["y"] - 5, 10, 10)
                
                # Verifica se o retângulo do projétil colide com o 
                        # retângulo do obstáculo.
                if projetil_rect.colliderect(obstaculo_rect):
                    
                    # Remove o obstáculo da lista, pois ele foi 
                            # destruído pelo projétil.
                    obstaculos.remove(obstaculo)
                    
                    # Remove o projétil da lista, pois ele já foi usado 
                            # para destruir o obstáculo.
                    projetil_lista.remove(projetil)
                    
                    # Adicionar efeito de destruição no local onde o
                            # obstáculo foi atingido.
                    # O efeito é adicionado como um dicionário com:
                    # - "x" e "y": posição central do obstáculo destruído
                    # - "raio": tamanho inicial do efeito de explosão
                    # - "tempo": duração do efeito
                    efeitos_destruicao.append({
                        "x": obstaculo["x"] + obstaculo["largura"] / 2,
                        "y": obstaculo["y"] + obstaculo["altura"] / 2,
                        "raio": 10,
                        "tempo": 15
                    })
                    
                    # Sai do loop interno de projéteis após destruir o obstáculo,
                    # pois o obstáculo já foi removido e não é necessário 
                            # verificar mais colisões com ele.
                    break


        # Atualizar pontuação com base na distância percorrida
        # Calcula a pontuação do jogador com base na distância que o
                # helicóptero avançou no túnel.
        
        # A pontuação é calculada como o deslocamento total do túnel 
                # mais a posição do helicóptero no eixo X,
        # dividido por 10 para tornar a pontuação mais gerenciável.
        # 'int()' é usado para arredondar o valor para um número inteiro.
        pontuacao = int((tunnel_offset + helicoptero_x) / 100)
        
        # Verifica se a pontuação atual é maior que a melhor pontuação registrada.
        # Se for, atualiza 'melhor_pontuacao' com a nova pontuação.
        if pontuacao > melhor_pontuacao:
            melhor_pontuacao = pontuacao

        # Exibir a pontuação
        # Chama a função para mostrar a pontuação atual e a 
                # melhor pontuação na tela,
        # permitindo que o jogador acompanhe seu progresso.
        mostrar_pontuacao(pontuacao, melhor_pontuacao)

        # Impedir que o helicóptero saia da tela
        # Verifica se o helicóptero ultrapassou a borda superior da tela.
        if helicoptero_y < 0:
            
            # Se ultrapassou, ajusta a posição Y para 0 (a borda 
                    # superior) e zera a velocidade vertical,
            # impedindo que o helicóptero saia da tela.
            helicoptero_y = 0
            velocidade_y = 0

        # Verifica se o helicóptero ultrapassou a borda inferior da tela.
        if helicoptero_y > ALTURA_TELA - helicoptero_altura:
            
            # Se ultrapassou, ajusta a posição Y para a altura 
                    # máxima permitida e zera a velocidade vertical,
            # impedindo que o helicóptero saia da tela.
            helicoptero_y = ALTURA_TELA - helicoptero_altura
            velocidade_y = 0

        # Atualização da tela
        # 'pygame.display.flip()' atualiza a tela com tudo o que foi
                # desenhado neste ciclo do loop,
        # permitindo que o jogador veja o movimento do helicóptero,
                # obstáculos, e outras animações.
        pygame.display.flip()


    # Pequena pausa antes de voltar ao menu
    pygame.time.delay(1000)

# Loop principal do programa
# Este é o loop principal do programa que controla o fluxo 
        # entre o menu inicial e o jogo em si.
while True:
    
    # Chama a função para mostrar o menu inicial, exibindo o 
            # título, instruções e melhor pontuação.
    mostrar_menu()
    
    # Espera o jogador pressionar ESPAÇO para iniciar o jogo
    # A variável 'esperando' mantém o loop de espera ativo até 
            # que o jogador pressione a tecla ESPAÇO.
    esperando = True
    while esperando:
        
        # Percorre todos os eventos que ocorrem enquanto o 
                # programa está em execução.
        for evento in pygame.event.get():
            
            # Verifica se o jogador fechou a janela do jogo.
            if evento.type == pygame.QUIT:
                
                # Encerra o Pygame e fecha o programa se a janela for fechada.
                pygame.quit()
                sys.exit()
            
            # Verifica se alguma tecla foi pressionada.
            if evento.type == pygame.KEYDOWN:
                
                # Verifica se a tecla pressionada é a tecla ESPAÇO.
                if evento.key == pygame.K_SPACE:
                    
                    # Se ESPAÇO foi pressionado, define 'esperando' como 
                            # False, saindo do loop de espera.
                    # Isso permite que o jogo inicie.
                    esperando = False

    # Inicia o jogo chamando a função 'jogo()'.
    # Após o jogador pressionar ESPAÇO, a função 'jogo()' é
            # executada, iniciando o loop principal do jogo.
    jogo()