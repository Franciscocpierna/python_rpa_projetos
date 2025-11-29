# Importa a biblioteca Pygame, usada para desenvolvimento
        # de jogos e interfaces gráficas
import pygame

# Importa a biblioteca random para a geração de números aleatórios
import random

# Importa a biblioteca sys para funções relacionadas ao 
        # sistema, como saída do programa
import sys

# Chama a função init() do módulo pygame, que inicializa
        # todos os módulos incluídos na biblioteca Pygame
pygame.init()

# Definição de cores no formato RGB
BRANCO = (255, 255, 255)  # Define a cor branca
PRETO = (0, 0, 0)         # Define a cor preta
VERMELHO = (255, 0, 0)    # Define a cor vermelha
VERDE = (0, 255, 0)       # Define a cor verde

# Definição das dimensões da tela de jogo
LARGURA = 800  # Define a largura da tela como 800 pixels
ALTURA = 600   # Define a altura da tela como 600 pixels

# Cria uma janela para o jogo com as dimensões especificadas
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela do jogo
pygame.display.set_caption("Jogo de Copos")

# Inicializa variáveis para o controle do jogo
pontuacao = 0               # Inicia a pontuação do jogo como 0
velocidade = 5              # Define a velocidade inicial como 5 pixels por frame
rodada = 1                  # Inicia o jogo na rodada 1

# Configuração de fonte para textos que serão exibidos no jogo
fonte = pygame.font.SysFont(None, 36)  # Cria uma fonte com tamanho 36


# Bloco try-except para carregar imagens dos copos e bola; 
        # encerra o programa se houver erro de carregamento
try:
    
    # Carrega a imagem do copo de frente, permite transparência com convert_alpha()
    copo_frente_original = pygame.image.load('copo_frente.png').convert_alpha()
    
    # Carrega a imagem do copo de trás, permite transparência com convert_alpha()
    copo_tras_original = pygame.image.load('copo_tras.png').convert_alpha()
    
    # Carrega a imagem da bola, permite transparência com convert_alpha()
    bola_imagem_original = pygame.image.load('bola.png').convert_alpha()

# Captura qualquer erro de carregamento de imagens
except pygame.error as e:
    
    # Imprime o erro de carregamento
    print(f"Erro ao carregar imagens: {e}")
    
    # Encerra todos os módulos do Pygame
    pygame.quit()
    
    # Encerra o programa
    sys.exit()

# Define as dimensões originais das imagens dos copos
copo_largura_original = 150  # Largura original do copo
copo_altura_original = 200   # Altura original do copo

# Redimensionamento das imagens para as dimensões 
        # originais especificadas
# Redimensiona a imagem do copo de frente para as 
        # dimensões originais
copo_frente_original = pygame.transform.scale(copo_frente_original, (copo_largura_original, copo_altura_original))

# Redimensiona a imagem do copo de trás para as dimensões originais
copo_tras_original = pygame.transform.scale(copo_tras_original, (copo_largura_original, copo_altura_original))

# Redimensiona a imagem da bola para 50x50 pixels
bola_imagem_original = pygame.transform.scale(bola_imagem_original, (50, 50))

# Define o tamanho mínimo aceitável para as imagens dos copos
MIN_CUPO_LARGURA = 50  # Largura mínima do copo
MIN_CUPO_ALTURA = 70   # Altura mínima do copo


