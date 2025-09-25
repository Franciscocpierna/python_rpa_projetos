"""
Gráficos em PyGame

    - Texturas e Imagens: Carregar e exibir imagens.
    Animações: Mover objetos, animação de quadros (sprites).
"""

# Importamos o módulo pygame, que é uma biblioteca usada 
# para fazer jogos e construir aplicações com funcionalidades gráficas.
import pygame

# Inicializamos o pygame, que é necessário para configurar 
# os módulos internos do pygame que serão utilizados.
pygame.init()

# Definimos as dimensões da janela (largura x altura) que será criada.
# Aqui a largura é definida como 800 pixels e a altura como 600 pixels.
largura_tela = 800
altura_tela = 600

# Criamos a janela onde será exibida a imagem.
# A função 'set_mode' do módulo 'display' do pygame é utilizada 
# para definir o tamanho da janela baseado nas dimensões fornecidas.
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Carregamos a imagem a partir do arquivo.
# A variável 'caminho_imagem' deve conter o caminho para a imagem que você deseja exibir.
# A função 'pygame.image.load()' é utilizada para carregar a imagem do disco.
caminho_imagem = 'imagem_exemplo.jpg'  # Substitua pelo caminho da sua imagem
imagem_original = pygame.image.load(caminho_imagem)

# Definimos o tamanho desejado para a imagem (largura x altura).
# Aqui a largura é definida como 700 pixels e a altura como 500 pixels.
tamanho_novo = (700, 500)

# Redimensionamos a imagem para o tamanho desejado.
# A função 'pygame.transform.scale()' é utilizada para ajustar a imagem ao tamanho novo.
# Isso é útil para garantir que a imagem se encaixe na interface do jogo ou aplicação.
imagem_redimensionada = pygame.transform.scale(imagem_original, tamanho_novo)

# Definimos a variável 'executando' para controlar o loop principal.
# Isso permite que o loop continue rodando enquanto 'executando' for verdadeiro.
executando = True

# Iniciamos o loop principal do programa.
while executando:
    
    # Verificamos a fila de eventos do pygame.
    # Eventos são ações do usuário como pressionar uma tecla ou mover o mouse.
    for evento in pygame.event.get():
        
        # Se o evento for um pedido para fechar a janela do jogo
        # (clique no 'X' da janela), saímos do loop.
        if evento.type == pygame.QUIT:
            executando = False

    # Preenchemos o fundo da tela com preto.
    # A cor preta é definida pela tupla (0, 0, 0), onde 
    # cada valor corresponde a uma parte do RGB (Vermelho, Verde, Azul).
    tela.fill((0, 0, 0))

    # Exibimos a imagem redimensionada na tela.
    # A função 'blit' é usada para desenhar a imagem na superfície da tela.
    # O primeiro argumento é a imagem a ser desenhada e o segundo é a
    # posição (x, y) onde o topo esquerdo da imagem será colocado.
    tela.blit(imagem_redimensionada, (50, 50))

    # Atualizamos o conteúdo da tela.
    # A função 'pygame.display.flip()' atualiza toda a superfície
    # da tela para mostrar as novas imagens ou cores que foram desenhadas.
    pygame.display.flip()

# Encerramos o pygame ao sair do loop principal.
# A função 'pygame.quit()' é usada para desinicializar todos os
# módulos do pygame e liberar os recursos.
pygame.quit()