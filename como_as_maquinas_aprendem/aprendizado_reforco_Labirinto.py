"""
O Aprendizado por Reforço

O Aprendizado por Reforço (Reinforcement Learning, RL) é uma 
subárea da aprendizagem de máquina que se concentra em como um
agente pode aprender a tomar decisões otimizadas em um ambiente 
para alcançar um objetivo específico. Ao contrário de outros tipos 
de aprendizado de máquina, como aprendizado supervisionado e não
supervisionado, o aprendizado por reforço não se baseia em um conjunto
de dados de treinamento etiquetado ou não etiquetado. Em vez disso, ele
se baseia na interação direta do agente com o ambiente para aprender a 
partir de suas experiências.

Componentes Básicos do Aprendizado por Reforço:

    - Agente: A entidade que aprende a partir da interação com o ambiente.
    - Ambiente: O contexto no qual o agente opera.
    - Estado (State): Uma representação do ambiente que o agente utiliza para tomar decisões.
    - Ação (Action): As operações que o agente pode executar.
    - Política (Policy): A estratégia que o agente segue para tomar 
        decisões. É uma função que mapeia estados em ações.
        
    - Recompensa (Reward): Um sinal do ambiente que informa ao agente
        quão boa foi a ação que ele tomou. O objetivo é maximizar a soma 
        total de recompensas.
        
    - Função de Valor (Value Function): Uma função que estima o valor 
        esperado de um estado, geralmente como a soma esperada de 
        recompensas futuras.
    
    Q-Valor (Q-Value): Uma função que estima a qualidade de uma ação específica 
        tomada em um estado específico.

Algoritmos Comuns:

    - Q-Learning
    - Sarsa
    - Algoritmos baseados em políticas como REINFORCE
    - Aprendizado por Aproximação de Função
    - Métodos de Ator-Crítico

Aplicações:

    - Jogos de tabuleiro e vídeo games (como Go, xadrez, e Dota 2)
    - Robótica
    - Otimização de sistemas de recomendação
    - Controle de sistemas autônomos (como veículos autônomos)
    - Finanças (otimização de portfólio)
    - Saúde (tratamentos personalizados)

O aprendizado por reforço é uma área rica e em rápido crescimento, com 
aplicações que vão desde problemas muito simples até tarefas muito 
complexas e realistas.
"""
print()


"""
Aprendizado por reforço

O aprendizado por reforço (Reinforcement Learning, RL) é uma
área da aprendizagem de máquina onde um agente aprende a tomar 
decisões ao interagir com um ambiente. O objetivo é encontrar uma
política que maximize algum tipo de recompensa cumulativa. 


Exercício de Aprendizado por Reforço: Resolvendo um Labirinto

Objetivo:

O objetivo deste exercício é criar um programa de aprendizado por 
reforço que resolve um labirinto 4x4. Você usará o algoritmo Q-Learning e a
biblioteca Tkinter para a interface gráfica.

Requisitos:

    - O agente deve começar no canto superior esquerdo do labirinto e o
        objetivo é chegar ao canto inferior direito.
    
    - Algumas células do labirinto são obstáculos e o agente não 
        pode passar por elas.
    
    - Use Q-Learning para treinar o agente para encontrar o caminho 
        mais eficiente para o objetivo.
    
    - Implemente uma interface gráfica usando Tkinter para visualizar 
        o labirinto e o movimento do agente.

Especificações:

    Crie uma matriz 4x4 para representar o labirinto, onde:
    
        '0' representa um espaço vazio.
        '1' representa um obstáculo.
        '2' representa a posição inicial (canto superior esquerdo).
        '3' representa a posição objetivo (canto inferior direito).       
        

    Implemente o algoritmo de Q-Learning para treinar o agente. Utilize 
    os seguintes parâmetros:
    
        - Taxa de aprendizado (alpha): 0.1
        - Fator de desconto (gamma): 0.9
        - Política de exploração (epsilon): 0.1
        - Número de episódios para treinamento: 5000

    Utilize Tkinter para criar a interface gráfica:
        - Cada célula do labirinto deve ser um quadrado de 50x50 pixels.
        - A posição inicial deve ser verde, a posição objetivo deve ser 
            vermelha e os obstáculos devem ser pretos.

    Adicione dois botões à interface:
        - "Andar": Quando clicado, o agente deve começar a se mover
            com base na política aprendida.
            
        - "Mudar Labirinto": Quando clicado, um novo labirinto deve 
            ser gerado. Certifique-se de que o novo labirinto seja solucionável.
"""

