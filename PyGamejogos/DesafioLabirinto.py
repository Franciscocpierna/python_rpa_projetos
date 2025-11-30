# Importa o módulo tkinter para criar interfaces gráficas.
import tkinter as tk

# Importa messagebox de tkinter, usado para mostrar caixas de 
        # diálogo (como alertas e prompts).
from tkinter import messagebox

# Importa a biblioteca PIL (Python Imaging Library) para lidar com
        # imagens, útil para manipular e exibir imagens.
from PIL import Image, ImageTk

# Configurações iniciais para definir o tamanho da janela do jogo.
# Define a largura da janela do jogo em pixels.
largura_janela = 800

# Define a altura da janela do jogo em pixels.
altura_janela = 600


# Define a classe Labirinto, que contém toda a 
        # lógica e interfaces do jogo.
class Labirinto:
    
    # Método construtor da classe, chamado quando uma instância é criada.
    def __init__(self, master):
        
        # 'master' é a janela principal do Tkinter onde os 
                # elementos gráficos são colocados.
        self.master = master
        
        # Define o título da janela do jogo.
        self.master.title("Desafio no Labirinto")
        
        # Configura as dimensões da janela com base nas variáveis 
                # pré-definidas de largura e altura.
        self.master.geometry(f"{largura_janela}x{altura_janela}")
        
        # Impede que a janela seja redimensionada, o que ajuda a 
                # manter a consistência da interface.
        self.master.resizable(False, False)
        
        # Variáveis de controle para gerenciar o estado do jogo.
        self.fase_atual = 1  # Controla em qual fase o jogo se encontra.
        self.jogador = None  # Mantém uma referência ao objeto gráfico que representa o jogador.
        self.jogo_iniciado = False  # Indica se o jogo foi iniciado.
        self.jogo_finalizado = False  # Indica se o jogo foi concluído em todas as fases.
        
        # Cria um objeto Canvas dentro da janela principal, 
                # onde o labirinto será desenhado.
        self.canvas = tk.Canvas(self.master, 
                                width=largura_janela, 
                                height=altura_janela,
                                bg="black")
        
        # Adiciona o Canvas à janela principal.
        self.canvas.pack()
        
        # Chama o método para criar o labirinto, que 
                # será explicado separadamente.
        self.criar_labirinto()
        
        # Registra eventos de clique e movimento do 
                # mouse para controlar o jogo.
        # Clique esquerdo do mouse inicia o jogo.
        self.master.bind("<Button-1>", self.iniciar_jogo)
        
        # Movimento do mouse move o jogador pelo labirinto.
        self.master.bind("<Motion>", self.mover_jogador)


    def criar_labirinto(self):
    
        # Remove qualquer desenho anterior do Canvas para garantir 
                # que um novo labirinto possa ser desenhado sem sobreposição.
        self.canvas.delete("all")
    
        # A lógica condicional a seguir decide qual função de desenho 
                # de labirinto chamar com base na fase atual do jogo.
        if self.fase_atual == 1:            
            self.fase1()  # Chama a função que desenha o labirinto da fase 1.
        elif self.fase_atual == 2:
            self.fase2()  # Chama a função que desenha o labirinto da fase 2.
        elif self.fase_atual == 3:
            self.fase3()  # Chama a função que desenha o labirinto da fase 3.
        elif self.fase_atual == 4:
            self.fase4()  # Chama a função que desenha o labirinto da fase 4.
        elif self.fase_atual == 5:
            self.fase5()  # Chama a função que desenha o labirinto da fase 5.
        elif self.fase_atual == 6:
            self.fase6()  # Chama a função que desenha o labirinto da fase 6.
        elif self.fase_atual == 7:
            self.fase7()  # Chama a função que desenha o labirinto da fase 7.
        elif self.fase_atual == 8:
            self.fase8()  # Chama a função que desenha o labirinto da fase 8.
        elif self.fase_atual == 9:
            self.fase9()  # Chama a função que desenha o labirinto da fase 9.
        else:
            
            # Se todas as fases foram concluídas, chama a função
                    # que exibe uma mensagem de felicitações.
            self.exibir_congratulations()

            # Interrompe a função para não redefinir 'jogo_iniciado' 
                    # se o jogo estiver concluído.
            return  
    
        # Reinicializa a flag para indicar que o jogo 
                # ainda não começou na nova fase.
        self.jogo_iniciado = False


    def fase1(self):
        
        # Cria um retângulo azul que serve como área inicial 
                # onde o jogador começa.
        # (50, 500) é o ponto superior esquerdo e (100, 550) é o 
                # ponto inferior direito do retângulo.
        self.area_inicial = self.canvas.create_rectangle(50, 500, 100, 550, fill="blue", outline="blue")
        
        # Desenha a primeira parte do caminho que o jogador deve 
                # seguir, usando uma linha cyan.
        # A linha começa no meio da área inicial (75, 500) e 
                # vai verticalmente até (75, 100).
        self.canvas.create_line(75, 500, 75, 100, fill="cyan", width=30)
        
        # Continua o caminho horizontalmente da extremidade da 
                # primeira linha até (600, 100).
        # Essa linha forma um "L" com a primeira, delineando o
                # caminho que o jogador deve seguir.
        self.canvas.create_line(75, 100, 600, 100, fill="cyan", width=30)
        
        # Adiciona um texto na tela indicando a fase atual,
                # posicionado em (400, 50).
        # "Fase 1" é exibido com fonte Arial, tamanho 24 e cor branca.
        self.canvas.create_text(400, 50, text="Fase 1", fill="white", font=("Arial", 24))
        
        # Cria uma representação oval (círculo) para o jogador.
        # (60, 540) e (80, 560) são os pontos que definem a 
                # extensão do círculo, com a cor roxa.
        self.jogador = self.canvas.create_oval(60, 540, 80, 560, fill="purple")
        
        # Define a área de saída do labirinto, onde o jogador
                # deve chegar para completar a fase.
        # Esta área é um retângulo vermelho localizado em (580, 80) a
                # (620, 120), sem contorno.
        self.saida = self.canvas.create_rectangle(580, 80, 620, 120, fill="red", outline="red")


    def fase2(self):
        
        # Desenha a área inicial onde o jogador começa a fase. 
        # A área é um retângulo com as bordas e o preenchimento em azul.
        # (50, 500) é o canto superior esquerdo e (100, 550) é
                # o canto inferior direito.
        self.area_inicial = self.canvas.create_rectangle(50, 500, 100, 550, fill="blue", outline="blue")
        
        # Desenha a primeira parte do caminho que o jogador deve seguir.
        # Esta linha vai verticalmente de (75, 500) até (75, 300).
        # A linha tem 30 pixels de largura e é colorida em cyan.
        self.canvas.create_line(75, 500, 75, 300, fill="cyan", width=30)
        
        # Desenha a segunda parte do caminho, que vai horizontalmente
                # da extremidade da primeira linha até (300, 300).
        self.canvas.create_line(75, 300, 300, 300, fill="cyan", width=30)
        
        # Desenha a terceira parte do caminho que vai verticalmente 
                # para cima, de (300, 300) até (300, 150).
        self.canvas.create_line(300, 300, 300, 150, fill="cyan", width=30)
        
        # Adiciona um texto na tela para indicar que esta é a "Fase 2".
        # O texto está posicionado no centro da parte superior da 
                # tela, com fonte Arial tamanho 24 em cor branca.
        self.canvas.create_text(400, 50, text="Fase 2", fill="white", font=("Arial", 24))
        
        # Cria uma representação oval para o jogador, que é o
                # avatar que o jogador move.
        # Esta oval está localizada começando em (60, 540) e 
                # terminando em (80, 560).
        # A cor do jogador é roxa, o que ajuda a se destacar 
                # contra o caminho cyan e o fundo preto.
        self.jogador = self.canvas.create_oval(60, 540, 80, 560, fill="purple")
        
        # Define a área de saída, onde o jogador deve chegar
                # para completar a fase.
        # Esta é um retângulo localizado em (280, 130) a (320, 170),
                # preenchido de vermelho com contorno também vermelho.
        self.saida = self.canvas.create_rectangle(280, 130, 320, 170, fill="red", outline="red")

    
    def fase3(self):
        
        # Cria um retângulo azul que define a área de partida 
                # onde o jogador começa nesta fase.
        # O retângulo é posicionado com o canto superior
                # esquerdo em (50, 500) e o inferior direito em (100, 550).
        self.area_inicial = self.canvas.create_rectangle(50, 500, 100, 550, fill="blue", outline="blue")
        
        # Desenha uma linha vertical que parte da área de 
                # partida até o topo do Canvas.
        # Esta linha serve como parte do caminho que o jogador deve seguir.
        self.canvas.create_line(75, 500, 75, 100, fill="cyan", width=30)
        
        # Continua o caminho horizontalmente da parte superior 
                # da linha vertical até a coordenada x=400.
        # Isso estende o caminho que o jogador precisa seguir.
        self.canvas.create_line(75, 100, 400, 100, fill="cyan", width=30)
        
        # Desenha outra linha vertical, agora partindo da 
                # extremidade da linha horizontal anterior até a
                # parte inferior do Canvas.
        # Isso forma um "L" invertido, aumentando a complexidade do caminho.
        self.canvas.create_line(400, 100, 400, 400, fill="cyan", width=30)
        
        # Adiciona um texto na tela para indicar que esta é a "Fase 3".
        # O texto é posicionado centralmente na parte superior 
                # do Canvas, com fonte Arial tamanho 24 e cor branca.
        self.canvas.create_text(400, 50, text="Fase 3", fill="white", font=("Arial", 24))
        
        # Define a posição inicial do jogador, criando um 
                # oval roxo no Canvas.
        # As coordenadas do oval são ajustadas para que o 
                # centro do jogador esteja na linha de partida.
        self.jogador = self.canvas.create_oval(60, 540, 80, 560, fill="purple")
        
        # Cria a área de saída do labirinto, um retângulo vermelho 
                # onde o jogador deve chegar para completar a fase.
        # A saída é definida com um contorno vermelho para maior
                # visibilidade e posicionada estrategicamente ao final do caminho.
        self.saida = self.canvas.create_rectangle(380, 380, 420, 420, fill="red", outline="red")


    def fase4(self):
        
        # Cria um retângulo azul que marca a área de partida do
                # jogador nesta fase do jogo.
        # As coordenadas (50, 500) até (100, 550) delimitam o
                # retângulo na tela.
        self.area_inicial = self.canvas.create_rectangle(50, 500, 100, 550, fill="blue", outline="blue")
        
        # Desenha a primeira parte do caminho que o jogador deve
                # seguir, uma linha vertical.
        # A linha se estende de (75, 500) até (75, 200), usando uma 
                # largura de 30 pixels para facilidade de navegação.
        self.canvas.create_line(75, 500, 75, 200, fill="cyan", width=30)
        
        # Desenha uma linha horizontal que se estende da extremidade 
                # da primeira linha até (700, 200).
        # Esta linha é mais estreita, com apenas 20 pixels de 
                # largura, aumentando o desafio da navegação.
        self.canvas.create_line(75, 200, 700, 200, fill="cyan", width=20)
        
        # A terceira linha é desenhada verticalmente de (700, 200) até (700, 400).
        # Com 20 pixels de largura, esta linha é um pouco mais 
                # grossa, oferecendo uma variação visual e tátil.
        self.canvas.create_line(700, 200, 700, 400, fill="cyan", width=20)
        
        # A última linha da fase retorna horizontalmente
                # de (700, 400) até (150, 400).
        # Com 30 pixels de largura, esta linha oferece uma 
                # sensação de retorno ou conclusão do percurso.
        self.canvas.create_line(700, 400, 150, 400, fill="cyan", width=30)
        
        # Adiciona um texto indicativo da fase atual, "Fase 4".
        # Localizado centralmente na parte superior do canvas, 
                # ajuda a contextualizar o estágio do jogo para o jogador.
        self.canvas.create_text(400, 50, text="Fase 4", fill="white", font=("Arial", 24))
        
        # Define a posição inicial do jogador com um oval roxo.
        # A localização e cor facilitam a identificação do
                # jogador no início da fase.
        self.jogador = self.canvas.create_oval(60, 540, 80, 560, fill="purple")
        
        # Marca a área de saída, um objetivo para o jogador 
                # alcançar para completar a fase.
        # A saída é visualmente distinta com a cor vermelha e
                # está localizada em (130, 380) a (170, 420).
        self.saida = self.canvas.create_rectangle(130, 380, 170, 420, fill="red", outline="red")


    def fase5(self):
        
        # Define a área inicial do jogador como um retângulo azul.
        # As coordenadas (50, 500) até (100, 550) definem um
                # retângulo que marca a posição de partida do jogador.
        self.area_inicial = self.canvas.create_rectangle(50, 500, 100, 550, fill="blue", outline="blue")
    
        # Repete o retângulo, garantindo que a área inicial 
                # seja claramente marcada.
        self.canvas.create_rectangle(50, 550, 100, 500, fill="blue")
    
        # Desenha a primeira parte do caminho vertical que o jogador
                # deve seguir, da área inicial até a parte superior do canvas.
        self.canvas.create_line(75, 500, 75, 100, fill="cyan", width=30)
    
        # Desenha uma linha horizontal que se estende da parte superior 
                # do caminho vertical até o lado direito do canvas.
        self.canvas.create_line(75, 100, 700, 100, fill="cyan", width=30)
    
        # Desenha outra linha vertical do final da linha horizontal 
                # até quase o fundo do canvas.
        self.canvas.create_line(700, 100, 700, 500, fill="cyan", width=20)
    
        # Retorna com uma linha horizontal no fundo do canvas da 
                # direita para a esquerda até cerca de 200 px da borda esquerda.
        self.canvas.create_line(700, 500, 200, 500, fill="cyan", width=30)
    
        # Desenha uma linha vertical final que sobe do final da 
                # linha horizontal até a altura de 300 px, finalizando o caminho.
        self.canvas.create_line(200, 500, 200, 300, fill="cyan", width=20)
    
        # Adiciona um texto no topo da tela para indicar a fase do
                # jogo, ajudando na orientação do jogador.
        self.canvas.create_text(400, 50, text="Fase 5", fill="white", font=("Arial", 24))
        
        # Cria a posição inicial do jogador com um oval roxo, 
                # facilitando sua identificação visual no jogo.
        self.jogador = self.canvas.create_oval(60, 540, 80, 560, fill="purple")
    
        # Define a área de saída onde o jogador deve chegar
                # para concluir a fase.
        # A saída é um retângulo vermelho, visivelmente
                # distinto e estrategicamente colocado.
        self.saida = self.canvas.create_rectangle(180, 280, 220, 320, fill="red")


    def fase6(self):
        
        # Define a área de partida como um retângulo azul, marcando
                # claramente onde o jogador deve iniciar a fase.
        # As coordenadas do retângulo são configuradas de modo que o
                # topo esteja em 500 e o fundo em 550.
        self.area_inicial = self.canvas.create_rectangle(50, 550, 100, 500, fill="blue", outline="blue")
    
        # Desenha uma linha vertical que vai da área de partida até o 
                # topo do canvas, marcando um dos caminhos possíveis.
        self.canvas.create_line(75, 500, 75, 100, fill="cyan", width=30)
    
        # Estende uma linha horizontal da parte superior da linha 
                # vertical anterior até a coordenada x=300.
        self.canvas.create_line(75, 100, 300, 100, fill="cyan", width=30)
    
        # Desenha uma linha vertical que desce até a coordenada y=400, 
                # formando um caminho mais longo e variado.
        self.canvas.create_line(300, 100, 300, 400, fill="cyan", width=20)
    
        # Conecta uma linha horizontal que vai da coordenada x=300 
                # até x=550, criando complexidade no percurso.
        self.canvas.create_line(300, 400, 550, 400, fill="cyan", width=20)
    
        # Desenha outra linha vertical que sobe até a coordenada y=150, 
                # formando um percurso que requer atenção e habilidade.
        self.canvas.create_line(550, 400, 550, 150, fill="cyan", width=30)
    
        # Fecha o percurso com uma linha horizontal que vai até o lado 
                # direito do canvas, marcando o caminho final para a saída.
        self.canvas.create_line(550, 150, 750, 150, fill="cyan", width=20)
        
        # Adiciona um texto na parte superior do canvas para indicar 
                # que o jogador está na "Fase 6".
        # O texto é centralizado e grande o suficiente para 
                # ser facilmente visível.
        self.canvas.create_text(400, 50, text="Fase 6", fill="white", font=("Arial", 24))
        
        # Cria o avatar do jogador como um oval roxo, posicionado na
                # área inicial, destacando-se contra o fundo e o caminho.
        self.jogador = self.canvas.create_oval(60, 540, 80, 560, fill="purple")
        
        # Define a saída do labirinto como um retângulo vermelho, 
                # localizado estrategicamente para ser o objetivo do percurso.
        # A saída é destacada com um contorno vermelho para ser 
                # claramente identificável.
        self.saida = self.canvas.create_rectangle(730, 130, 770, 170, fill="red", outline="red")

    
    def fase7(self):
        
        # Define a área inicial do jogador como um retângulo azul
                # na parte inferior do canvas.
        self.area_inicial = self.canvas.create_rectangle(50, 550, 100, 500, fill="blue", outline="blue")
    
        # Desenha uma linha vertical que se estende da área
                # inicial até o topo do canvas.
        self.canvas.create_line(75, 500, 75, 100, fill="cyan", width=30)
    
        # Conecta uma linha horizontal da parte superior da linha 
                # vertical até a coordenada x=200.
        self.canvas.create_line(75, 100, 200, 100, fill="cyan", width=30)
    
        # Desenha uma linha vertical descendo até a altura de y=250.
        self.canvas.create_line(200, 100, 200, 250, fill="cyan", width=30)
    
        # Cria uma linha horizontal que se estende até x=450.
        self.canvas.create_line(200, 250, 450, 250, fill="cyan", width=20)
    
        # Desenha outra linha vertical que sobe até y=50, 
                # formando um caminho mais alto.
        self.canvas.create_line(450, 250, 450, 50, fill="cyan", width=30)
    
        # Conecta uma linha horizontal estendendo-se até x=650.
        self.canvas.create_line(450, 50, 650, 50, fill="cyan", width=20)
    
        # Desenha uma linha vertical que desce até y=350.
        self.canvas.create_line(650, 50, 650, 350, fill="cyan", width=30)
    
        # Adiciona uma linha horizontal que se estende de volta 
                # até x=300, fechando quase um circuito.
        self.canvas.create_line(650, 350, 300, 350, fill="cyan", width=30)
    
        # Completa o caminho com uma linha vertical que desce até a 
                # parte inferior do canvas e outra linha horizontal
                # para fechar o circuito.
        self.canvas.create_line(300, 350, 300, 550, fill="cyan", width=30)
        self.canvas.create_line(300, 550, 750, 550, fill="cyan", width=30)
    
        # Exibe um texto na parte superior central do canvas
                # indicando que esta é a "Fase 7".
        self.canvas.create_text(400, 50, text="Fase 7", fill="white", font=("Arial", 24))
    
        # Define a posição inicial do jogador com um oval 
                # roxo na área inicial.
        self.jogador = self.canvas.create_oval(60, 540, 80, 560, fill="purple")
    
        # Define a área de saída como um retângulo vermelho na parte
                # inferior do canvas, marcando o objetivo final.
        self.saida = self.canvas.create_rectangle(730, 530, 770, 570, fill="red", outline="red")


    def fase8(self):
        
        # Configura a área inicial do jogador como um retângulo azul.
        # Este retângulo está localizado na parte inferior do canvas,
                # servindo como ponto de partida.
        self.area_inicial = self.canvas.create_rectangle(50, 550, 100, 500, fill="blue", outline="blue")
    
        # Desenha uma linha vertical do ponto de partida até 
                # quase o topo do canvas.
        # Esta linha serve como o primeiro caminho que o jogador deve seguir.
        self.canvas.create_line(75, 500, 75, 100, fill="cyan", width=30)
    
        # Cria uma linha horizontal que se estende para a direita, 
                # adicionando complexidade ao percurso.
        self.canvas.create_line(75, 100, 200, 100, fill="cyan", width=30)
    
        # Desenha outra linha vertical descendo de volta à
                # parte inferior do canvas.
        # Esta linha adiciona mais desafio ao fazer o jogador voltar 
                # na mesma direção de onde veio.
        self.canvas.create_line(200, 100, 200, 500, fill="cyan", width=30)
    
        # Cria uma linha horizontal mais longa na parte inferior, 
                # movendo-se mais para a direita.
        self.canvas.create_line(200, 500, 400, 500, fill="cyan", width=30)
    
        # Desenha outra linha vertical subindo, mas desta vez
                # parando a meio caminho.
        # Isso cria uma variação na altura que o jogador precisa alcançar.
        self.canvas.create_line(400, 500, 400, 200, fill="cyan", width=30)
    
        # Adiciona uma linha horizontal estreita que se estende
                # ainda mais para a direita.
        self.canvas.create_line(400, 200, 600, 200, fill="cyan", width=20)
    
        # Desenha uma linha vertical descendo até quase o fundo do
                # canvas, mas parando em uma altura média.
        self.canvas.create_line(600, 200, 600, 400, fill="cyan", width=30)
    
        # Finaliza o caminho com uma linha horizontal até o final do canvas.
        # Este é o último caminho antes de alcançar a saída.
        self.canvas.create_line(600, 400, 750, 400, fill="cyan", width=30)
    
        # Insere um texto na parte superior do canvas para informar ao
                # jogador que ele está na "Fase 8".
        # A cor branca e a fonte grande (Arial, 24) garantem visibilidade e clareza.
        self.canvas.create_text(400, 50, text="Fase 8", fill="white", font=("Arial", 24))
        
        # Define a posição inicial do jogador, representada por um oval roxo.
        # Esta cor contrastante facilita a identificação do jogador no labirinto.
        self.jogador = self.canvas.create_oval(60, 540, 80, 560, fill="purple")
    
        # Marca a área de saída, um retângulo vermelho que indica onde o
                # jogador deve chegar para completar a fase.
        # O retângulo está estrategicamente localizado para encorajar o progresso através do labirinto.
        self.saida = self.canvas.create_rectangle(730, 380, 770, 420, fill="red", outline="red")

    
    
    def fase9(self):
        
        # Define a área inicial do jogador como um retângulo azul
                # na parte inferior do canvas.
        # Este retângulo serve como ponto de partida onde o jogador
                # começa o percurso.
        self.area_inicial = self.canvas.create_rectangle(50, 550, 100, 500, fill="blue", outline="blue")
    
        # Desenha uma linha vertical a partir da área inicial
                # até o topo do canvas.
        # A linha é cyan e tem largura de 30 pixels, facilitando o
                # reconhecimento visual.
        self.canvas.create_line(75, 500, 75, 50, fill="cyan", width=30)
    
        # Cria uma linha horizontal estreita (10 pixels de largura) que
                # vai até x=300, adicionando desafio ao percurso.
        # Esse estreitamento exige maior precisão do jogador.
        self.canvas.create_line(75, 50, 300, 50, fill="cyan", width=20)
    
        # Desenha uma linha vertical para baixo de x=300 até y=250, 
                # ainda com 20 pixels de largura.
        # Mantém a necessidade de precisão, forçando o jogador a
                # seguir um trajeto bem definido.
        self.canvas.create_line(300, 50, 300, 250, fill="cyan", width=20)
    
        # Adiciona uma linha horizontal que vai de x=300 até x=100 na altura de y=250.
        # A linha continua estreita, aumentando a dificuldade do percurso.
        self.canvas.create_line(300, 250, 100, 250, fill="cyan", width=20)
    
        # Desenha uma linha vertical que desce de y=250 até y=400 em x=100.
        # A linha continua com 20 pixels de largura, exigindo precisão do jogador.
        self.canvas.create_line(100, 250, 100, 400, fill="cyan", width=20)
    
        # Conecta uma linha horizontal para a direita que vai de
                # x=100 até x=500 na altura de y=400.
        # Esta linha é uma reta longa e contínua, mas estreita, 
                # tornando o caminho um pouco mais difícil.
        self.canvas.create_line(100, 400, 500, 400, fill="cyan", width=20)
    
        # Adiciona uma linha vertical mais larga (30 pixels de largura) 
                # que sobe de y=400 até y=150 em x=500.
        # Essa linha fornece um caminho um pouco mais fácil em 
                # largura, compensando a extensão.
        self.canvas.create_line(500, 400, 500, 150, fill="cyan", width=30)
    
        # Cria uma linha horizontal de 30 pixels de largura que
                # vai de x=500 até x=700, na altura de y=150.
        # Ela amplia o percurso, mantendo um trajeto bem marcado.
        self.canvas.create_line(500, 150, 700, 150, fill="cyan", width=30)
    
        # Desenha uma linha vertical que desce de y=150 até y=450 
                # em x=700, com 30 pixels de largura.
        # O jogador precisa descer ao longo desta linha para
                # continuar no percurso.
        self.canvas.create_line(700, 150, 700, 450, fill="cyan", width=30)
    
        # Adiciona uma linha horizontal que vai de x=700 até x=400 na
                # altura de y=450, com 30 pixels de largura.
        # Esta linha aproxima o jogador da saída, criando um
                # trajeto mais fácil de identificar.
        self.canvas.create_line(700, 450, 400, 450, fill="cyan", width=30)
    
        # Desenha uma linha vertical que desce de y=450 até o
                # fundo do canvas em y=550 na coordenada x=400.
        # Esse é o último trecho antes da área de saída.
        self.canvas.create_line(400, 450, 400, 550, fill="cyan", width=30)
    
        # Adiciona um texto na parte superior do canvas que
                # indica ao jogador que ele está na "Fase 9".
        # Este texto é centralizado e usa uma fonte Arial grande,
                # facilitando a visualização.
        self.canvas.create_text(400, 50, text="Fase 9", fill="white", font=("Arial", 24))
    
        # Define a posição inicial do jogador como um oval roxo na área inicial.
        # A cor roxa se destaca no canvas, facilitando a localização do jogador.
        self.jogador = self.canvas.create_oval(60, 540, 80, 560, fill="purple")
    
        # Define a área de saída como um retângulo vermelho 
                # perto do final do percurso.
        # Este retângulo é o objetivo final do jogador, que deve 
                # alcançá-lo para completar a fase.
        self.saida = self.canvas.create_rectangle(380, 530, 420, 570, fill="red", outline="red")



    def iniciar_jogo(self, event):
        
        # Obtém as coordenadas da área inicial (quadrado azul) no 
                # formato (x1, y1, x2, y2).
        # `x1, y1` representam o canto superior esquerdo e `x2, y2` 
                # representam o canto inferior direito.
        x1, y1, x2, y2 = self.canvas.coords(self.area_inicial)
        
        # Verifica se o clique do jogador (event.x e event.y) ocorreu
                # dentro da área inicial.
        # `event.x` e `event.y` representam a posição do clique do 
                # mouse no eixo x e y, respectivamente.
        # A condição `x1 <= event.x <= x2` garante que o clique esteja 
                # dentro das bordas esquerda e direita do quadrado.
        # A condição `y1 <= event.y <= y2` garante que o clique esteja 
                # dentro das bordas superior e inferior do quadrado.
        # Também verifica se o jogo ainda não foi iniciado (`not self.jogo_iniciado`) e
                # não foi finalizado (`not self.jogo_finalizado`).
        if x1 <= event.x <= x2 and y1 <= event.y <= y2 and not self.jogo_iniciado and not self.jogo_finalizado:
            
            # Define `self.jogo_iniciado` como True, indicando que o jogo começou.
            # Isso impede que o jogador reinicie o jogo acidentalmente 
                    # com outro clique na área inicial.
            self.jogo_iniciado = True


    def mover_jogador(self, event):
        
        # Verifica se o jogo foi iniciado (`self.jogo_iniciado` é True) e 
                # se não foi finalizado (`self.jogo_finalizado` é False).
        # Se o jogo ainda não começou ou já foi finalizado, a função 
                # retorna e o movimento é impedido.
        if not self.jogo_iniciado or self.jogo_finalizado:

            # Só permite o movimento se o jogo estiver 
                    # iniciado e não finalizado
            return  
    
        # Atualiza a posição do jogador no canvas de acordo com a 
                # posição atual do cursor do mouse.
        # `event.x` e `event.y` capturam as coordenadas x e y do mouse.
        # `self.canvas.coords(self.jogador, x-10, y-10, x+10, y+10)` ajusta o 
                # jogador para que ele se mova junto com o mouse,
        # reposicionando o oval centralizado em torno do cursor.
        x, y = event.x, event.y
        self.canvas.coords(self.jogador, x-10, y-10, x+10, y+10)
    
        # Chama a função `verificar_colisao` para checar se o jogador
                # tocou em áreas não permitidas (como áreas pretas).
        # Se `verificar_colisao` retornar False, significa que 
                # houve uma colisão.
        if not self.verificar_colisao(x, y):
            
            # Exibe uma mensagem de "Fim de Jogo" caso o jogador
                    # toque em uma área preta.
            # `messagebox.showinfo` cria uma janela informativa
                    # que avisa o jogador sobre o erro.
            messagebox.showinfo("Fim de Jogo", "Você tocou na área preta! Voltando à Fase 1.")
            
            # Reinicia o jogo ao chamar a função `reiniciar_jogo`, que
                    # retorna o jogador à primeira fase.
            self.reiniciar_jogo()
    
        # Verifica se o jogador alcançou a área de saída ao 
                # chamar a função `verificar_chegada`.
        # Se `verificar_chegada` retornar True, o jogador avançará
                # para a próxima fase.
        if self.verificar_chegada():
            
            # Avança para a próxima fase ao chamar `proxima_fase`.
            # Isso atualiza o layout e configura a fase seguinte.
            self.proxima_fase()


    def verificar_colisao(self, x, y):
        
        # Encontra todos os itens gráficos que estão sobrepostos 
                # na posição atual do jogador.
        # `self.canvas.find_overlapping(x-10, y-10, x+10, y+10)` 
                # retorna uma lista de todos os itens
        # que estão dentro da área ao redor do jogador (um quadrado 
                # de 20x20 pixels, centrado no ponto x, y).
        itens_sobrepostos = self.canvas.find_overlapping(x-0, y-0, x+0, y+0)
    
        # Itera sobre cada item encontrado na área de sobreposição para 
                # verificar se o jogador está em uma área segura.
        # Áreas seguras têm as cores "cyan", "blue" ou "red", indicando 
                # que o jogador está no caminho ou na saída.
        for item in itens_sobrepostos:
            
            # `self.canvas.itemcget(item, "fill")` obtém a cor de 
                    # preenchimento (fill color) do item atual.
            cor = self.canvas.itemcget(item, "fill")
            
            # Verifica se a cor do item atual é uma das cores 
                    # seguras ("cyan", "blue" ou "red").
            # "cyan" indica uma área de caminho, "blue" indica a área 
                    # inicial, e "red" indica a área de saída.
            if cor == "cyan" or cor == "blue" or cor == "red":
                
                return True  # O jogador está em uma área segura, 
                                    # então retorna True.
    
        # Se o loop terminar sem encontrar nenhuma cor segura,
                # significa que o jogador tocou na área preta.
        # Isso indica uma colisão com uma área não permitida, 
                # então a função retorna False.
        return False


    def verificar_chegada(self):
        
        # Obtém as coordenadas do jogador como uma lista de
                # quatro valores (x1, y1, x2, y2).
        # `jogador_coords[0]` e `jogador_coords[1]` representam o 
                # canto superior esquerdo do jogador,
        # enquanto `jogador_coords[2]` e `jogador_coords[3]`
                # representam o canto inferior direito.
        jogador_coords = self.canvas.coords(self.jogador)
        
        # Obtém as coordenadas da área de saída da mesma 
                # forma (x1, y1, x2, y2).
        # `saida_coords` representa os limites da área de 
                # saída (retângulo vermelho).
        saida_coords = self.canvas.coords(self.saida)
    
        # Verifica se o jogador está completamente dentro da área de saída.
        # O jogador é considerado dentro da saída se:
        # - O canto esquerdo do jogador (`jogador_coords[0]`) é maior ou
                # igual ao canto esquerdo da saída (`saida_coords[0]`).
        # - O canto superior do jogador (`jogador_coords[1]`) é maior ou igual
                # ao canto superior da saída (`saida_coords[1]`).
        # - O canto direito do jogador (`jogador_coords[2]`) é menor ou igual 
                # ao canto direito da saída (`saida_coords[2]`).
        # - O canto inferior do jogador (`jogador_coords[3]`) é menor ou igual 
                # ao canto inferior da saída (`saida_coords[3]`).
        return (
            jogador_coords[0] >= saida_coords[0] and
            jogador_coords[1] >= saida_coords[1] and
            jogador_coords[2] <= saida_coords[2] and
            jogador_coords[3] <= saida_coords[3]
        )

    
    def reiniciar_jogo(self):
        
        # Reinicia o jogo, definindo a fase atual para 1.
        # Isso garante que o jogador volte ao início do jogo,
                # começando pela primeira fase.
        self.fase_atual = 1
    
        # Define `self.jogo_iniciado` como False, sinalizando que o 
                # jogo ainda não foi iniciado nesta nova fase.
        # Essa variável de controle impede movimentos até que o 
                # jogador clique na área inicial para começar.
        self.jogo_iniciado = False
    
        # Chama a função `criar_labirinto` para redesenhar o
                # labirinto da fase 1.
        # Isso limpa a tela e configura o layout do labirinto
                # correspondente à primeira fase, 
                # reiniciando o jogo visualmente e logicamente.
        self.criar_labirinto()


    def proxima_fase(self):
        
        # Incrementa o número da fase em 1, avançando para a próxima fase.
        # `self.fase_atual += 1` atualiza a fase atual, indicando
                # que o jogador completou a fase anterior.
        self.fase_atual += 1
    
        # Verifica se a fase atual é maior que 9, o que significa que o 
                # jogador concluiu todas as fases do jogo.
        # Se `self.fase_atual` ultrapassar 9, o jogo é finalizado
                # exibindo uma mensagem de parabéns.
        if self.fase_atual > 9:
            
            # Chama a função `exibir_congratulations` para mostrar 
                    # uma tela de congratulações.
            # Isso indica que o jogador completou com sucesso 
                    # todas as fases.
            self.exibir_congratulations()
            
        else:
            
            # Caso ainda existam fases a serem jogadas, chama a 
                    # função `criar_labirinto`.
            # `criar_labirinto` redesenha o layout para a próxima fase,
                    # ajustando o labirinto e reposicionando o jogador.
            self.criar_labirinto()


    def exibir_congratulations(self):
        
        # Limpa todos os elementos atuais do canvas, preparando-o
                # para exibir a imagem final.
        # `self.canvas.delete("all")` remove todos os elementos
                # gráficos do canvas.
        self.canvas.delete("all")
    
        # Carrega a imagem de parabéns chamada "congratulations.png".
        # `Image.open("congratulations.png")` abre o arquivo de 
                # imagem usando a biblioteca Pillow.
        img = Image.open("congratulations.png")
    
        # Redimensiona a imagem para ocupar toda a tela de jogo,
                # conforme as dimensões especificadas.
        # `img.resize((largura_janela, altura_janela), Image.LANCZOS)`
                # ajusta a imagem para o tamanho do canvas,
                # garantindo que ela preencha a tela. O filtro `Image.LANCZOS`
                # proporciona uma boa qualidade ao redimensionar.
        img = img.resize((largura_janela, altura_janela), Image.LANCZOS)
    
        # Converte a imagem redimensionada para um formato compatível 
                # com o Tkinter (`ImageTk.PhotoImage`).
        # Isso permite que a imagem seja exibida no canvas do Tkinter.
        self.congratulations_img = ImageTk.PhotoImage(img)
    
        # Exibe a imagem de parabéns no canvas, ajustada para começar no
                # canto superior esquerdo da tela.
        # `self.canvas.create_image(0, 0, anchor="nw", image=self.congratulations_img)` 
                # coloca a imagem no canvas, onde `anchor="nw"` garante que o
                # canto superior esquerdo (noroeste) da imagem esteja na posição (0, 0).
        self.canvas.create_image(0, 0, anchor="nw", image=self.congratulations_img)
    
        # Define `self.jogo_finalizado` como True, indicando 
                # que o jogo foi concluído.
        # Isso impede que o jogador continue se movendo ou interagindo,
                # pois o jogo chegou ao fim.
        self.jogo_finalizado = True


# Cria a janela principal do Tkinter, chamada `root`, que 
        # será a base da interface do jogo.
root = tk.Tk()

# Cria uma instância da classe `Labirinto`, passando a
        # janela principal (`root`) como parâmetro.
# Isso inicializa todos os elementos do jogo, como o canvas, as
        # fases e os eventos de movimento do jogador.
jogo = Labirinto(root)

# Inicia o loop principal do Tkinter, que mantém a janela 
        # aberta e responde a eventos.
# `root.mainloop()` entra em um loop de execução, onde o Tkinter
        # fica atento a eventos como cliques e movimentos,
        # permitindo que o jogo funcione até que o jogador feche a janela.
root.mainloop()