# Importa o módulo tkinter e renomeia-o como tk para 
        # facilitar o acesso às suas funções.
import tkinter as tk

# Importa o módulo messagebox do tkinter para permitir a 
        # criação de janelas de diálogo (como alertas e confirmações).
from tkinter import messagebox

# Importa o módulo random do Python, que fornece funções para 
        # gerar números aleatórios, útil para lógicas como 
        # sorteio ou aleatoriedade em jogos.
import random

# Define a classe BatalhaNaval para implementar a lógica do jogo.
class BatalhaNaval:
    
    # Construtor da classe que inicializa o jogo.
    def __init__(self, janela):
        
        # Associa a janela principal do Tkinter passada como 
                # argumento à variável de instância 'janela'.
        self.janela = janela
        
        # Define o título da janela.
        self.janela.title("Exercício Batalha Naval")
        
        # Configura a cor de fundo da janela principal.
        self.janela.configure(bg="#f0f0f0")
        
        # Define o tamanho da janela para 800x600 pixels.
        self.janela.geometry("800x600")  # Ajuste do tamanho da janela

        # Define o tamanho do tabuleiro de jogo como uma grade 15x15.
        self.TAMANHO_TABULEIRO = 15
        
        # Lista com os tamanhos dos navios a serem posicionados no tabuleiro.
        self.TAMANHO_NAVIOS = [5, 4, 3, 3, 2]
        
        # Define o número de vidas do jogador.
        self.vidas = 15
        
        # Inicializa a pontuação do jogador como zero.
        self.pontuacao = 0

        # Cria um conjunto para rastrear os navios que foram afundados.
        self.navios_afundados = set()  # Conjunto para 
                # rastrear navios afundados
        
        # Calcula o total de navios baseando-se no tamanho 
                # da lista TAMANHO_NAVIOS.
        self.total_navios = len(self.TAMANHO_NAVIOS)  # Total de navios no jogo

        # Cria uma grade para o tabuleiro inimigo, chamando o método criar_grade.
        self.grade_inimigo = self.criar_grade()
        
        # Posiciona os navios na grade de forma aleatória.
        self.posicionar_navios_aleatoriamente(self.grade_inimigo, self.TAMANHO_NAVIOS)

        # Chama o método para criar os widgets de interface.
        self.criar_widgets()
        
        # Atualiza a exibição das vidas do jogador na interface.
        self.atualizar_vidas()
        
        # Atualiza a exibição da pontuação do jogador na interface.
        self.atualizar_pontuacao()
        
        # Tenta carregar a pontuação do jogador de uma 
                # sessão anterior do jogo.
        self.carregar_pontuacao()


    # Este método é responsável por criar uma matriz que 
            # representará o tabuleiro do jogo Batalha Naval.
    # A matriz é composta de listas aninhadas, onde cada 
            # sublista representa uma linha do tabuleiro.
    def criar_grade(self):
        
        # Cria uma matriz quadrada para representar o tabuleiro de jogo, 
                # onde cada célula inicialmente tem o valor 0.
        # O valor 0 indica que a célula está vazia, ou seja, sem 
                # nenhum navio posicionado nela.
        # A compreensão de lista é usada para criar uma lista de 
                # listas (matriz), com a dimensão definida 
                # por 'TAMANHO_TABULEIRO'.
        # O uso do '_' como variável na compreensão de lista 
                # indica que o índice não é usado no corpo do 
                # loop, sendo apenas um iterador.
        # Isso resulta em um tabuleiro de 15x15 células, todas 
                # inicializadas com o valor 0, indicando que estão vazias.
        return [[0 for _ in range(self.TAMANHO_TABULEIRO)] for _ in range(self.TAMANHO_TABULEIRO)]



    def criar_widgets(self):
        
        # Cria um rótulo para servir como título do jogo na 
                # janela principal. 
        # O texto é "Exercício Batalha Naval".
        # Define a fonte do texto para Arial tamanho 24 e 
                # a cor de fundo igual ao fundo da janela principal.
        self.rotulo_titulo = tk.Label(self.janela, text="Exercício Batalha Naval", font=("Arial", 24), bg="#f0f0f0")
        
        # Posiciona o rótulo do título na janela usando 'pack', 
                # que é um gerenciador de geometria do Tkinter.
        # 'pady=10' adiciona um espaço vertical de 10 
                # pixels acima e abaixo do rótulo.
        self.rotulo_titulo.pack(pady=10)
    
        # Cria um frame para agrupar visualmente informações 
                # relacionadas ao jogo, como vidas e pontuação.
        # Configura o fundo do frame para combinar com o fundo da janela.
        self.frame_info = tk.Frame(self.janela, bg="#f0f0f0")
        
        # Posiciona o frame na janela principal. Sem parâmetros 
                # específicos, ele se ajusta ao topo central da janela.
        self.frame_info.pack()
    
        # Cria um rótulo (Label) para exibir as vidas do jogador. 
        # A função `f-string` é usada para interpolar variáveis 
                # diretamente nas strings, permitindo a atualização 
                # dinâmica do texto conforme o estado do jogo muda.
        self.rotulo_vidas = tk.Label(self.frame_info, 
                                     text=f"Vidas: {self.vidas}", 
                                     font=("Arial", 14), 
                                     bg="#f0f0f0")
        
        # Posiciona o rótulo das vidas dentro do frame de 
                # informações no lado esquerdo. 
        # O parâmetro 'padx=20' adiciona um padding de 20 pixels
                # à direita do rótulo, evitando que elementos 
                # vizinhos fiquem visualmente colados a ele, e 
                # contribuindo para uma estética mais clara e organizada.
        self.rotulo_vidas.pack(side=tk.LEFT, padx=20)
        
        # Cria um rótulo para mostrar a pontuação do jogador. 
        # Essa pontuação é atualizada dinamicamente durante o jogo,
                # e é essencial para dar ao jogador feedback 
                # imediato sobre seu desempenho.
        self.rotulo_pontuacao = tk.Label(self.frame_info, 
                                         text=f"Pontuação: {self.pontuacao}", 
                                         font=("Arial", 14), 
                                         bg="#f0f0f0")
        
        # Posiciona o rótulo da pontuação ao lado do rótulo de vidas. 
        # Usar o mesmo alinhamento ('LEFT') e o mesmo padding horizontal
                # ajuda a manter a interface uniforme e fácil de ler. 
        # Isso é importante para a usabilidade, permitindo que o jogador
                # visualize rapidamente seus stats sem confusão.
        self.rotulo_pontuacao.pack(side=tk.LEFT, padx=20)
        
        # Cria um frame para servir como o tabuleiro onde o jogador 
                # realizará ações de ataque. A cor de fundo escolhida,
                # um cinza claro '#f0f0f0', é usada para manter a 
                # consistência visual da aplicação, ajudando na 
                # concentração do jogador sem distrações visuais excessivas.
        self.frame_tabuleiro = tk.Frame(self.janela, 
                                        bg="#f0f0f0")
        
        # Posiciona o frame do tabuleiro imediatamente abaixo 
                # dos rótulos de informação. 
        # O espaçamento vertical de 10 pixels ('pady=10')
                # serve para separar visualmente o tabuleiro 
                # das informações, facilitando a distinção entre as 
                # áreas de jogo e de status.
        # Esse espaçamento também contribui para uma sensação 
                # de organização e evita uma interface sobrecarregada.
        self.frame_tabuleiro.pack(pady=10)


    
        # Inicializa um dicionário para armazenar os botões que 
                # representam as células do tabuleiro.
        # Este dicionário permite acessar facilmente qualquer 
                # célula do tabuleiro por suas coordenadas (linha, coluna).
        self.botoes_celulas = {}
        
        # Inicia um loop duplo para percorrer todas as posições do 
                # tabuleiro, que é definido pelo atributo 'TAMANHO_TABULEIRO'.
        # O loop externo itera sobre as linhas e o loop 
                # interno sobre as colunas.
        for linha in range(self.TAMANHO_TABULEIRO):
            
            for coluna in range(self.TAMANHO_TABULEIRO):
                
                # Cria um botão para cada célula do tabuleiro.
                # 'width=2' e 'height=1' definem as dimensões do botão.
                # 'bg="#add8e6"' define a cor de fundo do botão 
                        # como um azul claro.
                # 'relief="raised"' dá ao botão um efeito visual de 
                        # relevo, tornando-o mais perceptível como uma 
                        # célula interativa.
                # 'command=lambda l=linha, c=coluna: self.manejar_ataque(l, c)' 
                        # define a ação que ocorre quando o botão é clicado.
                # O uso de 'lambda' com parâmetros default permite passar as 
                        # coordenadas atuais da célula para a função de manejo de ataque.
                botao = tk.Button(self.frame_tabuleiro, 
                                  width=2, 
                                  height=1, 
                                  bg="#add8e6", 
                                  relief="raised",
                                  command=lambda l=linha, c=coluna: self.manejar_ataque(l, c))
        
                # Posiciona cada botão na grid do 'frame_tabuleiro' nas 
                        # posições especificadas pelas variáveis 'linha' e 'coluna'.
                # O método 'grid' é usado para organizar os botões em 
                        # formato de grade, correspondente ao tabuleiro do jogo.
                botao.grid(row=linha, column=coluna)
        
                # Armazena o botão recém-criado no dicionário 'botoes_celulas', 
                        # usando a tupla (linha, coluna) como chave.
                # Isso permite que alterações no estado do botão sejam 
                        # facilmente acessadas e modificadas durante o jogo,
                        # como mudar a cor do botão quando um navio é 
                        # atingido ou quando uma célula é revelada como água.
                self.botoes_celulas[(linha, coluna)] = botao

        
        # Cria um botão que permite ao jogador visualizar a 
                # posição dos navios no tabuleiro.
        self.botao_mostrar_navios = tk.Button(self.janela, 
                                              text="Mostrar Navios", 
                                              command=self.mostrar_navios)

        # Posiciona o botão para mostrar os navios na interface.
        self.botao_mostrar_navios.pack(pady=10)
    
        # Prepara um modal (ainda não criado) que será usado 
                # para permitir ao jogador reiniciar o jogo após terminar.
        # Inicialmente, é definido como None e será 
                # configurado quando necessário.
        self.modal_reiniciar = None

        

    # Este método atualiza o rótulo de vidas na interface do 
            # usuário para refletir o número atual de vidas do jogador.
    # Ele é chamado toda vez que o número de vidas do jogador 
            # muda, como quando ele erra um ataque.
    def atualizar_vidas(self):
        
        # Usa o método 'config' do Tkinter para alterar o texto do 
                # rótulo de vidas. O texto é atualizado dinamicamente
                # para exibir o valor da variável 'self.vidas', 
                # que contém o número atual de vidas do jogador.
        self.rotulo_vidas.config(text=f"Vidas: {self.vidas}")


    # Este método atualiza o rótulo de pontuação na interface do 
            # usuário para refletir a pontuação atual do jogador.
    # Ele é chamado sempre que o jogador acerta um navio,
            # aumentando a pontuação.
    def atualizar_pontuacao(self):
    
        # Usa o método 'config' para alterar o texto do rótulo de 
                # pontuação. 
        # O valor exibido é a variável 'self.pontuacao',
                # que contém a pontuação atualizada do jogador.
        self.rotulo_pontuacao.config(text=f"Pontuação: {self.pontuacao}")

    
    # Este método tenta carregar a pontuação salva anteriormente 
            # do arquivo "batalha_naval_pontuacao.txt".
    # Se o arquivo for encontrado, a pontuação é lida e 
            # carregada no jogo. Caso contrário, se o arquivo não existir,
            # a pontuação é inicializada como 0.
    def carregar_pontuacao(self):
            
        try:
            
            # Tenta abrir o arquivo "batalha_naval_pontuacao.txt" 
                    # no modo de leitura ('r').
            # Se o arquivo não existir, um erro FileNotFoundError será gerado.
            with open("batalha_naval_pontuacao.txt", "r") as arquivo:
                
                # Lê o conteúdo do arquivo (a 
                        # pontuação salva) e converte para inteiro.
                # A função read() lê o conteúdo como string, por 
                        # isso é necessário converter para int.
                self.pontuacao = int(arquivo.read())
                
                # Atualiza o rótulo de pontuação na interface 
                        # com a pontuação recém-carregada.
                # Isso garante que o jogador veja sua pontuação 
                        # salva no início do jogo.
                self.atualizar_pontuacao()
    
        # Se o arquivo não for encontrado (FileNotFoundError), o 
                # bloco 'except' é executado.
        # Isso acontece quando o jogo é iniciado pela primeira 
                # vez ou se o arquivo foi excluído.
        except FileNotFoundError:
            
            # Se o arquivo não for encontrado, define a pontuação 
                    # inicial como 0, pois não há pontuação salva.
            self.pontuacao = 0
    

    # Este método salva a pontuação atual do jogador em um 
            # arquivo de texto. Ele pode ser chamado após cada atualização
            # de pontuação para garantir que o progresso do 
            # jogador seja salvo e possa ser recuperado depois.
    def salvar_pontuacao(self):
    
        # Abre (ou cria) um arquivo chamado 'batalha_naval_pontuacao.txt' 
                # no modo de escrita ('w').
        # Isso significa que o conteúdo anterior do arquivo será substituído.
        with open("batalha_naval_pontuacao.txt", "w") as arquivo:
            
            # Escreve a pontuação atual do jogador no arquivo 
                    # como uma string.
            # 'self.pontuacao' é a pontuação atual e é convertida 
                    # para string antes de ser gravada no arquivo.
            arquivo.write(str(self.pontuacao))
            


    # Este método lida com a lógica quando o jogador clica em 
            # uma célula do tabuleiro.
    # Os parâmetros 'linha' e 'coluna' indicam a posição da 
            # célula que o jogador atacou.
    # A função verifica se o ataque atingiu um navio, água ou 
            # uma célula já atacada, e atualiza o estado do jogo de acordo.
    def manejar_ataque(self, linha, coluna):
            
        # Recupera o valor da célula no tabuleiro do inimigo, 
                # que indica o estado da célula:
        # 0 significa que é água (nenhum navio está nesta posição), 
                # um valor positivo indica que há um navio presente,
                # e um valor negativo indica que a célula já foi 
                # atacada anteriormente.
        celula_valor = self.grade_inimigo[linha][coluna]
    
        # Verifica se o valor da célula é maior que zero. 
        # Isso significa que há um navio (não atingido) na célula.
        if celula_valor > 0:
            
            # Armazena o identificador do navio na variável 'ship_id' 
                    # para ser utilizado mais tarde,
                    # como, por exemplo, para verificar se o 
                    # navio foi completamente afundado.
            ship_id = celula_valor
            
            # Atualiza a cor do botão correspondente na interface gráfica, 
                    # configurando o fundo como vermelho (#ff0000)
            # para indicar que o navio foi atingido, e desabilita o botão 
                    # para impedir futuros cliques nesta célula.
            self.botoes_celulas[(linha, coluna)].configure(bg="#ff0000", state="disabled")
            
            # Marca a célula no tabuleiro do inimigo como atacada ao 
                    # negativar seu valor. Isso permite que o jogo rastreie
                    # que esta célula já foi atacada, preservando o ID do 
                    # navio atingido, mas agora como um número negativo.
            self.grade_inimigo[linha][coluna] = -celula_valor
            
            # Incrementa a pontuação do jogador, já que 
                    # ele acertou um navio.
            self.pontuacao += 1
            
            # Exibe uma caixa de mensagem informando ao 
                    # jogador que ele acertou um navio.
            messagebox.showinfo("Acertou!", "Você acertou um navio!")
            
            # Chama o método 'verificar_afundou' para verificar se o 
                    # navio atingido foi completamente destruído.
            self.verificar_afundou(ship_id)
        
        # Se o valor da célula for 0, significa que o jogador 
                # atingiu uma célula de água, ou seja, não havia nenhum navio.
        elif celula_valor == 0:
            
            # Atualiza a cor do botão correspondente para 
                    # branco (#ffffff) para indicar que o ataque foi em água,
                    # e desabilita o botão, pois essa célula já foi 
                    # atacada e não pode ser clicada novamente.
            self.botoes_celulas[(linha, coluna)].configure(bg="#ffffff", state="disabled")
            
            # Marca a célula no tabuleiro como "atacada" colocando o 
                    # valor -1. 
            # Isso indica que esta célula de água já foi atacada.
            self.grade_inimigo[linha][coluna] = -1
            
            # Diminui o número de vidas do jogador, já que 
                    # ele desperdiçou um ataque em água.
            self.vidas -= 1
            
            # Exibe uma caixa de mensagem informando que o 
                    # jogador errou (acertou a água).
            messagebox.showinfo("Errou", "Você acertou na água.")
        
        # Se o valor da célula for negativo, significa que o 
                # jogador já havia atacado essa célula anteriormente,
                # então o jogo não faz nada e simplesmente retorna,
                # pois o ataque é inválido.
        else:
            
            # Retorna do método sem fazer nada, já que a 
                    # célula já foi clicada antes.
            return
    
        # Após qualquer ataque (bem-sucedido ou não), atualiza a 
                # exibição de vidas na interface do jogo.
        self.atualizar_vidas()
        
        # Também atualiza a exibição da pontuação do jogador.
        self.atualizar_pontuacao()
        
        # Salva a pontuação do jogador em um arquivo, 
                # para recuperação futura ou ranking.
        self.salvar_pontuacao()
    
        # Verifica se o jogador ainda tem vidas. Se o número 
                # de vidas for 0, o jogo termina.
        if self.vidas == 0:
            
            # Exibe uma mensagem informando que o jogo acabou e o jogador perdeu.
            messagebox.showinfo("Fim de Jogo", "Fim de jogo! Você perdeu.")
            
            # Desabilita o tabuleiro, impedindo que o jogador 
                    # continue clicando após perder.
            self.desabilitar_tabuleiro()
            
            # Mostra um modal oferecendo a opção de reiniciar o jogo.
            self.mostrar_modal_reinicio("Você perdeu!")


    # Cria uma nova janela modal que será usada para exibir uma 
            # mensagem ao jogador, oferecendo a opção de reiniciar o jogo.
    # 'mensagem' é uma string que será exibida ao jogador,
            # explicando o motivo pelo qual o modal está sendo exibido
            # (como, por exemplo, "Você perdeu!" ou "Você 
            # afundou todos os navios!").
    def mostrar_modal_reinicio(self, mensagem):
        
        
        # Cria uma nova janela (Toplevel) chamada 'modal_reiniciar' 
                # que será usada para o modal de reinício do jogo.
        # Essa janela é separada da principal, mas ainda está 
                # relacionada à janela principal do jogo.
        self.modal_reiniciar = tk.Toplevel(self.janela)
        
        # Define o título da nova janela como "Reiniciar Jogo",
                # para que o jogador saiba que essa janela 
                # oferece a opção de reiniciar.
        self.modal_reiniciar.title("Reiniciar Jogo")
        
        # Define o tamanho da janela modal como 300x200 pixels,
                # tornando-a menor que a janela principal, 
                # suficiente para a mensagem e o botão.
        self.modal_reiniciar.geometry("800x500")
        
        # Usa 'grab_set' para impedir que o jogador interaja com a 
                # janela principal enquanto o modal está aberto.
        # Isso força o jogador a tomar uma ação nesta 
                # janela (reiniciar ou fechar) antes de retornar ao jogo.
        self.modal_reiniciar.grab_set()
    
        # Cria um rótulo (Label) dentro do modal para exibir a 
                # mensagem passada como argumento ao método.
        # O texto será algo como "Você perdeu!" ou "Parabéns! Você afundou todos os navios!".
        # O rótulo usa a fonte Arial com tamanho 14 para
                # garantir que o texto seja legível.
        rotulo_mensagem = tk.Label(self.modal_reiniciar, 
                                   text=mensagem, 
                                   font=("Arial", 14))
        
        # Posiciona o rótulo na janela modal, adicionando 20 pixels 
                # de espaçamento vertical (pady=20) para não ficar 
                # colado nas bordas da janela.
        rotulo_mensagem.pack(pady=20)
    
        # Cria um botão que oferece ao jogador a opção 
                # de reiniciar o jogo.
        # Quando o botão é clicado, ele chama o método 'reiniciar_jogo', 
                # que reinicia o jogo desde o início.
        botao_reiniciar = tk.Button(self.modal_reiniciar, 
                                    text="Reiniciar Jogo", 
                                    command=self.reiniciar_jogo)
        
        # Posiciona o botão "Reiniciar Jogo" logo abaixo da 
                # mensagem, com um espaçamento vertical
                # de 10 pixels (pady=10).
        # Isso garante que o layout fique organizado, com 
                # espaço suficiente entre a mensagem e o botão.
        botao_reiniciar.pack(pady=10)
        

    # Este método é responsável por reiniciar o
            # jogo completamente.
    # Ele fecha as janelas atuais e chama a função 'iniciar_jogo' 
            # para começar uma nova partida do zero.
    def reiniciar_jogo(self):
        
        # Fecha a janela modal (janela de reinício) criada
                # anteriormente, removendo-a da tela.
        # Isso é importante para garantir que o modal não 
                # fique aberto quando o novo jogo começar.
        self.modal_reiniciar.destroy()
        
        # Fecha a janela principal do jogo atual, destruindo a 
                # instância da interface gráfica que representa o jogo.
        # Ao fazer isso, o jogo em andamento é encerrado completamente.
        self.janela.destroy()
        
        # Chama a função 'iniciar_jogo', que é responsável por 
                # iniciar uma nova instância do jogo.
        # Isso cria uma nova janela do jogo e reinicializa 
                # todos os elementos e variáveis para 
                # começar uma nova partida.
        iniciar_jogo()
        

    # O método recebe o 'ship_id', que identifica o navio atingido, e 
            # verifica se todas as partes desse navio foram destruídas.
    # Também verifica se todos os navios do jogo foram afundados, 
            # encerrando o jogo se necessário.
    def verificar_afundou(self, ship_id):
        
        # Inicializa a variável 'navio_afundado' como True, assumindo 
                # inicialmente que o navio foi completamente afundado.
        # Se encontrar qualquer parte do navio ainda intacta, 
                # essa variável será alterada para False.
        navio_afundado = True
    
        # Itera sobre todas as linhas do tabuleiro para procurar
                # se ainda existem partes não atingidas do navio com o 'ship_id'.
        for linha in range(self.TAMANHO_TABULEIRO):
            
            # Para cada linha, também itera sobre todas as colunas
                    # para verificar cada célula.
            for coluna in range(self.TAMANHO_TABULEIRO):
                
                # Verifica se a célula contém o identificador do 
                        # navio ('ship_id'), o que significa que essa 
                        # parte do navio ainda não foi atingida.
                if self.grade_inimigo[linha][coluna] == ship_id:
                    
                    # Se uma parte do navio for encontrada intacta, 
                            # define 'navio_afundado' como False.
                    navio_afundado = False
                    
                    # Sai do loop interno, já que encontrou uma parte
                            # intacta e o navio não está completamente afundado.
                    break
                    
            # Sai também do loop externo se uma parte intacta foi 
                    # encontrada, para evitar verificação desnecessária.
            if not navio_afundado:
                break
    
        # Se, após a verificação, 'navio_afundado' ainda for True, 
                # significa que todas as partes do navio foram atingidas.
        if navio_afundado:
            
            # Exibe uma mensagem ao jogador informando que ele afundou o navio.
            messagebox.showinfo("Navio Afundado!", "Você afundou um navio!")
            
            # Adiciona o 'ship_id' à lista de navios afundados.
                    # Isso é necessário para rastrear os navios já destruídos.
            self.navios_afundados.add(ship_id)
    
        # Após verificar o navio atual, o método verifica se 
                # todos os navios do jogo foram afundados.
        # Isso é feito comparando o número de navios afundados 
                # com o total de navios no jogo.
        if len(self.navios_afundados) == self.total_navios:
            
            # Se o número de navios afundados for igual ao 
                    # total de navios, o jogador venceu.
            # Mostra uma mensagem parabenizando o jogador
                    # por afundar todos os navios.
            messagebox.showinfo("Parabéns!", "Você afundou todos os navios!")
            
            # Desabilita o tabuleiro para impedir que o jogador 
                    # continue clicando após o jogo ter terminado.
            self.desabilitar_tabuleiro()
            
            # Exibe um modal para oferecer ao jogador a opção de reiniciar o jogo.
            self.mostrar_modal_reinicio("Parabéns! Você afundou todos os navios!")


    # Este método desativa todos os botões do tabuleiro, impedindo 
            # que o jogador continue clicando após o fim do jogo.
    def desabilitar_tabuleiro(self):
    
        # Itera sobre cada botão da grade (botoes_celulas é um 
                # dicionário com todas as células do tabuleiro).
        for botao in self.botoes_celulas.values():
            
            # Altera o estado de cada botão para "disabled", o 
                    # que impede que o jogador interaja com eles.
            # Quando um botão está desabilitado, ele não
                    # responde a cliques do usuário.
            botao.configure(state="disabled")

    
    # Este método arranja os navios no tabuleiro de modo aleatório.
    # Ele recebe como parâmetros a 'grade' que é a matriz do 
            # tabuleiro e 'tamanhos_navios' que é uma lista
            # contendo os tamanhos de cada navio a ser posicionado.
    def posicionar_navios_aleatoriamente(self, grade, tamanhos_navios):
        
        
        # Inicializa a variável ship_id com 1, que serve como 
                # identificador único para cada navio.
        # Isso é usado para distinguir diferentes navios na grade.
        # Cada navio no jogo recebe um número único começando por 1, 
                # que ajuda a identificar qual navio foi atingido durante o jogo.
        ship_id = 1  # Identificador único para cada navio
        
        # Itera sobre a lista de tamanhos de navios fornecida. 
        # Cada tamanho na lista representa o número de células
                # que o navio ocupará no tabuleiro.
        # Esta iteração permite posicionar cada navio de acordo 
                # com os tamanhos especificados na lista 'TAMANHO_NAVIOS'.
        for tamanho in tamanhos_navios:
            
            # Chama a função posicionar_navio para tentar 
                    # posicionar um navio na grade.
            # Passa a grade atual, o tamanho do navio a ser 
                    # posicionado e o identificador único do navio.
            # O método 'posicionar_navio' é responsável por 
                    # encontrar uma posição válida na grade onde o navio caiba
                    # sem sobrepor outro navio e considerando a orientação 
                    # desejada (horizontal ou vertical).
            self.posicionar_navio(grade, tamanho, ship_id)
            
            # Após tentar posicionar um navio, incrementa o ship_id 
                    # por 1, garantindo que o próximo navio
                    # tenha um identificador único. 
            # Isso ajuda a rastrear e identificar navios individualmente na grade.
            # Este incremento prepara o identificador para o 
                    # próximo navio a ser posicionado na próxima iteração do loop.
            ship_id += 1  # Incrementa o ship_id para o próximo navio



    # Inicia o método para inserir um navio na matriz que 
                    # representa o tabuleiro do jogo. 
    # A 'grade' refere-se ao tabuleiro onde o navio será 
            # posicionado, 'tamanho' indica quantas 
            # células o navio ocupa, e 'ship_id' é um identificador 
            # único para cada navio, facilitando a verificação 
            # de navios atingidos posteriormente.
    def posicionar_navio(self, grade, tamanho, ship_id):
        
        # 'posicionado' é um controle de fluxo que indica se o 
                # navio foi corretamente inserido na grade.
        # Inicialmente, é definido como False e será usado para 
                # manter o loop até que o navio esteja 
                # corretamente posicionado.
        posicionado = False
    
        # O loop executa enquanto o navio não estiver 
                # corretamente posicionado.
        # Isso assegura que tentativas continuarão até que uma 
                # posição válida seja encontrada, prevenindo 
                # falhas de posicionamento.
        while not posicionado:
            
            # Escolhe uma orientação aleatória para o navio. 
            # A aleatoriedade aqui é crucial para garantir variabilidade no jogo,
                    # fazendo com que cada partida seja única em 
                    # termos de configuração do tabuleiro.
            orientacao = random.choice(['horizontal', 'vertical'])
    
            # Gera uma posição inicial aleatória dentro dos 
                    # limites do tabuleiro.
            # 'linha' e 'coluna' são determinadas aleatoriamente 
                    # pelo tamanho do tabuleiro, considerando que as posições válidas
                    # vão de 0 até 'TAMANHO_TABULEIRO - 1'.
            linha = random.randint(0, self.TAMANHO_TABULEIRO - 1)
            coluna = random.randint(0, self.TAMANHO_TABULEIRO - 1)
    
            # Verifica se o navio pode ser posicionado a partir da 
                    # posição aleatória escolhida com a orientação definida.
            # Esta função considera as dimensões do tabuleiro e verifica 
                    # se o espaço necessário para o navio está livre de outros navios.
            if self.pode_posicionar_navio(grade, linha, coluna, tamanho, orientacao):
                
                # Se o navio puder ser posicionado, inicia-se um loop 
                        # para cada segmento do navio.
                for i in range(tamanho):
                
                    # Dependendo da orientação, o navio será colocado 
                            # horizontalmente ou verticalmente.
                    # Se 'horizontal', o navio é posicionado na mesma 
                            # linha e a coluna é incrementada por 'i'.
                    if orientacao == 'horizontal':
                        grade[linha][coluna + i] = ship_id
                    
                    # Se 'vertical', o navio é posicionado na mesma 
                            # coluna e a linha é incrementada por 'i'.
                    else:
                        grade[linha + i][coluna] = ship_id
                        
                # Depois de posicionado o navio, 'posicionado' é 
                        # configurado como True para encerrar o loop,
                        # indicando que o navio foi colocado com sucesso e 
                        # não são necessárias mais tentativas.
                posicionado = True


    # O método verifica se um navio pode ser posicionado na grade 
            # sem sobrepor outros navios e sem ultrapassar os limites do tabuleiro.
    def pode_posicionar_navio(self, grade, linha, coluna, tamanho, orientacao):
        
        # Se a orientação escolhida para o navio for 'horizontal'.
        if orientacao == 'horizontal':
            
            # Primeiro, verifica se o navio cabe no tabuleiro 
                    # horizontalmente a partir da coluna inicial.
            # Se a posição inicial da coluna mais o tamanho do 
                    # navio exceder o tamanho do tabuleiro, o navio não cabe.
            if coluna + tamanho > self.TAMANHO_TABULEIRO:
                
                # Retorna False indicando que não é possível 
                        # posicionar o navio nesta orientação e posição.
                return False
                
            # Itera sobre cada espaço que o navio ocupará para 
                    # garantir que todas as células estão livres (valor 0).
            for i in range(tamanho):
                
                # Verifica se a célula atual já está ocupada por 
                        # outro navio (diferente de 0).
                if grade[linha][coluna + i] != 0:
                    
                    # Se qualquer célula estiver ocupada, retorna False 
                            # pois o navio não pode ser posicionado aqui.
                    return False
    
        # Se a orientação escolhida para o navio for 'vertical'.
        else:
            
            # Primeiro, verifica se o navio cabe no tabuleiro 
                    # verticalmente a partir da linha inicial.
            # Se a posição inicial da linha mais o tamanho do navio 
                    # exceder o tamanho do tabuleiro, o navio não cabe.
            if linha + tamanho > self.TAMANHO_TABULEIRO:
                
                # Retorna False indicando que não é possível 
                        # posicionar o navio nesta orientação e posição.
                return False
                
            # Itera sobre cada espaço que o navio ocupará para 
                    # garantir que todas as células estão livres (valor 0).
            for i in range(tamanho):
                
                # Verifica se a célula atual já está ocupada por 
                        # outro navio (diferente de 0).
                if grade[linha + i][coluna] != 0:
                    
                    # Se qualquer célula estiver ocupada, retorna False 
                            # pois o navio não pode ser posicionado aqui.
                    return False
    
        # Se passar por todas as verificações sem encontrar problemas, 
                # retorna True indicando que é possível posicionar o navio.
        return True
                       
    


    def mostrar_navios(self):
        
        # Cria uma nova janela (janela secundária) que será 
                # usada para exibir a posição atual dos navios 
                # no tabuleiro do inimigo.
        # Isso é útil para depuração ou para fornecer ao jogador 
                # uma visualização da posição dos navios.
        self.janela_navios = tk.Toplevel(self.janela)
        
        # Define o título da nova janela como "Posição dos Navios", 
                # para que o jogador saiba que está visualizando o 
                # tabuleiro do inimigo.
        self.janela_navios.title("Posição dos Navios")
        
        # Define o tamanho da janela que exibe os navios como 500x500 pixels,
                # ajustando para caber todo o conteúdo do tabuleiro.
        self.janela_navios.geometry("500x500")
        
        # Usa 'grab_set' para impedir que o jogador interaja com a 
                # janela principal até que esta janela seja fechada,
                # garantindo foco exclusivo na visualização dos navios.
        self.janela_navios.grab_set()
    
        # Cria um 'Frame' dentro da janela 'janela_navios', que 
                # serve como um contêiner para organizar os labels (as células).
        frame_navios = tk.Frame(self.janela_navios)
        
        # Posiciona o frame dentro da janela com um espaçamento
                # vertical de 10 pixels (pady=10),
                # para garantir um espaço visual confortável 
                # entre o topo da janela e o frame.
        frame_navios.pack(pady=10)
    
        # Percorre todas as linhas do tabuleiro para 
                # verificar cada célula.
        for linha in range(self.TAMANHO_TABULEIRO):
            
            # Dentro de cada linha, percorre todas as colunas, 
                    # verificando as células uma por uma.
            for coluna in range(self.TAMANHO_TABULEIRO):
                
                # Recupera o valor da célula na grade do inimigo. 
                # Esse valor determina se há um navio ou água.
                celula_valor = self.grade_inimigo[linha][coluna]
                
                # Se o valor for maior que 0, isso indica que há um 
                        # navio não atingido nesta célula.
                if celula_valor > 0:
                    cor = "#0000ff"  # Define a cor da célula como azul para representar um navio não atingido.
                
                # Se o valor for menor que 0, isso indica que a 
                        # célula foi atacada anteriormente.
                elif celula_valor < 0:
                    
                    # Se o valor for -1, isso significa que a célula 
                            # era água e foi atacada.
                    if celula_valor == -1:

                        # Define a cor da célula como branco para 
                                # representar água atingida.
                        cor = "#ffffff"  
                        
                    # Se o valor for outro número negativo, significa
                            # que um navio foi atingido nesta célula.
                    else:

                        # Define a cor da célula como vermelho para 
                                # representar um navio atingido.
                        cor = "#ff0000"  
                
                # Se o valor for 0, isso significa que a célula não
                        # foi revelada ainda (nem navio nem água).
                else:

                    # Define a cor da célula como azul claro para células não reveladas.
                    cor = "#add8e6"  
    
                # Cria um Label (rótulo) para representar visualmente a
                        # célula do tabuleiro na janela.
                # O Label tem dimensões de 2x1 (pequeno quadrado) e usa a 
                        # cor definida acima para representar o estado da célula.
                # O parâmetro 'relief="raised"' dá ao rótulo um 
                        # efeito visual elevado, parecendo um botão.
                lbl = tk.Label(frame_navios, 
                               width=2, 
                               height=1, 
                               bg=cor, 
                               relief="raised")
                
                # Posiciona o Label na grade da janela, organizando-o 
                        # conforme sua posição na matriz 'grade_inimigo'.
                # 'grid' é usado para posicionar o label nas 
                        # coordenadas de linha e coluna corretas.
                lbl.grid(row=linha, column=coluna)
    
        # Cria um botão "Fechar" que permite ao jogador fechar a
                # janela de visualização dos navios.
        # Quando o botão é clicado, ele chama o método 'destroy'
                # da janela, fechando-a.
        botao_fechar = tk.Button(self.janela_navios, 
                                 text="Fechar", 
                                 command=self.janela_navios.destroy)
        
        # Posiciona o botão "Fechar" abaixo da grade, adicionando um 
                # espaçamento vertical (pady=10) para não ficar colado à grade.
        botao_fechar.pack(pady=10)




