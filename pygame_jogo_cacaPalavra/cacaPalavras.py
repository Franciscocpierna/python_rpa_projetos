# Importa o módulo pygame, que é uma biblioteca usada para criar jogos e aplicações multimídia.
import pygame

# Importa o módulo random, que permite a geração de números aleatórios.
import random

# Importa ascii_uppercase da biblioteca string, que é uma string contendo todas as letras maiúsculas do alfabeto inglês.
from string import ascii_uppercase

# Inicializa todos os módulos importados do pygame, que são necessários para funcionar corretamente.
pygame.init()

# Cria um objeto Clock que pode ser usado para controlar a taxa de quadros (frames per second, FPS) do jogo.
clock = pygame.time.Clock()

# Define constantes para a largura e a altura da janela do jogo.
LARGURA, ALTURA = 800, 600

# Define uma constante para a cor branca no formato RGB (Red, Green, Blue).
BRANCO = (255, 255, 255)

# Define uma constante para a cor preta, usada como a cor padrão da fonte no jogo.
COR_DA_FONTE = (0, 0, 0)

# Define uma constante para a cor azul, que será usada para destacar as palavras selecionadas.
COR_DESTAQUE = (0, 0, 255)  

# Define uma constante para a cor branca, que será usada para a fonte das palavras selecionadas.
COR_FONTE_DESTAQUE = (255, 255, 255)  

# Define uma constante para o tamanho da grade do caça-palavras, especificando quantas células haverá.
TAMANHO_DA_GRADE = 10

# Define uma constante para o tamanho da fonte usada no jogo.
TAMANHO_DA_FONTE = 36

# Define uma constante para o espaço entre as letras na grade, afetando a distância entre elas.
ESPACAMENTO = 50  


# Define um dicionário chamado FASES, que contém várias listas de palavras associadas a números de fases.
# Cada número de fase é uma chave, e a lista associada contém palavras que os jogadores devem encontrar naquela fase.
FASES = {
    1: ['PYTHON', 'PYGAME', 'CODIGO', 'QUEBRA', 'LACO'],
    2: ['LISTA', 'FUNCAO', 'MODULO', 'TEXTO', 'JOGO'],
    3: ['IMAGEM', 'INTERFACE', 'TELA', 'DESENHO', 'EVENTO'],
    4: ['COLISAO', 'OBJETO', 'NEVE', 'SONS', 'FISICA'],
}

# Inicializa uma variável chamada 'fase_atual' com o valor 1, que representa a fase atual do jogo.
fase_atual = 1

# Calcula o total de fases disponíveis no jogo, contando o número de chaves no dicionário FASES.
total_de_fases = len(FASES)

# Inicializa uma lista vazia chamada 'selecao_temporaria', que será usada para armazenar seleções temporárias de palavras.
selecao_temporaria = []

# Configura a janela do jogo definindo seu tamanho e habilitando o double buffering, 
# o que ajuda a reduzir o efeito de flickering ou cintilação durante a atualização da tela.
tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.DOUBLEBUF)

# Define o título da janela do jogo para 'Caça Palavras'.
pygame.display.set_caption('Caça Palavras')

# Cria um objeto de fonte do pygame, que é usado para renderizar texto na tela.
# O 'None' indica que a fonte padrão do sistema será usada, e 'TAMANHO_DA_FONTE' é o tamanho da fonte.
fonte = pygame.font.Font(None, TAMANHO_DA_FONTE)


# Define a função 'gerar_grade_fase_atual', que é uma função auxiliar para 
# gerar a grade de palavras da fase atual.
def gerar_grade_fase_atual():
    
    # Chama a função 'gerar_grade' passando a lista de palavras da fase atual e o tamanho definido da grade.
    # O retorno dessa função é então retornado como resultado de 'gerar_grade_fase_atual'.
    return gerar_grade(FASES[fase_atual], TAMANHO_DA_GRADE)

