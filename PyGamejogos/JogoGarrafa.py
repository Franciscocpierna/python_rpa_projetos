# Importa o módulo pygame, que é uma biblioteca usada para criar jogos
import pygame

# Importa o módulo sys, utilizado para interagir com o sistema operacional
import sys

# Importa o módulo math, que contém funções matemáticas
import math

# Importa o módulo random, que permite gerar números aleatórios
import random

# Inicializa todos os módulos importados do pygame
pygame.init()

# Configurações da tela
# Define a largura da tela do jogo em pixels
largura_tela = 850

# Define a altura da tela do jogo em pixels
altura_tela = 650

# Cria a tela com as dimensões especificadas e atribui a uma 
        # variável para manipulação posterior
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Define o título da janela do jogo
pygame.display.set_caption("Jogo da Garrafa")

# Cores
# Define a cor branca usando valores RGB (Red, Green, Blue)
branco = (255, 255, 255)

# Define a cor preta usando valores RGB
preto = (0, 0, 0)

# Define a cor cinza usando valores RGB
cinza = (200, 200, 200)

# Define a cor azul claro usando valores RGB
azul_claro = (173, 216, 230)

# Fonte
# Carrega uma fonte padrão do pygame com tamanho 36 
        # para usar no jogo
fonte = pygame.font.Font(None, 36)

# Carregar imagem da garrafa e ajustar tamanho
# Carrega a imagem da garrafa do arquivo 'garrafa.png'
garrafa_img_original = pygame.image.load("garrafa.png")

# Define o tamanho da garrafa redimensionada
tamanho_garrafa = (100, 200)

# Ajusta a imagem da garrafa para o tamanho especificado
garrafa_img = pygame.transform.scale(garrafa_img_original, tamanho_garrafa)

# Obtém o retângulo que engloba a imagem da garrafa e
        # centraliza na tela
