# Importa a biblioteca Pygame, necessária para criar jogos e gráficos em 2D
import pygame

# Importa a biblioteca Random, que permite a geração de valores aleatórios
# útil neste jogo para escolher palavras aleatoriamente para o jogador traduzir
import random

# Importa a biblioteca Time, que fornece funções relacionadas ao tempo
# essencial para controlar a contagem regressiva de tempo durante o jogo
import time

# Importa a biblioteca Os, que permite manipular arquivos e
        # interagir com o sistema operacional
        # # usada para salvar e carregar pontuações em um arquivo
import os

# Importa a biblioteca Sys, que fornece funcionalidades para
        # manipulação do sistema usada para permitir o 
        # encerramento do programa
import sys

# Inicializa todos os módulos do Pygame, preparando o 
        # ambiente necessário para executar o jogo
pygame.init()

# Define a cor Azul em formato RGB, usada para exibir 
        # uma das opções de resposta no jogo
AZUL = (0, 122, 255)

# Define a cor Vermelha em formato RGB, usada para 
        # exibir outra opção de resposta
VERMELHO = (255, 122, 122)

# Define a cor Amarela em formato RGB, usada como fundo 
        # para outras opções de resposta
AMARELO = (255, 204, 0)

# Define a cor Branca em formato RGB, usada como fundo da tela
BRANCO = (255, 255, 255)

# Define a cor Preta em formato RGB, usada para o
        # texto e outros elementos do jogo
PRETO = (0, 0, 0)

# Define a largura e a altura da tela do jogo em pixels, para 
        # configurar o tamanho da janela de exibição
LARGURA, ALTURA = 500, 500

# Cria a tela do jogo com as dimensões especificadas
# onde todos os elementos, como perguntas e 
        # respostas, serão exibidos
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela do jogo, exibido na barra
        # superior da janela
pygame.display.set_caption("Jogo de Tradução")

# Define a fonte principal para exibir textos grandes,
        # como o título do jogo ou perguntas
        # o valor 50 representa o tamanho da fonte
fonte_principal = pygame.font.Font(None, 50)

# Define a fonte secundária para exibir textos menores,
        # como instruções ou pontuação
        # o valor 30 representa o tamanho da fonte
fonte_secundaria = pygame.font.Font(None, 30)

# Define o nome do arquivo onde a pontuação será salva
        # para que o jogador possa continuar acumulando 
        # pontos em sessões futuras
ARQUIVO_PONTUACAO = "pontuacao.txt"

# Define o tempo inicial, em segundos, disponível para cada pergunta
tempo_inicial = 10

# Inicializa a pontuação do jogador com zero pontos
pontuacao = 0

# Define o tempo restante para responder, começando 
        # com o valor do tempo inicial
tempo_restante = tempo_inicial

# Define a variável para armazenar a resposta correta
        # da pergunta atual
resposta_correta = None

# Define o estado do jogo; a variável jogando indica 
        # se o jogo está em andamento
jogando = False

# Define a categoria de palavras escolhida pelo jogador, 
        # começando sem nenhuma categoria selecionada
categoria_selecionada = None

# Cria uma lista para armazenar palavras que já foram usadas
# evitando que a mesma palavra apareça repetidamente na
        # mesma sessão de jogo
palavras_usadas = []


# Dicionário com palavras em português e suas traduções, 
        # divididas por categorias
