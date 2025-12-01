# Importa o módulo pygame para criação de jogos
import pygame

# Importa o módulo random para geração de números aleatórios
import random

# Importa o módulo sys para interação com o sistema
import sys

# Inicializa o módulo pygame, que é necessário para 
        # qualquer funcionalidade do pygame
pygame.init()

# Define as dimensões da janela do jogo
LARGURA, ALTURA = 480, 640

# Cria a janela de exibição com as dimensões especificadas
janela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela
pygame.display.set_caption("Jogo das Bolhas Matemáticas")

# Define constantes para as cores usadas no jogo
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CORES_BOLHA = [
    (255, 99, 71),    # Cor tomate
    (135, 206, 250),  # Cor azul claro
    (144, 238, 144),  # Cor verde claro
    (238, 130, 238),  # Cor violeta
    (255, 215, 0)     # Cor ouro
]

# Configurações básicas do jogo

# Frames por segundo
FPS = 60  

# Relógio para controlar o tempo e FPS
relogio = pygame.time.Clock()  

# Fonte usada para o texto
fonte = pygame.font.SysFont(None, 48)  

# Variáveis para o controle do jogo
 # Número inicial de vidas
vidas = 3 

# Pontuação inicial
pontuacao = 0  

# Velocidade inicial das bolhas
velocidade_bolha = 2  

# Intervalo em milissegundos para geração de novas bolhas
intervalo_bolha = 2000  

# Armazena o tempo do último spawn de bolha
ultimo_tempo_bolha = pygame.time.get_ticks()  

# Definição de uma função chamada 'gerar_calculo' 
        # que não aceita parâmetros
def gerar_calculo():
    
    # Define uma lista de operadores matemáticos possíveis
    operadores = ['+', '-', '*', '/']
    
    # Gera um número inteiro aleatório entre 1 e 10
    num1 = random.randint(1, 10)
    
    # Gera outro número inteiro aleatório entre 1 e 10
    num2 = random.randint(1, 10)
    
    # Escolhe um operador aleatoriamente da lista de operadores
    operador = random.choice(operadores)
    
    # Se o operador selecionado for divisão, ajusta o primeiro número
            # para garantir que o resultado seja um inteiro
    if operador == '/':

        # Multiplica num1 por num2 para evitar divisão por 
                # zero e garantir um resultado inteiro
        num1 = num1 * num2
        
    # Formata a expressão matemática como uma string
    expressao = f"{num1} {operador} {num2}"
    
    # Avalia a expressão matemática usando a função eval, 
            # que executa a string como código Python
    resultado = eval(expressao)
    
    # Retorna um par contendo a expressão em string e o 
            # resultado da avaliação
    return expressao, resultado

# Chama a função 'gerar_calculo' e armazena o cálculo e o 
        # resultado correto em duas variáveis
calculo, resultado_correto = gerar_calculo()


# Define uma classe chamada 'Bolha', que é um modelo 
        # para criar objetos bolha no jogo