# Importa a biblioteca Tkinter e a renomeia para "tk"
# Tkinter é usada para criar interfaces gráficas.
import tkinter as tk

# Importa a biblioteca NumPy e a renomeia para "np"
# NumPy é usada para operações numéricas e manipulação de matrizes.
import numpy as np

# Importa o módulo time para manipular tempo (ex: sleep para pausas)
import time

# Importa a biblioteca random para gerar números aleatórios
import random

# Definição de Variáveis Globais
# -------------------------------------

# Variável global janela_aberta é inicializada como True.
# Isso é usado para verificar se a janela Tkinter está aberta ou fechada.
janela_aberta = True

# Variável global matriz_labirinto é inicializada como uma lista vazia.
# Esta lista será preenchida com informações sobre o labirinto.
# Cada célula pode ser 0 (caminho aberto), 1 (parede), 2 (início) ou 3 (fim).
matriz_labirinto = []

# Variável global q_tabela é inicializada como uma matriz de
# zeros com dimensões 16x4 usando NumPy.
# A tabela Q é usada em Q-learning para armazenar os 
# valores Q para cada par estado-ação.
# Temos 16 estados possíveis (uma posição para cada célula em 
# uma matriz 4x4) e 4 ações possíveis (cima, baixo, esquerda, direita).
q_tabela = np.zeros((16, 4))


# Funções Auxiliares
# ------------------------------

# Define a função fechar_janela para fechar a janela Tkinter e 
# atualizar o estado da variável janela_aberta.
def fechar_janela():
    
    # Declara que estamos usando a variável global janela_aberta.
    # Isso é necessário porque queremos alterar o valor de uma
    # variável global dentro desta função.
    global janela_aberta
    
    # Atualiza a variável janela_aberta para False.
    # Isso sinaliza que a janela Tkinter foi fechada.
    janela_aberta = False
    
    # Chama o método destroy do objeto janela_principal.
    # Isso fecha a janela Tkinter e termina o loop principal da interface gráfica.
    janela_principal.destroy()
    


# Define a função 'proximo_estado', que calcula o próximo estado 
# com base no estado e ação atuais.
def proximo_estado(estado_atual, acao_atual):

    # Utiliza a função 'divmod' para calcular o quociente e o resto da 
    # divisão de 'estado_atual' por 4.
    # O quociente é armazenado em 'linha' e o resto em 'coluna'.
    # Este passo converte um índice unidimensional 'estado_atual' em um 
    # índice bidimensional (linha, coluna).
    linha, coluna = divmod(estado_atual, 4)

    # A estrutura condicional abaixo decide o próximo estado baseado
    # na ação escolhida ('acao_atual').

    # Se a ação atual é 0 (mover para cima):
    # Atualiza a variável 'linha', subtraindo 1. Utiliza 'max' para garantir
    # que o valor não seja menor que 0.
    if acao_atual == 0:
        linha = max(linha - 1, 0)

    # Se a ação atual é 1 (mover para baixo):
    # Atualiza a variável 'linha', adicionando 1. Utiliza 'min' para garantir 
    # que o valor não seja maior que 3.
    elif acao_atual == 1:
        linha = min(linha + 1, 3)

    # Se a ação atual é 2 (mover para a esquerda):
    # Atualiza a variável 'coluna', subtraindo 1. Utiliza 'max' para
    # garantir que o valor não seja menor que 0.
    elif acao_atual == 2:
        coluna = max(coluna - 1, 0)

    # Se a ação atual é 3 (mover para a direita):
    # Atualiza a variável 'coluna', adicionando 1. Utiliza 'min' para garantir 
    # que o valor não seja maior que 3.
    elif acao_atual == 3:
        coluna = min(coluna + 1, 3)

    # Após determinar as novas coordenadas (linha, coluna), converte-as de 
    # volta para um único número.
    # Multiplica o valor da linha por 4 e adiciona o valor da coluna.
    # Isso resulta em um índice unidimensional que representa o novo estado.
    return linha * 4 + coluna



