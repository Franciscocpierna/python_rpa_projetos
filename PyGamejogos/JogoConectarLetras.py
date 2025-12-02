# Importa a biblioteca Pygame, que será usada para criar a 
        # interface gráfica e lógica do jogo.
import pygame

# Importa a biblioteca math para realizar cálculos matemáticos 
        # necessários para posicionamento e movimento.
import math

# Importa a biblioteca time para manipular contagens
        # de tempo dentro do jogo.
import time

# Importa a biblioteca random para gerar números aleatórios,
        # útil para embaralhar letras ou escolher palavras aleatoriamente.
import random

# Importa o módulo tkinter para criar interfaces gráficas 
        # adicionais, como caixas de diálogo.
import tkinter as tk

# Importa messagebox de tkinter para mostrar alertas e
        # mensagens ao usuário.
from tkinter import messagebox

# Inicializa a biblioteca Pygame, preparando o sistema
        # para uso de recursos como janelas, eventos e desenho gráfico.
pygame.init()

# Cria um objeto Tkinter que será usado para interagir com 
        # alertas e outras funcionalidades de interface gráfica.
tela_jogo = tk.Tk()

# Oculta a janela principal do Tkinter para não interferir na
        # interface do Pygame, mantendo o foco no jogo.
tela_jogo.withdraw()

# Define as dimensões da janela do jogo Pygame.
LARGURA, ALTURA = 400, 600

# Cria a janela do jogo com as dimensões especificadas.
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela do jogo, que aparece na barra de título da janela.
pygame.display.set_caption("Jogo de Conectar Letras")

# Define um conjunto de cores em formato RGB para 
        # serem usadas no jogo.
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (34, 177, 76)
AZUL_CLARO = (173, 216, 230)
VERMELHO = (237, 28, 36)
CINZA_CLARO = (200, 200, 200)

# Cria diferentes fontes e tamanhos para uso no jogo, usando a fonte 'arial'.
fonte_palavra = pygame.font.SysFont("arial", 30)  # Usada para exibir palavras formadas e mensagens.
fonte_letra = pygame.font.SysFont("arial", 50)   # Usada para desenhar as letras na tela.
fonte_botao = pygame.font.SysFont("arial", 20)   # Usada para etiquetar botões.

# Define uma função chamada 'salvar_pontuacao_txt', que é 
        # responsável por salvar a pontuação atual do jogador
        # em um arquivo de texto.
def salvar_pontuacao_txt(pontos):
    
    # Abre ou cria um arquivo chamado 'pontuacao.txt' no
            # modo de escrita ('w').
    # O modo 'w' significa que o conteúdo do arquivo será 
            # apagado e substituído pelo novo conteúdo.
    with open("pontuacao.txt", "w") as arquivo:
        
        # Converte a pontuação, que é um número inteiro, para
                # uma string usando 'str()' e escreve essa string
                # no arquivo. 
        # A conversão é necessária porque a função 'write' só aceita strings.
        arquivo.write(str(pontos))


# Define uma função chamada 'carregar_pontuacao', que tenta 
        # ler a pontuação salva no arquivo e retorná-la 
        # como um número inteiro.
def carregar_pontuacao():
    
    # Usa um bloco 'try' para tentar executar um 
            # código que pode gerar exceções (erros).
    try:
    
        # Tenta abrir o arquivo 'pontuacao.txt' no modo de leitura ('r').
        with open("pontuacao.txt", "r") as arquivo:
            
            # Lê o conteúdo do arquivo, que é esperado ser uma
                    # string representando um número inteiro.
            # Usa a função 'int()' para converter essa string 
                    # para um número inteiro.
            return int(arquivo.read())
            
    # O bloco 'except' captura exceções específicas que 
            # podem ocorrer no bloco 'try'.
    except (FileNotFoundError, ValueError):
        
        # Se o arquivo não existir ('FileNotFoundError') ou se o 
                # conteúdo do arquivo não puder ser convertido para
                # inteiro ('ValueError'),
        # a função retornará 0, assumindo que não há pontuação
                # salva ou que há um erro nos dados salvos.
        return 0


