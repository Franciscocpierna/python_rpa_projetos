"""
Lógica de Jogo

    Níveis e Transições: Como criar vários níveis em um jogo.
    
Para criar um jogo com vários níveis e transições entre eles, você 
precisa estruturar o seu jogo para lidar com diferentes estados ou 
cenas. Abaixo, você encontrará um exemplo básico de como implementar um 
jogo com três níveis diferentes. Quando o jogador coleta todos os itens de 
um nível, ele automaticamente avança para o próximo nível.

Vamos dividir isso em várias partes:

    Estruturação dos níveis.
    Transição entre os níveis.
    Inicialização e reinicialização das variáveis de cada nível.

Aqui está um código de exemplo que demonstra essa estrutura:
"""

# Importa a biblioteca pygame, que é usada para criar jogos e interfaces gráficas.
import pygame

# Importa a biblioteca sys, que fornece funções e variáveis que interagem 
# com o ambiente de execução do Python.
import sys

# Importa a biblioteca random, que contém funções para gerar números aleatórios.
import random

# Executa a função init() da biblioteca pygame, que inicializa todos
# os módulos importados necessários para o Pygame.
pygame.init()

# Define cores no formato RGB que serão utilizadas no jogo. Cada cor é uma tupla com três elementos.
# PRETO é definido como uma tupla contendo três zeros, representando a ausência de cor.
PRETO = (0, 0, 0)

# BRANCO é definido como uma tupla contendo o valor máximo para 
# vermelho, verde e azul, resultando em cor branca.
BRANCO = (255, 255, 255)

# VERDE é definido como uma tupla com o valor máximo para o verde e zero para as outras cores.
VERDE = (0, 255, 0)

# AZUL é definido como uma tupla com o valor máximo para o azul e zero para as outras cores.
AZUL = (0, 0, 255)

# Definição das dimensões da tela do jogo.
# LARGURA recebe o valor 800, representando a largura em pixels.
LARGURA = 800

# ALTURA recebe o valor 600, representando a altura em pixels.
ALTURA = 600

# A variável tela é criada chamando a função set_mode() do pygame, 
# que inicializa uma janela ou tela para exibição.
# A função recebe uma tupla com a largura e a altura definidas anteriormente.
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Configura o título da janela do jogo utilizando a função set_caption() do pygame.
# 'Níveis e Transições' é o título que aparecerá na barra de título da janela.
pygame.display.set_caption('Níveis e Transições')


# Configurações do jogador
# Define a posição x inicial do jogador como metade da 
# largura da tela, centralizando-o horizontalmente.
x_jogador = LARGURA // 2

# Define a posição y inicial do jogador como metade da altura
# da tela, centralizando-o verticalmente.
y_jogador = ALTURA // 2

# Define o tamanho do jogador, tanto para largura quanto altura, como 50 pixels.
tamanho_jogador = 50

# Define a velocidade do jogador, que é a quantidade de pixels que o jogador 
# se move a cada iteração do loop do jogo.
velocidade_jogador = 5

# Cria um objeto Rect (retângulo) para o jogador utilizando as 
# posições x e y e o tamanho especificado.
# Um Rect é uma maneira de armazenar e manipular as propriedades
# retangulares de um objeto (como posição e tamanho).
jogador = pygame.Rect(x_jogador, y_jogador, tamanho_jogador, tamanho_jogador)

# Configurações dos níveis
# Define a variável nivel_atual como 1, indicando que o jogo
# deve começar no nível 1.
nivel_atual = 1

# Define o número máximo de níveis que o jogo terá, neste caso, 3.
maximo_niveis = 3

# Cria um dicionário chamado itens_necessarios_por_nivel que mapeia
# cada nível a uma quantidade de itens que o jogador deve coletar para completá-lo.
# Por exemplo, o nível 1 requer a coleta de 3 itens, 
# o nível 2 requer 5 itens, 
# e o nível 3 requer 7 itens.
itens_necessarios_por_nivel = {1: 3, 2: 5, 3: 7}