# Define a função 'gerar_grade', que aceita uma lista de palavras e um
# tamanho de grade para criar uma grade de palavras.
def gerar_grade(palavras, tamanho):
    
    # Itera por cada palavra na lista de palavras fornecida como argumento.
    for palavra in palavras:
        
        # Verifica se o comprimento de qualquer palavra é maior do que o tamanho da grade fornecido.
        if len(palavra) > tamanho:
            
            # Se uma palavra for muito longa para caber na grade, levanta um erro com uma mensagem informativa.
            raise ValueError(f"A palavra '{palavra}' é muito longa para a grade de tamanho {tamanho}.")
    
    # Cria uma matriz 'grade' que é uma lista de listas. Cada lista interna representa uma linha da grade.
    # A grade é inicializada com espaços em branco usando compreensão de lista.
    # O tamanho da grade é definido pelo valor da variável 'tamanho'.
    # grade = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
    
    
    # Inicializa uma lista vazia para a grade.
    # Esta lista 'grade' eventualmente conterá outras listas, cada uma 
    # representando uma linha na grade do caça-palavras.
    grade = []

    # O loop externo itera tantas vezes quanto o 'tamanho' especificado.
    # 'tamanho' é uma variável que define o número de linhas e colunas na grade.
    # Cada iteração do loop externo adicionará uma nova linha à grade.
    for _ in range(tamanho):

        # Inicializa uma lista vazia para a linha atual.
        # Esta lista 'linha' representará uma linha individual dentro
        # da grade e conterá os caracteres dessa linha.
        linha = []

        # O loop interno itera tantas vezes quanto o 'tamanho' especificado, igual ao loop externo.
        # Isso garante que cada linha tenha o mesmo número de colunas que o número de linhas na 
        # grade, criando uma grade quadrada.
        for _ in range(tamanho):

            # Adiciona um espaço em branco (' ') à lista 'linha'.
            # Isso é feito para cada coluna da linha, inicializando a linha com espaços em branco.
            linha.append(' ')

        # Adiciona a lista 'linha', agora preenchida com espaços em branco, à lista 'grade'.
        # Após a conclusão do loop interno, uma linha completa com 'tamanho' colunas terá sido
        # criada e adicionada à grade.
        grade.append(linha)
        

    # Itera sobre cada palavra na lista de palavras que precisa ser colocada na grade.
    for palavra in palavras:
        
        # Inicializa uma variável booleana 'palavra_colocada' como False. Esta variável será usada para
        # verificar se a palavra atual foi colocada com sucesso na grade.
        palavra_colocada = False
        
        # Entra em um loop enquanto a palavra atual não for colocada na grade.
        while not palavra_colocada:
            
            # Escolhe aleatoriamente uma direção para a palavra: 0 para horizontal ou 1 para vertical.
            direcao = random.choice([0, 1])
            
            # Se a direção escolhida for 0 (horizontal), realiza o seguinte processo para colocar a palavra.
            if direcao == 0:
                
                # Escolhe aleatoriamente um ponto de partida para a palavra. O ponto de partida é um índice
                # na linha onde a palavra começará, garantindo que haja espaço suficiente para a palavra caber.
                passo = random.choice(range(tamanho - len(palavra) + 1))
                
                # Escolhe aleatoriamente uma linha da grade onde a palavra será colocada.
                linha = random.choice(range(tamanho))
                
                # Verifica se a palavra cabe horizontalmente na posição escolhida.
                # Isso é feito verificando se cada espaço na grade onde a palavra será colocada está vazio (contém um espaço em branco).
                # A variável 'linha' representa a linha da grade onde a palavra será colocada.
                # 'passo' é o ponto de início na linha onde a primeira letra da palavra será posicionada.

                # Inicializa uma variável 'cabe_na_grade' como True. Ela será usada para verificar se 
                # há espaço suficiente para a palavra.
                cabe_na_grade = True
                for l in range(len(palavra)):

                    # Verifica se a célula atual da grade está vazia.
                    # 'grade[linha][passo + l]' acessa a célula na grade na linha especificada e na
                    # coluna 'passo + l'.
                    # Se qualquer célula onde a palavra deve ser colocada não estiver vazia, 
                    # define 'cabe_na_grade' como False.
                    if grade[linha][passo + l] != ' ':
                        cabe_na_grade = False
                        break

                # Se houver espaço suficiente na grade para a palavra.
                if cabe_na_grade:

                    # Itera pelo comprimento da palavra.
                    for l in range(len(palavra)):

                        # Coloca cada letra da palavra na grade, na posição calculada.
                        # 'palavra[l]' é a letra atual da palavra.
                        # 'grade[linha][passo + l]' é a célula na grade onde a letra será colocada.
                        grade[linha][passo + l] = palavra[l]

                    # Depois que a palavra é colocada, define 'palavra_colocada' como True.
                    # Isso indica que a palavra foi colocada com sucesso na grade e o loop de
                    # colocação de palavras pode ser encerrado.
                    palavra_colocada = True


            # Se a direção escolhida não for 0 (horizontal), então é 1, e a palavra será colocada verticalmente.
            else:  
                
                # Escolhe um índice de início aleatório para a palavra na coluna. Este índice representa a linha
                # em que a primeira letra da palavra será colocada. O índice de início deve permitir que a palavra
                # inteira caiba na coluna, daí 'tamanho - len(palavra) + 1'.
                passo = random.choice(range(tamanho - len(palavra) + 1))
                
                # Escolhe uma coluna aleatória da grade onde a palavra será colocada.
                coluna = random.choice(range(tamanho))
                
                # Inicializa uma variável 'cabe_na_coluna' como True. Ela será usada para verificar se
                # há espaço suficiente na coluna para a palavra.
                cabe_na_coluna = True

                # Itera pelo comprimento da palavra para verificar se cada espaço necessário na
                # coluna está vazio.
                for l in range(len(palavra)):

                    # Verifica se a célula atual da grade está vazia.
                    # 'grade[passo + l][coluna]' acessa a célula na grade na linha 'passo + l' e 
                    # na coluna especificada.
                    # Se qualquer célula onde a palavra deve ser colocada não estiver vazia,
                    # define 'cabe_na_coluna' como False.
                    if grade[passo + l][coluna] != ' ':
                        cabe_na_coluna = False
                        break

                # Se houver espaço suficiente na coluna para a palavra.
                if cabe_na_coluna:

                    # Itera pelo comprimento da palavra.
                    for l in range(len(palavra)):

                        # Insere cada letra da palavra na grade na posição correta.
                        # 'palavra[l]' é a letra atual da palavra.
                        # 'grade[passo + l][coluna]' é a célula na grade onde a letra será colocada.
                        grade[passo + l][coluna] = palavra[l]

                    # Após a palavra ser inserida na grade, marca 'palavra_colocada' como True.
                    # Isso indica que a palavra foi colocada com sucesso na grade e o loop de colocação de palavras pode ser encerrado.
                    palavra_colocada = True



    # Este bloco de código preenche os espaços restantes na grade com letras aleatórias.
    # Isso é feito após todas as palavras terem sido colocadas horizontal ou verticalmente.

    # Itera sobre cada linha da grade, que é uma lista de listas.
    for linha in range(tamanho):
        
        # Dentro de cada linha, itera sobre cada coluna.
        for coluna in range(tamanho):
            
            # Verifica se a célula atual (identificada pelo índice [linha][coluna]) está vazia.
            # Uma célula vazia é representada por um espaço em branco ' '.
            if grade[linha][coluna] == ' ':
                
                # Se a célula está vazia, atribui a ela uma letra aleatória.
                # 'random.choice(ascii_uppercase)' seleciona uma letra aleatória de 'A' a 'Z'.
                grade[linha][coluna] = random.choice(ascii_uppercase)

    # Depois de preencher todos os espaços vazios, retorna a grade completa.
    # A grade agora contém as palavras posicionadas mais as letras aleatórias preenchendo os espaços em branco.
    return grade



# Função para desenhar a grade de letras
def desenhar_grade(superficie, grade, fonte, inicio_x, inicio_y, tamanho_da_letra):
    
    # Itera pelas linhas da grade de letras.
    # 'enumerate(grade)' retorna cada linha da grade ('linha') junto com seu índice ('y').
    # O índice 'y' representa a posição vertical da linha na grade.
    for y, linha in enumerate(grade):
        
        # Itera pelas colunas da linha atual da grade de letras.
        # 'enumerate(linha)' retorna cada letra ('letra') na linha atual junto com seu índice ('x').
        # O índice 'x' representa a posição horizontal da letra na linha.
        for x, letra in enumerate(linha):
            
            # Renderiza a letra atual usando a fonte fornecida.
            # 'fonte.render()' cria uma superfície com a letra renderizada.
            # 'letra' é o caractere a ser renderizado.
            # 'True' ativa o anti-aliasing, tornando o texto mais suave e legível.
            # 'COR_DA_FONTE' é a cor usada para renderizar o texto.
            # A superfície com o texto renderizado é armazenada em 'texto_da_letra'.
            texto_da_letra = fonte.render(letra, True, COR_DA_FONTE)
            
            # Calcula a posição central (centro_x, centro_y) onde a letra será desenhada na superfície.
            # 'inicio_x' e 'inicio_y' são as coordenadas do canto superior esquerdo da grade na tela.
            # 'x' e 'y' são os índices da letra na grade, representando sua posição na coluna e na linha, respectivamente.
            # 'tamanho_da_letra' é a largura e a altura de cada célula da grade.
            centro_x = inicio_x + x * tamanho_da_letra + tamanho_da_letra // 2
            centro_y = inicio_y + y * tamanho_da_letra + tamanho_da_letra // 2

            # Cria um retângulo (rect_da_letra) que envolve o texto renderizado, centralizado na posição calculada.
            # 'texto_da_letra.get_rect()' cria um retângulo que tem o tamanho exato para envolver o texto renderizado.
            # O argumento 'center=(centro_x, centro_y)' define o centro do retângulo nas coordenadas calculadas,
            # garantindo que a letra seja desenhada centralizada na célula da grade.
            rect_da_letra = texto_da_letra.get_rect(center=(centro_x, centro_y))

            # Desenha o texto renderizado (letra) na superfície na posição definida pelo retângulo (rect_da_letra).
            # 'superficie.blit()' desenha a superfície 'texto_da_letra' na superfície principal 'superficie'.
            # 'rect_da_letra' define a posição onde o texto será desenhado na superfície principal.
            superficie.blit(texto_da_letra, rect_da_letra)
    
    
