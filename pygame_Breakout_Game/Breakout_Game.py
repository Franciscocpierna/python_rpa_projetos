# Importa o módulo 'turtle' que é usado para criar
        # gráficos e jogos simples em uma janela.
import turtle

# Configura a janela principal onde o jogo será exibido.
# Cria um objeto Screen. Este objeto representa a janela do jogo.
janela = turtle.Screen()  

# Define o título da janela.
# O método 'title' é usado para dar um título à janela. 
        # Aqui, "Jogo Breakout" é o título escolhido.
janela.title("Jogo Breakout")  

# Define a cor de fundo da janela.
# O método 'bgcolor' é utilizado para definir a cor de 
        # fundo da janela. 'black' (preto) é a cor definida.
janela.bgcolor("black")  

# Configura o tamanho da janela.
# O método 'setup' define as dimensões da janela. Aqui, a 
        # largura é 800 pixels e a altura é 600 pixels.
janela.setup(width=800, height=600)  

# Desativa a atualização automática da tela.
# O método 'tracer' com o argumento 0 desliga a animação 
        # automática, ou seja, a tela não se atualiza automaticamente.
janela.tracer(0)  

# Cria um novo objeto Turtle para representar a raquete no jogo.
raquete = turtle.Turtle()

# Define a velocidade de animação do Turtle. O valor '0' 
        # desativa a animação, fazendo com que as mudanças 
        # sejam instantâneas.
raquete.speed(0)

# Configura a forma do Turtle. Aqui, a forma é 'square' (quadrado), 
        # mas você pode escolher outras formas como 'circle' (círculo), 
        # 'triangle' (triângulo), etc.
raquete.shape("square")

# Define a cor do Turtle. 'white' significa que a 
        # raquete será branca.
raquete.color("white")

# Define o tamanho do Turtle. 'stretch_wid' é o fator de 
        # estiramento na largura e 'stretch_len' é o 
        # fator de estiramento no comprimento.
# Neste caso, a raquete terá 1 unidade de altura e 
        # 5 unidades de largura.
raquete.shapesize(stretch_wid=1, stretch_len=5)

# Levanta a caneta do Turtle, o que significa que o 
        # Turtle se moverá sem desenhar uma linha.
raquete.penup()

# Move o Turtle para uma posição específica na tela. 
        # Aqui, ele é posicionado no meio na parte inferior 
        # da janela (coordenadas x=0, y=-250).
raquete.goto(0, -250)


# Cria um novo objeto Turtle para representar a bola no jogo.
bola = turtle.Turtle()

# Define a velocidade de animação da bola. O valor '1' 
        # proporciona uma animação básica e rápida.
bola.speed(1)

# Configura a forma da bola. A forma escolhida é 'square' (quadrado).
bola.shape("square")

# Define a cor da bola, que neste caso é 'white' (branca).
bola.color("white")

# Levanta a caneta do Turtle, o que significa que a 
        # bola se moverá sem desenhar uma linha na tela.
bola.penup()

# Posiciona a bola no centro da tela com as 
        # coordenadas x=0 e y=0.
bola.goto(0, 0)

# Define a velocidade horizontal inicial da bola. 
        # O valor '4' indica que a bola se moverá 
        # 4 unidades para a direita a cada atualização.
velocidade_inicial_dx = 4

# Define a velocidade vertical inicial da bola. 
        # O valor '-4' indica que a bola se moverá 
        # 4 unidades para cima a cada atualização.
velocidade_inicial_dy = -4

# Aplica as velocidades inicialmente definidas à bola. 
        # Essas variáveis controlam o movimento da bola no jogo.
bola.dx = velocidade_inicial_dx
bola.dy = velocidade_inicial_dy

# Inicializa uma lista vazia para armazenar os 
        # blocos que serão criados no jogo.
blocos = []

# Define uma lista de cores que serão usadas para os 
        # blocos, tornando o jogo mais colorido e 
        # visualmente atraente.
