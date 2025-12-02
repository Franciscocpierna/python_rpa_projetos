# Importa a biblioteca Pygame usada para desenvolvimento de jogos
import pygame

# Importa a biblioteca random para geração de números aleatórios
import random

# Importa a biblioteca time para operações relacionadas a tempo
import time

# Inicializa todos os módulos internos da biblioteca Pygame,
        # necessários para o funcionamento dos jogos
pygame.init()

# Define as dimensões da tela do jogo
LARGURA, ALTURA = 600, 700

# Cria uma janela gráfica com as dimensões definidas anteriormente
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela do jogo
pygame.display.set_caption("Jogo de Seleção de Frutas Iguais")

# Define a cor branca em formato RGB
BRANCO = (255, 255, 255)

# Define a cor vermelha em formato RGB
VERMELHO = (255, 0, 0)

# Define a cor preta em formato RGB
PRETO = (0, 0, 0)

# Define a cor verde em formato RGB
VERDE = (0, 255, 0)

# Define a cor azul usada para mensagens em formato RGB
AZUL = (0, 0, 255)

# Define a taxa de quadros por segundo (FPS) do jogo
fps = 30

# Cria um objeto de relógio para controlar a
        # atualização da tela e manter o FPS
relogio = pygame.time.Clock()

# Define o número inicial de vidas do jogador
vidas = 3

# Inicializa a pontuação do jogador como zero
pontuacao = 0

# Define a fase inicial do jogo como 1
fase = 1

# Define o número de frutas que devem ser
        # selecionadas para passar de fase
objetivo_fase = 20

# Inicializa o contador de frutas coletadas
        # na fase atual como zero
coletadas_na_fase = 0

# Define o limite de tempo de 60 segundos por fase
tempo_limite = 60

# Lista de nomes de arquivos de imagens de
        # frutas a serem carregadas
imagens_frutas = ["fruta1.png", "fruta2.png", "fruta3.png", "fruta4.png", "fruta5.png"]

# Associar cada tipo de fruta ao índice de sua imagem
        # na lista, para uso posterior em lógicas de seleção
try:
    
    # Carrega todas as imagens listadas, converte-as para um 
            # formato com canal alfa (transparência)
    frutas = [pygame.image.load(img).convert_alpha() for img in imagens_frutas]
    
except pygame.error as e:
    
    # Imprime uma mensagem de erro caso alguma imagem 
            # não possa ser carregada
    print(f"Erro ao carregar imagens de frutas: {e}")
    
    # Finaliza o Pygame de forma limpa
    pygame.quit()
    
    # Sai do programa
    exit()

# Define o tamanho padrão para as frutas 
        # dentro da grade do jogo
tamanho_fruta = 50

# Redimensiona todas as imagens de frutas para
        # terem o tamanho uniforme
for i in range(len(frutas)):
    frutas[i] = pygame.transform.scale(frutas[i], (tamanho_fruta, tamanho_fruta))

# Define a quantidade de linhas na grade do jogo
grade_linhas = 8

# Define a quantidade de colunas na grade do jogo
grade_colunas = 8

# Define o espaço entre as frutas na grade para
        # evitar sobreposição visual
espacamento = 10  # Espaço em pixels entre as frutas

# Inicializa uma lista para armazenar informações sobre a
        # posição e estado de cada fruta na grade
posicoes_frutas = []

# Inicializa uma variável para armazenar o tipo de fruta que o
        # jogador está atualmente selecionando
tipo_atual = None


# Define uma função para atualizar e desenhar elementos gráficos
        # na tela do jogo. O parâmetro 'tempo_restante' indica quanto
        # tempo falta para a fase acabar.