categorias_palavras = {
    "animais": {
        "cachorro": "dog",
        "gato": "cat",
        "cavalo": "horse",
        "leão": "lion",
        "tigre": "tiger",
        "pássaro": "bird",
        "peixe": "fish",
        "macaco": "monkey",
        "elefante": "elephant",
        "girafa": "giraffe",
        "urso": "bear",
        "raposa": "fox",
        "porco": "pig",
        "ovelha": "sheep",
        "coelho": "rabbit",
        "vaca": "cow",
        "cabra": "goat",
        "rato": "mouse",
        "cervo": "deer",
        "zebra": "zebra"
    },
    "objetos": {
        "casa": "house",
        "livro": "book",
        "mesa": "table",
        "cadeira": "chair",
        "porta": "door",
        "janela": "window",
        "telefone": "phone",
        "computador": "computer",
        "relógio": "clock",
        "lâmpada": "lamp",
        "cama": "bed",
        "sofá": "sofa",
        "espelho": "mirror",
        "geladeira": "fridge",
        "fogão": "stove",
        "prato": "plate",
        "copos": "glass",
        "panela": "pot",
        "garfo": "fork",
        "faca": "knife"
    },
    "natureza": {
        "sol": "sun",
        "lua": "moon",
        "estrela": "star",
        "nuvem": "cloud",
        "chuva": "rain",
        "vento": "wind",
        "árvore": "tree",
        "flor": "flower",
        "montanha": "mountain",
        "rio": "river",
        "mar": "sea",
        "lago": "lake",
        "areia": "sand",
        "pedra": "stone",
        "fogo": "fire",
        "grama": "grass",
        "céu": "sky",
        "neve": "snow",
        "relâmpago": "lightning",
        "vulcão": "volcano"
    },
    "numeros": {
        "um": "one",
        "dois": "two",
        "três": "three",
        "quatro": "four",
        "cinco": "five",
        "seis": "six",
        "sete": "seven",
        "oito": "eight",
        "nove": "nine",
        "dez": "ten",
        "onze": "eleven",
        "doze": "twelve",
        "treze": "thirteen",
        "catorze": "fourteen",
        "quinze": "fifteen",
        "dezesseis": "sixteen",
        "dezessete": "seventeen",
        "dezoito": "eighteen",
        "dezenove": "nineteen",
        "vinte": "twenty"
    }
}

# Função para carregar a pontuação de sessões anteriores
# Esta função verifica se existe um arquivo com a pontuação 
        # acumulada de jogos anteriores e, se sim, lê esse valor.
def carregar_pontuacao():
    
    # Declara a variável pontuacao como global, para que 
            # possamos modificar seu valor dentro da função
    global pontuacao
    
    # Verifica se o arquivo de pontuação existe no sistema
    if os.path.exists(ARQUIVO_PONTUACAO):
        
        # Abre o arquivo de pontuação no modo de leitura ("r") se ele existir
        with open(ARQUIVO_PONTUACAO, "r") as arquivo:
            
            # Tenta ler o conteúdo do arquivo e converter 
                    # para um número inteiro
            # Isso é importante para que a pontuação seja manipulada
                    # como um número e não como texto
            try:
                pontuacao = int(arquivo.read())
                
            # Caso ocorra um erro na conversão (por exemplo, se o 
                    # arquivo estiver vazio ou contiver dados inválidos),
                    # define a pontuação como 0 para evitar falhas no programa
            except ValueError:
                pontuacao = 0


# Função para salvar a pontuação
# Esta função grava a pontuação atual do jogador em um
        # arquivo para que seja preservada entre sessões de jogo
def salvar_pontuacao():
    
    # Abre o arquivo de pontuação no modo de escrita ("w"), o que
            # apaga o conteúdo existente no arquivo,
            # ou cria um novo arquivo se ele não existir
    with open(ARQUIVO_PONTUACAO, "w") as arquivo:
        
        # Converte a pontuação atual para uma string e grava no arquivo
        # Isso permite que a pontuação seja carregada na
                # próxima vez que o jogo iniciar
        arquivo.write(str(pontuacao))

# Chama a função para carregar a pontuação acumulada ao iniciar o jogo,
# garantindo que o jogador continue com a pontuação da última sessão
carregar_pontuacao()


# Função para criar uma nova pergunta de tradução com
        # base na categoria selecionada
# Essa função escolhe uma palavra aleatória da categoria 
        # selecionada pelo jogador e define sua tradução
        # correta, que será a resposta da pergunta.
