# Importar o módulo tkinter e renomeá-lo como 'tk' 
        # para facilitar o acesso às suas funcionalidades.
import tkinter as tk

# Definição da classe 'Semaforo', que encapsula toda a 
        # lógica e interface gráfica para simular um semáforo.
class Semaforo:
    
    # Método construtor da classe, chamado ao criar 
            # uma instância de 'Semaforo'.
    def __init__(self, janela_principal):
        
        # 'self.janela_principal' armazena a referência 
                # para a janela principal da aplicação Tkinter.
        # Este objeto será usado para configurar propriedades 
                # da janela e para adicionar elementos gráficos.
        self.janela_principal = janela_principal
        
        # Define o título da janela principal, que aparecerá 
                # na barra de título da janela.
        self.janela_principal.title("Simulador de Semáforo Interativo e Automático")

        # Configuração do canvas onde as luzes do semáforo 
                # serão desenhadas.
        # 'tk.Canvas' é usado para criar uma área retangular 
                # que pode conter desenhos ou outros elementos gráficos.
        # 'width=200' e 'height=600' definem a largura e 
                # altura do canvas em pixels.
        # 'bg='black'' configura a cor de fundo do canvas 
                # para preto, simulando o fundo típico de um semáforo.
        self.tela = tk.Canvas(janela_principal, width=200, height=600, bg='black')
        
        # 'self.tela.pack()' é um gerenciador de geometria 
                # que coloca o canvas dentro da janela 
                # principal e o torna visível.
        self.tela.pack()

        # Configuração inicial das luzes do semáforo.
        # 'self.cores' é uma lista que armazena as cores 
                # iniciais de cada luz do semáforo, começando 
                # todas como 'grey', indicando que estão apagadas.
        self.cores = ['grey', 'grey', 'grey']
        
        # 'self.luzes_id' é uma lista para armazenar os 
                # identificadores das luzes criadas no canvas. 
                # Estes IDs serão usados para modificar as 
                # luzes mais tarde.
        self.luzes_id = []
        
        # 'self.cores_ativas' é uma lista das cores que cada 
                # luz do semáforo deverá exibir quando estiver 
                # ativa: vermelho, amarelo e verde.
        self.cores_ativas = ['red', 'yellow', 'green']
        
        # 'self.intervalos' define quanto tempo (em milissegundos) 
                # cada luz ficará ativa antes de mudar para a 
                # próxima. Todos estão configurados para 
                # 2000 milissegundos (2 segundos).
        self.intervalos = [2000, 2000, 2000]


        # Este bloco de código cria três círculos no canvas, 
                # representando as luzes do semáforo.
        # Um loop 'for' é utilizado para repetir a criação de 
                # três círculos (para as luzes vermelha, 
                # amarela e verde).
        for i in range(3):
            
            # Coordenadas para o canto superior esquerdo (x0, y0) e 
                    # inferior direito (x1, y1) de cada círculo.
            # '50' e '150' definem a posição horizontal dos 
                    # círculos no canvas, centralizando-os na 
                    # largura de 200 pixels do canvas.
            # '50 + 200 * i' e '150 + 200 * i' calculam a posição 
                    # vertical de cada círculo, espaçando-os 
                    # verticalmente por 200 pixels.
            x0, y0 = 50, 50 + 200 * i
            x1, y1 = 150, 150 + 200 * i
        
            # 'self.tela.create_oval' cria um círculo (ou oval) no canvas.
            # 'fill=self.cores[i]' define a cor de preenchimento 
                    # inicial do círculo, começando todas como 'grey' (apagadas).
            # 'outline='white'' define a cor do contorno dos 
                    # círculos como branco.
            # 'width=2' define a espessura da linha do contorno 
                    # como 2 pixels.
            luz = self.tela.create_oval(x0, y0, x1, y1, fill=self.cores[i], outline='white', width=2)
        
            # 'self.luzes_id.append(luz)' adiciona o identificador 
                    # do círculo criado à lista 'self.luzes_id'.
            # Isso permite que esses círculos sejam acessados e 
                    # modificados posteriormente.
            self.luzes_id.append(luz)
        
            # 'self.tela.tag_bind' vincula um evento de clique do 
                    # mouse (botão esquerdo, '<Button-1>') ao círculo.
            # 'lambda event, idx=i: self.mudar_cor_manualmente(idx)' é 
                    # uma função anônima que chama 'mudar_cor_manualmente'
            # com o índice do círculo clicado. Isso permite que a 
                    # cor do semáforo seja alterada manualmente 
                    # clicando na luz correspondente.
            self.tela.tag_bind(luz, '<Button-1>', lambda event, idx=i: self.mudar_cor_manualmente(idx))
        
        # Variável 'self.estado_atual' inicia em 0, o que corresponde à 
                # luz vermelha do semáforo sendo a primeira a 
                # ser ativada na sequência automática.
        self.estado_atual = 0
        
        # 'self.ciclo_id' é usado para manter a referência do 
                # agendamento do ciclo automático de mudança de cores.
        # Inicialmente, é definido como None porque ainda não 
                # há um ciclo programado.
        self.ciclo_id = None
        
        # Chama o método 'self.mudar_cor_automatically' para 
                # iniciar a sequência automática de mudança 
                # de cores do semáforo.
        self.mudar_cor_automatically()


    # Definição do método 'mudar_cor_automatically' dentro 
            # da classe 'Semaforo'.
    # Este método é responsável por controlar a sequência 
            # automática de mudança de cores do semáforo.
    def mudar_cor_automatically(self):
        
        # Chama o método 'mudar_cor' passando o índice da cor atual.
        # Este método altera a cor da luz correspondente ao 
                # índice e define as outras para 'grey'.
        self.mudar_cor(self.estado_atual)
    
        # Atualiza 'self.estado_atual' para o próximo estado, 
                # que controla qual luz deve ser acesa.
        # '(self.estado_atual + 1) % 3' garante que o valor 
                # de 'self.estado_atual' seja sempre 0, 1 ou 2.
        # Este cálculo faz com que, após o índice 2 (verde), 
                # volte para 0 (vermelho), criando um ciclo contínuo.
        self.estado_atual = (self.estado_atual + 1) % 3
    
        # Agenda a próxima execução do método 'mudar_cor_automatically'.
        # 'self.janela_principal.after(self.intervalos[self.estado_atual], 
                # self.mudar_cor_automatically)' usa o método 'after' 
                # para agendar a mudança.
        # 'self.intervalos[self.estado_atual]' obtém o intervalo de 
                # tempo (em milissegundos) para a próxima mudança, 
                # garantindo que cada cor fique ativa pelo tempo especificado.
        # Quando esse tempo expirar, 'mudar_cor_automatically' será 
                # chamado novamente, continuando o ciclo de mudança de cores.
        self.ciclo_id = self.janela_principal.after(self.intervalos[self.estado_atual], self.mudar_cor_automatically)


    # Definição do método 'mudar_cor_manualmente', que permite a 
                # alteração manual da cor do semáforo.
    # 'index' é o parâmetro que indica qual luz (0 para vermelho, 1 
                # para amarelo, 2 para verde) deve ser ativada.
    def mudar_cor_manualmente(self, index):
        
        # Primeiro, verifica se há um ciclo de mudança 
                # automática em andamento.
        # 'self.ciclo_id' armazena a referência para o agendamento do 
                # ciclo automático, se ele estiver ativo.
        if self.ciclo_id:
            
            # Se um ciclo automático estiver ativo, ele é cancelado.
            # 'self.janela_principal.after_cancel(self.ciclo_id)' 
                    # cancela o agendamento do método 'mudar_cor_automatically'.
            # Isso interrompe o ciclo automático para que a mudança 
                    # manual possa ocorrer sem ser sobrescrita imediatamente.
            self.janela_principal.after_cancel(self.ciclo_id)

            # A referência é limpa, indicando que não há mais 
                    # um ciclo automático ativo.
            self.ciclo_id = None  
    
        # Atualiza 'self.estado_atual' para o índice fornecido, 
                # que corresponde à luz que o usuário deseja ativar.
        self.estado_atual = index
        
        # Chama o método 'mudar_cor' para atualizar visualmente o 
                # semáforo, ativando a luz especificada e 
                # apagando as outras.
        self.mudar_cor(self.estado_atual)
    
        # Após a mudança manual, reinicia o ciclo automático da 
                # mudança de cores a partir da cor selecionada.
        # 'self.janela_principal.after(self.intervalos[self.estado_atual], 
                # self.mudar_cor_automatically)' reagenda o 
                # método 'mudar_cor_automatically'
                # para continuar alterando as cores automaticamente 
                # após o intervalo especificado para a cor atual.
        # Isso garante que, mesmo após uma interação manual, o 
                # semáforo retorne ao seu ciclo automático.
        self.ciclo_id = self.janela_principal.after(self.intervalos[self.estado_atual], self.mudar_cor_automatically)


    # Definição do método 'mudar_cor', responsável por 
                # controlar a exibição das cores das luzes do semáforo.
    def mudar_cor(self, index):
        
        # Este loop percorre cada uma das três luzes do 
                # semáforo (índices 0, 1 e 2).
        for i in range(3):
            
            # Condicional que verifica se o índice atual do loop é 
                    # igual ao índice fornecido como parâmetro.
            if i == index:
                
                # Se verdadeiro, configura a luz correspondente 
                        # para sua cor ativa.
                # 'self.tela.itemconfig(self.luzes_id[i], fill=self.cores_ativas[i])' 
                        # modifica a configuração de um item no canvas.
                # 'self.luzes_id[i]' identifica qual luz está sendo modificada.
                # 'fill=self.cores_ativas[i]' define a cor de preenchimento da 
                        # luz para a cor ativa correspondente (vermelho, 
                        # amarelo ou verde).
                self.tela.itemconfig(self.luzes_id[i], fill=self.cores_ativas[i])
                
            else:
                
                # Se falso, apaga a luz configurando sua cor para cinza.
                # Isso garante que apenas uma luz esteja ativa por vez, 
                        # imitando o comportamento real de um semáforo.
                self.tela.itemconfig(self.luzes_id[i], fill='grey')


# Inicializar a aplicação
# Esta seção do código prepara e exibe a janela 
        # principal do programa.

# 'tk.Tk()' cria uma nova instância da janela 
        # principal do Tkinter.
# Esta instância é o contêiner principal onde todos os 
        # elementos gráficos (widgets) serão colocados.
janela_principal = tk.Tk()

# Criação de uma instância da classe 'Semaforo', passando a 
        # janela principal como argumento.
# 'semaforo = Semaforo(janela_principal)' chama o construtor da 
        # classe 'Semaforo', que configura o semáforo e 
        # inicia a animação.
semaforo = Semaforo(janela_principal)

# 'janela_principal.mainloop()' inicia o loop 
        # principal da aplicação.
janela_principal.mainloop()