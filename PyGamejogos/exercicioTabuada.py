# Importa a biblioteca 'tkinter' com o apelido 'tk', que 
        # será usada para construir a interface gráfica do jogo.
import tkinter as tk

# Importa as funções 'randint' do módulo 'random'.
# 'randint' será usada para gerar números aleatórios, como os 
        # fatores de multiplicação nas perguntas do jogo.
from random import randint

# Define a classe JogoTabuada que irá gerenciar o jogo de 
        # tabuada dentro de uma interface gráfica.
class JogoTabuada:
    
    # Método construtor que inicializa uma nova instância da classe JogoTabuada
    def __init__(self, janela):
        
        # 'self.janela' armazena a referência da janela principal 
                # do Tkinter onde o jogo será exibido
        self.janela = janela
        
        # Define o título da janela para "Jogo da Tabuada"
        self.janela.title("Jogo da Tabuada")
        
        # Define as dimensões da janela principal para 800x600 pixels
        self.janela.geometry("800x600")
        
        # Configura a cor de fundo da janela para branco, usando o 
                # código hexadecimal para branco
        # Cor de fundo para um layout mais claro e moderno
        self.janela.configure(bg="#ffffff")  

        # Variáveis de controle do jogo
        # Define a quantidade inicial de vidas do jogador como 3
        self.vidas = 3
        
        # Inicializa a pontuação do jogador como 0
        self.pontos = 0

        # Inicializa o contador de respostas corretas (acertos) como 0
        self.acertos = 0
        
        # Define o tempo restante para responder cada questão como 10 segundos
        self.tempo_restante = 10
        
        # 'self.timer_id' será usado para manter a referência do 
                # temporizador para poder cancelá-lo quando necessário
        self.timer_id = None
        
        # 'self.tabuada' armazenará o número da tabuada que o jogador 
                # escolheu praticar, inicialmente None
        self.tabuada = None
        
        # Define se o modo de jogo será aleatório. False significa 
                # que não é aleatório inicialmente
        self.modo_aleatorio = False
        
        # Lista que armazenará as perguntas da tabuada em 
                # ordem, inicialmente vazia
        self.perguntas_ordenadas = []


        # Frame centralizado para organizar os widgets
        # Cria um frame (quadro) dentro da janela principal para 
                # ajudar na organização dos elementos da interface.
        # O frame serve como um container para outros widgets.
        self.frame_central = tk.Frame(janela, 
                                      bg="#ffffff", 
                                      padx=20, 
                                      pady=20)
        # 'bg="#ffffff"' define a cor de fundo do frame como branco, 
                # garantindo consistência visual com o resto da interface.
        # 'padx=20' e 'pady=20' adicionam um preenchimento (padding) 
                # interno de 20 pixels nas direções x (horizontal) e y (vertical),
                # isto é, espaço extra dentro do frame para separar os 
                # widgets das bordas do frame.
        
        # Empacota o frame na janela usando o gerenciador de layout 'pack', 
                # que organiza os widgets em blocos.
        # 'expand=True' diz ao Tkinter para permitir que o frame expanda 
                # para preencher qualquer espaço extra na janela principal.
        # Isso ajuda a garantir que o frame central ocupe tanto espaço 
                # quanto possível, mantendo todos os widgets internos centralizados.
        self.frame_central.pack(expand=True)
        
        # Interface para escolher o modo de jogo
        # Cria um rótulo (label) dentro do frame central, que serve 
                # como título e instrução para o usuário.
        self.lbl_titulo = tk.Label(self.frame_central, 
                                   text="Escolha o Modo de Jogo", 
                                   font=("Arial", 28, "bold"), 
                                   bg="#ffffff")
        # 'text="Escolha o Modo de Jogo"' define o texto exibido no 
                # rótulo. Este texto instrui o usuário a escolher 
                # como deseja jogar.
        # 'font=("Arial", 28, "bold")' define a fonte do texto no rótulo. 
        # Arial tamanho 28 em negrito é usado para dar destaque e clareza.
        # 'bg="#ffffff"' especifica que a cor de fundo do rótulo deve 
                # ser branca, mantendo a consistência com o esquema de cores do frame.
        
        # Empacota o rótulo dentro do frame central usando o método 'pack', 
                # que também usa o gerenciador de layout 'pack'.
        # 'pady=20' adiciona um preenchimento vertical de 20 pixels 
                # acima e abaixo do rótulo. Isso cria um espaçamento 
                # visual entre o título e outros elementos que podem ser 
                # adicionados abaixo dele, melhorando a estética e a 
                # legibilidade da interface.
        self.lbl_titulo.pack(pady=20)


        # Cria um rótulo (Label) dentro do frame central que serve como 
                # uma instrução adicional para o usuário.
        self.lbl_instrucao = tk.Label(self.frame_central, 
                                      text="Selecione a opção desejada:", 
                                      font=("Arial", 16), 
                                      bg="#ffffff")
        # 'text="Selecione a opção desejada:"' define o texto exibido no rótulo. 
        # Este texto orienta o usuário a fazer uma escolha entre as opções disponíveis.
        # 'font=("Arial", 16)' especifica a fonte do texto, usando Arial 
                # tamanho 16, que é suficientemente grande para ser lido 
                # facilmente sem dominar o layout.
        # 'bg="#ffffff"' configura a cor de fundo do rótulo como branco, 
                # mantendo a uniformidade visual com o resto da interface.
        
        # Empacota o rótulo no frame central usando o gerenciador de layout 'pack'.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
                # abaixo do rótulo, ajudando a separá-lo de outros elementos na 
                # interface e melhorando a estética geral.
        self.lbl_instrucao.pack(pady=10)
        
        # Cria um botão dentro do frame central. Este botão é usado para 
                # iniciar o jogo no modo aleatório.
        self.btn_aleatorio = tk.Button(self.frame_central, 
                                       text="Treinar Tabuada de 1 a 10 (Aleatório)", 
                                       font=("Arial", 16), 
                                       command=self.iniciar_modo_aleatorio, 
                                       bg="#4CAF50", 
                                       fg="white", 
                                       padx=10, 
                                       pady=5)
        # 'text="Treinar Tabuada de 1 a 10 (Aleatório)"' define o texto 
                # do botão, que explica claramente sua função: iniciar o 
                # treinamento de tabuada em ordem aleatória.
        # 'font=("Arial", 16)' define a fonte e o tamanho do texto no 
                # botão, escolhido para ser claro e legível.
        # 'command=self.iniciar_modo_aleatorio' vincula o botão à função 
                # iniciar_modo_aleatorio(), que será chamada quando o botão 
                # for clicado, iniciando o jogo no modo aleatório.
        # 'bg="#4CAF50"' define a cor de fundo do botão como um verde 
                # vibrante, e 'fg="white"' define a cor do texto para branco, 
                # criando um alto contraste para fácil leitura.
        # 'padx=10' e 'pady=5' adicionam preenchimento interno horizontal e 
                # vertical ao botão, respectivamente, fazendo com que seja 
                # mais fácil de clicar e visualmente atraente.
        
        # Empacota o botão no frame central usando o método 'pack'.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
                # abaixo do botão, garantindo que não fique visualmente 
                # comprimido contra outros elementos.
        self.btn_aleatorio.pack(pady=10)


        # Cria um rótulo (Label) dentro do frame central que serve como 
                # uma opção alternativa para o usuário.
        self.lbl_tabuada_especifica = tk.Label(self.frame_central, 
                                               text="Ou digite o número da tabuada que deseja treinar:", 
                                               font=("Arial", 16), 
                                               bg="#ffffff")
        # 'text="Ou digite o número da tabuada que deseja treinar:"' 
                # informa ao usuário que ele pode escolher uma tabuada 
                # específica para praticar.
        # 'font=("Arial", 16)' define a fonte do texto, escolhendo 
                # Arial tamanho 16, que é claro e legível, mantendo a 
                # consistência com o estilo de fonte do restante da interface.
        # 'bg="#ffffff"' configura a cor de fundo do rótulo como branco, o 
                # que ajuda a manter o design limpo e moderno da interface.
        
        # Empacota o rótulo no frame central usando o método 'pack'.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
                # abaixo do rótulo, o que ajuda a separar visualmente este 
                # rótulo dos outros componentes e melhora a legibilidade.
        self.lbl_tabuada_especifica.pack(pady=10)
        
        # Cria um campo de entrada (Entry) para que o usuário possa 
                # digitar o número da tabuada que deseja praticar.
        self.entrada_tabuada = tk.Entry(self.frame_central, 
                                        font=("Arial", 16), 
                                        width=5)
        # 'font=("Arial", 16)' especifica a fonte e tamanho do texto 
                # dentro do campo de entrada, tornando-o fácil de ler e usar.
        # 'width=5' define a largura do campo de entrada, suficiente para 
                # inserir um ou dois dígitos, o que é adequado para a 
                # inserção de números de tabuada.
        
        # Empacota o campo de entrada no frame central usando o método 'pack'.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
                # abaixo do campo de entrada. 
        # Isso cria espaço suficiente para evitar que o campo de entrada 
                # pareça muito apertado e melhora a interação do usuário.
        self.entrada_tabuada.pack(pady=10)


        # Cria um botão dentro do frame central que permite ao usuário 
                # iniciar o treinamento da tabuada escolhida.
        self.btn_iniciar = tk.Button(self.frame_central, 
                                     text="Iniciar Treinamento", 
                                     font=("Arial", 16), 
                                     command=self.iniciar_modo_especifico, 
                                     bg="#2196F3", 
                                     fg="white", 
                                     padx=10, 
                                     pady=5)
        # 'text="Iniciar Treinamento"' define o texto que aparece no 
                # botão, indicando claramente sua função.
        # 'font=("Arial", 16)' especifica a fonte e o tamanho do texto 
                # no botão, escolhido para ser claro e legível.
        # 'command=self.iniciar_modo_especifico' associa o botão à função 
                # iniciar_modo_especifico(), que é chamada quando o botão é clicado.
        # 'bg="#2196F3"' define a cor de fundo do botão como um azul 
                # forte, e 'fg="white"' define a cor do texto para branco, 
                # criando um alto contraste para fácil leitura.
        # 'padx=10' e 'pady=5' adicionam preenchimento interno horizontal e 
                # vertical ao botão, respectivamente, fazendo com que seja 
                # mais fácil de clicar e visualmente atraente.
        
        # Empacota o botão no frame central usando o método 'pack'.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
                # abaixo do botão, garantindo que não fique visualmente 
                # comprimido contra outros elementos.
        self.btn_iniciar.pack(pady=10)
        
        # Interface do jogo (inicialmente escondida)
        # Cria um rótulo (Label) dentro do frame central que será 
                # usado para mostrar as questões de tabuada.
        self.lbl_questao = tk.Label(self.frame_central, 
                                    text="", 
                                    font=("Arial", 26, "bold"), 
                                    bg="#ffffff")
        # 'text=""' inicialmente não possui texto, pois as questões 
                # serão definidas durante o jogo.
        # 'font=("Arial", 26, "bold")' define a fonte do texto no rótulo, 
                # usando Arial tamanho 26 em negrito para destacar as 
                # questões e torná-las facilmente legíveis.
        # 'bg="#ffffff"' mantém a cor de fundo do rótulo como branca, 
                # consistente com o resto da interface.
        
        # Empacota o rótulo na interface, mas inicialmente o esconde.
        # 'pack(pady=20)' organiza o rótulo com um espaçamento vertical 
                # de 20 pixels, proporcionando um bom espaço visual em 
                # torno das questões.
        self.lbl_questao.pack(pady=20)

        # 'pack_forget()' é usado para esconder inicialmente o rótulo. 
        # Isso permite que a interface de jogo seja exibida apenas 
                # quando o usuário opta por começar a jogar.
        self.lbl_questao.pack_forget()


        # Cria um campo de entrada (Entry) dentro do frame central 
                # onde o usuário pode digitar sua resposta à questão de tabuada.
        self.entrada_resposta = tk.Entry(self.frame_central, 
                                         font=("Arial", 22), 
                                         width=10)
        # 'font=("Arial", 22)' define a fonte do texto que o usuário 
                # digita, escolhendo Arial tamanho 22, que é grande e facilmente legível.
        # 'width=10' especifica a largura do campo de entrada, permitindo ao 
                # usuário digitar respostas de até 10 caracteres.
        # Esse tamanho é suficiente para números e evita que o campo 
                # fique muito pequeno ou muito grande na tela.
        
        # Empacota o campo de entrada na interface gráfica, organizando-o 
                # dentro do frame central.
        # 'pady=20' adiciona um espaçamento vertical de 20 pixels acima e 
                # abaixo do campo de entrada, criando uma separação 
                # visual com outros elementos.
        self.entrada_resposta.pack(pady=20)
        
        # Vincula o evento de pressionar a tecla "Enter" à função 
                # `verificar_resposta`.
        # 'bind("<Return>", self.verificar_resposta)' associa a 
                # tecla Enter com a função de verificar a resposta.
        # Isso permite que o usuário submeta sua resposta pressionando Enter, 
                # sem a necessidade de clicar em um botão.
        self.entrada_resposta.bind("<Return>", 
                                   self.verificar_resposta)
        
        # Inicialmente, esconde o campo de entrada da interface 
                # usando o método 'pack_forget'.
        # 'pack_forget()' remove o campo de entrada da visualização 
                # até que o jogo comece.
        # Isso ajuda a manter a interface limpa até que o jogador 
                # realmente precise interagir com o campo.
        self.entrada_resposta.pack_forget()


        # Cria um rótulo (Label) que exibe a pontuação atual do jogador.
        self.lbl_pontos = tk.Label(self.frame_central,
                                   text="Pontos: 0", 
                                   font=("Arial", 18), 
                                   bg="#ffffff")
        # 'text="Pontos: 0"' define o texto inicial do rótulo, 
                # indicando que o jogador começa com 0 pontos.
        # Conforme o jogo avança, este rótulo será atualizado para 
                # refletir a pontuação acumulada.
        # 'font=("Arial", 18)' especifica a fonte do texto, escolhendo 
                # Arial tamanho 18 para manter a clareza, mas sem dominar o layout.
        # 'bg="#ffffff"' configura a cor de fundo do rótulo como branco, 
                # mantendo a estética visual consistente com o restante da interface.
        
        # Empacota o rótulo de pontuação na interface, organizando-o 
                # dentro do frame central.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels 
                # acima e abaixo do rótulo, criando uma separação 
                # adequada entre o rótulo de pontuação e outros elementos.
        self.lbl_pontos.pack(pady=10)
        
        # Inicialmente, esconde o rótulo de pontuação da interface 
                # usando o método 'pack_forget'.
        # 'pack_forget()' remove o rótulo de pontuação da visualização até 
                # que o jogo comece, evitando a exibição desnecessária de 
                # informações enquanto o jogador ainda não iniciou a jogada.
        self.lbl_pontos.pack_forget()


        # Cria um rótulo (Label) que exibe a quantidade de acertos do jogador.
        self.lbl_acertos = tk.Label(self.frame_central, 
                                    text="Acertos: 0", 
                                    font=("Arial", 18), 
                                    bg="#ffffff")
        # 'text="Acertos: 0"' define o texto inicial do rótulo, 
                # indicando que o jogador começa o jogo com 0 acertos.
        # Conforme o jogador responde corretamente às questões, o 
                # número de acertos será atualizado e exibido aqui.
        # 'font=("Arial", 18)' define a fonte do texto no rótulo, usando 
                # Arial tamanho 18, que é claro e legível sem ocupar muito espaço.
        # 'bg="#ffffff"' configura a cor de fundo do rótulo como branco, 
                # mantendo a consistência visual com o layout do jogo.
        
        # Empacota o rótulo de acertos na interface, organizando-o 
                # dentro do frame central.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
                # abaixo do rótulo, criando uma separação visual confortável 
                # com outros elementos da interface.
        self.lbl_acertos.pack(pady=10)
        
        # Inicialmente, esconde o rótulo de acertos da interface 
                # usando o método 'pack_forget'.
        # 'pack_forget()' remove o rótulo de acertos da visualização até 
                # que o jogo comece, já que os acertos só são relevantes 
                # durante o jogo.
        self.lbl_acertos.pack_forget()


        # Cria um rótulo (Label) que exibe o número de vidas restantes do jogador.
        self.lbl_vidas = tk.Label(self.frame_central, 
                                  text="Vidas: 3", 
                                  font=("Arial", 18), 
                                  fg="red", 
                                  bg="#ffffff")
        # 'text="Vidas: 3"' define o texto inicial do rótulo, 
                # indicando que o jogador começa com 3 vidas.
        # Este rótulo será atualizado toda vez que o jogador perder 
                # uma vida ao errar uma resposta.
        # 'font=("Arial", 18)' define a fonte do texto como Arial tamanho 18, 
                # proporcionando uma leitura fácil e clara.
        # 'fg="red"' configura a cor do texto como vermelho, destacando o 
                # número de vidas em uma cor associada a alertas e perda, 
                # chamando a atenção do jogador para essa informação.
        # 'bg="#ffffff"' configura a cor de fundo do rótulo como branco, 
                # mantendo a uniformidade visual com o resto da interface.
        
        # Empacota o rótulo de vidas na interface, organizando-o 
                # dentro do frame central.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
                # abaixo do rótulo, proporcionando uma separação adequada 
                # com outros elementos da interface.
        self.lbl_vidas.pack(pady=10)
        
        # Inicialmente, esconde o rótulo de vidas da interface 
                # usando o método 'pack_forget'.
        # 'pack_forget()' remove o rótulo de vidas da visualização até 
                # que o jogo comece, já que o número de vidas só 
                # será relevante durante o jogo.
        self.lbl_vidas.pack_forget()


        # Cria um rótulo (Label) que exibe o tempo restante para o 
                # jogador responder à questão.
        self.lbl_tempo = tk.Label(self.frame_central, 
                                  text="Tempo: 10", 
                                  font=("Arial", 18), 
                                  fg="blue", 
                                  bg="#ffffff")
        # 'text="Tempo: 10"' define o texto inicial do rótulo, indicando 
                # que o jogador tem 10 segundos para responder à questão.
        # Esse valor será atualizado durante o jogo conforme o tempo vai diminuindo.
        # 'font=("Arial", 18)' define a fonte do texto como Arial tamanho 18, 
                # garantindo que o jogador veja facilmente o tempo restante.
        # 'fg="blue"' define a cor do texto como azul, que é uma cor neutra e 
                # calmante, ideal para exibir contagens de tempo, em contraste 
                # com o vermelho de alerta usado para as vidas.
        # 'bg="#ffffff"' define a cor de fundo como branco, mantendo o 
                # layout da interface consistente com os outros elementos.
        
        # Empacota o rótulo de tempo na interface, organizando-o dentro do frame central.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
                # abaixo do rótulo, criando uma separação confortável entre o 
                # tempo e outros elementos, como a pergunta ou o campo de resposta.
        self.lbl_tempo.pack(pady=10)
        
        # Inicialmente, esconde o rótulo de tempo da interface usando o 
                # método 'pack_forget'.
        # 'pack_forget()' remove o rótulo de tempo da visualização até que o 
                # jogo comece, já que o tempo só é relevante quando o 
                # jogador está respondendo a perguntas.
        self.lbl_tempo.pack_forget()


        # Cria um botão que permite ao jogador enviar sua resposta 
                # para a questão atual.
        self.btn_enviar = tk.Button(self.frame_central, 
                                    text="Responder", 
                                    font=("Arial", 16), 
                                    command=self.verificar_resposta, 
                                    bg="#f57c00", 
                                    fg="white", 
                                    padx=10, 
                                    pady=5)
        # 'text="Responder"' define o texto que aparece no botão, 
                # indicando claramente a ação que o jogador deve tomar ao 
                # terminar de digitar a resposta.
        # 'font=("Arial", 16)' especifica a fonte e o tamanho do texto 
                # no botão, garantindo que seja legível e atraente.
        # 'command=self.verificar_resposta' vincula o botão à função `verificar_resposta`. 
                # Quando o botão é clicado, essa função é chamada para verificar 
                # se a resposta do jogador está correta.
        # 'bg="#f57c00"' define a cor de fundo do botão como laranja, uma cor 
                # que chama a atenção e incentiva o jogador a interagir com o botão.
        # 'fg="white"' define a cor do texto do botão como branco, criando um 
                # contraste claro com o fundo laranja, tornando o texto fácil de ler.
        # 'padx=10' e 'pady=5' adicionam um preenchimento interno horizontal e 
                # vertical ao botão, fazendo com que ele seja maior e mais 
                # fácil de clicar, além de visualmente atraente.
        
        # Empacota o botão de enviar resposta na interface, organizando-o 
                # dentro do frame central.
        # 'pady=20' adiciona um espaçamento vertical de 20 pixels acima e 
                # abaixo do botão, criando uma separação visual clara 
                # entre o botão e os outros elementos.
        self.btn_enviar.pack(pady=20)
        
        # Inicialmente, esconde o botão de enviar resposta da interface 
                # usando o método 'pack_forget'.
        # 'pack_forget()' remove o botão da visualização até que o jogo comece, 
                # uma vez que o botão só é necessário quando o jogador 
                # está pronto para enviar suas respostas.
        self.btn_enviar.pack_forget()


    def iniciar_modo_aleatorio(self):
        
        """Inicia o modo aleatório com tabuadas de 1 a 10."""
        
        # Define a variável de controle 'modo_aleatorio' como True.
        # Isso sinaliza ao jogo que o modo de jogo será aleatório, ou 
                # seja, as perguntas serão geradas aleatoriamente
                # com base nas tabuadas de 1 a 10, em vez de seguir uma sequência fixa.
        self.modo_aleatorio = True
        
        # Chama a função 'mostrar_jogo', que exibe a interface do jogo e 
                # esconde as opções de escolha de modo.
        # A função 'mostrar_jogo' ajusta a interface visual para ocultar 
                # as instruções iniciais e exibir
                # os elementos de jogo como a questão, o campo de resposta e os 
                # rótulos de pontuação, acertos, tempo e vidas.
        self.mostrar_jogo()
        
        # Chama a função 'nova_pergunta' para gerar e exibir uma nova questão.
        # No modo aleatório, essa função irá gerar dois números aleatórios e 
                # uma operação de multiplicação para o jogador resolver.
        # O tempo e o restante da lógica de jogo também são configurados 
                # dentro dessa função.
        self.nova_pergunta()


    def mostrar_jogo(self):
        
        """Mostra a interface do jogo e esconde as opções de seleção."""
        
        # Oculta o rótulo de título que estava exibindo a instrução 
                # de seleção do modo de jogo.
        # 'pack_forget()' remove o widget do layout atual, tornando-o 
                # invisível na interface.
        self.lbl_titulo.pack_forget()
        
        # Oculta o rótulo de instrução que orientava o jogador a 
                # escolher um modo de jogo.
        self.lbl_instrucao.pack_forget()
        
        # Oculta o campo de entrada onde o jogador pode digitar o 
                # número da tabuada que deseja treinar.
        self.entrada_tabuada.pack_forget()
        
        # Oculta o botão de iniciar o treino com uma tabuada específica.
        self.btn_iniciar.pack_forget()
        
        # Oculta o botão de iniciar o modo de treino aleatório, que 
                # permite treinar tabuadas de 1 a 10 de forma aleatória.
        self.btn_aleatorio.pack_forget()
        
        # Oculta o rótulo que solicita ao jogador para digitar o 
                # número da tabuada desejada.
        self.lbl_tabuada_especifica.pack_forget()
    
        # Exibe o rótulo da questão matemática (ex: "5 * 3"), que 
                # estava oculto durante a seleção do modo de jogo.
        # 'pack(pady=20)' adiciona um espaçamento vertical de 20 pixels ao 
                # redor do rótulo, criando uma separação visual.
        self.lbl_questao.pack(pady=20)
        
        # Exibe o campo de entrada onde o jogador digitará a resposta 
                # para a pergunta exibida no rótulo 'lbl_questao'.
        self.entrada_resposta.pack(pady=20)
        
        # Exibe o rótulo que mostra a pontuação atual do jogador, 
                # inicialmente começando com 0 pontos.
        self.lbl_pontos.pack(pady=10)
        
        # Exibe o rótulo que conta o número de acertos que o jogador 
                # teve até o momento, começando com 0.
        self.lbl_acertos.pack(pady=10)
        
        # Exibe o rótulo que indica o número de vidas restantes do 
                # jogador, começando com 3.
        self.lbl_vidas.pack(pady=10)
        
        # Exibe o rótulo que indica o tempo restante para responder à 
                # pergunta, começando com 10 segundos.
        self.lbl_tempo.pack(pady=10)
        
        # Exibe o botão que permite ao jogador enviar a resposta digitada 
                # no campo 'entrada_resposta'.
        # O botão também terá um espaçamento vertical de 20 pixels ao redor, 
                # criando uma separação visual confortável.
        self.btn_enviar.pack(pady=20)

    
    def nova_pergunta(self):
        
        """Gera uma nova questão, aleatória ou ordenada."""
        
        # Se já houver um temporizador ativo, ele é cancelado. 
        # Isso garante que, ao gerar uma nova pergunta, o temporizador 
                # anterior não continue rodando, evitando conflitos.
        if self.timer_id:
            self.janela.after_cancel(self.timer_id)
    
        # Verifica se o jogo está no modo aleatório (quando 'self.modo_aleatorio' é True).
        # Nesse caso, os números para a pergunta de multiplicação 
                # serão escolhidos de forma aleatória.
        if self.modo_aleatorio:
            
            # Gera dois números aleatórios entre 1 e 10 para a 
                    # questão de multiplicação.
            # Esses números representam o multiplicando e o 
                    # multiplicador da pergunta.
            num1 = randint(1, 10)
            num2 = randint(1, 10)
        
        # Caso o modo não seja aleatório, significa que o jogador está 
                # praticando uma tabuada específica.
        else:
            
            # Verifica se ainda existem perguntas na lista 'self.perguntas_ordenadas' (a 
                    # sequência de perguntas da tabuada).
            if not self.perguntas_ordenadas:
                
                # Se a lista estiver vazia (ou seja, o jogador completou a sequência 
                        # da tabuada), o jogo termina automaticamente.
                self.game_over(fim_automatico=True)
                return
            
            # Remove e retorna a próxima pergunta da lista 'self.perguntas_ordenadas'.
            # A lista contém tuplas da forma (num1, num2), representando 
                    # os números da tabuada em ordem.
            num1, num2 = self.perguntas_ordenadas.pop(0)
    
        # Formata a pergunta como uma string no formato "num1 * num2" e a 
                # armazena em 'self.questao'.
        # Isso é a pergunta que será exibida para o jogador responder.
        self.questao = f"{num1} * {num2}"
    
        # Calcula a resposta correta da pergunta (multiplicação de 'num1' 
                # por 'num2') e armazena o valor em 'self.resposta_correta'.
        # Esse valor será usado para verificar se a resposta do 
                # jogador está correta.
        self.resposta_correta = num1 * num2
    
        # Atualiza o rótulo 'lbl_questao' na interface gráfica para 
                # exibir a nova questão gerada.
        # O rótulo agora mostra a multiplicação atual que o 
                # jogador precisa resolver.
        self.lbl_questao.config(text=self.questao)
    
        # Reinicia o tempo restante para responder a pergunta, 
                # configurando-o para 10 segundos.
        # 'self.tempo_restante' é a variável que controla o 
                # tempo disponível para responder.
        self.tempo_restante = 10
    
        # Atualiza o rótulo que exibe o tempo restante, mostrando que o 
                # jogador tem 10 segundos para responder à nova pergunta.
        # Isso dá um feedback visual ao jogador sobre o tempo que ele tem disponível.
        self.lbl_tempo.config(text=f"Tempo: {self.tempo_restante}")
    
        # Chama a função 'contar_tempo' para iniciar a contagem regressiva do tempo.
        # O temporizador será acionado para diminuir o tempo a cada 
                # segundo até que o jogador responda ou o tempo acabe.
        self.contar_tempo()



    def contar_tempo(self):
        
        """Conta o tempo de 10 segundos para cada pergunta."""
        
        # Verifica se ainda há tempo restante.
        if self.tempo_restante > 0:
            
            # Reduz o tempo restante em 1 segundo. A cada chamada 
                    # desta função, o tempo é decrementado.
            self.tempo_restante -= 1
            
            # Atualiza o rótulo que exibe o tempo na interface gráfica. 
            # O novo valor do tempo restante é exibido para o jogador.
            self.lbl_tempo.config(text=f"Tempo: {self.tempo_restante}")
            
            # Reagenda a função 'contar_tempo' para ser chamada novamente 
                    # em 1000 milissegundos (1 segundo).
            # Isso cria um ciclo de contagem regressiva, onde a função será 
                    # chamada repetidamente até que o tempo chegue a 0.
            self.timer_id = self.janela.after(1000, self.contar_tempo)
        
        # Caso o tempo tenha acabado (self.tempo_restante == 0):
        else:
            
            # Chama a função 'perdeu_vida' para processar a perda de 
                    # uma vida, já que o jogador não respondeu a tempo.
            # Isso reduz o número de vidas e, se o jogador perder todas 
                    # as vidas, o jogo será encerrado.
            self.perdeu_vida()



    def perdeu_vida(self):
        
        """Reduz uma vida e verifica se o jogo deve acabar."""
        
        # Diminui o número de vidas do jogador em 1.
        self.vidas -= 1
    
        # Atualiza o rótulo na interface gráfica que exibe o 
                # número de vidas restantes.
        # Usa f-string para mostrar o novo valor de vidas.
        self.lbl_vidas.config(text=f"Vidas: {self.vidas}")
    
        # Verifica se o jogador perdeu todas as vidas (ou seja, se o 
                # número de vidas chegou a zero).
        if self.vidas == 0:
            
            # Se o número de vidas for zero, o jogo acaba, chamando o 
                    # método 'game_over' que lida com o encerramento.
            self.game_over()
        
        else:
            
            # Se o jogador ainda tiver vidas, uma nova pergunta é 
                    # gerada para continuar o jogo.
            # Isso permite que o jogo prossiga normalmente até que 
                    # todas as vidas sejam perdidas.
            self.nova_pergunta()


    def game_over(self, fim_automatico=False):
        
        """Exibe a mensagem de fim de jogo."""
        
        # Verifica se o jogo terminou automaticamente (completou todas 
                # as perguntas de uma tabuada específica)
        if fim_automatico:
            
            # Se o jogo terminar por completar uma tabuada (fim_automatico=True), 
                    # exibe uma mensagem de parabéns.
            self.lbl_questao.config(text=f"Parabéns! Você completou a tabuada.\nPontuação final: {self.pontos}. Acertos: {self.acertos}")
            
        else:
            
            # Se o jogo terminar por perda de todas as vidas, 
                    # exibe uma mensagem de fim de jogo.
            self.lbl_questao.config(text=f"Fim de jogo! Pontuação final: {self.pontos}. Acertos: {self.acertos}")
        
        # Desativa o campo de entrada onde o jogador insere suas respostas, 
                # para impedir interações após o fim do jogo.
        self.entrada_resposta.config(state=tk.DISABLED)
        
        # Desativa o botão de "Responder" para impedir mais 
                # respostas após o fim do jogo.
        self.btn_enviar.config(state=tk.DISABLED)
        
        # Verifica se o temporizador (timer) ainda está ativo.
        if self.timer_id:
            
            # Se houver um temporizador ativo, cancela o temporizador 
                    # para interromper a contagem regressiva.
            self.janela.after_cancel(self.timer_id)

    

    def verificar_resposta(self, event=None):
        
        """Verifica a resposta inserida pelo usuário."""
        
        try:
            # Obtém o valor inserido no campo de entrada (onde o jogador 
                    # digita a resposta) e tenta convertê-lo para inteiro.
            # O método 'get()' captura o valor como string e 'int()' 
                    # tenta converter para número.
            resposta_usuario = int(self.entrada_resposta.get())
    
            # Verifica se a resposta inserida pelo jogador é igual à 
                    # resposta correta da pergunta.
            if resposta_usuario == self.resposta_correta:
                
                # Se a resposta for correta:
                # Incrementa a pontuação em 10 pontos.
                self.pontos += 10
    
                # Incrementa o contador de acertos.
                self.acertos += 1
    
                # Atualiza o rótulo que exibe a pontuação na interface 
                        # gráfica, para mostrar os novos pontos.
                self.lbl_pontos.config(text=f"Pontos: {self.pontos}")
    
                # Atualiza o rótulo que exibe o número de acertos.
                self.lbl_acertos.config(text=f"Acertos: {self.acertos}")
    
                # Limpa o campo de entrada para que o jogador possa inserir 
                        # uma nova resposta na próxima pergunta.
                self.entrada_resposta.delete(0, tk.END)
    
                # Gera uma nova pergunta para continuar o jogo, já que a 
                        # resposta estava correta.
                self.nova_pergunta()
    
            else:
                
                # Se a resposta estiver incorreta:
                # No caso de o jogador estar no modo de tabuada específica (não 
                        # aleatório), a pergunta atual é repetida.
                # Isso é feito inserindo a pergunta errada de volta no 
                        # início da lista 'perguntas_ordenadas'.
                if not self.modo_aleatorio:
                    
                    # Divide a pergunta ('self.questao') no formato "num1 * num2" 
                            # em dois números inteiros.
                    num1, num2 = int(self.questao.split(' * ')[0]), int(self.questao.split(' * ')[1])
                    
                    # Reinsere a pergunta incorreta (num1, num2) no início da 
                            # lista para ser repetida na próxima rodada.
                    self.perguntas_ordenadas.insert(0, (num1, num2))
    
                # Chama o método 'perdeu_vida' para processar a perda de uma 
                        # vida, já que o jogador errou a resposta.
                self.perdeu_vida()
    
        except ValueError:
            
            # Se houver um erro ao tentar converter a entrada para um 
                    # número (por exemplo, se o jogador inserir texto em vez de números):
            # Atualiza o rótulo da pergunta para pedir que o jogador 
                    # insira um número válido.
            self.lbl_questao.config(text="Por favor, insira um número.")

    

    def iniciar_modo_especifico(self):
        
        """Inicia o modo de uma tabuada específica na ordem correta."""
        
        try:
            
            # Tenta converter o valor digitado no campo de 
                    # entrada (self.entrada_tabuada) em um número inteiro.
            # Este número representa a tabuada que o jogador deseja praticar.
            self.tabuada = int(self.entrada_tabuada.get())
            
            # Verifica se o número da tabuada está entre 1 e 10, pois estas 
                    # são as tabuadas permitidas para o treino.
            if 1 <= self.tabuada <= 10:
                
                # Define a variável 'modo_aleatorio' como False, indicando 
                        # que o jogo seguirá a sequência fixa da tabuada
                        # escolhida pelo jogador, ao invés de gerar 
                        # perguntas aleatórias.
                self.modo_aleatorio = False
                
                # Cria uma lista de perguntas organizadas para a tabuada escolhida.
                # 'self.perguntas_ordenadas' é uma lista de tuplas (self.tabuada, i), 
                        # onde 'i' varia de 1 a 10.
                # Isso significa que o jogador será questionado sobre a 
                        # tabuada escolhida em ordem crescente,
                        # começando com o número multiplicado por 1, depois 
                        # por 2, e assim por diante até 10.
                self.perguntas_ordenadas = [(self.tabuada, i) for i in range(1, 11)]
                
                # Chama a função 'mostrar_jogo', que oculta as instruções de 
                        # seleção de modo e exibe a interface do jogo.
                # Isso prepara a interface para o início do jogo, mostrando os 
                        # elementos como o campo de resposta,
                        # rótulos de pontuação, acertos, tempo e vidas, 
                        # além de exibir as perguntas.
                self.mostrar_jogo()
                
                # Chama a função 'nova_pergunta' para gerar a primeira 
                        # questão da tabuada específica escolhida.
                # A primeira pergunta será sempre (tabuada * 1), e as perguntas 
                        # seguintes seguirão a sequência (tabuada * 2), (tabuada * 3) e assim por diante.
                self.nova_pergunta()
            
            # Se o número da tabuada estiver fora do intervalo 
                    # permitido (não for entre 1 e 10):
            else:
                
                # Atualiza o texto do rótulo de instrução para informar o 
                        # usuário de que ele deve digitar um número entre 1 e 10.
                self.lbl_instrucao.config(text="Digite um número entre 1 e 10.")
        
        # Captura um erro se o valor digitado não for um número válido (por 
                # exemplo, se o jogador inserir texto ou caracteres não numéricos).
        except ValueError:
            
            # Atualiza o rótulo de instrução para informar ao usuário 
                # que ele deve digitar um número válido.
            self.lbl_instrucao.config(text="Por favor, insira um número válido para a tabuada.")


# Cria a janela principal da aplicação usando Tkinter.
# 'tk.Tk()' inicializa a janela que conterá todos os 
        # widgets e controles da interface gráfica.
janela = tk.Tk()

# Cria uma instância da classe 'JogoTabuada', passando a 
        # janela principal 'janela' como argumento.
# Isso configura a interface do jogo e inicializa o 
        # jogo dentro dessa janela.
jogo = JogoTabuada(janela)

# Inicia o loop principal da aplicação Tkinter.
# 'mainloop()' mantém a janela aberta, gerenciando eventos 
        # de interação, como cliques e entradas de teclado.
janela.mainloop()