# Define a função para desenhar os copos e a bola na tela do jogo
def desenhar_copos(copos, mostrando_bola=False, posicao_bola=0, estados_copos=None):
    
    # Preenche a tela inteira com a cor branca para limpar a tela anterior
    tela.fill(BRANCO)

    # Itera sobre a lista de copos para desenhar cada um deles
    for i in range(len(copos)):
        
        # Extrai as coordenadas x e y do copo atual na lista de copos
        x, y = copos[i]
        
        # Verifica se o estado do copo é 'frente' para decidir qual imagem usar
        if estados_copos and estados_copos[i] == 'frente':
            
            # Desenha o copo com a imagem de frente na posição (x, y) na tela
            tela.blit(copo_frente_resized, (x, y))
        else:
            
            # Desenha o copo com a imagem de trás na posição (x, y) 
                    # na tela se não estiver de frente
            tela.blit(copo_tras_resized, (x, y))

    # Verifica se a bola deve ser mostrada de acordo com a 
            # variável mostrando_bola
    # A variável mostrando_bola é um booleano que controla a
            # visibilidade da bola no jogo,
            # sendo True quando a bola deve ser exibida e False quando não deve.
    if mostrando_bola:
        
        # Atribui as coordenadas do copo selecionado (onde a bola está
                # escondida) às variáveis x_bola e y_bola.
        # posicao_bola é um índice que aponta para a posição atual da bola
                # nos copos, indicando em qual copo a bola está escondida.
        x_bola, y_bola = copos[posicao_bola]
        
        # A função blit desenha a bola na tela. O primeiro parâmetro é a imagem da bola,
        # e o segundo parâmetro é um tuple que define a posição (x, y) na 
                # tela onde a bola será desenhada.
        # A bola é centralizada horizontalmente dentro do
                # copo (x_bola + copo_largura//2 - bola_imagem_resized.get_width()//2)
                # e posicionada ligeiramente acima da base do 
                # copo (y_bola + copo_altura - bola_imagem_resized.get_height() - 10).
        tela.blit(bola_imagem_resized, (x_bola + copo_largura//2 - bola_imagem_resized.get_width()//2, y_bola + copo_altura - bola_imagem_resized.get_height() - 10))
    
    # Renderiza o texto da pontuação utilizando a fonte previamente definida.
    # O método render da classe font cria uma superfície com o 
            # texto desejado. Os parâmetros são:
    # 1. O texto a ser renderizado.
    # 2. Um booleano que ativa ou desativa a suavização das
            # bordas do texto (True para suavizado).
    # 3. A cor do texto, no caso, PRETO.
    texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, PRETO)

    # Desenha a superfície do texto da pontuação na tela. 
    # O primeiro parâmetro é a superfície do texto,
    # e o segundo é a posição (x, y) onde o texto será colocado.
    # Aqui, coloca-se o texto na posição (10, 10) da tela.
    tela.blit(texto_pontuacao, (10, 10))
    
    # Renderiza o texto que mostra a rodada atual, usando o 
            # mesmo processo do texto de pontuação.
    texto_rodada = fonte.render(f"Rodada: {rodada}", True, PRETO)

    # A superfície do texto da rodada é desenhada na tela com um 
            # alinhamento à direita. Para isso, calculamos a posição x
    # subtraindo a largura do texto (texto_rodada.get_width()) de
            # LARGURA (largura total da tela) e subtraindo 10 pixels
            # adicionais para margem.
    # A posição y é fixada em 10 pixels do topo, o que mantém o 
            # texto da rodada alinhado horizontalmente com o texto da pontuação.
    tela.blit(texto_rodada, (LARGURA - texto_rodada.get_width() - 10, 10))


    # Atualiza a tela para mostrar os novos desenhos
    pygame.display.update()


# Define uma função para calcular as posições
        # iniciais dos copos na tela
def gerar_posicoes_iniciais(numero_copos, copo_largura):

    # Cria uma lista vazia para armazenar as posições dos copos
    posicoes = []  

    # Define o espaço de 50 pixels nas bordas laterais da tela
    espaco = 50  

    # Calcula o espaço total disponível para os copos subtraindo o 
            # espaço das bordas da largura total da tela
    espaco_total = LARGURA - 2 * espaco

    # Calcula a largura total ocupada pelos copos multiplicando o
            # número de copos pela largura de um copo
    largura_total_copos = numero_copos * copo_largura

    # Condicional para calcular o espaço entre os copos, se 
            # houver mais de um copo
    if numero_copos > 1:
        
        # Calcula o espaço entre os copos dividindo o espaço 
                # restante pelo número de copos menos um
        espaco_entre_copos = (espaco_total - largura_total_copos) / (numero_copos - 1)
        
        # Se o espaço calculado entre os copos for negativo, 
                # define-o como zero
        if espaco_entre_copos < 0:
            espaco_entre_copos = 0
            
    else:
        
        # Se houver apenas um copo, não há necessidade de espaço entre eles
        espaco_entre_copos = 0

    # Define a posição x inicial do primeiro copo, que é a 
            # distância da borda esquerda
    x = espaco
    
    # Define a posição y para todos os copos, centralizando-os 
            # verticalmente na tela
    y = ALTURA // 2 - copo_largura // 2  # Usa a divisão inteira 
                                         # para centralizar os copos verticalmente

    # Loop para calcular a posição de cada copo
    for i in range(numero_copos):
        
        # Adiciona a posição (x, y) atual ao final da lista de posições
        posicoes.append((x, y))
        
        # Atualiza a posição x para o próximo copo, adicionando a 
                # largura de um copo e o espaço entre eles
        x += copo_largura + espaco_entre_copos

    # Retorna a lista de posições calculadas para os copos
    return posicoes

    

# Define a função para animar o giro de um copo específico, tornando o 
            # efeito visual de um copo girando para mostrar a frente ou o verso.
def animar_girar_copo(copos, idx, velocidade, girar_para='frente'):
    
    # Obtém as coordenadas x e y do copo que será animado.
    x, y = copos[idx]

    # Inicia um loop que simula a animação de girar o copo, 
            # onde 'escala' controla o grau de rotação.
    for escala in range(0, 21):
        
        # Processa eventos do Pygame para manter a aplicação responsiva, 
                # permitindo, por exemplo, fechar a janela durante a animação.
        for evento in pygame.event.get():

            # Se o usuário tentar fechar a janela do jogo
            if evento.type == pygame.QUIT: 

                # Encerra todos os módulos do Pygame
                pygame.quit()              

                # Sai do script completamente
                sys.exit()                 

        # Preenche toda a tela com branco para limpar o quadro anterior.
        # Isso é necessário para evitar rastros dos movimentos
                # anteriores dos gráficos na animação.
        tela.fill(BRANCO)

        # Desenha todos os outros copos que não estão sendo animados.
        # Este passo mantém os outros elementos estáticos enquanto 
                # apenas o copo especificado gira.
        for i in range(len(copos)):
            
            # Verifica se o índice do copo atual não é o que está sendo animado.
            if i != idx:
                
                # Desenha o copo com a imagem de trás em suas 
                        # respectivas coordenadas,
                # garantindo que todos os outros copos permaneçam
                        # visíveis e estáticos.
                tela.blit(copo_tras_resized, copos[i])
        
            
        # Calcula um fator de escala que é usado para simular a 
                # rotação horizontal do copo.
        # 'escala' varia de 0 a 20, onde 10 é o ponto médio da animação. 
        # A função abs(escala - 10) / 10 cria uma variação de escala 
                # que diminui até 0 no ponto médio (escala = 10) e
                # depois aumenta novamente,
                # simulando o copo girando para frente e para trás.
        fator_escala = 1 - abs(escala - 10)/10
    
        # Usa o fator de escala para ajustar dinamicamente a largura do
                # copo durante a animação, criando um efeito de rotação visual.
        # A imagem do copo é redimensionada de acordo com o fator de escala
                # calculado, alterando sua largura mas mantendo a altura original.
        copo_escalado = pygame.transform.scale(
            copo_frente_resized if girar_para == 'frente' else copo_tras_resized,
            (int(copo_largura * fator_escala), int(copo_altura))
        )
    
        # Calcula a posição x correta para centralizar o copo
                # escalado horizontalmente.
        # Isso é necessário porque ao alterar a largura da imagem, seu
                # ponto de ancoragem (canto superior esquerdo) poderia
                # deslocá-lo visualmente.
        pos_x = x + (copo_largura - copo_escalado.get_width()) // 2
    
        # Desenha o copo escalado na tela na posição calculada. 
        # Isso efetivamente mostra o copo 'girando' pela alteração de sua largura.
        tela.blit(copo_escalado, (pos_x, y))
    
        # Se a animação estiver configurada para mostrar a frente do
                # copo e já tiver passado do ponto médio da animação (escala >= 10),
        # essa condição se torna verdadeira. O ponto médio (escala = 10) é 
                # quando o copo está no momento de maior 'compressão' visual,
                # o que simula o copo sendo visto de lado no ponto
                # mais estreito da rotação.
        if girar_para == 'frente' and escala >= 10:
            
            # A função blit é usada para desenhar a bola sobre o copo.
            # Aqui, a bola é posicionada de modo que
                    # pareça estar escondida sob o copo que está 
                    # sendo girado para a frente.
            # O cálculo da posição x da bola é feito para centralizá-la no copo:
                    # x + copo_largura//2 ajusta para o centro do copo,
                    # subtraindo metade da largura da bola com bola_imagem_resized.get_width()//2 
                    # para centralizar a bola exatamente no meio do copo.
            # A posição y é ajustada para que a bola apareça logo 
                    # acima da base do copo, criando a ilusão de que 
                    # está dentro ou sob o copo.
            tela.blit(bola_imagem_resized, (
                x + copo_largura//2 - bola_imagem_resized.get_width()//2,
                y + copo_altura - bola_imagem_resized.get_height() - 10
            ))
        
        # Atualiza a pontuação e a rodada atual na tela.
        # Renderiza o texto da pontuação atual com a fonte pré-definida,
                # cor preta e com antialiasing ativado (True).
        # O antialiasing suaviza as bordas do texto, melhorando a legibilidade.
        texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, PRETO)

        # Posiciona o texto da pontuação no canto superior 
                # esquerdo da tela (10 pixels da borda superior
                # e 10 da borda esquerda), garantindo que ele esteja 
                # sempre visível e não sobreposto por outros elementos gráficos.
        tela.blit(texto_pontuacao, (10, 10))
        
        # Renderiza o texto da rodada atual com as mesmas configurações de fonte e cor.
        texto_rodada = fonte.render(f"Rodada: {rodada}", True, PRETO)

        # Posiciona o texto da rodada na tela. Calcula-se a posição x 
                # subtraindo a largura do texto renderizado
                # do limite direito da tela (LARGURA) e subtraindo 10 pixels 
                # adicionais para manter uma margem da borda,
                # garantindo que o texto não fique muito próximo da
                # borda e seja fácil de ler.
        tela.blit(texto_rodada, (LARGURA - texto_rodada.get_width() - 10, 10))
        
        # Após posicionar todos os elementos gráficos (copos, bola, textos 
                # de pontuação e rodada), a tela é atualizada,
                # refletindo todas as alterações visuais feitas no
                # ciclo atual do loop de animação.
        pygame.display.update()
    
        # Atualiza a tela com todos os novos elementos desenhados.
        pygame.display.update()
    
        # Introduz um pequeno atraso definido pela 'velocidade' para que
                # a animação seja visível e não apenas um borrão rápido.
        pygame.time.delay(int(velocidade))
    
    # Ao final do loop de animação, garante que todos os 
            # copos sejam redesenhados na tela,
    # com o copo que estava girando mostrando a parte 
            # especificada (frente ou trás) e a bola.
    desenhar_copos(copos, mostrando_bola=(girar_para == 'frente'), posicao_bola=idx)