cores = ["red", "orange", "yellow", "green", "blue"]


# Define a função 'criar_blocos' que não recebe 
        # nenhum argumento.
def criar_blocos():
    
    # Loop 'for' externo que itera cinco vezes 
            # (uma para cada linha de blocos).
    for y in range(5):
        
        # Loop 'for' interno que itera sobre um range de 
                # valores, criando blocos em diferentes posições 'x'.
        for x in range(-350, 400, 100):
            
            # Cria um novo objeto Turtle para cada bloco.
            bloco = turtle.Turtle()
            
            # Define a velocidade de animação do Turtle 
                    # para o valor mais rápido '0', que é instantâneo.
            bloco.speed(0)
            
            # Define a forma do Turtle como 'square' (quadrado).
            bloco.shape("square")
            
            # Define a cor do bloco usando um índice 'y' 
                    # para selecionar da lista de cores.
            bloco.color(cores[y])
            
            # Ajusta o tamanho do Turtle para que seja mais 
                    # largo do que alto (5 unidades de 
                    # comprimento e 1 unidade de largura).
            bloco.shapesize(stretch_wid=1, stretch_len=5)
            
            # Levanta a caneta do Turtle para evitar desenhar 
                    # linhas ao mover o bloco para a posição inicial.
            bloco.penup()
            
            # Posiciona o bloco em uma coordenada 'x' específica e 
                    # calcula a posição 'y' para criar várias linhas de blocos.
            # '250 - y * 30' move cada linha de blocos 30 
                    # pixels para baixo da anterior.
            bloco.goto(x, 250 - y * 30)
            
            # Adiciona o bloco recém-criado à lista 'blocos', 
                    # permitindo que eles sejam manipulados 
                    # mais tarde no jogo.
            blocos.append(bloco)


# Chama a função 'criar_blocos()' que foi 
        # definida anteriormente.
# Esta função é responsável por inicializar os 
        # blocos do jogo na tela.
criar_blocos()

# Inicializa a variável 'pontuacao' com 0 para começar a 
        # contar os pontos do jogador desde o início do jogo.
pontuacao = 0

# Inicializa a variável 'nivel' com 1, indicando que o 
        # jogador começa no primeiro nível.
nivel = 1

# Cria um novo objeto Turtle para exibir o placar na tela.
exibir_pontuacao = turtle.Turtle()

# Configura a velocidade de animação do Turtle para '0', 
        # o que faz com que as atualizações sejam instantâneas.
exibir_pontuacao.speed(0)

# Define a cor do texto do placar como 'white' (branco) 
        # para garantir que seja visível contra o fundo escuro.
exibir_pontuacao.color("white")

# Levanta a caneta do Turtle para mover o objeto 
        # sem desenhar linhas.
exibir_pontuacao.penup()

# Oculta o Turtle para que apenas o texto seja visível, e 
        # não a representação gráfica do objeto Turtle.
exibir_pontuacao.hideturtle()

# Move o Turtle para a posição (0, 260) no topo da tela para 
        # que o placar fique visível acima dos blocos e da área de jogo.
exibir_pontuacao.goto(0, 260)

# Escreve o texto inicial do placar na tela, mostrando 
        # tanto a pontuação quanto o nível atual.
# O texto é centralizado, e a fonte utilizada é "Courier" com 
        # tamanho 24 e estilo normal.
exibir_pontuacao.write("Pontuação: 0  Nível: 1", 
                       align="center", 
                       font=("Courier", 24, "normal"))



# Define a função 'fim_do_jogo' para ser chamada 
            # quando o jogador perder ou concluir o jogo.
