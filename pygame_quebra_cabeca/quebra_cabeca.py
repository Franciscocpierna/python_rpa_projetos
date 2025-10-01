# Importação dos módulos necessários para o jogo
import pygame  # Biblioteca para criação de jogos e interfaces gráficas
import sys  # Módulo de sistema para interação com o interpretador Python
import random  # Módulo para geração de números aleatórios
import os  # Módulo para interação com o sistema operacional

# Inicialização de todos os módulos importados do pygame, necessária para qualquer jogo
pygame.init()

# Definição de cores no formato RGB, que serão usadas no jogo
BRANCO = (255, 255, 255)  # Cor branca, onde todos os canais RGB estão no máximo
PRETO = (0, 0, 0)  # Cor preta, onde todos os canais RGB estão no mínimo

# Definição das dimensões da janela do jogo
LARGURA_TELA = 600  # Largura da tela em pixels
ALTURA_TELA = 600  # Altura da tela em pixels

# Criação da janela do jogo, definindo seu tamanho com as dimensões especificadas anteriormente
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Definição do título da janela do jogo
pygame.display.set_caption('Quebra-Cabeça')


# Definição da função que irá listar as imagens em um diretório específico
def listar_imagens(pasta):
    
    # Lista de extensões de arquivo consideradas válidas para imagens
    extensoes_validas = ['.jpg', '.jpeg', '.png', '.bmp']
    
    # Utiliza a função listdir do módulo os para listar
    # todos os arquivos no diretório especificado
    arquivos = os.listdir(pasta)
    
    # Compreensão de lista para criar uma lista de caminhos completos para os arquivos de imagem
    # A função os.path.join é utilizada para garantir que o caminho do arquivo seja 
    # construído corretamente, independentemente do sistema operacional
    # A função os.path.splitext é usada para dividir o nome do arquivo em nome e extensão
    # A condição após o if verifica se a extensão do arquivo atual está na lista de extensões válidas
    # Apenas os arquivos com extensões válidas são incluídos na lista final que a função retorna
    # return [os.path.join(pasta, arquivo) for arquivo in arquivos if os.path.splitext(arquivo)[1] in extensoes_validas]

    # Cria uma lista vazia chamada 'imagens_validas' que armazenará os
    # caminhos dos arquivos de imagem que atendem aos critérios de seleção
    imagens_validas = []

    # Começa um loop 'for' que passará por cada item na lista 'arquivos', que se 
    # espera que contenha os nomes dos arquivos encontrados em um diretório específico
    for arquivo in arquivos:
        
        # Utiliza a função os.path.splitext do módulo 'os' para dividir
        # o nome do arquivo em duas partes: o nome base e a extensão
        # A função retorna uma tupla onde o índice [0] é o nome do arquivo e
        # o índice [1] é a extensão do arquivo
        # A extensão do arquivo é então armazenada na variável 'extensao'
        extensao = os.path.splitext(arquivo)[1]

        # Verifica se a extensão do arquivo atual (armazenada na variável 'extensao') 
        # está na lista 'extensoes_validas'
        # A lista 'extensoes_validas' é uma lista pré-definida de extensões
        # que são aceitas como imagens válidas, como .jpg ou .png
        if extensao in extensoes_validas:
            
            # Se a extensão do arquivo for considerada válida, o próximo 
            # passo é construir o caminho completo do arquivo
            # A função os.path.join é utilizada para garantir que o caminho
            # seja construído corretamente para o sistema operacional em uso
            # Ela combina a string 'pasta' (que se espera ser o caminho do 
            # diretório onde os arquivos estão localizados) com o 'arquivo' (o nome do arquivo)
            caminho_completo = os.path.join(pasta, arquivo)

            # Adiciona o 'caminho_completo' à lista 'imagens_validas'
            # Esta lista eventualmente conterá todos os caminhos completos dos 
            # arquivos de imagem que estão em um formato aceitável
            imagens_validas.append(caminho_completo)

    # Após o loop ser concluído e todos os arquivos válidos serem
    # adicionados à lista, 'imagens_validas' é retornada
    # Esta lista pode então ser usada em outras partes do programa 
    # para, por exemplo, carregar as imagens em um jogo
    return imagens_validas


