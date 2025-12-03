# Importa a biblioteca Pygame, usada para desenvolver
        # jogos e aplicações multimídia.
import pygame

# Importa a biblioteca random, que permite a geração 
        # de números aleatórios.
import random

# Importa a biblioteca time, utilizada para manipular 
        # contagens de tempo no jogo.
import time

# Importa a biblioteca os, que fornece funcionalidades para 
        # interagir com o sistema operacional, como
        # manipulação de arquivos.
import os

# Importa a biblioteca sys, usada para acessar funções e variáveis que
        # interagem fortemente com o ambiente de execução do Python.
import sys

# Inicializa todos os módulos necessários da biblioteca Pygame, 
        # preparando o ambiente para desenvolvimento de jogos.
pygame.init()

# Define cores utilizando valores RGB para serem usadas no jogo,
        # facilitando a identificação e uso no código.
AZUL = (0, 122, 255)
VERMELHO = (255, 122, 122)
AMARELO = (255, 204, 0)
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Define as dimensões da janela do jogo, com uma largura de 400
        # pixels e altura de 500 pixels.
LARGURA, ALTURA = 400, 500

# Configura a tela do jogo com as dimensões especificadas.
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela do jogo que aparecerá no topo da janela.
pygame.display.set_caption("Jogo de Matemática")

# Carrega fontes do sistema para uso no jogo. 'None'
        # especifica o uso da fonte padrão do sistema.
# A primeira fonte tem tamanho 50, usada para textos principais, e a
        # segunda tem tamanho 30 para textos secundários.
fonte_principal = pygame.font.Font(None, 50)
fonte_secundaria = pygame.font.Font(None, 30)

# Especifica o nome do arquivo onde a pontuação do jogo será armazenada.
ARQUIVO_PONTUACAO = "pontuacao.txt"

# Inicializa variáveis importantes para a mecânica do jogo:
# 'tempo_inicial' define o tempo dado ao jogador para 
        # responder cada pergunta.
tempo_inicial = 10

# 'pontuacao' armazena a pontuação atual do jogador, iniciando em 0.
pontuacao = 0


# 'tempo_restante' armazena o tempo restante para a pergunta atual,
        # inicializado com o valor de 'tempo_inicial'.
tempo_restante = tempo_inicial


# 'resposta_correta' armazenará a resposta correta para a 
        # pergunta atual, iniciada como None.
resposta_correta = None


# 'jogando' é um flag que indica se o jogo está 
        # ativo, iniciado como False.
jogando = False


# Define a função para carregar a pontuação acumulada de 
        # sessões anteriores do jogo
def carregar_pontuacao():
    
    # Declara que a variável 'pontuacao' será utilizada como 
            # uma variável global dentro desta função
    global pontuacao
    
    # Verifica se o arquivo de pontuação existe no diretório atual
    if os.path.exists(ARQUIVO_PONTUACAO):
        
        # Abre o arquivo de pontuação em modo leitura
        with open(ARQUIVO_PONTUACAO, "r") as arquivo:
            
            # Tenta ler e converter o conteúdo do arquivo para inteiro e
                    # armazenar na variável 'pontuacao'
            try:
                pontuacao = int(arquivo.read())
                
            # Caso haja um erro na conversão devido ao conteúdo não 
                    # ser um inteiro válido
            except ValueError:
                
                # Define a pontuação como 0 se o conteúdo do arquivo não 
                        # puder ser convertido em um inteiro
                pontuacao = 0


# Define a função responsável por salvar a pontuação acumulada do 
        # jogo em um arquivo de texto
def salvar_pontuacao():
    
    # Abre (ou cria, se não existir) o arquivo especificado
            # no modo de escrita
    with open(ARQUIVO_PONTUACAO, "w") as arquivo:
        
        # Escreve a pontuação acumulada no arquivo, convertendo-a primeiro para string
        arquivo.write(str(pontuacao))


# Carregar pontuação ao iniciar
carregar_pontuacao()

# Define a função para criar uma nova pergunta matemática que
        # será apresentada ao jogador.
