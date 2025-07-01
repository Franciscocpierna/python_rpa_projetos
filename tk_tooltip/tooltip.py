# Importa o módulo tkinter e renomeia-o como 'tk', 
        # utilizado para criar interfaces gráficas.
import tkinter as tk

# Importa o submódulo ttk do tkinter, que contém widgets 
        # com estilos aprimorados.
from tkinter import ttk


# Define a classe 'CaixaDeDica' que será utilizada para criar 
        # uma caixa de dicas (tooltip).
class CaixaDeDica:
    
    # Método construtor da classe, chamado quando um objeto é criado.
    def __init__(self, widget, texto=''):
        
        # Atribui o widget pai, no qual a dica será exibida.
        self.widget = widget
        
        # Atribui o texto que será mostrado na caixa de dica. 
                # Padrão é uma string vazia.
        self.texto = texto
        
        # Inicializa a variável 'janela_dica' como None. Esta variável 
                # armazenará a janela do tooltip.
        self.janela_dica = None


    # Método para mostrar a dica na interface gráfica.
    def mostrar_dica(self, x, y):
        
        # Cria uma nova janela 'top-level' que será usada como a janela do 
                # tooltip. Esta janela é filha do widget pai.
        self.janela_dica = jd = tk.Toplevel(self.widget)
        
        # Configura a janela para não ter bordas ou barra de título.
        jd.wm_overrideredirect(True)
        
        # Define a geometria da janela para posicioná-la nas 
                # coordenadas (x, y) especificadas.
        jd.wm_geometry(f"+{x}+{y}")
    
        # Cria um rótulo dentro da janela do tooltip. Um rótulo é um 
                # widget que exibe texto ou imagens.
        # 'jd' é o objeto da janela de nível superior onde o rótulo será colocado.
        # 'text=self.texto' define o conteúdo do texto do rótulo, que é 
                # passado ao criar uma instância da caixa de dica.
        label = tk.Label(jd, 
                         text=self.texto, 
                         background="yellow", 
                         relief="solid", 
                         borderwidth=1,
                         font=("tahoma", "20", "bold"))
        # Atributos adicionais do rótulo:
        # 'background="yellow"' define a cor de fundo do rótulo como 
                # amarelo, tornando-o visualmente distinto.
        # 'relief="solid"' especifica o tipo de borda do rótulo, que 
                # neste caso é sólida, oferecendo um contorno mais definido.
        # 'borderwidth=1' estabelece a largura da borda do rótulo em 1 pixel.
        # 'font=("tahoma", "20", "bold")' configura a fonte do texto no 
                # rótulo usando a fonte Tahoma, tamanho 20 e em negrito,
                # o que torna o texto facilmente legível.
        
        # Empacota o rótulo dentro da janela 'jd'. O método 'pack' é um 
                # gerenciador de geometria que organiza widgets em blocos 
                # antes de colocá-los na janela pai.
        # 'ipadx=10' e 'ipady=5' adicionam 10 pixels de preenchimento 
                # interno no eixo x (horizontal) e 5 pixels no eixo y (vertical),
        # respectivamente. Isso ajuda a criar um espaço extra dentro do 
                # rótulo, garantindo que o texto não fique muito apertado 
                # contra as bordas do widget.
        label.pack(ipadx=10, ipady=5)

    
    # Método para esconder a dica, ocultando a janela do tooltip.
    def esconder_dica(self):
        
        # Verifica se a janela do tooltip está atualmente visível.
        if self.janela_dica:
            
            # Destrói a janela do tooltip, efetivamente a removendo da tela.
            self.janela_dica.destroy()
            
        # Redefine a variável 'janela_dica' para None, indicando que 
                # não há tooltip sendo exibido no momento.
        self.janela_dica = None
        

# Define a classe 'TabelaComCaixaDeDica' que inclui uma tabela 
                # interativa com caixas de dica associadas.