# Função para iniciar ou reiniciar um nível
def iniciar_nivel(nivel):
    
    # Cria uma lista vazia chamada 'itens', que será preenchida com
    # os retângulos representando os itens a serem coletados no nível.
    itens = []
    
    # Inicia um loop que irá iterar um número de vezes igual ao valor 
    # associado à chave 'nivel' no dicionário 'itens_necessarios_por_nivel'.
    # Este valor representa a quantidade de itens necessários para completar o nível.
    for _ in range(itens_necessarios_por_nivel[nivel]):
        
        # Gera uma posição x aleatória para o item dentro da largura da tela,
        # subtraindo 20 para garantir que o item não seja posicionado fora da tela.
        item_x = random.randint(0, LARGURA - 20)
        
        # Gera uma posição y aleatória para o item dentro da altura da tela, 
        # aplicando a mesma lógica de subtração para evitar que o item ultrapasse
        # as bordas da tela.
        item_y = random.randint(0, ALTURA - 20)
        
        # Cria um retângulo (pygame.Rect) que representa um item, usando as 
        # posições x e y aleatórias geradas e define seu tamanho como 20x20 pixels.
        # O retângulo é a forma como o Pygame lida com os objetos gráficos em termos 
        # de sua posição e tamanho, facilitando a detecção de colisões e o desenho na tela.
        itens.append(pygame.Rect(item_x, item_y, 20, 20))
        
    # Retorna a lista de itens (retângulos) que foram criados, que será 
    # utilizada para desenhar os itens na tela e detectar colisões com o jogador.
    return itens


# Inicia o primeiro nível
itens = iniciar_nivel(nivel_atual)

# Função responsável por atualizar a aparência da tela do jogo.
def desenhar_tela():
    
    # Preenche o fundo da tela com a cor preta. Este é geralmente o primeiro passo ao redesenhar a cena,
    # para limpar qualquer desenho anterior antes de iniciar um novo quadro.
    tela.fill(PRETO)
    
    # Desenha o jogador na tela. O jogador é representado por um retângulo (pygame.Rect) e
    # é preenchido com a cor verde. O retângulo 'jogador' já contém a posição e o
    # tamanho definidos anteriormente.
    pygame.draw.rect(tela, VERDE, jogador)
    
    # Inicia um loop para desenhar cada item coletável na tela. Esses 
    # itens estão armazenados na lista 'itens'.
    for item in itens:
        
        # Cada item é desenhado na tela na forma de uma elipse azul. O objeto 
        # 'item' é um retângulo que define a posição e o tamanho da elipse.
        pygame.draw.ellipse(tela, AZUL, item)
    
    # Define a fonte do texto que será utilizado para mostrar o nível atual na tela. 
    # O tamanho da fonte é 36.
    # O 'None' significa que está sendo usada a fonte padrão do sistema.
    fonte = pygame.font.SysFont(None, 36)
    
    # Cria um objeto de imagem do texto que mostra o nível atual. A função 'render'
    # recebe o texto a ser mostrado,
    # um valor booleano para anti-aliasing (True significa que 
    # o anti-aliasing está ativado, o que torna o texto mais suave),
    # e a cor do texto, que neste caso é branco.
    texto_nivel = fonte.render(f'Nível: {nivel_atual}', True, BRANCO)
    
    # Coloca a imagem do texto sobre a superfície da tela. O texto 
    # do nível é posicionado no canto superior esquerdo (10, 10) da tela.
    tela.blit(texto_nivel, (10, 10))
    
    # Atualiza a tela completa para mostrar o novo quadro que acabamos
    # de desenhar. Este comando efetivamente faz o Pygame
    # trocar os buffers da tela, onde o buffer de trás, que acabamos de
    # desenhar, passa a ser o buffer de frente, visível ao jogador.
    pygame.display.flip()


# Este é o loop principal do jogo, onde o estado do jogo é atualizado constantemente.
rodando = True  # A variável 'rodando' é usada para manter o loop em execução. É inicialmente definida como True.
    