# Define a função 'labirinto_solucionavel' para verificar se o 
# labirinto gerado tem um caminho solucionável do início ao fim.
def labirinto_solucionavel():

    # Inicializa um conjunto 'visitados' para manter um registro de todas
    # as células já visitadas no labirinto.
    visitados = set()

    # Inicializa uma pilha 'pilha' e coloca a posição inicial (0,0) 
    # como primeiro elemento.
    pilha = [(0, 0)]

    # Enquanto a pilha não estiver vazia, continua a busca.
    while pilha:

        # Desempilha a posição atual (linha, coluna) do topo da pilha.
        (linha, coluna) = pilha.pop()
        
        # Verifica se a posição atual é o destino (3,3). Se for, retorna True.
        if (linha, coluna) == (3, 3):
            return True
        
        # Varre as direções possíveis: 
        # cima (-1, 0), 
        # baixo (1, 0), 
        # esquerda (0, -1) e 
        # direita (0, 1).
        for (dlinha, dcoluna) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

            # Calcula a nova posição somando as coordenadas atuais 
            # com as direções possíveis.
            nova_linha, nova_coluna = linha + dlinha, coluna + dcoluna
            
            # Verifica se a nova posição está dentro dos limites do tabuleiro.
            if 0 <= nova_linha < 4 and 0 <= nova_coluna < 4:
                
                # Verifica se a nova célula não é uma parede (valor 1) e 
                # ainda não foi visitada.
                if matriz_labirinto[nova_linha][nova_coluna] != 1 and (nova_linha, nova_coluna) not in visitados:
                    
                    # Adiciona a nova posição à pilha.
                    pilha.append((nova_linha, nova_coluna))

                    # Marca a nova posição como visitada, adicionando-a
                    # ao conjunto 'visitados'.
                    visitados.add((nova_linha, nova_coluna))

    # Se o loop terminar e a função ainda não tiver retornado True, 
    # então o labirinto não é solucionável.
    return False
        
    
# Define a função 'mudar_labirinto' que gera um novo labirinto, 
# desenha ele na interface e treina o modelo de Q-learning.
def mudar_labirinto():

    # Utiliza a palavra-chave 'global' para indicar que a função vai 
    # modificar a variável global 'matriz_labirinto'.
    global matriz_labirinto

    # Entra em um loop infinito até encontrar um labirinto solucionável.
    while True:

        # Chama a função 'criar_labirinto' para gerar uma nova 
        # matriz de labirinto.
        criar_labirinto()

        # Chama a função 'labirinto_solucionavel' para verificar se o 
        # labirinto atual tem uma solução.
        # Se o labirinto for solucionável, sai do loop.
        if labirinto_solucionavel():
            break
            
    
    # Limpa todos os desenhos anteriores do painel.
    painel.delete("all")
    
    
    # Chama a função 'desenhar_labirinto' para desenhar o novo
    # labirinto na interface gráfica.
    desenhar_labirinto()

    # Chama a função 'treinar_modelo' para treinar o modelo de 
    # Q-learning com base no novo labirinto.
    treinar_modelo()

    