def desenhar_interface(tempo_restante):
    
    # Limpa a tela, preenchendo tudo com branco. Isso remove qualquer
            # desenho anterior, garantindo que nada antigo apareça na
            # nova atualização da tela.
    tela.fill(BRANCO)
    
    # Configura a fonte (estilo e tamanho de letra) que será usada para
            # escrever texto na tela. 'None' usa a fonte padrão do
            # Pygame e '30' é o tamanho da fonte.
    fonte = pygame.font.SysFont(None, 30)
    
    # Renderiza (cria) um texto que mostra quantas vidas o jogador 
            # ainda tem. 'True' significa que o texto será 
            # antialiasing (suavizado), e 'VERMELHO' é a cor do texto.
    texto_vidas = fonte.render(f'Vidas: {vidas}', True, VERMELHO)
    
    # Renderiza um texto que mostra a pontuação atual do jogador, usando a cor preta.
    texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, PRETO)
    
    # Renderiza um texto que indica em que fase o jogo está, também em preto.
    texto_fase = fonte.render(f'Fase: {fase}', True, PRETO)
    
    # Renderiza um texto mostrando o tempo restante na fase, em vermelho.
    texto_tempo = fonte.render(f'Tempo: {tempo_restante}s', True, VERMELHO)
    
    # Renderiza um texto que mostra quantas frutas já foram coletadas na
            # fase atual em relação ao total necessário, usando a cor verde.
    texto_coletadas = fonte.render(f'Coletadas: {coletadas_na_fase}/{objetivo_fase}', True, VERDE)
    
    # Coloca o texto das vidas na tela na posição x=10, y=10.
    tela.blit(texto_vidas, (10, 10))
    
    # Coloca o texto da pontuação na tela um pouco 
            # abaixo do texto das vidas.
    tela.blit(texto_pontuacao, (10, 50))
    
    # Coloca o texto da fase ainda mais abaixo.
    tela.blit(texto_fase, (10, 90))
    
    # Coloca o texto das frutas coletadas ainda mais abaixo.
    tela.blit(texto_coletadas, (10, 130))
    
    # Coloca o texto do tempo restante no canto superior direito da tela.
    tela.blit(texto_tempo, (LARGURA - 150, 10))
    
    # O loop 'for' começa percorrendo cada item na lista 'posicoes_frutas'.
            # Cada item nesta lista é um dicionário contendo detalhes
            # de uma fruta específica.
    for fruta_info in posicoes_frutas:
        
        # 'fruta_info' é um dicionário que contém informações como
                # tipo de fruta, imagem da fruta, sua posição na
                # tela e se está selecionada.
        # Aqui, acessamos a imagem da fruta armazenada na
                # chave 'imagem' do dicionário.
        fruta = fruta_info['imagem']
        
        # Aqui, acessamos a posição da fruta armazenada na 
                # chave 'posicao' do dicionário. 
        # Essa posição é uma tupla contendo coordenadas x e y.
        pos = fruta_info['posicao']
        
        # Aqui, verificamos o estado de seleção da fruta, 
                # armazenado na chave 'selecionada' do dicionário.
        # Esse valor é um booleano, True se a fruta estiver 
                # selecionada e False caso contrário.
        selecionada = fruta_info['selecionada']
        
        # Se a fruta estiver selecionada, uma borda será desenhada ao 
                # redor da fruta para indicar visualmente que ela foi 
                # selecionada pelo jogador.
        # 'pygame.draw.rect' desenha um retângulo (neste caso, uma borda).
        # 'tela' é o objeto de superfície onde estamos desenhando.
        # 'VERMELHO' é a cor da borda.
        # '(pos[0]-2, pos[1]-2, tamanho_fruta+4, tamanho_fruta+4)' define a
                # posição e tamanho do retângulo. O retângulo é desenhado 
                # ligeiramente maior que a fruta (2 pixels a mais de 
                # cada lado) para formar a borda.
        # '4' é a espessura da borda em pixels.
        if selecionada:
            pygame.draw.rect(tela, VERMELHO, (pos[0]-2, pos[1]-2, tamanho_fruta+4, tamanho_fruta+4), 4)
        
        # Finalmente, desenhamos a imagem da fruta na tela na
                # posição especificada. 
        # 'tela.blit' é o método que copia o conteúdo de uma
                # imagem para outra superfície.
        # 'fruta' é a superfície da imagem da fruta que queremos desenhar.
        # 'pos' são as coordenadas (x, y) na tela onde a 
                # imagem da fruta será colocada.
        tela.blit(fruta, pos)


    # Atualiza a tela para mostrar todos os elementos que foram desenhados. 
    # Isso efetivamente faz com que tudo que foi programado 
            # acima apareça para o jogador.
    pygame.display.flip()



# Define uma função chamada 'gerar_frutas' que não recebe parâmetros 
            # e é responsável por popular a grade do jogo com frutas aleatórias.
