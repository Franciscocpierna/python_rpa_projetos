"""
Introdução ao PyGame

    - Conceitos Básicos: Janela, cores, coordenadas.
    
Neste exemplo, criaremos uma janela com uma dimensão 
de 500x500 pixels. Dentro dessa janela, desenharemos um 
retângulo vermelho e um círculo azul para demonstrar o uso 
de cores e coordenadas.
"""

# Importamos o módulo pygame
import pygame

# Inicializamos o módulo pygame
pygame.init()

# Definimos as dimensões da janela (largura x altura)
tela_largura = 800
tela_altura = 600

# Criamos a janela onde tudo será desenhado
# A função 'set_mode()' é chamada no módulo 'display' do Pygame para inicializar uma janela ou tela para exibição.
# Ela requer uma tupla ou lista com dois elementos, representando a largura e a altura da tela, respectivamente.
# O valor de retorno é um objeto Surface que é desenhado na tela real quando 'display.flip()' ou 'display.update()' é chamado.
tela = pygame.display.set_mode((tela_largura, tela_altura))

# Definimos as cores em formato RGB
# As cores no Pygame são definidas utilizando uma estrutura de dados do tipo tupla com três elementos.
# Cada elemento representa um dos canais de cor: vermelho (R), verde (G) e azul (B).
# Cada valor do canal de cor pode variar de 0 a 255, onde 0 significa ausência da cor e 255 a intensidade máxima.

# A cor BRANCO é definida com a máxima intensidade dos três 
# canais de cor, resultando em branco puro.
BRANCO = (255, 255, 255)

# A cor VERDE é definida com a intensidade máxima no canal 
# verde e ausência de cor nos canais vermelho e azul.
VERDE = (0, 255, 0)

# A cor AZUL é definida com a intensidade máxima no canal 
# azul e ausência de cor nos canais vermelho e verde.
AZUL = (0, 0, 255)

# A cor VERMELHO é definida com a intensidade máxima no 
# canal vermelho e ausência de cor nos canais verde e azul.
VERMELHO = (255, 0, 0)


# Definimos um booleano para manter nosso loop de jogo rodando
rodando = True

# Iniciamos o loop principal do jogo
# Este é o início do loop principal do jogo. 'rodando' é uma variável booleana que mantém o loop em execução.
# O loop continuará a executar até que a variável 'rodando' seja definida como False.
while rodando:
    
    # Verificamos a fila de eventos
    # Pygame trabalha com um sistema de eventos para interagir com o usuário.
    # A função 'pygame.event.get()' obtém uma lista de todos os eventos que 
    # aconteceram desde a última vez que a função foi chamada.
    # Cada evento é um objeto Pygame com pelo menos dois atributos: 'type' e 'dict'.
    # 'type' é um identificador inteiro de um evento específico, e 'dict' é um
    # dicionário com mais informações sobre o evento, quando aplicável.
    for evento in pygame.event.get():
        
        # if evento.type == pygame.QUIT:
        # Este é um teste condicional para verificar se o tipo de evento atual é um evento 'QUIT'.
        # 'pygame.QUIT' é um evento que é acionado quando o usuário fecha a janela do
        # jogo, normalmente através do botão de fechar na barra de título.
        if evento.type == pygame.QUIT:
            
            # rodando = False
            # Se o evento for do tipo 'QUIT', a variável 'rodando' é definida como False.
            # Isso causa a saída do loop principal, já que a condição 'while rodando' não será mais verdadeira.
            # A saída do loop principal geralmente leva a um encerramento ordenado do programa ou jogo.
            rodando = False

    
    # Preenchemos o fundo com branco
    tela.fill(BRANCO)
    
    # Desenhamos um retângulo verde
    # A função 'pygame.draw.rect()' é usada para desenhar um retângulo na superfície especificada.
    # O primeiro argumento 'tela' é a superfície onde o retângulo será desenhado.
    # O segundo argumento 'VERDE' é a cor do retângulo, que foi definida anteriormente com uma tupla RGB.
    # O terceiro argumento é uma tupla que define a posição e o tamanho do retângulo: (x, y, largura, altura).
    # A posição (x, y) é o canto superior esquerdo do retângulo.
    # O argumento opcional 'width' especifica a espessura das bordas do retângulo.
    # Se 'width' for omitido ou definido como 0, o retângulo será preenchido.
    pygame.draw.rect(tela, VERDE, (50, 50, 100, 50))

    # Desenhamos um círculo azul
    # A função 'pygame.draw.circle()' é usada para desenhar um círculo na superfície especificada.
    # O primeiro argumento 'tela' é a superfície onde o círculo será desenhado.
    # O segundo argumento 'AZUL' é a cor do círculo, que foi definida anteriormente com uma tupla RGB.
    # O terceiro argumento é uma tupla ou lista com dois elementos que representam o centro do círculo (x, y).
    # O quarto argumento '75' é o raio do círculo.
    # O argumento opcional 'width' especifica a espessura da linha do círculo.
    # Se 'width' for omitido ou definido como 0, o círculo será preenchido.
    pygame.draw.circle(tela, AZUL, (200, 150), 75)

    # Desenhamos uma linha vermelha
    # A função 'pygame.draw.line()' é usada para desenhar uma linha na superfície especificada.
    # O primeiro argumento 'tela' é a superfície onde a linha será desenhada.
    # O segundo argumento 'VERMELHO' é a cor da linha, que foi definida anteriormente com uma tupla RGB.
    # Os argumentos terceiro e quarto são as tuplas que representam o ponto inicial (x1, y1) 
    # e o ponto final (x2, y2) da linha.
    # O quinto argumento '5' é a espessura da linha.
    pygame.draw.line(tela, VERMELHO, (100, 200), (300, 350), 5)

    # Atualizamos a tela para exibir o que foi desenhado
    # 'pygame.display.flip()' é uma função que atualiza toda a superfície da tela para mostrar o que foi desenhado.
    # Após desenhar todas as formas, esta função é chamada para tornar as mudanças visíveis na tela.
    # Essa função troca os buffers de tela, se estiver usando a dupla bufferização.
    # Isso significa que todas as operações de desenho são feitas em um buffer de tela oculto, 
    # e 'flip()' faz esse buffer se tornar visível.
    pygame.display.flip()


# Finalizamos o Pygame antes de fechar o programa
pygame.quit()