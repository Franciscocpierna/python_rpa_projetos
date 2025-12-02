# Importação da biblioteca pygame para 
        # criar jogos gráficos
import pygame

# Importação da biblioteca random para geração 
        # de números aleatórios
import random

# Importação da biblioteca time para manipulação
        # de tempo (cronômetros, pausas)
import time

# Importação da biblioteca os para interação 
        # com o sistema operacional
import os

# Inicializa a biblioteca Pygame, configurando todos os
        # módulos necessários para o jogo
pygame.init()

# Configuração das dimensões da tela do jogo
LARGURA, ALTURA = 400, 600

# Cria a janela do jogo com as dimensões especificadas
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título que aparecerá na barra de 
        # título da janela do jogo
pygame.display.set_caption("Jogo de Conectar Números")

# Definição das cores básicas usadas no jogo, 
        # usando tuplas RGB
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Dicionário que associa cada número de 1 a 9 a uma cor
        # específica para fácil visualização
cores = {
    1: (0, 255, 0),     # Verde
    2: (0, 0, 255),     # Azul
    3: (255, 0, 0),     # Vermelho
    4: (255, 255, 0),   # Amarelo
    5: (200, 0, 200),   # Roxo
    6: (255, 100, 0),   # Laranja
    7: (0, 255, 255),   # Ciano
    8: (255, 100, 150), # Rosa
    9: (100, 0, 255)    # Azul escuro
}

# Seleção da fonte para o texto no jogo, definindo 
        # tipo e tamanho da fonte
fonte = pygame.font.SysFont("arial", 24)

# Configurações da grade de jogo, especificando número de
        # linhas e colunas, e o tamanho de cada célula
linhas, colunas = 6, 5
tamanho_celula = 60
margem = 5

# Criação da matriz que representa a grade do jogo, 
        # preenchida com números aleatórios de 1 a 9
numeros_grade = [[random.randint(1, 9) for _ in range(colunas)] for _ in range(linhas)]

# Inicialização das variáveis de controle do jogo

# Pontuação inicial do jogador
pontuacao = 0  

# Número de conexões necessárias para avançar 
        # para a próxima fase
meta_conexoes = 20  

# Lista para armazenar as conexões feitas pelo jogador
conexoes = []  

# Flag para verificar se o botão do mouse 
        # está pressionado
mouse_pressionado = False

# Duração de cada fase em segundos
tempo_fase = 60  

# Fase inicial do jogo
fase = 1  

# Flag para controlar se o jogo terminou
jogo_terminado = False  

# Marca o tempo inicial da fase corrente
inicio_tempo = time.time()

# Contador para acompanhar o progresso de 
        # conexões feitas na fase atual
progresso_conexao = 0  


# Esta função é responsável por desenhar os círculos
        # com números dentro na tela do jogo.
