# Importa o módulo tkinter e renomeia para 'tk' para 
        # facilitar o acesso aos seus componentes
import tkinter as tk

# Importa as classes messagebox e simpledialog do módulo 
        # tkinter para uso em diálogos interativos
from tkinter import messagebox, simpledialog

# Importa o módulo random, que contém funções para 
        # geração de números e escolhas aleatórias
import random

# Importa o módulo string, que contém constantes e 
        # operações comuns para manipulação de strings em Python
import string


# Definição da classe Termo, que encapsula a lógica e a interface do jogo.
class Termo:
    
    # Método construtor da classe, responsável por inicializar a 
            # janela e as propriedades básicas do jogo.
    def __init__(self, janela):
        
        # Atribuição do objeto janela passado como parâmetro 
                # para a propriedade self.janela da classe.
        self.janela = janela
        
        # Configuração do título da janela.
        self.janela.title("Termo")
        
        # Definição do tamanho da janela para 600x600 pixels.
        self.janela.geometry("600x600")
        
        # Configuração da cor de fundo da janela para um cinza escuro.
        self.janela.configure(bg="#3a3a3c")
        
        # Inicialização do nível de dificuldade do jogo como 5, 
                # que pode representar o número de letras das palavras.
        self.dificuldade = 5
        
        # Inicialização da pontuação do jogador, convertendo o valor
                # recuperado pelo método recuperar_pontuacao para inteiro.
        self.pontos = int(self.recuperar_pontuacao())
        
        # Inicialização da variável que armazena a palavra
                # correta como uma string vazia.
        self.palavra_correta = ""
        
        # Inicialização da variável que armazena a tentativa
                # atual do jogador como uma string vazia.
        self.tentativa_atual = ""
        
        # Inicialização da variável que armazena o número da linha atual em
                # que o jogador está inserindo as letras.
        self.linha_atual = 0
        
        # Definição de uma lista de palavras com 5 letras para o
                # jogo, usada na dificuldade inicial.
        self.palavras5 = [
            "TERMO", "CARRO", "MACIO", "FLORA", "TERRA", "LIVRO", "MOUSE",
            "TECLA", "CORES", "PIZZA", "LAPIS", "BOLSA", "TORRE", "MUNDO",
            "LENTO", "FORTE", "MAIOR", "VESTE", "CAMPO", "CRAVO", "VIDRO",
            "SONHO", "TROPA", "BICHO", "HUMOR", "VELHO", "CALOR", "BOMBA",
            "FESTA"
        ]
        
        # Definição de uma lista de palavras com 8 letras, para
                # uma dificuldade intermediária.
        self.palavras8 = [
            "AVENTURA", "BALANCAR", "CACHORRO", "DESAFIOS", "ELEFANTE",
            "GIGANTES", "HARMONIA", "INTERNET", "HISTORIA", "MUSICAIS",
            "NEGOCIOS", "PACIENTE", "PALAVRAS", "MACHISTA", "PENSARES",
            "PODEROSO", "POLICIAL", "PRIMAVERA", "PROFESSOR", "QUADRADO",
            "RECEITAS", "SISTEMAS", "SOLUCOES", "TELEVISAO", "MADRINHA",
            "MANDIOCA"
        ]
        
        # Definição de uma lista de palavras com 12 letras,
                # para a maior dificuldade do jogo.
        self.palavras12 = [
            "APROVADAMENTE", "DOCUMENTARIO", "EXPERIMENTAL", "ALMOXARIFADO",
            "APERFEICOADO", "EMPREENDEDOR", "INDEPENDENTE", "JORNALISTICO",
            "INTERPRETADO", "INVESTIMENTO", "TRANSPORTADO", "ESPECIALISTA",
            "ESTRATEGISTA", "FACILITADORA", "LUMINOSIDADE", "FUNDAMENTAIS",
            "REDUCIONISMO", "REGULAMENTAR", "PROFISSIONAL"
        ]
        
        # Chamada ao método criar_widgets para configurar os
                # componentes visuais da interface.
        self.criar_widgets()
        
        # Chamada ao método escolher_palavra para definir a primeira 
                # palavra correta com base na dificuldade inicial.
        self.escolher_palavra()


    # Definição do método criar_widgets dentro da classe Termo.
    def criar_widgets(self):
        
        # Criação de um rótulo (label) para título do jogo.
        # 'self.lbl_titulo' é uma instância da classe Label de 
                # tkinter configurada para exibir o texto "TERMO".
        # 'font=("Arial", 24)' define a fonte do texto como Arial e tamanho 24.
        # 'bg="#6a6a6d"' configura a cor de fundo do rótulo para um cinza.
        # 'fg="white"' configura a cor do texto para branco.
        self.lbl_titulo = tk.Label(self.janela,
                                   text="TERMO", 
                                   font=("Arial", 24),
                                   bg="#6a6a6d", 
                                   fg="white")
        
        # Método 'pack()' é usado para posicionar o
                # rótulo dentro da janela. 
        # 'pady=5' adiciona um espaçamento vertical de 5 
                # pixels acima e abaixo do rótulo.
        self.lbl_titulo.pack(pady=5)
    
        # Definição de uma string com as instruções do jogo.
        instrucoes = "Descubra a palavra certa em 7 tentativas. Depois de cada tentativa, as peças mostram o quão perto você está da solução."
        
        # Criação de um rótulo para exibir as instruções do
                # jogo na interface gráfica.
        # 'self.lbl_instrucoes' é uma variável que armazena uma
                # instância da classe Label do tkinter.
        # 'text=instrucoes' configura o texto do rótulo para a string 
                # armazenada na variável 'instrucoes'.
        # 'font=("Arial", 10)' define a fonte do texto como Arial e o tamanho da
                # fonte como 10, tornando o texto legível mas não muito grande.
        # 'bg="#6a6a6d"' define a cor de fundo do rótulo para um cinza escuro,
                # seguindo o esquema de cores da interface.
        # 'fg="white"' configura a cor do texto para branco, garantindo um bom 
                # contraste com o fundo escuro para facilitar a leitura.
        # 'wraplength=500' especifica que o texto do rótulo deve ser 
                # quebrado em linhas que não ultrapassem 500 pixels de largura,
                # isso ajuda a evitar que o texto se estenda muito horizontalmente, o
                # que pode dificultar a leitura.
        # 'justify="center"' alinha o texto ao centro do rótulo, tanto 
                # horizontalmente quanto verticalmente, proporcionando um 
                # layout mais estético e organizado.
        self.lbl_instrucoes = tk.Label(self.janela, 
                                       text=instrucoes, 
                                       font=("Arial", 10), 
                                       bg="#6a6a6d", 
                                       fg="white", 
                                       wraplength=500, 
                                       justify="center")

        # Posiciona o rótulo das instruções na janela.
        self.lbl_instrucoes.pack(pady=5)
    
        # Criação de um quadro (frame) para organizar o tabuleiro 
                # do jogo dentro da janela.
        # 'self.frame_tabuleiro' é um container que vai agrupar 
                # elementos visuais (como as casas do jogo).
        # 'bg="#6a6a6d"' define a cor de fundo do quadro como
                # cinza, igual ao dos rótulos.
        self.frame_tabuleiro = tk.Frame(self.janela,
                                        bg="#6a6a6d")
        
        # Posiciona o quadro do tabuleiro na janela, com um 
                # espaçamento vertical de 5 pixels acima e abaixo.
        self.frame_tabuleiro.pack(pady=5)
    
        # Inicialização de uma lista vazia para armazenar as
                # casas do tabuleiro.
        # 'self.casas' vai conter os rótulos que representam 
                # cada casa onde as letras serão inseridas.
        self.casas = []

        # Este loop for externo cria 7 linhas de rótulos, pois o jogo
                # permite até 7 tentativas para adivinhar a palavra.
        for i in range(7):  # 'i' é o índice de cada linha, variando de 0 a 6.
            
            # Cria uma lista vazia chamada 'linha' para armazenar os 
                    # rótulos que representam as letras de cada tentativa.
            linha = []
        
            # Este loop for interno cria rótulos para cada letra da palavra
                    # com base no nível de dificuldade atual.
            # 'j' é o índice para cada coluna na linha 'i', 
                    # variando de acordo com a dificuldade.
            for j in range(self.dificuldade):  
                
                # Criação de um rótulo para representar uma casa do tabuleiro.
                # 'text=""' inicializa o rótulo sem texto.
                # 'font=("Arial", 20, "bold")' define a fonte do texto como Arial,
                        # tamanho 20, em negrito, tornando-o bem visível.
                # 'width=2' e 'height=1' definem as dimensões do rótulo, 
                        # suficientes para uma letra.
                # 'bg="#818384"' define a cor de fundo do rótulo como um cinza claro.
                # 'fg="white"' define a cor do texto para branco.
                # 'bd=2' ajusta a largura da borda do rótulo para 2 pixels.
                # 'relief="raised"' dá ao rótulo um efeito de relevo, o que 
                        # melhora a estética do tabuleiro.
                lbl = tk.Label(self.frame_tabuleiro, 
                               text="", 
                               font=("Arial", 20, "bold"),
                               width=2, 
                               height=1,
                               bg="#818384", 
                               fg="white",
                               bd=2, 
                               relief="raised")
                
                # Posicionamento do rótulo na grade. 'row=i' coloca o
                        # rótulo na linha 'i', e 'column=j' coloca na coluna 'j'.
                # 'padx=2' e 'pady=2' adicionam um pequeno espaçamento
                        # entre os rótulos para evitar que eles fiquem muito juntos.
                lbl.grid(row=i, column=j, padx=2, pady=2)
                
                # Adiciona o rótulo criado à lista 'linha'.
                linha.append(lbl)
        
            # Após preencher a lista 'linha' com os rótulos da 
                    # linha atual, ela é adicionada à lista 'self.casas'.
            # 'self.casas' mantém todas as linhas do tabuleiro, 
                    # permitindo acesso fácil aos rótulos em qualquer parte do jogo.
            self.casas.append(linha)


        # Criação de um quadro (frame) para organizar os botões que 
                # representam as letras do teclado dentro da janela.
        # 'self.frame_teclado' é uma variável que armazena o frame criado.
        # 'bg="#6a6a6d"' define a cor de fundo do frame como 
                # cinza escuro, mantendo consistência com o design da interface.
        self.frame_teclado = tk.Frame(self.janela, bg="#6a6a6d")
        
        # Posicionamento do frame do teclado na janela principal.
        # 'pack()' é um gerenciador de geometria em tkinter que 
                # organiza os widgets em blocos antes de colocá-los na janela.
        # 'pady=5' adiciona um espaçamento vertical de 5 pixels
                # acima e abaixo do frame para separá-lo de 
                # outros elementos da interface.
        self.frame_teclado.pack(pady=5)
        
        # Definição de uma lista de letras que serão usadas 
                # para criar botões de teclado.
        # A lista contém todas as letras do alfabeto latino 
                # usadas na língua inglesa, permitindo ao 
                # jogador inserir suas tentativas.
        letras = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M'
        ]
        
        # Inicialização de um dicionário para armazenar os botões
                # correspondentes a cada letra do alfabeto.
        # 'self.botoes_teclado' vai conter a referência para 
                # cada botão de letra, permitindo manipular
                # os botões durante o jogo (por exemplo, desabilitar um
                # botão quando a letra correspondente já foi usada).
        self.botoes_teclado = {}

        # Iteração sobre a lista de letras, usando a função 
                # enumerate para obter tanto o índice quanto a letra.
        for idx, letra in enumerate(letras):
            
            # Criação de um botão para cada letra na lista 'letras'.
            # 'text=letra' define o texto do botão como a letra da lista.
            # 'width=3' e 'height=1' especificam as dimensões do 
                    # botão, suficientes para exibir uma letra.
            # 'bg="#818384"' define a cor de fundo do botão como cinza claro.
            # 'fg="white"' define a cor do texto para branco, 
                    # garantindo bom contraste.
            # 'font=("Arial", 10, "bold")' define a fonte do texto do 
                    # botão como Arial, tamanho 10, em negrito.
            # 'command=lambda l=letra: self.adicionar_letra(l)' define 
                    # uma função anônima (lambda) como o comando que é executado
                    # quando o botão é pressionado. Essa função chama 'self.adicionar_letra' 
                    # com a letra do botão como argumento.
            btn = tk.Button(self.frame_teclado, 
                            text=letra,
                            width=3, 
                            height=1,
                            bg="#818384", 
                            fg="white",
                            font=("Arial", 10, "bold"),
                            command=lambda l=letra: self.adicionar_letra(l))
            
            # Posicionamento do botão na grade do 'frame_teclado'.
            # 'row=idx // 10' e 'column=idx % 10' calculam a posição 
                    # do botão baseado no índice. Isso distribui os 
                    # botões em até 10 colunas.
            # 'padx=1' e 'pady=1' adicionam um pequeno espaçamento ao 
                    # redor de cada botão para evitar que eles fiquem muito juntos.
            btn.grid(row=idx // 10, column=idx % 10, padx=1, pady=1)
            
            # Armazenamento de cada botão no dicionário 'self.botoes_teclado' 
                    # usando a letra como chave.
            # Isso permite fácil acesso ao botão correspondente a cada 
                    # letra para manipulações futuras, como 
                    # desabilitar o botão após uso.
            self.botoes_teclado[letra] = btn


        # Controles
        # Criação de um quadro (frame) para organizar botões de 
                # controle como "Apagar".
        # 'self.frame_controles' é uma variável que armazena este quadro.
        # 'bg="#6a6a6d"' define a cor de fundo do quadro como um 
                # cinza escuro, consistente com o esquema de cores da interface.
        self.frame_controles = tk.Frame(self.janela, bg="#6a6a6d")
        
        # Posicionamento do quadro de controles na janela principal.
        # 'pack()' é usado para posicionar o frame na janela, e 'pady=5'
                # adiciona um espaçamento vertical de 5 pixels 
                # acima e abaixo do frame.
        self.frame_controles.pack(pady=5)
        
        # Criação de um botão para apagar a última letra inserida.
        # 'text="Apagar"' define o texto exibido no botão.
        # 'width=8' especifica a largura do botão, o que é suficiente 
                # para exibir o texto claramente.
        # 'command=self.apagar_letra' define a função que será chamada 
                # quando o botão for pressionado. Esta função deve
                # remover a última letra da entrada do jogador.
        self.btn_apagar = tk.Button(self.frame_controles, 
                                    text="Apagar",
                                    width=8,
                                    command=self.apagar_letra)
        
        # Posicionamento do botão 'Apagar' na grade do frame de controles.
        # 'row=0' e 'column=0' posicionam o botão na primeira
                # linha e primeira coluna da grade.
        # 'padx=2' adiciona um pequeno espaçamento horizontal de 2 pixels ao
                # redor do botão para evitar que ele fique
                # muito próximo de outros elementos.
        self.btn_apagar.grid(row=0, column=0, padx=2)


        # Criação de um botão 'Enviar' no frame de controles.
        # 'text="Enviar"' define o texto exibido no botão, que é 
                # a ação de enviar a tentativa atual do jogador.
        # 'width=8' especifica a largura do botão para assegurar
                # que o texto caiba adequadamente.
        # 'command=self.validar_tentativa' associa este botão à 
                # função que valida a tentativa do jogador,
        # verificando se as letras correspondem à palavra 
                # correta e fornecendo feedback visual.
        self.btn_enviar = tk.Button(self.frame_controles,
                                    text="Enviar", 
                                    width=8, 
                                    command=self.validar_tentativa)
        
        # Posicionamento do botão 'Enviar' na grade.
        # 'row=0' indica que o botão está na primeira linha do frame.
        # 'column=1' posiciona o botão na segunda coluna, ao 
                # lado do botão 'Apagar'.
        # 'padx=2' adiciona um espaçamento horizontal de 2 pixels
                # para separar este botão do botão 'Apagar'.
        self.btn_enviar.grid(row=0, column=1, padx=2)


        # Criação de um botão 'Ver Palavra' no frame de controles.
        # 'text="Ver Palavra"' define o texto no botão, indicando a 
                # ação de revelar a palavra correta do jogo.
        # 'width=10' assegura que o texto "Ver Palavra" tenha espaço
                # suficiente para ser exibido claramente.
        # 'command=self.ver_palavra' liga este botão à função 
                # que mostra a palavra correta ao jogador,
                # útil para aprender ou quando o jogo termina e o
                # jogador deseja saber a resposta.
        self.btn_ver_palavra = tk.Button(self.frame_controles, 
                                         text="Ver Palavra", 
                                         width=10, 
                                         command=self.ver_palavra)
        
        # Posicionamento do botão 'Ver Palavra' na grade.
        # 'row=0' mantém este botão na mesma linha dos 
                # outros botões de controle.
        # 'column=2' posiciona este botão na terceira coluna,
                # garantindo que esteja ao lado do botão 'Enviar'.
        # 'padx=2' insere um espaçamento horizontal de 2 pixels
                # entre este botão e o botão 'Enviar', mantendo uma 
                # distância adequada para a interface.
        self.btn_ver_palavra.grid(row=0, column=2, padx=2)


        # Criação de um botão 'Dificuldade' no frame de controles.
        # 'text="Dificuldade"' define o texto exibido no botão, 
                # indicando sua função de ajustar o nível de dificuldade do jogo.
        # 'width=10' especifica a largura do botão para assegurar 
                # que o texto 'Dificuldade' caiba adequadamente.
        # 'command=self.aumentar_dificuldade' associa este botão à
                # função que permite ao jogador alterar a dificuldade do jogo.
        # Esta função pode oferecer opções como mudar o número de 
                # letras da palavra ou o número de tentativas permitidas.
        self.btn_dificuldade = tk.Button(self.frame_controles,
                                         text="Dificuldade", 
                                         width=10, 
                                         command=self.aumentar_dificuldade)
        
        # Posicionamento do botão 'Dificuldade' na grade do frame de controles.
        # 'row=0' indica que o botão está na primeira linha do frame.
        # 'column=3' posiciona o botão na quarta coluna, ao 
                # lado do botão 'Ver Palavra'.
        # 'padx=2' adiciona um espaçamento horizontal de 2 pixels 
                # para separar este botão do botão 'Ver Palavra', 
                # mantendo uma organização clara.
        self.btn_dificuldade.grid(row=0, column=3, padx=2)
        
        # Criação de um botão 'Regras' no frame de controles.
        # 'text="Regras"' define o texto no botão, que, ao ser
                # pressionado, exibirá as regras do jogo ao usuário.
        # 'width=8' assegura que o texto 'Regras' tenha espaço 
                # suficiente para ser exibido claramente.
        # 'command=self.mostrar_regras' liga este botão à função 
                # que exibe um resumo das regras do jogo.
        # Isso é útil para novos jogadores ou para relembrar as
                # regras se houver dúvidas durante o jogo.
        self.btn_regras = tk.Button(self.frame_controles, 
                                    text="Regras", 
                                    width=8, 
                                    command=self.mostrar_regras)
        
        # Posicionamento do botão 'Regras' na grade do frame de controles.
        # 'row=0' mantém este botão na mesma linha dos
                # outros botões de controle.
        # 'column=4' posiciona este botão na quinta coluna, 
                # garantindo que esteja ao lado do botão 'Dificuldade'.
        # 'padx=2' insere um espaçamento horizontal de 2 pixels 
                # entre este botão e o botão 'Dificuldade', evitando 
                # que eles fiquem muito próximos.
        self.btn_regras.grid(row=0, column=4, padx=2)


       # Criação de um rótulo para exibir a pontuação atual do jogador.
        # 'self.lbl_pontuacao' é uma instância da classe Label de tkinter.
        # 'text=f"Pontuação: {self.pontos}"' define o texto do 
                # rótulo para exibir a palavra "Pontuação" seguida do 
                # valor atual da pontuação, que é armazenado na
                # variável 'self.pontos'.
        # 'font=("Arial", 14)' define a fonte do texto como Arial e o 
                # tamanho da fonte como 14, tornando-o claro e legível.
        # 'bg="#6a6a6d"' define a cor de fundo do rótulo para cinza escuro, 
                # consistente com o esquema de cores da interface.
        # 'fg="white"' define a cor do texto para branco, garantindo bom
                # contraste com o fundo para facilitar a leitura.
        self.lbl_pontuacao = tk.Label(self.janela, 
                                      text=f"Pontuação: {self.pontos}", 
                                      font=("Arial", 14), 
                                      bg="#6a6a6d", 
                                      fg="white")
        
        # Posicionamento do rótulo de pontuação na janela.
        # 'pack()' é usado para posicionar o rótulo na janela, e 'pady=5'
                # adiciona um espaçamento vertical de 5 pixels acima e 
                # abaixo do rótulo para separá-lo de outros elementos da interface.
        self.lbl_pontuacao.pack(pady=5)
        
        # Configuração dos eventos de teclado na janela principal.
        # 'self.janela.bind("<Key>", self.evento_teclado)' associa todos os
                # eventos de pressionamento de teclas na janela à
                # função 'self.evento_teclado'.
        # Isso significa que qualquer tecla pressionada enquanto a 
                # janela está ativa será capturada pela função 'self.evento_teclado',
                # que pode processar a entrada do teclado de acordo com a lógica do jogo.
        self.janela.bind("<Key>", self.evento_teclado)    


    
    # Definição do método evento_teclado que é chamado sempre que
            # uma tecla é pressionada enquanto a janela do jogo está focada.
    # O parâmetro 'event' contém informações sobre o evento do 
            # teclado, incluindo qual tecla foi pressionada.
    def evento_teclado(self, event):
        
        # Converte o caractere da tecla pressionada para maiúsculas.
        # 'event.char' acessa o caractere associado ao 
                # evento de tecla pressionada.
        # 'upper()' é um método de string que converte letras
                # para suas formas maiúsculas.
        letra = event.char.upper()
    
        # Checa se a letra pressionada é uma letra maiúscula válida e 
                # se está no dicionário de botões do teclado.
        # 'string.ascii_uppercase' é uma constante que contém todas
                # as letras de A a Z em maiúsculas.
        # 'self.botoes_teclado' é um dicionário que contém os botões 
                # correspondentes às letras.
        # Isso impede a adição de caracteres que não são letras (como
                # números ou símbolos) ou letras que não têm botões associados.
        if letra in string.ascii_uppercase and letra in self.botoes_teclado:
            
            # Chama o método 'adicionar_letra' com a letra pressionada 
                    # como argumento para adicioná-la à tentativa atual do jogo.
            self.adicionar_letra(letra)
    
        # Checa se a tecla 'BackSpace' foi pressionada.
        # 'event.keysym' é uma propriedade do evento que fornece o 
                # nome simbólico da tecla pressionada.
        elif event.keysym == "BackSpace":
            
            # Chama o método 'apagar_letra' para remover a última 
                    # letra inserida na tentativa atual do jogo.
            self.apagar_letra()
    
        # Checa se a tecla 'Return' (Enter) foi pressionada.
        elif event.keysym == "Return":
            
            # Chama o método 'validar_tentativa' para verificar se a 
                    # tentativa atual do jogador corresponde à palavra correta.
            self.validar_tentativa()



    # Definição do método mostrar_regras, que exibe as regras do 
            # jogo em uma caixa de diálogo informativa.
    def mostrar_regras(self):
        
        # Define uma string multilinha que detalha as regras do jogo.
        regras = (
            "Descubra a palavra certa em 7 tentativas.\n"
            "Depois de cada tentativa, as peças mostram o quão perto você está da solução:\n\n"
            "Verde: Letra correta na posição correta.\n"
            "Amarelo: Letra correta na posição errada.\n"
            "Cinza: Letra incorreta."
        )
        
        # Exibe as regras em uma janela de mensagem de informação, 
                # usando o título "Regras do Jogo" e o texto definido em 'regras'.
        messagebox.showinfo("Regras do Jogo", regras)


    # Definição do método aumentar_dificuldade, que permite ao 
                # jogador alterar o nível de dificuldade do jogo.
    def aumentar_dificuldade(self):
        
        # Solicita ao jogador para escolher um novo nível de 
                # dificuldade por meio de uma caixa de diálogo.
        # 'simpledialog.askinteger' exibe uma caixa de diálogo que 
                # pede ao usuário para inserir um número inteiro.
        # "Dificuldade" é o título da caixa de diálogo.
        # "Escolha a dificuldade: 8 ou 12 letras" é a mensagem 
                # exibida, orientando o jogador sobre as opções de
                # dificuldade disponíveis.
        nova_dificuldade = simpledialog.askinteger("Dificuldade", "Escolha a dificuldade: 8 ou 12 letras")
        
        # Verifica se a nova dificuldade escolhida está entre as 
                # opções permitidas (8 ou 12 letras).
        if nova_dificuldade in [8, 12]:
            
            # Atualiza a propriedade de dificuldade do jogo para a
                    # nova dificuldade escolhida.
            self.dificuldade = nova_dificuldade
            
            # Chama o método recriar_tabuleiro para ajustar o
                    # tabuleiro de jogo à nova dificuldade.
            # Isso envolve redefinir o layout do tabuleiro para
                    # acomodar o novo número de letras.
            self.recriar_tabuleiro()
            
            # Inicia uma nova palavra para o jogador tentar, adaptando-se ao
                    # novo nível de dificuldade escolhido.
            # Isso garante que a mudança de dificuldade seja aplicada
                    # imediatamente, permitindo ao jogador começar uma
                    # nova rodada com a nova configuração.
            self.proxima_palavra()


    # Definição do método proxima_palavra, responsável por
            # preparar o jogo para uma nova palavra.
    def proxima_palavra(self):
        
        # Reinicialização da linha atual no tabuleiro para 0, indicando
                # que o jogador começará uma nova tentativa na primeira linha.
        self.linha_atual = 0
        
        # Limpeza da variável que armazena a tentativa atual,
                # preparando para uma nova palavra.
        self.tentativa_atual = ""
        
        # Loop sobre cada linha de rótulos no tabuleiro de jogo.
        for linha in self.casas:
            
            # Loop sobre cada rótulo dentro de cada linha.
            for lbl in linha:
                
                # Configura cada rótulo para não ter texto e define a
                        # cor de fundo para o cinza padrão.
                # 'text=""' limpa qualquer letra mostrada anteriormente.
                # 'bg="#818384"' retorna a cor de fundo do rótulo para o 
                        # cinza padrão, removendo quaisquer marcas de 
                        # feedback (verde, amarelo, cinza escuro).
                lbl.configure(text="", bg="#818384")
        
        # Loop sobre cada botão no teclado virtual.
        for btn in self.botoes_teclado.values():
            
            # Redefine a cor de fundo de cada botão para cinza, indicando 
                    # que estão disponíveis para serem pressionados novamente.
            btn.configure(bg="#818384")
        
        # Chamada ao método escolher_palavra para selecionar uma nova 
                # palavra correta do conjunto de palavras disponíveis.
        self.escolher_palavra()
        
        # Atualização do rótulo de pontuação para refletir qualquer
                # mudança nos pontos do jogador.
        # 'text=f"Pontuação: {self.pontos}"' atualiza o texto 
                # mostrando a pontuação atualizada.
        self.lbl_pontuacao.configure(text=f"Pontuação: {self.pontos}")



    # Definição do método recriar_tabuleiro, que reconstrói o
                # tabuleiro de jogo baseado na dificuldade atual.
    def recriar_tabuleiro(self):
        
        # Primeiro passo é limpar o tabuleiro antigo.
        # Itera sobre todos os widgets (elementos gráficos, como rótulos) 
                # que estão dentro do frame do tabuleiro.
        for widget in self.frame_tabuleiro.winfo_children():
            
            # Destroi cada widget. O método 'destroy()' remove efetivamente o
                    # widget da interface, liberando recursos.
            widget.destroy()
    
        # Reinicializa a lista de 'casas', que armazena referências para os
                # rótulos de cada casa no tabuleiro.
        # Isso é necessário para reconstruir a lista desde o início.
        self.casas = []
    
        # Cria um novo tabuleiro com base na dificuldade atual, 
                # ajustando o número de casas.
        # Itera sete vezes, correspondendo ao número de
                # tentativas que o jogador tem.
        # Fixo em 7 tentativas independentemente da dificuldade.
        for i in range(7):  
            
            # Cria uma lista temporária para armazenar os
                    # rótulos da linha atual.
            linha = []
            
            # Itera para cada casa que deve existir na linha,
                    # baseado no valor de 'self.dificuldade'.
            for j in range(self.dificuldade):
                
                # Cria um rótulo que representa uma casa no tabuleiro.
                # 'text=""' inicializa o rótulo sem texto.
                # 'font=("Arial", 20, "bold")' configura a fonte do 
                        # texto dentro do rótulo.
                # 'width=2' e 'height=1' definem as dimensões do rótulo.
                # 'bg="#818384"' define a cor de fundo do rótulo como cinza.
                # 'fg="white"' define a cor do texto para branco.
                # 'bd=2' e 'relief="raised"' configuram a borda do rótulo
                        # para dar um efeito de relevo, melhorando a estética.
                lbl = tk.Label(self.frame_tabuleiro, 
                               text="", 
                               font=("Arial", 20, "bold"), 
                               width=2, 
                               height=1,
                               bg="#818384", 
                               fg="white", 
                               bd=2, 
                               relief="raised")
                
                # Posiciona o rótulo na grade do frame do tabuleiro.
                # 'row=i' define a linha onde o rótulo será colocado.
                # 'column=j' define a coluna.
                # 'padx=2' e 'pady=2' adicionam um pequeno espaçamento ao
                        # redor do rótulo para evitar que eles fiquem muito juntos.
                lbl.grid(row=i, column=j, padx=2, pady=2)
                
                # Adiciona o rótulo à lista 'linha'.
                linha.append(lbl)
            
            # Adiciona a lista 'linha', que contém todos os 
                    # rótulos para uma linha do tabuleiro, à lista 'casas'.
            self.casas.append(linha)
            

    
    # Definição do método ver_palavra, que exibe a palavra correta em
            # um diálogo de mensagem.
    # Este método é chamado quando o jogador deseja ver a resposta
            # correta, geralmente após o término do jogo ou por opção própria.
    def ver_palavra(self):
        
        # Exibe uma caixa de mensagem informativa com a palavra correta.
        # 'messagebox.showinfo' cria um pop-up que mostra uma mensagem ao usuário.
        # "Palavra Correta" é o título da caixa de mensagem.
        # 'f"A palavra correta é: {self.palavra_correta}"' formata a
                # mensagem para incluir a palavra correta.
        messagebox.showinfo("Palavra Correta", f"A palavra correta é: {self.palavra_correta}")


    
    # Definição do método marcar_tecla, que ajusta a cor de
            # fundo de um botão do teclado virtual.
    # Este método é usado para fornecer feedback visual ao
            # jogador sobre a precisão de suas letras na tentativa.
    # Parâmetros:
    # 'letra': A letra do botão a ser marcado.
    # 'cor': A cor de fundo a ser aplicada ao botão, indicando o
            # status da letra na tentativa (correta, presente, ou incorreta).
    def marcar_tecla(self, letra, cor):
        
        # Tenta obter o botão correspondente à letra fornecida a
                # partir do dicionário de botões do teclado.
        btn = self.botoes_teclado.get(letra)
        
        # Verifica se o botão existe no dicionário. Se o botão
                # for encontrado, ele será configurado.
        if btn:
            
            # Configura a cor de fundo do botão para a cor especificada.
            # Isso muda a aparência do botão, refletindo o status
                    # da letra na palavra tentada.
            btn.configure(bg=cor)


        

    # Definição do método validar_tentativa, que verifica se a
            # tentativa atual do jogador corresponde à palavra correta.
    def validar_tentativa(self):
        
        # Verifica se o número de letras na tentativa atual é igual à
                # dificuldade do jogo, o que significa que a tentativa está completa.
        if len(self.tentativa_atual) == self.dificuldade:
            
            # Inicializa um contador para o número de acertos.
            acertos = 0
            
            # Iteração sobre cada letra e seu índice na tentativa atual.
            for idx, letra in enumerate(self.tentativa_atual):
                
                # Acessa o rótulo correspondente no tabuleiro, que
                        # mostra a letra na posição correta.
                lbl = self.casas[self.linha_atual][idx]
                
                # Verifica se a letra na tentativa está na posição 
                        # correta na palavra.
                if letra == self.palavra_correta[idx]:
                    
                    # Configura a cor de fundo do rótulo para verde,
                            # indicando posição correta.
                    lbl.configure(bg="#538d4e")
                    
                    # Chama o método marcar_tecla para ajustar a cor do
                            # botão correspondente a essa letra.
                    self.marcar_tecla(letra, "#538d4e")
                    
                    # Incrementa o contador de acertos.
                    acertos += 1
                    
                # Verifica se a letra está na palavra, mas em 
                        # posição diferente.
                elif letra in self.palavra_correta:
                    
                    # Configura a cor de fundo do rótulo para amarelo,
                            # indicando letra correta em posição errada.
                    lbl.configure(bg="#b59f3b")
                    self.marcar_tecla(letra, "#b59f3b")
                    
                # Caso a letra não esteja na palavra.
                else:
                    
                    # Configura a cor de fundo do rótulo para cinza escuro,
                            # indicando letra incorreta.
                    lbl.configure(bg="#3a3a3c")
                    self.marcar_tecla(letra, "#3a3a3c")
            
            # Verifica se o número de acertos corresponde à dificuldade, o
                    # que significa que todas as letras estão corretas.
            if acertos == self.dificuldade:
                
                # Incrementa a pontuação do jogador.
                self.pontos += 1
                
                # Chama o método salvar_pontuacao para atualizar o
                        # arquivo de pontuação.
                self.salvar_pontuacao()
                
                # Exibe uma mensagem de parabéns ao jogador.
                messagebox.showinfo("Parabéns!", "Você acertou a palavra!")
                
                # Chama o método proxima_palavra para iniciar uma
                        # nova rodada com uma nova palavra.
                self.proxima_palavra()
                
            # Se não acertou todas as letras, prepara para a próxima tentativa.
            else:
                
                # Incrementa o índice da linha atual, movendo para a 
                        # próxima linha do tabuleiro.
                self.linha_atual += 1
                
                # Reinicia a tentativa atual.
                self.tentativa_atual = ""
                
                # Verifica se o jogador alcançou o número máximo de tentativas.
                if self.linha_atual >= 7:
                    
                    # Exibe uma mensagem indicando o fim do jogo e a palavra correta.
                    messagebox.showinfo("Fim de Jogo", f"Você usou todas as tentativas!\nA palavra era: {self.palavra_correta}")
                    
                    # Chama o método tentar_novamente para permitir ao
                            # jogador iniciar um novo jogo.
                    self.tentar_novamente()


    

    # Definição do método apagar_letra, responsável por remover a 
            # última letra inserida na tentativa atual do jogador.
    def apagar_letra(self):
        
        # Verifica se a string 'tentativa_atual' contém alguma letra.
        # 'len(self.tentativa_atual) > 0' assegura que há 
                # pelo menos uma letra para ser apagada.
        if len(self.tentativa_atual) > 0:
            
            # Calcula o índice da última letra na tentativa atual.
            # 'len(self.tentativa_atual) - 1' fornece o índice
                    # da última letra inserida.
            idx = len(self.tentativa_atual) - 1
            
            # Apaga o texto do rótulo correspondente no tabuleiro de jogo.
            # 'self.casas[self.linha_atual][idx]['text'] = ""' limpa o
                    # texto do rótulo que corresponde à última letra inserida.
            # Isso atualiza a interface gráfica, removendo a letra
                    # do display visual no tabuleiro.
            self.casas[self.linha_atual][idx]['text'] = ""
            
            # Remove a última letra da string 'tentativa_atual'.
            # 'self.tentativa_atual = self.tentativa_atual[:-1]' corta 
                    # a última letra da string.
            # '[:-1]' é uma operação de slicing em Python que obtém 
                    # todos os caracteres da string exceto o último.
            self.tentativa_atual = self.tentativa_atual[:-1]


    # Definição do método adicionar_letra, que é responsável por
            # adicionar uma letra à tentativa atual do jogador.
    # O parâmetro 'letra' recebe a letra que o jogador
            # deseja adicionar à sua tentativa.
    def adicionar_letra(self, letra):
        
        # Verifica se o comprimento da tentativa atual é menor que
                # a dificuldade estabelecida.
        # A 'dificuldade' define quantas letras a palavra correta possui e,
                # consequentemente, quantas letras a tentativa pode ter.
        if len(self.tentativa_atual) < self.dificuldade:
            
            # Adiciona a letra passada como parâmetro ao final da
                    # string 'tentativa_atual'.
            # 'tentativa_atual' é uma string que armazena as letras inseridas
                    # pelo jogador até que a tentativa seja completa ou reiniciada.
            self.tentativa_atual += letra
            
            # Calcula o índice da última letra adicionada à 'tentativa_atual'.
            # 'len(self.tentativa_atual) - 1' fornece o índice da última 
                    # posição na string, que é onde a nova letra foi adicionada.
            idx = len(self.tentativa_atual) - 1
            
            # Atualiza o rótulo correspondente no tabuleiro de jogo
                    # para mostrar a letra.
            # 'self.casas[self.linha_atual][idx]['text'] = letra' coloca a
                    # letra no rótulo correspondente da interface gráfica.
            # 'self.casas' é uma matriz de rótulos que representam as
                    # casas do tabuleiro onde as letras são mostradas.
            # 'self.linha_atual' indica a linha atual de tentativas no tabuleiro.
            # '[idx]' acessa a casa específica na linha atual que
                    # corresponde à posição da letra na tentativa.
            self.casas[self.linha_atual][idx]['text'] = letra
            

    # Definição do método escolher_palavra, que seleciona uma nova
            # palavra correta com base no nível de 
            # dificuldade e na pontuação do jogador.
    def escolher_palavra(self):
        
        # Verifica o nível de dificuldade atual para determinar de
                # qual lista de palavras selecionar.
        if self.dificuldade == 5:
        
            # Seleciona a lista de palavras com 5 letras se a dificuldade for 5.
            palavras = self.palavras5
            
        elif self.dificuldade == 8:
            
            # Seleciona a lista de palavras com 8 letras se a dificuldade for 8.
            palavras = self.palavras8
            
        else:
            
            # Por padrão, escolhe a lista de palavras com 12 letras para 
                    # qualquer dificuldade não coberta explicitamente 
                    # pelos casos anteriores.
            palavras = self.palavras12
    
        # Calcula o índice da palavra a ser escolhida com base na
                # pontuação atual do jogador.
        # Utiliza o módulo da pontuação pelo número de palavras na lista
                # selecionada para garantir que o índice seja válido.
        # '(self.pontos - 1) % len(palavras)' ajusta o índice baseando-se 
                # na pontuação ajustada (pontos - 1) para evitar um
                # índice fora do intervalo.
        indice_palavra = (self.pontos - 1) % len(palavras)
        
        # Atribui a palavra escolhida à variável 'self.palavra_correta'.
        self.palavra_correta = palavras[indice_palavra]
        
        # Imprime a palavra escolhida no console para fins de depuração. 
        # Esta linha deve ser removida ou comentada em um ambiente de produção.
        print(f"Debug: Palavra escolhida é {self.palavra_correta}")





    # Definição do método recuperar_pontuacao, que tenta ler a
            # pontuação gravada anteriormente a partir de um arquivo.
    def recuperar_pontuacao(self):
        
        try:
            
            # Tenta abrir o arquivo 'pontuacao_termo.txt' no modo de leitura.
            with open("pontuacao_termo.txt", "r") as f:
                
                # Retorna o conteúdo lido do arquivo, a 
                        # pontuação anteriormente salva.
                return f.read()
                
        # Trata o caso em que o arquivo não é encontrado, o que
                # pode ocorrer na primeira execução do jogo.
        except FileNotFoundError:
            
            # Retorna "0" se o arquivo não existir, indicando
                    # que não há pontuação anterior.
            return "0"




    # Definição do método salvar_pontuacao, que grava a pontuação
                # atual do jogador em um arquivo de texto.
    def salvar_pontuacao(self):
        
        # Abre ou cria um arquivo chamado 'pontuacao_termo.txt' no modo de escrita.
        with open("pontuacao_termo.txt", "w") as f:
            
            # Escreve a pontuação atual, convertida em string, no arquivo.
            f.write(str(self.pontos))


    # Definição do método tentar_novamente, que reinicia o jogo para 
            # permitir que o jogador comece uma nova rodada.
    def tentar_novamente(self):
        
        # Reinicializa a variável que controla a linha atual de entrada para 0, 
                # significando que o jogador começará do início do tabuleiro.
        self.linha_atual = 0
        
        # Limpa a variável que armazena a tentativa atual do jogador, resetando
                # qualquer texto que tenha sido inserido anteriormente.
        self.tentativa_atual = ""
        
        # Itera sobre todas as linhas de rótulos (casas) no tabuleiro do jogo.
        for linha in self.casas:
            
            # Itera sobre cada rótulo (label) dentro de cada linha do tabuleiro.
            for lbl in linha:
                
                # Configura cada rótulo para não mostrar nenhum texto e para
                        # ter a cor de fundo padrão (cinza claro).
                # Isso limpa visualmente o tabuleiro de quaisquer letras ou
                        # cores de fundo que indicavam o estado anterior das tentativas.
                lbl.configure(text="", bg="#818384")
        
        # Itera sobre todos os botões do teclado virtual.
        for btn in self.botoes_teclado.values():
            
            # Configura cada botão para ter a cor de fundo padrão (cinza claro).
            # Isso indica visualmente que todos os botões estão 
                    # disponíveis para serem pressionados novamente.
            btn.configure(bg="#818384")
        
        # Chama o método escolher_palavra para selecionar uma nova 
                # palavra aleatoriamente do conjunto disponível.
        # Isso garante que o jogador tenha uma nova palavra
                # para tentar adivinhar.
        self.escolher_palavra()




# Inicialização do objeto principal Tkinter, que serve
        # como a janela raiz da aplicação.
tela = tk.Tk()

# Criação de uma instância da classe Termo, passando a 
        # janela recém-criada como argumento.
app = Termo(tela)

# Inicia o loop de eventos principal da aplicação.
# Este comando faz a janela aparecer e começa a processar
        # eventos como cliques de mouse e teclas pressionadas.
# O loop continuará executando até que a janela seja
        # fechada, o que encerra o programa.
tela.mainloop()