def nova_pergunta():
    
    # Declara 'resposta_correta' como uma variável global para ser
            # acessada e modificada dentro da função.
    global resposta_correta
    
    # Escolhe aleatoriamente uma operação matemática entre adição,
            # subtração, multiplicação e divisão.
    operacao = random.choice(["+", "-", "*", "/"])
    
    # Gera aleatoriamente o primeiro número da operação matemática entre 1 e 10.
    num1 = random.randint(1, 10)
    
    # Gera aleatoriamente o segundo número da operação matemática entre 1 e 10.
    num2 = random.randint(1, 10)

    # Certifica que não ocorra divisão por zero e que o resultado de
            # divisões seja sempre um número inteiro.
    if operacao == "/":
        
        # Multiplica num1 por num2 para garantir que a divisão seja exata,
                # evitando números decimais e divisão por zero.
        num1 *= num2

    # Monta a pergunta no formato de string, mostrando a operação a
            # ser realizada pelo usuário.
    pergunta = f"{num1} {operacao} {num2} = ?"
    
    # Calcula a resposta correta baseada na operação escolhida.
    if operacao == "+":
        
        # Soma num1 e num2 se a operação for adição.
        resposta_correta = num1 + num2
    
    elif operacao == "-":
    
        # Subtrai num2 de num1 se a operação for subtração.
        resposta_correta = num1 - num2
        
    elif operacao == "*":
        
        # Multiplica num1 por num2 se a operação for multiplicação.
        resposta_correta = num1 * num2
    
    elif operacao == "/":
    
        # Divide num1 por num2 (garantido ser divisão exata) se a 
                # operação for divisão, usando divisão inteira.
        resposta_correta = num1 // num2

    # Cria uma lista de opções de resposta, que inclui a resposta correta e
            # variações para aumentar o desafio.
    opcoes = [resposta_correta, resposta_correta + random.randint(1, 10), resposta_correta - random.randint(1, 10), resposta_correta + random.randint(1, 5)]
    
    # Embaralha as opções para que a posição da resposta 
            # correta não seja previsível.
    random.shuffle(opcoes)
    
    # Retorna a pergunta formulada e as opções como uma tupla.
    return pergunta, opcoes


# Define uma função para exibir texto na tela do jogo. A função 
        # centraliza o texto nas coordenadas especificadas.
def exibir_texto(texto, fonte, cor, x, y):
    
    # Renderiza o texto usando a fonte e cor especificadas. 
    # O segundo parâmetro 'True' habilita o anti-aliasing,
            # tornando o texto mais suave.
    superficie = fonte.render(texto, True, cor)
    
    # Obtém um retângulo com as dimensões do texto renderizado e
            # centraliza-o nas coordenadas (x, y) fornecidas.
    rect = superficie.get_rect(center=(x, y))
    
    # Desenha a superfície do texto renderizado na tela, na
            # posição especificada pelo retângulo.
    tela.blit(superficie, rect)



