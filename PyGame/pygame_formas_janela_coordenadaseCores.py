"""
Introdução ao PyGame

    - Conceitos Básicos: Janela, cores, coordenadas.
    
Neste exemplo, criaremos uma janela com uma dimensão 
de 500x500 pixels. Dentro dessa janela, desenharemos um 
retângulo vermelho e um círculo azul para demonstrar o uso 
de cores e coordenadas.
"""

# Importa o módulo Pygame para usar suas funções e classes
import pygame

# Inicializa todos os módulos do Pygame
pygame.init()

# Define as dimensões da janela (500 pixels de largura e 500 pixels de altura)
largura, altura = 500, 500

# Cria uma janela com as dimensões especificadas
# O resultado é armazenado na variável 'janela', que é um objeto Surface
janela = pygame.display.set_mode((largura, altura))

# Define cores usando tuplas (R, G, B)
vermelho = (255, 0, 0)
azul = (0, 0, 255)

# Variável para controlar o loop principal do jogo
rodando = True

# Loop principal do jogo
while rodando:

    # Captura todos os eventos que acontecem na janela
    for evento in pygame.event.get():
        
        # Se o tipo do evento for QUIT (fechar janela), sai do loop
        if evento.type == pygame.QUIT:
            rodando = False

    # Desenha um retângulo vermelho na janela
    # As coordenadas (50, 50) representam a posição do canto superior esquerdo do retângulo
    # As dimensões do retângulo são 100x50 (largura x altura)
    pygame.draw.rect(janela, vermelho, (50, 50, 100, 50))

    # Desenha um círculo azul na janela
    # As coordenadas (250, 250) representam o centro do círculo
    # O raio do círculo é 50 pixels
    pygame.draw.circle(janela, azul, (250, 250), 50)

    # Atualiza a janela para mostrar os desenhos
    pygame.display.update()

# Finaliza o Pygame
pygame.quit()