# Define a função 'palavra_na_posicao', que verifica se uma palavra está na posição especificada na grade.
def palavra_na_posicao(grade, inicio, fim, tamanho):
    
    # Verifica se os índices de início e fim da seleção estão dentro dos limites da grade.
    # Este bloco de código é crucial para assegurar que a seleção feita pelo jogador 
    # seja válida dentro da grade do jogo.
    # As variáveis 'inicio' e 'fim' representam as coordenadas de início e
    # fim da seleção, respectivamente.
    # Cada uma dessas variáveis é um par de coordenadas, onde o primeiro elemento é o 
    # índice da linha e o segundo é o índice da coluna.
    # A variável 'tamanho' representa o número de linhas e colunas da grade, assumindo uma grade quadrada.
    # A condição verifica cada elemento das coordenadas de 'inicio' e 'fim' para garantir
    # que eles estejam dentro dos limites da grade.
    # Por exemplo, 'inicio[0] < tamanho' assegura que a linha de início
    # não ultrapasse o número total de linhas da grade.
    if (0 <= inicio[0] < tamanho) and (0 <= inicio[1] < tamanho) and (0 <= fim[0] < tamanho) and (0 <= fim[1] < tamanho):

        # Inicializa uma string vazia para construir a palavra que está sendo selecionada na grade.
        # Esta variável 'palavra_selecionada' será usada para armazenar sequencialmente
        # as letras da palavra à medida que são encontradas.
        # Inicializar como uma string vazia é importante para começar a construção da palavra do zero.
        palavra_selecionada = ""

        # Verifica se a seleção é horizontal.
        # A seleção é considerada horizontal se as coordenadas de linha de 'inicio' e 'fim' forem iguais, ou seja, 'inicio[0] == fim[0]'.
        # Isso significa que a seleção do jogador se estende ao longo de uma única linha da grade.
        if inicio[0] == fim[0]:

            # Itera pelas colunas entre o início e o fim da seleção.
            # 'range(min(inicio[1], fim[1]), max(inicio[1], fim[1]) + 1)' cria uma sequência
            # de números que representam as colunas da seleção.
            # O uso de 'min()' e 'max()' garante que a sequência esteja correta 
            # independentemente de o jogador ter selecionado da esquerda para a direita ou vice-versa.
            # A adição de '+ 1' no 'max()' é necessária para incluir a coluna de 'fim' na sequência.
            for col in range(min(inicio[1], fim[1]), max(inicio[1], fim[1]) + 1):

                # Concatena as letras encontradas na linha selecionada para formar a palavra.
                # 'grade[inicio[0]][col]' acessa a letra na grade na linha especificada por
                # 'inicio[0]' (a linha da seleção) e na coluna 'col' (iterada no loop).
                # Cada letra encontrada é adicionada à string 'palavra_selecionada'.
                palavra_selecionada += grade[inicio[0]][col]

                
        # Verifica se a seleção é vertical, ou seja, se a coordenada da coluna do ponto de início e do fim são iguais.
        # Esta condição verifica se o jogador fez uma seleção vertical na grade.
        # 'inicio[1]' e 'fim[1]' representam as coordenadas das colunas dos pontos de início e fim da seleção.
        # Se esses valores são iguais, significa que a seleção foi feita na mesma coluna, indicando uma seleção vertical.
        elif inicio[1] == fim[1]:

            # Itera sobre o intervalo de linhas entre o ponto de início e o ponto de fim da seleção.
            # 'range(min(inicio[0], fim[0]), max(inicio[0], fim[0]) + 1)' cria uma sequência de índices de linha da seleção.
            # 'min()' e 'max()' são usados para garantir que os valores estejam na ordem correta.
            # Isso é importante porque o jogador pode ter feito a seleção de baixo para cima ou de cima para baixo.
            for row in range(min(inicio[0], fim[0]), max(inicio[0], fim[0]) + 1):

                # Concatena as letras encontradas na coluna selecionada para formar a palavra.
                # 'grade[row][inicio[1]]' acessa a letra na grade na linha 'row' e na coluna 'inicio[1]' (a coluna da seleção).
                # Cada letra encontrada é adicionada à string 'palavra_selecionada'.
                palavra_selecionada += grade[row][inicio[1]]

        # Retorna a palavra selecionada depois de terminar a iteração.
        # Após concatenar todas as letras da seleção vertical, a função retorna a palavra completa formada.
        return palavra_selecionada

    # Se os pontos de início e fim da seleção não estiverem dentro dos limites da grade,
    # retorna uma string vazia, indicando que nenhuma palavra válida foi selecionada.
    # Este retorno ocorre se a seleção do jogador sair dos limites da grade, garantindo 
    # que a função não produza resultados inválidos.
    return ""


# Define a função 'encontrar_palavra', que verifica se uma palavra
# específica foi encontrada.
# Esta função é usada para verificar se uma palavra já foi 
# identificada pelo jogador.
def encontrar_palavra(palavra, palavras_encontradas):
    
    # Retorna True se a 'palavra' estiver na lista 'palavras_encontradas', 
    # caso contrário, retorna False.
    # A operação 'palavra in palavras_encontradas' é uma pesquisa de 
    # pertencimento que verifica se
    # o item 'palavra' está presente na lista 'palavras_encontradas'.
    return palavra in palavras_encontradas

# Define a função 'obter_palavras_da_fase', que busca as palavras
# associadas a uma determinada fase do jogo.
def obter_palavras_da_fase(fase):
    
    # Utiliza o método '.get()' no dicionário 'FASES' para obter a 
    # lista de palavras associadas à chave 'fase'.
    # Se a chave 'fase' não existir no dicionário 'FASES', retorna 
    # uma lista vazia como padrão ([]).
    # Isso evita erros caso a 'fase' solicitada não esteja definida 
    # no dicionário 'FASES'.
    return FASES.get(fase, [])

    
