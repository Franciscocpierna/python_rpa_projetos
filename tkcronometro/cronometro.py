# Importa a biblioteca Tkinter para criação de
        # interfaces gráficas de usuário.
import tkinter as tk

# Importa classes adicionais do Tkinter, incluindo StringVar para 
        # armazenar strings de forma que mudanças disparem atualizações de 
        # interface, e messagebox para caixas de diálogo.
from tkinter import StringVar, messagebox

# Importa o módulo ttk do Tkinter, que fornece acesso a widgets 
        # temáticos Tk que parecem mais modernos.
from tkinter import ttk

# Define a classe CronometroApp que é responsável pela 
        # lógica e interface do cronômetro.
class CronometroApp:
    
    # Método construtor que inicializa uma nova instância da 
            # classe CronometroApp.
    # 'janela' é um parâmetro que recebe uma instância de tk.Tk(), 
            # que representa a janela principal da aplicação.
    def __init__(self, janela):
        
        # Atribui a instância tk.Tk() recebida ao atributo self.janela 
                # para ser utilizada em outros métodos da classe.
        self.janela = janela
        
        # Define o título da janela principal, que aparece na 
                # barra de título da janela.
        self.janela.title("Cronômetro")
        
        # Define as dimensões da janela principal (largura x altura).
        self.janela.geometry("400x200")
        
        # Configura a cor de fundo da janela principal usando um 
                # código de cor hexadecimal para um azul escuro.
        self.janela.configure(bg="#2E3B4E")

        # Inicialização de variáveis que serão usadas para 
                # controlar o cronômetro.
        # Define a variável self.tempo_segundos para contar o 
                # tempo em segundos. Inicia em 0.
        self.tempo_segundos = 0
        
        # Cria uma instância de StringVar, que é uma variável especial 
                # do Tkinter usada para armazenar strings em uma GUI.
        # StringVar permite atualizações automáticas na GUI quando o 
                # valor da variável muda.
        self.tempo_texto = StringVar()
        
        # Inicializa self.tempo_texto com a string "00:00:00", que é o 
                # formato inicial do tempo exibido.
        self.tempo_texto.set("00:00:00")
        
        # Define a variável self.em_execucao como False. Esta variável 
                # controla se o cronômetro está ativo ou não.
        self.em_execucao = False
        
        # Inicializa self.id_contador com None. Esta variável será 
                # usada para armazenar o identificador do método de agendamento do Tkinter.
        self.id_contador = None

        # Chama o método self.configurar_layout para configurar os 
                # componentes visuais da janela.
        # Este método organiza os widgets dentro da janela, como 
                # rótulos e botões.
        self.configurar_layout()


    # Definição do método 'configurar_layout' dentro da 
            # classe 'CronometroApp'.
    # Este método configura a disposição dos elementos gráficos da 
            # interface, como botões e labels.
    def configurar_layout(self):
        
        # Criando e configurando o estilo dos botões dentro da 
                # aplicação usando a classe Style do módulo ttk.
        # A classe Style permite modificar os estilos temáticos 
                # dos widgets ttk.
        estilo_botao = ttk.Style()
        
        # Configuração do estilo 'TButton', aplicável aos botões ttk.
        # Define a fonte como Helvetica tamanho 12, com um 
                # espaçamento interno de 6 pixels.
        estilo_botao.configure("TButton", font=("Helvetica", 12), padding=6)
    
        # Criação de um widget Label para exibir o tempo do cronômetro.
        # 'self.label_tempo' é uma variável de instância que 
                # armazena o widget Label.
        # 'textvariable=self.tempo_texto' associa este label à 
                # variável StringVar 'self.tempo_texto' que 
                # mantém o texto do tempo.
        # A fonte é configurada como Helvetica tamanho 48, 
                # com fundo azul escuro e texto branco.
        self.label_tempo = tk.Label(self.janela, 
                                    textvariable=self.tempo_texto, 
                                    font=("Helvetica", 48), 
                                    bg="#2E3B4E", 
                                    fg="#FFFFFF")
        
        # Posiciona o label_tempo na janela usando o gerenciador 
                # de layout 'pack'.
        # 'pady=20' adiciona um espaçamento vertical de 20 pixels 
                # acima e abaixo do label para separação visual.
        self.label_tempo.pack(pady=20)

        
        # Criação de um Frame para agrupar os botões de 
                # controle do cronômetro.
        # 'frame_botoes' é um widget Frame com fundo azul 
                # escuro que servirá como container para os botões.
        frame_botoes = tk.Frame(self.janela, bg="#2E3B4E")
        
        # Posiciona o frame_botoes usando o gerenciador de layout 'pack'.
        # 'pady=10' adiciona um espaçamento vertical de 10 
                # pixels acima e abaixo do frame.
        frame_botoes.pack(pady=10)
    
        # Criação do botão 'Iniciar' que inicia a contagem do 
                # tempo do cronômetro.
        # 'command=self.iniciar' define que o método self.iniciar 
                # será chamado quando o botão for clicado.
        self.botao_iniciar = ttk.Button(frame_botoes, 
                                        text="Iniciar", 
                                        command=self.iniciar)
        
        # Posiciona o botão 'Iniciar' no frame_botoes usando o 
                # gerenciador de layout 'grid'.
        # 'row=0, column=0, padx=5' coloca o botão na primeira 
                # linha, primeira coluna, com um espaçamento horizontal de 5 pixels.
        self.botao_iniciar.grid(row=0, column=0, padx=5)
    
        # Criação do botão 'Parar' que interrompe a contagem do tempo.
        # 'command=self.parar' define que o método self.parar 
                # será chamado quando o botão for clicado.
        self.botao_parar = ttk.Button(frame_botoes, 
                                      text="Parar", 
                                      command=self.parar)
        
        # Posiciona o botão 'Parar' ao lado do botão 'Iniciar' usando 'grid'.
        # 'row=0, column=1, padx=5' coloca o botão na primeira 
                # linha, segunda coluna, com um espaçamento horizontal de 5 pixels.
        self.botao_parar.grid(row=0, column=1, padx=5)
    
        # Criação do botão 'Reiniciar' que zera o cronômetro e 
                # atualiza o display.
        # 'command=self.reiniciar' define que o método self.reiniciar 
                # será chamado quando o botão for clicado.
        self.botao_reiniciar = ttk.Button(frame_botoes, 
                                          text="Reiniciar", 
                                          command=self.reiniciar)
        
        # Posiciona o botão 'Reiniciar' ao lado do botão 'Parar' usando 'grid'.
        # 'row=0, column=2, padx=5' coloca o botão na primeira linha, 
                # terceira coluna, com um espaçamento horizontal de 5 pixels.
        self.botao_reiniciar.grid(row=0, column=2, padx=5)
        

    # Definição do método 'iniciar' na classe 'CronometroApp'.
    # Este método é responsável por iniciar a contagem do cronômetro, 
                # mas apenas se ele já não estiver em execução.
    def iniciar(self):
        
        # Documentação do método. Este comentário explica o propósito 
                # do método: iniciar a contagem do cronômetro, mas 
                # somente se não estiver já em execução.
        """Inicia a contagem do cronômetro se não estiver em execução."""
    
        # Condicional que verifica se o cronômetro não está em execução.
        # 'self.em_execucao' é uma variável booleana (True/False) 
                # que indica o estado do cronômetro.
        # 'not self.em_execucao' é verdadeiro quando o cronômetro está 
                # parado, permitindo que a contagem seja iniciada.
        if not self.em_execucao:
            
            # Se o cronômetro não estiver em execução, o valor de 
                    # 'self.em_execucao' é alterado para True.
            # Isso indica que o cronômetro está agora em execução.
            self.em_execucao = True
            
            # Chama o método 'contar' para iniciar a contagem do tempo.
            # 'self.contar()' é um método na mesma classe que manipula a 
                    # lógica para incrementar o contador de tempo e 
                    # atualizar o display.
            self.contar()


    # Definição do método 'contar' dentro da classe 'CronometroApp'.
    # Este método é responsável por atualizar o tempo do 
                # cronômetro e o display a cada segundo.
    def contar(self):
        
        # Documentação do método, explicando que ele atualiza o 
                # tempo do cronômetro e o display a cada segundo.
        """Atualiza o tempo do cronômetro e o display a cada segundo."""
    
        # Verifica se o cronômetro está em execução.
        # 'self.em_execucao' é uma variável booleana (True/False) que 
                # indica o estado do cronômetro.
        # Se 'self.em_execucao' for True, o cronômetro está ativo e 
                # deve continuar contando.
        if self.em_execucao:
            
            # Incrementa o contador de segundos em 1.
            # 'self.tempo_segundos' armazena a quantidade de segundos que 
                    # se passaram desde que o cronômetro foi iniciado.
            self.tempo_segundos += 1
            
            # Converte o tempo total em segundos para minutos e segundos.
            # 'divmod(self.tempo_segundos, 60)' divide 'self.tempo_segundos' 
                    # por 60 e retorna o quociente e o resto.
            # O quociente representa os minutos e o resto representa os segundos.
            minutos, segundos = divmod(self.tempo_segundos, 60)
            
            # Converte os minutos totais para horas e minutos.
            # 'divmod(minutos, 60)' divide 'minutos' por 60 e 
                    # retorna o quociente e o resto.
            # O quociente representa as horas e o resto representa os minutos.
            horas, minutos = divmod(minutos, 60)
            
            # Formata o tempo em horas, minutos e segundos no formato HH:MM:SS.
            # '{:02}' garante que cada unidade de tempo seja exibida 
                    # com dois dígitos, adicionando um zero à esquerda, se necessário.
            tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}"
            
            # Atualiza a variável 'self.tempo_texto' com o tempo formatado.
            # 'self.tempo_texto' é uma instância de StringVar vinculada ao 
                    # display visual do cronômetro.
            # Atualizar essa variável garante que a interface gráfica 
                    # mostre o tempo atualizado.
            self.tempo_texto.set(tempo_formatado)
            
            # Agenda a próxima chamada do método 'contar' para daqui a 
                    # 1000 milissegundos (1 segundo).
            # 'self.janela.after(1000, self.contar)' usa o método 'after' 
                    # do Tkinter para agendar a execução futura de 'self.contar'.
            # Isso cria um loop que faz com que o método 'contar' seja 
                    # chamado repetidamente a cada segundo.
            self.id_contador = self.janela.after(1000, self.contar)


    # Definição do método 'parar' dentro da classe 'CronometroApp'.
    # Este método é responsável por parar a contagem do cronômetro 
            # se ele estiver em execução.
    def parar(self):
        
        # Documentação do método. Este comentário explica que o método 
                # irá interromper a contagem do cronômetro.
        """Para a contagem do cronômetro."""
    
        # Condicional que verifica se o cronômetro está em execução.
        # 'self.em_execucao' é uma variável booleana (True/False) que 
                # indica o estado do cronômetro.
        # 'if self.em_execucao:' é verdadeiro se o cronômetro estiver ativo.
        if self.em_execucao:
            
            # Altera o estado do cronômetro para não ativo (False).
            # Isso impede que o cronômetro continue a contagem.
            self.em_execucao = False
            
            # Verifica se existe um identificador para uma tarefa agendada.
            # 'self.id_contador' armazena o identificador de uma tarefa 
                    # agendada que está incrementando o tempo do cronômetro.
            # 'if self.id_contador:' verifica se esse identificador existe, 
                    # indicando que uma tarefa está ativa.
            if self.id_contador:
                
                # Cancela a tarefa agendada usando 'self.janela.after_cancel()'.
                # 'after_cancel()' é um método do Tkinter que cancela tarefas agendadas.
                # 'self.id_contador' é passado como argumento para identificar 
                        # qual tarefa cancelar.
                self.janela.after_cancel(self.id_contador)
                
                # Define 'self.id_contador' como None para limpar o identificador, 
                        # indicando que não há tarefas agendadas ativas.
                # Isso é importante para garantir que tentativas futuras de 
                        # cancelar ou reiniciar o cronômetro não afetem tarefas erradas.
                self.id_contador = None


    # Definição do método 'reiniciar' dentro da classe 'CronometroApp'.
    # Este método é responsável por reiniciar a contagem do cronômetro, 
            # zerando o tempo e atualizando a exibição.
    def reiniciar(self):
        
        # Documentação do método, explicando o que ele faz: reinicia o 
                # cronômetro para zero e atualiza o display visual do cronômetro.
        """Reinicia o cronômetro para zero e atualiza o display."""
    
        # Chamada ao método 'parar' para interromper a contagem do cronômetro.
        # Este passo é importante para garantir que o cronômetro 
                # pare de contar antes de ser reiniciado.
        # O método 'parar' também cuida de limpar qualquer tarefa 
                # agendada que estivesse incrementando o tempo.
        self.parar()
    
        # Redefine a variável 'self.tempo_segundos' para 0.
        # 'self.tempo_segundos' é a variável que armazena a quantidade de 
                # segundos que se passaram desde que o cronômetro foi iniciado.
        # Zerar essa variável é necessário para reiniciar a contagem 
                # do tempo desde o início.
        self.tempo_segundos = 0
    
        # Atualiza a variável 'self.tempo_texto', que é uma instância de 
                # StringVar vinculada ao display visual do cronômetro.
        # 'self.tempo_texto.set("00:00:00")' define o texto da variável 
                # para "00:00:00", que é a representação visual do tempo zerado.
        # Isso assegura que o display do cronômetro na interface 
                # gráfica mostre o tempo como zero.
        self.tempo_texto.set("00:00:00")