def nova_pergunta():
    
    # Declara as variáveis globais que serão modificadas na função
    # 'resposta_correta' irá armazenar a tradução da palavra sorteada,
    # e 'palavras_usadas' irá acumular as palavras que já
            # foram sorteadas nesta rodada
    global resposta_correta, palavras_usadas
    
    # Obtém o dicionário de palavras e suas traduções para a
            # categoria atualmente selecionada
            # 'categoria_selecionada' é a categoria escolhida pelo jogador, 
            # que mapeia palavras para suas traduções
    palavras_traducao = categorias_palavras[categoria_selecionada]

    # Verifica se todas as palavras dessa categoria já foram usadas, 
            # comparando o tamanho de 'palavras_usadas'
            # com o número total de palavras em 'palavras_traducao'
    # Caso todas as palavras já tenham sido usadas, a
            # lista 'palavras_usadas' é reiniciada para um novo ciclo
    if len(palavras_usadas) >= len(palavras_traducao):
        palavras_usadas = []

    # Escolhe aleatoriamente uma palavra em português da 
            # lista de palavras disponíveis na categoria
    # Converte as chaves do dicionário em uma lista e usa 
            # 'random.choice' para selecionar uma palavra
    palavra_portugues = random.choice(list(palavras_traducao.keys()))
    
    # Enquanto a palavra escolhida já estiver na lista 
            # de 'palavras_usadas' (ou seja, já foi utilizada),
            # continua escolhendo outra palavra até encontrar uma
            # que ainda não foi utilizada
    while palavra_portugues in palavras_usadas:
        palavra_portugues = random.choice(list(palavras_traducao.keys()))

    # Adiciona a palavra selecionada à lista 'palavras_usadas' 
            # para evitar repetições nesta rodada
    palavras_usadas.append(palavra_portugues)
    
    # Define a tradução da palavra escolhida como a resposta 
            # correta para a pergunta de tradução atual
    # 'resposta_correta' irá armazenar a tradução da palavra, 
            # que é o valor correspondente à chave 'palavra_portugues'
    resposta_correta = palavras_traducao[palavra_portugues]


    # Gera as opções de resposta
    # Cria uma lista para armazenar as opções de resposta 
            # que serão exibidas ao jogador
    # Começa com a resposta correta já adicionada 
            # como primeira opção
    opcoes = [resposta_correta]
    
    # Continua adicionando opções até que a lista tenha 4 alternativas
    # Esse loop garante que o jogador veja sempre quatro opções de resposta
    while len(opcoes) < 4:
        
        # Escolhe uma tradução incorreta aleatoriamente entre 
                # todas as traduções da categoria
        opcao_errada = random.choice(list(palavras_traducao.values()))
        
        # Verifica se a opção errada ainda não foi adicionada
                # às opções de resposta
        # Isso evita que a mesma resposta incorreta apareça
                # mais de uma vez
        if opcao_errada not in opcoes:
            
            # Adiciona a opção incorreta à lista de opções
            opcoes.append(opcao_errada)
    
    # Embaralha a lista de opções para que a resposta correta 
            # não esteja sempre na mesma posição
    # Isso cria uma experiência mais desafiadora para o jogador
    random.shuffle(opcoes)
    
    # Retorna a palavra em português escolhida e a lista
            # completa das opções de resposta
    return palavra_portugues, opcoes


# Função para exibir texto centralizado na tela
# Esta função é usada para desenhar textos, como perguntas e
        # respostas, centralizados na posição desejada
def exibir_texto(texto, fonte, cor, x, y):
    
    # Renderiza o texto para criar uma superfície com o 
            # conteúdo especificado
    # 'texto' é o conteúdo que será exibido
    # 'fonte' é o estilo e o tamanho do texto
    # 'True' ativa a suavização do texto para melhor aparência
    # 'cor' define a cor do texto
    superficie = fonte.render(texto, True, cor)
    
    # Obtém o retângulo (área de exibição) do texto renderizado
    # Esse retângulo é necessário para centralizar o
            # texto na posição desejada
    rect = superficie.get_rect(center=(x, y))
    
    # Desenha (ou "blita") a superfície de texto na tela, 
            # centralizada nas coordenadas fornecidas (x, y)
    # 'tela' é onde o texto será exibido
    tela.blit(superficie, rect)


# Função para exibir o menu de seleção de categoria
# Esta função apresenta ao jogador as opções de categorias 
            # para ele escolher antes de iniciar o jogo
