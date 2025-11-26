# Importa o módulo tkinter com o apelido 'tk' para 
        # construir a interface gráfica
import tkinter as tk

# Importa as funções 'randint' e 'choice' do módulo 'random' 
        # para gerar números aleatórios e escolher elementos 
        # aleatórios de uma lista, respectivamente
from random import randint, choice

# Define a classe 'JogoMatematica' para construir a lógica do jogo
class JogoMatematica:
    
    # Método construtor que inicializa uma nova instância 
            # da classe JogoMatematica
    def __init__(self, janela):
        
        # Atribui o objeto de janela tkinter passado como argumento 
                # para a variável de instância 'self.janela'
        self.janela = janela
        
        # Configura o título da janela tkinter
        self.janela.title("Exercício Jogo de Matemática")
        
        # Inicializa a variável de instância 'self.vidas' com o 
                # valor 3, representando o número de vidas do jogador
        self.vidas = 3
        
        # Inicializa a variável de instância 'self.pontos' com 0, 
                # representando a pontuação inicial do jogador
        self.pontos = 0
        
        # Inicializa a variável de instância 'self.acertos' com 0, 
                # representando o número inicial de respostas corretas
        self.acertos = 0
        
        # Inicializa a variável de instância 'self.erros' com 0, 
                # representando o número inicial de respostas incorretas
        self.erros = 0
        
        # Inicializa a variável de instância 'self.tempo_restante' com 10, 
                # configurando o tempo inicial para responder cada pergunta
        self.tempo_restante = 10
        
        # Inicializa a variável de instância 'self.timer_id' com None, 
                # que será usada para armazenar o ID do timer do jogo
        self.timer_id = None

        
        # Interface do usuário:
        # Cria um rótulo de título na interface gráfica 
                # usando a classe Label do tkinter.
        # 'janela' é o container principal onde este rótulo será colocado.
        # 'text' define o texto exibido no rótulo.
        # 'font' especifica a fonte do texto; aqui usamos Arial 
                # tamanho 24 em negrito.
        self.lbl_titulo = tk.Label(janela, 
                                   text="Exercício Jogo de Matemática", 
                                   font=("Arial", 24, "bold"))
        
        # Adiciona o rótulo de título ao layout da janela principal.
        # 'pack' é um gerenciador de geometria que organiza widgets em 
                # blocos antes de colocá-los na janela.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels 
                # acima e abaixo do rótulo.
        self.lbl_titulo.pack(pady=10)

        # Cria um widget de rótulo (Label) para mostrar as questões 
                # matemáticas durante o jogo.
        # 'janela' é o container principal onde este rótulo será colocado, 
                # tornando-o visível na interface gráfica.
        # 'text=""' significa que inicialmente o rótulo não tem texto 
                # definido — ele será atualizado quando uma nova pergunta for gerada.
        # 'font=("Arial", 20)' define que a fonte do texto será 
                # Arial, tamanho 20, o que torna o texto claramente visível para o usuário.
        self.lbl_questao = tk.Label(janela, 
                                    text="", 
                                    font=("Arial", 20))
        
        # Organiza o rótulo da questão na janela principal. 
        # 'pack()' é um método que organiza widgets em blocos, 
                # permitindo-lhes expandir e contrair com a janela.
        # 'pady=10' adiciona um espaçamento vertical de 10 pixels 
                # acima e abaixo do rótulo, ajudando a separá-lo 
                # visualmente de outros widgets.
        self.lbl_questao.pack(pady=10)
        
        # Cria um campo de entrada (Entry) onde o usuário pode 
                # digitar suas respostas.
        # 'font=("Arial", 14)' especifica que o texto digitado neste 
                # campo será na fonte Arial de tamanho 14, garantindo 
                # que seja grande o suficiente para leitura fácil.
        self.entrada_resposta = tk.Entry(janela, 
                                         font=("Arial", 14))
        
        # Adiciona o campo de entrada à interface gráfica. 
        # 'pack(pady=10)' usa novamente o método pack para adicionar o 
                # campo de entrada na janela com um espaçamento vertical 
                # de 10 pixels, similar ao rótulo da questão.
        self.entrada_resposta.pack(pady=10)
        
        # Associa o evento de pressionar a tecla 'Enter' ao método 'verificar_resposta'.
        # 'bind("<Return>", self.verificar_resposta)' liga a 
                # tecla Enter (Retorno) ao método verificar_resposta.
        # Isso significa que quando o usuário pressiona Enter após 
                # digitar uma resposta, a função verificar_resposta é 
                # automaticamente chamada para avaliar a resposta.
        self.entrada_resposta.bind("<Return>", self.verificar_resposta)

        
        # Cria um rótulo (Label) para exibir a pontuação atual do jogador.
        # 'janela' é o container onde este rótulo é colocado, 
                # fazendo parte da interface gráfica principal do jogo.
        # 'text="Pontos: 0"' define o texto inicial do rótulo, mostrando 
                # que o jogador começa o jogo com 0 pontos.
        # 'font=("Arial", 14)' especifica que o texto do rótulo será na 
                # fonte Arial de tamanho 14, o que é adequado 
                # para uma leitura clara e fácil.
        self.lbl_pontos = tk.Label(janela, text="Pontos: 0", font=("Arial", 14))
        
        # Adiciona o rótulo da pontuação ao layout da janela.
        # 'pack(pady=5)' usa o método pack para organizar o rótulo na 
                # interface. O parâmetro 'pady=5' adiciona um espaço 
                # vertical de 5 pixels acima e abaixo do rótulo,
                # criando uma separação visual entre este rótulo e 
                # outros elementos da interface.
        self.lbl_pontos.pack(pady=5)
        
        # Cria outro rótulo para exibir o número de respostas 
                # corretas (acertos) do jogador.
        # 'text="Acertos: 0"' mostra que inicialmente o jogador não 
                # tem acertos, iniciando o contador de acertos em 0.
        # A fonte é a mesma do rótulo de pontos para manter a 
                # consistência visual na interface.
        self.lbl_acertos = tk.Label(janela, 
                                    text="Acertos: 0", 
                                    font=("Arial", 14))
        
        # Adiciona o rótulo de acertos à janela principal.
        # O uso de 'pack(pady=5)' também aqui significa que 
                # este rótulo será organizado com o mesmo espaçamento 
                # vertical que o rótulo de pontos,
                # ajudando a manter um layout uniforme e organizado.
        self.lbl_acertos.pack(pady=5)

        
        # Cria um rótulo (Label) para exibir a quantidade de 
                # vidas restantes do jogador.
        # 'janela' é o container onde este rótulo é colocado, 
                # fazendo parte da interface gráfica principal do jogo.
        # 'text="Vidas: 3"' define o texto inicial do rótulo, 
                # mostrando que o jogador começa o jogo com 3 vidas.
        # 'font=("Arial", 14)' especifica que o texto do rótulo 
                # será na fonte Arial de tamanho 14, o que é adequado 
                # para uma leitura clara e fácil.
        # 'fg="red"' configura a cor do texto para vermelho, destacando a 
                # importância das vidas no contexto do jogo, pois o 
                # vermelho geralmente denota urgência ou alerta.
        self.lbl_vidas = tk.Label(janela, 
                                  text="Vidas: 3", 
                                  font=("Arial", 14), 
                                  fg="red")
        
        # Adiciona o rótulo das vidas ao layout da janela.
        # 'pack(pady=5)' usa o método pack para organizar o rótulo na 
                # interface. O parâmetro 'pady=5' adiciona um espaço 
                # vertical de 5 pixels acima e abaixo do rótulo,
                # criando uma separação visual entre este rótulo e 
                # outros elementos da interface.
        self.lbl_vidas.pack(pady=5)
        
        # Cria um rótulo para exibir o tempo restante para 
                # responder a pergunta atual.
        # 'text="Tempo: 10"' mostra que inicialmente o jogador 
                # tem 10 segundos para responder a cada pergunta.
        # 'fg="blue"' configura a cor do texto para azul, usando 
                # uma cor que é frequentemente associada à calma e 
                # concentração, contrastando com o vermelho usado para as vidas.
        self.lbl_tempo = tk.Label(janela, 
                                  text="Tempo: 10", 
                                  font=("Arial", 14), 
                                  fg="blue")
        
        # Adiciona o rótulo do tempo à janela principal.
        # 'pack(pady=5)' organiza este rótulo com o mesmo espaçamento 
                # vertical usado para outros rótulos, mantendo a consistência do layout.
        self.lbl_tempo.pack(pady=5)
        
        # Cria um botão que permite ao usuário enviar sua resposta.
        # 'text="Responder"' define o texto no botão, que é a 
                # ação que o usuário realizará ao clicá-lo.
        # 'command=self.verificar_resposta' vincula este botão à 
                # função verificar_resposta, que será executada 
                # quando o botão for pressionado.
        # Isso permite que a resposta inserida no campo de 
                # entrada seja avaliada assim que o botão for clicado.
        self.btn_enviar = tk.Button(janela, 
                                    text="Responder", 
                                    command=self.verificar_resposta)
        
        # Adiciona o botão à interface gráfica.
        # 'pack(pady=10)' usa o método pack com um espaçamento vertical 
                # de 10 pixels, proporcionando um espaço maior ao redor 
                # do botão para facilitar a interação do usuário.
        self.btn_enviar.pack(pady=10)
        
        # Chama o método 'nova_pergunta' para gerar a primeira pergunta 
                # do jogo e iniciar o ciclo de perguntas e respostas.
        # Esse método é responsável por configurar todo o necessário para 
                # começar a interação do jogo, incluindo selecionar uma 
                # pergunta aleatória e configurar o temporizador.
        self.nova_pergunta()


    def nova_pergunta(self):
    
        """Gera uma nova questão de matemática desafiadora."""
        
        # Verifica se há um timer ativo (uma contagem regressiva 
                # para a resposta) e, se sim, cancela esse timer.
        # Isso é necessário para reiniciar o timer cada vez que 
                # uma nova pergunta é gerada.
        if self.timer_id:
            self.janela.after_cancel(self.timer_id)
        
        # Lista das operações matemáticas possíveis no jogo.
        operacoes = ['+', '-', '*', '/']
        
        # Gera dois números aleatórios entre 1 e 100 que 
                # serão usados na questão.
        self.num1 = randint(1, 100)
        self.num2 = randint(1, 100)
        
        # Escolhe aleatoriamente uma operação da lista de operações.
        self.operador = choice(operacoes)
        
        # Verifica qual operador foi escolhido aleatoriamente e 
                # executa o bloco de código correspondente.
        if self.operador == '+':
            
            # Se o operador for '+', cria uma pergunta de adição 
                    # usando os números gerados aleatoriamente.
            # Formata a pergunta como uma string "num1 + num2" e a 
                    # atribui à variável self.questao.
            self.questao = f"{self.num1} + {self.num2}"
            
            # Calcula a resposta correta somando num1 e num2. 
            # O resultado da soma é armazenado em self.resposta_correta, 
                    # que será usada para verificar a resposta do usuário mais tarde.
            self.resposta_correta = self.num1 + self.num2
            
        elif self.operador == '-':
            
            # Se o operador for '-', cria uma pergunta de subtração.
            # Formata a questão como "num1 - num2" e atribui à 
                    # variável self.questao.
            self.questao = f"{self.num1} - {self.num2}"
            
            # Calcula a resposta correta subtraindo num2 de num1.
            # Armazena o resultado em self.resposta_correta para 
                    # uso na verificação da resposta.
            self.resposta_correta = self.num1 - self.num2
        
        elif self.operador == '*':
            
            # Se o operador for '*', cria uma pergunta de multiplicação.
            # Formata a questão como "num1 * num2" e atribui à 
                    # variável self.questao.
            self.questao = f"{self.num1} * {self.num2}"
            
            # Calcula a resposta correta multiplicando num1 por num2.
            # O resultado da multiplicação é armazenado em 
                    # self.resposta_correta.
            self.resposta_correta = self.num1 * self.num2
        
        else:
            
            # Se nenhum dos operadores anteriores foi selecionado, o 
                    # operador de divisão é assumido.
            # Ajusta 'num1' para ser um múltiplo de 'num2' para 
                    # garantir que a resposta seja um número inteiro.
            # Multiplica num2 por um número aleatório 
                    # entre 1 e 10 para criar num1.
            self.num1 = self.num2 * randint(1, 10)
            
            # Formata a questão de divisão como "num1 / num2" e 
                    # atribui à variável self.questao.
            self.questao = f"{self.num1} / {self.num2}"
            
            # Calcula a resposta correta usando a divisão 
                    # inteira de num1 por num2.
            # Armazena o resultado inteiro em self.resposta_correta.
            self.resposta_correta = self.num1 // self.num2
        
        # Atualiza o texto do rótulo de questão na interface do 
                # usuário para mostrar a nova questão gerada.
        self.lbl_questao.config(text=self.questao)
        
        # Define o tempo restante para responder a 
                # pergunta para 10 segundos.
        self.tempo_restante = 10
        
        # Atualiza o texto do rótulo de tempo na interface do 
                # usuário para refletir o novo tempo restante.
        self.lbl_tempo.config(text=f"Tempo: {self.tempo_restante}")
        
        # Chama o método contar_tempo para iniciar a contagem 
                # regressiva do tempo restante.
        # Esse método reduzirá o tempo restante a cada segundo e 
                # verificará se o tempo se esgotou.
        self.contar_tempo()



    def contar_tempo(self):
        
        """Conta o tempo de 10 segundos para cada pergunta."""
        # Este docstring explica o propósito do método, que é 
                # manter a contagem regressiva do tempo para cada pergunta.
    
        # Verifica se ainda há tempo restante para responder e 
                # se o jogador ainda tem vidas.
        if self.tempo_restante > 0 and self.vidas > 0:
            
            # Se ainda há tempo restante e o jogador não perdeu 
                    # todas as vidas, reduz o tempo restante em 1 segundo.
            self.tempo_restante -= 1
            
            # Atualiza o rótulo na interface gráfica que mostra o 
                    # tempo restante. O uso de f-string permite inserir
                    # diretamente o valor da variável `self.tempo_restante` no texto.
            self.lbl_tempo.config(text=f"Tempo: {self.tempo_restante}")
            
            # Reagenda a execução deste mesmo método (`contar_tempo`) 
                    # para daqui a 1000 milissegundos (1 segundo).
            # O método `after` é uma função do Tkinter que executa 
                    # uma função após um delay especificado.
            # Aqui, ele é usado para criar um loop que atualiza o 
                    # contador de tempo a cada segundo.
            self.timer_id = self.janela.after(1000, self.contar_tempo)
    
        # Se o tempo restante for 0 e o jogador ainda tem vidas, 
                # então o jogador perde uma vida por não responder a tempo.
        elif self.vidas > 0:
            
            # Chama o método `perdeu_vida`, que processa a perda de 
                    # uma vida. Isso pode incluir atualizar a interface do usuário
                    # para mostrar uma vida a menos e, terminar o jogo se 
                    # todas as vidas foram perdidas.
            self.perdeu_vida()


    def verificar_resposta(self, event=None):
    
        """Verifica a resposta inserida pelo usuário."""
        # Esta linha começa a função e inclui um comentário 
                # docstring que explica o propósito da função.
    
        try:
            # Tenta executar o seguinte bloco de código que pode 
                    # potencialmente causar um erro se a entrada não for um número.
            
            # Obtém o texto da caixa de entrada, onde o usuário insere 
                    # sua resposta, e tenta converter para um inteiro.
            resposta_usuario = int(self.entrada_resposta.get())
            
            # Compara a resposta do usuário com a resposta 
                    # correta previamente calculada.
            if resposta_usuario == self.resposta_correta:
                
                # Se a resposta estiver correta, adiciona 10 
                        # pontos à pontuação do usuário.
                self.pontos += 10
                
                # Incrementa o contador de acertos.
                self.acertos += 1
                
                # Atualiza o rótulo na interface gráfica para 
                        # mostrar os novos pontos.
                self.lbl_pontos.config(text=f"Pontos: {self.pontos}")
                
                # Atualiza o rótulo na interface gráfica para mostrar o 
                        # novo número de acertos.
                self.lbl_acertos.config(text=f"Acertos: {self.acertos}")
                
            else:
                
                # Se a resposta do usuário estiver incorreta, chama a 
                        # função que processa a perda de uma vida.
                self.perdeu_vida()
            
            # Limpa o campo de entrada para que esteja pronto 
                    # para a próxima pergunta.
            self.entrada_resposta.delete(0, tk.END)
            
            # Gera uma nova pergunta matemática para continuar o jogo.
            self.nova_pergunta()
            
        except ValueError:
            
            # Este bloco é executado se a conversão da entrada do 
                    # usuário para inteiro falhar,
                    # o que ocorre se o usuário inserir algo que não 
                    # pode ser convertido para número (como letras ou símbolos).
            
            # Atualiza o rótulo da pergunta para pedir ao usuário 
                    # que insira um número válido,
                    # indicando que a entrada anterior não foi apropriada.
            self.lbl_questao.config(text="Por favor, insira um número.")


    def perdeu_vida(self):
        
        """Reduz uma vida e verifica se o jogo deve acabar."""
        # Este comentário docstring descreve brevemente o 
                # propósito da função.
    
        # Reduz o número de vidas do jogador em uma unidade.
        self.vidas -= 1
        
        # Atualiza o rótulo na interface gráfica que mostra o 
                # número de vidas restantes.
        # Utiliza f-string para incorporar a variável `self.vidas` 
                # diretamente no texto, mostrando o novo valor de vidas.
        self.lbl_vidas.config(text=f"Vidas: {self.vidas}")
        
        # Verifica se o número de vidas restantes chegou a zero.
        if self.vidas == 0:
            
            # Se o jogador não tem mais vidas, o método `game_over` é chamado.
            # Este método é responsável por encerrar o jogo, mostrando 
                    # uma mensagem de fim de jogo e desativando elementos da interface.
            self.game_over()
            
        else:
            
            # Se ainda restam vidas, o jogo continua e uma nova pergunta é gerada.
            # O método `nova_pergunta` é chamado para continuar o 
                    # jogo, apresentando uma nova desafio ao jogador.
            self.nova_pergunta()


    def game_over(self):
        
        """Exibe a mensagem de fim de jogo."""
        # Este docstring oferece uma breve descrição do que o método faz.
    
        # Configura o texto do rótulo da questão para informar ao 
                # jogador que o jogo acabou e mostra a pontuação final
                # e o total de acertos que ele conseguiu durante o jogo. 
        # A utilização de f-string permite inserir as variáveis
                # diretamente no texto, facilitando a leitura e 
                # manutenção do código.
        self.lbl_questao.config(text=f"Fim de jogo! Pontuação final: {self.pontos}. Acertos: {self.acertos}")
        
        # Desativa o campo de entrada de resposta. A propriedade `state=tk.DISABLED` 
                # impede que o usuário interaja com o campo de entrada, 
                # efetivamente bloqueando a inserção de novas respostas 
                # após o término do jogo.
        self.entrada_resposta.config(state=tk.DISABLED)
        
        # Desativa o botão de enviar. Isso impede que o usuário 
                # possa enviar respostas após o jogo ter terminado,
                # garantindo que nenhuma função associada ao botão 
                # seja acionada depois do fim do jogo.
        self.btn_enviar.config(state=tk.DISABLED)
        
        # Verifica se existe um temporizador ativo. Se `self.timer_id` 
                # não for None, significa que um temporizador
                # foi configurado e ainda pode estar contando.
        if self.timer_id:
            
            # Cancela o temporizador ativo usando o método `after_cancel`. 
            # Isso é importante para garantir que o método `contar_tempo` 
                    # não seja mais chamado, evitando que a contagem do 
                    # tempo continue indevidamente
                    # após o jogo ter terminado.
            self.janela.after_cancel(self.timer_id)
            
            # Define `self.timer_id` para None, resetando a variável. 
            # Isso é uma boa prática para garantir que o estado
                    # do temporizador seja consistentemente gerenciado e 
                    # para evitar chamadas acidentais se o jogo for reiniciado
                    # ou se outras funções verificarem o status do temporizador.
            self.timer_id = None




# Cria uma nova instância da classe Tk, que é a janela 
        # principal para aplicações Tkinter.
# Esta instância será usada como a janela principal onde 
        # todos os widgets (elementos gráficos) serão colocados.
janela = tk.Tk()

# Cria uma nova instância da classe JogoMatematica, passando a 
        # janela principal como argumento.
# O construtor da classe JogoMatematica configura toda a 
        # interface do usuário dentro desta janela,
        # incluindo rótulos, botões e lógica do jogo.
jogo = JogoMatematica(janela)

# Inicia o loop principal da aplicação Tkinter.
# Este método é essencial porque faz a janela aparecer e começar a 
        # responder a eventos como cliques de mouse e teclas pressionadas.
# Sem esta chamada, a janela não seria exibida, e o programa 
        # terminaria imediatamente após a execução.
janela.mainloop()