def gerar_frutas():
    
    # Limpa a lista 'posicoes_frutas' para remover quaisquer frutas
            # que possam ter sido geradas anteriormente.
    posicoes_frutas.clear()
    
    # Calcula a margem horizontal para que as frutas fiquem centralizadas na tela. 
    # Isso é feito subtraindo a largura total ocupada pelas frutas e
            # espaços entre elas da largura total da tela e dividindo por 2.
    margem_x = (LARGURA - (grade_colunas * tamanho_fruta + (grade_colunas - 1) * espacamento)) // 2
    
    # Define um espaço fixo no topo da tela para exibição de informações do 
            # jogo como pontuação e tempo, deixando espaço suficiente 
            # para isso antes de começar a posicionar as frutas.
    margem_y = 150  
    
    # Executa um loop que percorre cada linha da grade onde 
            # as frutas serão posicionadas.
    for linha in range(grade_linhas):
        
        # Dentro de cada linha, percorre cada coluna onde uma 
                # fruta será posicionada.
        for coluna in range(grade_colunas):
        
            # Gera um número aleatório entre 0 e o número de tipos de frutas menos um.
            # Este número será usado para selecionar uma fruta da lista de imagens.
            tipo = random.randint(0, len(frutas) - 1)
            
            # Seleciona a imagem da fruta correspondente ao
                    # número aleatório gerado.
            fruta = frutas[tipo]
            
            # Calcula a posição x da fruta atual. Esta posição é determinada pela 
                    # margem horizontal, mais o índice da coluna multiplicado pela
                    # soma do tamanho da fruta e o espaço entre as frutas.
            x = margem_x + coluna * (tamanho_fruta + espacamento)
            
            # Calcula a posição y da fruta atual. Similar ao cálculo
                    # de x, mas usando o índice da linha.
            y = margem_y + linha * (tamanho_fruta + espacamento)
            
            # Adiciona um dicionário representando a fruta à lista 'posicoes_frutas'. 
            # Este dicionário contém o tipo da fruta, sua imagem, sua 
                    # posição e um estado 'selecionada' inicialmente definido como False.
            posicoes_frutas.append({
                'tipo': tipo,
                'imagem': fruta,
                'posicao': (x, y),
                'selecionada': False
            })



# Define uma função que substitui as frutas que foram 
        # selecionadas por novas frutas aleatórias.
# O parâmetro 'selecionados' contém uma lista de dicionários, 
        # cada um representando uma fruta que foi selecionada pelo jogador.
def substituir_frutas_selecionadas(selecionados):
    
    # O loop percorre cada fruta dentro da lista 'selecionados'.
    for fruta_info in selecionados:
        
        # Gera um número aleatório entre 0 e o número total de frutas
                # disponíveis menos um. Este número será usado para
                # selecionar uma nova fruta aleatoriamente.
        tipo = random.randint(0, len(frutas) - 1)
        
        # Seleciona uma nova imagem de fruta da lista de imagens
                # baseada no número aleatório gerado.
        fruta = frutas[tipo]
        
        # Atualiza o tipo da fruta no dicionário 'fruta_info' 
                # com o novo tipo aleatório.
        fruta_info['tipo'] = tipo
        
        # Atualiza a imagem no dicionário 'fruta_info' com a
                # nova imagem de fruta.
        fruta_info['imagem'] = fruta
        
        # Reseta o estado de seleção da fruta para False, indicando 
                # que ela não está mais selecionada.
        fruta_info['selecionada'] = False


# Define uma função para recarregar todas as frutas na grade.
# Essa função pode ser usada em caso de erro ou quando é 
        # necessário reiniciar o posicionamento das frutas.
def recarregar_todas_as_frutas():
    
    # Chama a função 'gerar_frutas' para criar uma nova
            # grade de frutas aleatórias.
    gerar_frutas()


# Define uma função chamada 'exibir_mensagem', utilizada para
        # mostrar mensagens na tela por um tempo limitado.
# 'texto' é o conteúdo da mensagem a ser exibida.
# 'cor' define a cor do texto.
# 'tempo_duracao' é um parâmetro opcional que determina quantos 
        # segundos a mensagem será exibida. O padrão é 2 segundos.