# Definição de uma função que desenha retângulos na tela para cada
# imagem, atuando como botões para seleção
def desenha_selecao_imagens(imagens):
    
    # Iteração sobre a lista de caminhos de imagem, com o índice e o caminho de cada imagem
    for index, caminho_imagem in enumerate(imagens):
        
        # Desenho de um retângulo cinza claro para cada imagem na lista
        # As dimensões e a posição do retângulo são calculadas com base no índice da imagem
        # O retângulo tem uma largura fixa de 500 pixels e altura de 60 pixels
        # O retângulo é posicionado 50 pixels para a direita da borda
        # esquerda e 50 pixels mais 80 vezes o índice a partir do topo
        # Isso cria uma lista vertical de retângulos com espaçamento de 20 pixels entre eles
        pygame.draw.rect(tela, (200, 200, 200), (50, index * 80 + 50, 500, 60))
        
        # Carregamento da fonte padrão do pygame com tamanho 36 para o texto
        font = pygame.font.Font(None, 36)
        
        # Renderização do nome da imagem (sem o caminho completo) em cor cinza escuro
        # A função os.path.basename é usada para extrair apenas o nome do arquivo da imagem do caminho completo
        # O parâmetro 'True' habilita o anti-aliasing do texto, tornando-o mais suave
        texto = font.render(os.path.basename(caminho_imagem), True, (50, 50, 50))
        
        # Colocação do texto renderizado na tela
        # O texto é posicionado ligeiramente para a direita (60 pixels) e 
        # centralizado verticalmente dentro do retângulo correspondente
        tela.blit(texto, (60, index * 80 + 65))


# Esta função é responsável por desenhar as pecas do quebra-cabeça na tela
def desenhar_quebra_cabeca():
    
    # Loop através de cada peca na lista de pecas do quebra-cabeça
    # 'i' é o índice da peca na lista, e 'peca' é a tupla contendo as informações da peca
    for i, peca in enumerate(pecas):
        
        # Calcula a posição x onde a peca deve ser desenhada na tela
        # Isso é feito pegando o resto da divisão do índice por 3
        # Por exemplo, se a peca está na posição 4, x será 1 (4 % 3 = 1), indicando a segunda coluna
        x = i % 3
        
        # Calcula a posição y onde a peca deve ser desenhada na tela
        # Isso é feito dividindo o índice por 3 e pegando a parte inteira do resultado
        # Por exemplo, se a peca está na posição 4, y será 1 (4 // 3 = 1), indicando a segunda linha
        y = i // 3
        
        # A função 'blit' do objeto 'tela' do Pygame é usada para desenhar a peca na tela
        # 'peca[2]' é o objeto de superfície do Pygame que contém a imagem da peca
        # '(x*TAMANHO_BLOCO_LARGURA, y*TAMANHO_BLOCO_ALTURA)' é a posição onde a peca será desenhada
        # Essa posição é calculada multiplicando a posição da coluna e da linha pelo tamanho de cada bloco
        tela.blit(peca[2], (x * TAMANHO_BLOCO_LARGURA, y * TAMANHO_BLOCO_ALTURA))


# A variável 'imagens' é definida chamando a função 'listar_imagens'
# O argumento passado para a função é um caminho de diretório onde as imagens do quebra-cabeça estão localizadas
# Este caminho é uma string bruta (indicado pelo prefixo 'r'), 
# o que significa que os caracteres de escape não são processados
# Isso é útil para caminhos do Windows que usam o caractere
# de barra invertida ('\') que, de outra forma, seria 
# interpretado como um caractere de escape
imagens = listar_imagens(r'C:\python_projetos\python_rpa_projetos\pygame_quebra_cabeca\imagens')

