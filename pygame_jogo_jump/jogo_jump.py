# Primeiro, importamos os módulos necessários para o jogo:
import pygame  # Pygame é uma biblioteca de jogos que permite criar jogos facilmente
import sys     # Sys é usado para interagir com o sistema, como sair do jogo
import random  # Random é usado para gerar números aleatórios, como a posição das plataformas
import pandas as pd  # Pandas é uma biblioteca de análise de dados, usada aqui para salvar a pontuação

# Definimos uma função para mostrar mensagens na tela
def mostrar_mensagem(tela, mensagem, tamanho, cor, posicao):
    
    # Cria uma fonte do sistema com um tamanho definido
    fonte = pygame.font.SysFont(None, tamanho)
    
    # Renderiza a mensagem em uma 'superfície' com a fonte definida, antialiasing ativado e a cor escolhida
    texto_superficie = fonte.render(mensagem, True, cor)
    
    # Coloca a superfície do texto na tela na posição especificada
    tela.blit(texto_superficie, posicao)
    

# Esta é a definição da função que salva a pontuação do jogo em um arquivo Excel.
def salvar_pontuacao(pontos):
    
    # O bloco 'try' tentará executar o código que pode gerar uma 
    # exceção específica que queremos tratar.
    try:
        
        # Aqui tentamos ler um arquivo Excel existente chamado 'pontuacao.xlsx'.
        # Se o arquivo existir, os dados são carregados em um DataFrame do pandas.
        df_existente = pd.read_excel('pontuacao.xlsx')
        
    # O bloco 'except' captura a exceção 'FileNotFoundError', que é 
    # lançada se o arquivo não existir.
    except FileNotFoundError:
        
        # Se o arquivo 'pontuacao.xlsx' não for encontrado, um novo DataFrame é criado.
        # Esse DataFrame possui apenas uma coluna chamada 'Pontos'.
        df_existente = pd.DataFrame(columns=['Pontos'])
    
    # Aqui criamos um novo DataFrame para a pontuação atual.
    # Esse DataFrame possui uma única linha com a pontuação atual e uma coluna chamada 'Pontos'.
    nova_entrada = pd.DataFrame([pontos], columns=['Pontos'])
    
    # O novo DataFrame 'nova_entrada' é concatenado com o 'df_existente'.
    # 'ignore_index=True' significa que o índice do DataFrame resultante será reiniciado para uma sequência padrão,
    # ou seja, 0, 1, 2, ..., sem considerar os índices dos DataFrames originais.
    df_atualizado = pd.concat([df_existente, nova_entrada], ignore_index=True)
    
    # Finalmente, o DataFrame atualizado 'df_atualizado' é salvo de volta ao arquivo 'pontuacao.xlsx'.
    # 'index=False' significa que os índices do DataFrame não serão escritos no arquivo Excel.
    # Portanto, o arquivo terá apenas os dados da coluna 'Pontos'.
    df_atualizado.to_excel('pontuacao.xlsx', index=False)
    

# Inicializa todos os módulos importados do pygame, é sempre
# necessário antes de começar a usar o pygame.
pygame.init()

# Define as dimensões da tela do jogo.
largura, altura = 800, 555

# Cria uma janela ou tela para o jogo com as dimensões definidas acima.
tela = pygame.display.set_mode((largura, altura))

# Define o título da janela do jogo.
pygame.display.set_caption("Jogo Jump")

# Define algumas cores que serão usadas no jogo, com base em valores RGB.
BRANCO = (255, 255, 255)  # cor branca
AZUL = (0, 0, 255)        # cor azul
PRETO = (0, 0, 0)         # cor preta

# Define a posição inicial do jogador como uma lista [x, y].
posicao_jogador = [400, 300]

# Define a altura de um pulo normal.
altura_pulo = -20

# Define a altura de um pulo mais alto.
altura_pulo_alto = -40

# Define a velocidade inicial do jogador como uma lista [velocidade_x, velocidade_y].
velocidade_jogador = [0, 0]

# Define a força da gravidade, que afetará o jogador (quanto 
# maior, mais rápido o jogador cairá após pular).
gravidade = 1.0

# Define a velocidade de pulo, que é a velocidade inicial dada ao jogador quando ele pula.
velocidade_pulo = 10

# Define o tempo máximo que o jogador pode manter um 
# pulo (a quantidade de frames durante os quais o pulo é efetivo).
tempo_pulo_max = 20