def fim_do_jogo():
    
    # Limpa o placar atual para remover a pontuação e o 
            # nível exibidos anteriormente.
    exibir_pontuacao.clear()
    
    # Escreve a mensagem "Fim de Jogo. Clique para 
            # reiniciar" no placar.
    # A mensagem é centralizada e usa a fonte "Courier" 
            # com tamanho 24 e estilo normal.
    exibir_pontuacao.write("Fim de Jogo. Clique para reiniciar", 
                           align="center", 
                           font=("Courier", 24, "normal"))
    
    # Cria um novo objeto Turtle que funcionará 
            # como um botão visual para reiniciar o jogo.
    botao_reiniciar = turtle.Turtle()
    
    # Define a velocidade de animação do Turtle 
            # para '0', que é instantâneo.
    botao_reiniciar.speed(0)
    
    # Configura a forma do Turtle como 'square' (quadrado).
    botao_reiniciar.shape("square")
    
    # Define a cor do Turtle (botão) como 'grey' (cinza).
    botao_reiniciar.color("grey")
    
    # Ajusta o tamanho do Turtle para ser mais largo do 
            # que alto, formando uma barra que se assemelha a um botão.
    botao_reiniciar.shapesize(stretch_wid=2, 
                              stretch_len=10)
    
    # Levanta a caneta do Turtle para mover o objeto 
            # sem desenhar linhas.
    botao_reiniciar.penup()
    
    # Posiciona o botão no centro da tela.
    botao_reiniciar.goto(0, 0)
    
    # Cria outro objeto Turtle para o texto do botão.
    texto_reiniciar = turtle.Turtle()
    
    # Define a velocidade de animação para o texto do 
            # botão como '0', que é instantâneo.
    texto_reiniciar.speed(0)
    
    # Define a cor do texto como 'white' (branco).
    texto_reiniciar.color("white")
    
    # Levanta a caneta do Turtle para mover o 
            # objeto sem desenhar linhas.
    texto_reiniciar.penup()
    
    # Oculta o Turtle do texto para que apenas o 
            # texto seja visível.
    texto_reiniciar.hideturtle()
    
    # Posiciona o texto ligeiramente abaixo do 
            # centro da tela.
    texto_reiniciar.goto(0, -10)
    
    # Escreve o texto "Recomeçar" no botão, 
            # centralizado e com a fonte "Courier" tamanho 24.
    texto_reiniciar.write("Recomeçar", 
                          align="center", 
                          font=("Courier", 24, "normal"))

    
    # Define a função 'ao_clicar' que é chamada quando um 
            # clique do mouse é detectado na janela do jogo.
    # Os parâmetros 'x' e 'y' representam as 
            # coordenadas do clique na janela.
    def ao_clicar(x, y):
        
        # Verifica se as coordenadas do clique estão 
                # dentro dos limites definidos que 
                # correspondem à área do botão.
        # A condição -100 < x < 100 verifica se o 
                # clique foi horizontalmente dentro do botão.
        # A condição -20 < y < 20 verifica se o 
                # clique foi verticalmente dentro do botão.
        if -100 < x < 100 and -20 < y < 20:
            
            # Oculta o Turtle usado para desenhar o 
                    # botão de reiniciar, removendo-o visualmente da tela.
            botao_reiniciar.hideturtle()
            
            # Limpa qualquer texto que tenha sido escrito 
                    # pelo Turtle de texto do botão, limpando a 
                    # área onde "Recomeçar" foi mostrado.
            texto_reiniciar.clear()
            
            # Desvincula qualquer função previamente ligada a 
                    # cliques na janela, impedindo que a função 
                    # 'ao_clicar' seja chamada novamente.
            janela.onclick(None)
            
            # Chama a função 'reiniciar_jogo' para reiniciar o 
                    # jogo, resetando todas as configurações e 
                    # começando uma nova partida.
            reiniciar_jogo()
    
    # Associa o evento de clique na janela à função 'ao_clicar'.
    # Qualquer clique dentro da janela agora invocará a função 
            # 'ao_clicar', passando as coordenadas do clique 
            # como argumentos.
    janela.onclick(ao_clicar)


# Define a função 'mover_raquete_direita', que é 
        # responsável por mover a raquete para a 
        # direita quando chamada.
