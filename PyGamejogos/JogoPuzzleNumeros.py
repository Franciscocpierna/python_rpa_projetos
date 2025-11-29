# Importa o módulo pygame, que fornece funcionalidades para a 
        # criação de jogos e interfaces gráficas.
import pygame

# Importa o módulo random, usado para gerar números aleatórios, 
        # crucial para embaralhar peças ou escolher posições aleatórias.
import random

# Importa o módulo sys, utilizado para interagir com o sistema, 
        # permitindo, por exemplo, sair do jogo chamando sys.exit().
import sys

# Importa o módulo os, que fornece uma maneira portátil de usar 
        # funcionalidades dependentes do sistema operacional, 
        # como ler ou escrever arquivos.
import os

# Chama a função init() do módulo pygame, que inicializa todos os 
        # módulos incluídos no pygame, necessários para o 
        # funcionamento correto do jogo.
pygame.init()

# Define a largura da tela do jogo como 500 pixels.
LARGURA_TELA = 500

# Define a altura da tela do jogo como 600 pixels.
ALTURA_TELA = 600

# Define a cor de fundo da tela como cinza claro, usando uma 
        # tupla que representa cores no formato RGB (Red, Green, Blue).
COR_FUNDO = (240, 240, 240)  # Cinza claro

# Define o nome da fonte a ser usada no jogo. 'arial' é 
        # uma escolha comum por sua clareza e legibilidade.
NOME_FONTE = 'arial'

# Cria uma janela ou tela para o jogo, especificando as 
        # dimensões configuradas anteriormente. 
# A função set_mode() do pygame cria uma superfície 
        # representando a janela visível e retorna esta superfície.
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Cria um objeto de fonte no tamanho grande (32 pixels) 
        # usando a fonte Arial.
fonte_grande = pygame.font.SysFont(NOME_FONTE, 32)

# Cria um objeto de fonte no tamanho médio (24 pixels) 
        # usando a fonte Arial.
fonte_media = pygame.font.SysFont(NOME_FONTE, 24)

# Cria um objeto de fonte no tamanho pequeno (18 pixels) 
        # usando a fonte Arial.
fonte_pequena = pygame.font.SysFont(NOME_FONTE, 18)

# Define uma variável global 'arquivo_pontos' para armazenar o 
        # nome do arquivo onde a pontuação do jogo será salva.
arquivo_pontos = 'pontos_puzzle.txt'

# Verifica se o arquivo especificado pela variável 
        # 'arquivo_pontos' existe no sistema de arquivos.
if os.path.exists(arquivo_pontos):
    
    # Se o arquivo existe, abre o arquivo no modo de leitura ('r').
    with open(arquivo_pontos, 'r') as f:
        
        # Lê o conteúdo do arquivo, que espera-se que seja um 
                # número representando a pontuação anterior,
                # converte esse conteúdo de string para inteiro e 
                # armazena na variável 'pontos'.
        pontos = int(f.read())
        
else:
    
    # Se o arquivo não existir, inicializa a variável 'pontos' com o 
            # valor 0, indicando que não há pontuações anteriores.
    pontos = 0


# Define a classe 'PuzzleNumeros', que é responsável por 
        # gerenciar todas as funcionalidades do jogo de 
        # quebra-cabeça numérico.
