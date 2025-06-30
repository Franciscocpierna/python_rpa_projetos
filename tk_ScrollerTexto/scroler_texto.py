# Importa o módulo tkinter e o renomeia como 'tk', 
        # facilitando sua utilização no código.
import tkinter as tk

# 'class ScrollerTexto' define uma classe chamada 'ScrollerTexto'.
# Uma classe é um modelo para a criação de objetos (instâncias), 
        # que agrupa informações (atributos) e operações (métodos) relacionadas.
class ScrollerTexto:
    
    # Método '__init__' é o construtor da classe. É chamado 
            # automaticamente quando um novo objeto desta classe é criado.
    # O objetivo deste método é inicializar os atributos do 
            # objeto com valores padrão ou valores fornecidos.
    def __init__(self, janela_principal):
        
        # 'self' refere-se à instância específica da classe que 
                # está sendo criada ou manipulada.
        # 'self.janela_principal' cria um atributo chamado 
                # 'janela_principal' e armazena a referência da 
                # janela Tkinter passada como argumento.
        self.janela_principal = janela_principal
        
        # 'self.janela_principal.title("Scroller de Texto Interativo")' 
                # configura o título da janela principal.
        # Este título é o texto que aparecerá na barra de título 
                # da janela quando ela for exibida.
        self.janela_principal.title("Scroller de Texto Interativo")

        # Configuração do canvas onde o texto será desenhado
        # A largura e a altura do canvas são definidas. 
                # Aqui, '800' e '100' são medidas em pixels.
        self.largura = 800
        self.altura = 100
        
        # 'self.tela' cria um atributo 'tela' e instancia um 
                # novo objeto 'Canvas' que é uma área retangular 
                # destinada para desenho.
        # 'tk.Canvas(janela_principal, width=self.largura, 
                # height=self.altura, bg='black')' cria um canvas 
                # com as dimensões especificadas e fundo preto.
        # O argumento 'janela_principal' indica que este canvas é 
                # um componente da janela principal.
        self.tela = tk.Canvas(janela_principal, width=self.largura, height=self.altura, bg='black')
        
        # 'self.tela.pack()' organiza o canvas dentro da janela principal. 
        # O método 'pack' é um gerenciador de geometria que 
                # coloca o widget na janela e o exibe seguindo um 
                # conjunto de regras de layout.
        self.tela.pack()

        # Define o texto que será animado no scroller.
        # 'self.texto' é um atributo da classe que armazena a 
                # string do texto a ser exibido.
        self.texto = "Este é um exemplo de Python..."
        
        # Cria o texto no canvas configurado previamente.
        # 'self.tela.create_text(self.largura, 50, text=self.texto, 
                # font=('Helvetica', 20), fill='white', anchor='w')' adiciona o texto ao canvas.
        # 'self.largura' indica a posição inicial x do texto, 
                # que é na extremidade direita do canvas.
        # '50' é a posição y do texto, colocando-o no meio da 
                # altura do canvas (que é 100).
        # 'text=self.texto' define o conteúdo do texto.
        # 'font=('Helvetica', 20)' define a fonte e o tamanho do texto.
        # 'fill='white'' define a cor do texto como branco.
        # 'anchor='w'' faz com que o texto seja alinhado pelo 
                # lado esquerdo da posição inicial.
        self.texto_id = self.tela.create_text(self.largura, 50, text=self.texto, font=('Helvetica', 50), fill='white', anchor='w')
        
        # Define a velocidade e a direção do movimento do texto.
        # 'self.velocidade = -2' significa que o texto se moverá 2 
                # pixels para a esquerda a cada iteração da animação.
        self.velocidade = -2
        
        # Define se a animação está ativa.
        # 'self.animando = True' inicia a animação como ativa.
        self.animando = True
        
        # Adiciona eventos de mouse para controlar a animação.
        # 'self.tela.bind("<Enter>", self.parar_animacao)' associa o 
                # evento de passar o mouse sobre o canvas à função 'parar_animacao'.
        # Quando o cursor entra no canvas, a animação pausa.
        self.tela.bind("<Enter>", self.parar_animacao)
        
        # 'self.tela.bind("<Leave>", self.retomar_animacao)' associa o 
                # evento de o mouse sair do canvas à função 'retomar_animacao'.
        # Quando o cursor deixa o canvas, a animação continua.
        self.tela.bind("<Leave>", self.retomar_animacao)
        
        # Chama a função para iniciar a movimentação do texto.
        # 'self.mover_texto()' inicia o loop da animação que move o texto.
        self.mover_texto()


    # Define o método 'mover_texto' responsável por animar o 
            # texto no canvas.
    def mover_texto(self):
        
        # Verifica se a animação está ativa.
        # 'self.animando' é um atributo booleano que determina 
                # se o texto deve se mover ou não.
        if self.animando:
            
            # Mover o texto horizontalmente de acordo com a 
                    # velocidade definida.
            # 'self.tela.move(self.texto_id, self.velocidade, 0)' 
                    # move o texto identificado por 'self.texto_id' na tela.
            # 'self.velocidade' é o deslocamento horizontal (negativo 
                    # para mover para a esquerda).
            # '0' significa que não há movimento vertical.
            self.tela.move(self.texto_id, self.velocidade, 0)
    
            # Obtém a posição atual do lado direito do texto.
            # 'self.tela.bbox(self.texto_id)[2]' retorna a coordenada x 
                    # do lado direito da caixa delimitadora do texto.
            # A caixa delimitadora é um retângulo que completamente contém o texto.
            pos_x = self.tela.bbox(self.texto_id)[2]  
    
            # Verifica se o texto saiu completamente da área 
                    # visível do canvas.
            # Se a borda direita do texto é menor que 0, significa 
                    # que o texto não está mais visível.
            if pos_x < 0:
                
                # Reseta a posição do texto para o lado direito do 
                        # canvas, fazendo-o reaparecer.
                # 'self.tela.coords(self.texto_id, self.largura, 50)' 
                        # define a nova posição do texto.
                # 'self.largura' é a largura do canvas, fazendo o 
                        # texto começar do lado direito novamente.
                # '50' é a posição y, mantendo o texto na mesma altura vertical.
                self.tela.coords(self.texto_id, self.largura, 50)
    
        # Repete a função mover_texto a cada 50 milissegundos.
        # 'self.janela_principal.after(50, self.mover_texto)' 
                # agenda a próxima chamada do método 'mover_texto'.
        # '50' indica o intervalo de tempo em milissegundos até a 
                # função ser chamada novamente.
        self.janela_principal.after(50, self.mover_texto)


    # Define o método 'parar_animacao', responsável por 
            # pausar a animação do texto.
    def parar_animacao(self, event):
        
        # 'self.animando = False' altera o valor do atributo 
                # 'self.animando' para False.
        # Isso faz com que a condição no método 'mover_texto' 
                # deixe de ser verdadeira, interrompendo o 
                # movimento do texto.
        # 'event' é um parâmetro que recebe informações sobre o 
                # evento que disparou essa função, como por 
                # exemplo um evento de mouse.
        self.animando = False
    
    # Define o método 'retomar_animacao', responsável por 
            # retomar a animação do texto.
    def retomar_animacao(self, event):
        
        # 'self.animando = True' altera o valor do atributo 
                # 'self.animando' para True.
        # Isso permite que a condição no método 'mover_texto' 
                # seja novamente verdadeira, reiniciando o 
                # movimento do texto.
        # 'event' funciona da mesma forma que na função anterior, 
                # fornecendo contexto sobre o evento que chamou esta função.
        self.animando = True


# Inicializar a aplicação
# Esta seção do código prepara e exibe a janela principal do programa.

# 'tk.Tk()' cria uma nova instância da janela principal do Tkinter.
# 'tk' é a abreviação de tkinter, que foi importado anteriormente.
# Essa instância é a base da interface gráfica, onde todos os 
        # widgets (componentes gráficos como botões, 
        # textos, etc.) serão colocados.
janela_principal = tk.Tk()

# 'aplicacao = ScrollerTexto(janela_principal)' cria uma 
        # instância da classe 'ScrollerTexto'.
# Esta linha passa 'janela_principal' como argumento para o 
        # construtor da classe 'ScrollerTexto', indicando 
        # que a aplicação deve operar dentro desta janela.
# A classe 'ScrollerTexto' é responsável por configurar e 
        # gerenciar o scroller de texto, incluindo definir 
        # eventos e iniciar a animação do texto.
aplicacao = ScrollerTexto(janela_principal)

# 'janela_principal.mainloop()' inicia o loop principal da aplicação.
# Este método é crucial porque mantém a janela aberta, 
        # permitindo que ela seja interativa e responda a 
        # eventos como cliques do mouse ou teclados.
janela_principal.mainloop()