# Define a função 'criar_labirinto' responsável por inicializar
# e preencher a matriz do labirinto.
def criar_labirinto():

    # Utiliza a palavra-chave 'global' para indicar que a função vai 
    # modificar a variável global 'matriz_labirinto'.
    global matriz_labirinto

    # Cria uma matriz 4x4 preenchida com zeros. 
    # Um zero indica uma célula vazia na matriz do labirinto.
    matriz_labirinto = [[0 for _ in range(4)] for _ in range(4)]
    
    
    # Define a célula de partida (canto superior esquerdo) como sendo do tipo 2.
    # O número 2 serve como um marcador para indicar o ponto de partida do agente.
    matriz_labirinto[0][0] = 2
    
    
    # Define a célula de destino (canto inferior direito) como sendo do tipo 3.
    # O número 3 serve como um marcador para indicar o ponto de chegada do agente.
    matriz_labirinto[3][3] = 3
    
    # Inicia um loop que será executado 5 vezes para colocar obstáculos no labirinto.
    for _ in range(5):

        # Gera coordenadas aleatórias para a linha e a coluna dentro 
        # dos limites da matriz 4x4.
        linha, coluna = random.randint(0, 3), random.randint(0, 3)
    
        # Verifica se a célula escolhida aleatoriamente está 
        # vazia (ou seja, contém um zero).
        if matriz_labirinto[linha][coluna] == 0:

            # Se a célula está vazia, ela se torna um obstáculo, 
            # marcado com o número 1.
            matriz_labirinto[linha][coluna] = 1
            
            