# Este é o loop principal do jogo que continuará rodando até 
# que o programa seja fechado
while True:
    
    # Estado que indica se o jogador está atualmente no processo de 
    # escolher uma imagem para o quebra-cabeça
    escolhendo_imagem = True
    
    # Loop para a seleção de imagem. Continuará até que uma imagem seja escolhida
    while escolhendo_imagem:
        
        # Processamento da fila de eventos do Pygame
        for evento in pygame.event.get():
            
            # Se o evento for do tipo QUIT (janela fechada), termina o jogo 
            # e fecha a aplicação
            if evento.type == pygame.QUIT:
                
                # Finaliza todos os módulos do Pygame
                pygame.quit()
                
                # Fecha a janela e termina a execução do programa
                sys.exit()
                
            # É responsável por capturar e responder aos eventos de clique do mouse.
            # O evento MOUSEBUTTONDOWN é acionado quando um botão do mouse é pressionado.
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

                # Quando o botão esquerdo do mouse (botão 1) é pressionado, o
                # Pygame registra o tempo atual em milissegundos.
                # A função get_ticks() do módulo time do Pygame retorna o 
                # número de milissegundos desde que o Pygame foi inicializado.
                # Esse tempo é armazenado na variável start_click e será usado
                # para calcular a duração do clique.
                start_click = pygame.time.get_ticks()

            # A próxima condição verifica se o evento capturado é o MOUSEBUTTONUP, que
            # é acionado quando um botão do mouse é solto.
            if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:

                # Similarmente ao MOUSEBUTTONDOWN, quando o botão esquerdo do mouse é solto,
                # o Pygame registra o tempo atual em milissegundos e o armazena na variável end_click.
                end_click = pygame.time.get_ticks()

                # Agora, o código verifica se a duração do clique foi rápida, ou seja, se o botão foi solto
                # rapidamente após ser pressionado. Um clique é considerado "rápido" se a duração for menor que 500 milissegundos.
                # Isso é feito subtraindo o tempo do start_click do end_click e comparando se o resultado é menor que 500.
                # Essa verificação é usada para diferenciar entre cliques e cliques longos (ou "cliques e segura").
                if end_click - start_click < 500:

                    # Se foi detectado um clique rápido, as coordenadas x e y onde o clique ocorreu são obtidas.
                    # A função get_pos() retorna uma tupla contendo as posições x e y do cursor no momento do clique.
                    # Essas coordenadas serão usadas para determinar qual elemento gráfico foi clicado,
                    # como uma peça de um quebra-cabeça ou um botão em uma interface.
                    x, y = pygame.mouse.get_pos()

                    
                    # Calcula o índice da imagem com base na posição do clique
                    # As imagens são desenhadas começando 50 pixels para baixo, e 
                    # cada uma tem 80 pixels de altura
                    index = (y - 50) // 80
                    
                    # Verifica se o clique foi dentro da área dos retângulos onde as imagens são desenhadas
                    # Isso é feito verificando se o clique foi entre 50 e 550 pixels na horizontal (x)
                    # e se o clique foi dentro do intervalo vertical (y) onde a imagem está desenhada
                    # Também verifica se o índice calculado é menor que o número de imagens disponíveis
                    if 50 < x < 550 and 50 + index * 80 < y < 110 + index * 80 and index < len(imagens):
                        
                        # Se o clique foi válido, a imagem correspondente é selecionada
                        imagem_escolhida = imagens[index]
                        
                        # O estado 'escolhendo_imagem' é definido como False para sair do loop de seleção de imagem
                        escolhendo_imagem = False


        # Preenche toda a tela com a cor branca definida anteriormente
        # Isso efetivamente limpa a tela ou atualiza a tela com uma cor de fundo uniforme
        tela.fill(BRANCO)
        
        # Chama a função 'desenha_selecao_imagens' que irá desenhar os retângulos de seleção na tela
        # Cada retângulo corresponde a uma imagem que pode ser escolhida para jogar o quebra-cabeça
        # Esta função também desenha o texto com o nome da imagem sobre os retângulos
        desenha_selecao_imagens(imagens)
        
        # Atualiza a tela inteira para mostrar tudo o que foi desenhado desde a última atualização
        # Este é um método de 'double buffering', onde as alterações são feitas em um 'buffer' de tela fora da vista
        # e então rapidamente trocado com o 'buffer' que está sendo exibido
        # Isso é feito para evitar 'flickering' ou outros artefatos visuais
        pygame.display.flip()
        
    # Carrega a imagem selecionada pelo jogador usando a função load do módulo image do Pygame
    # O método convert() é chamado para converter o formato da imagem carregada
    # Isso é feito para otimizar o desempenho, garantindo que a imagem esteja no mesmo formato de pixel que a tela
    imagem = pygame.image.load(imagem_escolhida).convert()
    
    # Redimensiona a imagem para que ela se ajuste exatamente ao tamanho da tela
    # Usa a função scale do módulo transform do Pygame
    # LARGURA_TELA e ALTURA_TELA são as dimensões da tela definidas anteriormente
    # O resultado é que a imagem de quebra-cabeça preencherá toda a tela
    imagem = pygame.transform.scale(imagem, (LARGURA_TELA, ALTURA_TELA))
                
    
    # Define as dimensões de cada bloco (peca) do quebra-cabeça
    # A tela é dividida em uma grade 3x3, então a largura e a altura de cada bloco são um terço da largura e altura da tela
    # O operador // garante que a divisão seja inteira, pois as dimensões em pixels não podem ser fracionárias
    TAMANHO_BLOCO_LARGURA = LARGURA_TELA // 3
    TAMANHO_BLOCO_ALTURA = ALTURA_TELA // 3


    # Inicializa uma lista vazia para armazenar as pecas do quebra-cabeça
    pecas = []

    # Inicializa outra lista para armazenar a ordem correta das pecas para referência
    ordem_correta = []

    # Loop duplo para iterar através de uma grade 3x3
    for i in range(3):  # 'i' é o índice da coluna
        for j in range(3):  # 'j' é o índice da linha
            
            # Cria uma superfície Pygame para a peca do quebra-cabeça
            # A função subsurface cria uma nova superfície que referencia uma porção da imagem original
            # pygame.Rect define a área da imagem original que será usada para a peca
            # (i*TAMANHO_BLOCO_LARGURA, j*TAMANHO_BLOCO_ALTURA) é o canto superior esquerdo da peca
            # (TAMANHO_BLOCO_LARGURA, TAMANHO_BLOCO_ALTURA) são a largura e altura da peca
            peca = imagem.subsurface(pygame.Rect(i * TAMANHO_BLOCO_LARGURA,
                                                 j * TAMANHO_BLOCO_ALTURA, 
                                                 TAMANHO_BLOCO_LARGURA, 
                                                 TAMANHO_BLOCO_ALTURA))

            # Adiciona a peca à lista ordem_correta com suas coordenadas de grade (i, j)
            # Isso é usado para verificar a solução do quebra-cabeça mais tarde
            ordem_correta.append((i, j, peca))

    # Faz uma cópia da lista ordem_correta para pecas
    # Isso é necessário para embaralhar as pecas sem alterar a lista de ordem correta
    pecas = ordem_correta.copy()

    # Embaralha a lista de pecas para iniciar o jogo com um quebra-cabeça misturado
    # A função shuffle do módulo random reorganiza os elementos da lista de pecas em uma ordem aleatória
    random.shuffle(pecas)


    # Inicializa a variável 'selecionado' como None. 
    # Esta variável será usada para manter o índice da peca do quebra-cabeça que o
    # jogador selecionou para mover
    selecionado = None
    
    # Inicializa a variável 'jogo_terminado' como False. 
    # Este é um indicador de estado para controlar o loop de jogo principal - 
    # o jogo continua rodando enquanto 'jogo_terminado' for False
    jogo_terminado = False
    
    # Inicia o loop de jogo principal. Este loop continuará até que 'jogo_terminado' seja True
    while not jogo_terminado:
        
        # Itera sobre e processa todos os eventos da fila de eventos do Pygame
        for evento in pygame.event.get():
            
            # Verifica se o evento atual é um evento de QUIT (geralmente gerado
            # quando a janela do jogo é fechada)
            if evento.type == pygame.QUIT:
                
                # Chama a função quit do Pygame para terminar todos os módulos do
                # Pygame de forma limpa
                pygame.quit()
                
                # Chama sys.exit para encerrar o programa imediatamente
                sys.exit()

            # Verifica se o evento capturado é um evento de clique do mouse
            if evento.type == pygame.MOUSEBUTTONDOWN:
                
                # Caso seja, obtém as coordenadas x e y do clique do mouse na tela
                x, y = pygame.mouse.get_pos()
                
                # Calcula o índice da peca que foi clicada baseando-se nas posições x e y do clique
                # Primeiro, a posição x é dividida pela largura de um bloco, para determinar a coluna da peca
                # A posição y é dividida pela altura de um bloco, para determinar a linha da peca
                # Como a grade do quebra-cabeça é 3x3, multiplica-se a linha por 3 e soma-se a coluna para obter
                # o índice linear da peca
                index = x // TAMANHO_BLOCO_LARGURA + (y // TAMANHO_BLOCO_ALTURA) * 3
                
                # A variável 'selecionado' é atualizada para referenciar o índice da peca que o jogador quer mover
                # Este índice será usado mais tarde para trocar a peca selecionada com 
                # outra peca quando o jogador clicar em uma segunda posição
                selecionado = index

            # Verifica se o evento capturado é um evento de soltura do botão do mouse
            if evento.type == pygame.MOUSEBUTTONUP:
                
                # Antes de processar a soltura do botão, verifica se uma peca foi 
                # previamente selecionada (não é None)
                if selecionado is not None:
                    
                    # Obtém as coordenadas x e y da posição onde o botão do mouse foi solto
                    x, y = pygame.mouse.get_pos()
                    
                    # Calcula o índice da peca na qual o botão do mouse foi solto, similar ao evento de MOUSEBUTTONDOWN
                    # Isso é feito para determinar a nova posição da peca que o jogador deseja mover
                    index = x // TAMANHO_BLOCO_LARGURA + (y // TAMANHO_BLOCO_ALTURA) * 3
                    
                    # Troca a peca que foi selecionada com a peca na posição onde o botão do mouse foi solto
                    # 'selecionado' é o índice da peca selecionada e 'index' é o índice da posição de soltura
                    # Esta operação efetivamente move a peca no quebra-cabeça
                    pecas[selecionado], pecas[index] = pecas[index], pecas[selecionado]
                    
                    # Reinicializa a variável 'selecionado' para None para permitir nova seleção de peca
                    selecionado = None
                
                
        # Preenche a tela inteira com a cor branca definida pela constante BRANCO.
        # Isso limpa a tela de qualquer conteúdo anterior, agindo como um 'reset' visual para o próximo frame.
        # Essa ação é comum em jogos para evitar que desenhos anteriores afetem a aparência atual da tela.
        tela.fill(BRANCO)
        
        
        desenhar_quebra_cabeca()


        # Atualiza a tela para refletir todos os desenhos realizados desde a última vez que este comando foi executado.
        # O método 'flip' do Pygame faz com que tudo que foi desenhado em 'buffer' oculto seja exibido na tela.
        # Isso cria uma transição suave de frames e é uma prática padrão para evitar 'flickering' ou 'tearing' na animação.
        pygame.display.flip()
        