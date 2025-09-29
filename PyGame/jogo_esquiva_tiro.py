import pygame

# Importa o módulo random, que contém funções para gerar números aleatórios.
import random

# Inicializa todos os módulos importados do pygame, o que é necessário
# para usar as funcionalidades do pygame.
pygame.init()

# Define as dimensões da janela do jogo, com uma largura de 800 pixels e altura de 600 pixels.
largura, altura = 800, 600

# Cria a janela do jogo com as dimensões definidas acima.
tela = pygame.display.set_mode((largura, altura))

# Define o título da janela do jogo.
pygame.display.set_caption('Jogo de Esquiva e Tiro')

# Carrega a imagem do jogador do arquivo 'jogador.png'. O caminho do 
# arquivo deve ser ajustado se a imagem não estiver na mesma pasta do script.
imagem_jogador = pygame.image.load('jogador.png')

# Redimensiona a imagem do jogador para ter 50 pixels de largura e 50 pixels de altura.
imagem_jogador = pygame.transform.scale(imagem_jogador, (50, 50))

# Carrega a imagem do inimigo do arquivo 'inimigo.png'. Assim como o 
# jogador, o caminho precisa ser ajustado se necessário.
imagem_inimigo = pygame.image.load('inimigo.png')

# Redimensiona a imagem do inimigo para ter as mesmas dimensões da
# imagem do jogador, ou seja, 50x50 pixels.
imagem_inimigo = pygame.transform.scale(imagem_inimigo, (50, 50))

# Carrega a imagem da explosão do arquivo 'explosao.png', que é 
# usada para mostrar a destruição de um inimigo.
imagem_explosao = pygame.image.load('explosao.png')

# Redimensiona a imagem da explosão para 50x50 pixels para manter a 
# consistência no tamanho das imagens do jogo.
imagem_explosao = pygame.transform.scale(imagem_explosao, (50, 50))


# Lista de inimigos em explosão
explosoes = []


# Carregar som de tiro
# Substitua 'tiro.mp3' pelo caminho correto para o seu arquivo de som
som_tiro = pygame.mixer.Sound('tiro.mp3')


# Definição de duas cores em formato RGB: 
# preto e branco. O preto é definido como (0, 0, 0), 
# o que significa que não há contribuição de vermelho, verde ou azul.
preto = (0, 0, 0)

# Branco é definido como (255, 255, 255), o que significa a contribuição
# máxima de todas as três cores primárias de luz, resultando em branco.
branco = (255, 255, 255)

# Configurações específicas do jogador no jogo.
# Define o tamanho do jogador para 50 pixels.
tamanho_jogador = 50

# A posição inicial do jogador é configurada para ser horizontalmente no
# centro da tela (usando a largura dividida por 2) e verticalmente acima da 
# parte inferior da tela (altura menos duas vezes o tamanho do jogador).
posicao_jogador = [largura // 2, altura - 2 * tamanho_jogador]

# Define a velocidade do jogador. Esse valor pode ser usado para atualizar
# a posição do jogador a cada quadro.
velocidade_jogador = 5

# Configurações relacionadas aos inimigos dentro do jogo.
# Define o número de inimigos que aparecerão na tela.
num_inimigos = 10

# Define o tamanho de cada inimigo, assim como foi definido para o jogador.
tamanho_inimigo = 50

largura = 800  # Largura da janela de exibição

# Inicialização da lista vazia
posicoes_inimigos = []

# Loop `for` para adicionar a cada inimigo na lista
for _ in range(num_inimigos):
    
    # Cria um dicionário para o inimigo com uma posição 'x' aleatória, 
    # posição 'y' aleatória e 
    # velocidade aleatória
    inimigo = {
        'x': random.randint(0, largura - tamanho_inimigo),
        'y': random.randint(-200, 0),
        'velocidade': random.randint(3, 7)
    }
    
    # Adiciona o dicionário do inimigo na lista `posicoes_inimigos`
    posicoes_inimigos.append(inimigo)
    
    
# Configurações para os tiros disparados pelo jogador.
# Uma lista vazia para armazenar os tiros que serão disparados pelo jogador.
tiros = []

# Define a velocidade com a qual os tiros se movem pela tela.
velocidade_tiro = 7

# Variáveis para manter a pontuação e o número de vidas restantes do jogador.
# Inicia a pontuação do jogador como 0.
pontos = 0

# O jogador começa com 3 vidas.
vidas = 3

# Configuração do texto que será exibido na tela do jogo.
# Escolhe a fonte padrão do sistema para usar na 
# renderização do texto com tamanho 36.
fonte = pygame.font.SysFont(None, 36)

# Início do loop principal do jogo.
# Cria um objeto Clock que pode ser usado para controlar o tempo
# dentro do jogo, por exemplo, para limitar a taxa de quadros por segundo.
relogio = pygame.time.Clock()

# Define uma variável booleana para determinar se o jogo terminou ou
# não. Inicialmente é definida como False, pois o jogo ainda não terminou.
fim_de_jogo = False


# Após iniciar o pygame e antes de entrar no loop do jogo, carrega e dimensiona a imagem de fundo
imagem_fundo = pygame.image.load('fundo_estrelas.jpg')

# Assegura de que a imagem cubra toda a tela
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))