# Define a função 'treinar_modelo' responsável por treinar 
# o agente usando o algoritmo de Q-Learning.
def treinar_modelo():

    # Declara que a função modificará as variáveis 
    # globais 'q_tabela' e 'matriz_labirinto'.
    global q_tabela, matriz_labirinto

    # Define o valor de alpha, o fator de aprendizado, como 0.1.
    alpha = 0.1

    # Define o valor de gamma, o fator de desconto, como 0.9.
    gamma = 0.9

    # Define o valor de epsilon, utilizado para a estratégia epsilon-greedy, como 0.1.
    epsilon = 0.1

    # Define o número total de episódios para treinar o modelo como 5000.
    num_episodios = 5000

    # Inicializa a Q-tabela com zeros. A tabela tem 16 estados
    # (para as 16 células) e 4 ações (cima, baixo, esquerda, direita).
    q_tabela = np.zeros((16, 4))
    
    # Inicia o loop de treinamento para um número específico de episódios.
    for episodio in range(num_episodios):

        # Define o estado inicial como 0, que representa a célula 
        # inicial (0,0) no labirinto.
        estado = 0

        # O loop continua até que o estado atinja 15, que é o estado 
        # objetivo (3,3) no labirinto.
        while estado != 15:

            # Implementa a estratégia epsilon-greedy para escolher uma ação.
            if np.random.rand() < epsilon:
                
                # Escolhe uma ação aleatória.
                acao = np.random.choice(4)
                
            else:
                
                # Escolhe a melhor ação com base na Q-tabela atual.
                acao = np.argmax(q_tabela[estado])

            # Obtém o próximo estado com base no estado atual e na ação escolhida.
            estado_seguinte = proximo_estado(estado, acao)
            
            
            
            """
            estado_seguinte // 4 e estado_seguinte % 4: Aqui, estamos transformando o
                estado unidimensional estado_seguinte em duas coordenadas bidimensionais
                que correspondem à localização na matriz do labirinto. O operador // é a 
                divisão inteira, e % é o operador módulo.
            
                    Exemplo: se estado_seguinte = 5, então estado_seguinte // 4 = 1 e 
                    estado_seguinte % 4 = 1, o que corresponderia à localização (1,1) na 
                    matriz do labirinto.

            matriz_labirinto[estado_seguinte // 4][estado_seguinte % 4]: Esta expressão 
                obtém o valor na matriz do labirinto correspondente ao próximo estado. O valor 
                poderia ser 0 (caminho aberto), 1 (obstáculo), 2 (estado inicial), 
                ou 3 (estado final).

            matriz_labirinto[estado_seguinte // 4][estado_seguinte % 4] == 1: Estamos 
                verificando se o valor na posição do próximo estado na matriz do labirinto 
                é 1, o que significaria que há um obstáculo nesse estado.

            recompensa = -100 if ... else 0: Finalmente, a variável recompensa é 
                definida com base nesta condição. Se a posição do próximo estado contém
                um obstáculo (valor 1), a recompensa é definida como -100. Caso contrário, 
                ela é definida como 0.

            Em resumo, essa linha de código é responsável por calcular a recompensa 
                para uma transição de estado específica, penalizando fortemente o agente 
                se ele se mover para uma célula contendo um obstáculo.
            """
            # Calcula a recompensa. Se o próximo estado contém um
            # obstáculo, a recompensa é -100.
            recompensa = -100 if matriz_labirinto[estado_seguinte // 4][estado_seguinte % 4] == 1 else 0
            
            
            # Se o próximo estado é o estado objetivo, a recompensa é 100.
            if estado_seguinte == 15:
                recompensa = 100
                
            
            """
            é a atualização da Q-tabela usando a equação Q-Learning.
            
            q_tabela[estado, acao]: Esta é a entrada na Q-tabela para o estado 
                atual e a ação atual. Ela contém o valor Q aprendido até agora para 
                esta combinação de estado-ação.

            alpha: Esta é a taxa de aprendizagem. Ela define até que ponto o 
                novo valor Q calculado substitui o valor Q anterior. Se alpha = 1, o 
                valor aprendido substitui completamente o antigo. Se alpha = 0, o 
                valor aprendido não é incorporado de forma alguma. Tipicamente, você 
                quer um valor entre 0 e 1.

            recompensa: Esta é a recompensa obtida ao tomar a ação acao no estado
                e chegar ao estado_seguinte.

            gamma: Este é o fator de desconto, que pondera quão importante são as 
                recompensas futuras em relação às atuais. Se gamma = 0, o agente é 
                totalmente "miópe" e só se preocupa com recompensas imediatas. Se 
                gamma = 1, o agente valoriza todas as recompensas futuras tanto 
                quanto as atuais.

            np.max(q_tabela[estado_seguinte]): Este termo pega o maior valor Q possível 
                para o próximo estado (estado_seguinte) considerando todas as ações 
                possíveis. Isso é parte do aprendizado: estamos sempre procurando o 
                "melhor futuro" possível a partir do próximo estado.

            (1 - alpha) * q_tabela[estado, acao] + alpha * (recompensa + gamma * np.max(q_tabela[estado_seguinte])): Esta é a 
                equação Q-Learning em si. Ela atualiza o valor Q para a combinação atual 
                de estado e ação com base na recompensa recebida e na melhor estimativa 
                futura (parte gamma * np.max(q_tabela[estado_seguinte])).

            A ideia da equação é misturar o valor Q atual e o novo valor Q de tal
                forma que o resultado reflete mais precisamente o valor "real" da
                ação no estado dado. O valor "real" é uma combinação da recompensa 
                imediata e da melhor recompensa futura que se pode obter a partir do
                próximo estado. Isso é feito ponderando a contribuição do valor Q atual 
                e o valor Q recém-calculado usando a taxa de aprendizagem alpha.
            """
            # Atualiza a Q-tabela usando a fórmula Q-Learning.
            q_tabela[estado, acao] = (1 - alpha) * q_tabela[estado, acao] + alpha * (recompensa + gamma * np.max(q_tabela[estado_seguinte]))

            # Atualiza o estado atual para o próximo estado.
            estado = estado_seguinte
            
    
    
# Definindo a função 'mover_agente', cuja responsabilidade é mover 
# o agente através do labirinto.
def mover_agente():
    
    # Utilizando as variáveis globais que vão ser usadas nessa função.
    # 'janela_aberta' indica se a janela do Tkinter ainda está aberta.
    # 'matriz_labirinto' contém a estrutura atual do labirinto.
    # 'q_tabela' contém os valores Q aprendidos durante o treinamento.
    global janela_aberta, matriz_labirinto, q_tabela
    
    # Inicializando a variável 'estado' como 0, o que geralmente 
    # representa o ponto de partida no labirinto.
    estado = 0
    
    # O loop 'while' continua executando até que o agente alcance o estado final 15.
    while estado != 15:
        
        # Verificando se a janela da interface gráfica ainda está aberta.
        # Se a janela foi fechada, a função 'return' é chamada para sair da função.
        if not janela_aberta:
            return
        
        
        # A variável 'acao' é determinada pegando a ação que tem o 
        # maior valor Q para o estado atual.
        # Isso é feito buscando o índice do maior valor na linha da 
        # 'q_tabela' correspondente ao 'estado' atual.
        acao = np.argmax(q_tabela[estado])
        
        # A função 'proximo_estado' é chamada para calcular qual será 
        # o próximo estado com base no estado atual e a ação escolhida.
        estado_seguinte = proximo_estado(estado, acao)
        
        # Converte o estado em uma forma unidimensional (estado_seguinte) para
        # coordenadas bidimensionais (linha, coluna).
        linha, coluna = divmod(estado_seguinte, 4)
        
        
        """
        é responsável por desenhar um círculo (oval) azul no canvas, representando a
            posição atual do agente no labirinto.

        painel.create_oval: Este método é chamado no objeto painel, que é 
            um Canvas Tkinter. O método create_oval desenha um oval (que neste caso é 
            um círculo, pois a altura e a largura são iguais) no Canvas.

        coluna * 50 + 10, linha * 50 + 10, coluna * 50 + 40, linha * 50 + 40: Estas 
            são as coordenadas que definem a caixa delimitadora dentro da qual o oval 
            será desenhado. A caixa começa no ponto (coluna * 50 + 10, linha * 50 + 10) e 
            termina em (coluna * 50 + 40, linha * 50 + 40). Aqui, linha e coluna são as
            posições do agente no labirinto. Os números adicionados (+ 10 e + 40) centralizam
            o oval dentro da célula do labirinto, que é um retângulo de 50x50 pixels.

        fill='blue': Este parâmetro define que o círculo será preenchido com a cor azul.

        tags='agente': Este parâmetro permite associar uma tag ao oval. Isso é útil se 
            você quiser fazer alguma operação em todos os objetos que compartilham essa 
            tag mais tarde, como excluí-los ou movê-los.

        Então, resumindo, esta linha de código desenha um círculo azul que representa 
            o agente no labirinto. O círculo é posicionado na célula atual do agente e 
            é desenhado de forma a ser centralizado dentro dessa célula.
        """
        # Desenhando o agente (um círculo azul) na posição calculada no painel Tkinter.
        # A posição é calculada multiplicando as coordenadas de linha e coluna 
        # por 50 e ajustando para caber dentro do quadro.
        painel.create_oval(coluna * 50 + 10, linha * 50 + 10, coluna * 50 + 40, linha * 50 + 40, fill='blue', tags='agente')
        
        # O método 'update' é chamado para garantir que o painel Tkinter
        # mostre as atualizações gráficas (neste caso, o movimento do agente).
        painel.update()
        
        # A função 'time.sleep(1)' pausa o programa por 1 segundo para 
        # que o usuário possa ver o agente se mover.
        time.sleep(1)
        
        # O método 'delete' remove o círculo azul anterior, para que um 
        # novo possa ser desenhado na próxima iteração do loop.
        painel.delete('agente')
        
        # Atualizando o estado atual para ser o 'estado_seguinte', permitindo que 
        # o agente continue se movendo no próximo ciclo do loop.
        estado = estado_seguinte
        
        
    
    
# Define a função 'desenhar_labirinto' responsável por desenhar 
# o labirinto no painel Tkinter.
def desenhar_labirinto():
    
    # Acessa a variável global 'matriz_labirinto' que contém a 
    # estrutura atual do labirinto.
    global matriz_labirinto
    
    # Percorre cada linha do labirinto, indexada por 'i'.
    for i in range(4):
        
        # Percorre cada coluna do labirinto na linha atual, indexada por 'j'.
        for j in range(4):
            
            # Inicialmente, define a cor do quadrado como 'black' se o 
            # valor na 'matriz_labirinto' for 1 (representando uma parede)
            # e 'white' se for 0 (representando um espaço aberto).
            cor = 'black' if matriz_labirinto[i][j] == 1 else 'white'
            
            # Se o valor na 'matriz_labirinto' for 2, isso representa o ponto de partida. 
            # Portanto, define a cor do quadrado como 'green'.
            if matriz_labirinto[i][j] == 2:
                cor = 'green'
            
            # Se o valor na 'matriz_labirinto' for 3, isso representa o ponto de chegada.
            # Portanto, define a cor do quadrado como 'red'.
            elif matriz_labirinto[i][j] == 3:
                cor = 'red'
                
            
            """
            é responsável por desenhar um único retângulo na tela, que é 
                uma célula do labirinto.

            painel.create_rectangle: Este método é chamado no objeto painel, 
                que é um Canvas Tkinter. O método create_rectangle desenha um 
                retângulo no Canvas.

            j * 50, i * 50, j * 50 + 50, i * 50 + 50: Estas são as coordenadas 
                que definem o retângulo. O retângulo começa na 
                coordenada (j * 50, i * 50) e termina na 
                coordenada (j * 50 + 50, i * 50 + 50). Essas coordenadas 
                são multiplicadas por 50 para escalonar o tamanho do retângulo, 
                tornando-o grande o suficiente para ser visto facilmente. 
                Aqui, i e j são índices da matriz matriz_labirinto que 
                representam as linhas e colunas do labirinto, respectivamente.

            fill=cor: O parâmetro fill define a cor de preenchimento do 
                retângulo. A variável cor é definida anteriormente na função, 
                com base no valor da célula do labirinto representada por 
                matriz_labirinto[i][j]. A cor pode ser preta (para um obstáculo), 
                branca (para um espaço vazio), verde (para a célula de início), ou 
                vermelha (para a célula de destino).

            Então, resumindo, essa linha de código desenha um retângulo (uma célula 
            do labirinto) no Canvas Tkinter, preenchendo-o com a cor adequada. Isso é
            feito para cada célula do labirinto, criando assim a representação gráfica
            completa do labirinto na GUI.
            """
            
            # Usa a função 'create_rectangle' do Tkinter para desenhar
            # um retângulo (quadrado, neste caso) no painel.
            # As coordenadas do quadrado são calculadas com base nos índices 'i' e 'j'.
            # O 'fill=cor' preenche o quadrado com a cor determinada.
            painel.create_rectangle(j * 50, i * 50, j * 50 + 50, i * 50 + 50, fill=cor)
    

    
# Inicializa a janela Tkinter e a armazena na 
# variável 'janela_principal'.
janela_principal = tk.Tk()

# Define o título da janela como "Labirinto com Q-Learning".
janela_principal.title("Labirinto com Q-Learning")

# Cria um objeto Canvas (painel) Tkinter, onde o labirinto
# e outros elementos serão desenhados.
# Define sua largura e altura como 200x200 pixels.
painel = tk.Canvas(janela_principal, width=200, height=200)

# Empacota o Canvas na janela principal para que ele seja exibido.
painel.pack()

# Chama a função 'mudar_labirinto()' para criar e
# exibir o labirinto inicial.
mudar_labirinto()

# Cria um botão com o rótulo "Andar" e associa a função 'mover_agente()' a ele.
# Quando o botão for clicado, a função 'mover_agente()' será chamada.
botao_andar = tk.Button(janela_principal, 
                        text="Andar", 
                        command=mover_agente)

# Empacota o botão 'botao_andar' para que ele 
# seja exibido na janela principal.
botao_andar.pack()

# Cria um botão com o rótulo "Mudar Labirinto" e 
# associa a função 'mudar_labirinto()' a ele.
# Quando o botão for clicado, a função 'mudar_labirinto()' será chamada.
botao_mudar_labirinto = tk.Button(janela_principal, 
                                  text="Mudar Labirinto", 
                                  command=mudar_labirinto)

# Empacota o botão 'botao_mudar_labirinto' para que ele 
# seja exibido na janela principal.
botao_mudar_labirinto.pack()

# Define um protocolo para o evento de fechamento da janela.
# Quando a janela for fechada, a função 'fechar_janela()' será chamada.
janela_principal.protocol("WM_DELETE_WINDOW", fechar_janela)



# Entra no loop principal da Tkinter para manter a
# janela aberta e responsiva.
janela_principal.mainloop()