def mover_raquete_direita():
    
    # Obtém a posição x atual da raquete usando o método 
            # 'xcor()', que retorna a coordenada x do objeto Turtle.
    x = raquete.xcor()

    # Verifica se a posição x atual da raquete é menor que 350.
    # O valor 350 é um limite estabelecido para evitar que a 
            # raquete saia da tela para a direita.
    if x < 350:
        
        # Se a raquete ainda não atingiu o limite direito da 
                # tela, incrementa a posição x da raquete em 40 unidades.
        # Este valor (40) representa o quanto a raquete se move 
                # para a direita a cada chamada da função.
        x += 40

    # Atualiza a posição x da raquete usando o método 'setx()'. 
    # Este método define a nova posição x da raquete, 
            # efetivamente movendo-a horizontalmente.
    raquete.setx(x)


# Define a função 'mover_raquete_esquerda', que é responsável 
            # por mover a raquete para a esquerda quando chamada.
def mover_raquete_esquerda():
    
    # Obtém a posição x atual da raquete usando o 
            # método 'xcor()', que retorna a coordenada x 
            # do objeto Turtle.
    x = raquete.xcor()

    # Verifica se a posição x atual da raquete é maior que -350.
    # O valor -350 é um limite estabelecido para evitar que a 
            # raquete saia da tela para a esquerda.
    if x > -350:
        
        # Se a raquete ainda não atingiu o limite esquerdo da 
                # tela, decrementa a posição x da raquete em 40 unidades.
        # Este valor (40) representa o quanto a raquete se move 
                # para a esquerda a cada chamada da função.
        x -= 40

    # Atualiza a posição x da raquete usando o método 'setx()'.
    # Este método define a nova posição x da raquete, 
            # efetivamente movendo-a horizontalmente.
    raquete.setx(x)


# Ativa a detecção de eventos de teclado na janela do jogo.
# Isso permite que a janela 'escute' eventos de 
        # pressionamento de teclas.
janela.listen()

# Vincula o pressionamento da tecla "Right" (seta 
        # para a direita) à função 'mover_raquete_direita'.
# Quando a tecla "Right" é pressionada, a 
        # função 'mover_raquete_direita' é 
        # chamada automaticamente.
janela.onkeypress(mover_raquete_direita, "Right")

# Vincula o pressionamento da tecla "Left" (seta para a 
        # esquerda) à função 'mover_raquete_esquerda'.
# Quando a tecla "Left" é pressionada, a função 
        # 'mover_raquete_esquerda' é chamada automaticamente.
janela.onkeypress(mover_raquete_esquerda, "Left")

# Inicializa uma variável 'velocidade_aumentada' como False.
# Esta variável é usada para controlar se a 
        # velocidade da bola foi aumentada ou não.
# 'False' indica que a velocidade inicial da 
        # bola é a normal e que ainda não foi aumentada.
velocidade_aumentada = False


# Define a função 'aumentar_velocidade', que é chamada 
        # para aumentar a velocidade da bola no jogo.
def aumentar_velocidade():
    
    # Utiliza a palavra-chave 'global' para modificar a 
            # variável 'velocidade_aumentada' definida fora da função.
    # Isso permite que a função altere o valor 
            # dessa variável global.
    global velocidade_aumentada

    # Verifica se a velocidade da bola ainda 
            # não foi aumentada.
    # A condição 'not velocidade_aumentada' será 
            # verdadeira se 'velocidade_aumentada' for False.
    if not velocidade_aumentada:
        
        # Dobra a velocidade horizontal da bola 
                # multiplicando o valor de 'bola.dx' por 2.
        bola.dx *= 2
        
        # Dobra a velocidade vertical da bola 
                # multiplicando o valor de 'bola.dy' por 2.
        bola.dy *= 2

        # Atualiza o estado da variável 
                # 'velocidade_aumentada' para True.
        # Isso indica que a velocidade já foi aumentada e 
                # evita que seja duplicada novamente até 
                # que seja reiniciada.
        velocidade_aumentada = True