class Bolha:
    
    # O método '__init__' é chamado automaticamente 
            # quando uma nova bolha é criada
    def __init__(self):
        
        # Define o raio da bolha como 30 pixels
        self.raio = 30
        
        # Define a posição x da bolha; ela é escolhida aleatoriamente 
                # entre 'raio' e 'LARGURA - raio'
        # Isso garante que a bolha não será criada parcialmente 
                # fora da tela horizontalmente
        self.x = random.randint(self.raio, LARGURA - self.raio)
        
        # Define a posição y inicial da bolha em '-self.raio', o 
                # que coloca a bolha logo acima da tela
                # para que ela 'entre' na tela quando começar a se mover para baixo
        self.y = -self.raio
        
        # Escolhe uma cor aleatoriamente para a bolha de
                # uma lista predefinida de cores
        self.cor = random.choice(CORES_BOLHA)
        
        # Atribui a velocidade da bolha com base na 
                # variável 'velocidade_bolha' definida globalmente
        self.velocidade = velocidade_bolha
        
        # Escolhe um número aleatório dentro de uma faixa de 10 números
                # abaixo e 10 números acima do resultado correto do cálculo atual
        self.numero = random.randint(int(resultado_correto) - 10, int(resultado_correto) + 10)
        
        # Decisão aleatória para substituir o número na
                # bolha pelo resultado correto
        # Isso acontece com uma probabilidade de 30% para garantir
                # que pelo menos uma bolha tenha o resultado correto
        if random.random() < 0.3:
            self.numero = resultado_correto


    # Define o método 'mover' da classe 'Bolha'
    def mover(self):
        
        # Incrementa a posição y da bolha pela sua velocidade atual
        # Isso faz com que a bolha se mova para baixo na
                # tela a cada chamada deste método
        self.y += self.velocidade
    
    # Define o método 'desenhar' da classe 'Bolha'
    def desenhar(self, superficie):
        
        # Desenha um círculo na superfície do jogo que representa a bolha
        # Utiliza a cor da bolha, posição x e y, e o raio
        pygame.draw.circle(superficie, self.cor, (self.x, int(self.y)), self.raio)
        
        # Renderiza o número dentro da bolha como texto
        # Converte o número da bolha para string e define a 
                # cor do texto para preto
        texto = fonte.render(str(int(self.numero)), True, PRETO)
        
        # Obtém o retângulo que engloba o texto, centralizado
                # na posição x e y da bolha
        rect_texto = texto.get_rect(center=(self.x, int(self.y)))
        
        # Desenha o texto na superfície do jogo na posição
                # definida pelo retângulo
        superficie.blit(texto, rect_texto)
    
    # Define o método 'foi_clicada' da classe 'Bolha'
    def foi_clicada(self, pos):
        
        # Calcula a diferença no eixo x entre a posição do 
                # clique e o centro da bolha
        dx = self.x - pos[0]
        
        # Calcula a diferença no eixo y entre a posição do
                # clique e o centro da bolha
        dy = self.y - pos[1]
        
        # Retorna True se a distância entre o clique e o centro 
                # da bolha for menor ou igual ao raio da bolha
        # Isto é, verifica se o clique foi dentro do círculo da bolha
        return dx * dx + dy * dy <= self.raio * self.raio


# Cria uma lista vazia para armazenar os objetos Bolha
bolhas = []

# Inicia a variável 'executando' como True, que controla a
        # execução do loop do jogo
executando = True

# Entra no loop principal do jogo. Este loop se repete até que a
        # variável 'executando' seja False.
