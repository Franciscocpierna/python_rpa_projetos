
"""
Introdução ao PyGame

    - Instalação e Configuração: Como instalar e configurar o PyGame.
    

pip install pygame


Isso instalará a última versão do PyGame. Para verificar se a instalação
foi bem-sucedida, você pode executar o seguinte comando Python no seu terminal:

import pygame
print(pygame.ver)

"""
print()
"""
Introdução ao PyGame

    - Hello World em PyGame: Seu primeiro programa.
    
Agora que o PyGame está instalado, você pode criar seu primeiro 
programa. Esse será um programa simples que abre uma janela do PyGame.
"""

# Importa o módulo pygame para que possamos usar suas classes e funções.
import pygame

# Chama a função init() do módulo pygame.
# Isso inicializa todos os módulos e bibliotecas internas que o Pygame usa.
pygame.init()

# Define as variáveis 'largura' e 'altura' para armazenar as dimensões da janela do jogo.
# Neste caso, a janela terá 800 pixels de largura e 600 pixels de altura.
largura, altura = 800, 600

# Cria a janela do jogo usando a função set_mode() do módulo pygame.display.
# O argumento desta função é uma tupla que contém a largura e a altura da janela.
# A função retorna um objeto Surface que representa a janela visível.
janela = pygame.display.set_mode((largura, altura))

# Utiliza a classe SysFont para criar um objeto de fonte.
# O primeiro argumento é o nome da fonte a ser usada (None para usar a fonte padrão).
# O segundo argumento é o tamanho da fonte em pontos.
fonte = pygame.font.SysFont(None, 74)

# Usa o método 'render' do objeto de fonte para criar um objeto de superfície contendo texto.
# O primeiro argumento é o texto a ser renderizado.
# O segundo argumento é um booleano que indica se o texto deve ser suavizado (True) ou não (False).
# O terceiro argumento é a cor do texto, fornecida como uma tupla (R, G, B).
texto = fonte.render('Olá, Mundo!', True, (255, 255, 255))

# Declara uma variável booleana 'rodando' e a inicializa como True.
# Essa variável será usada para controlar o loop principal do jogo.
# Enquanto 'rodando' for True, o loop continuará a ser executado.
rodando = True

# Este é o loop principal do jogo, que continuará a ser 
# executado enquanto a variável 'rodando' for True.
while rodando:
    
    # O método pygame.event.get() retorna uma lista de eventos que 
    # ocorreram desde a última vez que o método foi chamado.
    # O loop 'for' itera sobre cada um desses eventos.
    for evento in pygame.event.get():
        
        # Verifica se o tipo do evento é QUIT.
        # O evento QUIT ocorre quando o usuário fecha a janela do jogo.
        if evento.type == pygame.QUIT:
            
            # Se o evento QUIT ocorrer, a variável 'rodando' é definida como False.
            # Isso fará com que o loop principal do jogo pare de executar.
            rodando = False

    # O método 'blit' do objeto Surface (neste caso, 'janela') desenha um 
    # objeto de superfície (neste caso, 'texto') em sua superfície.
    # Os números (250, 250) representam as coordenadas x e y na superfície 'janela' onde 
    # o canto superior esquerdo do objeto de superfície 'texto' será colocado.
    janela.blit(texto, (250, 250))

    # O método pygame.display.update() atualiza a janela inteira.
    # Isso significa que quaisquer mudanças feitas na superfície da janela desde a última atualização se tornarão visíveis.
    pygame.display.update()

# Finaliza o PyGame
pygame.quit()