# Definição da função que embaralha os copos em uma sequência 
        # para dificultar o rastreamento pelo jogador.
def embaralhar_copos(copos, velocidade):
    
    # Número fixo de vezes que os copos serão trocados de 
            # posição para garantir uma boa mistura.
    numero_de_embaralhamentos = 10
    
    # Loop que se repete pelo número de vezes definido em 
            # numero_de_embaralhamentos.
    for i in range(numero_de_embaralhamentos):
        
        # Este bloco de código processa eventos da fila de 
                # eventos do Pygame para manter a janela responsiva.
        # Sem isso, o programa pode parecer que travou se o usuário 
                # tentar interagir com a janela durante a execução deste loop.
        for evento in pygame.event.get():
            
            # Checa se o evento é de tipo QUIT, que ocorre quando o 
                    # usuário clica no botão de fechar a janela.
            if evento.type == pygame.QUIT:
                
                pygame.quit()  # Fecha todos os módulos do Pygame, liberando recursos.
                sys.exit()     # Sai do programa completamente.

        # Verifica se há mais de um copo para garantir que
                # uma troca possa ocorrer.
        if len(copos) > 1:
            
            # Escolhe aleatoriamente dois índices distintos da lista de
                    # copos, garantindo que a troca aconteça entre dois copos diferentes.
            idx1, idx2 = random.sample(range(len(copos)), 2)
            
            # Chama a função animar_troca para realizar a troca visual
                    # dos copos nos índices escolhidos com a velocidade definida.
            animar_troca(copos, idx1, idx2, velocidade)

    # Após completar todas as trocas, retorna a lista de
            # copos já embaralhada.
    return copos


