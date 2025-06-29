# Importa o módulo tkinter e o renomeia como tk
        # para simplificar o acesso às suas funcionalidades
import tkinter as tk

# Importa as classes Image, ImageTk e ImageDraw do 
        # módulo PIL para manipulação de imagens
from PIL import Image, ImageTk, ImageDraw

# Definição da classe 'AplicacaoEfeitoRevelacao' que 
        # contém toda a lógica da aplicação
class AplicacaoEfeitoRevelacao:
    
    # Método construtor chamado automaticamente quando uma 
            # instância da classe é criada.
    def __init__(self, janela_principal, caminho_imagem_inferior, caminho_imagem_superior):
        
        # A variável 'self.janela_principal' é usada para 
                # armazenar a referência da janela principal do aplicativo Tkinter.
        self.janela_principal = janela_principal
        
        # Define o título da janela principal para 
                # "Efeito de Revelação Dinâmica"
        self.janela_principal.title("Efeito de Revelação Dinâmica")

        try:
            # Tentativa de executar o código dentro deste 
                    # bloco. Se ocorrer erro, o bloco 'except' será executado.

            # Carregar a imagem inferior usando a biblioteca 
                    # PIL (Python Imaging Library).
            # 'Image.open' abre o arquivo da imagem a partir do 
                    # caminho fornecido e armazena o objeto de 
                    # imagem em 'self.imagem_inferior'.
            self.imagem_inferior = Image.open(caminho_imagem_inferior)
            
            # Carregar a imagem superior de forma semelhante.
            self.imagem_superior = Image.open(caminho_imagem_superior)

            # Ajustar o tamanho da imagem superior para ser 
                    # igual ao da imagem inferior.
            # 'self.imagem_superior.resize' redimensiona a 
                    # imagem. 'self.imagem_inferior.size' fornece as 
                    # dimensões da imagem inferior como destino 
                    # para o redimensionamento.
            # 'Image.Resampling.LANCZOS' é um método de 
                    # interpolação para alta qualidade.
            self.imagem_superior = self.imagem_superior.resize(self.imagem_inferior.size, Image.Resampling.LANCZOS)

            # Criar um canvas (tela) no Tkinter onde as 
                    # imagens serão exibidas.
            # 'tk.Canvas' cria um espaço para desenho dentro 
                    # da janela principal.
            # 'width' e 'height' definem a largura e altura do 
                    # canvas, baseadas nas dimensões da imagem inferior.
            self.tela = tk.Canvas(janela_principal, width=self.imagem_inferior.width, height=self.imagem_inferior.height)
            
            # 'pack' é um gerenciador de geometria que organiza 
                    # widgets em blocos antes de colocá-los na janela pai.
            self.tela.pack()

            # Converter as imagens para um formato que o Tkinter 
                    # pode usar e manter uma referência a essas imagens.
            # 'ImageTk.PhotoImage' converte um objeto de 
                    # imagem PIL em um objeto de imagem Tkinter.
            self.tk_imagem_inferior = ImageTk.PhotoImage(self.imagem_inferior)
            self.tk_imagem_superior = ImageTk.PhotoImage(self.imagem_superior)

            # Exibir a imagem inferior no canvas.
            # 'create_image' coloca a imagem no canvas na posição 
                    # especificada (0,0), que é o canto superior esquerdo.
            # 'anchor="nw"' significa que a imagem é ancorada do 
                    # lado norte e oeste (topo esquerdo).
            self.tela.create_image(0, 0, image=self.tk_imagem_inferior, anchor="nw")
            
            # Vincular um evento de movimento do mouse ao canvas.
            # 'self.tela.bind' associa um evento (neste caso, 
                    # movimento do mouse, '<Motion>') a um método 
                    # que será chamado quando o evento ocorrer.
            # 'self.movimento_mouse' é o método que será chamado 
                    # sempre que o mouse se mover sobre o canvas.
            self.tela.bind("<Motion>", self.movimento_mouse)
            
            # Mensagem indicando que a inicialização foi concluída e 
                    # instruindo o usuário a interagir.
            print("Inicialização completa. Passe o mouse sobre a janela para ver o efeito.")
            
        except Exception as erro:
            
            # Se ocorrer um erro durante a execução do bloco 
                    # 'try', este bloco será executado.
            # 'print' mostra uma mensagem de erro detalhando o problema.
            print(f"Erro ao inicializar a aplicação: {erro}")



    # Definição do método 'movimento_mouse', que é chamado 
            # sempre que o mouse se move sobre o canvas.
    def movimento_mouse(self, evento):
        
        # Captura as coordenadas x e y do mouse no momento do 
                # evento. 'evento.x' e 'evento.y' são as posições 
                # horizontal e vertical do cursor.
        x, y = evento.x, evento.y
    
        # Criar uma nova imagem (máscara) para definir quais 
                # partes da imagem superior serão visíveis.
        # 'Image.new' cria uma nova imagem. O primeiro argumento "L" 
                # indica que a imagem é em escala de cinza.
        # 'self.imagem_inferior.size' especifica o tamanho da 
                # máscara igual ao tamanho da imagem inferior.
        # '0' é o valor inicial para a cor de cada pixel (0 representa preto,
                # que é totalmente transparente neste contexto).
        mascara = Image.new("L", self.imagem_inferior.size, 0)
        
        # Desenha uma elipse branca (valor 255 de cor, que 
                # representa opacidade total) na máscara no 
                # local do cursor do mouse.
        # 'ImageDraw.Draw(mascara)' cria um objeto que pode 
                # desenhar na imagem 'mascara'.
        # '.ellipse' é uma função que desenha uma elipse definida pela 
                # caixa delimitadora (x-50, y-50, x+50, y+50), que é um 
                # retângulo centrado no cursor.
        # 'fill=255' preenche a elipse de branco, fazendo essa 
                # parte da máscara opaca e revelando a imagem superior nessa área.
        ImageDraw.Draw(mascara).ellipse((x - 50, y - 50, x + 50, y + 50), fill=255)
        
        # Combinar a imagem superior e inferior usando a máscara 
                # criada. A elipse branca na máscara revelará 
                # partes da imagem superior.
        # 'Image.composite' é usado para combinar duas imagens (aqui 
                # são a imagem superior e inferior).
        # A 'mascara' determina quais partes de cada imagem 
                # são visíveis.
        imagem_com_mascara = Image.composite(self.imagem_superior, self.imagem_inferior, mascara)
        
        # Converte a imagem resultante para um formato que pode 
                # ser usado no Tkinter.
        # 'ImageTk.PhotoImage(imagem_com_mascara)' converte a 
                # 'imagem_com_mascara' para um formato de imagem do Tkinter.
        self.tk_imagem_com_mascara = ImageTk.PhotoImage(imagem_com_mascara)
        
        # Atualiza o canvas para mostrar a nova imagem com o 
                # efeito de revelação.
        # 'self.tela.create_image' coloca a nova imagem no 
                # canvas na posição (0, 0), que é o canto 
                # superior esquerdo.
        # 'anchor="nw"' assegura que a imagem é ancorada a 
                # partir do canto superior esquerdo.
        self.tela.create_image(0, 0, image=self.tk_imagem_com_mascara, anchor="nw")



# Iniciar a janela principal
# Esta seção do código é responsável por criar e exibir a 
        # janela principal da aplicação.

# 'tk.Tk()' é uma chamada ao Tkinter para criar a janela 
        # principal da interface gráfica do usuário.
# Esta janela serve como a base para qualquer interação 
        # gráfica na aplicação.
janela_principal = tk.Tk()

# Cria uma instância da classe 'AplicacaoEfeitoRevelacao'.
# Este é o momento em que o construtor '__init__' 
        # da classe é chamado.
# Passamos 'janela_principal' como a janela na qual a 
        # aplicação vai operar.
# 'imagem-inferior.jpg' e 'imagem-superior.jpg' são 
        # argumentos que representam os caminhos das 
        # imagens usadas na aplicação.
# Esses caminhos indicam quais imagens serão carregadas 
        # para criar o efeito de revelação dinâmica.
aplicacao = AplicacaoEfeitoRevelacao(janela_principal, 'imagem-inferior.jpg', 'imagem-superior.jpg')

# 'janela_principal.mainloop()' é um método que inicia o 
        # loop de eventos da interface gráfica.
janela_principal.mainloop()