# Define a função 'velocidade_normal', que é chamada 
        # para redefinir a velocidade da bola 
        # para o valor normal.
def velocidade_normal():
    
    # Utiliza a palavra-chave 'global' para acessar e 
            # modificar a variável 'velocidade_aumentada' 
            # definida fora da função.
    # Isso permite que a função altere o estado dessa 
            # variável global.
    global velocidade_aumentada

    # Verifica se a velocidade da bola já foi aumentada.
    # A condição 'velocidade_aumentada' será verdadeira se a 
            # velocidade da bola já tiver sido aumentada.
    if velocidade_aumentada:
        
        # Reduz pela metade a velocidade horizontal da 
                # bola dividindo o valor de 'bola.dx' por 2.
        bola.dx /= 2
        
        # Reduz pela metade a velocidade vertical da 
                # bola dividindo o valor de 'bola.dy' por 2.
        bola.dy /= 2

        # Atualiza o estado da variável 'velocidade_aumentada' 
                # para False.
        # Isso indica que a velocidade da bola foi restaurada 
                # ao normal, permitindo futuros aumentos se necessário.
        velocidade_aumentada = False


# Vincula a tecla Shift esquerda (Shift_L) ao evento de 
        # pressionar a tecla, associando-a à função 
        # 'aumentar_velocidade'.
# Quando a tecla Shift esquerda é pressionada, a função 
        # 'aumentar_velocidade' é chamada, aumentando a 
        # velocidade da bola.
janela.onkeypress(aumentar_velocidade, "Shift_L")

# Vincula a tecla Shift esquerda (Shift_L) ao evento de 
        # soltar a tecla, associando-a à função 'velocidade_normal'.
# Quando a tecla Shift esquerda é solta, a função 
        # 'velocidade_normal' é chamada, normalizando a 
        # velocidade da bola.
janela.onkeyrelease(velocidade_normal, "Shift_L")


# Define a função 'detectar_colisao', que verifica se 
        # dois objetos estão suficientemente próximos 
        # para ser considerada uma colisão.
def detectar_colisao(obj1, obj2):
    
    # Utiliza o método 'distance' para calcular a 
            # distância entre dois objetos Turtle.
    # 'obj1.distance(obj2)' retorna a distância entre o 
            # centro de 'obj1' e 'obj2'.
    
    # Verifica se a distância entre os dois objetos é 
            # menor que 50 pixels.
    # Se for menor, retorna True, indicando que 
            # uma colisão ocorreu.
    return obj1.distance(obj2) < 50

    
# Define a função 'reiniciar_jogo' para resetar o 
        # jogo ao seu estado inicial.
def reiniciar_jogo():
    
    # Declara que as variáveis 'pontuacao', 'nivel', 
            # 'bola', e 'blocos' serão modificadas globalmente.
    global pontuacao, nivel, bola, blocos

    # Move a bola de volta ao centro da tela (posição inicial).
    bola.goto(0, 0)

    # Redefine a velocidade horizontal da bola para o 
            # valor inicial definido anteriormente.
    bola.dx = velocidade_inicial_dx

    # Redefine a velocidade vertical da bola para o 
            # valor inicial definido anteriormente.
    bola.dy = velocidade_inicial_dy

    # Reseta a pontuação para 0, começando o jogo sem pontos.
    pontuacao = 0

    # Reseta o nível para 1, começando o jogo no 
            # primeiro nível.
    nivel = 1

    # Limpa a exibição anterior do placar para evitar 
            # sobreposições de texto.
    exibir_pontuacao.clear()

    # Escreve a nova pontuação e o nível no placar, 
            # mostrando ambos como 0 e 1, respectivamente.
    exibir_pontuacao.write("Pontuação: 0  Nível: 1", 
                           align="center", 
                           font=("Courier", 24, "normal"))

    # Loop que move todos os blocos existentes para uma 
            # posição fora da tela visível (coordenadas 1000, 1000).
    for bloco in blocos:
        bloco.goto(1000, 1000)

    # Limpa a lista de blocos para remover todas as 
            # referências aos blocos antigos.
    blocos.clear()

    # Chama a função 'criar_blocos' para criar 
            # novos blocos no início do jogo.
    criar_blocos()

    # Atualiza a janela para refletir todas as 
            # mudanças visuais feitas acima.
    janela.update()

    # Chama a função 'loop_jogo' para iniciar ou 
            # continuar o loop principal do jogo.
    loop_jogo()