# Inicializa um contador para rastrear por quanto tempo o 
# botão de pulo está sendo pressionado.
tempo_pulo_atual = 0

# Uma variável para atribuir uma identificação única para cada plataforma no jogo. 
# Isso pode ser útil para rastrear plataformas individualmente, por exemplo, para 
# pontuação ou eventos de jogo.
plataforma_id = 0  

# Uma lista de tuplas onde cada tupla representa uma plataforma. Cada plataforma tem sua posição x e y, 
# largura e altura, seguida do ID único atribuído acima. Isso define as plataformas estáticas que o jogador 
# poderá utilizar para pular sobre ou para chegar a diferentes áreas do jogo.
# (posição x, posição y, largura, altura, id da plataforma)
plataformas = [
    (0, 550, largura, 50, plataforma_id),  # Plataforma base que ocupa a largura toda da tela
    (400, 450, 100, 20, 1),                # Plataforma localizada em (400, 450) com 100px de largura e 20px de altura
    (200, 350, 100, 20, 2),                # Plataforma localizada em (200, 350) com 100px de largura e 20px de altura
    (100, 250, 100, 20, 3)                 # Plataforma localizada em (100, 250) com 100px de largura e 20px de altura
]

# Essa variável pode ser usada para manter uma referência à última plataforma que o jogador estava em contato.
# Inicialmente é definida como None porque o jogador ainda não interagiu com nenhuma plataforma.
plataforma_anterior = None

# Um contador de pontos para o jogador que será incrementado durante o jogo.
# Pode ser utilizado para manter a pontuação do jogador, como por exemplo, cada vez que ele atinge uma nova plataforma.
pontos = 0

# Uma variável booleana para controlar se os pontos já foram contados ou não.
# Isso é útil para garantir que os pontos sejam contabilizados uma
# única vez para cada ação qualificável para pontuação.
pontos_contados = False

# Um objeto de relógio do pygame que pode ser usado para controlar o framerate do jogo.
# Ele é utilizado para garantir que o jogo seja atualizado de maneira consistente em diferentes sistemas.
relogio = pygame.time.Clock()


# Após iniciar o pygame e antes de entrar no loop do jogo, carregue e dimensione a imagem de fundo.
# Carrega a imagem do arquivo 'fundo_nuvem.jpg'. É necessário que o caminho do arquivo esteja correto.
imagem_fundo = pygame.image.load('fundo_nuvem.jpg')

# Redimensiona a imagem de fundo para cobrir toda a tela do jogo. 
# As variáveis 'largura' e 'altura' devem ter sido definidas 
# anteriormente e correspondem às dimensões da tela do jogo.
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

# Inicializa o módulo mixer do Pygame, que é necessário para carregar e reproduzir sons.
pygame.mixer.init()

# Carrega o som que será tocado quando a tecla de espaço for pressionada. 
# É necessário substituir 'som_espaco.mp3' pelo caminho correto do arquivo de som.
som_espaco = pygame.mixer.Sound('som_espaco.mp3')

# Define o volume do som da tecla de espaço para 50%. O volume pode
# variar de 0.0 (silencioso) a 1.0 (volume máximo).
som_espaco.set_volume(0.5)

# Carrega o som que será tocado quando a tecla de seta para cima for pressionada.
# Novamente, substitua 'som_seta_cima.mp3' pelo caminho correto do arquivo de som.
som_seta_cima = pygame.mixer.Sound('som_seta_cima.mp3')

# Ajusta o volume para 50%, assim como foi feito para o som da tecla de espaço.
som_seta_cima.set_volume(0.5)

# Carrega o som de encerramento do jogo. Certifique-se de que o caminho 'som_encerramento.mp3' esteja correto.
som_encerramento = pygame.mixer.Sound('som_encerramento.mp3')

# Ajuste o volume do som de encerramento conforme necessário. Aqui está definido como 50%.
som_encerramento.set_volume(0.5)

# Define uma variável booleana para manter o estado do loop do jogo. 
# Enquanto 'jogo_ativo' for True, o jogo continua rodando.
# Se for definido como False, o jogo encerra.
jogo_ativo = True