# Este método é responsável por iniciar o jogo. Ele cria 
        # uma nova janela principal do Tkinter e 
# inicializa uma nova instância da classe 'BatalhaNaval', 
        # que define a lógica e a interface do jogo.
def iniciar_jogo():
    
    # Cria a janela principal do aplicativo, que serve 
            # como a interface principal onde o jogo será exibido.
    # 'tk.Tk()' inicializa uma nova instância da janela do
            # Tkinter. 
    # Esta janela será usada para conter todos os 
            # elementos gráficos do jogo.
    janela_principal = tk.Tk()
    
    # Cria uma nova instância da classe 'BatalhaNaval',
            # passando a janela principal recém-criada
            # como argumento. 
    # Isso inicializa todo o layout e lógica do jogo 
            # dentro da janela.
    # A classe 'BatalhaNaval' contém todo o código 
            # necessário para criar o tabuleiro, definir as regras,
            # e controlar a interação do jogador.
    app = BatalhaNaval(janela_principal)
    
    # Inicia o loop principal da interface gráfica, 
            # que mantém a janela aberta e gerencia
            # todos os eventos (como cliques de botão e 
            # outros tipos de interação).
    # 'mainloop()' faz com que a janela fique em execução 
            # até que o jogador a feche manualmente.
    janela_principal.mainloop()

# Chama a função 'iniciar_jogo' para começar o jogo.
iniciar_jogo()