def exibir_mensagem(texto, cor, tempo_duracao=2):
    
    # Cria uma nova fonte usando a fonte padrão do sistema com tamanho 50.
    fonte = pygame.font.SysFont(None, 50)
    
    # Renderiza o texto em uma superfície. 'True' ativa o suavizado (antialiasing) 
            # do texto, que faz com que o texto pareça menos "pixelizado".
    texto_render = fonte.render(texto, True, cor)
    
    # Limpa a tela, preenchendo-a completamente com a cor branca. Isso é feito para 
            # remover quaisquer desenhos antigos antes de mostrar a nova mensagem.
    tela.fill(BRANCO)
    
    # 'blit' é um método que desenha uma superfície sobre outra. 
    # Neste caso, desenha o texto renderizado na tela.
    # A posição x é calculada para centralizar o texto horizontalmente: 
            # calcula-se a metade da largura da tela e subtrai-se a
            # metade da largura do texto.
    # A posição y é calculada para centralizar o texto verticalmente: 
            # calcula-se a metade da altura da tela e subtrai-se a 
            # metade da altura do texto.
    tela.blit(texto_render, (
        LARGURA // 2 - texto_render.get_width() // 2, 
        ALTURA // 2 - texto_render.get_height() // 2
    ))
    
    # Atualiza a tela inteira para mostrar a mensagem.
    pygame.display.flip()
    
    # Pausa a execução do programa pelo tempo especificado em segundos,
            # multiplicado por 1000 para converter em milissegundos, o
            # que é necessário para o método 'delay'.
    pygame.time.delay(tempo_duracao * 1000)


# Define uma função chamada 'fim_do_jogo' que não recebe parâmetros e é
        # usada para exibir a tela de encerramento do jogo.