# Definição da função 'encerrar_jogo' que será chamada quando o jogo for terminar.
def encerrar_jogo():
    
    # A palavra-chave 'global' é usada para modificar a variável 'jogo_ativo', que é global.
    global jogo_ativo
    
    # Executa o som de encerramento que foi previamente carregado e ajustado.
    som_encerramento.play()
    
    # Chama a função 'mostrar_mensagem' definida anteriormente para mostrar a mensagem de jogo encerrado e a pontuação final.
    # A mensagem é exibida na tela na posição (200, 200), com tamanho de fonte 50 e cor preta.
    mostrar_mensagem(tela, "Jogo Encerrado! Pontuação: " + str(pontos), 50, PRETO, (200, 200))
    
    # Atualiza a tela para garantir que a mensagem de encerramento seja exibida.
    pygame.display.update()
    
    # Pausa o jogo por 2000 milissegundos (ou 2 segundos), permitindo que o 
    # som de encerramento seja ouvido.
    pygame.time.wait(2000)
    
    # Chama a função 'salvar_pontuacao', que salva a pontuação atual em um arquivo Excel.
    salvar_pontuacao(pontos)
    
    # Define a variável global 'jogo_ativo' como False, indicando que o loop do 
    # jogo deve ser encerrado.
    jogo_ativo = False
    
    