# Aqui estamos definindo uma função chamada `criar_novo_inimigo`. Funções
# são blocos reutilizáveis de código que realizam uma ação específica.
def criar_novo_inimigo():
    
    # Dentro da função, criamos um dicionário chamado `novo_inimigo`. 
    # Um dicionário em Python é uma coleção não ordenada de itens.
    # Cada item do dicionário é um par de chave: valor.
    # Chaves são únicas dentro de um dicionário, enquanto valores podem não ser.
    novo_inimigo = {
        
        # A chave 'x' armazena a posição horizontal do novo inimigo. 
        # `random.randint(a, b)` retorna um número inteiro aleatório N tal que a <= N <= b.
        # `largura - tamanho_inimigo` é usada para garantir que o inimigo não
        # apareça parcialmente fora da tela. `largura` é a largura total da tela e 
        # `tamanho_inimigo` é a largura do inimigo.
        'x': random.randint(0, largura - tamanho_inimigo),
        
        # A chave 'y' armazena a posição vertical do novo inimigo. O inimigo 
        # aparecerá em uma posição vertical aleatória acima da tela (entre -200 
        # e 0 pixels acima da borda superior), permitindo que ele "caia" para dentro da tela.
        'y': random.randint(-200, 0),
        
        # A chave 'velocidade' determina a velocidade com a qual o inimigo 
        # se move para baixo em direção ao jogador. Um número aleatório entre 3 e 7 é 
        # escolhido, significando que os inimigos terão velocidades variadas.
        'velocidade': random.randint(3, 7)
        
    }
    
    # Após criar o dicionário `novo_inimigo` com as chaves e valores 
    # definidos, adicionamos esse dicionário à lista global `posicoes_inimigos`.
    # `append` é um método de lista que adiciona um item ao final da lista. 
    # Neste caso, estamos adicionando o `novo_inimigo` à lista `posicoes_inimigos`.
    posicoes_inimigos.append(novo_inimigo)
    
    