def fim_do_jogo():
    
    # Limpa a tela, preenchendo tudo com a cor branca. Isso remove
            # qualquer conteúdo anterior, preparando a tela para 
            # novos elementos gráficos.
    tela.fill(BRANCO)
    
    # Cria uma nova fonte com tamanho 72, que será usada para 
            # exibir o texto na tela. A fonte é a padrão do sistema.
    fonte = pygame.font.SysFont(None, 72)
    
    # Renderiza o texto "Fim do Jogo!" usando a cor vermelha.
    # O parâmetro 'True' ativa o suavizado do texto, tornando-o mais legível.
    texto_fim = fonte.render("Fim do Jogo!", True, VERMELHO)
    
    # Renderiza o texto mostrando a pontuação final do jogador, usando a cor preta.
    texto_pontuacao_final = fonte.render(f'Pontuação Final: {pontuacao}', True, PRETO)
    
    # Desenha o texto "Fim do Jogo!" na tela. O texto é centralizado 
            # horizontalmente e posicionado um pouco acima do 
            # centro vertical da tela.
    # Calcula-se a posição x subtraindo metade da largura do
            # texto da metade da largura da tela.
    # A posição y é ajustada para 50 pixels acima do
            # centro vertical da tela.
    tela.blit(
        texto_fim, 
        (LARGURA // 2 - texto_fim.get_width() // 2, ALTURA // 2 - 50)
    )
    
    # Desenha o texto da pontuação final na tela, abaixo do 
            # texto "Fim do Jogo!".
    # Similar ao posicionamento do texto "Fim do Jogo!", mas o 
            # texto é posicionado 50 pixels abaixo do centro vertical.
    tela.blit(
        texto_pontuacao_final, 
        (LARGURA // 2 - texto_pontuacao_final.get_width() // 2, ALTURA // 2 + 50)
    )
    
    # Atualiza a tela para mostrar os textos que foram desenhados.
    pygame.display.flip()
    
    # Pausa o jogo por 3000 milissegundos (ou 3 segundos), permitindo 
            # que o jogador leia a mensagem de encerramento antes de
            # o jogo fechar ou retornar ao menu principal.
    pygame.time.delay(3000)


# Define a função principal do jogo que controla o fluxo geral, 
        # incluindo o início da partida, a lógica de jogo e o fim do jogo.
def jogo():
    
    # Declara que as variáveis a seguir são globais, o que permite 
            # que elas sejam modificadas dentro desta função.
    global vidas, pontuacao, fase, objetivo_fase, coletadas_na_fase, tempo_limite, tipo_atual
    
    # Chama a função para gerar uma nova grade de frutas
            # aleatórias no início do jogo.
    gerar_frutas()
    
    # Registra o tempo de início da fase em segundos desde a
            # época (usualmente 1 de janeiro de 1970).
    inicio_tempo = time.time()
    
    # Define a variável 'rodando' como True, que controla o loop 
            # principal do jogo. Enquanto 'rodando' for True, o jogo continua executando.
    rodando = True
    
    # Inicia um loop que continuará enquanto 'rodando' for True.
    while rodando:
        
        # Limita a taxa de atualizações (ou quadros) por segundo (FPS)
                # para manter o jogo rodando de forma suave e consistente.
        relogio.tick(fps)
        
        # Calcula o tempo restante na fase atual. 'max' garante que o tempo
                # não fique negativo. Subtrai o tempo atual desde a época 
                # do 'inicio_tempo' para obter o tempo decorrido e 
                # subtrai isso do 'tempo_limite'.
        tempo_restante = max(0, tempo_limite - int(time.time() - inicio_tempo))

        
        # Inicia um loop que verifica todos os eventos que ocorrem 
                # durante o jogo, como cliques de mouse e fechamento da janela.
        for evento in pygame.event.get():
        
            # Verifica se o tipo do evento é QUIT, que ocorre geralmente 
                    # quando o usuário clica no botão de fechar a janela.
            if evento.type == pygame.QUIT:
            
                # Se o evento for QUIT, define a variável 'rodando' como 
                        # False, o que terminará o loop principal e encerrará o jogo.
                rodando = False
            
            # Verifica se o tipo do evento é MOUSEBUTTONDOWN, que ocorre
                    # quando o usuário clica em algum botão do mouse.
            elif evento.type == pygame.MOUSEBUTTONDOWN:
            
                # Obtém as posições x e y do cursor do mouse no momento do clique.
                x, y = pygame.mouse.get_pos()
                
                # Inicializa a variável 'fruta_clicada' como None. Esta variável 
                        # será usada para armazenar informações sobre a fruta 
                        # que foi clicada, se houver alguma.
                fruta_clicada = None
                
                # Inicia um loop que percorre cada fruta na lista 'posicoes_frutas' 
                        # para verificar se alguma fruta foi clicada.
                for fruta_info in posicoes_frutas:
                
                    # Obtém a posição da fruta atual.
                    pos = fruta_info['posicao']
                    
                    # Cria um retângulo que representa a área ocupada pela fruta na tela.
                    rect = pygame.Rect(pos[0], pos[1], tamanho_fruta, tamanho_fruta)
                    
                    # Verifica se o ponto onde o mouse foi clicado (x, y) está dentro 
                            # do retângulo da fruta e se a fruta não está
                            # atualmente selecionada.
                    if rect.collidepoint(x, y) and not fruta_info['selecionada']:
                    
                        # Se o clique foi na fruta e ela não está selecionada, armazena 
                                # as informações da fruta na variável 'fruta_clicada'.
                        fruta_clicada = fruta_info
                        
                        # Sai do loop assim que a fruta clicada for encontrada, evitando 
                                # verificações desnecessárias das outras frutas.
                        break

                
                # Verifica se alguma fruta foi clicada.
                if fruta_clicada:
                    
                    # Verifica se é a primeira fruta a ser selecionada na rodada atual.
                    if tipo_atual is None:
                        
                        # Se nenhuma fruta foi selecionada anteriormente, a fruta
                                # clicada define o tipo para a seleção atual.
                        tipo_atual = fruta_clicada['tipo']
                        
                        # Marca a fruta clicada como selecionada.
                        fruta_clicada['selecionada'] = True
                        
                        # Aumenta a pontuação do jogador por selecionar uma fruta.
                        pontuacao += 1
                        
                        # Contabiliza a fruta como coletada na contagem da fase atual.
                        coletadas_na_fase += 1
                        
                    # Verifica se o tipo da fruta clicada corresponde ao tipo da 
                            # fruta que já estava sendo selecionado.
                    elif fruta_clicada['tipo'] == tipo_atual:
                        
                        # Se a fruta clicada é do mesmo tipo, ela é marcada como 
                                # selecionada, continuando a sequência de seleção.
                        fruta_clicada['selecionada'] = True
                        
                        # Aumenta novamente a pontuação, já que o jogador continua
                                # selecionando frutas corretamente.
                        pontuacao += 1
                        
                        # Incrementa o contador de frutas coletadas para a fase.
                        coletadas_na_fase += 1
                        
                    # Caso a fruta clicada não corresponda ao tipo atualmente 
                            # selecionado, indica uma seleção errada.
                    else:
                        
                        # Penaliza o jogador diminuindo a pontuação por um erro.
                        # A função 'max' garante que a pontuação não fique negativa.
                        pontuacao = max(pontuacao - 1, 0)
                        
                        # Reduz uma vida do jogador devido ao erro. A função 'max' 
                                # assegura que o número de vidas não fique negativo.
                        vidas = max(vidas - 1, 0)
                        
                        # Exibe uma mensagem de erro, alertando que tipos diferentes 
                                # foram selecionados.
                        print("Selecionou uma fruta de tipo diferente! Todas as frutas serão recarregadas.")
                        
                        # Chama a função que exibe uma mensagem temporária na tela com o
                                # texto "Erro! Tipo Diferente." e a cor vermelha.
                        exibir_mensagem("Erro! Tipo Diferente.", VERMELHO, tempo_duracao=2)
                        
                        # Recarrega todas as frutas para reiniciar a seleção,
                                # limpando a seleção atual.
                        recarregar_todas_as_frutas()
                        
                        # Reseta o tipo de fruta selecionado para permitir uma nova seleção.
                        tipo_atual = None
                        
                        # Verifica se o jogador ainda possui vidas após o erro.
                        if vidas == 0:
                            
                            # Se não restarem vidas, o jogo é encerrado.
                            rodando = False
                            
                            # Sai do loop para evitar múltiplas penalidades ou 
                                    # processamento adicional.
                            break
                            
                        else:
                            
                            # Se ainda houver vidas, apenas sai do loop de seleção para 
                                    # evitar múltiplas penalidades no mesmo clique.
                            break

                
                # Verifica se o número de frutas coletadas durante a fase atual é 
                        # igual ou superior ao objetivo estabelecido para a fase.
                if coletadas_na_fase >= objetivo_fase:
                    
                    # Caso a meta seja atingida, exibe uma mensagem indicando que a 
                            # fase foi completada. A mensagem é exibida em azul e dura 2 segundos.
                    exibir_mensagem("Fase Completa!", AZUL, tempo_duracao=2)
                    
                    # Incrementa o número da fase atual, movendo o jogador 
                            # para a próxima fase do jogo.
                    fase += 1
                    
                    # Aumenta o objetivo de frutas a serem coletadas para a 
                            # próxima fase, adicionando 10 frutas ao objetivo anterior.
                    objetivo_fase += 10
                    
                    # Reseta o contador de frutas coletadas para zero, para
                            # começar a contar novamente na próxima fase.
                    coletadas_na_fase = 0
                    
                    # Define o tempo limite de cada fase para 60 segundos novamente, 
                            # garantindo que cada nova fase comece com o tempo completo.
                    tempo_limite = 60
                    
                    # Registra o momento em que a nova fase começa, para começar a 
                            # contagem do tempo limite a partir deste ponto.
                    inicio_tempo = time.time()
                    
                    # Gera uma nova disposição de frutas na tela, para que o jogador
                            # tenha novos desafios na próxima fase.
                    gerar_frutas()
                    
                    # Reseta a variável 'tipo_atual', que é usada para verificar 
                            # se o jogador está selecionando frutas do mesmo tipo.
                    # Isso evita que seleções da fase anterior interfiram na nova fase.
                    tipo_atual = None
                    
                    # Exibe uma mensagem na tela informando que uma nova fase começou, 
                            # também em azul e com duração de 2 segundos.
                    exibir_mensagem(f"Fase {fase} Iniciada!", AZUL, tempo_duracao=2)
                    
                    # Continua o loop principal do jogo. O uso de 'continue' faz com 
                            # que o loop salte para o próximo ciclo, recomeçando o 
                            # processamento de eventos e atualizações do jogo.
                    continue

                
                # Verifica se uma fruta foi clicada e se há um tipo de 
                        # fruta atualmente sendo coletado.
                if fruta_clicada and tipo_atual is not None:
                    
                    # Usa a função 'all()' para verificar se todas as frutas do 
                            # tipo atual foram selecionadas.
                    # 'all()' retornará True se todos os elementos do iterável forem
                            # verdadeiros. O iterável é gerado por uma expressão geradora
                            # que percorre todas as frutas e verifica se cada uma 
                            # delas que corresponde ao tipo atual está selecionada.
                    todas_selecionadas = all(
                        fruta_info['selecionada'] 
                        for fruta_info in posicoes_frutas 
                        if fruta_info['tipo'] == tipo_atual
                    )
                    
                    # Se todas as frutas do tipo especificado foram selecionadas:
                    if todas_selecionadas:
                        
                        # Registra no console do servidor ou no terminal que 
                                # todas as frutas desse tipo foram selecionadas.
                        print(f"Todas as frutas do tipo {tipo_atual} foram selecionadas!")
                        
                        # Cria uma lista das frutas que estão atualmente selecionadas e 
                                # correspondem ao tipo atual.
                        # Isso é feito por uma compreensão de lista que 
                                # filtra 'posicoes_frutas' para encontrar todas as frutas
                                # que são do 'tipo_atual' e estão selecionadas.
                        selecionados = [
                            fruta_info for fruta_info in posicoes_frutas 
                            if fruta_info['tipo'] == tipo_atual and fruta_info['selecionada']
                        ]
                        
                        # Chama a função 'substituir_frutas_selecionadas' passando a 
                                # lista de frutas selecionadas.
                        # Esta função substitui essas frutas por novas frutas
                                # aleatórias, reiniciando o processo de seleção
                                # para o tipo de fruta em questão.
                        substituir_frutas_selecionadas(selecionados)
                        
                        # Reseta 'tipo_atual' para None, indicando que não há 
                                # mais um tipo específico sendo coletado,
                                # permitindo ao jogador começar a selecionar um
                                # novo tipo na próxima interação.
                        tipo_atual = None
                        
                        # Incrementa a pontuação do jogador por ter completado 
                                # uma seleção completa de todas as frutas de um tipo.
                        # Adiciona um bônus de 5 pontos, reconhecendo o 
                                # sucesso na coleta focada.
                        pontuacao += 5  # Por exemplo, 5 pontos extras
                        

        # Verifica se o tempo restante para completar a fase chegou a zero.
        if tempo_restante == 0:
        
            # Reduz uma vida do jogador porque o tempo para completar a fase expirou. 
            # A função 'max' garante que o número de vidas não fique negativo.
            vidas = max(vidas - 1, 0)
        
            # Verifica se o jogador ainda tem vidas restantes após perder 
                    # uma vida devido ao tempo esgotado.
            if vidas > 0:
            
                # Exibe uma mensagem informando que o tempo para a fase acabou, 
                        # usando a cor vermelha na mensagem e mostrando por 2 segundos.
                exibir_mensagem("Tempo Esgotado!", VERMELHO, tempo_duracao=2)
                
                # Registra o momento atual como o novo tempo de início para a nova 
                        # tentativa na mesma fase, reiniciando o contador de tempo.
                inicio_tempo = time.time()
                
                # Reseta o contador de frutas coletadas para a fase, já que a 
                        # fase será reiniciada.
                coletadas_na_fase = 0
                
                # Gera novamente as frutas na tela, oferecendo ao jogador uma 
                        # nova chance de completar a fase com uma nova 
                        # configuração de frutas.
                gerar_frutas()
                
                # Reseta o tipo atual de fruta que estava sendo coletado,
                        # permitindo que o jogador comece a coletar qualquer 
                        # tipo de fruta novamente.
                tipo_atual = None
                
                # Imprime uma mensagem no console indicando que as frutas foram 
                        # recarregadas e a fase reiniciada devido ao esgotamento do tempo.
                print("Tempo esgotado! Recarregando as frutas para a mesma fase.")
                
            else:
                
                # Se não restarem vidas, exibe uma mensagem de "Fim do Jogo" em 
                        # vermelho por 2 segundos, indicando o término da partida.
                exibir_mensagem("Fim do Jogo!", VERMELHO, tempo_duracao=2)
                
                # Define a variável 'rodando' como False, o que causará a saída do
                        # loop principal do jogo e, consequentemente, o encerramento do jogo.
                rodando = False
        
        # Chama a função 'desenhar_interface' passando o tempo restante como 
                # argumento para atualizar os elementos visuais na tela, 
                # como o contador de tempo e pontuação.
        desenhar_interface(tempo_restante)

# Função para iniciar o jogo, colocando todas as 
        # lógicas descritas em prática.
jogo()

# Após o loop do jogo ser encerrado, chama a 
        # função 'fim_do_jogo' para exibir a tela final.
fim_do_jogo()

# Encerra todos os módulos do Pygame e libera os recursos,
        # finalizando completamente o jogo.
pygame.quit()