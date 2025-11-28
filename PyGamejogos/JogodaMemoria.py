# Importa as bibliotecas necessárias para o jogo.
import pygame  # Usada para criar a interface gráfica e lógica do jogo.
import random  # Usada para embaralhar as cartas.
import os  # Usada para manipular caminhos e verificar a existência de arquivos.
import sys  # Usada para encerrar o programa se necessário.

# Inicializa o módulo Pygame, preparando a biblioteca para uso.
pygame.init()

# Define variáveis para as cores usadas no jogo, utilizando 
        # tuplas para representar as cores em RGB.
# BRANCO é definido como completo RGB (255, 255, 255), 
        # resultando em uma cor branca.
BRANCO = (255, 255, 255)

# PRETO é definido como ausência de RGB (0, 0, 0), 
        # resultando em uma cor preta.
PRETO = (0, 0, 0)


# Define constantes para a largura e altura da tela do jogo, 
        # tornando o código mais organizado e fácil de ajustar.
LARGURA_TELA = 600
ALTURA_TELA = 600

# A janela do jogo é inicializada com as dimensões definidas 
        # pelas constantes LARGURA_TELA e ALTURA_TELA.
# 'set_mode' configura o tamanho da janela de 
        # visualização gráfica do Pygame.
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))

# Define o título que aparece na barra de 
        # título da janela do jogo.
pygame.display.set_caption('Jogo da Memória')


# Cria um objeto de fonte usando a função 'SysFont', 
        # que busca e usa uma fonte do sistema.
# O primeiro argumento é None, o que significa que o Pygame 
        # escolherá a primeira fonte que encaixe.
# O segundo argumento, 48, define o tamanho da fonte, o que 
        # afeta o tamanho do texto renderizado na tela.
fonte = pygame.font.SysFont(None, 48)


# Define a função 'carregar_imagens' que não recebe 
        # parâmetros e retorna uma lista de imagens processadas.
def carregar_imagens():
    
    # Cria uma lista vazia para armazenar as imagens após 
            # serem carregadas e processadas.
    imagens = []
    
    # Inicia um loop que itera dez vezes, de 1 a 10, correspondendo
            # aos números das imagens.
    for i in range(1, 11):
        
        # Constrói o caminho do arquivo de cada imagem usando 'os.path.join'
                # para garantir compatibilidade entre diferentes sistemas operacionais.
        # 'f'img{i}.jpg'' usa a formatação de string para inserir o 
                # número da imagem no nome do arquivo.
        #caminho = os.path.join('imagens', f'img{i}.jpg')
        caminho = os.path.join(f'img{i}.jpg')
         
        
        # Verifica se o arquivo de imagem existe no caminho especificado.
        if not os.path.exists(caminho):
            
            # Se o arquivo não for encontrado, imprime uma mensagem 
                    # de erro e encerra o programa.
            print(f"A imagem '{caminho}' não foi encontrada.")
            
            pygame.quit()  # Finaliza todos os módulos do Pygame.
            sys.exit()  # Sai do programa completamente.
            
        # Carrega a imagem do disco usando 'pygame.image.load' 
                # que retorna um objeto Surface contendo a imagem.
        imagem = pygame.image.load(caminho).convert()
        
        # Escala a imagem para o tamanho de 100x100 pixels 
                # usando 'pygame.transform.scale'.
        imagem = pygame.transform.scale(imagem, (100, 100))
        
        # Adiciona a imagem processada à lista 'imagens'.
        imagens.append(imagem)
        
    # Retorna a lista de imagens após todas serem 
            # carregadas e processadas.
    return imagens


# Define uma função chamada 'carregar_imagem_verso' que não 
        # recebe parâmetros e retorna uma imagem processada.
