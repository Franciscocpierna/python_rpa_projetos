# Importa o módulo 'pygame' para a criação e gerenciamento de jogos.
import pygame

# Importa o módulo 'sys' para acessar funções específicas 
        # do sistema, como saída do programa.
import sys

# Importa o módulo 'random' para gerar números aleatórios, 
        # útil para dinâmicas de jogo.
import random

# Importa o módulo 'os' para interagir com funcionalidades 
        # dependentes do sistema operacional, como manipulação de arquivos.
import os

# Chama a função 'init' do pygame para inicializar todos os 
        # módulos necessários para o Pygame funcionar.
pygame.init()

# Define a largura da tela do jogo como 400 pixels.
LARGURA_TELA = 400

# Define a altura da tela do jogo como 600 pixels.
ALTURA_TELA = 600

# Cria uma tela ou janela para o jogo com as dimensões definidas
        # pelas variáveis LARGURA_TELA e ALTURA_TELA.
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Define o título da janela do jogo.
pygame.display.set_caption("Solte o Objeto na Lixeira")

# Define a cor AZUL usando uma tupla com valores RGB (Red, Green, Blue).
AZUL = (0, 0, 255)

# Define a cor LARANJA usando uma tupla com valores RGB.
LARANJA = (255, 140, 0)

# Define a cor BRANCO usando uma tupla com valores RGB para branco puro.
BRANCO = (255, 255, 255)

# Cria uma fonte de texto para a pontuação usando a fonte
        # padrão do sistema e definindo o tamanho como 40.
fonte = pygame.font.SysFont(None, 40)

# Carrega uma imagem do disco que representa uma mão
        # segurando um objeto, usando o caminho 'mao.png'.
imagem_mao = pygame.image.load("mao.png")

# Carrega uma imagem de um objeto que será usado no jogo,
        # identificado por 'nuvem.png'.
imagem_objeto = pygame.image.load("nuvem.png")

# Carrega uma imagem da lixeira para o jogo usando o arquivo 'lixeira.png'.
imagem_cesta = pygame.image.load("lixeira.png")

# Redimensiona a imagem da mão para uma largura e altura
        # de 80 pixels para adequação ao design do jogo.
imagem_mao = pygame.transform.scale(imagem_mao, (80, 80))

# Redimensiona a imagem do objeto para 40x40 pixels para garantir 
        # que se ajuste visualmente no contexto do jogo.
imagem_objeto = pygame.transform.scale(imagem_objeto, (40, 40))

# Redimensiona a imagem da lixeira para 60x60 pixels para ser
        # visualmente coerente com outros elementos gráficos.
imagem_cesta = pygame.transform.scale(imagem_cesta, (60, 60))

# Define um nome de arquivo para armazenar os dados de
        # pontuação acumulada.
ARQUIVO_PONTUACAO = "pontuacao_acumulada.txt"


# Define uma função chamada 'carregar_pontuacao_acumulada' para 
        # ler a pontuação do arquivo e retornar o valor.
def carregar_pontuacao_acumulada():
    
    # Verifica se o arquivo de pontuação especificado 
            # em 'ARQUIVO_PONTUACAO' existe no diretório atual.
    if os.path.exists(ARQUIVO_PONTUACAO):
        
        # Abre o arquivo de pontuação em modo de leitura ('r').
        with open(ARQUIVO_PONTUACAO, "r") as arquivo:
            
            # Tenta executar o código dentro do bloco 'try'.
            try:
                
                # Lê o conteúdo do arquivo, remove espaços em 
                        # branco extras com 'strip()' e converte para inteiro.
                return int(arquivo.read().strip())
                
            # Captura a exceção 'ValueError' que ocorre se a conversão
                    # para inteiro falhar (e.g., arquivo vazio ou dados inválidos).
            except ValueError:
                
                # Retorna 0 se a conversão para inteiro falhar, indicando 
                        # que não há pontuação válida salva.
                return 0
                
    # Retorna 0 se o arquivo não existir, indicando que
            # não há pontuações anteriores.
    return 0


# Define a função 'salvar_pontuacao_acumulada' que 
        # aceita um argumento 'pontos'.