while executando:
    
    # Mantém o jogo rodando a uma taxa constante de quadros por segundo (FPS). 
    # Isso garante que o jogo funcione de forma suave e
            # consistente em diferentes hardware.
    relogio.tick(FPS)
    
    # Preenche toda a tela com a cor branca a cada iteração do loop.
    # Isso limpa o que estava desenhado antes, preparando a tela para o novo quadro.
    janela.fill(BRANCO)

    # Processa todos os eventos de entrada do usuário acumulados
            # desde a última iteração do loop.
    for evento in pygame.event.get():
        
        # Verifica se o evento atual é do tipo QUIT, que é 
                # disparado ao fechar a janela do jogo.
        if evento.type == pygame.QUIT:
            
            # Se a janela foi fechada, a variável 'executando' é 
                    # setada como False, o que fará com que o loop principal pare.
            executando = False
            
            # Fecha a janela do jogo e termina a execução do 
                    # programa imediatamente.
            sys.exit()
            
        # Verifica se o evento atual é um clique do mouse (MOUSEBUTTONDOWN).
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            # Armazena a posição do cursor do mouse no momento do clique. 
            # Isso é usado para determinar se uma bolha foi clicada.
            pos = pygame.mouse.get_pos()
            
            # Itera sobre a lista de bolhas no jogo. A cópia da lista é 
                    # usada para permitir modificar a lista original (removendo
                    # bolhas) sem interferir na iteração.
            for bolha in bolhas[:]:
                
                # Verifica se a bolha atual foi clicada, chamando o 
                        # método 'foi_clicada' e passando a posição do clique.
                if bolha.foi_clicada(pos):
                    
                    # Verifica se o número na bolha clicada é igual ao 
                            # resultado correto do cálculo matemático atual.
                    if bolha.numero == resultado_correto:
                        
                        # Aumenta a pontuação do jogador em 1 ponto por 
                                # acertar a bolha correta.
                        pontuacao += 1
                        
                        # Remove a bolha clicada da lista de bolhas, 
                                # pois ela já foi acertada.
                        bolhas.remove(bolha)
                        
                        # Gera um novo cálculo matemático e atualiza o resultado
                                # correto, para o próximo desafio.
                        calculo, resultado_correto = gerar_calculo()
                        
                        # Aumenta a velocidade de movimento das bolhas, 
                                # tornando o jogo mais desafiador.
                        velocidade_bolha += 0.2
                        
                        # Reduz o intervalo entre o surgimento de novas bolhas,
                                # aumentando a frequência com que elas aparecem.
                        if intervalo_bolha > 500:
                            intervalo_bolha -= 50
                            
                    else:
                        
                        # Se a bolha clicada não contém o número correto, o 
                                # jogador perde uma vida.
                        vidas -= 1
                        
                        # Remove a bolha errada clicada da lista de bolhas.
                        bolhas.remove(bolha)
                        
                        # Verifica se o jogador ficou sem vidas.
                        if vidas == 0:
                            
                            # Se não restarem vidas, o jogo termina, e o 
                                    # loop principal é encerrado.
                            executando = False
                            
                            # Exibe uma mensagem "Game Over" no console.
                            print("Game Over")
                            
                    # Após processar um clique, interrompe a iteração sobre as bolhas, 
                            # pois não é necessário verificar as demais após 
                            # um clique ser reconhecido.
                    break

    # Adiciona novas bolhas no jogo
    # Obtém o número atual de ticks (milissegundos desde que o 
            # Pygame foi inicializado)
    tempo_atual = pygame.time.get_ticks()
    
    # Verifica se o tempo decorrido desde a última bolha adicionada é maior que o 
            # intervalo definido para criação de novas bolhas
    if tempo_atual - ultimo_tempo_bolha > intervalo_bolha:
        
        # Se o intervalo necessário tiver passado, uma nova bolha é criada e 
                # adicionada à lista de bolhas
        bolhas.append(Bolha())
        
        # Atualiza a variável 'ultimo_tempo_bolha' com o tempo atual, para que 
                # possamos controlar quando a próxima bolha será adicionada
        ultimo_tempo_bolha = tempo_atual


    # Itera sobre cada bolha existente na lista de bolhas
    for bolha in bolhas[:]:
        
        # Atualiza a velocidade da bolha para a velocidade atual do jogo
        bolha.velocidade = velocidade_bolha
        
        # Chama o método 'mover' da bolha, que aumenta sua posição y de
                # acordo com sua velocidade
        bolha.mover()
    
        # Verifica se a bolha já passou do limite inferior da tela (ou 
                # seja, se já "saiu" da tela)
        if bolha.y - bolha.raio > ALTURA:
            
            # Se a bolha que saiu era aquela que continha o número 
                    # correto (a resposta certa do cálculo)
            if bolha.numero == resultado_correto:
                
                # Decrementa uma vida do jogador, pois a resposta certa foi perdida
                vidas -= 1
                
                # Verifica se após perder uma vida, o jogador ainda tem vidas restantes
                if vidas == 0:
                    
                    # Se não houver mais vidas, o jogo termina
                    executando = False
                    
                    # Exibe uma mensagem "Game Over" indicando o fim do jogo
                    print("Game Over")
                    
                else:
                    
                    # Se ainda restam vidas, gera um novo cálculo 
                            # matemático para ser resolvido
                    calculo, resultado_correto = gerar_calculo()
                    
            # Remove a bolha da lista, pois ela já não é mais visível na tela
            bolhas.remove(bolha)
            
        else:
            
            # Se a bolha ainda está visível na tela, chama o método 'desenhar' para desenhá-la na janela
            bolha.desenhar(janela)


    # Renderiza o texto com o cálculo atual usando a fonte definida, 
            # com a cor preta sobre um fundo transparente.
    texto_calculo = fonte.render(f"Resolva: {calculo}", True, PRETO)
    
    # Posiciona o texto do cálculo na janela, começando na 
            # posição x=20 e y=20 pixels.
    janela.blit(texto_calculo, (20, 20))
    
    # Renderiza o texto com a pontuação atual do jogador.
    texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", True, PRETO)
    
    # Posiciona o texto da pontuação na janela, começando na
            # posição x=20 e y=80 pixels.
    janela.blit(texto_pontuacao, (20, 80))
    
    # Renderiza o texto com a quantidade de vidas restantes do jogador.
    texto_vidas = fonte.render(f"Vidas: {vidas}", True, PRETO)
    
    # Posiciona o texto das vidas na janela, começando na 
            # posição x=20 e y=140 pixels.
    janela.blit(texto_vidas, (20, 140))
    
    # Atualiza a tela inteira para mostrar todos os elementos 
            # gráficos desenhados durante este quadro.
    pygame.display.flip()

# Fecha a biblioteca Pygame de maneira adequada ao fim do
        # jogo para liberar recursos do sistema.
pygame.quit()