# Função para desenhar o destaque de uma palavra na grade de letras
def desenhar_destaque_palavra(superficie, palavra, grade, tamanho_da_letra, cor_destaque, cor_fonte_destaque, palavras_encontradas):
    
    # Verifica se a palavra está na lista de palavras encontradas.
    # A função 'encontrar_palavra' verifica se a palavra dada ('palavra') está na lista 'palavras_encontradas'.
    # Se a palavra foi encontrada pelo jogador, ela será destacada na grade.
    if encontrar_palavra(palavra, palavras_encontradas):
        
        # Loop pelas linhas da grade de letras.
        # 'range(len(grade))' cria uma sequência de números que correspondem aos índices das linhas na grade.
        # Cada número nessa sequência representa uma linha na grade.
        for linha in range(len(grade)):
            
            # Loop pelas colunas da linha atual da grade.
            # 'range(len(grade[linha]))' cria uma sequência de números que correspondem aos índices das colunas na linha atual.
            # Cada número nessa sequência representa uma coluna na linha especificada da grade.
            for coluna in range(len(grade[linha])):

                
                # Loop pelas direções: horizontal, vertical, diagonal direita e diagonal esquerda
                # (1, 0): Movimento horizontal, onde avançamos uma posição para a direita na grade e não movemos verticalmente (0 na coordenada y).
                # (0, 1): Movimento vertical, onde avançamos uma posição para baixo na grade e não movemos horizontalmente (0 na coordenada x).
                # (1, 1): Movimento diagonal direita, onde avançamos uma posição para a direita e uma posição para baixo na grade.
                # (-1, 1): Movimento diagonal esquerda, onde avançamos uma posição para a esquerda e uma posição para baixo na grade.
                for direcao in [(1, 0), (0, 1), (1, 1), (-1, 1)]:
                    
                    # Inicializa as coordenadas (x, y) na posição atual da linha e coluna
                    x, y = coluna, linha
                    
                    # Inicializa a variável para acompanhar se a palavra foi encontrada nesta posição
                    palavra_encontrada = False
                    
                    # Inicializa a lista para armazenar as coordenadas onde a palavra é destacada
                    coordenadas_palavra = []
                    
                    # Loop pelas letras da palavra
                    for letra in palavra:
                        
                        # Verifica se as coordenadas (x, y) estão fora dos limites da grade
                        """
                        if x < 0: Esta parte verifica se o valor da variável x é menor que 
                            zero. Isso significa que estamos verificando se a coordenada x está 
                            fora dos limites à esquerda da grade.
                            
                        or: Este é um operador lógico "ou". Ele permite que a condição seja verdadeira se 
                            pelo menos uma das condições que o circundam for verdadeira.
                            
                        y < 0: Similar ao primeiro ponto, esta parte verifica se o valor da variável y é
                            menor que zero. Estamos verificando se a coordenada y está fora dos limites acima da grade.
                            
                        x >= len(grade[0]): Aqui, estamos verificando se o valor de x é maior ou igual ao 
                            comprimento da primeira linha da grade. Isso verifica se a coordenada x está fora
                            dos limites à direita da grade.
                            
                        y >= len(grade): Similar ao ponto anterior, estamos verificando se o valor de y é maior 
                            ou igual ao comprimento total da grade. Isso verifica se a coordenada y está fora dos
                            limites abaixo da grade.
                        """
                        if x < 0 or y < 0 or x >= len(grade[0]) or y >= len(grade):
                            
                            # Se estiverem fora dos limites, sai do loop
                            break

                        # Verifica se a letra na posição atual da grade é igual à letra da palavra
                        if grade[y][x] != letra:
                            
                            # Se não for igual, sai do loop
                            break

                        # Se a letra na posição atual for igual à letra da palavra, adiciona as coordenadas a 'coordenadas_palavra'
                        coordenadas_palavra.append((x, y))

                        # Atualiza as coordenadas (x, y) para a próxima posição na direção atual
                        x += direcao[0]
                        y += direcao[1]

                    # Verifica se o número de letras encontradas na palavra é igual ao número
                    # de letras na palavra que estamos procurando
                    if len(coordenadas_palavra) == len(palavra):
                        
                        # Se o número de letras encontradas for igual, a palavra foi encontrada na grade
                        palavra_encontrada = True

                    # Verifica se a palavra foi encontrada
                    if palavra_encontrada:
                        
                        # Itera através das coordenadas onde as letras da palavra foram encontradas na grade
                        for letra_x, letra_y in coordenadas_palavra:
                            
                            # Calcula a posição central da letra na grade
                            
                            # Para a coordenada X (horizontal):
                            # - 'inicio_x' representa a posição inicial na horizontal onde começamos a desenhar a grade.
                            # - 'letra_x' é o número da coluna onde a letra foi encontrada na grade.
                            # - 'tamanho_da_letra' é o tamanho de cada letra na grade.
                            # - 'tamanho_da_letra // 2' é metade do tamanho da letra, usado para centralizar a letra.
                            # Portanto, 'centro_x_letra' representa o ponto central na horizontal onde a letra será desenhada.
                            centro_x_letra = inicio_x + letra_x * tamanho_da_letra + tamanho_da_letra // 2
                            
                            # Para a coordenada Y (vertical):
                            # - 'inicio_y' representa a posição inicial na vertical onde começamos a desenhar a grade.
                            # - 'letra_y' é o número da linha onde a letra foi encontrada na grade.
                            # - 'tamanho_da_letra' é o tamanho de cada letra na grade.
                            # - 'tamanho_da_letra // 2' é metade do tamanho da letra, usado para centralizar a letra.
                            # Portanto, 'centro_y_letra' representa o ponto central na vertical onde a letra será desenhada.

                            # Em resumo, essas duas linhas de código calculam as coordenadas exatas onde o centro da letra será posicionado na grade.
                            centro_y_letra = inicio_y + letra_y * tamanho_da_letra + tamanho_da_letra // 2
                            
                            # Desenha um retângulo azul ao redor da letra para destacá-la
                            pygame.draw.rect(
                                
                                superficie,  # A superfície onde o retângulo será desenhado
                                cor_destaque,  # A cor do destaque (azul, no caso)
                                
                                (
                                    centro_x_letra - tamanho_da_letra // 2,  # Coordenada X do canto superior esquerdo do retângulo
                                    centro_y_letra - tamanho_da_letra // 2,  # Coordenada Y do canto superior esquerdo do retângulo
                                    tamanho_da_letra,  # Largura do retângulo
                                    tamanho_da_letra  # Altura do retângulo
                                )
                            )

                            # Renderiza a letra da palavra destacada:
                            # - 'grade[letra_y][letra_x]' obtém a letra da grade na posição (letra_x, letra_y), que 
                            # faz parte da palavra destacada.
                            # - 'fonte.render(grade[letra_y][letra_x], True, cor_fonte_destaque)' renderiza a
                            # letra com a fonte especificada, usando a cor 'cor_fonte_destaque'.
                            # - 'texto_da_letra' armazena o resultado da renderização da letra.
                            texto_da_letra = fonte.render(grade[letra_y][letra_x], True, cor_fonte_destaque)

                            # Cria um retângulo em torno do texto renderizado ('texto_da_letra') e o centraliza 
                            # nas coordenadas calculadas anteriormente ('centro_x_letra' e 'centro_y_letra').
                            # Isso é útil para posicionar o texto no local correto.
                            rect_da_letra = texto_da_letra.get_rect(center=(centro_x_letra, centro_y_letra))

                            # Desenha o texto renderizado ('texto_da_letra') na superfície da tela na 
                            # posição definida pelo retângulo ('rect_da_letra').
                            # Isso coloca a letra destacada na grade.
                            superficie.blit(texto_da_letra, rect_da_letra)

                            # Atualiza a parte da tela delimitada pelo retângulo ('rect_da_letra').
                            # Isso é necessário para garantir que a letra seja exibida na tela.
                            pygame.display.update(rect_da_letra)
    