def salvar_pontuacao_acumulada(pontos):
    
    # Chama a função 'carregar_pontuacao_acumulada' para obter a 
            # pontuação atual do arquivo e adiciona os novos pontos.
    pontuacao_acumulada = carregar_pontuacao_acumulada() + pontos
    
    # Abre o arquivo especificado por 'ARQUIVO_PONTUACAO' no modo de 
            # escrita ('w') para salvar a pontuação acumulada.
    with open(ARQUIVO_PONTUACAO, "w") as arquivo:
    
        # Converte a 'pontuacao_acumulada' em string e escreve no arquivo.
        arquivo.write(str(pontuacao_acumulada))

# Define a função 'exibir_pontuacao' que recebe 'pontos' como parâmetro.
def exibir_pontuacao(pontos):
    
    # Renderiza o texto de pontuação usando a 'fonte' definida, 
            # habilitando antialiasing (True) e usando a cor LARANJA.
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, LARANJA)
    
    # Desenha o texto renderizado na tela na posição (10, 10).
    tela.blit(texto_pontos, (10, 10))


# Define a função 'mostrar_menu' para exibir o menu inicial do jogo.
def mostrar_menu():
    
    # Carrega a pontuação acumulada do arquivo utilizando 
            # uma função definida anteriormente.
    pontuacao_acumulada = carregar_pontuacao_acumulada()
    
    # Preenche a tela inteira com a cor AZUL definida anteriormente.
    tela.fill(AZUL)
    
    # Renderiza o título do jogo usando a fonte e cor 
            # especificadas, com antialiasing ativado (True).
    titulo = fonte.render("Solte o Objeto na Lixeira", True, LARANJA)
    
    # Posiciona o título no centro horizontal da tela e um
            # quarto da altura total da tela para baixo.
    tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, ALTURA_TELA // 4))
    
    # Renderiza o texto que exibe a pontuação acumulada, 
            # usando BRANCO como cor do texto.
    texto_acumulado = fonte.render(f"Pontuação Acumulada: {pontuacao_acumulada}", True, BRANCO)
    
    # Posiciona o texto da pontuação acumulada no centro
            # horizontal e na metade da altura da tela.
    tela.blit(texto_acumulado, (LARGURA_TELA // 2 - texto_acumulado.get_width() // 2, ALTURA_TELA // 2))

    # Renderiza instruções para iniciar o jogo, também com 
            # antialiasing e na cor BRANCO.
    instrucao = fonte.render("Clique para começar", True, BRANCO)
    
    # Posiciona as instruções no centro horizontal e a três 
            # quartos da altura total da tela para baixo.
    tela.blit(instrucao, (LARGURA_TELA // 2 - instrucao.get_width() // 2, ALTURA_TELA // 1.5))
    
    # Atualiza a tela inteira para mostrar todos os 
            # elementos gráficos renderizados.
    pygame.display.flip()

    # Inicializa uma variável booleana para controlar a
            # espera pelo início do jogo.
    esperando = True
    
    # Entra em um loop que continua enquanto 'esperando' for verdadeiro.
    while esperando:
        
        # Processa cada evento na fila de eventos do Pygame.
        for evento in pygame.event.get():
            
            # Verifica se o evento é de saída do jogo, ou seja, se o
                    # usuário clicou no botão de fechar a janela.
            if evento.type == pygame.QUIT:
                
                # Finaliza todos os módulos do Pygame e fecha o jogo.
                pygame.quit()
                
                # Sai do programa, encerrando completamente.
                sys.exit()
                
            # Verifica se houve um clique do mouse.
            if evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Encerra o loop, permitindo que o jogo prossiga além do menu.
                esperando = False


# Define a função principal 'jogo' que controla a lógica e o estado do jogo.
def jogo():
    
    # Inicializa a posição horizontal da mão no começo da tela.
    pos_x_mao = 0
    
    # Define a posição vertical da mão fixada em 100 pixels do topo.
    pos_y_mao = 100
    
    # Define a velocidade horizontal da mão como 2 pixels por
            # atualização de frame.
    velocidade_mao = 2
    
    # Define um estado booleano para controlar se o objeto foi 
            # solto pela mão ou não.
    objeto_solto = False
    
    # Define a posição inicial horizontal do objeto como 
            # sendo 20 pixels à direita da posição da mão.
    pos_x_objeto = pos_x_mao + 20
    
    # Define a posição inicial vertical do objeto como sendo 50 
            # pixels abaixo da posição da mão.
    pos_y_objeto = pos_y_mao + 50
    
    # Define a velocidade de queda do objeto como 5 pixels 
            # por atualização de frame.
    velocidade_objeto = 5
    
    # Inicializa o contador de pontos do jogo como zero.
    pontos = 0

    # Define a posição horizontal da cesta, centralizando-a na tela.
    pos_x_cesta = LARGURA_TELA // 2 - imagem_cesta.get_width() // 2
    
    # Define a posição vertical da cesta colocando-a 10 
            # pixels acima do fundo da tela.
    pos_y_cesta = ALTURA_TELA - imagem_cesta.get_height() - 10

    # Inicializa a variável de controle do loop principal 
            # do jogo como verdadeira.
    rodando = True

    # Continua o loop enquanto a variável 'rodando' for verdadeira.
    while rodando:
        
        # Preenche toda a tela com a cor BRANCO antes de desenhar
                # outros elementos, definindo o fundo do jogo.
        tela.fill(BRANCO)
    
        # Processa cada evento na fila de eventos do Pygame para
                # reagir às ações do usuário.
        for evento in pygame.event.get():
        
            # Verifica se o tipo do evento é QUIT, que indica que o 
                    # usuário fechou a janela do jogo.
            if evento.type == pygame.QUIT:
            
                # Encerra todos os módulos do Pygame, liberando recursos.
                pygame.quit()
                
                # Sai do script completamente, encerrando o programa.
                sys.exit()
            
            # Verifica se o tipo do evento é um clique do mouse.
            if evento.type == pygame.MOUSEBUTTONDOWN:
            
                # Checa se o objeto ainda não foi solto e se o clique
                        # ocorreu sobre a região da mão.
                if not objeto_solto and mao_rect.collidepoint(evento.pos):
                
                    # Marca o objeto como solto, permitindo que ele comece a 
                            # se mover livremente na tela.
                    objeto_solto = True
                    
                    # Ajusta a posição inicial do objeto para ser alinhada 
                            # com a mão no momento do clique.
                    pos_x_objeto = pos_x_mao + 20
 

        # Movimento da mão
        # Verifica se o objeto ainda não foi solto.
        if not objeto_solto:
        
            # Move a mão horizontalmente adicionando a velocidade da 
                    # mão à sua posição atual.
            pos_x_mao += velocidade_mao
            
            # Checa se a mão alcançou o limite da tela, seja no lado 
                    # esquerdo (pos_x_mao < 0) ou no lado direito 
            if pos_x_mao > LARGURA_TELA - imagem_mao.get_width() or pos_x_mao < 0:
            
                # Inverte a direção do movimento da mão ao multiplicar a
                        # velocidade por -1.
                velocidade_mao *= -1  

            # Mantém o objeto alinhado horizontalmente com a mão, 
                    # adicionando 20 pixels à posição x da mão.
            pos_x_objeto = pos_x_mao + 20
            
            # Mantém o objeto alinhado verticalmente com a mão, 
                    # adicionando 50 pixels à posição y da mão.
            pos_y_objeto = pos_y_mao + 50


        # Movimento do objeto solto
        if objeto_solto:
            
            # Incrementa a posição vertical do objeto pela sua
                    # velocidade, fazendo-o cair.
            pos_y_objeto += velocidade_objeto
        
            # Verifica se o objeto caiu na cesta considerando se algum ponto 
                    # do objeto está dentro da largura da cesta.
            if (pos_y_objeto + imagem_objeto.get_height() >= pos_y_cesta and
                pos_x_cesta <= pos_x_objeto + imagem_objeto.get_width() and pos_x_objeto <= pos_x_cesta + imagem_cesta.get_width()):
                
                pontos += 1  # Atribui ponto ao jogador
                velocidade_mao += 0.5  # Aumenta a velocidade da mão a cada ponto ganho
                velocidade_objeto += 0.5  # Aumenta a velocidade de queda do objeto
                objeto_solto = False  # Marca o objeto como não solto, resetando para a posição inicial
                pos_y_objeto = pos_y_mao + 50  # Reseta a posição vertical do objeto
                pos_x_mao = 0.5  # Reposiciona a mão no início
                pos_x_cesta = random.randint(0, LARGURA_TELA - imagem_cesta.get_width())  # Muda a posição da cesta


            # Condicional que verifica se o objeto caiu para 
                    # fora da tela sem acertar a cesta.
            elif pos_y_objeto > ALTURA_TELA:
                
                # Encerra o loop do jogo, indicando o fim de jogo por
                        # falha ao acertar a cesta.
                rodando = False


        # Desenha os elementos na tela
        # Armazena o retângulo que contém a imagem da mão na 
                # variável 'mao_rect' para possibilitar detecção de colisões.
        mao_rect = tela.blit(imagem_mao, (pos_x_mao, pos_y_mao))
        
        # Desenha a imagem do objeto na posição atualizada na tela.
        tela.blit(imagem_objeto, (pos_x_objeto, pos_y_objeto))
        
        # Desenha a imagem da cesta na posição definida na tela.
        tela.blit(imagem_cesta, (pos_x_cesta, pos_y_cesta))

        # Chama a função 'exibir_pontuacao' para mostrar a 
                # pontuação atual do jogador na tela.
        exibir_pontuacao(pontos)

        # Atualiza a tela inteira para refletir todas as mudanças 
                # visuais feitas nos passos anteriores.
        pygame.display.flip()
        
        # Controla a taxa de atualização do jogo, limitando-a a 30 quadros
                # por segundo para manter a jogabilidade consistente.
        pygame.time.Clock().tick(30)

    # Quando o loop termina (jogo termina), chama a função para 
            # salvar a pontuação acumulada no arquivo.
    salvar_pontuacao_acumulada(pontos)
    
    # Chama a função 'fim_jogo' para exibir a mensagem de fim de
            # jogo e oferecer a opção para reiniciar.
    fim_jogo(pontos)


# Define a função 'fim_jogo' que aceita a pontuação final como 
        # argumento para exibir na tela de fim de jogo.
def fim_jogo(pontos):
    
    # Preenche toda a tela com a cor BRANCO para iniciar a 
            # tela de fim de jogo.
    tela.fill(BRANCO)
    
    # Renderiza a mensagem "Fim de Jogo!" usando a fonte definida 
            # anteriormente, com antialiasing ativado (True) e na cor LARANJA.
    mensagem_fim = fonte.render("Fim de Jogo!", True, LARANJA)
    
    # Desenha a mensagem "Fim de Jogo!" no centro horizontal da tela e 
            # um terço do caminho para baixo da altura total.
    tela.blit(mensagem_fim, (LARGURA_TELA // 2 - mensagem_fim.get_width() // 2, ALTURA_TELA // 3))
    
    # Renderiza a mensagem que exibe a pontuação final do 
            # jogador, usando a cor BRANCO.
    pontuacao_final = fonte.render(f"Pontuação: {pontos}", True, BRANCO)
    
    # Desenha a pontuação final no centro horizontal da tela e a
            # metade do caminho para baixo da altura total.
    tela.blit(pontuacao_final, (LARGURA_TELA // 2 - pontuacao_final.get_width() // 2, ALTURA_TELA // 2))
    
    # Renderiza instruções para reiniciar o jogo, também em BRANCO.
    instrucao_reiniciar = fonte.render("Clique para jogar novamente", True, BRANCO)
    
    # Desenha as instruções no centro horizontal da tela e três 
            # quartos do caminho para baixo da altura total.
    tela.blit(instrucao_reiniciar, (LARGURA_TELA // 2 - instrucao_reiniciar.get_width() // 2, ALTURA_TELA // 1.5))
    
    # Atualiza a tela inteira para mostrar todas as 
            # mensagens renderizadas.
    pygame.display.flip()


    # Espera o jogador clicar para reiniciar
    # Inicializa uma variável booleana 'esperando' como True
            # para começar a espera por uma ação do usuário.
    esperando = True
    
    # Entra em um loop enquanto 'esperando' for verdadeiro. 
            # Este loop aguarda ações do usuário.
    while esperando:
        
        # Itera sobre cada evento na fila de eventos do Pygame.
        for evento in pygame.event.get():
        
            # Verifica se o tipo do evento é QUIT, que ocorre quando o
                    # usuário clica no botão de fechar a janela do jogo.
            if evento.type == pygame.QUIT:
            
                # Encerra todos os módulos do Pygame para limpar os
                        # recursos antes de fechar.
                pygame.quit()
                
                # Sai do programa, terminando a execução completamente.
                sys.exit()
                
            # Verifica se houve um clique do mouse.
            if evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Interrompe o loop 'esperando', mudando a variável para False,
                        # uma vez que o usuário clicou para continuar.
                esperando = False
                
                # Chama a função 'jogo' para reiniciar o jogo, 
                        # começando um novo ciclo de jogo.
                jogo()


# Executa o menu e inicia o jogo
mostrar_menu()
jogo()