def carregar_imagem_verso():
    
    # Utiliza 'os.path.join' para construir o caminho do arquivo de 
            # forma que seja compatível com diferentes sistemas operacionais.
    # 'imagens' é o diretório e 'verso.jpg' é o nome do arquivo 
            # da imagem do verso das cartas.
    caminho = os.path.join('verso.jpg')
    
    # Verifica se o arquivo de imagem existe no local especificado.
    if not os.path.exists(caminho):
        
        # Se o arquivo não existir, imprime uma mensagem de erro 
                # indicando que o arquivo não foi encontrado.
        print(f"A imagem '{caminho}' não foi encontrada.")

        # Finaliza todos os módulos do Pygame, liberando recursos.
        pygame.quit() 

        # Sai do programa, evitando a execução de qualquer 
                # código subsequente sem a imagem necessária.
        sys.exit()  
    
    # Carrega a imagem do arquivo especificado. 
    # O método 'load' retorna uma superfície que contém a imagem.
    # 'convert' é chamado para converter o formato de pixel da 
            # imagem para o formato de pixel da tela,
            # o que pode acelerar significativamente as operações 
            # de blitting na superfície.
    imagem = pygame.image.load(caminho).convert()
    
    # Redimensiona a imagem para 100x100 pixels 
            # usando 'pygame.transform.scale'.
    # Isso garante que a imagem do verso terá o tamanho 
            # adequado para ser usada nas cartas no jogo,
            # mantendo a consistência visual e o layout organizado.
    imagem = pygame.transform.scale(imagem, (100, 100))
    
    # Retorna a imagem processada.
    return imagem


# Definição da classe Carta que será usada para criar 
        # objetos representando cada carta no jogo da memória.
class Carta:
    
    # Construtor da classe que inicializa cada objeto Carta com 
            # uma imagem de frente, uma imagem de verso e uma posição.
    def __init__(self, imagem_frente, posicao):
        
        # Armazena a imagem que aparece na frente da carta.
        self.imagem_frente = imagem_frente
        
        # Armazena a imagem que aparece no verso da carta. 
        # A variável 'imagem_verso' deve ser definida 
                # globalmente ou passada de alguma forma.
        self.imagem_verso = imagem_verso
        
        # Define o retângulo de posicionamento da carta na tela. 
        # 'get_rect' cria um novo retângulo que encapsula a imagem.
        # 'topleft=posicao' posiciona o retângulo no ponto 
                # especificado pela variável 'posicao'.
        self.rect = self.imagem_verso.get_rect(topleft=posicao)
        
        # Flag que determina se a frente da carta está sendo mostrada.
        self.mostrando_frente = False
        
        # Flag que indica se a carta já foi pareada com 
                # sua correspondente.
        self.pareada = False

    # Método para desenhar a carta na tela.
    def desenhar(self, tela):
        
        # Verifica se a frente da carta deve ser mostrada ou 
                # se a carta foi pareada.
        if self.mostrando_frente or self.pareada:
            
            # Se sim, desenha a imagem da frente da carta na posição 
                    # especificada pelo retângulo 'rect'.
            tela.blit(self.imagem_frente, self.rect.topleft)
            
        else:
            
            # Se não, desenha a imagem do verso da carta.
            tela.blit(self.imagem_verso, self.rect.topleft)

    # Método para verificar se a carta foi clicada, 
            # baseado na posição do clique.
    def checar_clique(self, posicao):
        
        # Verifica se o ponto de clique (posição do mouse) 
                # está dentro do retângulo da carta.
        # 'collidepoint' retorna True se o ponto estiver dentro do retângulo.
        if self.rect.collidepoint(posicao) and not self.mostrando_frente and not self.pareada:
            
            # Retorna True se a carta não estiver mostrando a 
                    # frente e não estiver pareada,
                    # indicando que o clique é válido para revelar a carta.
            return True
            
        # Retorna False se o clique não for válido para esta carta.
        return False


# Define a função 'embaralhar' que recebe uma lista 
        # de cartas como argumento.
def embaralhar(lista):
    
    # Utiliza a função 'shuffle' do módulo 'random' para 
            # reordenar os elementos da lista de maneira aleatória.
    # Esta função modifica a lista in-place, ou seja, altera a 
            # ordem dos elementos diretamente na lista original sem criar uma nova.
    random.shuffle(lista)
    
    # Retorna a lista após ser embaralhada.
    # Embora a função 'shuffle' altere a lista in-place, retornar a 
            # lista pode ser útil para encadeamento de chamadas ou clareza.
    return lista