# Define a função 'loop_jogo' que contém o loop principal do jogo, 
        # controlando a lógica do jogo e a animação.
def loop_jogo():
    
    # Declara que as variáveis 'pontuacao', 'nivel', e 'blocos' 
            # serão modificadas globalmente dentro desta função.
    global pontuacao, nivel, blocos

    # Verifica se a posição vertical da bola é menor que -290, o 
            # que indica que a bola passou da raquete.
    if bola.ycor() < -290:
        
        # Chama a função 'fim_do_jogo' para encerrar o jogo e 
                # mostrar a tela de fim de jogo.
        fim_do_jogo()
        
        # Retorna do loop de jogo para impedir a execução de 
                # mais código após o fim do jogo.
        return

    # Atualiza a tela para refletir as mudanças feitas nas 
            # posições dos objetos.
    janela.update()

    # Movimenta a bola horizontalmente adicionando o 
            # deslocamento 'bola.dx' à posição x atual da bola.
    bola.setx(bola.xcor() + bola.dx)
    
    # Movimenta a bola verticalmente adicionando o 
            # deslocamento 'bola.dy' à posição y atual da bola.
    bola.sety(bola.ycor() + bola.dy)


    # Verifica se a bola ultrapassou a borda superior 
            # da área de jogo.
    if bola.ycor() > 290:
        
        # Se a bola passar da borda superior, reajusta sua 
                # posição para 290 para mantê-la dentro da área visível.
        bola.sety(290)
        
        # Inverte a direção vertical da bola, fazendo-a se mover 
                # para baixo após colidir com a borda superior.
        bola.dy *= -1
    
    # Verifica se a bola ultrapassou a borda direita da área de jogo.
    if bola.xcor() > 390:
        
        # Se a bola passar da borda direita, reajusta sua posição 
                # para 390 para mantê-la dentro da área visível.
        bola.setx(390)
        
        # Inverte a direção horizontal da bola, fazendo-a se 
                # mover para a esquerda após colidir com a borda direita.
        bola.dx *= -1
    
    # Verifica se a bola ultrapassou a borda esquerda da área de jogo.
    if bola.xcor() < -390:
        
        # Se a bola passar da borda esquerda, reajusta sua 
                # posição para -390 para mantê-la dentro da área visível.
        bola.setx(-390)
        
        # Inverte a direção horizontal da bola, fazendo-a se 
                # mover para a direita após colidir com a borda esquerda.
        bola.dx *= -1


    # Verifica a condição de colisão entre a bola e a raquete.
    # A condição é composta por múltiplos testes para garantir 
            # que a bola realmente toque a raquete.
    if (bola.dy < 0) and (bola.ycor() > -240 and bola.ycor() < -230) and (bola.xcor() > raquete.xcor() - 50 and bola.xcor() < raquete.xcor() + 50):
        
        # Se a bola estiver se movendo para baixo (bola.dy < 0) e estiver 
                # dentro do intervalo vertical onde a raquete está posicionada,
                # e também estiver horizontalmente alinhada com a 
                # raquete (dentro de 50 unidades de distância do 
                # centro da raquete),
                # então considera-se que a colisão ocorreu.
    
        # Ajusta a posição y da bola para -230, que é logo acima da 
                # raquete, para evitar que ela "fique presa" na 
                # raquete ou que pareça atravessá-la.
        bola.sety(-230)
        
        # Inverte a direção vertical da bola (bola.dy), fazendo 
                # com que ela comece a se mover para cima após a colisão.
        bola.dy *= -1


    # Inicia um loop que verifica cada bloco na lista 'blocos' 
                # para detectar possíveis colisões.
    for bloco in blocos:
        
        # Chama a função 'detectar_colisao' para verificar se há 
                    # colisão entre a bola e o bloco atual do loop.
        if detectar_colisao(bola, bloco):
            
            # Se uma colisão for detectada, inverte a direção vertical 
                    # da bola para simular o rebote.
            bola.dy *= -1
            
            # Move o bloco para uma posição fora da área visível do 
                    # jogo (1000, 1000), efetivamente "removendo-o" do jogo.
            bloco.goto(1000, 1000)
            
            # Remove o bloco da lista 'blocos', garantindo que ele 
                    # não será mais processado nas iterações futuras do jogo.
            blocos.remove(bloco)
            
            # Aumenta a pontuação em 10 pontos cada vez que um 
                    # bloco é atingido e "removido".
            pontuacao += 10
            
            # Limpa o texto atual do placar para evitar 
                    # sobreposições ou erros de visualização.
            exibir_pontuacao.clear()
            
            # Atualiza o placar exibindo a nova pontuação e o 
                    # nível atual do jogo.
            exibir_pontuacao.write(f"Pontuação: {pontuacao}  Nível: {nivel}", 
                                   align="center", 
                                   font=("Courier", 24, "normal"))
            
            # Sai do loop após a primeira colisão detectada para evitar 
                    # múltiplos blocos sendo removidos em um 
                    # único movimento da bola.
            break


    # Verifica se a lista 'blocos' está vazia, o que 
            # indica que todos os blocos foram destruídos.
    if not blocos:
        
        # Incrementa o 'nivel' por 1, avançando o jogo 
                # para o próximo nível.
        nivel += 1
        
        # Reposiciona a bola no centro da tela para 
                # começar o novo nível.
        bola.goto(0, 0)
        
        # Ajusta a velocidade horizontal da bola multiplicando a 
                # velocidade inicial pela variável 'nivel'.
        # Isso faz com que a bola fique progressivamente mais 
                # rápida a cada nível.
        bola.dx = velocidade_inicial_dx * nivel
        
        # Ajusta a velocidade vertical da bola da mesma forma, 
                # aumentando a dificuldade a cada nível.
        bola.dy = velocidade_inicial_dy * nivel
        
        # Limpa o placar atual para evitar sobreposição de texto.
        exibir_pontuacao.clear()
        
        # Atualiza o placar exibindo a pontuação atual e o novo nível.
        exibir_pontuacao.write(f"Pontuação: {pontuacao}  Nível: {nivel}", 
                               align="center", 
                               font=("Courier", 24, "normal"))
        
        # Chama a função 'criar_blocos' para gerar um novo 
                # conjunto de blocos para o novo nível.
        criar_blocos()
    
    # Configura um temporizador para chamar a função 'loop_jogo' 
            # após um breve intervalo de 10 milissegundos.
    # Esta chamada recursiva mantém o loop do jogo 
            # executando continuamente.
    janela.ontimer(loop_jogo, 10)




# Chama a função 'loop_jogo' para iniciar o loop principal do jogo.
# Esta é a primeira chamada para o loop que controlará as dinâmicas 
        # do jogo, como movimentos da bola, colisões e 
        # atualizações do placar.
loop_jogo()

# Entra no loop principal da janela do turtle.
# 'mainloop' é uma função do 'turtle' que mantém a janela 
        # aberta, aguardando eventos como cliques e 
        # pressionamento de teclas.
# Isso permite que o jogo continue rodando e respondendo a 
        # interações do usuário até que a janela seja fechada.
janela.mainloop()