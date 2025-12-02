# Importa a biblioteca pygame para manipulação de
        # eventos, gráficos e jogos.
import pygame

# Importa a biblioteca random para geração de números aleatórios.
import random

# Importa a biblioteca time para manipulação de tempo (ex.: delays).
import time

# Importa a biblioteca tkinter para criar interfaces gráficas.
import tkinter as tk

# Importa a função messagebox da biblioteca tkinter 
        # para exibir caixas de diálogo.
from tkinter import messagebox

# Importa a classe Counter da biblioteca collections para 
        # contar elementos em uma lista.
from collections import Counter

# Inicializa o módulo pygame, preparando a biblioteca para uso.
pygame.init()

# Cria uma janela oculta do tkinter para ser usada em pop-ups de alerta.
tela_inicial = tk.Tk()
tela_inicial.withdraw()

# Define as dimensões da janela do jogo.
LARGURA, ALTURA = 400, 600

# Configura a janela do jogo com a largura e altura definidas.
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela do jogo.
pygame.display.set_caption("Exercício - Jogo de Bolhas com Letras")

# Define as cores utilizadas no jogo como tuplas RGB.
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CORES_BOLHAS = [(34, 177, 76), (237, 28, 36), (0, 162, 232), (163, 73, 164), (255, 127, 39)]
AZUL_CLARO = (173, 216, 230)
VERMELHO = (237, 28, 36)
CINZA_CLARO = (200, 200, 200)

# Configura as fontes para texto no jogo usando Arial,
        # com tamanhos específicos.
fonte_letra = pygame.font.SysFont("arial", 30)
fonte_info = pygame.font.SysFont("arial", 20)

# Define uma lista de palavras que serão usadas no jogo.
palavras = ["CALA", "CASA", "MOLHO", "DANÇA", "CATIVA", "BALANÇO", "PROVAÇÃO", "ALEGRIA", "COMPORTO", "EXPECTATIVA",
            "HARMONIA", "FORTALEZA", "SUSTENTAR", "ENCANTADOR", "MOVIMENTO", "CONSOLADOR", "INSPIRADOR", "LUMINOSIDADE",
            "ESTABILIDADE", "RESILIÊNCIA"]


# Função para carregar a pontuação do arquivo
def carregar_pontuacao():
    
    try:
        
        # Tenta abrir o arquivo 'pontuacao.txt' no modo de leitura.
        with open("pontuacao.txt", "r") as arquivo:
            
            # Lê o conteúdo do arquivo, remove espaços em branco
                    # extras e converte para inteiro.
            return int(arquivo.read().strip())
            
    except:
        
        # Caso ocorra algum erro (como o arquivo não existir),
                # retorna 0 como pontuação padrão.
        return 0


# Função para salvar a pontuação no arquivo
def salvar_pontuacao(pontuacao):
    
    # Abre o arquivo 'pontuacao.txt' no modo de escrita.
    with open("pontuacao.txt", "w") as arquivo:
        
        # Converte a pontuação para string e grava no arquivo.
        arquivo.write(str(pontuacao))


# Carrega a pontuação do arquivo para definir a
        # pontuação inicial do jogo.
pontuacao = carregar_pontuacao()

# Calcula a fase do jogo baseando-se na pontuação,
        # cada 10 pontos avançam uma fase.
fase = pontuacao // 10 + 1

# Seleciona a palavra atual baseando-se na pontuação. O índice é
        # calculado com o resto da divisão da pontuação por 10,
        # e então acessa a lista de palavras usando esse índice.