# Este loop 'while' continua executando enquanto a variável 'jogo_ativo' for verdadeira.
while jogo_ativo:
    
    # Desenha a imagem de fundo na tela. A função 'blit' do pygame é usada para desenhar a imagem na tela.
    # A imagem é desenhada na posição (0, 0), que é o canto superior esquerdo da tela.
    tela.blit(imagem_fundo, (0, 0))

    # O método 'tick' do objeto 'Clock' é chamado para limitar a velocidade do jogo a 60 quadros por segundo.
    # Isso ajuda a garantir que o jogo funcione com a mesma velocidade em diferentes máquinas.
    relogio.tick(60)
    
    # Verifica se a posição y do jogador é menor ou igual a um quarto da altura da tela.
    # Se verdadeiro, o código abaixo irá executar, criando um efeito de 'câmera seguindo o jogador' para cima.
    if posicao_jogador[1] <= altura // 4:
        
        # Incrementa o identificador da plataforma, usado para manter uma contagem única para cada plataforma.
        plataforma_id += 1
        
        # Gera uma nova plataforma com uma posição x aleatória, mas mantém a mesma altura relativa à última plataforma.
        # A largura é fixa em 100 pixels, e a altura é fixa em 20 pixels.
        nova_plataforma = random.randint(50, largura-100), plataformas[-1][1] - 100, 100, 20, plataforma_id
        
        # Adiciona a nova plataforma à lista de plataformas.
        plataformas.append(nova_plataforma)
        
        # Aumenta a posição y do jogador pelo valor absoluto da sua velocidade y.
        # Isso simula o jogador 'subindo' junto com as plataformas quando o jogador alcança 1/4 da tela.
        posicao_jogador[1] += abs(velocidade_jogador[1])


        # Este 'for' percorre todas as plataformas, que estão armazenadas na lista 'plataformas'.
        for i in range(len(plataformas)):
            
            # Atualiza cada plataforma na lista. Cada plataforma é uma tupla com as seguintes informações:
            # posição x, posição y, largura, altura e identificador.
            # Aqui, só a posição y é atualizada, ela é incrementada pela velocidade vertical absoluta do jogador.
            # Isso cria o efeito de todas as plataformas se movendo para baixo quando o jogador sobe.
            plataformas[i] = (plataformas[i][0], plataformas[i][1] + abs(velocidade_jogador[1]), plataformas[i][2], plataformas[i][3], plataformas[i][4])

    # Chama a função 'mostrar_mensagem' para desenhar os pontos atuais do jogador na tela.
    # A mensagem é composta pela string "Pontos: " seguida da conversão da variável 'pontos' para string.
    # O tamanho da fonte é definido como 36, a cor é preta e a posição da mensagem é no canto superior esquerdo (10, 10).
    mostrar_mensagem(tela, "Pontos: " + str(pontos), 36, PRETO, (10, 10))

    # Este 'for' percorre a lista de plataformas. A variável 'plat' é uma tupla representando uma única plataforma.
    for plat in plataformas:
        
        # A função 'draw.rect' do pygame é usada para desenhar cada plataforma na tela.
        # O primeiro argumento é a tela onde a plataforma será desenhada.
        # O segundo argumento é a cor da plataforma, que é definida como azul.
        # O terceiro argumento é um retângulo representando a plataforma, que é a própria tupla 'plat' sem o último elemento,
        # que é o identificador da plataforma e não é necessário para o desenho.
        pygame.draw.rect(tela, AZUL, plat[:-1])  # Ignorando o último elemento (ID)


    # Esta variável indica se o jogador está no chão ou não. Inicialmente é definida como False.
    no_chao = False
    
    # 'plataforma_atual' será usada para armazenar o identificador da
    # plataforma em que o jogador está atualmente.
    # Começa como None porque o jogador ainda não está em nenhuma plataforma.
    plataforma_atual = None

    # Inicia um loop que irá percorrer todas as plataformas existentes na lista 'plataformas'.
    for plat in plataformas:
        
        # Cria um retângulo representando o jogador com a função 'pygame.Rect'.
        # Este retângulo é definido pela posição x e y do jogador e um tamanho fixo de 50x50 pixels.
        # Em seguida, verifica se este retângulo está colidindo com algum retângulo que representa uma plataforma
        # (ignorando o último elemento de 'plat' que é o identificador da plataforma com 'plat[:-1]').
        if pygame.Rect(posicao_jogador[0], posicao_jogador[1], 50, 50).colliderect(plat[:-1]):
            
            # Se a verificação de colisão for verdadeira e a velocidade vertical do jogador for maior que 0
            # (ou seja, o jogador está se movendo para baixo), então o jogador "aterra" na plataforma.
            if velocidade_jogador[1] > 0:
                
                # Ajusta a posição y do jogador para que ele esteja em cima da plataforma.
                # Isso é feito subtraindo 50 da posição y da plataforma, que é a altura do retângulo do jogador,
                # fazendo com que ele fique visualmente em cima da plataforma.
                posicao_jogador[1] = plat[1] - 50
                
                # Atualiza a variável 'no_chao' para True, indicando que o jogador está no chão.
                no_chao = True
                
                # Atualiza 'plataforma_atual' com o identificador único da plataforma que está colidindo com o jogador.
                # Esse identificador está na quinta posição da tupla 'plat' (índice 4).
                plataforma_atual = plat[4]
                
                # Sai do loop forçadamente com 'break' porque não é necessário verificar colisões com outras plataformas
                # uma vez que o jogador já encontrou uma plataforma para "aterrar".
                break


    # Verifica se a variável 'plataforma_atual' tem um valor diferente de None,
    # o que indicaria que o jogador está atualmente em cima de uma plataforma.
    if plataforma_atual is not None:
        
        # Verifica se a plataforma atual é diferente da última plataforma em que o jogador estava.
        # Isso é importante para garantir que os pontos sejam contados apenas uma vez por plataforma.
        if plataforma_atual != plataforma_anterior:
            
            # A variável 'pontos_contados' é usada para verificar se os pontos já foram contados para essa plataforma.
            # Se não foram, o jogador recebe pontos.
            if not pontos_contados:
                
                # Aumenta a pontuação do jogador em 10 pontos.
                pontos += 10
                
                # A variável 'pontos_contados' é definida como True para indicar que os pontos para essa plataforma
                # já foram contados, evitando que sejam contados novamente se o jogador continuar na mesma plataforma.
                pontos_contados = True
                
            # A variável 'plataforma_anterior' é atualizada para corresponder à plataforma atual.
            # Isso é usado para detectar quando o jogador chega a uma nova plataforma.
            plataforma_anterior = plataforma_atual
            
        else:
            
            # Se a plataforma atual é a mesma que a anterior, não contamos os pontos novamente.
            # A variável 'pontos_contados' é resetada para False para permitir que pontos sejam contados
            # quando o jogador chegar a uma nova plataforma.
            pontos_contados = False


    # Verifica se a variável 'no_chao' é False, o que significaria que o jogador não está
    # atualmente tocando o chão (ou uma plataforma).
    if not no_chao:
        
        # Se o jogador não está no chão, a gravidade é aplicada, aumentando a velocidade vertical do jogador.
        # Isso simula a aceleração devido à gravidade enquanto o jogador está no ar.
        velocidade_jogador[1] += gravidade
        
    else:
        
        # Se o jogador está no chão, a velocidade vertical é redefinida para 0,
        # o que impede o jogador de continuar se movendo para baixo e simula o contato com o chão.
        velocidade_jogador[1] = 0
        
    
    # Inicia um loop para verificar os eventos que estão acontecendo no jogo.
    for evento in pygame.event.get():
        
        # Verifica se algum dos eventos é do tipo QUIT, que é acionado quando o 
        # usuário clica no botão de fechar a janela do jogo.
        if evento.type == pygame.QUIT:
            
            # Se o evento for do tipo QUIT, o Pygame é finalizado, efetivamente
            # fechando a aplicação do jogo.
            pygame.quit()
            
            # O comando 'sys.exit()' é chamado para garantir que o programa seja encerrado.
            # Sem isso, o programa Python pode continuar rodando em segundo plano mesmo depois de fechar a janela do jogo.
            sys.exit()

        # Este bloco de código é parte de um loop de eventos e lida 
        # especificamente com o pressionamento de teclas.
        if evento.type == pygame.KEYDOWN:
            
            # Verifica se a tecla pressionada é a barra de espaço (K_SPACE) e
            # se o jogador está no chão (no_chao).
            if evento.key == pygame.K_SPACE and no_chao:
                
                # Se ambas as condições forem verdadeiras, o som atribuído ao pulo é tocado. 
                # Esta é uma feedback auditivo para o usuário saber que um pulo foi iniciado.
                som_espaco.play()
                
                # A velocidade vertical do jogador é ajustada para um valor negativo, 
                # causando um movimento ascendente e iniciando o pulo.
                velocidade_jogador[1] = -velocidade_pulo
                
                # O contador de tempo de pulo é iniciado (ou reiniciado se já estava ativo), 
                # permitindo que o código acompanhe por quanto tempo a tecla de pulo foi pressionada.
                tempo_pulo_atual = 1
                
            # Verifica se a tecla pressionada é a seta para cima (K_UP) e se o jogador está no chão.
            if evento.key == pygame.K_UP and no_chao:
                
                # Se ambas as condições são verdadeiras, o som de um pulo mais forte é tocado.
                # Este é um feedback auditivo diferenciado para indicar um pulo mais alto.
                som_seta_cima.play()
                
                # A velocidade vertical do jogador é ajustada para um valor mais negativo que o normal, 
                # criando um pulo mais alto do que o provocado pela barra de espaço.
                velocidade_jogador[1] = -velocidade_pulo * 1.5
                
                # O contador de tempo de pulo é também iniciado aqui, 
                # da mesma forma que é para o pulo normal com a barra de espaço.
                tempo_pulo_atual = 1
                
                

    # A gravidade é uma força que atua constantemente sobre o jogador, 
    # puxando-o para baixo quando ele está no ar.
    # Este comando incrementa a velocidade vertical do jogador pela quantidade definida pela gravidade,
    # fazendo com que o jogador caia ou desacelere seu movimento ascendente durante um pulo.
    velocidade_jogador[1] += gravidade

    # Atualiza a posição vertical do jogador adicionando a velocidade vertical atual.
    # Se a velocidade vertical for positiva, o jogador desce; se for negativa, o jogador sobe.
    posicao_jogador[1] += velocidade_jogador[1]

    # Obtém o estado atual de todas as teclas. 
    # 'teclas' se torna uma lista onde cada elemento é um booleano indicando se uma tecla específica está sendo pressionada ou não.
    teclas = pygame.key.get_pressed()

    # Define uma velocidade horizontal que será usada para mover o jogador para a esquerda ou para a direita.
    # Este valor pode ser ajustado para tornar o movimento mais rápido ou mais lento.
    velocidade_horizontal = 10

    
    # A primeira condição verifica se a tecla de espaço está sendo pressionada.
    if teclas[pygame.K_SPACE]:
        
        # A segunda condição verifica se o contador do tempo de pulo está dentro do
        # intervalo permitido para o pulo continuar.
        # Isso permite um pulo mais longo se a tecla de espaço for mantida pressionada.
        if tempo_pulo_atual > 0 and tempo_pulo_atual < tempo_pulo_max:
            
            # Se ainda está no intervalo permitido, a velocidade vertical é definida para a velocidade de pulo negativa.
            # Isto faz com que o personagem continue se movendo para cima na tela, contrariando a gravidade.
            velocidade_jogador[1] = -velocidade_pulo
            
            # O contador de tempo do pulo é incrementado, o que controla por quanto tempo o pulo continuará.
            tempo_pulo_atual += 1
            
    else:
        
        # Se a tecla de espaço não está sendo pressionada, o contador de tempo do pulo é resetado.
        # Isso garante que o pulo só ocorra enquanto o jogador estiver pressionando a tecla.
        tempo_pulo_atual = 0


    # Este código verifica se a tecla de seta para esquerda está pressionada.
    if teclas[pygame.K_LEFT]:
        
        # Se a tecla de seta para esquerda está pressionada, o jogador se move para a esquerda.
        # A posição horizontal do jogador é decrementada pela velocidade horizontal estabelecida,
        # o que faz com que o jogador se mova para a esquerda na tela.
        posicao_jogador[0] -= velocidade_horizontal

    # Este código verifica se a tecla de seta para direita está pressionada.
    if teclas[pygame.K_RIGHT]:
        
        # Se a tecla de seta para direita está pressionada, o jogador se move para a direita.
        # A posição horizontal do jogador é incrementada pela velocidade horizontal estabelecida,
        # o que faz com que o jogador se mova para a direita na tela.
        posicao_jogador[0] += velocidade_horizontal

    # Este código verifica se a tecla de espaço está pressionada e se o jogador está no chão.
    if teclas[pygame.K_SPACE] and no_chao:
        
        # Se a tecla de espaço está pressionada e o jogador está no chão, inicia-se um pulo.
        # A velocidade vertical do jogador é ajustada pela altura do pulo estabelecida (um valor negativo),
        # o que faz com que o jogador se mova para cima na tela, simulando um pulo.
        velocidade_jogador[1] += altura_pulo

    # Este código verifica se a tecla de seta para cima está pressionada e se o jogador está no chão.
    if teclas[pygame.K_UP] and no_chao:
        
        # Se a tecla de seta para cima está pressionada e o jogador está no chão, inicia-se um pulo mais alto.
        # A velocidade vertical do jogador é ajustada pela altura do pulo alto estabelecida (um valor negativo maior),
        # o que faz com que o jogador se mova mais para cima na tela, simulando um pulo mais alto.
        velocidade_jogador[1] += altura_pulo_alto

       
    # Esta condição verifica se a posição vertical do jogador é maior que a altura da tela.
    if posicao_jogador[1] > altura:
        
        print("Posição:", posicao_jogador[1])
        print("Altura:", altura)
        
        # Se a posição do jogador for maior que a altura da tela, significa que ele caiu para fora da tela.
        # Neste caso, a função encerrar_jogo() é chamada para finalizar o jogo.
        # A função encerrar_jogo irá tratar da lógica de encerramento, como tocar o som de game over,
        # exibir a pontuação final, salvar a pontuação se necessário, e atualizar a tela para refletir estas mudanças.
        encerrar_jogo()
        
    # Aqui, a imagem do personagem (um sapo neste exemplo) é carregada.
    # O caminho 'sapo.png' deve ser substituído pelo caminho correto onde a imagem está localizada no seu projeto.
    imagem_personagem = pygame.image.load('sapo.png')

    # A imagem do personagem é redimensionada para se adequar ao tamanho desejado na tela.
    # Neste caso, ela é dimensionada para um retângulo de 50 pixels de largura por 50 pixels de altura.
    imagem_personagem = pygame.transform.scale(imagem_personagem, (50, 50))

    # A imagem redimensionada do personagem é desenhada na tela na posição especificada pela tupla
    # (posicao_jogador[0], posicao_jogador[1]), que representa a posição atual do personagem no jogo.
    # O método blit é utilizado para desenhar a imagem sobre a superfície da tela.
    tela.blit(imagem_personagem, (posicao_jogador[0], posicao_jogador[1]))

    
    # Atualize a tela e outros elementos necessários
    pygame.display.update()
    relogio.tick(200)  # Mantém o jogo rodando a uma taxa de 60 quadros por segundo


    
    
# Pare qualquer música ou som em execução
pygame.mixer.music.stop()

# Termina o Pygame
pygame.quit()

# Por fim, a função `sys.exit()` é invocada para sair do programa.
# Embora `pygame.quit()` termine todos os módulos do Pygame, o Python ainda estará rodando.
# Portanto, `sys.exit()` informa ao Python para parar a execução do script atual.
sys.exit()