while rodando:  # Começa o loop que continuará rodando enquanto a variável 'rodando' for True.
    
    # Inicia um loop que verificará todos os eventos que o Pygame detecta.
    # Os eventos são ações do usuário como pressionamento de teclas, cliques do mouse, etc.
    for evento in pygame.event.get():  
        
        # Aqui é feita a verificação para o tipo de evento. Se o tipo do evento for QUIT, isso indica que o usuário
        # deseja fechar a janela do jogo, o que é geralmente feito clicando no
        # 'X' da janela ou enviando um sinal de fechamento.
        if evento.type == pygame.QUIT:  
            
            # Esta chamada de função desativa o módulo do Pygame e fecha a janela do jogo. 
            # É uma boa prática chamar essa função antes de fechar o seu programa.
            pygame.quit()  
            
            # 'sys.exit()' é uma função do módulo 'sys' que sai do programa. Quando o Pygame é fechado,
            # 'sys.exit()' assegura que nenhum código adicional será executado e o programa termina.
            sys.exit()  

    
    # Movimento do jogador
    # Esta função cria uma sequência de valores booleanos representando o estado de cada tecla do teclado,
    # onde True indica que a tecla está sendo pressionada no momento.
    teclas = pygame.key.get_pressed()  # Obtém o estado de todas as teclas do teclado. 
    
    # Verifica se a tecla de seta para a esquerda está pressionada.
    if teclas[pygame.K_LEFT]:
        
        # Move o jogador para a esquerda diminuindo o valor de 'x' pela 'velocidade_jogador'.
        # O 'x' representa a posição horizontal do jogador na tela.
        jogador.x -= velocidade_jogador
        
    # Verifica se a tecla de seta para a direita está pressionada.
    if teclas[pygame.K_RIGHT]:
        
        # Move o jogador para a direita aumentando o valor de 'x' pela 'velocidade_jogador'.
        # Isso move o retângulo do jogador horizontalmente para a direita na tela.
        jogador.x += velocidade_jogador
        

    # Verifica se a tecla de seta para cima está pressionada.
    if teclas[pygame.K_UP]:
        
        # Move o jogador para cima diminuindo o valor de 'y' pela 'velocidade_jogador'.
        # O 'y' representa a posição vertical do jogador na tela.
        jogador.y -= velocidade_jogador
        

    # Verifica se a tecla de seta para baixo está pressionada.
    if teclas[pygame.K_DOWN]:
        
        # Move o jogador para baixo aumentando o valor de 'y' pela 'velocidade_jogador'.
        # Isso move o retângulo do jogador verticalmente para baixo na tela.
        jogador.y += velocidade_jogador
        

    # Mantém o jogador dentro da tela
    # Este método assegura que o jogador (um objeto Rect) nunca se mova para fora da área da tela.
    # 'clamp_ip' altera o retângulo do jogador in-place (ou seja, no próprio objeto) para 
    # que ele seja movido para dentro do retângulo da tela se estiver fora.
    # 'tela.get_rect()' obtém um novo retângulo que tem o tamanho da tela.
    # Se alguma parte do jogador estiver fora desse retângulo, ele será ajustado 
    # para que se encaixe dentro dos limites da tela.
    jogador.clamp_ip(tela.get_rect())
    
    
    # Verifica colisão com itens
    # Cria um loop sobre uma cópia da lista de itens para
    # evitar modificar a lista enquanto ela está sendo iterada.
    for item in itens[:]:
        
        # Verifica se o retângulo do jogador colide com o retângulo do item.
        if jogador.colliderect(item):
            
            # Se uma colisão é detectada, o item é removido da lista original de itens.
            itens.remove(item)

    # Se todos os itens forem coletados, avança para o próximo nível
    # Checa se a lista de itens está vazia (ou seja, todos os itens foram 
    # coletados) e se o nível atual é menor que o número máximo de níveis.
    if not itens and nivel_atual < maximo_niveis:
        
        # Incrementa o contador do nível atual, avançando para o próximo nível.
        nivel_atual += 1
        
        # Reinicia ou inicia o próximo nível gerando uma nova lista de itens
        # com a função 'iniciar_nivel'.
        itens = iniciar_nivel(nivel_atual)

    
    # Se passou do último nível, o jogo termina
    # Verifica se não restam itens a serem coletados e se o jogador está no último nível.
    elif not itens and nivel_atual == maximo_niveis:
        
        # Se verdadeiro, imprime uma mensagem de parabéns no console.
        print("Parabéns, você completou todos os níveis!")
        
        # Altera a variável 'rodando' para False, o que causa a saída do 
        # loop principal do jogo e, consequentemente, termina o jogo.
        rodando = False

    # Desenha a tela
    # Chama a função 'desenhar_tela()' para atualizar o display com
    # os elementos visuais atuais do jogo.
    desenhar_tela()

    # Controla a taxa de quadros por segundo (fps)
    # Cria um relógio e o usa para limitar o jogo a um máximo de 60 quadros
    # por segundo (fps), o que ajuda a manter o jogo rodando de maneira suave e consistente.
    pygame.time.Clock().tick(60)

# Após sair do loop do jogo, aguarda 2000 milissegundos (ou 2 segundos), 
# o que pode ser usado para mostrar uma tela final ou simplesmente dar um tempo
# antes de encerrar completamente o jogo.
pygame.time.delay(2000)

# Fecha a janela do jogo e termina todos os módulos do Pygame,
# limpando os recursos usados pelo Pygame.
pygame.quit()
    