palavra_atual = palavras[pontuacao // 10 % len(palavras)]

# Inicializa uma lista vazia para armazenar as 
        # letras selecionadas pelo jogador.
letras_selecionadas = []

# Define o número inicial de vidas por fase.
vidas = 7

# Inicializa uma lista vazia para armazenar as
        # letras disponíveis nas bolhas.
letras_bolhas = []

# Define a função que seleciona uma palavra da lista de 
        # palavras com base na pontuação atual do jogador.
def escolher_palavra():
    
    # Calcula o índice da palavra na lista 'palavras'. O cálculo 
            # divide a pontuação por 10 e usa o módulo da divisão pelo
            # número de palavras para garantir que o índice 
            # esteja dentro dos limites da lista.
    indice_palavra = pontuacao // 10 % len(palavras)
    
    # Retorna a palavra correspondente ao índice calculado.
    return palavras[indice_palavra]


# Define a função para reiniciar o jogo. Isso configura tudo
            # para começar um novo jogo ou uma nova rodada.
def reiniciar_jogo():
    
    # Usa variáveis globais para que as mudanças aqui 
            # impactem todo o jogo.
    global palavra_atual, letras_selecionadas, bolhas, tempo_inicio, vidas, letras_bolhas
    
    # Escolhe uma nova palavra baseada na pontuação 
            # atual do jogador.
    palavra_atual = escolher_palavra()
    
    # Reinicia a lista de letras que o jogador já 
            # selecionou, começando vazia.
    letras_selecionadas = []
    
    # Cria uma lista inicial de letras que aparecerão nas
            # bolhas, começando com as letras da nova palavra.
    letras_bolhas = list(palavra_atual)
    
    # Cria uma lista de letras que podem ser usadas nas bolhas,
            # mas que não são parte da palavra atual.
    # Isso é feito filtrando o alfabeto para excluir as 
            # letras que já estão na palavra atual.
    letras_possiveis = [letra for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if letra not in palavra_atual]
    
    # Escolhe 5 letras aleatoriamente de 'letras_possiveis'
            # para adicionar variedade às bolhas.
    letras_aleatorias = random.sample(letras_possiveis, 5)
    
    # Adiciona essas letras aleatórias à lista de letras nas bolhas.
    letras_bolhas += letras_aleatorias
    
    # Cria uma nova lista de bolhas, com cada bolha representando 
            # uma letra da lista 'letras_bolhas'.
    # Cada bolha é uma instância da classe Bolha, que tem
            # propriedades como posição e velocidade.
    bolhas = [Bolha(letra) for letra in letras_bolhas]
    
    # Reinicia o contador de tempo para a nova rodada, 
            # marcando o momento atual como início.
    tempo_inicio = time.time()
    
    # Define o número de vidas do jogador para 7, permitindo que o 
            # jogador erre até 6 vezes antes de perder o jogo.
    vidas = 7



# Define uma função chamada 'formatar_palavra' que mostra 
        # visualmente o progresso na adivinhação da palavra.
def formatar_palavra():
    
    # Utiliza o objeto 'Counter' para contar quantas vezes 
            # cada letra foi selecionada pelo jogador.
    contador_selecionadas = Counter(letras_selecionadas)
    
    # Inicializa uma lista vazia chamada 'resultado' que vai conter as 
            # letras adivinhadas e sublinhados para as não adivinhadas.
    resultado = []
    
    # Itera sobre cada letra na 'palavra_atual'.
    for letra in palavra_atual:
        
        # Verifica se a letra atual foi selecionada pelo jogador (ou 
                # seja, está no contador e foi selecionada ao menos uma vez).
        if contador_selecionadas[letra] > 0:
            
            # Se a letra foi adivinhada, adiciona essa letra à lista 'resultado'.
            resultado.append(letra)
            
            # Decrementa o contador para essa letra, indicando que
                    # uma ocorrência dela foi usada.
            contador_selecionadas[letra] -= 1
            
        else:
            
            # Se a letra não foi adivinhada, adiciona um
                    # sublinhado '_' à lista 'resultado'.
            resultado.append('_')
    
    # Junta todos os elementos da lista 'resultado' em uma única 
            # string, com espaços entre eles para melhor visualização.
    # Isso facilita o entendimento de quantas letras há e quais são
            # as posições das letras não adivinhadas.
    return " ".join(resultado)


# Define uma função para verificar se a palavra completa foi
        # corretamente adivinhada pelo jogador.
def checar_palavra():
    
    # Cria um contador que registra quantas vezes cada letra
            # aparece na palavra atual.
    contador_palavra = Counter(palavra_atual)
    
    # Cria outro contador que registra quantas vezes cada
            # letra foi selecionada pelo jogador.
    contador_selecionadas = Counter(letras_selecionadas)
    
    # Itera sobre cada letra única presente na palavra atual.
    for letra in contador_palavra:
        
        # Verifica se a quantidade de vezes que a letra foi selecionada é 
                # menor que a quantidade necessária.
        if contador_selecionadas[letra] < contador_palavra[letra]:
            
            # Se uma letra não foi selecionada vezes suficientes, retorna False,
                    # indicando que a palavra está incompleta.
            return False
    
    # Se todas as letras necessárias foram selecionadas na 
            # quantidade correta, retorna True.
    return True


# Define a classe Bolha, que representa uma bolha individual no jogo.
class Bolha:
    
    # O método construtor __init__ é chamado automaticamente quando 
            # uma nova instância da classe Bolha é criada.
    def __init__(self, letra):
        
        # Armazena a letra que a bolha vai mostrar.
        self.letra = letra
        
        # Define a posição horizontal inicial da bolha aleatoriamente 
                # dentro da largura da tela.
        # O valor é limitado para que a bolha não apareça muito 
                # próxima das bordas.
        self.x = random.randint(50, LARGURA - 50)
        
        # Define a posição vertical inicial da bolha. As bolhas começam 
                # acima do topo da tela (valores negativos),
        # fazendo com que "subam" para dentro da tela.
        self.y = random.randint(-100, -40)
        
        # Define a velocidade de movimento vertical da bolha, escolhida 
                # aleatoriamente entre 3 e 6.
        # Isso determina quão rápido a bolha se move para baixo na tela.
        self.velocidade = random.randint(3, 6)
        
        # Define o raio da bolha. Todas as bolhas terão o mesmo tamanho.
        self.raio = 25
        
        # Escolhe uma cor aleatoriamente de uma lista pré-definida de cores.
        # Isso adiciona variedade visual ao jogo.
        self.cor = random.choice(CORES_BOLHAS)

    # Método para mover a bolha. Este método será chamado em cada 
            # ciclo do jogo para atualizar a posição da bolha.
    def mover(self):
        
        # Aumenta o valor de 'y' pela 'velocidade'. Isso faz a bolha
                # se mover para baixo na tela.
        self.y += self.velocidade


    def desenhar(self):
        
        # Desenha a bolha na tela como um círculo. 'pygame.draw.circle' é
                # usado para desenhar círculos.
        # 'tela' é a superfície na qual o círculo será desenhado.
        # 'self.cor' define a cor do círculo, que é uma propriedade da bolha.
        # '(self.x, self.y)' são as coordenadas do centro do círculo.
        # 'self.raio' é o raio do círculo, definindo o tamanho da bolha.
        pygame.draw.circle(tela, self.cor, (self.x, self.y), self.raio)
        
        # Renderiza a letra para ser exibida dentro da bolha. 'fonte_letra.render'
                # cria uma superfície com o texto.
        # 'self.letra' é a letra a ser renderizada.
        # 'True' habilita o anti-aliasing no texto, o que faz com que
                # as bordas do texto fiquem mais suaves.
        # 'BRANCO' define a cor do texto, que neste caso é branco 
                # para contrastar com a cor da bolha.
        texto = fonte_letra.render(self.letra, True, BRANCO)
        
        # 'tela.blit' desenha a superfície do texto na tela. 'blit' é 
                # um método para desenhar uma superfície sobre outra.
        # '(self.x - texto.get_width() // 2, self.y - texto.get_height() // 2)' 
                # calcula a posição do texto para que ele
        # fique centralizado dentro da bolha. 'texto.get_width()' 
                # e 'texto.get_height()' retornam a largura e a altura
                # da superfície do texto, respectivamente.
        tela.blit(texto, (self.x - texto.get_width() // 2, self.y - texto.get_height() // 2))


    def checar_clique(self, pos):
        
        # Calcula a distância entre o ponto onde o mouse foi
                # clicado e o centro da bolha.
        # 'pos' é uma tupla contendo as coordenadas (x, y) do clique do mouse.
        # 'self.x' e 'self.y' são as coordenadas do centro da bolha.
        # A distância é calculada usando o teorema de Pitágoras, 
                # onde (pos[0] - self.x) é a diferença na direção x,
        # e (pos[1] - self.y) é a diferença na direção y. Elevamos cada
                # diferença ao quadrado, somamos ambos os resultados,
                # e tiramos a raiz quadrada do total para obter a distância.
        distancia = ((pos[0] - self.x) ** 2 + (pos[1] - self.y) ** 2) ** 0.5
        
        # Verifica se a distância calculada é menor que o raio da bolha.
        # Se for menor, significa que o clique do mouse foi dentro da bolha.
        # 'self.raio' é o raio da bolha, e se a distância até o 
                # centro da bolha é menor que o raio, o ponto clicado
                # está dentro da área do círculo da bolha.
        return distancia < self.raio


# Define uma função chamada 'mostrar_palavra_alerta', que é responsável 
        # por informar ao jogador qual é a palavra correta.
def mostrar_palavra_alerta():
    
    # Utiliza a função 'showinfo' do módulo 'messagebox' que faz
            # parte da biblioteca tkinter.
    # 'showinfo' é usado para exibir uma caixa de mensagem de
            # informação, que é uma janela popup simples.
    
    # O primeiro argumento "Palavra Correta" é o título da 
            # janela de mensagem.
    # O segundo argumento é o texto que será exibido na janela. 
            # Aqui, ele informa ao jogador qual era a palavra correta.
    # 'f"A palavra correta é: {palavra_atual}"' é uma string 
            # formatada que inclui o valor da variável 'palavra_atual',
            # que contém a palavra que o jogador estava tentando adivinhar. 
    messagebox.showinfo("Palavra Correta", f"A palavra correta é: {palavra_atual}")


# Define uma função para inicializar as bolhas que
            # aparecerão na tela do jogo.
def inicializar_bolhas():
    
    # Usa a palavra 'global' para indicar que a variável 'letras_bolhas' 
            # será modificada globalmente.
    global letras_bolhas
    
    # Cria uma lista de letras possíveis para as bolhas, excluindo as
            # letras que já estão na palavra atual.
    # Isso evita que as letras da palavra atual sejam super-representadas.
    letras_possiveis = [letra for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if letra not in palavra_atual]
    
    # Seleciona 5 letras aleatoriamente da lista de letras possíveis.
            # Essa seleção adiciona imprevisibilidade e dificuldade.
    letras_aleatorias = random.sample(letras_possiveis, 5)
    
    # Combina as letras da palavra atual com as 5 letras aleatórias 
            # para formar a lista completa de letras que aparecerão nas bolhas.
    letras_bolhas = list(palavra_atual) + letras_aleatorias
    
    # Cria uma lista de objetos 'Bolha', um para cada letra 
            # na lista 'letras_bolhas'.
    # A classe 'Bolha' é definida em outra parte do código e é 
            # responsável por gerenciar as propriedades e 
            # comportamentos das bolhas.
    return [Bolha(letra) for letra in letras_bolhas]


# Chama a função 'inicializar_bolhas()' para criar e configurar
        # todas as bolhas necessárias no jogo.
# Esta função prepara uma lista de bolhas com letras, que 
        # incluem as letras da palavra atual mais cinco letras aleatórias.
# O resultado (lista de objetos 'Bolha') é armazenado na variável 'bolhas'.
bolhas = inicializar_bolhas()

# Define a duração total do tempo de jogo para esta 
        # rodada ou fase em segundos.
# 'tempo_total' é usado para estabelecer um limite de tempo, após o 
        # qual o jogo pode terminar ou avançar para outra fase.
tempo_total = 60

# Armazena o momento atual em que esta parte do código é executada. 
# 'time.time()' retorna o tempo atual em segundos desde a 
        # época (normalmente 1 de janeiro de 1970).
# 'tempo_inicio' é usado para calcular o tempo decorrido e 
        # controlar o tempo restante de jogo.
tempo_inicio = time.time()


# Define a função responsável por desenhar e atualizar o 
        # layout da interface do jogo.
def desenhar_layout():
    
    # Preenche o fundo da tela com uma cor azul clara.
            # Isso define a cor de fundo da tela de jogo.
    tela.fill(AZUL_CLARO)

    # Calcula quanto tempo já passou desde o início da fase atual.
    tempo_decorrido = time.time() - tempo_inicio
    
    # Determina o tempo restante subtraindo o tempo decorrido do 
            # tempo total alocado para a fase.
    tempo_restante = max(0, int(tempo_total - tempo_decorrido))
    
    # Prepara o texto com o tempo restante usando a fonte de 
            # informação, definindo o texto como preto.
    texto_tempo = fonte_info.render(f"Tempo: {tempo_restante}s", True, PRETO)
    
    # Desenha o texto do tempo no canto superior 
            # esquerdo da tela.
    tela.blit(texto_tempo, (10, 10))

    # Prepara o texto da pontuação, fase e vidas restantes 
            # usando a mesma fonte.
    texto_pontuacao = fonte_info.render(f"Pontuação: {pontuacao}  Fase: {fase}  Vidas: {vidas}", True, PRETO)
    
    # Desenha o texto da pontuação no canto superior direito, 
            # ajustando para que fique alinhado à direita.
    tela.blit(texto_pontuacao, (LARGURA - texto_pontuacao.get_width() - 10, 10))

    # Prepara o texto com a palavra que está sendo formada, chamando a 
            # função que formata a palavra com sublinhados.
    texto_palavra = fonte_info.render(f"Palavra: {formatar_palavra()}", True, PRETO)
    
    # Desenha o texto da palavra centralizado na tela, um 
            # pouco abaixo dos outros textos.
    tela.blit(texto_palavra, (LARGURA // 2 - texto_palavra.get_width() // 2, 50))

    # Prepara o botão "Ver Palavra" que pode ser clicado 
            # para revelar a palavra correta.
    botao_texto = fonte_info.render("Ver Palavra", True, PRETO)
    
    # Define o retângulo do botão, posicionando-o na parte inferior da tela.
    botao_retangulo = pygame.Rect(20, ALTURA - 50, 120, 30)
    
    # Desenha o retângulo do botão na tela, usando uma cor cinza claro.
    pygame.draw.rect(tela, CINZA_CLARO, botao_retangulo)
    
    # Desenha o texto do botão dentro do retângulo do botão,
            # ajustando para centralizar o texto no botão.
    tela.blit(botao_texto, (botao_retangulo.x + 10, botao_retangulo.y + 5))

    # Retorna o retângulo do botão para que possa ser 
            # usado para detectar cliques nele.
    return botao_retangulo


# Define uma variável de controle para manter o jogo rodando. 
        # Enquanto 'rodando' for True, o jogo continua.
rodando = True

# Inicia o loop principal do jogo. Este loop se repete 
        # enquanto a variável 'rodando' for True.
while rodando:
    
    # Chama a função 'desenhar_layout' para atualizar a 
            # interface do jogo.
    # Essa função também retorna o retângulo do botão "Ver Palavra",
            # que é usado para detectar cliques.
    botao_ver_palavra = desenhar_layout()

    # Atualiza e desenha cada bolha presente na lista de bolhas.
    # Usa uma cópia da lista 'bolhas[:]' para permitir modificações na
            # lista original durante a iteração.
    for bolha in bolhas[:]:  # Itera sobre uma cópia da lista

        # Move a bolha verticalmente de acordo com sua velocidade.
        bolha.mover()
        
        # Desenha a bolha na tela.
        bolha.desenhar()
        
        # Verifica se a bolha saiu da tela (ou seja, se sua
                # posição 'y' é maior que a altura da tela).
        if bolha.y > ALTURA:
            
            # Se a bolha saiu da tela, ela é removida da lista de bolhas.
            bolhas.remove(bolha)
            
            # Uma nova bolha é criada e adicionada à lista para
                    # substituir a bolha que saiu.
            # A letra para a nova bolha é escolhida aleatoriamente 
                    # da lista 'letras_bolhas'.
            bolhas.append(Bolha(random.choice(letras_bolhas)))


    # Verifica se o jogador clicou em uma bolha ou 
            # no botão "Ver Palavra"
    for evento in pygame.event.get():
        
        # Verifica se o evento foi um pedido para fechar o 
                # jogo (clicar no X da janela).
        if evento.type == pygame.QUIT:

            # Altera a variável 'rodando' para False, terminando o 
                    # loop principal e fechando o jogo.
            rodando = False  
        
        # Verifica se o evento foi um clique do mouse.
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            # Obtém a posição do mouse no momento do clique.
            pos = pygame.mouse.get_pos()
            
            # Verifica se o clique do mouse foi sobre o botão "Ver Palavra".
            if botao_ver_palavra.collidepoint(pos):
                
                # Chama a função que exibe a palavra correta em 
                        # um alerta, se o botão foi clicado.
                mostrar_palavra_alerta()  # Exibe a palavra correta ao clicar no botão.
            
            # Se o clique não foi sobre o botão, verifica se 
                    # foi sobre alguma bolha.
            else:
                
                # Itera sobre cada bolha na lista de bolhas.
                for bolha in bolhas:
                    
                    # Verifica se a bolha foi clicada utilizando o método 'checar_clique', 
                            # que calcula a distância entre a posição do clique e o centro da bolha.
                    if bolha.checar_clique(pos):
                        
                        # Verifica se a letra dentro da bolha clicada faz parte da 
                                # palavra que o jogador está tentando formar.
                        if bolha.letra in palavra_atual:
                            
                            # Se a letra é parte da palavra, a letra é adicionada à
                                    # lista de letras selecionadas.
                            # Isso é usado para rastrear quais letras da palavra o
                                    # jogador já encontrou.
                            letras_selecionadas.append(bolha.letra)
                            
                            # Remove a bolha que foi clicada da lista de bolhas ativas no jogo.
                            # Isso previne que a mesma bolha seja clicada novamente e
                                    # garante que a interface seja atualizada.
                            bolhas.remove(bolha)
                            
                            # Adiciona uma nova bolha com uma letra aleatória escolhida para
                                    # manter o número de bolhas constante.
                            # A letra é selecionada aleatoriamente das letras disponíveis, 
                                    # podendo ou não ser útil para a palavra atual.
                            bolhas.append(Bolha(random.choice(letras_bolhas)))
                        
                        # Se a letra da bolha clicada não faz parte da palavra 
                                # atual, trata-se como um erro.
                        else:
                            
                            # Reduz o número de vidas do jogador por um. Cada vida 
                                    # perdida é uma chance a menos para completar o jogo com sucesso.
                            vidas -= 1  
                            
                            # Checa se o jogador perdeu todas as suas vidas, o que
                                    # indica um possível fim de jogo.
                            if vidas == 0:
                                
                                # Se todas as vidas forem perdidas, uma mensagem é exibida 
                                        # perguntando se o jogador deseja tentar novamente.
                                resposta = messagebox.askyesno("Fim de Jogo", "Você perdeu todas as vidas!\nDeseja reiniciar o jogo?")
                                
                                # Se o jogador escolhe reiniciar, a pontuação atual é salva e o
                                        # jogo é reiniciado, resetando as condições iniciais.
                                if resposta:
                                    salvar_pontuacao(pontuacao)
                                    reiniciar_jogo()
                                    
                                else:
                                    
                                    # Se o jogador escolher não reiniciar, o jogo é 
                                            # terminado e a janela é fechada.
                                    rodando = False
                                    
                                # Sai do loop de processamento de bolhas porque o estado do 
                                        # jogo mudará significativamente (reinício ou término).
                                break
                            
                            # Se ainda restarem vidas, simplesmente remove a bolha errada e
                                    # adiciona uma nova, permitindo que o jogo continue.
                            else:
                                bolhas.remove(bolha)
                                bolhas.append(Bolha(random.choice(letras_bolhas)))


                        # Sai do loop de bolhas após tratar um clique válido.
                        break  


    # Verifica se a palavra formada pelo jogador é correta 
            # chamando a função 'checar_palavra'.
    if checar_palavra():
        
        # Se a palavra estiver correta, adiciona 10 pontos à
                # pontuação atual do jogador.
        pontuacao += 10
        
        # Chama a função 'salvar_pontuacao' para salvar a nova pontuação no
                # arquivo ou em um registro apropriado.
        salvar_pontuacao(pontuacao)  # Salva a pontuação atualizada.
        
        # Incrementa o número da fase, avançando o jogador para o
                # próximo nível ou desafio.
        fase += 1
        
        # Renderiza um texto de felicitação usando a fonte
                # definida e a cor vermelha.
        # 'fonte_info.render' cria uma superfície gráfica com o
                # texto "Parabéns! Palavra correta!".
        texto_completo = fonte_info.render("Parabéns! Palavra correta!", True, VERMELHO)
        
        # 'tela.blit' desenha o texto na tela. O texto é centralizado 
                # horizontalmente e posicionado no meio vertical da tela.
        tela.blit(texto_completo, (LARGURA // 2 - texto_completo.get_width() // 2, ALTURA // 2))
        
        # 'pygame.display.flip()' atualiza a tela inteira para refletir
                # qualquer desenho feito pela função 'blit'.
        pygame.display.flip()
        
        # Pausa o jogo por 2000 milissegundos (2 segundos) para permitir 
                # que o jogador veja a mensagem de felicitação.
        pygame.time.delay(2000)
        
        # Chama a função 'reiniciar_jogo' para reiniciar o jogo com uma
                # nova palavra e redefinir as condições iniciais.
        reiniciar_jogo()


    # Atualiza a tela inteira para refletir qualquer mudança
            # feita durante o ciclo do loop.
    pygame.display.flip()
    
    # Introduz um pequeno atraso de 30 milissegundos 
            # no loop do jogo.
    # Esse atraso ajuda a controlar a velocidade do loop do jogo,
            # tornando o jogo jogável em velocidades razoáveis
            # e evitando o uso excessivo da CPU.
    pygame.time.delay(30)

# Chama a função para finalizar todos os módulos 
        # do Pygame corretamente.
# Isso é necessário para liberar recursos e garantir
        # que o jogo termine sem deixar processos pendentes ou travar.
pygame.quit()

# Destruí a janela do Tkinter que foi usada para as 
        # caixas de diálogo.
# Isso garante que todos os elementos gráficos do Tkinter 
        # sejam fechados apropriadamente, evitando 
        # qualquer erro de runtime.
tela_inicial.destroy()