def menu_categorias():
    
    # Preenche a tela com a cor branca para limpar
            # qualquer conteúdo anterior
    tela.fill(BRANCO)
    
    # Exibe o título "Selecione uma Categoria" na 
            # parte superior do menu
    # A posição é centralizada horizontalmente e situada 
            # no quarto superior da tela
    exibir_texto("Selecione uma Categoria", fonte_principal, PRETO, LARGURA // 2, ALTURA // 4)
    
    # Obtém a lista de categorias disponíveis a partir das 
            # chaves do dicionário 'categorias_palavras'
    # Isso permite que o menu mostre todas as categorias 
            # disponíveis no jogo
    categorias = list(categorias_palavras.keys())
    
    # Loop para exibir cada categoria como uma opção para o jogador
    # 'i' é o índice da categoria na lista, e 'categoria' é
            # o nome da categoria atual
    for i, categoria in enumerate(categorias):
        
        # Calcula a posição vertical para cada categoria, com 
                # espaçamento entre as opções
        # 'ALTURA // 2' posiciona o primeiro item no meio da 
                # tela, e 'i * 50' adiciona 50 pixels de espaço entre cada opção
        y = ALTURA // 2 + i * 50
        
        # Exibe o nome da categoria na posição calculada, 
                # centralizado horizontalmente
        # 'categoria.capitalize()' exibe o nome com a 
                # primeira letra em maiúscula
        exibir_texto(categoria.capitalize(), fonte_secundaria, AZUL, LARGURA // 2, y)

    # Atualiza a tela para que o menu seja exibido
    pygame.display.flip()
    
    # Define uma variável de controle para aguardar a interação do jogador
    aguardando = True

    # Inicia um loop que aguarda o jogador interagir com o
            # menu para selecionar uma categoria ou fechar o jogo
    while aguardando:
        
        # Captura todos os eventos que ocorrem na janela, como 
                # cliques ou o fechamento do programa
        for evento in pygame.event.get():
            
            # Verifica se o jogador clicou para fechar a janela do jogo
            # pygame.QUIT é o evento de fechamento da janela
            # Se esse evento ocorre, o programa precisa ser encerrado
            if evento.type == pygame.QUIT:
                
                # Encerra o Pygame, liberando todos os recursos utilizados
                pygame.quit()
                
                # Encerra o programa completamente, saindo do sistema
                sys.exit()
            
            # Verifica se o jogador pressionou o botão do mouse
            # pygame.MOUSEBUTTONDOWN é o evento de clicar com o
                    # mouse, importante para seleção de categoria
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Obtém a posição (x, y) do clique do jogador na tela em pixels
                # Essa posição ajuda a identificar onde o jogador 
                        # clicou para verificar se corresponde a uma categoria
                x, y = pygame.mouse.get_pos()
                
                # Loop para verificar se o jogador clicou em uma das
                        # opções de categoria exibidas no menu
                # 'i' é o índice da categoria, enquanto 'categoria' é o nome dela
                for i, categoria in enumerate(categorias):
                    
                    # Calcula a área vertical em torno de cada categoria para
                            # determinar se o clique está dentro dessa área
                    # ALTURA // 2 + i * 50 define a posição vertical de cada
                            # categoria, espaçada de 50 pixels entre si
                    # O intervalo de +/- 20 pixels cria uma área clicável 
                            # acima e abaixo do centro do texto da categoria
                    if y > ALTURA // 2 + i * 50 - 20 and y < ALTURA // 2 + i * 50 + 20:
                        
                        # Declara 'categoria_selecionada' como global para 
                                # permitir que a variável seja atualizada
                        # Essa variável armazena a categoria escolhida pelo
                                # jogador para ser usada no jogo
                        global categoria_selecionada
                        
                        # Define a categoria clicada pelo jogador como a
                                # selecionada para o jogo
                        categoria_selecionada = categoria
                        
                        # Define 'aguardando' como False para sair do loop de espera
                        # Isso permite iniciar o jogo com a categoria 
                                # escolhida, interrompendo o menu
                        aguardando = False


# Função para exibir o menu inicial
# Esta função apresenta a tela inicial do jogo, onde o 
        # jogador pode ver o título,
# a pontuação acumulada e instruções para iniciar o jogo.
def menu_inicial():
    
    # Preenche a tela com a cor branca para limpar 
            # qualquer conteúdo anterior
    tela.fill(BRANCO)
    
    # Exibe o título "Jogo de Tradução" na tela, usando a fonte principal
    # O texto é centralizado horizontalmente e posicionado
            # na parte superior do menu
    exibir_texto("Exercício Jogo de Tradução", fonte_principal, PRETO, LARGURA // 2, ALTURA // 4)
    
    # Exibe a pontuação acumulada do jogador, utilizando a fonte
            # secundária para menor destaque
    # A posição é centralizada horizontalmente e no meio da tela
    exibir_texto(f"Pontuação Acumulada: {pontuacao}", fonte_secundaria, PRETO, LARGURA // 2, ALTURA // 2)
    
    # Exibe o texto "Clique para Jogar" para instruir o jogador a
            # clicar na tela para iniciar o jogo
    # O texto é centralizado horizontalmente e posicionado na 
            # metade inferior da tela
    exibir_texto("Clique para Jogar", fonte_secundaria, AZUL, LARGURA // 2, ALTURA // 1.5)
    
    # Atualiza a tela para mostrar o conteúdo do menu inicial
    pygame.display.flip()

    # Define uma variável de controle para aguardar a 
            # interação do jogador
    aguardando = True
    
    # Inicia um loop que aguarda o jogador clicar na
            # tela ou fechar o jogo
    while aguardando:
        
        # Captura e processa todos os eventos que ocorrem na janela
        for evento in pygame.event.get():
            
            # Verifica se o jogador clicou para fechar a janela do jogo
            if evento.type == pygame.QUIT:
                
                # Encerra o Pygame e fecha o programa
                pygame.quit()
                sys.exit()
            
            # Verifica se o jogador clicou com o botão do mouse na tela
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Sai do loop de espera e inicia o jogo
                aguardando = False


# Função principal do jogo
# Esta função controla a execução do jogo, gerenciando 
        # perguntas, respostas e o tempo disponível
def jogo():
    
    # Declara as variáveis globais que serão modificadas na função
    # 'tempo_restante' para controlar o tempo disponível para cada pergunta
    # 'pontuacao' para acumular a pontuação do jogador
    # 'resposta_correta' para armazenar a resposta correta da pergunta atual
    # 'jogando' para indicar o estado do jogo (ativo ou finalizado)
    global tempo_restante, pontuacao, resposta_correta, jogando

    # Gera uma nova pergunta para o jogador, escolhendo uma 
            # palavra e suas opções de tradução
    # 'palavra_portugues' é a palavra em português a ser traduzida, e
            # 'opcoes' são as alternativas de resposta
    palavra_portugues, opcoes = nova_pergunta()
    
    # Define 'resposta_selecionada' como None inicialmente, pois o
            # jogador ainda não escolheu uma resposta
    resposta_selecionada = None
    
    # Armazena o momento atual em segundos (timestamp) para
            # controlar o tempo que se passa durante o jogo
    # 'ultima_vez' será usado para calcular a passagem de 
            # tempo e diminuir 'tempo_restante' progressivamente
    ultima_vez = time.time()
    
    # Define a variável 'jogando' como True para indicar que o
            # jogo está em andamento
    jogando = True
    
    # Define o tempo disponível para responder a pergunta 
            # como o valor inicial de tempo
    tempo_restante = tempo_inicial


    # Inicia o loop principal do jogo, que continua enquanto 'jogando' for True
    # Este loop controla cada etapa do jogo, atualizando a tela e 
            # verificando o tempo e as respostas
    while jogando:
        
        # Preenche a tela com a cor branca para apagar o conteúdo 
                # anterior e preparar para a nova exibição
        tela.fill(BRANCO)
        
        # Captura o momento atual em segundos (timestamp) para 
                # medir a passagem de tempo
        agora = time.time()
        
        # Calcula o tempo que se passou desde o último quadro
        # 'tempo_passado' é a diferença entre o momento atual e 'ultima_vez'
        tempo_passado = agora - ultima_vez
        
        # Diminui 'tempo_restante' pelo tempo que se passou, 
                # reduzindo progressivamente o tempo disponível
        tempo_restante -= tempo_passado
        
        # Atualiza 'ultima_vez' para o momento atual, para ser 
                # usado no próximo quadro
        ultima_vez = agora

        # Verifica se o tempo disponível para responder a pergunta 
                # chegou a zero ou menos
        if tempo_restante <= 0:
            
            # Exibe a mensagem "Tempo Esgotado!" em vermelho no 
                    # centro da tela para informar o jogador
            exibir_texto("Tempo Esgotado!", fonte_principal, VERMELHO, LARGURA // 2, ALTURA // 2)
            
            # Atualiza a tela para mostrar a mensagem de tempo esgotado
            pygame.display.flip()
            
            # Pausa o jogo por 2000 milissegundos (2 segundos) para o 
                    # jogador ver a mensagem
            pygame.time.delay(2000)
            
            # Define 'jogando' como False para encerrar o loop e 
                    # finalizar o jogo
            jogando = False
            
            # Salva a pontuação atual para que o jogador não 
                    # perca o progresso
            salvar_pontuacao()
            
            # 'continue' volta ao início do loop, mas como 'jogando' é 
                    # False, o loop será encerrado
            continue

        # Exibe o tempo restante em segundos no canto superior esquerdo da tela
        # 'int(tempo_restante)' converte o valor em segundos para um número inteiro
        exibir_texto(f"{int(tempo_restante)}s", fonte_secundaria, PRETO, 50, 30)
        
        # Exibe a pontuação atual no canto superior direito da tela
        exibir_texto(f"Pontuação: {pontuacao}", fonte_secundaria, PRETO, LARGURA - 80, 30)
        
        # Exibe a pergunta de tradução para o jogador, centralizada
                # na parte superior da tela
        exibir_texto(f"Traduza: {palavra_portugues}", fonte_principal, PRETO, LARGURA // 2, 100)

        # Define uma lista de cores para os botões de resposta que
                # serão exibidos ao jogador
        # Cada resposta terá uma cor de fundo diferente para
                # facilitar a identificação
        cores = [AZUL, VERMELHO, AMARELO, BRANCO]

        # Loop para desenhar os quatro botões de resposta na tela,
                # cada um com uma opção de tradução
        # 'i' é o índice que vai de 0 a 3, representando cada
                # opção de resposta
        for i in range(4):
            
            # Calcula a posição horizontal (x) do botão, baseado em 'i'
            # 'i % 2' alterna entre 0 e 1 para cada botão, colocando 
                    # dois botões por linha
            # Multiplica pelo meio da largura da tela (LARGURA // 2) para
                    # centralizar cada par de botões
            x = (i % 2) * (LARGURA // 2)
            
            # Calcula a posição vertical (y) do botão, baseado em 'i'
            # 'i // 2' é 0 para os dois primeiros botões e 1 para os dois
                    # últimos, posicionando os botões em duas linhas
            # Começa a primeira linha de botões em 200 pixels de altura e 
                    # posiciona a segunda 100 pixels abaixo
            y = 200 + (i // 2) * 100
            
            # Desenha um retângulo (botão) na tela com a cor 
                    # correspondente em 'cores[i]'
            # Cada botão ocupa metade da largura da tela (LARGURA // 2) e 
                    # tem altura de 100 pixels
            # A posição e a cor do botão são determinadas pelas 
                    # variáveis calculadas
            pygame.draw.rect(tela, cores[i], (x, y, LARGURA // 2, 100))
            
            # Exibe o texto da opção de resposta dentro do botão, 
                    # centralizado no meio do botão
            # 'opcoes[i]' é o texto da opção de resposta, 'fonte_principal'
                    # define a fonte do texto
            # A posição é calculada para centralizar o texto dentro do botão: 
            # 'x + (LARGURA // 4)' centraliza horizontalmente dentro do botão,
            # 'y + 50' centraliza verticalmente (considerando que a 
                    # altura do botão é 100 pixels)
            exibir_texto(opcoes[i], fonte_principal, PRETO, x + (LARGURA // 4), y + 50)


        # Loop para capturar e processar eventos, como 
                    # cliques e fechamento do jogo
        for evento in pygame.event.get():
            
            # Verifica se o jogador clicou para fechar a janela do jogo
            # Se sim, salva a pontuação, encerra o Pygame e sai do sistema
            if evento.type == pygame.QUIT:
                salvar_pontuacao()    # Salva a pontuação antes de sair
                pygame.quit()         # Encerra o Pygame
                sys.exit()            # Encerra o programa
            
            # Verifica se o jogador clicou com o botão do mouse na tela
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Obtém as coordenadas (x, y) do clique do jogador na tela
                x, y = pygame.mouse.get_pos()
                
                # Calcula em qual coluna da tela o clique foi feito
                # 'LARGURA // 2' divide a tela em duas colunas para as opções
                coluna = x // (LARGURA // 2)
                
                # Calcula em qual linha o clique foi feito em relação à
                        # posição inicial dos botões
                # 'y - 200' ajusta a posição em relação ao topo da área 
                        # dos botões, que começa em 200 pixels
                # '100' é a altura de cada botão, usada para
                        # identificar a linha correspondente
                linha = (y - 200) // 100
                
                # Calcula o índice do botão clicado, usando coluna e linha
                # 'linha * 2' dá o valor de cada linha em múltiplos 
                        # de 2 (dois botões por linha)
                indice = coluna + linha * 2

                # Verifica se o índice calculado está dentro do intervalo
                        # das opções válidas (0 a 3)
                if 0 <= indice < 4:
                    
                    # Define 'resposta_selecionada' como a opção 
                            # correspondente ao índice calculado
                    resposta_selecionada = opcoes[indice]
                    
                    # Verifica se a resposta escolhida pelo jogador está correta
                    if resposta_selecionada == resposta_correta:
                        
                        # Aumenta a pontuação em 1 ponto se a resposta for correta
                        pontuacao += 1
                        
                        # Exibe uma mensagem "Correto!" em azul na parte 
                                # inferior da tela
                        exibir_texto("Correto!", fonte_secundaria, AZUL, LARGURA // 2, ALTURA - 50)
                        
                        # Atualiza a tela para mostrar a mensagem de acerto
                        pygame.display.flip()
                        
                        # Pausa o jogo por 1 segundo para que o jogador veja a mensagem
                        pygame.time.delay(1000)
                        
                        # Gera uma nova pergunta, escolhendo outra palavra e 
                                # novas opções de resposta
                        palavra_portugues, opcoes = nova_pergunta()
                        
                        # Reinicia o tempo restante para responder a nova pergunta
                        tempo_restante = tempo_inicial
                    
                    # Caso a resposta seja incorreta
                    else:
                        
                        # Exibe uma mensagem "Errado!" em vermelho na parte inferior da tela
                        exibir_texto("Errado!", fonte_secundaria, VERMELHO, LARGURA // 2, ALTURA - 50)
                        
                        # Atualiza a tela para mostrar a mensagem de erro
                        pygame.display.flip()
                        
                        # Pausa o jogo por 2 segundos para que o jogador veja a mensagem
                        pygame.time.delay(2000)
                        
                        # Define 'jogando' como False para encerrar o 
                                # loop e finalizar o jogo
                        jogando = False
                        
                        # Salva a pontuação do jogador antes de encerrar a partida
                        salvar_pontuacao()

        # Atualiza a tela com todos os elementos desenhados na 
                # iteração atual do loop
        pygame.display.flip()


# Inicia o loop principal do programa
# Este loop controla o fluxo geral do jogo, passando pelas
        # telas de menu e executando a partida
while True:
    
    # Chama a função 'menu_inicial' para exibir a tela inicial do jogo
    # Esta função mostra o título do jogo, a pontuação
            # acumulada e instruções para iniciar
    menu_inicial()
    
    # Chama a função 'menu_categorias' para exibir o menu 
            # de seleção de categorias
    # Aqui, o jogador escolhe a categoria de palavras 
            # que deseja traduzir
    menu_categorias()
    
    # Chama a função principal 'jogo' para iniciar a partida
    # Esta função gera as perguntas de tradução, controla o
            # tempo e atualiza a pontuação
    jogo()