def desenhar_grade():
    
    # Itera sobre cada linha da matriz que 
            # representa a grade do jogo.
    for linha in range(linhas):
        
        # Para cada linha, itera sobre cada coluna.
        for coluna in range(colunas):
            
            # Obtém o número armazenado na posição
                    # específica [linha][coluna] da matriz.
            numero = numeros_grade[linha][coluna]
            
            # Calcula a posição x (horizontal) onde o círculo
                    # deve ser desenhado.
            # Multiplica a coluna pelo tamanho da célula e pela
                    # margem, e adiciona um deslocamento de 50 pixels
                    # para não desenhar muito próximo da borda da janela.
            x = coluna * (tamanho_celula + margem) + 50
            
            # Calcula a posição y (vertical) de maneira similar à 
                    # posição x, mas adiciona um deslocamento de 150 pixels.
            y = linha * (tamanho_celula + margem) + 150
            
            # Acessa o dicionário 'cores' usando o número como 
                    # chave para obter a cor correspondente.
            cor = cores[numero]
            
            # Desenha um círculo na tela na posição (x, y) calculada. 
            # A posição é ajustada para o centro da célula
                    # ao adicionar metade do tamanho da célula tanto 
                    # para x quanto para y. O último argumento é 
                    # o raio do círculo,
                    # que é metade do tamanho da célula.
            pygame.draw.circle(tela, cor, (x + tamanho_celula // 2, y + tamanho_celula // 2), tamanho_celula // 2)
            
            # Determina a cor do texto que será desenhado sobre o círculo.
            # Isso depende da luminosidade da cor do círculo.
            # Se a soma dos componentes RGB da cor for maior que 400, é
                    # considerada uma cor clara e o texto deve
                    # ser preto (cor contrastante).
            # Caso contrário, usa-se branco para o texto 
                    # sobre fundos escuros.
            if sum(cor) > 400:  # Cor clara
                cor_texto = PRETO
                
            else:  # Cor escura
                cor_texto = BRANCO
                
            # Cria um objeto de texto renderizando o número como 
                    # string, com anti-aliasing ativado (True) e
                    # na cor determinada.
            texto = fonte.render(str(numero), True, cor_texto)
            
            # Posiciona o texto renderizado sobre o círculo, ajustando 
                    # levemente a posição para centralizar o número.
            # A posição x é ajustada para a direita por 20 pixels e y
                    # para baixo por 15 pixels da posição do círculo.
            tela.blit(texto, (x + 20, y + 15))


# Esta função verifica se o local onde o mouse foi clicado 
        # corresponde a uma célula válida para fazer
        # uma conexão no jogo.
def verificar_conexao(pos):
    
    # Extrai as coordenadas x e y da posição do
            # mouse da variável 'pos'.
    x, y = pos
    
    # Calcula em qual coluna da grade o clique do mouse caiu.
    # Subtrai 50 pixels, que é o deslocamento inicial, e
            # divide pelo tamanho total da célula incluindo a
            # margem para encontrar o índice da coluna.
    coluna = (x - 50) // (tamanho_celula + margem)
    
    # Calcula em qual linha da grade o clique do mouse
            # caiu, de maneira similar à coluna.
    linha = (y - 150) // (tamanho_celula + margem)
    
    # Verifica se os índices da linha e coluna calculados
            # estão dentro dos limites válidos da grade.
    if 0 <= linha < linhas and 0 <= coluna < colunas:
    
        # Obtém o número da célula clicada na grade.
        numero = numeros_grade[linha][coluna]
        
        # Verifica se a lista de conexões está vazia, o
                # que significa que é o primeiro clique,
                # ou se o número clicado é igual ao último 
                # número na lista de conexões.
        if not conexoes or (numero == numeros_grade[conexoes[-1][0]][conexoes[-1][1]]):
        
            # Verifica se a célula clicada está adjacente à última 
                    # célula na lista de conexões,
                    # considerando conexões diagonais também.
            if not conexoes or (abs(linha - conexoes[-1][0]) <= 1 and abs(coluna - conexoes[-1][1]) <= 1):
            
                # Verifica se a célula já foi incluída na lista de
                        # conexões para evitar que seja conectada novamente.
                if (linha, coluna) not in conexoes:
                
                    # Adiciona a célula à lista de conexões se ela 
                            # passar por todas as verificações anteriores.
                    conexoes.append((linha, coluna))


# Função para desenhar linhas conectando os 
        # números selecionados pelo jogador.
def desenhar_conexoes():
    
    # Itera através dos índices das conexões já feitas, mas
            # ignora o último elemento por enquanto,
            # pois precisamos de um ponto inicial e um ponto
            # final para formar uma linha.
    for i in range(len(conexoes) - 1):
    
        # Calcula a posição x (horizontal) do primeiro ponto
                # da linha (ponto inicial).
        # Isso é feito pegando a coluna do número na lista de 
                # conexões, multiplicando pelo tamanho da
                # célula e pela margem, adicionando um deslocamento
                # horizontal de 50 pixels, e ajustando pela metade 
                # do tamanho da célula para centralizar.
        x1 = conexoes[i][1] * (tamanho_celula + margem) + 50 + tamanho_celula // 2
        
        # Calcula a posição y (vertical) do primeiro ponto de 
                # maneira similar, mas com um deslocamento 
                # vertical de 150 pixels.
        y1 = conexoes[i][0] * (tamanho_celula + margem) + 150 + tamanho_celula // 2
        
        # Calcula a posição x do segundo ponto da linha (ponto final) 
                # usando o próximo índice na lista de conexões.
        x2 = conexoes[i + 1][1] * (tamanho_celula + margem) + 50 + tamanho_celula // 2
        
        # Calcula a posição y do segundo ponto da mesma 
                # forma que o primeiro.
        y2 = conexoes[i + 1][0] * (tamanho_celula + margem) + 150 + tamanho_celula // 2
        
        # Desenha uma linha na tela do jogo usando as
                # posições calculadas (x1, y1) e (x2, y2).
        # A linha é desenhada na cor branca, com uma 
                # espessura de 5 pixels para ser bem visível.
        pygame.draw.line(tela, BRANCO, (x1, y1), (x2, y2), 5)


# Função destinada a atualizar a grade após cada
        # movimento válido do jogador.
def atualizar_grade():
    
    # Declara que as variáveis 'pontuacao' e 'progresso_conexao' 
            # serão utilizadas como globais,
            # permitindo que modificações feitas aqui 
            # se reflitam em todo o programa.
    global pontuacao, progresso_conexao

    # Verifica se o jogador fez uma conexão válida (ao 
            # menos duas células foram conectadas).
    if len(conexoes) > 1:
    
        # Incrementa a pontuação do jogador pelo número de
                # conexões feitas.
        pontuacao += len(conexoes)
        
        # Incrementa o progresso de conexão, que é usado para
                # determinar quando o jogador avança de fase.
        progresso_conexao += len(conexoes)

        # Itera sobre cada par (linha, coluna) na 
                # lista de conexões.
        for linha, coluna in conexoes:
            
            # Substitui o número na célula especificada por um 
                    # novo número aleatório entre 1 e 9.
            numeros_grade[linha][coluna] = random.randint(1, 9)
        
        # Chama a função 'garantir_conexoes_disponiveis' para
                # assegurar que ainda existam possíveis 
                # conexões após a atualização.
        # Isso evita situações onde o jogador não possa 
                # realizar nenhum movimento.
        garantir_conexoes_disponiveis()

    # Limpa a lista de conexões após atualizar a grade, preparando-a 
            # para o próximo conjunto de movimentos do jogador.
    conexoes.clear()


# Função que atualiza a tela do jogo para mostrar as
        # informações de pontuação, fase, tempo e progresso.
def desenhar_pontuacao():
    
    # Renderiza o texto da pontuação atual usando a fonte definida,
            # ativando o anti-aliasing com True,
            # e define a cor do texto como preto.
    # "Pontuação: {pontuacao}" é uma string formatada 
            # que mostra o valor atual da pontuação.
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, PRETO)
    
    # Desenha o texto da pontuação na tela na 
            # posição (10, 10), que é próximo ao 
            # canto superior esquerdo.
    tela.blit(texto_pontuacao, (10, 10))
    
    # Renderiza o texto da fase atual da mesma forma,
            # informando em que fase o jogador está.
    texto_fase = fonte.render(f"Fase: {fase}", True, PRETO)
    
    # Posiciona o texto da fase um pouco abaixo do texto
            # da pontuação, na posição (10, 40).
    tela.blit(texto_fase, (10, 40))
    
    # Calcula o tempo restante para a fase atual. `time.time()` 
            # retorna o tempo atual em segundos desde a época,
            # e `inicio_tempo` é o momento em que a fase começou.
    # A diferença dá o tempo decorrido, que subtraído do tempo
            # total da fase dá o tempo restante.
    # `max(0, int(...))` garante que o tempo exibido
            # não seja negativo caso o tempo estimado 
            # tenha sido ultrapassado.
    tempo_restante = max(0, int(tempo_fase - (time.time() - inicio_tempo)))
    
    # Renderiza o texto do tempo restante.
    texto_tempo = fonte.render(f"Tempo: {tempo_restante}s", True, PRETO)
    
    # Posiciona o texto do tempo restante abaixo do 
            # texto da fase, na posição (10, 70).
    tela.blit(texto_tempo, (10, 70))
    
    # Renderiza o texto do progresso das conexões, mostrando
            # quantas conexões foram feitas e quantas são
            # necessárias para completar a fase.
    texto_progresso = fonte.render(f"Progresso: {progresso_conexao}/{meta_conexoes}", True, PRETO)
    
    # Posiciona o texto do progresso abaixo do texto 
            # do tempo, na posição (10, 100).
    tela.blit(texto_progresso, (10, 100))


# Esta função é responsável por verificar se o jogador 
        # atingiu a meta necessária para avançar para a
        # próxima fase do jogo.
def verificar_proxima_fase():
    
    # Utiliza as variáveis globais 'fase', 'meta_conexoes', 
            # 'inicio_tempo', 'pontuacao' e 'progresso_conexao'
            # para manter a continuidade e atualização 
            # do estado do jogo.
    global fase, meta_conexoes, inicio_tempo, pontuacao, progresso_conexao

    # Checa se o progresso atual de conexões alcançou ou excedeu a 
            # meta necessária para passar para a próxima fase.
    if progresso_conexao >= meta_conexoes:
        
        # Se a condição for verdadeira, o jogo avança para a 
                # próxima fase, incrementando o número da fase.
        fase += 1
        
        # Reseta o contador de progresso de conexões para 
                # zero para começar a contagem da nova fase.
        progresso_conexao = 0
        
        # Aumenta a meta de conexões necessárias para a 
                # próxima fase em 5 unidades.
        # Isso faz com que cada nova fase se torne 
                # progressivamente mais desafiadora.
        meta_conexoes += 5
        
        # Reseta o relógio para medir o tempo da nova fase, 
                # armazenando o momento atual em que a fase começa.
        inicio_tempo = time.time()
        
        # Chama a função 'salvar_pontuacao' para gravar a 
                # pontuação do jogador ao atingir uma nova fase.
        # Essa funcionalidade é importante para manter um 
                # registro de desempenho ao longo do tempo.
        salvar_pontuacao()


# Esta função verifica se o tempo alocado para a fase 
        # atual do jogo se esgotou, determinando o fim do jogo.
def verificar_fim_jogo():
    
    # Utiliza a variável global 'jogo_terminado' para 
            # modificar seu estado em todo o contexto do programa.
    global jogo_terminado

    # Calcula o tempo restante na fase atual. 'time.time()' 
            # retorna o tempo atual em segundos desde a época,
    # e 'inicio_tempo' é o momento em que a fase começou, 
            # também em segundos. A subtração resulta no 
            # tempo decorrido, que é então subtraído 
            # do 'tempo_fase', o tempo total alocado para a fase.
    tempo_restante = tempo_fase - (time.time() - inicio_tempo)

    # Verifica se o tempo restante é menor ou igual a 
            # zero e se o jogo ainda não foi marcado 
            # como terminado.
    if tempo_restante <= 0 and not jogo_terminado:
        
        # Se ambos os critérios forem verdadeiros,
                # marca o jogo como terminado.
        jogo_terminado = True
        
        # Chama a função 'salvar_pontuacao' para registrar a 
                # pontuação final do jogador.
        # Isso é útil para manter um histórico de pontuações 
                # ou para apresentar ao jogador ao final do jogo.
        salvar_pontuacao()


# Função destinada a exibir uma mensagem de fim de jogo na
            # tela quando o tempo de uma fase se esgota.
def exibir_fim_jogo():
    
    # Preenche a tela inteira com a cor branca para criar um
            # fundo limpo onde a mensagem será exibida.
    # Isso remove qualquer conteúdo anterior que estava 
            # sendo exibido na tela.
    tela.fill(BRANCO)

    # Define a mensagem de texto que será exibida ao usuário.
    mensagem = "Tempo esgotado! Fim de jogo."

    # Cria um objeto de imagem de texto usando a fonte 
            # pré-definida. O texto é renderizado com
            # anti-aliasing (True), o que suaviza as bordas
            # das letras, e a cor do texto é definida
            # como preta (PRETO).
    texto = fonte.render(mensagem, True, PRETO)

    # Posiciona o texto renderizado no centro da tela. 
    # O cálculo é feito subtraindo metade da largura e altura do texto
    # das coordenadas centrais da tela (LARGURA // 2 e 
            # ALTURA // 2). Isso centraliza o texto
            # horizontal e verticalmente.
    tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - texto.get_height() // 2))

    # Atualiza a tela inteira para garantir que qualquer
            # alteração feita (neste caso, o texto adicionado)
            # seja refletida visualmente na tela do usuário.
    pygame.display.flip()

    # Pausa o jogo por 3000 milissegundos (ou 3 segundos) 
            # antes de prosseguir. Isso dá tempo suficiente
    # para o jogador ler a mensagem de fim de jogo antes
            # que o programa possa fechar ou reiniciar.
    pygame.time.delay(3000)

# Esta função verifica se existem possíveis conexões (pares
        # de números adjacentes iguais) na grade do jogo.
# Se não encontrar nenhum par válido, ela rearranja os 
        # números para garantir que haja pelo menos uma
        # possível conexão.
def garantir_conexoes_disponiveis():

    # Verifica horizontalmente se existem pares de 
            # números adjacentes iguais em cada linha.
    for linha in range(linhas):

        # Colunas - 1 para evitar sair do limite da lista.
        for coluna in range(colunas - 1):
            
            # Se um par adjacente igual for encontrado na
                    # mesma linha, encerra a função,
                    # pois isso indica que ainda existem 
                    # movimentos possíveis.
            if numeros_grade[linha][coluna] == numeros_grade[linha][coluna + 1]:
                return

    # Inicia a verificação de pares adjacentes iguais
            # verticalmente para cada coluna da grade.
    for coluna in range(colunas):
        
        # Percorre cada linha na coluna atual, exceto a última,
                # para evitar acessar um índice fora dos
                # limites da lista.
        for linha in range(linhas - 1):
        
            # Compara o número atual com o número na linha 
                    # seguinte na mesma coluna.
            # Se os números forem iguais, significa que existe
                    # uma conexão possível entre eles.
            if numeros_grade[linha][coluna] == numeros_grade[linha + 1][coluna]:
            
                # Interrompe a função imediatamente e retorna ao chamador,
                        # pois a existência de pelo menos um par
                        # adjacente igual significa que ainda há
                        # jogadas possíveis.
                return
    
    # Se a função não encontrou nenhum par adjacente igual 
            # nas verificações verticais, começa o processo 
            # de redefinição da grade para garantir que o 
            # jogador tenha novas possibilidades de conexões.
    for linha in range(linhas):
        for coluna in range(colunas):
            
            # Gera um novo número aleatório entre 1 e 9 e o
                    # atribui à posição atual da grade.
            # Isso é feito para cada célula da grade, 
                    # efetivamente embaralhando todos os números.
            numeros_grade[linha][coluna] = random.randint(1, 9)



# Define a função para salvar a pontuação do jogador em
        # um arquivo de texto, permitindo um 
        # histórico de desempenho.
def salvar_pontuacao():
    
    # Abre (ou cria, se não existir) um arquivo 
            # chamado 'pontuacao.txt' no modo de adição ('a'),
            # que permite escrever no final do arquivo
            # sem apagar o conteúdo existente.
    with open("pontuacao.txt", "a") as arquivo:
        
        # Escreve uma linha no arquivo com o 
                # formato "Fase x, Pontuação: y",
                # onde 'x' é o número da fase atual e 'y' é 
                # a pontuação atual do jogador.
        # O '\n' no final da string assegura que cada 
                # entrada será em uma nova linha.
        arquivo.write(f"Fase {fase}, Pontuação: {pontuacao}\n")

# Inicializa a variável 'rodando' como True, que será 
        # usada para controlar o loop principal do jogo.
rodando = True

# Loop principal do jogo que continua executando 
        # enquanto a variável 'rodando' for True.
while rodando:
    
    # Verifica se o jogo ainda não foi marcado
            # como terminado.
    if not jogo_terminado:
        
        # Preenche a tela com a cor branca para 
                # limpar o quadro anterior.
        tela.fill(BRANCO)
        
        # Chama a função para desenhar a grade
                # de números na tela.
        desenhar_grade()
        
        # Chama a função para desenhar as linhas 
                # conectando os números selecionados.
        desenhar_conexoes()
        
        # Chama a função para desenhar a pontuação, 
                # fase e tempo restante na tela.
        desenhar_pontuacao()

        # Processa eventos da fila de eventos do Pygame.
        for evento in pygame.event.get():
            
            # Verifica se o tipo do evento é QUIT (clicar 
                    # no botão de fechar a janela).
            if evento.type == pygame.QUIT:
                
                # Define 'rodando' como False para sair do 
                        # loop principal e terminar o jogo.
                rodando = False
                
            # Verifica se o botão do mouse foi pressionado e
                    # o jogo não está terminado.
            elif evento.type == pygame.MOUSEBUTTONDOWN and not jogo_terminado:
                
                # Marca que o mouse foi pressionado.
                mouse_pressionado = True
                
                # Chama a função para verificar se o clique do
                        # mouse foi em uma conexão válida.
                verificar_conexao(pygame.mouse.get_pos())
                
            # Verifica se o botão do mouse foi solto e o
                    # jogo não está terminado.
            elif evento.type == pygame.MOUSEBUTTONUP and not jogo_terminado:
                
                # Marca que o mouse foi solto.
                mouse_pressionado = False
                
                # Atualiza a grade com base nas conexões feitas.
                atualizar_grade()
                
                # Verifica se o jogador avançou para a próxima fase.
                verificar_proxima_fase()
                
                # Verifica se o tempo para a fase atual terminou.
                verificar_fim_jogo()
                
            # Verifica se o mouse está em movimento enquanto o
                    # botão está pressionado.
            elif evento.type == pygame.MOUSEMOTION and mouse_pressionado:
                
                # Continua verificando conexões enquanto o mouse se
                    # move com o botão pressionado.
                verificar_conexao(pygame.mouse.get_pos())

        # Verifica a condição de fim de jogo em cada frame, para 
                # garantir que o jogo termine quando o tempo esgotar.
        verificar_fim_jogo()
        
        # Atualiza a tela com as mudanças feitas.
        pygame.display.flip()
        
    else:
        
        # Se o jogo terminou, exibe a mensagem de fim de jogo.
        exibir_fim_jogo()

        # Define 'rodando' como False para sair do loop
                # principal após a mensagem de fim de
                # jogo ser exibida.
        rodando = False

# Encerra todos os módulos do Pygame e fecha
        # a janela do jogo.
pygame.quit()