class PuzzleNumeros:
    
    # Método construtor que inicializa uma nova instância da classe.
    def __init__(self):
        
        # Define o tamanho padrão do tabuleiro como 3x3.
        self.tamanho_tabuleiro = 3  
        
        # Atribui a pontuação carregada do arquivo, se 
                # disponível, ou inicia com 0.
        self.pontos = pontos  
        
        # Cria uma lista vazia para armazenar as peças do quebra-cabeça.
        self.pecas = []  
        
        # Define a margem entre as peças do quebra-cabeça em pixels.
        self.margem_peca = 5  
        
        # Calcula o tamanho de cada peça com base no tamanho da tela e 
                # no número de peças por linha, considerando as margens.
        self.tamanho_peca = int((LARGURA_TELA - ((self.tamanho_tabuleiro + 1) * self.margem_peca)) / self.tamanho_tabuleiro)
        
        # Define a posição inicial do tabuleiro na tela. A margem é 
                # aplicada à esquerda, e a posição vertical começa 
                # a 100 pixels da borda superior.
        self.posicao_tabuleiro = (self.margem_peca, 100)  
        
        # Inicializa uma lista vazia que armazenará a ordem 
                # atual das peças no tabuleiro.
        self.ordem_pecas = []  
        
        # Inicializa uma variável para armazenar o índice da 
                # peça vazia no tabuleiro.
        self.indice_peca_vazia = None  
        
        # Flag para verificar se o jogo foi finalizado.
        self.jogo_finalizado = False  
        
        # Carrega a fonte a ser usada para desenhar texto na 
                # interface, como pontuação e números nas peças.
        self.fonte = pygame.font.SysFont(NOME_FONTE, 32)  
        
        # Chama o método para criar elementos da interface, como 
                # botões e opções de tamanho de tabuleiro.
        self.criar_elementos_interface()  
        
        # Chama o método para inicializar o jogo, configurando o 
                # tabuleiro e embaralhando as peças.
        self.inicializar_jogo() 

    
    def criar_elementos_interface(self):
    
        # Define um botão para testar ou reiniciar o puzzle. O botão é 
                # posicionado centralmente na horizontal e a 60 pixels da borda superior.
        self.botao_testar = pygame.Rect(int(LARGURA_TELA / 2 - 50), 60, 100, 30)
        
        # Renderiza o texto 'Testar' para o botão, usando a fonte pequena, 
                # antialiasing ativado (True), e cor branca (255, 255, 255).
        self.texto_botao_testar = fonte_pequena.render('Testar', True, (255, 255, 255))
        
        # Define opções de tamanho do tabuleiro que podem ser alteradas 
                # pelo jogador, limitadas a tamanhos 3x3 e 4x4.
        # Apenas 3x3 e 4x4 opções de tamanho estão disponíveis.
        self.opcoes_tamanho = [3, 4]  
        
        # Cria uma lista para armazenar os retângulos que representarão 
                # visualmente as opções de tamanho na interface.
        self.retangulos_opcoes_tamanho = []
        
        # Calcula a posição inicial horizontal dos retângulos das 
                # opções de tamanho para que sejam centralizados.
        x_inicial = int(LARGURA_TELA / 2 - (len(self.opcoes_tamanho) * 60) / 2)
        
        # Define a posição vertical inicial dos retângulos 
                # das opções de tamanho.
        y_inicial = 20
        
        # Inicia um loop que percorre cada opção de tamanho disponível no 
                # jogo, que são 3x3 e 4x4, representados pelo vetor self.opcoes_tamanho.
        for i, tamanho in enumerate(self.opcoes_tamanho):
            
            # Dentro do loop, cria um objeto Rect (retângulo) para cada opção de 
                    # tamanho de tabuleiro. O retângulo é criado usando a função pygame.Rect.
            # 'x_inicial + i * 70' calcula a posição x do retângulo, começando de x_inicial e 
                    # movendo-se para a direita 70 pixels para cada nova opção.
            # 'y_inicial' é a posição y do retângulo, que é constante, pois 
                    # todos os retângulos de opções estão na mesma linha horizontal.
            # '60' é a largura de cada retângulo, e '30' é a altura de cada retângulo.
            retangulo = pygame.Rect(x_inicial + i * 70, y_inicial, 60, 30)
            
            # Adiciona cada retângulo criado, juntamente com seu respectivo 
                    # tamanho de tabuleiro, à lista self.retangulos_opcoes_tamanho.
            # Essa lista armazena pares de retângulos e tamanhos, facilitando o 
                    # acesso e a manipulação durante a interação do usuário.
            self.retangulos_opcoes_tamanho.append((retangulo, tamanho))
            
            # Inicializa a variável self.retangulo_tamanho_selecionado com None. 
            # Esta variável é usada para manter o estado do retângulo
                    # do tamanho de tabuleiro atualmente selecionado, 
                    # permitindo destacá-lo visualmente na interface.
            self.retangulo_tamanho_selecionado = None


    def inicializar_jogo(self):
        
        # Recalcula o tamanho de cada peça do tabuleiro com base no 
                # tamanho atual do tabuleiro (3x3 ou 4x4).
        # O cálculo leva em consideração a largura da tela, o número 
                # de peças e as margens entre elas.
        # A fórmula divide o espaço disponível pela quantidade de 
                # peças em uma linha, levando em consideração a 
                # margem entre as peças.
        self.tamanho_peca = int((LARGURA_TELA - ((self.tamanho_tabuleiro + 1) * self.margem_peca)) / self.tamanho_tabuleiro)
        
        # Define a posição inicial do tabuleiro na tela. A posição horizontal é 
                # a margem entre as peças e a borda esquerda da tela.
        # A posição vertical começa a partir de 100 pixels a partir da 
                # parte superior da tela, criando uma área separada para o tabuleiro.
        self.posicao_tabuleiro = (self.margem_peca, 100)
        
        # Gera uma lista com a ordem inicial das peças. A função 'criar_ordem_inicial' 
                # cria uma lista numerada de 1 até o número total de peças,
                # deixando o último espaço como vazio (representado por 'None'). 
        # Esta lista é a configuração inicial do jogo antes de ser embaralhada.
        self.ordem_pecas = self.criar_ordem_inicial(self.tamanho_tabuleiro)
        
        # Embaralha a lista de peças gerada. A função 'embaralhar' reorganiza a 
                # lista aleatoriamente, mas também garante que a configuração 
                # resultante seja possível de resolver, evitando que o 
                # jogador receba um quebra-cabeça insolúvel.
        self.embaralhar(self.ordem_pecas)
        
        # Cria as peças no tabuleiro com base na lista embaralhada. 
        # A função 'criar_pecas' coloca cada peça em sua posição no tabuleiro,
                # associando uma imagem ou número a cada uma, exceto a peça vazia.
        self.criar_pecas()
        
        # Define a flag 'jogo_finalizado' como False, o que indica que o 
                # jogo ainda não foi concluído e que o jogador ainda
                # precisa organizar as peças.
        self.jogo_finalizado = False


    def criar_ordem_inicial(self, tamanho):
    
        # Cria uma lista de números sequenciais, começando de 1 até o 
                # número total de peças (tamanho * tamanho - 1).
        # Isso cria a sequência de peças para um tabuleiro de 
                # NxN (por exemplo, 3x3 ou 4x4).
        ordem = list(range(1, tamanho * tamanho))
        
        # Adiciona 'None' ao final da lista, representando o 
                # espaço vazio no quebra-cabeça.
        # O espaço vazio é essencial para permitir o movimento das
                # peças durante o jogo.
        ordem.append(None)
        
        # Retorna a lista que contém a ordem inicial das 
                # peças (numerada e com um espaço vazio).
        return ordem

    
    def criar_ordem_teste(self, tamanho):
        
        # Cria uma lista de números sequenciais, começando de 1 até o
                # penúltimo número do tabuleiro (tamanho * tamanho - 2).
        # Essa sequência exclui o último número e o espaço vazio,
                # deixando espaço para uma configuração personalizada.
        ordem = list(range(1, tamanho * tamanho - 1))
        
        # Adiciona 'None' ao final da lista, que representa o 
                # espaço vazio no quebra-cabeça.
        ordem.append(None)
        
        # Adiciona o último número ao final da lista, colocando-o 
                # após o espaço vazio.
        # Isso cria uma configuração propositalmente incorreta,
                # onde a peça final está fora de ordem, atrás do espaço vazio.
        ordem.append(tamanho * tamanho - 1)
        
        # Retorna a lista modificada, que agora contém uma
                # configuração específica de teste.
        return ordem


    def embaralhar(self, lista):
        
        # Embaralha a lista de peças de forma aleatória usando a 
                # função 'shuffle' do módulo 'random'.
        random.shuffle(lista)
        
        # Verifica se a configuração atual do tabuleiro é resolvível. 
        # A função 'eh_resolvivel' determina se a configuração do quebra-cabeça
        # pode ser resolvida (se há uma sequência de movimentos possível 
                # para organizar todas as peças na ordem correta).
        # Caso não seja resolvível, o loop continua embaralhando até 
                # encontrar uma configuração válida.
        while not self.eh_resolvivel(lista):
            
            # Se a configuração não for resolvível, embaralha novamente a 
                    # lista até que uma configuração válida seja gerada.
            random.shuffle(lista)

    
    def eh_resolvivel(self, lista):
        
        # Inicializa uma variável para contar o número de 
                # inversões no tabuleiro.
        # Uma inversão ocorre quando um número maior precede
                # um número menor na sequência.
        inversoes = 0
        
        # Remove o valor 'None' (que representa a peça vazia) 
                # da lista de peças.
        # O 'None' não é considerado na contagem de inversões, pois 
                # ele não pode participar das comparações de valores.
        lista_sem_nulos = [num for num in lista if num is not None]
        
        # Itera sobre todos os elementos da lista de peças, exceto o 
                # último, para comparar com os demais.
        # A função verifica cada par de números da lista e conta 
                # quantas inversões existem.
        for i in range(len(lista_sem_nulos)):  
            
            # O segundo loop começa a partir do próximo elemento após 'i', 
                    # para comparar cada número com os números à sua frente na lista.
            for j in range(i + 1, len(lista_sem_nulos)):
                
                # Verifica se há uma inversão: ou seja, se o número atual (lista_sem_nulos[i]) é
                        # maior que o próximo número (lista_sem_nulos[j]).
                # Se sim, isso indica que os números estão fora de ordem em 
                        # relação à sequência correta.
                if lista_sem_nulos[i] > lista_sem_nulos[j]:
                    
                    # Se uma inversão for detectada, incrementa o 
                            # contador de inversões.
                    inversoes += 1
        
        # Verifica se o tamanho do tabuleiro é ímpar.
        # Para tabuleiros ímpares (como 3x3), o quebra-cabeça é resolvível
                # apenas se o número de inversões for par.
        if self.tamanho_tabuleiro % 2 != 0:
            
            # Retorna True se o número de inversões for par, ou 
                    # seja, o quebra-cabeça é resolvível.
            return inversoes % 2 == 0
        
        # Se o tamanho do tabuleiro for par, a posição da peça vazia 
                # também deve ser levada em consideração.
        # Tabuleiros pares (como 4x4) têm regras diferentes 
                # dependendo da linha onde está o espaço vazio.
        else:
            
            # Calcula em qual linha (contada de cima para baixo, 
                    # começando de 0) está a peça vazia.
            # O índice da peça vazia (None) na lista é dividido pelo número de
                    # colunas do tabuleiro para determinar a linha.
            linha_vazia = lista.index(None) // self.tamanho_tabuleiro
            
            # Se a linha onde a peça vazia está for par (0, 2, 4, etc.), o 
                    # número de inversões deve ser ímpar para que o 
                    # quebra-cabeça seja resolvível.
            if linha_vazia % 2 == 0:
                
                # Retorna True se o número de inversões for ímpar, indicando 
                        # que o quebra-cabeça pode ser resolvido.
                return inversoes % 2 != 0
                
            # Se a linha onde a peça vazia está for ímpar (1, 3, 5, etc.), o
                    # número de inversões deve ser par para que o 
                    # quebra-cabeça seja resolvível.
            else:
                
                # Retorna True se o número de inversões for par, indicando 
                        # que o quebra-cabeça pode ser resolvido.
                return inversoes % 2 == 0

                    

    def criar_pecas(self):
    
        # Inicializa uma lista vazia para armazenar as peças do quebra-cabeça.
        self.pecas = []
        
        # Itera sobre cada valor e seu índice correspondente na 
                # lista 'ordem_pecas', que contém a ordem das peças no tabuleiro.
        for idx, valor in enumerate(self.ordem_pecas):
            
            # Calcula a posição x da peça no tabuleiro. O cálculo é feito com
                    # base na posição inicial do tabuleiro e o índice da peça.
            # 'idx % self.tamanho_tabuleiro' encontra a posição da peça na 
                    # linha (coluna), multiplicando pelo tamanho da peça e a margem.
            x = self.posicao_tabuleiro[0] + (idx % self.tamanho_tabuleiro) * (self.tamanho_peca + self.margem_peca)
            
            # Calcula a posição y da peça no tabuleiro. Aqui, 'idx // self.tamanho_tabuleiro' 
                    # encontra em qual linha a peça está,
                    # multiplicando pelo tamanho da peça e a margem 
                    # para obter a posição exata na linha.
            y = self.posicao_tabuleiro[1] + (idx // self.tamanho_tabuleiro) * (self.tamanho_peca + self.margem_peca)
            
            # Cria um objeto 'Rect' (retângulo) para representar a área 
                    # ocupada pela peça no tabuleiro.
            # O retângulo é definido com base na posição x e y calculadas, e
                    # tem as dimensões de 'tamanho_peca' x 'tamanho_peca'.
            retangulo = pygame.Rect(x, y, self.tamanho_peca, self.tamanho_peca)
            
            # Cria um dicionário para representar a peça. O dicionário contém o
                    # retângulo da peça e o valor da peça (número 
                    # ou 'None' se for a peça vazia).
            peca = {'retangulo': retangulo, 'valor': valor}
            
            # Verifica se a peça atual é a peça vazia ('None'). 
            # Se for, armazena o índice da peça vazia.
            if valor is None:
                self.indice_peca_vazia = idx
            
            # Adiciona a peça (dicionário contendo o retângulo e
                    # valor) à lista de peças.
            self.pecas.append(peca)

            
    def desenhar(self, tela):
        
        # Preenche toda a tela com a cor de fundo especificada (COR_FUNDO), 
                # que define o fundo da interface.
        tela.fill(COR_FUNDO)
        
        # Renderiza o texto que exibe a pontuação atual do jogador. Usa a 
                # fonte média e a cor cinza escuro (85, 85, 85).
        # O texto é criado com base no valor da pontuação
                # armazenado em 'self.pontos'.
        texto_pontos = fonte_media.render(f'Pontos: {self.pontos}', True, (85, 85, 85))
        
        # Desenha o texto da pontuação na tela, posicionando-o no 
                # canto superior esquerdo (10, 60).
        tela.blit(texto_pontos, (10, 60))
        
        # Desenha os controles para seleção do tamanho do tabuleiro. 
                # Itera sobre a lista de retângulos de opções de tamanho.
        for retangulo, tamanho in self.retangulos_opcoes_tamanho:
            
            # Desenha um retângulo branco (255, 255, 255) para representar
                    # visualmente as opções de tamanho.
            pygame.draw.rect(tela, (255, 255, 255), retangulo)
            
            # Desenha um contorno cinza claro (204, 204, 204) em volta do
                    # retângulo para destacar a borda.
            pygame.draw.rect(tela, (204, 204, 204), retangulo, 1)
            
            # Renderiza o texto do tamanho do tabuleiro dentro do 
                    # retângulo (ex: '3x3', '4x4'), com a cor cinza escuro (51, 51, 51).
            texto_tamanho = fonte_pequena.render(f'{tamanho}x{tamanho}', True, (51, 51, 51))
            
            # Calcula a posição onde o texto deve ser desenhado, 
                    # centralizando-o dentro do retângulo da opção de tamanho.
            tela.blit(texto_tamanho, (retangulo.x + (retangulo.width - texto_tamanho.get_width()) // 2,
                                      retangulo.y + (retangulo.height - texto_tamanho.get_height()) // 2))
            
            # Se o tamanho atual do tabuleiro for igual ao tamanho desta opção, 
                    # desenha um contorno verde em volta do retângulo
                    # para indicar visualmente que essa opção de
                    # tamanho está selecionada.
            if tamanho == self.tamanho_tabuleiro:
                pygame.draw.rect(tela, (76, 175, 80), retangulo, 2)
        
        # Desenha o botão 'Testar' com um fundo verde (76, 175, 80), 
                # que serve para testar ou reiniciar o jogo.
        pygame.draw.rect(tela, (76, 175, 80), self.botao_testar)
        
        # Desenha o texto 'Testar' centralizado dentro do botão. Calcula a
                # posição para que o texto fique no centro do botão,
                # tanto horizontalmente quanto verticalmente.
        tela.blit(self.texto_botao_testar, (self.botao_testar.x + (self.botao_testar.width - self.texto_botao_testar.get_width()) // 2,
                                            self.botao_testar.y + (self.botao_testar.height - self.texto_botao_testar.get_height()) // 2))

        # Desenhar todas as peças que estão no tabuleiro do jogo.
        for peca in self.pecas:
            
            # Cada peça é representada por um dicionário que 
                    # contém duas informações principais:
            # 1. 'retangulo': a área da peça no tabuleiro (a posição e tamanho dela).
            # 2. 'valor': o número que a peça contém (ou None, se for a peça vazia).
            
            # Armazena o retângulo (área) da peça, que contém a 
                    # posição (x, y) e o tamanho (largura e altura) da peça.
            retangulo = peca['retangulo']
            
            # Armazena o valor da peça, que é o número nela (ou 
                    # None, se for a peça vazia).
            valor = peca['valor']
            
            # Se a peça tiver um número (não for a peça vazia), o 
                    # valor será diferente de 'None'.
            if valor is not None:
                
                # Desenha o retângulo da peça preenchido com a cor
                        # bege (RGB: 255, 218, 185).
                # Esse retângulo é desenhado na posição x e y especificada 
                        # no 'retangulo', com o tamanho da peça.
                pygame.draw.rect(tela, (255, 218, 185), retangulo)
                
                # Desenha um contorno ao redor do retângulo, usando a cor 
                        # preta (RGB: 0, 0, 0) com uma borda de 1 pixel de espessura.
                pygame.draw.rect(tela, (0, 0, 0), retangulo, 1)
                
                # Renderiza o número da peça (seu valor) como um texto. 
                # A função 'render' transforma o valor da peça em uma
                        # imagem de texto, que será desenhada depois.
                # O valor é convertido para string, e a cor do texto é preta (RGB: 0, 0, 0).
                texto_valor = self.fonte.render(str(valor), True, (0, 0, 0))
                
                # Calcula a posição onde o texto (número) será desenhado dentro do retângulo.
                # O cálculo centraliza o número horizontalmente e verticalmente dentro da peça.
                tela.blit(texto_valor, (retangulo.x + (retangulo.width - texto_valor.get_width()) // 2,
                                        retangulo.y + (retangulo.height - texto_valor.get_height()) // 2))
                
            else:
                
                # Se a peça for a peça vazia (None), desenha um retângulo 
                        # com a cor marrom (RGB: 139, 90, 43).
                # Esse retângulo representa o espaço vazio no tabuleiro, 
                        # onde as peças se movem.
                pygame.draw.rect(tela, (139, 90, 43), retangulo)
        
        # Verifica se o jogo foi finalizado, ou seja, se o jogador venceu.
        # Se o jogo terminou, exibe uma mensagem de vitória na tela.
        if self.jogo_finalizado:
            self.mostrar_vitoria(tela)
        
        # Atualiza a tela com todas as mudanças feitas. 
        # Isso inclui as peças desenhadas, os números, as cores e 
                # qualquer outra atualização visual.
        pygame.display.flip()

    
    def lidar_evento(self, evento):
    
        # Verifica se o evento foi um clique do mouse (MOUSEBUTTONDOWN).
        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            # Obtém a posição (x, y) do clique do mouse e armazena em 'posicao'.
            posicao = evento.pos
            
            # Verifica se o clique foi em uma das opções de tamanho do
                    # tabuleiro (como 3x3 ou 4x4).
            for retangulo, tamanho in self.retangulos_opcoes_tamanho:
                
                # Verifica se a posição do clique do mouse está dentro do
                        # retângulo que representa uma opção de tamanho.
                if retangulo.collidepoint(posicao):
                    
                    # Se a posição do clique estiver dentro de uma das opções de tamanho,
                            # muda o tamanho do tabuleiro para o tamanho correspondente.
                    self.tamanho_tabuleiro = tamanho
                    
                    # Após a mudança do tamanho do tabuleiro, reinicializa o jogo 
                            # para recriar o tabuleiro com o novo tamanho e 
                            # embaralha as peças.
                    self.inicializar_jogo()
            
            # Verifica se o clique foi no botão 'Testar', que é responsável por
                    # colocar o jogo em um estado de teste.
            if self.botao_testar.collidepoint(posicao):
                
                # Se o botão 'Testar' foi clicado, cria uma ordem de peças especial de
                        # teste, em que as peças são posicionadas de forma previsível.
                self.ordem_pecas = self.criar_ordem_teste(self.tamanho_tabuleiro)
                
                # Recria todas as peças do tabuleiro com base na nova 
                        # ordem de peças de teste.
                self.criar_pecas()
                
                # Define que o jogo não está finalizado, permitindo que o
                        # jogador continue jogando após o teste.
                self.jogo_finalizado = False
            
            # Verifica se o clique foi em uma das peças do 
                    # tabuleiro (para movê-la).
            for idx, peca in enumerate(self.pecas):
                
                # Se a posição do clique estiver dentro da área (retângulo) que
                        # representa uma das peças do tabuleiro.
                if peca['retangulo'].collidepoint(posicao):
                    
                    # Chama a função 'mover_peca', passando o índice da peça clicada.
                    # A função tentará mover a peça para a posição vazia.
                    self.mover_peca(idx)
                    
                    # Após mover a peça, sai do loop para garantir que
                            # apenas uma peça seja movida por clique.
                    break

                    
    def mover_peca(self, indice_peca):
        
        # Verifica se a jogada é válida. A jogada é válida se a peça 
                # selecionada (indice_peca) estiver adjacente à peça vazia.
        # A função 'jogada_valida' retorna True se a peça clicada puder
                # ser movida para a posição da peça vazia.
        if self.jogada_valida(indice_peca, self.indice_peca_vazia):
            
            # Se a jogada for válida, troca a peça selecionada com a peça vazia. 
            # Isso é feito trocando os valores das posições das peças
                    # no array 'ordem_pecas'.
            # O valor da peça no índice 'indice_peca' é trocado com o 
                    # valor da peça no índice 'indice_peca_vazia'.
            self.ordem_pecas[indice_peca], self.ordem_pecas[self.indice_peca_vazia] = \
                self.ordem_pecas[self.indice_peca_vazia], self.ordem_pecas[indice_peca]
            
            # Após trocar os valores das peças, a função 'criar_pecas' é 
                    # chamada para atualizar a interface do jogo.
            # Isso atualiza a posição visual das peças na tela, de acordo 
                    # com a nova ordem do array 'ordem_pecas'.
            self.criar_pecas()
            
            # Verifica se, após a jogada, o jogador completou o quebra-cabeça (ou 
                    # seja, todas as peças estão na ordem correta).
            if self.verificar_vitoria():
                
                # Se o jogador completou o quebra-cabeça corretamente, 
                        # adiciona 10 pontos à pontuação do jogador.
                self.pontos += 10
                
                # Abre o arquivo 'arquivo_pontos' no modo de escrita ('w') 
                        # para atualizar a pontuação no arquivo.
                with open(arquivo_pontos, 'w') as f:
                    
                    # Escreve a pontuação atualizada (convertida 
                            # para string) no arquivo.
                    f.write(str(self.pontos))
                
                # Define que o jogo foi finalizado, indicando
                        # que o jogador venceu.
                self.jogo_finalizado = True


    def jogada_valida(self, indice_origem, indice_destino):
        
        # Armazena o número de colunas do tabuleiro, que é o mesmo que o 
                # número de peças em cada linha (por exemplo, 3 para um tabuleiro 3x3).
        colunas = self.tamanho_tabuleiro
        
        # Calcula a linha em que a peça de origem (a peça que
                # queremos mover) está localizada.
        # Para isso, divide o índice da peça pelo número de 
                # colunas do tabuleiro.
        # Exemplo: Se o índice for 5 em um tabuleiro 3x3, a
                # linha será 5 // 3 = 1 (segunda linha).
        linha_origem = indice_origem // colunas
        
        # Calcula a coluna da peça de origem (a peça que queremos
                # mover) usando o operador de resto.
        # O resultado é o resto da divisão do índice pelo número de 
                # colunas, que nos dá a coluna da peça.
        # Exemplo: Se o índice for 5 em um tabuleiro 3x3, a coluna
                # será 5 % 3 = 2 (terceira coluna).
        coluna_origem = indice_origem % colunas
        
        # Calcula a linha em que a peça de destino (a peça vazia) está
                # localizada, da mesma forma que foi feito para a peça de origem.
        linha_destino = indice_destino // colunas
        
        # Calcula a coluna da peça de destino (a peça vazia), da mesma
                # forma que foi feito para a peça de origem.
        coluna_destino = indice_destino % colunas
        
        # Calcula a "distância" entre a peça de origem e a 
                # peça de destino (a peça vazia).
        # A distância é a soma das diferenças absolutas entre as
                # linhas e as colunas das duas peças.
        # Exemplo: Se a peça de origem está na linha 1, coluna 2 e a 
                # peça de destino está na linha 1, coluna 1, a distância será
        # abs(1 - 1) + abs(2 - 1) = 0 + 1 = 1, ou seja, as peças são adjacentes.
        distancia = abs(linha_origem - linha_destino) + abs(coluna_origem - coluna_destino)
        
        # Retorna True se a distância for 1, o que significa que as
                # peças estão adjacentes (somente peças adjacentes
                # podem ser movidas).
        return distancia == 1

    
    def verificar_vitoria(self):
    
        # Cria a ordem correta das peças para o tabuleiro atual.
        # A ordem correta é uma lista que contém os números em
                # sequência crescente, terminando com 'None' (a peça vazia).
        # Exemplo para um tabuleiro 3x3: [1, 2, 3, 4, 5, 6, 7, 8, None].
        ordem_correta = self.criar_ordem_inicial(self.tamanho_tabuleiro)
        
        # Compara a ordem atual das peças no tabuleiro (self.ordem_pecas) 
                # com a ordem correta (ordem_correta).
        # Se forem iguais, isso significa que o jogador organizou 
                # todas as peças na sequência correta, e o jogo foi vencido.
        # Retorna True se o jogador venceu, caso contrário, retorna False.
        return self.ordem_pecas == ordem_correta


    def mostrar_vitoria(self, tela):
        
        # Define a largura e altura do modal de vitória que 
                # será exibido quando o jogador vencer o jogo.
        largura_modal = 300
        altura_modal = 150
        
        # Calcula a posição 'x' do modal para centralizá-lo
                # horizontalmente na tela.
        # A posição é calculada subtraindo a largura do modal 
                # da largura da tela e dividindo o resultado por 2.
        x_modal = (LARGURA_TELA - largura_modal) // 2
        
        # Calcula a posição 'y' do modal para centralizá-lo
                # verticalmente na tela.
        # A posição é calculada subtraindo a altura do modal da
                # altura da tela e dividindo o resultado por 2.
        y_modal = (ALTURA_TELA - altura_modal) // 2
        
        # Cria um retângulo que define a área do modal, usando as
                # coordenadas calculadas (x_modal, y_modal) e o tamanho do modal.
        retangulo_modal = pygame.Rect(x_modal, y_modal, largura_modal, altura_modal)
        
        # Desenha o retângulo do modal na tela, preenchendo-o 
                # com a cor branca (255, 255, 255).
        pygame.draw.rect(tela, (255, 255, 255), retangulo_modal)
        
        # Desenha a borda do retângulo do modal com a cor 
                # preta (0, 0, 0) e uma espessura de 2 pixels.
        pygame.draw.rect(tela, (0, 0, 0), retangulo_modal, 2)
        
        # Renderiza o texto "Parabéns!" com a fonte média, 
                # na cor cinza escuro (51, 51, 51).
        texto = fonte_media.render('Parabéns!', True, (51, 51, 51))
        
        # Centraliza o texto dentro do modal. Calcula a posição x 
                # centralizando o texto na largura do modal.
        # A posição y é definida para ficar 20 pixels 
                # abaixo do topo do modal.
        tela.blit(texto, (retangulo_modal.x + (retangulo_modal.width - texto.get_width()) // 2,
                          retangulo_modal.y + 20))
        
        # Renderiza a mensagem "Você completou o jogo!" com a fonte
                # pequena, também na cor cinza escuro (51, 51, 51).
        texto2 = fonte_pequena.render('Você completou o jogo!', True, (51, 51, 51))
        
        # Centraliza essa mensagem dentro do modal, calculando a 
                # posição x da mesma forma e posicionando-a 60 pixels
                # abaixo do topo do modal.
        tela.blit(texto2, (retangulo_modal.x + (retangulo_modal.width - texto2.get_width()) // 2,
                           retangulo_modal.y + 60))
        
        # Renderiza o texto "Clique para continuar" com a fonte
                # pequena, também na cor cinza escuro (51, 51, 51).
        texto3 = fonte_pequena.render('Clique para continuar', True, (51, 51, 51))
        
        # Centraliza essa mensagem no modal, posicionando-a 100 
                # pixels abaixo do topo do modal.
        tela.blit(texto3, (retangulo_modal.x + (retangulo_modal.width - texto3.get_width()) // 2,
                           retangulo_modal.y + 100))


    def lidar_evento_vitoria(self, evento):
        
        # Verifica se o evento foi um clique do mouse (MOUSEBUTTONDOWN).
        if evento.type == pygame.MOUSEBUTTONDOWN:
            
            # Se o jogador clicou após a vitória, o jogo é reiniciado.
            # Define 'jogo_finalizado' como False, indicando que o
                    # jogo pode continuar e não está mais no estado de vitória.
            self.jogo_finalizado = False
            
            # Reinicializa o jogo, recriando o tabuleiro, embaralhando as
                    # peças e colocando o jogo em estado inicial.
            self.inicializar_jogo()

    

def principal():
    
    # Cria um objeto 'relogio' que será usado para controlar a
            # taxa de atualização do jogo (FPS).
    # O objeto 'Clock' do Pygame ajuda a limitar o
            # número de frames por segundo.
    relogio = pygame.time.Clock()
    
    # Cria uma instância do jogo, chamando a classe 'PuzzleNumeros', 
            # que inicializa o tabuleiro, as peças e o estado do jogo.
    jogo = PuzzleNumeros()
    
    # Define a variável 'executando' como True, o que indica que o 
            # jogo está em execução. O loop principal do jogo continua 
            # enquanto 'executando' for True.
    executando = True
    
    # Inicia o loop principal do jogo. Este loop continua 
            # até que 'executando' se torne False.
    while executando:
        
        # Itera sobre todos os eventos que ocorrem (como cliques, 
                # teclas pressionadas, fechar a janela, etc.).
        for evento in pygame.event.get():
            
            # Verifica se o evento é o fechamento da 
                    # janela do jogo (pygame.QUIT).
            if evento.type == pygame.QUIT:
                
                # Se o jogo for fechado, salva a pontuação do 
                        # jogador no arquivo 'arquivo_pontos' antes de sair.
                with open(arquivo_pontos, 'w') as f:
                    
                    # Escreve a pontuação atual do jogador no
                            # arquivo de texto.
                    f.write(str(jogo.pontos))
                
                # Define 'executando' como False, o que interrompe o
                        # loop principal e encerra o jogo.
                executando = False
                
            else:
                
                # Se o jogo está finalizado (o jogador venceu), lida 
                        # com os eventos especiais de vitória.
                if jogo.jogo_finalizado:
                    
                    # Chama a função 'lidar_evento_vitoria' para gerenciar o
                            # que acontece após o jogador vencer.
                    jogo.lidar_evento_vitoria(evento)
                    
                else:
                    
                    # Se o jogo não foi finalizado, continua lidando com
                            # eventos normais, como cliques nas peças ou botões.
                    jogo.lidar_evento(evento)
        
        # Desenha o estado atual do jogo na tela, incluindo o tabuleiro e
                # as peças, chamando a função 'desenhar' da classe do jogo.
        jogo.desenhar(tela)
        
        # Limita a taxa de atualização do jogo para 30 frames por segundo, 
                # garantindo que o jogo não seja executado muito rápido.
        relogio.tick(30)
    
    # Após o loop principal ser encerrado (quando
            # 'executando' é False), encerra o Pygame.
    pygame.quit()
    
    # Encerra o programa, garantindo que o jogo 
            # seja fechado corretamente.
    sys.exit()


# Execulta a função principal
principal()