# Verifica se o script está sendo executado como o programa principal.
# '__name__' é uma variável especial do Python que indica 
        # como o módulo foi executado.
# Se '__name__' for igual a '__main__', significa que o 
        # script está sendo executado diretamente.
# Isso não acontece se o script foi importado como um 
        # módulo em outro script.
if __name__ == "__main__":
    
    # Cria uma instância da janela principal do Tkinter.
    # 'tk.Tk()' inicializa uma nova janela principal que 
            # será a base da aplicação.
    # Esta janela serve como o container principal onde todos os 
            # widgets da aplicação serão colocados.
    janela_principal = tk.Tk()

    # Cria uma instância da classe 'CronometroApp', passando 
            # 'janela_principal' como argumento.
    # 'app_cronometro' é o objeto que representa a aplicação do cronômetro.
    # A instância 'CronometroApp' inicializa e configura a aplicação, 
            # preparando todos os elementos visuais e a lógica do cronômetro.
    app_cronometro = CronometroApp(janela_principal)


    # Inicia o loop de eventos do Tkinter, que mantém a janela 
            # aberta e a aplicação responsiva.
    # 'mainloop()' é um método do Tkinter que entra em um 
            # loop de espera de eventos.
    # Este loop continua executando até que a janela seja fechada, 
            # processando eventos como cliques do mouse e entradas do teclado.
    janela_principal.mainloop()