# Esta linha define a função principal 'main', que coordenará 
        # todas as operações principais do jogo.
def main():
    
    # Esta linha torna a variável 'imagem_verso' acessível e 
            # modificável em todo o escopo do programa, não 
            # apenas dentro desta função.
    global imagem_verso

    # Esta linha chama a função que carrega todas as imagens que 
            # representarão a frente das cartas no jogo.
    imagens_pares = carregar_imagens()
    
    # Esta linha chama a função que carrega a imagem usada 
            # para o verso de todas as cartas no jogo.
    imagem_verso = carregar_imagem_verso()

    # Esta linha duplica a lista de imagens para que cada 
            # imagem tenha um par correspondente no jogo.
    imagens_cartas = imagens_pares * 2
    
    # Esta linha embaralha as imagens duplicadas para garantir 
            # que a disposição das cartas seja aleatória.
    random.shuffle(imagens_cartas)

    # Esta linha inicializa uma lista vazia que será preenchida 
            # com objetos 'Carta', cada um representando uma carta do jogo.
    cartas = []
    
    # Esta linha inicializa um contador que ajudará a 
            # posicionar cada carta na tela.
    index = 0
    
    # Esta linha define o espaço em pixels entre as 
            # cartas no tabuleiro do jogo.
    espaco = 10
    
    # Esta linha define o número de colunas de cartas 
            # que serão exibidas no tabuleiro.
    num_colunas = 5
    
    # Esta linha define o número de linhas de cartas 
            # que serão exibidas no tabuleiro.
    num_linhas = 4
    
    # Esta linha estabelece a largura de cada carta em pixels.
    largura_carta = 100
    
    # Esta linha estabelece a altura de cada carta em pixels.
    altura_carta = 100
    
    # Esta linha calcula a margem horizontal para centralizar as 
            # cartas na tela, subtraindo o espaço ocupado pelas 
            # cartas e dividindo o restante por dois.
    margem_x = (LARGURA_TELA - (largura_carta * num_colunas + espaco * (num_colunas - 1))) // 2
    
    # Esta linha calcula a margem vertical para centralizar as 
            # cartas na tela, de forma similar à margem horizontal.
    margem_y = (ALTURA_TELA - (altura_carta * num_linhas + espaco * (num_linhas - 1))) // 2


    # Inicia um loop que irá iterar sobre o número de linhas 
            # definido para o tabuleiro de cartas.
    for linha in range(num_linhas):
        
        # Dentro do loop das linhas, inicia um segundo loop que irá 
                # iterar sobre o número de colunas.
        for coluna in range(num_colunas):
            
            # Verifica se o índice atual ainda é menor que o número total de 
                    # imagens disponíveis para evitar indexação fora do alcance.
            if index < len(imagens_cartas):
                
                # Calcula a posição horizontal 'x' da carta atual. A posição é 
                        # determinada pela margem esquerda mais o deslocamento 
                        # das colunas anteriores.
                # Cada deslocamento é a soma da largura de uma carta e o espaço 
                        # entre as cartas, multiplicado pelo índice da coluna.
                x = margem_x + coluna * (largura_carta + espaco)
                
                # Calcula a posição vertical 'y' da carta atual. Funciona de 
                        # forma semelhante ao cálculo de 'x', mas usa o índice de linhas.
                y = margem_y + linha * (altura_carta + espaco)
                
                # Cria um novo objeto Carta, passando a imagem atual e a 
                        # posição (x, y) calculada.
                carta = Carta(imagens_cartas[index], (x, y))
                
                # Adiciona a nova carta à lista de cartas, que será usada para
                        # manter e gerenciar todas as cartas no jogo.
                cartas.append(carta)
                
                # Incrementa o índice para acessar a próxima imagem 
                        # na próxima iteração.
                index += 1


    # Esta linha define a variável 'mostrar_todas' como True, o que 
            # indica que todas as cartas devem ser mostradas viradas 
            # para cima inicialmente.
    mostrar_todas = True
    
    # Esta linha captura o tempo atual em milissegundos desde 
            # que o Pygame foi inicializado. 
    # Esse tempo é usado para controlar quanto tempo as cartas 
            # permanecerão visíveis no início do jogo.
    tempo_exibicao_inicial = pygame.time.get_ticks()
    
    # Define a variável 'running' como True, que será usada no loop
            # principal do jogo para determinar se o jogo deve 
            # continuar executando.
    running = True

    # Cria um objeto Clock para ajudar a controlar a taxa de 
            # atualização do jogo, garantindo que ele rode a uma 
            # velocidade consistente em diferentes sistemas.
    clock = pygame.time.Clock()

    # Inicializa a variável 'travar_tabuleiro' como True, o que 
            # impede que o jogador interaja com as cartas enquanto 
            # todas estão sendo exibidas.
    travar_tabuleiro = True

    # Inicializa uma lista vazia 'cartas_selecionadas' para armazenar 
            # as cartas que o jogador seleciona durante o jogo.
    cartas_selecionadas = []

    # Inicializa a variável 'pares_encontrados' como 0, que é usada 
            # para rastrear quantos pares de cartas foram
            # encontrados pelo jogador.
    pares_encontrados = 0


    # Este é o loop principal do jogo, que continua executando 
            # enquanto a variável 'running' for True.
    while running:
        
        # Limita o número de frames por segundo (FPS) a 60 para 
                # garantir que o jogo não execute rápido demais ou 
                # consuma recursos excessivos.
        clock.tick(60)
        
        # Preenche a tela com a cor branca a cada ciclo do loop, 
                # limpando o que foi desenhado anteriormente.
        tela.fill(BRANCO)
    
        # Itera sobre todos os eventos que ocorreram desde a última 
                # vez que os eventos foram obtidos.
        for event in pygame.event.get():
            
            # Verifica se o evento foi do tipo QUIT (geralmente 
                    # enviado quando a janela do jogo é fechada).
            if event.type == pygame.QUIT:
                
                # Define 'running' como False para sair do loop 
                        # principal e terminar o jogo.
                running = False
    
            # Verifica se houve um clique do mouse e se o tabuleiro 
                    # não está travado (travar_tabuleiro é False).
            if event.type == pygame.MOUSEBUTTONDOWN and not travar_tabuleiro:
                
                # Obtém a posição atual do mouse no momento do clique.
                posicao_mouse = pygame.mouse.get_pos()
                
                # Itera sobre todas as cartas no tabuleiro.
                for carta in cartas:
                    
                    # Chama o método 'checar_clique' da carta para ver se a 
                            # posição do clique coincide com a posição da carta.
                    if carta.checar_clique(posicao_mouse):
                        
                        # Se a carta foi clicada e ainda não está mostrando a 
                                # frente, muda o estado da carta para mostrar a frente.
                        carta.mostrando_frente = True
                        
                        # Adiciona a carta clicada à lista de cartas selecionadas.
                        cartas_selecionadas.append(carta)
                        
                        # Verifica se já existem duas cartas selecionadas.
                        if len(cartas_selecionadas) == 2:
                            
                            # Se duas cartas foram selecionadas, trava o 
                                    # tabuleiro para impedir mais cliques.
                            travar_tabuleiro = True
                            
                            # Define um temporizador que enviará um evento 
                                    # USEREVENT + 1 após 1000 milissegundos (1 segundo).
                            pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
                            
                        # Sai do loop de cartas assim que uma carta válida é 
                                # clicada para evitar múltiplas seleções com um único clique.
                        break


            # Verifica se o evento atual é do tipo USEREVENT + 1, um evento 
                    # personalizado utilizado para controlar ações temporizadas.
            if event.type == pygame.USEREVENT + 1:
                
                # Checa se duas cartas foram selecionadas.
                if len(cartas_selecionadas) == 2:
                    
                    # Desempacota as duas cartas selecionadas nas 
                            # variáveis carta1 e carta2.
                    carta1, carta2 = cartas_selecionadas
                    
                    # Compara as imagens de frente das duas cartas 
                            # selecionadas para ver se são iguais.
                    if carta1.imagem_frente == carta2.imagem_frente:
                        
                        # Se as imagens forem iguais, marca ambas as 
                                # cartas como pareadas.
                        carta1.pareada = True
                        carta2.pareada = True
                        
                        # Incrementa o contador de pares encontrados.
                        pares_encontrados += 1
                        
                        # Verifica se o número de pares encontrados é 
                                # igual ao número total de pares possíveis.
                        if pares_encontrados == len(imagens_pares):
                            
                            # Se todos os pares foram encontrados, o jogo termina.
                            # Limpa a tela com a cor branca.
                            tela.fill(BRANCO)
                            
                            # Renderiza o texto 'Você GANHOU!' usando a fonte 
                                    # definida, com antialiasing ativado (True) e cor preta.
                            texto = fonte.render('Você GANHOU!', True, PRETO)
                            
                            # Posiciona o texto centralizado na tela.
                            tela.blit(texto, ((LARGURA_TELA - texto.get_width()) // 2, (ALTURA_TELA - texto.get_height()) // 2))
                            
                            # Atualiza a tela para mostrar o texto.
                            pygame.display.flip()
                            
                            # Pausa o jogo por 3000 milissegundos (3 segundos) para 
                                    # que o jogador possa ver a mensagem de vitória.
                            pygame.time.wait(3000)
                            
                            # Chama a função main novamente para reiniciar o jogo.
                            main()
                            
                            # Sai da função atual para evitar execuções 
                                    # adicionais após reiniciar.
                            return
                            
                    else:
                        
                        # Se as imagens das cartas não forem iguais, vira as 
                                # cartas de volta para o verso.
                        carta1.mostrando_frente = False
                        carta2.mostrando_frente = False
                        
                    # Limpa a lista de cartas selecionadas para novas seleções.
                    cartas_selecionadas = []
                    
                    # Desbloqueia o tabuleiro para permitir novas interações.
                    travar_tabuleiro = False
                    
                    # Cancela o temporizador definido anteriormente, parando a 
                            # geração de eventos USEREVENT + 1.
                    pygame.time.set_timer(pygame.USEREVENT + 1, 0)


        # Verifica se todas as cartas estão sendo mostradas e se o tempo 
                    # estipulado para essa exibição inicial (10 segundos) já se esgotou.
        if mostrar_todas and pygame.time.get_ticks() - tempo_exibicao_inicial >= 10000:
            
            # Se o tempo de exibição inicial de 10 segundos (10000 milissegundos) 
                    # acabou, a variável 'mostrar_todas' é definida como False.
            mostrar_todas = False
            
            # A variável 'travar_tabuleiro', que impede interações enquanto 
                    # todas as cartas estão sendo mostradas, também é definida como False,
                    # permitindo que o jogador comece a interagir com o tabuleiro.
            travar_tabuleiro = False
            
            # Itera por todas as cartas no jogo.
            for carta in cartas:
                
                # Define a propriedade 'mostrando_frente' de cada carta 
                        # como False, fazendo com que todas as cartas
                        # sejam viradas para baixo.
                carta.mostrando_frente = False


        # Itera sobre cada objeto 'Carta' contido na lista 'cartas'.
        for carta in cartas:
            
            # Verifica se a fase de exibição inicial ainda está ativa.
            if mostrar_todas:
                
                # Se estiver, cada carta deverá mostrar a frente (a 
                        # imagem real da carta) ao invés do verso.
                carta.mostrando_frente = True
                
            # Chama o método 'desenhar' do objeto 'Carta', passando a 
                    # tela como argumento.
            # Este método é responsável por desenhar a carta na tela, 
                    # mostrando a frente ou o verso conforme o estado da carta.
            carta.desenhar(tela)
        
        # Atualiza a tela inteira para refletir quaisquer mudanças visuais 
                # feitas no loop. Este comando é essencial para que as mudanças 
                # no conteúdo visual da tela sejam efetivamente exibidas ao jogador.
        pygame.display.flip()


    # Sai do loop principal e executa a função 'quit' do pygame para 
            # encerrar todos os módulos carregados, garantindo uma 
            # terminação limpa do programa.
    pygame.quit()

# Inicial o main
main()