# Define a função que exibe o menu inicial do jogo.
def menu_inicial():
    
    # Preenche a tela inteira com a cor branca para limpar
            # quaisquer gráficos anteriores.
    tela.fill(BRANCO)
    
    # Exibe o título do jogo na parte superior da tela,
            # centralizado horizontalmente.
    exibir_texto("Jogo de Matemática", fonte_principal, PRETO, LARGURA // 2, ALTURA // 4)
    
    # Exibe a pontuação acumulada do jogador, centralizado 
            # horizontalmente na metade da tela.
    exibir_texto(f"Pontuação Acumulada: {pontuacao}", fonte_secundaria, PRETO, LARGURA // 2, ALTURA // 2)
    
    # Exibe uma mensagem para iniciar o jogo, centralizada e mais abaixo na tela.
    exibir_texto("Clique para Jogar", fonte_secundaria, AZUL, LARGURA // 2, ALTURA // 1.5)
    
    # Atualiza a tela para mostrar os textos renderizados.
    pygame.display.flip()

    # Inicializa uma variável para controlar o loop de
            # espera do menu inicial.
    aguardando = True

    # Continua executando o loop enquanto estiver aguardando o
            # usuário iniciar o jogo.
    while aguardando:
        
        # Itera sobre a fila de eventos do Pygame, buscando eventos
                # como cliques e fechamento da janela.
        for evento in pygame.event.get():
            
            # Verifica se o evento é do tipo QUIT, o que indica que o 
                    # usuário fechou a janela do jogo.
            if evento.type == pygame.QUIT:
                
                # Encerra a execução do Pygame, liberando recursos.
                pygame.quit()
                
                # Encerra completamente o programa.
                sys.exit()  # Encerrar o programa completamente
                
            # Verifica se o evento é um clique do mouse (botão pressionado).
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Altera a variável para sair do loop e começar o jogo.
                aguardando = False  # Começar o jogo ao clicar


# Define a função principal que controla o fluxo de jogo, manipulando 
        # perguntas, respostas e o tempo de jogo.
def jogo():

    # Declara variáveis globais que serão modificadas dentro da função.
    global tempo_restante, pontuacao, resposta_correta, jogando

    # Gera uma nova pergunta e opções de resposta 
            # chamando a função nova_pergunta.
    pergunta, opcoes = nova_pergunta()

    # Inicializa a variável que armazenará a resposta 
            # selecionada pelo jogador.
    resposta_selecionada = None

    # Armazena o momento atual em segundos desde a 
            # época (1 de janeiro de 1970) para controle de tempo.
    ultima_vez = time.time()

    # Define o estado do jogo como ativo, permitindo que o
            # loop do jogo seja executado.
    jogando = True

    # Inicializa o tempo restante com o tempo inicial definido globalmente, 
            # começando a contagem para responder à pergunta.
    tempo_restante = tempo_inicial


    # Mantém o jogo em execução enquanto a condição 'jogando' for verdadeira.
    while jogando:
        
        # Limpa a tela, preenchendo-a com a cor branca para 
                # preparar para nova renderização.
        tela.fill(BRANCO)
        
        # Obtém o tempo atual para calcular quanto tempo passou 
                # desde a última atualização.
        agora = time.time()
        
        # Calcula quanto tempo passou desde a última vez que o
                # tempo foi registrado.
        tempo_passado = agora - ultima_vez
        
        # Subtrai o tempo passado do tempo restante para a resposta.
        tempo_restante -= tempo_passado
        
        # Atualiza 'ultima_vez' para o momento atual
                # para a próxima iteração.
        ultima_vez = agora
    
        # Verifica se o tempo restante para responder à pergunta
                # chegou a zero ou menos.
        if tempo_restante <= 0:
            
            # Mostra na tela uma mensagem indicando que o tempo
                    # para responder acabou.
            exibir_texto("Tempo Esgotado!", fonte_principal, VERMELHO, LARGURA // 2, ALTURA // 2)
            
            # Atualiza a tela para mostrar a mensagem.
            pygame.display.flip()
            
            # Aguarda 2000 milissegundos (2 segundos) antes de continuar,
                    # para que o jogador veja a mensagem.
            pygame.time.delay(2000)
            
            # Muda a condição de 'jogando' para False para sair do 
                    # loop e terminar o jogo.
            jogando = False
            
            # Chama a função para salvar a pontuação acumulada no 
                    # arquivo antes de sair do jogo.
            salvar_pontuacao()
            
            # Continua para a próxima iteração do loop, caso haja
                    # mais código a executar.
            continue


        # Atualiza e exibe o tempo restante na tela, formatando-o como
                # inteiro e adicionando o sufixo 's' para segundos.
        exibir_texto(f"{int(tempo_restante)}s", fonte_secundaria, PRETO, 50, 30)
        
        # Exibe a pontuação atual do jogador na tela, localizada no
                # canto superior direito.
        exibir_texto(f"Pontuação: {pontuacao}", fonte_secundaria, PRETO, LARGURA - 80, 30)
        
        # Mostra a pergunta atual no centro da tela, um pouco abaixo do
                # topo para clareza visual.
        exibir_texto(pergunta, fonte_principal, PRETO, LARGURA // 2, 100)
        
        # Itera sobre as opções de resposta para a pergunta 
                # atual e as exibe na tela.
        # Define um conjunto de cores para diferenciar 
                # visualmente cada opção de resposta.
        cores = [AZUL, VERMELHO, AMARELO, BRANCO]
        
        # Utiliza um loop para posicionar e desenhar cada opção em
                # partes distintas da tela.
        for i in range(4):
            
            # Calcula a posição x baseada no índice da opção, 
                    # dividindo a tela em duas colunas.
            x = (i % 2) * (LARGURA // 2)
            
            # Calcula a posição y baseada no índice da opção, dividindo a 
                    # parte inferior da tela em duas linhas.
            y = 200 + (i // 2) * 100
            
            # Desenha um retângulo para cada opção, usando as cores 
                    # definidas anteriormente.
            pygame.draw.rect(tela, cores[i], (x, y, LARGURA // 2, 100))
            
            # Exibe o texto da opção dentro do retângulo, centralizado verticalmente e
                    # ajustado para ficar no centro horizontal da coluna.
            exibir_texto(str(opcoes[i]), fonte_principal, PRETO, x + (LARGURA // 4), y + 50)

        
        # Itera sobre todos os eventos que o Pygame capturou.
        for evento in pygame.event.get():
            
            # Verifica se o evento capturado é do tipo QUIT, que ocorre quando o
                    # jogador tenta fechar a janela do jogo.
            if evento.type == pygame.QUIT:
                
                # Chama a função para salvar a pontuação acumulada no arquivo antes de 
                        # sair, garantindo que o progresso do jogador seja preservado.
                salvar_pontuacao()
                
                # Encerra a biblioteca Pygame, liberando recursos.
                pygame.quit()
                
                # Encerra completamente o programa, fechando a janela e 
                        # terminando a execução.
                sys.exit()  # Encerrar o programa completamente
                
            # Verifica se o evento é um clique do mouse.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Obtém as coordenadas x e y do local onde o mouse 
                        # foi clicado na tela.
                x, y = pygame.mouse.get_pos()
                
                # Calcula em qual coluna da tela o clique ocorreu, considerando 
                        # que a tela é dividida verticalmente em duas colunas.
                coluna = x // (LARGURA // 2)
                
                # Calcula em qual linha da tela o clique ocorreu, ajustando o valor 
                        # de y para considerar apenas a área abaixo de 200 pixels do topo.
                linha = (y - 200) // 100
                
                # Calcula um índice único para a opção de resposta clicada, combinando a
                        # coluna e a linha onde o clique ocorreu.
                indice = coluna + linha * 2

                
                # Verifica se o índice calculado é válido, ou seja, se está dentro do 
                        # intervalo dos índices das opções de resposta (0 a 3).
                if 0 <= indice < 4:
                    
                    # Atribui a opção de resposta selecionada com base no
                            # índice calculado.
                    resposta_selecionada = opcoes[indice]
                    
                    # Verifica se a resposta selecionada é igual à resposta correta.
                    if resposta_selecionada == resposta_correta:
                        
                        # Incrementa a pontuação do jogador em 1 ponto por
                                # acertar a resposta.
                        pontuacao += 1
                        
                        # Exibe um texto informando que a resposta está correta
                                # na parte inferior da tela.
                        exibir_texto("Correto!", fonte_secundaria, AZUL, LARGURA // 2, ALTURA - 50)
                        
                        # Atualiza a tela para mostrar o texto "Correto!".
                        pygame.display.flip()
                        
                        # Pausa o jogo por 1000 milissegundos (1 segundo) para que o 
                                # jogador possa ver a mensagem de acerto.
                        pygame.time.delay(1000)
                        
                        # Gera uma nova pergunta e novas opções de resposta.
                        pergunta, opcoes = nova_pergunta()
                        
                        # Reinicia o tempo restante para responder à nova pergunta.
                        tempo_restante = tempo_inicial
                        
                    else:
                        
                        # Exibe um texto informando que a resposta está errada na 
                                # parte inferior da tela.
                        exibir_texto("Errado!", fonte_secundaria, VERMELHO, LARGURA // 2, ALTURA - 50)
                        
                        # Atualiza a tela para mostrar o texto "Errado!".
                        pygame.display.flip()
                        
                        # Pausa o jogo por 2000 milissegundos (2 segundos) para que o
                                # jogador possa ver a mensagem de erro.
                        pygame.time.delay(2000)
                        
                        # Define a condição de jogo para False, terminando o loop do jogo.
                        jogando = False
                        
                        # Chama a função para salvar a pontuação acumulada no
                                # arquivo antes de sair do jogo.
                        salvar_pontuacao()


        # Atualiza a tela do jogo para refletir quaisquer mudanças 
                # gráficas feitas no frame atual.
        pygame.display.flip()

# Inicia um loop infinito que mantém o jogo em execução, permitindo que o
        # jogo seja reiniciado após cada sessão.
while True:
    
    # Chama a função que exibe o menu inicial e espera por uma 
            # ação do usuário para começar o jogo.
    menu_inicial()
    
    # Inicia a lógica principal do jogo após o usuário escolher
            # começar a jogar a partir do menu inicial.
    jogo()