class TabelaComCaixaDeDica:
    
    # Método construtor da classe, chamado quando um objeto 
            # desta classe é criado.
    def __init__(self, raiz):
        
        # Atribui o widget raiz passado ao objeto e define o 
                # título da janela principal.
        self.raiz = raiz
        self.raiz.title("Tabela com Caixa de Dica")

        # Cria um 'quadro' (Frame) dentro do widget 'raiz'. Um quadro é um contêiner 
                # que serve para agrupar widgets e controlar o layout da interface.
        quadro = ttk.Frame(raiz)
        
        # Configura o quadro para ajustar-se automaticamente ao tamanho disponível 
                # no widget 'raiz'. O método 'pack' organiza o quadro dentro do seu contêiner pai.
        # 'padx' e 'pady' adicionam uma margem interna de 10 pixels em x (esquerda e direita) 
                # e y (topo e base), respectivamente.
        # 'fill="both"' faz com que o quadro expanda tanto na horizontal quanto na vertical.
        # 'expand=True' permite que o quadro expanda para preencher qualquer 
                # espaço não usado no contêiner pai.
        quadro.pack(padx=10, pady=10, fill="both", expand=True)
        
        # Cria uma tabela chamada 'Treeview' dentro do 'quadro'. 'Treeview' é um 
                # widget usado para exibir listas hierárquicas de informações.
        # 'columns=("Nome", "Idade", "Profissão")' define as colunas que a tabela terá.
        # 'show="headings"' configura a tabela para mostrar apenas os cabeçalhos 
                # das colunas, sem a coluna de identificação principal à esquerda.
        # 'style="Estilo.Treeview"' aplica um estilo predefinido chamado 'Estilo.Treeview' 
                # que pode ser configurado para alterar a aparência das linhas e cabeçalhos.
        self.tabela = ttk.Treeview(quadro, 
                                   columns=("Nome", "Idade", "Profissão"), 
                                   show="headings", 
                                   style="Estilo.Treeview")
        
        # Define os cabeçalhos das colunas, especificando o texto que 
                # aparecerá em cada cabeçalho.
        # 'self.tabela.heading("Nome", text="Nome")' configura o cabeçalho 
                # da coluna 'Nome' para mostrar o texto 'Nome'.
        self.tabela.heading("Nome", text="Nome")

        # Repete o processo para as colunas 'Idade' e 'Profissão'.
        self.tabela.heading("Idade", text="Idade")
        self.tabela.heading("Profissão", text="Profissão")
        
        # Configura a tabela para preencher completamente o espaço horizontal ('fill="both"') 
                # do 'quadro' e expandir conforme necessário ('expand=True').
        # Isso significa que a tabela se ajustará para ocupar o máximo de espaço 
                # possível dentro do 'quadro', tanto na largura quanto na altura.
        self.tabela.pack(fill="both", expand=True)


        # Define um novo estilo para customizar a aparência da tabela, 
                # aumentando a legibilidade.
        # Cria um objeto 'Style', que permite configurar estilos 
                # de widgets no tkinter.
        estilo = ttk.Style()
        
        # Configura o estilo para as linhas normais da tabela 'Treeview'.
        # 'font=("tahoma", 20)' define a fonte das linhas como Tahoma 
                # tamanho 20, aumentando a legibilidade.
        # 'rowheight=30' define a altura de cada linha da tabela em 30 
                # pixels, proporcionando mais espaço entre as linhas.
        estilo.configure("Estilo.Treeview", 
                         font=("tahoma", 20), 
                         rowheight=30)

        # Configura o estilo para os cabeçalhos das colunas da tabela 'Treeview'.
        # 'font=("tahoma", 20, "bold")' define a fonte dos cabeçalhos como 
                # Tahoma tamanho 20 e em negrito, destacando-os das linhas normais.
        estilo.configure("Estilo.Treeview.Heading", 
                         font=("tahoma", 20, "bold"))
        
        # Cria uma lista de tuplas contendo dados fictícios para 
                # inserir na tabela.
        # Cada tupla representa uma linha da tabela, com elementos 
                # correspondendo às colunas 'Nome', 'Idade' e 'Profissão'.
        dados = [
            ("Carlos", 34, "Engenheiro"),
            ("Ana", 28, "Médica"),
            ("Pedro", 45, "Professor"),
            ("Maria", 23, "Estudante"),
            ("Cesar", 30, "Enfermeiro"),
            ("Paulo", 23, "Médico"),
        ]
        
        # Itera sobre cada item na lista 'dados'.
        for item in dados:
            
            # Insere cada item como uma nova linha na tabela.
            # '' indica que a linha será adicionada na raiz da árvore 
                    # de dados da tabela.
            # 'end' especifica que o novo item deve ser adicionado no 
                    # final da lista de itens existentes.
            # 'values=item' passa os valores das colunas para a linha 
                    # que está sendo inserida.
            self.tabela.insert("", 
                               "end", 
                               values=item)
        
        # Configura um evento que será acionado quando o mouse se mover sobre a tabela.
        # '<Motion>' é o evento que detecta qualquer movimento do mouse sobre o widget.
        # 'self.ao_mover_mouse' é o método que será chamado cada vez 
                # que o evento de movimento do mouse ocorrer.
        self.tabela.bind("<Motion>", self.ao_mover_mouse)

        # Inicializa a variável 'self.caixa_dica' como None. Esta variável 
                # será usada para controlar a exibição das caixas de dica.
        self.caixa_dica = None


    # Define o método que é chamado sempre que o mouse se move sobre a tabela.
    def ao_mover_mouse(self, evento):
        
        # Identifica a linha da tabela onde o mouse está posicionado 
                # usando a coordenada y do evento.
        id_linha = self.tabela.identify_row(evento.y)
        
        # Verifica se algum ID de linha foi identificado (o mouse 
                # está sobre uma linha válida da tabela).
        if id_linha:
            
            # Obtém o item (linha) da tabela correspondente ao ID identificado.
            item = self.tabela.item(id_linha)
            
            # Extrai os valores armazenados na linha (nome, idade, profissão).
            valores = item['values']
            
            # Prepara o texto que será exibido na caixa de dica, 
                    # formatado com informações da linha.
            texto_dica = f"Nome: {valores[0]}\nIdade: {valores[1]}\nProfissão: {valores[2]}"
            
            # Obtém a posição e dimensão da linha dentro da tabela para 
                    # posicionar corretamente a caixa de dica.
            x, y, largura, altura = self.tabela.bbox(id_linha)
            
            # Verifica se uma caixa de dica (tooltip) já foi criada e 
                    # está sendo exibida.
            if not self.caixa_dica:
                
                # Se o valor de 'self.caixa_dica' é None (não existe uma 
                        # caixa de dica ativa), então não há uma caixa de 
                        # dica atualmente em exibição.
            
                # Cria uma nova instância da classe 'CaixaDeDica'. Passa o 
                        # widget 'self.tabela' (a tabela onde a caixa de dica será exibida)
                        # e o texto formatado 'texto_dica' que contém informações da 
                        # linha da tabela onde o mouse está posicionado.
                self.caixa_dica = CaixaDeDica(self.tabela, 
                                              texto=texto_dica)
            
                # Chama o método 'mostrar_dica' no objeto 'self.caixa_dica' 
                        # para exibir a caixa de dica.
                # 'evento.x_root + 20' e 'evento.y_root + 20' calculam a posição 
                        # onde a caixa de dica será mostrada.
                # 'evento.x_root' e 'evento.y_root' são as coordenadas absolutas do 
                        # mouse na tela; adicionando 20 pixels a esses valores,
                        # a caixa de dica é posicionada ligeiramente à direita e abaixo da 
                        # posição do cursor, evitando obstruir o elemento que o 
                        # usuário está tentando visualizar.
                self.caixa_dica.mostrar_dica(evento.x_root + 20, evento.y_root + 20)
            
            else:
                # Se 'self.caixa_dica' não é None, significa que já existe uma 
                        # caixa de dica criada e sendo exibida.
            
                # Antes de recriar e mostrar uma nova caixa de dica com informações 
                        # atualizadas, a caixa de dica atual é escondida.
                # Isso é importante para evitar sobreposições visuais desordenadas e 
                        # garantir que a interface permaneça limpa e compreensível.
                self.caixa_dica.esconder_dica()
            
                # Cria uma nova instância da classe 'CaixaDeDica' para atualizar a 
                        # caixa de dica com novo conteúdo.
                # Isso é feito para garantir que o conteúdo da caixa de dica reflita as 
                        # informações da linha atual sobre a qual o mouse está posicionado.
                self.caixa_dica = CaixaDeDica(self.tabela, texto=texto_dica)
            
                # Exibe a caixa de dica atualizada na posição calculada, deslocada da 
                        # posição atual do cursor.
                # Esse deslocamento é necessário para que a caixa de dica não apareça 
                        # diretamente sob o cursor do mouse, o que poderia impedir a 
                        # visualização do conteúdo.
                self.caixa_dica.mostrar_dica(evento.x_root + 20, evento.y_root + 20)

                
        else:
        # Este bloco é executado quando não há uma linha válida sob o cursor 
                    # do mouse. Ou seja, o mouse não está posicionado sobre 
                    # uma linha da tabela.
    
            # Verifica se uma caixa de dica (tooltip) está atualmente 
                    # ativa (existe uma instância de 'self.caixa_dica').
            if self.caixa_dica:
                # Se 'self.caixa_dica' não é None, isso significa que há 
                        # uma caixa de dica sendo exibida na tela.
        
                # Chama o método 'esconder_dica' do objeto 'self.caixa_dica'.
                # Este método é responsável por fechar a janela da caixa de 
                        # dica e removê-la visualmente da interface do usuário.
                # A ação de esconder a caixa é importante para evitar que 
                        # informações irrelevantes ou desatualizadas permaneçam na tela,
                        # o que poderia confundir o usuário ou sobrecarregar visualmente a interface.
                self.caixa_dica.esconder_dica()
        
                # Define 'self.caixa_dica' como None.
                # Essa atribuição limpa a referência ao objeto da caixa de dica, 
                        # indicando que não há mais uma caixa de dica ativa.
                # Resetar 'self.caixa_dica' para None é crucial para controlar 
                        # corretamente o estado da interface,
                        # permitindo que uma nova caixa de dica seja criada quando 
                        # necessário sem interferência de uma antiga instância.
                self.caixa_dica = None


# Cria um objeto 'raiz' que será a janela principal da aplicação. 'Tk()' é 
        # um construtor da classe Tk, parte do módulo tkinter.
# Este objeto 'raiz' serve como a janela principal onde todos os 
        # widgets (componentes da interface gráfica) serão organizados.
raiz = tk.Tk()

# Cria uma instância da classe 'TabelaComCaixaDeDica'. Essa classe foi 
        # definida anteriormente e é responsável por criar uma interface
# que inclui uma tabela com informações e caixas de dica que aparecem quando o 
        # usuário move o mouse sobre as linhas da tabela.
# 'raiz' é passado como argumento para o construtor da classe 
        # 'TabelaComCaixaDeDica', designando-o como o widget pai para 
        # todos os elementos GUI criados dentro desta classe.
app = TabelaComCaixaDeDica(raiz)

# Inicia o loop principal da interface gráfica. 'mainloop()' é um 
        # método da classe 'Tk' que precisa ser chamado para que a janela
        # fique visível e comece a responder a eventos, como cliques do mouse 
        # ou pressionamentos de teclas.
raiz.mainloop()