# Carrega a pontuação salva anteriormente ao iniciar o jogo. 
# Se não houver pontuação salva ou se ocorrer algum erro ao 
        # ler o arquivo, a pontuação será zero.
pontuacao = carregar_pontuacao()

# Cria uma lista de palavras que serão usadas no jogo.
# Estas palavras variam em comprimento de 4 a 10 letras,
        # proporcionando diferentes níveis de desafio.
palavras = ["CALA", "CASA", "MOLHO", "DANÇA", "CATIVA", "BALANÇO", "PROVAÇÃO", "ALEGRIA", "COMPORTO", "EXPECTATIVA",
            "HARMONIA", "FORTALEZA", "SUSTENTAR", "ENCANTADOR", "MOVIMENTO", "CONSOLADOR", "INSPIRADOR", "LUMINOSIDADE",
            "ESTABILIDADE", "RESILIÊNCIA", "AMIZADE", "COOPERAÇÃO", "PERSISTÊNCIA", "COMPREENSÃO", "INTERPRETAR",
            "DESENVOLVIMENTO", "CONHECIMENTO", "CRIATIVIDADE", "INOVAÇÃO", "PERSEVERANÇA"]

# Configura a variável 'letras', que armazena as letras da 
        # palavra atual que o jogador deve formar.
# A palavra é selecionada com base no valor da pontuação, 
        # usando o operador módulo (%) para ciclar pelas palavras na lista.
# Isso garante que sempre haja uma palavra correspondente 
        # disponível, independentemente do valor da pontuação.
letras = list(palavras[pontuacao % len(palavras)])  # Seleciona a palavra inicial baseada na pontuação atual

# Inicializa uma lista vazia que será usada para armazenar
        # as posições das letras na tela.
posicoes_letras = []

# Inicializa uma string vazia que irá acumular as letras
        # selecionadas pelo jogador para formar a palavra.
palavra_formada = ""

# Define uma variável booleana para controlar se o botão do 
        # mouse está sendo pressionado. Isso é útil para 
        # rastrear movimentos de arrasto.
mouse_pressionado = False

# Inicializa uma variável para armazenar o resultado de cada 
        # tentativa de formar uma palavra. Pode ser 'Correto!' 
        # ou 'Incorreto!', mas começa como None.
resultado = None

# Inicializa uma variável para registrar o momento em que um 
        # resultado (correto ou incorreto) é mostrado, para 
        # controlar quanto tempo ele fica visível.
mostrar_resultado_tempo = 0

# Define uma função para calcular posições circulares para
        # as letras no jogo.
# Esta função é útil para distribuir uniformemente as letras
        # ao redor de um ponto central na tela.
def calcular_posicoes_circulares(centro_x, centro_y, raio, letras):
    
    # Define o ângulo inicial de posicionamento das letras como 0 graus.
    angulo_inicial = 0
    
    # Calcula o incremento de ângulo com base no número total de letras.
    # Isso divide um círculo completo (360 graus) igualmente para todas as letras.
    angulo_incremento = 360 / len(letras)
    
    # Inicializa uma lista vazia que armazenará as posições (x, y) de cada letra.
    posicoes = []
    
    # Itera sobre o número de letras fornecido.
    for i in range(len(letras)):
        
        # Calcula o ângulo atual para a letra multiplicando o incremento 
                # de ângulo pelo índice da letra.
        # O resultado é convertido de graus para radianos, pois as funções
                # trigonométricas do Python usam radianos.
        angulo = math.radians(angulo_inicial + i * angulo_incremento)
        
        # Calcula a posição x da letra usando o cosseno do ângulo. 
        # O cosseno determina a coordenada x no círculo, baseado no
                # raio e no centro especificado.
        # O resultado é ajustado para ser um inteiro e é somado à 
                # coordenada x do centro para posicionar corretamente.
        x = centro_x + int(raio * math.cos(angulo))
        
        # Calcula a posição y da letra usando o seno do ângulo.
        # O seno determina a coordenada y no círculo, de forma similar ao cosseno para x.
        # Também é ajustado para ser um inteiro e somado à coordenada y do centro.
        y = centro_y + int(raio * math.sin(angulo))
        
        # Adiciona a posição calculada (x, y) à lista de posições.
        posicoes.append((x, y))
    
    # Retorna a lista completa de posições. Cada posição corresponde a 
            # uma letra da palavra a ser formada no jogo.
    return posicoes