# Define uma função para animar a troca de posições entre dois copos.
def animar_troca(copos, idx1, idx2, velocidade):
    
    # Recupera as posições iniciais dos dois copos envolvidos na troca.
            # copos[idx1] acessa o copo na posição idx1 na lista, 
            # retornando suas coordenadas (x, y).
    x1_inicial, y1_inicial = copos[idx1]  # Coordenadas do primeiro copo.
    x2_inicial, y2_inicial = copos[idx2]  # Coordenadas do segundo copo.

    # Calcula a diferença nas posições x e y entre os dois copos para 
            # determinar a distância que cada um deve percorrer.
    dx1 = x2_inicial - x1_inicial  # Distância horizontal que o primeiro copo precisa percorrer para chegar à posição inicial do segundo.
    dy1 = y2_inicial - y1_inicial  # Distância vertical que o primeiro copo precisa percorrer para chegar à posição inicial do segundo.

    dx2 = x1_inicial - x2_inicial  # Distância horizontal que o segundo copo precisa percorrer para chegar à posição inicial do primeiro.
    dy2 = y1_inicial - y2_inicial  # Distância vertical que o segundo copo precisa percorrer para chegar à posição inicial do primeiro.

    # Calcula o número de passos necessários para completar a animação,
            # baseado na maior distância a ser percorrida (horizontal ou vertical)
            # e na velocidade definida. A função abs() é usada para 
            # garantir que a distância seja um valor positivo.
    # A velocidade controla o número de pixels movidos em 
            # cada passo da animação.
    passos = max(abs(int(dx1)), abs(int(dy1))) // velocidade  # Usa a divisão inteira para determinar o número total de passos.

    # Garante que haja pelo menos um passo na animação para evitar
            # divisão por zero ou movimento instantâneo, o que
            # poderia causar erros visuais.
    if passos == 0:

        # Se o cálculo de passos resultar em zero, força pelo menos um passo.
        passos = 1  

    # Inicia um loop que se repete um número de vezes igual a 
            # 'passos', definido anteriormente.
    for passo in range(passos):
        
        # Este loop interno processa eventos do Pygame para 
                # manter a janela responsiva.
        # Se eventos não forem processados, a janela pode parecer congelada.
        for evento in pygame.event.get():
            
            # Verifica se o evento é do tipo QUIT, o que significa
                    # que o usuário fechou a janela do jogo.
            if evento.type == pygame.QUIT:
                
                pygame.quit()  # Encerra todos os módulos do Pygame.
                sys.exit()     # Sai do script, encerrando o programa completamente.
    
        # 't' é uma variável que representa a fração do caminho
                # que cada copo deve ter movido até o momento atual do loop.
        t = (passo + 1) / passos  # 't' varia de 1/passos até 1 durante a animação.
    
        # Define a altura máxima que os copos atingem ao trocar de
                # lugar, criando uma curva parabólica no movimento.
        h = 150  # Altura máxima da curva, pode ser ajustada para
                # aumentar ou diminuir o arco do movimento.
    
        # Calcula as novas posições x e y para o primeiro copo 
                # usando interpolação linear e uma equação parabólica.
        # A interpolação linear é utilizada para calcular a 
                # posição linear entre dois pontos com base em
                # um fator 't' que varia de 0 a 1.
        # Aqui, 'dx1 * t' calcula o deslocamento horizontal 
                # proporcional ao tempo 't', onde 'dx1' é a 
                # diferença total de x a percorrer.
        nova_x1 = x1_inicial + dx1 * t

        # Para o deslocamento vertical, além da interpolação 
                # linear 'dy1 * t', aplicamos uma equação parabólica
                # para adicionar um efeito de arco.
        # '- h * 4 * t * (1 - t)' cria uma curva parabólica
                # onde 'h' é a altura máxima da curva.
        # O termo '4 * t * (1 - t)' é máximo no meio da 
                # animação (t = 0.5), fazendo o copo atingir o
                # ponto mais alto do arco neste momento.
        nova_y1 = y1_inicial + dy1 * t - h * 4 * t * (1 - t)
        
        # Realiza os mesmos cálculos para o segundo copo, 
                # usando 'dx2' e 'dy2' que representam as 
                # distâncias a serem percorridas
                # na direção oposta às do primeiro copo.
        nova_x2 = x2_inicial + dx2 * t

        # Similarmente, aplica a interpolação linear e a 
                # equação parabólica para o movimento 
                # vertical do segundo copo, garantindo que ele 
                # também siga uma trajetória curva simétrica à do primeiro copo.
        nova_y2 = y2_inicial + dy2 * t - h * 4 * t * (1 - t)

    
        # Atualiza as posições dos copos na lista 'copos' para 
                # as novas posições calculadas.
        copos[idx1] = (nova_x1, nova_y1)
        copos[idx2] = (nova_x2, nova_y2)
    
        # Chama a função desenhar_copos para atualizar a
                # visualização dos copos na tela com as novas posições.
        desenhar_copos(copos)
    
        # Pausa a execução do programa por 10 milissegundos 
                # para que a animação seja visível.
        pygame.time.delay(10)
    
    # Garante que as posições dos copos ao final da animação
            # sejam exatamente as posições iniciais um do outro.
    # Isso corrige quaisquer discrepâncias menores causadas 
            # pela interpolação durante o loop.
    copos[idx1] = (x2_inicial, y2_inicial)
    copos[idx2] = (x1_inicial, y1_inicial)
    
    # Desenha os copos uma última vez nas posições finais para 
            # garantir que estejam corretamente posicionados.
    desenhar_copos(copos)