# Este loop `while` continuará executando até que a variável
# `fim_de_jogo` seja verdadeira. `fim_de_jogo` é uma variável 
# que controla se o jogo deve continuar rodando ou se deve terminar. 
# No início, ela é definida como False, então o loop se iniciará.
while not fim_de_jogo:

    # `relogio.tick(30)` é uma chamada para limitar o jogo a rodar
    # a um máximo de 30 quadros por segundo (fps). Isso é feito para 
    # garantir que o jogo não execute muito rápido e que a jogabilidade 
    # seja a mesma independente da rapidez do hardware do computador.
    relogio.tick(30)
    
    # `tela.blit(imagem_fundo, (0, 0))` é usado para desenhar a imagem 
    # de fundo na tela do jogo. O método `blit` é uma forma eficiente de 
    # desenhar imagens ou 'sprites' em uma superfície no Pygame. O primeiro 
    # argumento é o objeto de imagem a ser desenhado, e o segundo argumento é 
    # a posição onde a imagem será colocada na tela. (0, 0) é o canto superior
    # esquerdo da tela.
    tela.blit(imagem_fundo, (0, 0))


    # Aqui, começamos um loop que verificará todos os eventos da fila de 
    # eventos do Pygame. Eventos são ações do usuário, como pressionar uma
    # tecla ou mover o mouse. `pygame.event.get()` obtém todos os eventos 
    # da fila de eventos.
    for evento in pygame.event.get():
        
        # Dentro deste loop, verificamos se o tipo de algum evento é
        # `pygame.QUIT`. `pygame.QUIT` é um evento que é disparado quando o 
        # usuário tenta fechar a janela do jogo, como clicar no botão 'fechar' da janela.
        if evento.type == pygame.QUIT:
            
            # Se um evento `pygame.QUIT` for detectado, definimos a 
            # variável `fim_de_jogo` como True. Isso fará com que a condição
            # do loop while não seja mais atendida (pois `not fim_de_jogo` não 
            # será mais verdadeiro) e o loop principal será encerrado, terminando o jogo.
            fim_de_jogo = True


        # Continuação do loop que verifica os eventos
        # Aqui estamos verificando se algum evento de tecla foi pressionado.
        # O evento `pygame.KEYDOWN` é disparado sempre que uma tecla é pressionada.
        if evento.type == pygame.KEYDOWN:
            
            # Agora, estamos verificando se a tecla pressionada é a
            # tecla de espaço (`pygame.K_SPACE`).
            # A tecla de espaço geralmente é usada para ações como atirar em jogos.
            if evento.key == pygame.K_SPACE:

                # Criamos um dicionário que representa o tiro que será disparado do lado esquerdo do jogador.
                # A posição x do tiro é a mesma do jogador, significando que ele será disparado da posição atual do jogador no eixo x.
                # A posição y também é a mesma do jogador, para que o tiro comece onde o jogador está atualmente.
                # A 'velocidade' é um valor que será usado para mover o tiro pelo eixo y (para cima, se for positivo).
                tiro_esquerda = {'x': posicao_jogador[0], 'y': posicao_jogador[1], 'velocidade': velocidade_tiro}
                
                # O tiro é então adicionado à lista de tiros, será iterada em outra parte do código
                # para atualizar a posição dos tiros e desenhá-los na tela.
                tiros.append(tiro_esquerda)

                # Aqui, um segundo dicionário é criado para o tiro que será disparado do lado direito do jogador.
                # Ele é similar ao tiro esquerdo, mas a posição x é incrementada pelo tamanho do jogador para que
                # apareça ao lado do jogador e não sobre a mesma posição que o tiro esquerdo.
                tiro_direita = {'x': posicao_jogador[0] + tamanho_jogador, 'y': posicao_jogador[1], 'velocidade': velocidade_tiro}
                
                # Este tiro também é adicionado à lista de tiros.
                tiros.append(tiro_direita)

                # 'som_tiro.play()' chama o método play() no objeto som_tiro.
                # Isso irá reproduzir o som de tiro que foi carregado e atribuído a `som_tiro` no ponto anterior do código.
                # Este som será reproduzido toda vez que a tecla de espaço for pressionada e os tiros forem disparados.
                som_tiro.play()
      
    # A função `pygame.key.get_pressed()` é chamada para obter o
    # estado atual de todas as teclas do teclado.
    # O retorno é uma lista onde cada tecla tem um valor de True se 
    # estiver sendo pressionada no momento, e False caso contrário.
    teclas = pygame.key.get_pressed()

    # A seguir, temos uma série de verificações para as teclas de
    # movimento - esquerda, direita, cima e baixo.

    # Aqui, verificamos se a tecla de seta para a esquerda (K_LEFT) está 
    # pressionada E também se a posição x do jogador é maior que 0.
    # Isso é para garantir que o jogador não se mova para fora da tela pela esquerda.
    if teclas[pygame.K_LEFT] and posicao_jogador[0] > 0:
        
        # Se a condição for verdadeira, diminuímos a posição x do jogador pela 'velocidade_jogador',
        # o que move o jogador para a esquerda na tela.
        posicao_jogador[0] -= velocidade_jogador

    # Aqui, verificamos se a tecla de seta para a direita (K_RIGHT) está 
    # pressionada E também se a posição x do jogador
    # é menor que a largura da tela menos o tamanho do jogador.
    # Isso impede que o jogador se mova para fora da tela pela direita.
    if teclas[pygame.K_RIGHT] and posicao_jogador[0] < largura - tamanho_jogador:
        
        # Se a condição for verdadeira, aumentamos a posição x do 
        # jogador pela 'velocidade_jogador',
        # o que move o jogador para a direita na tela.
        posicao_jogador[0] += velocidade_jogador

    # Aqui, verificamos se a tecla de seta para cima (K_UP) está pressionada
    # E também se a posição y do jogador é maior que 0.
    # Isso evita que o jogador se mova para fora da tela pela parte superior.
    if teclas[pygame.K_UP] and posicao_jogador[1] > 0:
        
        # Se a condição for verdadeira, diminuímos a posição y do 
        # jogador pela 'velocidade_jogador',
        # o que move o jogador para cima na tela.
        posicao_jogador[1] -= velocidade_jogador

    # Finalmente, verificamos se a tecla de seta para baixo (K_DOWN) está 
    # pressionada E também se a posição y do jogador
    # é menor que a altura da tela menos o tamanho do jogador.
    # Isso impede que o jogador se mova para fora da tela pela parte inferior.
    if teclas[pygame.K_DOWN] and posicao_jogador[1] < altura - tamanho_jogador:
        
        # Se a condição for verdadeira, aumentamos a posição y do jogador 
        # pela 'velocidade_jogador',
        # o que move o jogador para baixo na tela.
        posicao_jogador[1] += velocidade_jogador
        
    
    # Iniciamos um loop 'for' para iterar sobre uma cópia da lista 'posicoes_inimigos'.
    # Usamos 'posicoes_inimigos[:]' para criar uma cópia da lista porque talvez
    # precisemos alterar a lista original enquanto iteramos sobre ela.
    # Alterar uma lista enquanto se itera diretamente sobre ela pode levar a 
    # comportamentos inesperados.
    for inimigo in posicoes_inimigos[:]:  

        # Aumentamos a posição 'y' do inimigo pela 'velocidade' do inimigo.
        # Isso simula o movimento do inimigo para baixo na tela.
        # A 'velocidade' é um valor que foi definido aleatoriamente quando o inimigo foi criado.
        inimigo['y'] += inimigo['velocidade']

        # Aqui verificamos se o inimigo saiu da parte inferior da tela.
        # 'altura' é a altura total da tela, então se a posição 'y' do inimigo 
        # for maior que isso, ele saiu da tela.
        if inimigo['y'] > altura:
            
            # Se o inimigo saiu da tela, nós o removemos da lista 'posicoes_inimigos'.
            # Isso é feito para que não continuemos a processar inimigos que não estão mais visíveis,
            # e também para liberar memória.
            posicoes_inimigos.remove(inimigo)

            # Depois de remover um inimigo, chamamos a função 'criar_novo_inimigo' 
            # para adicionar um novo inimigo à lista.
            # Isso mantém o número de inimigos constante no jogo.
            criar_novo_inimigo()


    # Lista para manter tiros e inimigos a serem removidos
    tiros_a_remover = []
    inimigos_a_remover = []
            
    
    # Inicia um loop 'for' que irá percorrer cada 'tiro' na lista de 'tiros'.
    # Esta lista contém todos os tiros atualmente ativos na tela do jogo.
    for tiro in tiros:
        
        # O valor da coordenada 'y' do tiro é decrementado pela quantidade especificada pela 'velocidade' do tiro.
        # Isso efetivamente move o tiro para cima na tela, pois em sistemas de coordenadas de tela, 
        # um valor menor de 'y' significa uma posição mais alta na tela.
        # O operador '-=' é uma forma abreviada de escrever 'tiro['y'] = tiro['y'] - tiro['velocidade']'.
        tiro['y'] -= tiro['velocidade']

        # Aqui ocorre uma checagem condicional para saber se o tiro saiu da área visível da tela.
        # Se a posição 'y' do tiro for menor que 0, isso significa que o tiro moveu-se para além
        # da borda superior da tela e, portanto, não é mais visível para o jogador.
        if tiro['y'] < 0:
            
            # Se o tiro saiu da tela, ele é adicionado à lista 'tiros_a_remover'.
            # Esta lista é utilizada para acompanhar quais tiros precisam ser removidos da lista de tiros ativos,
            # pois manter tiros que não estão mais na tela consumiria memória e poder de processamento desnecessariamente.
            tiros_a_remover.append(tiro)


    # Este bloco de código está dentro de um loop que atualiza a posição dos tiros e verifica se eles colidiram com algum inimigo.
    for tiro in tiros:  # Começa a iterar sobre cada tiro presente na lista 'tiros'.
        for inimigo in posicoes_inimigos:  # Dentro do loop de tiros, itera sobre cada inimigo na lista 'posicoes_inimigos'.
            
            # A próxima linha é uma condição complexa que verifica se as posições do tiro e do inimigo se sobrepõem.
            # A condição 'inimigo['x'] < tiro['x'] < inimigo['x'] + tamanho_inimigo' verifica se a posição 'x' do tiro
            # está entre a posição 'x' do inimigo e o limite direito do inimigo (sua posição 'x' mais o seu tamanho).
            # A condição 'inimigo['y'] < tiro['y'] < inimigo['y'] + tamanho_inimigo' faz o mesmo para a posição 'y'.
            if (inimigo['x'] < tiro['x'] < inimigo['x'] + tamanho_inimigo) and (inimigo['y'] < tiro['y'] < inimigo['y'] + tamanho_inimigo):
                
                # Se houve colisão, o tiro é adicionado à lista 'tiros_a_remover'.
                tiros_a_remover.append(tiro)
                
                # O inimigo também é adicionado à lista 'inimigos_a_remover'.
                inimigos_a_remover.append(inimigo)

                # A colisão resulta na criação de uma 'explosão'. Uma nova entrada é adicionada à lista 'explosoes'.
                # Essa entrada é um dicionário que guarda a posição do inimigo e o tempo atual do jogo.
                # O tempo é obtido chamando 'pygame.time.get_ticks()', que retorna o número de milissegundos desde
                # que 'pygame.init()' foi chamado.
                explosoes.append({'x': inimigo['x'], 'y': inimigo['y'], 'tempo': pygame.time.get_ticks()})

                # A pontuação do jogador é incrementada em 10 pontos para cada inimigo atingido.
                pontos += 10
                
                # O loop é interrompido após a detecção de uma colisão para evitar múltiplas colisões com o mesmo tiro.
                break
             
    
    # Inicia um loop 'for' que itera através de cada elemento na lista 'tiros_a_remover'.
    # A lista 'tiros_a_remover' contém todos os objetos 'tiro' que colidiram com inimigos ou saíram dos limites da tela.
    for tiro in tiros_a_remover:
        
        # Dentro do loop, há uma verificação condicional 'if' que checa se o objeto 'tiro' ainda está presente na lista 'tiros'.
        # É possível que um 'tiro' seja adicionado mais de uma vez à lista 'tiros_a_remover' antes da atualização da lista 'tiros'.
        # Isso pode ocorrer devido a várias condições no jogo, como múltiplas colisões quase simultâneas.
        if tiro in tiros:
            
            # Se o 'tiro' ainda estiver na lista 'tiros', este é removido usando o método 'remove'.
            # O método 'remove' exclui a primeira ocorrência do valor fornecido da lista, neste caso, o objeto 'tiro' específico.
            tiros.remove(tiro)  # O 'tiro' é removido da lista de tiros ativos no jogo.

    # Inicia um segundo loop 'for' que itera por cada elemento na lista 'inimigos_a_remover'.
    # A lista 'inimigos_a_remover' contém todos os objetos 'inimigo' que foram atingidos por tiros.
    for inimigo in inimigos_a_remover:
        
        # Da mesma forma que com os 'tiros', há uma verificação condicional 'if' 
        # para determinar se o 'inimigo' ainda está presente na lista 'posicoes_inimigos'.
        # Novamente, isso é necessário para evitar tentativas de remover um 'inimigo' que
        # já foi excluído, o que geraria um erro.
        if inimigo in posicoes_inimigos:
            
            # Se o 'inimigo' ainda estiver na lista 'posicoes_inimigos', ele é removido.
            # A exclusão é feita da mesma maneira que para os 'tiros', removendo a primeira
            # ocorrência encontrada na lista que corresponde ao 'inimigo'.
            posicoes_inimigos.remove(inimigo)
            
            # Imediatamente após remover o 'inimigo', a função 'criar_novo_inimigo' é chamada.
            # Esta função é definida em outro lugar no código e é responsável por gerar um novo 'inimigo'.
            # O novo 'inimigo' tem propriedades aleatórias para sua posição e velocidade e é adicionado à lista 'posicoes_inimigos'.
            criar_novo_inimigo()  # Isso mantém o número de inimigos no jogo e assegura um fluxo contínuo de desafios para o jogador.


    
    # O loop 'for' percorre cada 'tiro' presente na lista 'tiros'.
    for tiro in tiros:
        
        # Para cada 'tiro', a função 'pygame.draw.rect' é utilizada para desenhar o tiro na tela.
        # 'pygame.draw.rect' recebe vários argumentos: o primeiro é o objeto 'tela', que é
        # a superfície onde o retângulo será desenhado.
        # O segundo argumento é a cor do retângulo (neste caso, 'branco').
        # O terceiro argumento é um tuple que define as propriedades do
        # retângulo: posição x, posição y, largura e altura.
        # Desenha um retângulo branco para representar o tiro.
        pygame.draw.rect(tela, branco, (tiro['x'], tiro['y'], 5, 10))

    # Após desenhar os tiros, a imagem do jogador é desenhada na tela.
    # O método 'blit' é usado para desenhar a 'imagem_jogador' na tela, com a 
    # posição x e y definida pelo objeto 'posicao_jogador'.
    # Desenha a imagem do jogador na posição atual.
    tela.blit(imagem_jogador, (posicao_jogador[0], posicao_jogador[1]))
    
    
    # Outro loop 'for' começa, desta vez iterando sobre cada 'inimigo' na 
    # lista 'posicoes_inimigos'.
    for inimigo in posicoes_inimigos:
        
        # Semelhante ao jogador, a imagem de cada inimigo é desenhada na tela 
        # na posição x e y especificada no objeto 'inimigo'.
        # Desenha cada inimigo na sua posição atual.
        tela.blit(imagem_inimigo, (inimigo['x'], inimigo['y']))

    # A pontuação do jogo é exibida na tela.
    # A função 'render' do objeto 'fonte' cria uma superfície de texto.
    # O primeiro argumento é a string a ser renderizada, neste caso, uma 
    # concatenação da palavra "Pontos: " com a variável 'pontos', que representa a pontuação do jogador.
    # O segundo argumento 'True' habilita o anti-aliasing do texto, tornando-o mais suave e fácil de ler.
    # O terceiro argumento é a cor do texto, aqui definida como 'branco'.
    texto_pontuacao = fonte.render(f"Pontos: {pontos}", True, branco)
    
    # Finalmente, o texto da pontuação é desenhado na tela utilizando o método 'blit'.
    # As coordenadas (10, 10) são usadas para posicionar o texto no canto superior esquerdo da tela.
    # Exibe a pontuação do jogador na tela.
    tela.blit(texto_pontuacao, (10, 10))
    
    
    # Este loop percorre cada inimigo presente na lista 'posicoes_inimigos'.
    for inimigo in posicoes_inimigos:
        
        # O código verifica se há uma colisão entre o jogador e o inimigo.
        # Uma colisão é detectada se qualquer uma das seguintes condições for verdadeira:
        # 1. O lado esquerdo do jogador (posicao_jogador[0]) está entre a extremidade
        # esquerda e a direita do inimigo (inimigo['x'] e inimigo['x'] + tamanho_inimigo).
        # 2. O lado direito do jogador (posicao_jogador[0] + tamanho_jogador) está
        # entre a extremidade esquerda e a direita do inimigo.
        # E simultaneamente:
        # 3. O topo do jogador (posicao_jogador[1]) está entre o topo e o fundo do inimigo (inimigo['y'] e inimigo['y'] + tamanho_inimigo).
        # 4. A parte inferior do jogador (posicao_jogador[1] + tamanho_jogador) está entre o topo e o fundo do inimigo.
        if (inimigo['x'] < posicao_jogador[0] < inimigo['x'] + tamanho_inimigo or
            inimigo['x'] < posicao_jogador[0] + tamanho_jogador < inimigo['x'] + tamanho_inimigo) and \
           (inimigo['y'] < posicao_jogador[1] < inimigo['y'] + tamanho_inimigo or
            inimigo['y'] < posicao_jogador[1] + tamanho_jogador < inimigo['y'] + tamanho_inimigo):

            # Se uma colisão é detectada, uma vida é subtraída do total de vidas do jogador.
            vidas -= 1

            # Se o jogador não tem mais vidas restantes, a variável 'fim_de_jogo' é definida como True.
            # Isso geralmente desencadeia o fim do jogo, saindo do loop principal e 
            # potencialmente mostrando uma tela de fim de jogo.
            if vidas == 0:
                fim_de_jogo = True
            else:
                
                # Se o jogador ainda tem vidas restantes, sua posição é reiniciada.
                # Aqui, a posição do jogador é definida para estar no meio da largura da tela e
                # um pouco acima da parte inferior da tela, considerando duas vezes a altura do jogador.
                posicao_jogador = [largura // 2, altura - 2 * tamanho_jogador]

            # O 'break' é importante porque sem ele, o jogador poderia perder mais de uma vida por colisão,
            # já que o loop poderia detectar colisões múltiplas em um único quadro.
            # Isso encerra o loop imediatamente após a detecção da primeira colisão para evitar esse problema.
            break
            
            
    # Primeiramente, capturamos o tempo atual com 'pygame.time.get_ticks()', que
    # retorna o número de milissegundos desde que 'pygame.init()' foi chamado.
    tempo_atual = pygame.time.get_ticks()

    # Uma lista chamada 'explosoes_a_remover' é criada para armazenar as explosões que
    # devem ser removidas após serem exibidas por tempo suficiente.
    explosoes_a_remover = []
    
    
    # Um loop 'for' é usado para iterar sobre cada explosão dentro da lista 'explosoes'.
    for explosao in explosoes:
        
        # Dentro do loop, verificamos se o tempo atual menos o tempo em que a 
        # explosão ocorreu é maior que 500 milissegundos.
        # Se mais de 500ms se passaram desde que a explosão ocorreu...
        if tempo_atual - explosao['tempo'] > 500:
            
            # a explosão é adicionada à lista 'explosoes_a_remover', pois já foi exibida
            # por tempo suficiente.
            explosoes_a_remover.append(explosao)
            
        else:
            
            # Se menos de 500ms se passaram, a explosão ainda deve ser exibida.
            # Usamos 'tela.blit()' para desenhar a imagem da explosão na tela na posição especificada.
            # 'imagem_explosao' é a imagem da explosão, enquanto 'explosao['x']' e 
            # 'explosao['y']' são as coordenadas onde a explosão deve ser desenhada.
            tela.blit(imagem_explosao, (explosao['x'], explosao['y']))

    
    # Este loop percorre todas as explosões que foram marcadas para remoção.
    for explosao in explosoes_a_remover:
        
        # Remove cada explosão da lista principal de explosões.
        explosoes.remove(explosao)

    # Agora, vamos exibir a pontuação e as vidas restantes do jogador.
    # 'fonte.render()' é chamado para criar um objeto de imagem do texto contendo a pontuação atual do jogador.
    # O primeiro argumento é a string do texto a ser renderizado.
    # O segundo argumento 'True' significa que o texto é anti-aliased, o que o torna mais suave e fácil de ler.
    # O terceiro argumento 'branco' é a cor do texto.
    texto_pontuacao = fonte.render(f"Pontos: {pontos}", True, branco)

    # Similarmente, um objeto de imagem do texto é criado para mostrar as vidas restantes do jogador.
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, branco)

    # 'tela.blit()' é usado para desenhar as imagens de texto na tela.
    # O primeiro argumento é o objeto de imagem do texto.
    # O segundo argumento é uma tupla (10, 10), que representa a posição na 
    # tela onde o texto da pontuação será desenhado.
    # Isso é colocado no canto superior esquerdo, 10 pixels para a direita e 10 pixels para baixo.
    tela.blit(texto_pontuacao, (10, 10))

    # Da mesma forma, o texto das vidas é desenhado logo abaixo do texto da pontuação.
    # A posição y é aumentada para 40 para separar os dois textos.
    tela.blit(texto_vidas, (10, 40))

    # Após desenhar tudo que é necessário para o quadro atual, 'pygame.display.flip()' é chamado.
    # Isso atualiza o conteúdo de toda a tela com tudo que foi blitado nela desde a última atualização.
    # No Pygame, isso pode ser visto como o fim do ciclo de desenho, e o quadro é agora apresentado ao jogador.
    pygame.display.flip()

# Fora do loop do jogo, depois que 'fim_de_jogo' é definido como True e o loop é terminado, 'pygame.quit()' é chamado.
# Esta função desativa todas as bibliotecas do Pygame, que é uma operação de limpeza necessária.
# É uma boa prática chamar 'pygame.quit()' antes do final do script para garantir que todos os recursos do Pygame sejam liberados corretamente.
pygame.quit()