garrafa_rect = garrafa_img.get_rect(center=(largura_tela // 2, altura_tela // 2))

# Define o ângulo inicial da garrafa como 0 graus
angulo = 0

# Configurações do círculo
# Calcula o ponto central do círculo no eixo x
centro_x = largura_tela // 2

# Calcula o ponto central do círculo no eixo y
centro_y = altura_tela // 2

# Define o raio do círculo onde a garrafa será posicionada
raio = 250

# Definir os ângulos específicos e seus tipos
# Cria um dicionário para mapear ângulos com
        # eventos específicos do jogo
setores = {
    0: "Perdeu Ponto",
    60: "Pergunta",
    120: "Perdeu Ponto",
    180: "Pergunta",
    240: "Perdeu Ponto",
    300: "Pergunta"
}


# Define uma função chamada 'gerar_pergunta' que 
        # não recebe argumentos
def gerar_pergunta():
    
    # Cria uma lista de operadores matemáticos
    operadores = ['+', '-', '*', '/']
    
    # Escolhe aleatoriamente um operador da lista
    operador = random.choice(operadores)
    
    # Verifica qual operador foi escolhido e gera uma 
            # pergunta e resposta apropriadas
    if operador == '+':  # Se o operador for soma (+)
        
        a = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10 para 'a'
        b = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10 para 'b'
        pergunta = f'{a} + {b} = ?'  # Monta a pergunta como uma string
        resposta = a + b  # Calcula a resposta somando 'a' e 'b'
        
    elif operador == '-':  # Se o operador for subtração (-)
        
        a = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10 para 'a'
        b = random.randint(1, a)  # Gera um número aleatório entre 1 e 'a' para 'b' para garantir que 'a' - 'b' não seja negativo
        pergunta = f'{a} - {b} = ?'  # Monta a pergunta como uma string
        resposta = a - b  # Calcula a resposta subtraindo 'b' de 'a'
        
    elif operador == '*':  # Se o operador for multiplicação (*)
        
        a = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10 para 'a'
        b = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10 para 'b'
        pergunta = f'{a} * {b} = ?'  # Monta a pergunta como uma string
        resposta = a * b  # Calcula a resposta multiplicando 'a' e 'b'
        
    elif operador == '/':  # Se o operador for divisão (/)
        
        b = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10 para 'b'
        resposta = random.randint(1, 10)  # Gera um número aleatório entre 1 e 10 para a resposta
        a = b * resposta  # Calcula 'a' para garantir que a divisão seja exata
        pergunta = f'{a} / {b} = ?'  # Monta a pergunta como uma string
    
    # Retorna a pergunta e a resposta como uma tupla
    return pergunta, resposta


# Variáveis do jogo

# Define 'girando' como False inicialmente para 
        # controlar se a garrafa está girando
girando = False

# Inicializa 'pontuacao' com 0, a pontuação do jogador no início do jogo
pontuacao = 0

# Inicializa 'resposta_usuario' como uma string vazia, para 
        # armazenar a resposta dada pelo usuário
resposta_usuario = ''

# Define 'setor_parado' como None, será usado para saber em 
        # qual setor a garrafa parou após girar
setor_parado = None

# Inicializa 'pergunta_atual' como uma string vazia, onde 
        # será armazenada a pergunta gerada
pergunta_atual = ''

# Inicializa 'resposta_correta' como None, para armazenar a 
        # resposta correta da pergunta gerada
resposta_correta = None

# Define 'estado' como 'principal', para controlar o 
        # estado do jogo (e.g., mostrando a tela principal, perguntas, etc.)
estado = 'principal'

# Define 'aguardando' como False, usado para controlar se o 
        # jogo está em um período de espera entre ações
aguardando = False

# Inicializa 'tempo_espera_inicio' como None, usado para 
        # marcar o início de um período de espera
tempo_espera_inicio = None

# Cria um objeto 'Clock' do pygame para controlar a 
        # taxa de atualização do jogo
clock = pygame.time.Clock()

# Inicia um loop infinito que continuará executando o
        # jogo até que seja fechado
while True:
    
    # Percorre todos os eventos que ocorreram (como cliques
            # de mouse, teclas pressionadas, etc.)
    for evento in pygame.event.get():
        
        # Se o evento for do tipo QUIT (fechar janela)
        if evento.type == pygame.QUIT:
            
            # Finaliza a biblioteca pygame
            pygame.quit()
            
            # Sai do programa
            sys.exit()
            
        # Se o evento for um clique do mouse
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            
            # Se o estado do jogo estiver em 'principal', indicando 
                    # que está na tela inicial ou principal
            if estado == 'principal':
                
                # Verifica se a garrafa não está girando e não 
                        # está aguardando (sem interações pendentes)
                if not girando and not aguardando:
                    
                    # Inicia o giro da garrafa
                    girando = True
                    
                    # Sorteia um ângulo específico de parada 
                            # baseado nos setores definidos
                    angulo_alvo = random.choice(list(setores.keys()))
                    
                    # Determina um número aleatório de rotações 
                            # completas (360 graus) para dar naturalidade ao giro
                    rotacoes = random.randint(3, 5) * 360
                    
                    # Calcula a rotação total adicionando o deslocamento para o ângulo alvo
                    total_rotation = rotacoes + (angulo_alvo - angulo) % 360
                    
                    # Define o número total de quadros que o giro deverá levar
                    total_frames = 120
                    
                    # Inicializa o contador de quadros
                    frame = 0
                    
                    # Define o ângulo inicial do giro
                    angulo_inicial = angulo % 360
                    
                    # Calcula a velocidade angular por quadro para uma rotação suave
                    velocidade_angular = total_rotation / total_frames
                    
            # Verifica se o estado atual do jogo é 'pergunta', o que 
                    # indica que o jogador deve responder uma pergunta
            elif estado == 'pergunta':
                
                # Verifica se o jogador clicou no botão "Responder"
                # `botao_responder_rect.collidepoint(evento.pos)` verifica se o
                        # clique do mouse está dentro da área do botão
                if botao_responder_rect.collidepoint(evento.pos):
                    
                    # Inicia um bloco try-except para tentar processar a 
                            # resposta digitada pelo jogador
                    try:
                        
                        # Converte o texto digitado pelo jogador (em 'resposta_usuario') 
                                # para um número de ponto flutuante (float)
                                # e o compara com a resposta correta armazenada em 'resposta_correta'
                        if float(resposta_usuario) == resposta_correta:
                            
                            # Se a resposta do jogador estiver correta, 
                                    # adiciona 10 pontos à pontuação total
                            pontuacao += 10
                            
                        else:
                            
                            # Se a resposta estiver incorreta, subtrai 10
                                    # pontos da pontuação atual
                            # A função 'max(pontuacao - 10, 0)' garante que a
                                    # pontuação não caia abaixo de zero
                            pontuacao = max(pontuacao - 10, 0)
                    
                    # Exceção para capturar erros ao converter a resposta
                    # Isso trata casos onde a resposta do jogador não é
                            # um número, evitando falhas no código
                    except ValueError:
                        
                        # Se ocorrer um erro (ex.: texto inválido como letras), 
                                # subtrai 10 pontos da pontuação
                        # 'max(pontuacao - 10, 0)' impede que a pontuação fique negativa
                        pontuacao = max(pontuacao - 10, 0)
                    
                    # Após processar a resposta, limpa o campo 'resposta_usuario' 
                            # para que esteja vazio na próxima pergunta
                    resposta_usuario = ''
                    
                    # Retorna o jogo para o estado 'principal' após verificar a resposta
                    # Isso indica que o jogador volta para a tela inicial, 
                            # onde pode girar a garrafa novamente
                    estado = 'principal'

            
        # Verifica se o tipo de evento atual é a pressão de uma tecla no teclado
        elif evento.type == pygame.KEYDOWN:
            
            # Verifica se o estado atual do jogo é 'pergunta', ou seja, se o 
                    # jogador deve responder uma pergunta
            if estado == 'pergunta':
                
                # Verifica se a tecla pressionada foi o BACKSPACE, usado 
                        # para apagar o último caractere
                if evento.key == pygame.K_BACKSPACE:
                    
                    # Apaga o último caractere da string 'resposta_usuario', 
                            # usando uma fatia que exclui o último caractere
                    # Isso permite que o jogador corrija a resposta ao pressionar BACKSPACE
                    resposta_usuario = resposta_usuario[:-1]
                
                # Caso contrário (se uma tecla diferente de BACKSPACE foi pressionada)
                else:
                    
                    # Adiciona o caractere correspondente à tecla pressionada
                            # ao final da string 'resposta_usuario'
                    # 'evento.unicode' captura o caractere da tecla, 
                            # considerando letras, números e símbolos
                    # Isso permite que o jogador construa sua resposta
                            # digitando múltiplas teclas
                    resposta_usuario += evento.unicode




    # Verifica se o jogo está no estado de 'aguardando', o que 
            # acontece após a garrafa terminar de girar
    if aguardando:
        
        # Obtém o tempo atual em milissegundos desde que o 
                # pygame foi inicializado
        tempo_atual = pygame.time.get_ticks()
        
        # Verifica se já se passaram 2000 milissegundos (2 segundos) 
                # desde que começou a aguardar
        if tempo_atual - tempo_espera_inicio >= 2000:
            
            # Desativa o estado de 'aguardando', permitindo que o jogo continue
            aguardando = False
            
            # Lógica para determinar o resultado com base no
                    # ângulo onde a garrafa parou
            # Checa se o ângulo parado corresponde a um dos setores 
                    # de pergunta ('Pergunta')
            if setor_parado in [0, 120, 240]:
                
                # Muda o estado do jogo para 'pergunta', para mostrar
                        # uma pergunta ao usuário
                estado = 'pergunta'
                
                # Chama a função 'gerar_pergunta' para obter uma nova 
                        # pergunta e sua resposta correta
                pergunta_atual, resposta_correta = gerar_pergunta()
                
                # Reseta a variável de resposta do usuário para garantir 
                        # que está limpa para a nova pergunta
                resposta_usuario = ''
                
            else:
                
                # Caso a garrafa pare em um setor que não é de pergunta ('Perdeu Ponto')
                # Subtrai 10 pontos da pontuação do usuário, sem 
                        # permitir que a pontuação se torne negativa
                pontuacao = max(pontuacao - 10, 0)
    
    # Preenche a tela com a cor branca, preparando o fundo para
            # desenhar novos elementos gráficos
    tela.fill(branco)


    # Verifica se o estado atual do jogo é 'principal'
    if estado == 'principal':
        
        # Percorre cada ângulo definido no dicionário de setores
        for ang in setores:
            
            # Calcula as coordenadas do ponto final de cada linha de
                    # setor usando funções trigonométricas
            # X é calculado como o cosseno do ângulo convertido para radianos
            ponto1 = (
                centro_x + raio * math.cos(math.radians(ang)),  # Posição X do ponto final da linha
                centro_y - raio * math.sin(math.radians(ang))   # Posição Y do ponto final da linha
            )
            
            # Desenha uma linha do centro do círculo até o ponto final do setor
            pygame.draw.line(tela, preto, (centro_x, centro_y), ponto1, 2)
    
            # Calcula a posição para o texto do setor, deslocando um 
                    # pouco para fora do círculo central
            # X é deslocado usando o cosseno do ângulo ajustado para o meio do setor
            x_texto = centro_x + (raio + 60) * math.cos(math.radians(ang + 30))  # Posição X para o texto
            
            # Y é deslocado usando o seno do ângulo ajustado para o meio do setor
            y_texto = centro_y - (raio + 60) * math.sin(math.radians(ang + 30))  # Posição Y para o texto
            
            # Cria um objeto de texto com a descrição do setor
            texto_setor = fonte.render(setores[ang], True, preto)
            
            # Obtém o retângulo que centraliza o texto no ponto calculado
            rect_texto = texto_setor.get_rect(center=(x_texto, y_texto))
            
            # Coloca o texto na tela no local especificado
            tela.blit(texto_setor, rect_texto)
    
        # Desenha o círculo base para os setores na tela
        pygame.draw.circle(tela, preto, (centro_x, centro_y), raio, 2)
    
        # Rotaciona a imagem da garrafa de acordo com o ângulo atual
        garrafa_rotacionada = pygame.transform.rotate(garrafa_img, angulo)  # Rotaciona a imagem da garrafa
        
        # Obtém o retângulo que centraliza a garrafa rotacionada
        novo_rect = garrafa_rotacionada.get_rect(center=garrafa_rect.center)
        
        # Desenha a garrafa rotacionada na posição centralizada
        tela.blit(garrafa_rotacionada, novo_rect.topleft)


        # Controle de rotação da garrafa
        # Verifica se a variável 'girando' está como True, indicando 
                # que a garrafa deve estar girando
        if girando:
            
            # Verifica se o quadro atual (frame) é menor que o total de 
                    # quadros necessários para completar a rotação
            if frame < total_frames:
            
                # Calcula o ângulo atual da garrafa usando o ângulo inicial e
                        # a velocidade angular multiplicada pelo quadro atual
                # A operação "% 360" garante que o ângulo esteja sempre 
                        # dentro do intervalo de 0 a 359 graus
                angulo = (angulo_inicial + velocidade_angular * frame) % 360
                
                # Incrementa o contador de quadros para que no próximo loop, o
                        # ângulo seja ajustado para o próximo quadro
                frame += 1
                
            else:
                
                # Se o quadro atual atingiu ou ultrapassou o total de 
                        # quadros, significa que a rotação deve parar
                # Define o ângulo final da garrafa no ângulo 
                        # alvo (posição onde a garrafa deve parar)
                angulo = angulo_alvo
                
                # Define 'girando' como False, indicando que a rotação terminou
                girando = False
                
                # Define 'setor_parado' com o ângulo alvo para
                        # armazenar a posição final da garrafa
                setor_parado = angulo_alvo
                
                # Define 'aguardando' como True para iniciar o 
                        # estado de espera antes da próxima ação
                aguardando = True
                
                # Armazena o tempo atual (em milissegundos desde o
                        # início do jogo) para gerenciar a duração do estado de espera
                tempo_espera_inicio = pygame.time.get_ticks()
        
        # Mostrar pontuação
        # Renderiza o texto de pontuação usando a fonte definida, 
                # com o valor atual da pontuação
        texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, preto)
        
        # Exibe o texto de pontuação na tela na posição (10, 10), 
                # no canto superior esquerdo
        tela.blit(texto_pontuacao, (10, 10))


    # Verifica se o estado do jogo está em 'pergunta', indicando 
            # que uma pergunta matemática está sendo exibida
    elif estado == 'pergunta':

        # Preenche a tela com a cor azul claro para diferenciar 
                # visualmente a tela de pergunta
        tela.fill(azul_claro)
        
        # Renderiza o título "Tela de Pergunta" para informar o 
                # jogador sobre o estado atual
        texto_titulo = fonte.render("Tela de Pergunta", True, preto)

        # Obtém o retângulo para o texto do título, centralizando-o horizontalmente 
                # na tela (posição vertical em 30 pixels)
        rect_titulo = texto_titulo.get_rect(center=(largura_tela // 2, 30))

        # Desenha o texto do título na tela na posição definida 
                # pelo retângulo centralizado
        tela.blit(texto_titulo, rect_titulo)
    
        # Renderiza a pergunta matemática atual para exibição ao jogador
        # Usa a variável 'pergunta_atual', que contém a pergunta
                # formatada como string (ex: "5 + 3 = ?")
        texto_pergunta = fonte.render(f"{pergunta_atual}", True, preto)

        # Obtém o retângulo para o texto da pergunta, centralizando-o
                # horizontalmente (posição vertical em 80 pixels)
        rect_texto = texto_pergunta.get_rect(center=(largura_tela // 2, 80))

        # Desenha o texto da pergunta na tela na posição definida
                # pelo retângulo centralizado
        tela.blit(texto_pergunta, rect_texto)


        # Cria uma caixa de resposta na tela onde o jogador pode
                # ver o texto que está digitando
        # Define as dimensões e posição da caixa: centralizada 
                # horizontalmente e um pouco abaixo da pergunta
        caixa_resposta = pygame.Rect((largura_tela // 2) - 150, 130, 300, 50)
        
        # Desenha o retângulo da caixa de resposta na tela
                # usando a cor cinza
        # A caixa será usada como um campo visual para mostrar o
                # texto digitado pelo usuário
        pygame.draw.rect(tela, cinza, caixa_resposta)
        
        # Renderiza o texto que o jogador digitou até o 
                # momento ('resposta_usuario') na cor preta
        # O texto é atualizado dinamicamente enquanto o jogador digita
        texto_resposta = fonte.render(resposta_usuario, True, preto)
        
        # Desenha o texto da resposta dentro da caixa de resposta, com
                # um deslocamento para não encostar nas bordas
        # O deslocamento de 10 pixels para a direita e para baixo
                # melhora a legibilidade do texto dentro da caixa
        tela.blit(texto_resposta, (caixa_resposta.x + 10, caixa_resposta.y + 10))


        # Cria um retângulo para o botão "Responder", onde o jogador
                # pode clicar para enviar sua resposta
        # A posição do retângulo é centralizada horizontalmente, com
                # uma largura de 150 pixels e altura de 50 pixels
        botao_responder_rect = pygame.Rect((largura_tela // 2) - 75, 200, 150, 50)
        
        # Desenha o retângulo do botão na tela usando uma cor 
                # verde escura (RGB: 0, 128, 0)
        # Esse retângulo representa o botão de "Responder" 
                # que o jogador irá clicar
        pygame.draw.rect(tela, (0, 128, 0), botao_responder_rect)
        
        # Renderiza o texto "Responder" usando a fonte configurada, 
                # na cor branca, para ser colocado no botão
        # Esse texto indica a ação do botão e será exibido centralizado 
                # dentro do botão verde
        texto_botao = fonte.render('Responder', True, branco)
        
        # Obtém o retângulo do texto renderizado e centraliza-o 
                # dentro do retângulo do botão
        # Isso garante que o texto "Responder" esteja alinhado no centro do botão verde
        texto_botao_rect = texto_botao.get_rect(center=botao_responder_rect.center)
        
        # Desenha o texto "Responder" na tela, posicionado dentro do
                # botão verde, usando as coordenadas calculadas
        # Isso coloca o texto dentro do botão, pronto para o
                # jogador visualizar e interagir
        tela.blit(texto_botao, texto_botao_rect)


        # Renderiza o texto da pontuação atual do jogador, 
                # usando o valor da variável 'pontuacao'
        # O texto é criado com a fonte previamente configurada e a cor preta
        # O uso de 'f"Pontuação: {pontuacao}"' insere o valor 
                # atual da pontuação na string
        texto_pontuacao = fonte.render(f"Pontuação: {pontuacao}", True, preto)
        
        # Desenha o texto da pontuação na tela na posição (10, 10),
                # no canto superior esquerdo
        # O posicionamento em (10, 10) garante que a pontuação 
                # esteja sempre visível ao jogador
        tela.blit(texto_pontuacao, (10, 10))
        
    # Atualiza a tela do jogo para que todas as mudanças visuais
            # fiquem visíveis para o jogador
    # O método 'flip()' do pygame troca o buffer da tela, 
            # exibindo o que foi desenhado nesta iteração do loop
    pygame.display.flip()
    
    # Controla a velocidade de atualização da tela, limitando a 
            # 60 quadros por segundo (FPS)
    # Isso ajuda a garantir que o jogo funcione de maneira suave e
            # consistente em diferentes dispositivos
    clock.tick(60)