# Loop principal do jogo
jogando = True

# Variável para verificar se o jogador acertou
acerto = False  

 # Número inicial de copos
numero_copos = 3 

# Este é o loop principal do jogo, que continua rodando 
        # enquanto a variável 'jogando' for verdadeira.
while jogando:
    
    # A cada 5 rodadas, o número de copos no jogo é incrementado. Isso
            # aumenta a dificuldade do jogo progressivamente.
    # 'rodada % 5 == 0' verifica se o número da rodada atual é divisível
            # por 5, o que indica que cinco rodadas completas ocorreram.
    # 'rodada != 0' garante que o incremento não aconteça na rodada zero,
            # que é tecnicamente a primeira rodada antes de qualquer jogo.
    if rodada % 5 == 0 and rodada != 0:
        numero_copos += 1  # Aumenta o número de copos por um.

    # Calcula o espaço disponível na tela para os copos, subtraindo o
            # espaço de margem fixo de 50 pixels de cada lado.
    espaco = 50  # Espaço de margem de cada lado da tela.
    espaco_total = LARGURA - 2 * espaco  # Espaço total disponível subtraindo as margens laterais.

    # Calcula a largura máxima que cada copo pode ter, considerando o
            # número atual de copos e o espaço entre eles de 10 pixels.
    # '(numero_copos - 1) * 10' calcula o espaço total necessário
            # para as margens entre os copos.
    max_copo_largura = (espaco_total - (numero_copos - 1) * 10) / numero_copos
    
    # Verifica se a largura máxima calculada é maior que a largura
            # original dos copos (copo_largura_original).
    # Se for, usa a largura original; se não, usa o maior valor entre a
            # largura máxima calculada e a largura mínima permitida.
    if max_copo_largura > copo_largura_original:

        # Usa a largura original se a largura máxima for muito grande.
        copo_largura = copo_largura_original  
        
    else:

        # Garante que a largura do copo não seja menor que o mínimo.
        copo_largura = max(max_copo_largura, MIN_CUPO_LARGURA)  

    # Calcula a altura do copo para manter a proporção original
            # entre largura e altura dos copos.
    # A razão entre a altura original e a largura original
            # (copo_altura_original / copo_largura_original) é usada
            # para calcular a nova altura com base na nova largura ajustada.
    copo_altura = copo_largura * (copo_altura_original / copo_largura_original)


    # Redimensionar imagens dos copos e da bola para se ajustarem às
            # novas dimensões necessárias no jogo.
    # A função pygame.transform.scale é usada para redimensionar
            # uma imagem para as dimensões desejadas.
    copo_frente_resized = pygame.transform.scale(copo_frente_original, (int(copo_largura), int(copo_altura)))

    # Redimensiona a imagem do copo de frente para as novas dimensões de
            # largura e altura calculadas previamente.
    copo_tras_resized = pygame.transform.scale(copo_tras_original, (int(copo_largura), int(copo_altura)))

    # Redimensiona a imagem do copo de trás, utilizando as
            # mesmas novas dimensões.
    bola_imagem_resized = pygame.transform.scale(
        bola_imagem_original, (int(copo_largura * 0.33), int(copo_largura * 0.33)))
    # Redimensiona a imagem da bola para ser proporcional à
            # largura do copo. Aqui, a bola é configurada para ter um terço (1/3)
            # da largura do copo, o que ajuda a manter a proporção
            # visual e o realismo do jogo.
    
    # Chama uma função para gerar as posições iniciais dos copos na tela.
    # A função gerar_posicoes_iniciais calcula e retorna uma
            # lista com as coordenadas (x, y) para cada copo.
    copos = gerar_posicoes_iniciais(numero_copos, copo_largura)
    
    # Define a posição inicial da bola sob um dos copos.
    # Se o jogador não acertou a posição da bola na rodada
            # anterior (indicado pela variável acerto),
            # uma nova posição aleatória para a bola é escolhida
            # entre os copos disponíveis.
    if not acerto:
        posicao_bola = random.randint(0, numero_copos - 1)
    
    # Cria uma lista para manter o estado de cada copo como 'tras',
            # indicando que todos os copos começam mostrando o lado de trás.
    estados_copos = ['tras'] * numero_copos
    
    # Inicia uma sequência de animações para mostrar a bola
            # sob o copo selecionado.
    # A função animar_girar_copo é chamada para girar o copo e
            # revelar a bola por um momento.
    animar_girar_copo(copos, posicao_bola, 30, girar_para='frente')

    # Pausa o jogo por 3000 milissegundos (3 segundos) para que
            # os jogadores possam ver a bola sob o copo.
    pygame.time.delay(3000)

    # Após a pausa, a função animar_girar_copo é chamada novamente
            # para girar o copo de volta, escondendo a bola e 
            # retornando o copo para o estado inicial.
    animar_girar_copo(copos, posicao_bola, 30, girar_para='tras')
    
    # Chama a função para embaralhar os copos, iniciando a fase de 
            # desafio onde o jogador deve acompanhar onde a 
            # bola foi escondida.
    # A função embaralhar_copos mistura os copos várias 
            # vezes para aumentar a dificuldade do jogo.
    embaralhar_copos(copos, velocidade)


    # Configura um loop para esperar a ação do usuário,
            # especificamente um clique do mouse.
    esperando_escolha = True
    while esperando_escolha:
        
        # Chama a função para desenhar os copos na tela, 
                # atualizando a visualização.
        desenhar_copos(copos)
    
        # Processa todos os eventos que foram enviados para a
                # fila de eventos do Pygame.
        for evento in pygame.event.get():
            
            # Verifica se o evento é do tipo QUIT, o que ocorre quando o 
                    # usuário fecha a janela do jogo.
            if evento.type == pygame.QUIT:

                # Altera a variável 'jogando' para False, o que encerra o 
                        # loop principal do jogo.
                jogando = False  

                # Sai do loop de espera por escolha, encerrando a espera por interação.
                esperando_escolha = False  
    
            # Verifica se houve um clique do mouse.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Captura a posição (x, y) onde o clique ocorreu.
                x_click, y_click = evento.pos
    
                # Inicia um loop que percorre todos os copos para identificar 
                        # qual deles foi clicado pelo usuário.
                for i in range(len(copos)):
                    
                    # Extrai as coordenadas x e y do copo atual da lista de copos.
                    x, y = copos[i]
                    
                    # Cria um objeto retângulo (pygame.Rect) que representa a 
                            # área ocupada pelo copo na tela.
                    # Este retângulo é definido pelas coordenadas x e y do 
                            # copo e por sua largura e altura.
                    rect = pygame.Rect(x, y, copo_largura, copo_altura)
                
                    # Verifica se o ponto onde ocorreu o clique do
                            # mouse (coordenadas x_click e y_click) está dentro
                            # das coordenadas que definem o retângulo do copo.
                    # A função 'collidepoint' é utilizada aqui para determinar 
                            # se um ponto específico (x_click, y_click)
                            # está dentro do retângulo definido por 'rect', 
                            # que representa a área ocupada pelo copo na tela.
                    if rect.collidepoint(x_click, y_click):
                        
                        # Se a condição é verdadeira, isso indica que o usuário 
                                # clicou diretamente sobre um dos copos.
                        # Neste caso, a função 'animar_girar_copo' é chamada para 
                                # iniciar a animação que revela o que está sob o copo.
                        # Este processo visual é crucial para indicar ao jogador o 
                                # resultado de sua escolha.
                        animar_girar_copo(copos, i, 30, girar_para='frente')
                    
                        # Após a animação de girar o copo, verifica-se se o copo que o 
                                # jogador escolheu é aquele sob o qual a bola está escondida.
                        if i == posicao_bola:
                            
                            # Se o jogador escolheu corretamente, a pontuação é
                                    # incrementada por 1, refletindo o sucesso em seguir a bola.
                            pontuacao += 1
                            
                            # Aumenta também a velocidade da animação por 2 unidades, tornando o 
                                    # jogo mais desafiador à medida que o jogador demonstra habilidade.
                            velocidade += 2 # AQUIIIIIIIIIIIIIIIIIIIIIIIIII
                            
                            # A variável 'acerto' é definida como True, sinalizando
                                    # que o jogador acertou a localização da bola,
                                    # o que pode influenciar a lógica do jogo em rodadas subsequentes.
                            acerto = True
                    
                            # Cria um texto de felicitação utilizando a fonte definida
                                    # anteriormente. O texto é renderizado com cor verde.
                            texto = fonte.render("Parabéns! Você acertou!", True, VERDE)
                            
                            # O texto é então posicionado no centro horizontal da tela,
                                    # ajustado para ser visível acima dos copos.
                            tela.blit(texto, (LARGURA//2 - texto.get_width()//2, 50))
                            
                            # Atualiza a tela para mostrar imediatamente a mensagem de sucesso.
                            pygame.display.update()
                            
                            # Pausa o jogo por 2000 milissegundos (2 segundos), dando
                                    # tempo para o jogador ler e processar a mensagem de sucesso.
                            pygame.time.delay(2000)
                    
                        else:
                            
                            # Se o jogador escolheu o copo errado, ou seja, o copo
                                    # selecionado não é aquele que esconde a bola.
                            acerto = False  # Atualiza a variável 'acerto' para False, indicando o erro.
                            
                            # Inicia a animação que revela a posição correta da
                                    # bola, girando o copo correto para frente.
                            animar_girar_copo(copos, posicao_bola, 30, girar_para='frente')
                    
                            # Cria um texto de erro, informando ao jogador que
                                    # sua escolha foi incorreta.
                            texto = fonte.render(f"Errado! A bola estava no copo {posicao_bola+1}.", True, VERMELHO)
                            
                            # Posiciona este texto no mesmo local que a mensagem de
                                    # acerto para consistência visual.
                            tela.blit(texto, (LARGURA//2 - texto.get_width()//2, 50))
                            
                            # Atualiza a tela para mostrar a mensagem de erro.
                            pygame.display.update()
                            
                            # Pausa o jogo por 2000 milissegundos (2 segundos), permitindo
                                    # que o jogador veja claramente onde errou.
                            pygame.time.delay(2000)
                    
                        # Encerra o loop de espera por escolha do jogador, já que uma
                                # ação válida foi registrada.
                        esperando_escolha = False
                    
                        # Sai do loop for assim que um clique válido é processado, pois não
                                # é necessário continuar verificando outros copos.
                        break


        # Atualiza a tela após processar os eventos e possíveis animações.
        pygame.display.update()
    
    # Incrementa o número da rodada após o término da interação do usuário e
            # o processamento de todos os eventos.
    rodada += 1

# É utilizado para desinicializar todos os módulos do Pygame que foram
        # inicializados anteriormente com pygame.init().
# Esta função é chamada para limpar os recursos de Pygame
        # antes de fechar o programa.
pygame.quit()

# É usada para sair do programa Python. Por padrão,
        # ela levanta a exceção
sys.exit()