# Define uma função chamada 'atualizar_palavra' que não recebe 
        # argumentos externos, mas modifica várias variáveis globais.
def atualizar_palavra():
    
    # Declara que as variáveis listadas serão usadas como globais, 
            # permitindo que esta função modifique seus valores.
    global letras, posicoes_letras, palavra_formada, resultado, mostrar_resultado_tempo, conexoes
    
    # Seleciona uma nova palavra da lista 'palavras' baseada
            # na pontuação atual do jogador.
    # O índice da palavra é determinado usando o módulo da pontuação
            # pela quantidade de palavras disponíveis,
            # garantindo que sempre haverá uma palavra válida
            # independente do valor da pontuação.
    letras = list(palavras[pontuacao % len(palavras)])
    
    # Embaralha as letras da palavra selecionada para aumentar o
            # desafio e garantir que cada jogo seja único.
    random.shuffle(letras)
    
    # Chama a função 'calcular_posicoes_circulares' para 
            # determinar as posições em que as letras embaralhadas
            # serão exibidas na tela. Isso cria um layout circular
            # das letras ao redor do ponto central da tela.
    posicoes_letras = calcular_posicoes_circulares(LARGURA // 2, ALTURA // 2, 120, letras)
    
    # Reseta a variável 'palavra_formada', que é usada para armazenar a
            # sequência de letras que o jogador forma ao interagir com o jogo.
    palavra_formada = ""
    
    # Limpa a lista 'conexoes', que armazena as posições das letras 
            # que o jogador conectou até agora.
    conexoes = []
    
    # Reseta a variável 'resultado', usada para informar ao 
            # jogador se a palavra formada está correta ou incorreta.
    resultado = None
    
    # Reseta a variável 'mostrar_resultado_tempo', que controla 
            # quanto tempo o resultado é exibido na tela.
    mostrar_resultado_tempo = 0


# Inicia com a primeira palavra embaralhada
atualizar_palavra()

# Define uma função chamada 'desenhar_jogo', que não recebe
        # argumentos e é responsável por atualizar a interface gráfica do jogo.
def desenhar_jogo():
    
    # Preenche toda a tela com a cor azul claro, criando um fundo 
            # limpo para desenhar os outros elementos gráficos.
    tela.fill(AZUL_CLARO)

    # Renderiza o texto que mostra a palavra que está sendo formada 
            # pelo jogador, usando a fonte definida anteriormente.
    # O parâmetro 'True' ativa o suavizado do texto, tornando-o 
            # mais legível e agradável visualmente.
    texto_palavra = fonte_palavra.render(f"Palavra: {palavra_formada}", True, PRETO)
    
    # Posiciona o texto da palavra formada no centro horizontal 
            # da tela e a 80 pixels de altura.
    tela.blit(texto_palavra, (LARGURA // 2 - texto_palavra.get_width() // 2, 80))

    # Renderiza o texto que mostra a pontuação atual do jogador, 
            # também com suavização ativada.
    texto_pontuacao = fonte_palavra.render(f"Pontuação: {pontuacao}", True, PRETO)
    
    # Posiciona o texto da pontuação no canto superior direito da tela, 
            # subtraindo a largura do texto mais 20 pixels da largura
            # total da tela para um pequeno recuo.
    tela.blit(texto_pontuacao, (LARGURA - texto_pontuacao.get_width() - 20, 20))

    # Prepara o texto para o botão 'Ver Palavra', que pode ser 
            # pressionado para revelar a palavra correta.
    botao_texto = fonte_botao.render("Ver Palavra", True, PRETO)
    
    # Define as dimensões e posição do retângulo do botão, que 
            # fica na parte inferior esquerda da tela.
    botao_retangulo = pygame.Rect(20, ALTURA - 50, 120, 30)
    
    # Desenha o retângulo do botão na tela, preenchendo-o
            # com a cor cinza claro.
    pygame.draw.rect(tela, CINZA_CLARO, botao_retangulo)
    
    # Posiciona o texto do botão centralizado horizontalmente dentro do 
            # retângulo do botão e ajusta verticalmente para ficar 
            # visivelmente centralizado.
    tela.blit(botao_texto, (botao_retangulo.x + 10, botao_retangulo.y + 5))


    # Itera sobre cada letra e sua posição correspondente. 
    # A função enumerate() é usada para obter o índice (i) 
            # junto com a letra e a posição.
    for i, (letra, (x, y)) in enumerate(zip(letras, posicoes_letras)):
        
        # Desenha um círculo para cada letra na posição (x, y) 
                # com um raio de 30 pixels. A cor do círculo é verde.
        # Este círculo serve como fundo para a letra, 
                # destacando-a na interface do jogo.
        pygame.draw.circle(tela, VERDE, (x, y), 30)
        
        # Renderiza a letra usando a fonte especificada para letras, 
                # definida globalmente na inicialização do jogo.
        # O segundo parâmetro 'True' ativa o suavizado do texto, 
                # tornando a letra mais nítida e agradável visualmente.
        # A cor do texto é branca, o que contrasta com o fundo verde do círculo.
        texto_letra = fonte_letra.render(letra, True, BRANCO)
        
        # Posiciona o texto da letra na tela. As coordenadas x e y são
                # ajustadas para que o texto fique centralizado
                # dentro do círculo.
        # Isso é feito subtraindo metade da largura e metade da altura 
                # do texto renderizado das coordenadas x e y, respectivamente.
        tela.blit(texto_letra, (x - texto_letra.get_width() // 2, y - texto_letra.get_height() // 2))


    # Verifica se existem pelo menos duas conexões, o que significa
                # que o jogador conectou pelo menos duas letras.
    if len(conexoes) > 1:
        
        # Itera sobre cada par de conexões consecutivas 
                # para desenhar linhas entre elas.
        for i in range(len(conexoes) - 1):
            
            # Desenha uma linha entre a conexão atual e a próxima na lista.
            # A cor da linha é preta, e a largura da linha é 3 pixels, 
                    # tornando-a claramente visível.
            pygame.draw.line(tela, PRETO, conexoes[i], conexoes[i + 1], 3)


    # Verifica se há um resultado para ser exibido (se a
            # palavra foi julgada como correta ou incorreta).
    if resultado:
        
        # Define a cor do texto do resultado baseado na correção da resposta.
        # Verde para respostas corretas, vermelho para incorretas.
        cor = VERDE if resultado == "Correto!" else VERMELHO
        
        # Renderiza o texto do resultado usando a fonte 
                # especificada para palavras.
        # A renderização inclui suavização (antialiasing) 
                # para melhorar a clareza visual.
        texto_resultado = fonte_palavra.render(resultado, True, cor)
        
        # Posiciona o texto do resultado centralizado horizontalmente
                # na tela e na posição y = 500 pixels.
        # Isso coloca o resultado visivelmente abaixo do centro
                # da tela, facilitando a distinção visual entre 
                # a jogabilidade e o feedback.
        tela.blit(texto_resultado, (LARGURA // 2 - texto_resultado.get_width() // 2, 500))


# Define uma função que recebe a posição do mouse como um argumento e 
        # verifica qual letra está mais próxima dessa posição.
def verificar_letra_mais_proxima(pos):
    
    # Itera sobre cada letra e suas posições na tela. A função enumerate() é
            # usada para obter o índice (i) junto com as coordenadas (x, y) de cada letra.
    for i, (x, y) in enumerate(posicoes_letras):
        
        # Calcula a distância euclidiana entre a posição do 
                # mouse (pos) e a posição da letra.
        # A distância é calculada usando o Teorema de Pitágoras, 
                # onde (pos[0] - x) e (pos[1] - y) são os lados do triângulo retângulo.
        distancia = math.sqrt((pos[0] - x) ** 2 + (pos[1] - y) ** 2)
        
        # Verifica se a distância calculada é menor que 30 pixels.
        # Este valor, 30, atua como um limiar para determinar se o
                # mouse está suficientemente próximo para considerar 
                # que a letra foi selecionada.
        if distancia < 30:
            
            # Se a distância for menor que 30 pixels, retorna a 
                    # letra correspondente e suas coordenadas.
            # Isso permite que a letra seja considerada como
                    # selecionada pelo jogador.
            return letras[i], (x, y)
    
    # Se nenhuma letra estiver suficientemente próxima do 
            # mouse (nenhuma letra dentro do raio de 30 pixels),
            # a função retorna None, None, indicando que
            # nenhuma seleção válida foi feita.
    return None, None


# Define uma função para verificar se a palavra
            # formada pelo jogador é a correta.
def verificar_palavra():
    
    # Declara que a função modificará as variáveis globais 
            # 'resultado', 'pontuacao' e 'mostrar_resultado_tempo'.
    global resultado, pontuacao, mostrar_resultado_tempo

    # Compara a palavra que o jogador formou ('palavra_formada') com a
            # palavra correta no momento, que é determinada pela pontuação atual.
    # A palavra correta é obtida acessando a lista 'palavras' no índice 
            # correspondente ao resto da divisão da pontuação pelo
            # número total de palavras.
    if palavra_formada == palavras[pontuacao % len(palavras)]:
        
        # Se a palavra formada é correta, define 'resultado' como "Correto!".
        resultado = "Correto!"
        
        # Incrementa a pontuação do jogador em 1, reconhecendo seu
                # sucesso em formar a palavra correta.
        pontuacao += 1
        
        # Chama a função 'salvar_pontuacao_txt' para salvar a nova 
                # pontuação no arquivo, garantindo que o progresso
                # não seja perdido.
        salvar_pontuacao_txt(pontuacao)
        
    else:
        
        # Se a palavra formada não é a correta, define
                # 'resultado' como "Incorreto!".
        resultado = "Incorreto!"

    # Registra o momento atual (usando 'time.time()') em
            # 'mostrar_resultado_tempo'.
    # Isso é usado para controlar por quanto tempo o 
            # resultado (correto ou incorreto) será exibido na tela.
    mostrar_resultado_tempo = time.time()


# Define uma função que não recebe argumentos e é usada para
        # mostrar a palavra correta ao jogador por meio de um alerta.
def mostrar_palavra_alerta():
    
    # Calcula o índice da palavra correta atual baseado na pontuação
            # do jogador e no número total de palavras disponíveis.
    # Isso assegura que a palavra exibida sempre corresponda à 
            # tentativa atual do jogador.
    palavra_atual = palavras[pontuacao % len(palavras)]
    
    # Utiliza a função 'showinfo' do módulo 'messagebox' do
            # Tkinter para exibir uma janela de alerta.
    # O título da janela é "Palavra Correta", e o conteúdo do alerta é
            # a palavra correta atual, formatada em uma frase explicativa.
    messagebox.showinfo("Palavra Correta", f"A palavra correta é: {palavra_atual}")


# Inicializa uma lista vazia chamada 'conexoes'. Esta lista 
        # será usada para armazenar as conexões (linhas) entre
        # as letras selecionadas pelo jogador.
conexoes = []

# Inicia uma variável booleana 'rodando' como True. 
# Esta variável controla a continuação ou não do loop principal do jogo.
rodando = True

# Inicia o loop principal que mantém o jogo em execução.
while rodando:
    
    # Itera por cada evento na fila de eventos do Pygame.
    for evento in pygame.event.get():
        
        # Verifica se o evento é do tipo QUIT, o que ocorre 
                # quando o jogador fecha a janela do jogo.
        if evento.type == pygame.QUIT:
            
            # Altera a variável 'rodando' para False, o que
                    # encerra o loop e termina o jogo.
            rodando = False
        
        # Verifica se houve um evento de clique do mouse (botão pressionado).
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            # Verifica se o clique foi dentro das coordenadas do botão "Ver Palavra".
            if pygame.Rect(20, ALTURA - 50, 120, 30).collidepoint(evento.pos):
                
                # Chama a função que mostra a palavra correta em um alerta do Tkinter.
                mostrar_palavra_alerta()
                
            else:
                
                # Se o clique foi em qualquer outro lugar, inicia o
                        # processo de formação de palavra.
                mouse_pressionado = True
                
                # Reinicia a palavra formada para começar a
                        # formação de uma nova palavra.
                palavra_formada = ""
                
                # Limpa a lista de conexões, que guarda as posições 
                        # das letras selecionadas.
                conexoes = []
        
        # Verifica se o botão do mouse foi solto.
        elif evento.type == pygame.MOUSEBUTTONUP:
            
            # Marca que o mouse não está mais sendo pressionado.
            mouse_pressionado = False
            
            # Chama a função para verificar se a palavra formada é correta.
            verificar_palavra()
        
        # Verifica se o mouse está se movendo enquanto o botão está pressionado.
        elif evento.type == pygame.MOUSEMOTION and mouse_pressionado:
            
            # Chama a função para encontrar a letra mais
                    # próxima da posição atual do mouse.
            letra, pos = verificar_letra_mais_proxima(evento.pos)
            
            # Verifica se a letra foi identificada e ainda não
                    # foi adicionada às conexões.
            if letra and pos not in conexoes:
                
                # Adiciona a letra à palavra que está sendo formada.
                palavra_formada += letra
                
                # Adiciona a posição da letra à lista de conexões.
                conexoes.append(pos)


    # Desenha o jogo
    desenhar_jogo()
    
    # Verifica se um resultado foi definido e se passaram
            # mais de 2 segundos desde que ele foi mostrado.
    if resultado and time.time() - mostrar_resultado_tempo > 2:
        
        # Checa se o resultado da tentativa anterior foi "Correto!".
        if resultado == "Correto!":
            
            # Se o jogador acertou a palavra, a função 'atualizar_palavra' é chamada.
            # Esta função carrega uma nova palavra e reinicia todos 
                    # os parâmetros necessários para começar uma nova rodada.
            atualizar_palavra()
            
        else:
            
            # Se o jogador não acertou a palavra, a palavra formada é 
                    # limpa para permitir uma nova tentativa.
            palavra_formada = ""
            
            # As conexões, que guardam as posições das letras 
                    # selecionadas, são também limpas.
            conexoes = []
            
            # O resultado é limpo para remover qualquer texto de 
                    # feedback da tela, limpando a interface para nova tentativa.
            resultado = None
    
    # Atualiza a tela, desenhando quaisquer mudanças feitas 
            # nos passos anteriores.
    pygame.display.flip()

# Encerra a execução do Pygame, fechando a janela do
        # jogo e liberando os recursos utilizados.
pygame.quit()

# Destroi a janela do Tkinter, que estava oculta mas
        # ainda em execução em segundo plano.
tela_jogo.destroy()