# Função para desenhar as palavras da fase na tela.
def desenhar_palavras_da_fase(superficie, palavras, palavras_encontradas, fonte):
    
    # Itera sobre a lista de palavras usando 'enumerate' para obter o índice 'i' e a palavra 'palavra'.
    # 'enumerate(palavras)' retorna tanto o índice da palavra na lista (i) quanto a própria palavra (palavra).
    for i, palavra in enumerate(palavras):
        
        # Verifica se a palavra atual ('palavra') está na lista de palavras encontradas ('palavras_encontradas').
        # Isso é usado para determinar se a palavra deve ser desenhada de maneira diferente (por exemplo, riscada).
        if palavra in palavras_encontradas:
            
            # Se a palavra foi encontrada, desenha a palavra com um traço sobre ela (riscada).
            
            # 'fonte.render' cria uma superfície com a palavra renderizada.
            # O primeiro argumento é o texto a ser renderizado ('palavra').
            # O segundo argumento, 'True', ativa o anti-aliasing, que suaviza as bordas do texto.
            # 'COR_DA_FONTE' define a cor do texto.
            texto_palavra = fonte.render(palavra, True, COR_DA_FONTE)

            # Cria uma superfície temporária do mesmo tamanho do texto renderizado.
            # 'texto_palavra.get_size()' obtém as dimensões da superfície do texto renderizado.
            # 'pygame.Surface()' cria uma nova superfície com essas dimensões.
            texto_palavra_riscada = pygame.Surface(texto_palavra.get_size())

            # Preenche a superfície temporária com a cor branca.
            # 'fill(BRANCO)' preenche toda a superfície com a cor branca.
            texto_palavra_riscada.fill(BRANCO)

            # Copia o texto renderizado para a superfície temporária.
            # 'blit' é usado para desenhar uma superfície sobre outra.
            # O primeiro argumento é a superfície a ser desenhada ('texto_palavra').
            # O segundo argumento é a posição na superfície de destino onde a superfície será desenhada.
            texto_palavra_riscada.blit(texto_palavra, (0, 0))


            # A largura da linha é definida como 2 pixels, tornando a linha visível e destacada.
            # Esta linha desenha uma linha horizontal sobre a palavra renderizada para criar um efeito de "palavra riscada".
            # 'pygame.draw.line()' é uma função do Pygame usada para desenhar linhas.
            # Os argumentos são:
            # - 'texto_palavra_riscada': a superfície onde a linha será desenhada.
            # - 'COR_DA_FONTE': a cor da linha.
            # - '(0, TAMANHO_DA_FONTE // 2)': as coordenadas do ponto inicial da linha.
            #   A linha começa no lado esquerdo da superfície e na metade da altura da fonte.
            # - '(texto_palavra.get_width(), TAMANHO_DA_FONTE // 2)': as coordenadas do ponto final da linha.
            #   A linha termina no lado direito da superfície e na mesma altura vertical do ponto inicial.
            # - '2': a largura da linha em pixels.
            pygame.draw.line(texto_palavra_riscada, COR_DA_FONTE, (0, TAMANHO_DA_FONTE // 2), (texto_palavra.get_width(), TAMANHO_DA_FONTE // 2), 2)

            # Posiciona a palavra riscada na tela com um espaço de 20 pixels entre cada
            # palavra e uma altura fixa a 50 pixels a partir da parte inferior da tela.
            # Esta linha posiciona a superfície da palavra riscada na tela principal ('superficie').
            # 'blit()' é usado para desenhar uma superfície sobre outra.
            # Os argumentos são:
            # - 'texto_palavra_riscada': a superfície da palavra riscada a ser desenhada.
            # - '(20 + i * 150, ALTURA - 50)': as coordenadas onde a superfície será posicionada na tela.
            #   O valor '20 + i * 150' determina a posição horizontal da palavra, criando um espaçamento
            # horizontal de 150 pixels entre cada palavra, mais um offset inicial de 20 pixels.
            #   'ALTURA - 50' posiciona a palavra a 50 pixels da parte inferior da tela, onde 'ALTURA' é a altura total da tela.
            superficie.blit(texto_palavra_riscada, (20 + i * 150, ALTURA - 50))


        else:
            
            # Renderiza a palavra como uma string com a fonte especificada e a cor da fonte padrão.
            # 'fonte.render()' cria uma superfície com a palavra renderizada.
            # O primeiro argumento é o texto a ser renderizado, que neste caso é a 'palavra' convertida para string.
            # O segundo argumento, 'True', ativa o anti-aliasing, que suaviza as bordas do texto, tornando-o mais legível.
            # 'COR_DA_FONTE' define a cor do texto.
            texto_palavra = fonte.render(str(palavra), True, COR_DA_FONTE)

            # Posiciona a palavra na tela da mesma forma que a palavra riscada, mas sem o traço.
            # 'superficie.blit()' é usado para desenhar a superfície da palavra renderizada na tela principal.
            # Os argumentos são:
            # - 'texto_palavra': a superfície da palavra renderizada a ser desenhada.
            # - '(20 + i * 150, ALTURA - 50)': as coordenadas onde a superfície será posicionada na tela.
            #   O valor '20 + i * 150' determina a posição horizontal da palavra, criando um espaçamento
            # horizontal de 150 pixels entre cada palavra, mais um offset inicial de 20 pixels.
            #   'ALTURA - 50' posiciona a palavra a 50 pixels da parte inferior da tela, 
            # onde 'ALTURA' é a altura total da tela.
            superficie.blit(texto_palavra, (20 + i * 150, ALTURA - 50))
            

# Antes do loop principal, calcular o início centralizado da grade
# 'inicio_x' e 'inicio_y' representam as coordenadas do canto superior esquerdo da
# grade de palavras na tela.
# Eles são calculados de forma a posicionar a grade centralizada horizontal
# e verticalmente na janela do jogo.
inicio_x = (LARGURA - TAMANHO_DA_GRADE * ESPACAMENTO) // 2
inicio_y = (ALTURA - TAMANHO_DA_GRADE * ESPACAMENTO) // 2

# Cria a grade inicial
# 'grade' é uma matriz que representa a disposição das letras na grade de palavras.
# É gerada com base nas informações da fase atual e do tamanho da grade.
grade = gerar_grade(FASES[fase_atual], TAMANHO_DA_GRADE)

# Lista de palavras encontradas e suas posições
# 'palavras_encontradas' é uma lista que armazena as palavras 
# que o jogador encontrou durante o jogo.
# 'posicoes_palavras_encontradas' é uma lista que armazena as
# posições das palavras encontradas na grade.
palavras_encontradas = []
posicoes_palavras_encontradas = []


# 'rodando' é uma variável booleana que controla se o jogo está em execução ou não. 
# Inicialmente, está definida como True, indicando que o jogo está ativo.
rodando = True

# 'inicio_da_selecao' e 'fim_da_selecao' são usadas para rastrear a seleção
# de letras pelo jogador.
# Inicialmente, ambas estão definidas como None, indicando que nenhuma seleção 
# foi iniciada ou concluída.
inicio_da_selecao = None
fim_da_selecao = None

# 'rodando' é uma variável booleana que controla se o jogo está em execução ou não.
# 'inicio_da_selecao' e 'fim_da_selecao' são usados para rastrear a seleção
# de letras pelo jogador.
# 'desenhando_selecao' é uma variável que controla se o jogador está
# atualmente desenhando uma seleção de letras na tela.
desenhando_selecao = False


# Loop principal do jogo
while rodando:
    
    # Preenche toda a tela com a cor branca. A variável 'tela' representa a superfície principal do jogo,
    # e 'fill()' é um método do Pygame para preencher toda a superfície com uma cor uniforme.
    # 'BRANCO' é uma constante definida anteriormente no código que representa a cor branca.
    tela.fill(BRANCO)
    
    # Chama a função 'desenhar_grade'. Esta função é responsável por desenhar a grade
    # de letras na tela.
    # Os argumentos passados são:
    # - 'tela': a superfície principal onde a grade será desenhada.
    # - 'grade': a matriz da grade de palavras usada no jogo.
    # - 'fonte': a fonte usada para renderizar as letras na grade.
    # - 'inicio_x' e 'inicio_y': coordenadas x e y que determinam onde a
    # grade começa a ser desenhada na tela.
    # - 'ESPACAMENTO': o espaço entre as letras na grade.
    desenhar_grade(tela, grade, fonte, inicio_x, inicio_y, ESPACAMENTO)
    
    
    # Este loop itera sobre cada palavra encontrada pelo jogador.
    # A variável 'posicoes_palavras_encontradas' é uma lista de tuplas. Cada tupla contém:
    # - 'palavra': a palavra encontrada.
    # - 'inicio_palavra': a posição inicial da palavra na grade.
    # - 'fim_palavra': a posição final da palavra na grade.
    for palavra, inicio_palavra, fim_palavra in posicoes_palavras_encontradas:
        
        # Chama a função 'desenhar_destaque_palavra'. Esta função é responsável por destacar as palavras encontradas na grade.
        # Os argumentos passados são:
        # - 'tela': a superfície principal onde a grade é desenhada.
        # - 'palavra': a palavra atual a ser destacada.
        # - 'grade': a matriz da grade de palavras usada no jogo.
        # - 'ESPACAMENTO': o espaço entre as letras na grade.
        # - 'COR_DESTAQUE': a cor usada para destacar a palavra encontrada.
        # - 'COR_FONTE_DESTAQUE': a cor da fonte usada para as letras da palavra destacada.
        # - 'palavras_encontradas': a lista de todas as palavras que foram encontradas até o momento.
        desenhar_destaque_palavra(tela, palavra, grade, ESPACAMENTO, COR_DESTAQUE, COR_FONTE_DESTAQUE, palavras_encontradas)
        
        
    # A função 'desenhar_palavras_da_fase' é chamada com os seguintes argumentos:
    # - 'tela': a superfície principal do Pygame onde os elementos gráficos são desenhados.
    # - 'FASES[fase_atual]': uma lista de palavras pertencentes à fase atual do jogo.
    #   'FASES' é um dicionário onde cada chave é um número de fase, e o valor é uma lista de palavras.
    #   'fase_atual' é uma variável que mantém o controle de qual fase do jogo está ativa no momento.
    # - 'palavras_encontradas': uma lista de palavras que o jogador já encontrou.
    #   Essa informação é usada para alterar a forma como as palavras são exibidas 
    # (por exemplo, palavras já encontradas podem ser mostradas de maneira diferente).
    # - 'fonte': a fonte usada para renderizar o texto na tela.
    desenhar_palavras_da_fase(tela, FASES[fase_atual], palavras_encontradas, fonte)

    # Desenha as palavras da dica na parte inferior da tela
    # Este comentário é repetido e serve para o próximo bloco de código que realiza uma função semelhante ao bloco anterior.

    # 'palavras_da_fase' é uma variável que armazena a lista de palavras para a fase atual do jogo.
    # O valor é obtido acessando o dicionário 'FASES' com a chave 'fase_atual'.
    palavras_da_fase = FASES[fase_atual]

    # A função 'desenhar_palavras_da_fase' é chamada novamente, mas desta vez usando a variável 'palavras_da_fase'.
    # Isso tem o mesmo efeito que a chamada anterior, mas a lista de palavras é primeiro armazenada em uma variável.
    # Isso pode ser útil se 'palavras_da_fase' for usada em outras partes do código além desta função.
    desenhar_palavras_da_fase(tela, palavras_da_fase, palavras_encontradas, fonte)


    # Processamento de eventos
    # O loop 'for' itera sobre uma lista de todos os eventos que ocorreram desde a última vez que os eventos foram obtidos.
    # 'pygame.event.get()' retorna uma lista de 'Event' objects, cada um representando algo que aconteceu.
    for evento in pygame.event.get():

        # Verifica se o tipo do evento é 'pygame.QUIT'.
        # 'pygame.QUIT' é acionado quando o usuário fecha a janela do jogo, por exemplo, clicando no botão 'fechar' da janela.
        if evento.type == pygame.QUIT:

            # Se o evento é um evento 'QUIT', define a variável 'rodando' como False.
            # Isso irá encerrar o loop principal do jogo e fechar o jogo.
            rodando = False

        # Verifica se o tipo do evento é 'pygame.MOUSEBUTTONDOWN'.
        # 'MOUSEBUTTONDOWN' é um evento que ocorre quando um botão do mouse é pressionado.
        elif evento.type == pygame.MOUSEBUTTONDOWN:

            # Se um botão do mouse foi pressionado, armazena a posição do mouse nesse momento.
            # 'evento.pos' contém as coordenadas (x, y) da posição do mouse.
            inicio_da_selecao = evento.pos

            # Define a variável 'desenhando_selecao' como True.
            # Isso indica que o usuário começou uma seleção (por exemplo, para selecionar uma palavra na grade).
            desenhando_selecao = True  # Começa a desenhar a seleção

        # Verifica se o tipo do evento é 'pygame.MOUSEMOTION' e se 'desenhando_selecao' é True.
        # 'MOUSEMOTION' é um evento que ocorre quando o mouse é movido.
        # A condição adicional verifica se uma seleção está atualmente sendo desenhada.
        elif evento.type == pygame.MOUSEMOTION and desenhando_selecao:

            # Se o mouse está se movendo enquanto uma seleção está sendo desenhada,
            # atualiza a posição final da seleção para a posição atual do mouse.
            fim_da_selecao = evento.pos

        # Verifica se o tipo do evento é 'pygame.MOUSEBUTTONUP'.
        # 'MOUSEBUTTONUP' é um evento que ocorre quando um botão do mouse é solto.
        elif evento.type == pygame.MOUSEBUTTONUP:

            # Quando o botão do mouse é solto, finaliza a seleção.
            # Armazena a posição final da seleção.
            fim_da_selecao = evento.pos

            # Define 'desenhando_selecao' como False.
            # Isso indica que o usuário terminou a seleção (por exemplo, depois de selecionar uma palavra na grade).
            desenhando_selecao = False  # Para de desenhar a seleção


            # Convertendo a posição do clique do mouse em coordenadas da grade
            # Aqui, o código está convertendo as coordenadas do pixel onde o mouse foi clicado ou solto
            # para as coordenadas correspondentes na grade de palavras.

            # Calcula a linha inicial da seleção na grade.
            # 'inicio_da_selecao[1]' é a coordenada y do ponto onde o mouse foi inicialmente pressionado.
            # 'inicio_y' é a coordenada y do início da grade na tela.
            # A diferença entre essas coordenadas é dividida pelo 'ESPACAMENTO' (espaço entre as células da grade)
            # para determinar em qual linha da grade o clique inicial ocorreu.
            inicio_linha = (inicio_da_selecao[1] - inicio_y) // ESPACAMENTO

            # Calcula a coluna inicial da seleção na grade.
            # 'inicio_da_selecao[0]' é a coordenada x do ponto onde o mouse foi inicialmente pressionado.
            # 'inicio_x' é a coordenada x do início da grade na tela.
            # A diferença entre essas coordenadas é dividida pelo 'ESPACAMENTO' para
            # determinar em qual coluna da grade o clique inicial ocorreu.
            inicio_coluna = (inicio_da_selecao[0] - inicio_x) // ESPACAMENTO

            # Calcula a linha final da seleção na grade.
            # 'fim_da_selecao[1]' é a coordenada y do ponto onde o mouse foi solto.
            # O processo de cálculo é o mesmo que o usado para calcular 'inicio_linha'.
            fim_linha = (fim_da_selecao[1] - inicio_y) // ESPACAMENTO

            # Calcula a coluna final da seleção na grade.
            # 'fim_da_selecao[0]' é a coordenada x do ponto onde o mouse foi solto.
            # O processo de cálculo é o mesmo que o usado para calcular 'inicio_coluna'.
            fim_coluna = (fim_da_selecao[0] - inicio_x) // ESPACAMENTO

            # Corrige as coordenadas em caso de arrasto para cima ou para a esquerda
            # Esta parte do código garante que as coordenadas de início e fim estejam na ordem correta,
            # independentemente de o usuário ter arrastado o mouse para cima/esquerda ou para baixo/direita.
            # 'sorted()' é usado para organizar as coordenadas em ordem crescente.
            inicio_linha, fim_linha = sorted([inicio_linha, fim_linha])
            inicio_coluna, fim_coluna = sorted([inicio_coluna, fim_coluna])

            # Certifica-se de que os índices da seleção estão dentro da grade
            # Esta condição verifica se as coordenadas da seleção estão dentro dos limites da grade de palavras.
            # 'TAMANHO_DA_GRADE' é uma constante que define o número de células da grade em cada dimensão.
            if (0 <= inicio_linha < TAMANHO_DA_GRADE and 0 <= inicio_coluna < TAMANHO_DA_GRADE and
                    0 <= fim_linha < TAMANHO_DA_GRADE and 0 <= fim_coluna < TAMANHO_DA_GRADE):

                # Encontrando a palavra selecionada
                # Chama a função 'palavra_na_posicao' para identificar a palavra que está na posição selecionada.
                # 'grade' é a matriz da grade de palavras.
                # '(inicio_linha, inicio_coluna)' e '(fim_linha, fim_coluna)' definem a seleção na grade.
                # 'TAMANHO_DA_GRADE' é passado para garantir que a seleção esteja dentro dos limites da grade.
                palavra_selecionada = palavra_na_posicao(
                    grade, 
                    (inicio_linha, inicio_coluna), 
                    (fim_linha, fim_coluna), 
                    TAMANHO_DA_GRADE
                )


                # Verifica se a palavra selecionada está na lista de palavras
                # Esta linha verifica se a palavra que o jogador selecionou está na lista de palavras da fase atual.
                # 'palavra_selecionada' é a palavra que o jogador selecionou na grade.
                # 'FASES[fase_atual]' refere-se à lista de palavras da fase atual do jogo.
                # 'fase_atual' é uma variável que armazena o número da fase atual que o jogador está jogando.
                if palavra_selecionada in FASES[fase_atual] and palavra_selecionada not in palavras_encontradas:

                    # Se a palavra selecionada estiver na lista de palavras da fase atual e ainda não tiver sido encontrada,
                    # ela é adicionada à lista 'palavras_encontradas'.
                    # 'palavras_encontradas' é uma lista que armazena todas as palavras que o jogador já encontrou.
                    palavras_encontradas.append(palavra_selecionada)

                    # Armazena as posições da palavra na grade
                    # 'inicio_palavra' armazena as coordenadas da linha e coluna onde a seleção da palavra começou na grade.
                    inicio_palavra = (inicio_linha, inicio_coluna)

                    # 'fim_palavra' armazena as coordenadas da linha e coluna onde a seleção da palavra terminou na grade.
                    fim_palavra = (fim_linha, fim_coluna)

                    # A palavra selecionada junto com suas posições de início e fim são adicionadas à lista 'posicoes_palavras_encontradas'.
                    # 'posicoes_palavras_encontradas' é uma lista de tuplas onde cada tupla contém uma palavra encontrada e suas posições iniciais e finais na grade.
                    posicoes_palavras_encontradas.append((palavra_selecionada, inicio_palavra, fim_palavra))

                # Limpa a seleção temporária
                # Esta linha limpa a seleção temporária que foi feita. Isso é útil para reiniciar o estado de seleção
                # após uma palavra ser selecionada ou quando o jogador inicia uma nova seleção.
                selecao_temporaria.clear()
                
    
    # Verifica se o jogo deve continuar ou se todas as palavras foram encontradas
    # Esta condição verifica se o número de palavras encontradas é igual ao número 
    # de palavras na fase atual.
    # 'palavras_encontradas' é a lista das palavras que o jogador já encontrou.
    # 'FASES[fase_atual]' contém a lista de palavras para a fase atual do jogo.
    if len(palavras_encontradas) == len(FASES[fase_atual]):

        # Se o jogador encontrou todas as palavras, imprime uma mensagem de parabéns.
        print("Parabéns! Você encontrou todas as palavras!")

        # Espera por 2 segundos (2000 milissegundos) antes de prosseguir.
        # 'pygame.time.wait(2000)' pausa a execução do programa por 2000 milissegundos.
        # Isso dá ao jogador um tempo para visualizar a mensagem antes de passar para a próxima fase.
        pygame.time.wait(2000)  # Espera 2 segundos antes de passar para a próxima fase

        # Limpa as dicas da fase anterior e cria uma lista temporária para a próxima fase
        # Esta linha limpa a lista de palavras da fase atual, pois o jogador já as encontrou.
        # 'FASES[fase_atual] = []' redefine a lista de palavras para a fase atual como uma lista vazia.
        FASES[fase_atual] = []

        # 'proxima_fase_palavras' é uma variável que armazenará as palavras da próxima fase.
        # Aqui ela é inicializada como uma lista vazia.
        # Isso pode ser usado posteriormente no código para carregar as palavras da próxima fase.
        proxima_fase_palavras = []
        
        # Incrementa a fase atual para avançar para a próxima fase do jogo.
        # 'fase_atual' é uma variável que rastreia a fase atual em que o jogador está.
        # Ao adicionar 1 a 'fase_atual', o jogo se prepara para avançar para a próxima fase.
        fase_atual += 1

        # Verifica se a fase atual ainda está dentro do limite total de fases do jogo.
        # 'total_de_fases' é uma variável que armazena o número total de fases disponíveis no jogo.
        if fase_atual <= total_de_fases:

            # Se ainda houver fases restantes, imprime uma mensagem indicando o início da nova fase.
            print(f"Iniciando a Fase {fase_atual}...")

            # Obtenha as palavras da próxima fase.
            # A função 'obter_palavras_da_fase' é chamada com a 'fase_atual' como argumento.
            # Esta função retorna a lista de palavras que estão na fase atual.
            palavras_da_proxima_fase = obter_palavras_da_fase(fase_atual)

            # Atualiza a lista de palavras para a fase atual no dicionário 'FASES'.
            # 'FASES' é um dicionário onde cada chave corresponde a um número de 
            # fase e o valor é a lista de palavras dessa fase.
            FASES[fase_atual] = palavras_da_proxima_fase

            # Gera uma nova grade com as palavras da fase atual.
            # A função 'gerar_grade' é usada para criar uma nova grade de caça-palavras
            # com as palavras fornecidas.
            # 'palavras_da_proxima_fase' são as palavras a serem incluídas na grade
            # e 'TAMANHO_DA_GRADE' é o tamanho da grade.
            grade = gerar_grade(palavras_da_proxima_fase, TAMANHO_DA_GRADE)

            # Limpa a lista de palavras encontradas e as posições das palavras encontradas.
            # Isso prepara o jogo para a nova fase, removendo quaisquer referências às 
            # palavras encontradas nas fases anteriores.
            palavras_encontradas.clear()
            posicoes_palavras_encontradas.clear()
            
        else:
            
            # Se não houver mais fases restantes, imprime uma mensagem indicando que o jogo terminou.
            print("Você concluiu todas as fases! O jogo terminou.")

            # Define a variável 'rodando' como False, o que causará a saída do
            # loop principal do jogo e encerrará o jogo.
            rodando = False




    # Desenha a seleção temporária (pintando letras enquanto arrasta o mouse)
    # Este comentário explica que o próximo bloco de código é para desenhar uma seleção retangular na tela,
    # o que acontece quando o jogador está segurando e arrastando o mouse para selecionar palavras.

    # Verifica se o jogador está atualmente fazendo uma seleção.
    # 'desenhando_selecao' é uma variável booleana que se torna True quando o jogador começa a arrastar o mouse.
    # 'inicio_da_selecao' e 'fim_da_selecao' são variáveis que armazenam as posições iniciais e finais da seleção, respectivamente.
    if desenhando_selecao and inicio_da_selecao and fim_da_selecao:

        # Desenha um retângulo na tela para representar a seleção do jogador.
        # 'pygame.draw.rect()' é uma função do Pygame usada para desenhar retângulos.
        # Os argumentos são:
        # - 'tela': a superfície onde o retângulo será desenhado.
        # - 'COR_DESTAQUE': a cor do retângulo, definida anteriormente no jogo.
        # - Um tuple que define a posição e o tamanho do retângulo:
        #   - 'inicio_da_selecao[0]': a coordenada x do ponto de início da seleção.
        #   - 'inicio_da_selecao[1]': a coordenada y do ponto de início da seleção.
        #   - 'fim_da_selecao[0] - inicio_da_selecao[0]': a largura do retângulo, calculada como a diferença entre 
        # as coordenadas x do fim e do início da seleção.
        #   - 'fim_da_selecao[1] - inicio_da_selecao[1]': a altura do retângulo, calculada como
        # a diferença entre as coordenadas y do fim e do início da seleção.
        # - '2': a largura da borda do retângulo, em pixels.
        pygame.draw.rect(
            tela,
            COR_DESTAQUE,
            (
                inicio_da_selecao[0],
                inicio_da_selecao[1],
                fim_da_selecao[0] - inicio_da_selecao[0],
                fim_da_selecao[1] - inicio_da_selecao[1]
            ),
            5  # Largura da borda da seleção temporária
        )
    
        
    
    # Atualização da tela
    pygame.display.flip()  # Atualiza a tela inteira uma vez por iteração do loop

    # Controle a taxa de quadros para reduzir o piscamento
    clock.tick(60)  # Por exemplo, 60 quadros por segundo

# Encerramento do jogo
pygame.quit()