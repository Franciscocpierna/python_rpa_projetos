# Importa o módulo tkinter e o renomeia como 'tk' para facilitar 
        # seu uso ao longo do código.
import tkinter as tk

# Importa o módulo 'ttk' de 'tkinter', que fornece acesso a widgets 
        # temáticos que melhoram a aparência dos widgets padrão do Tkinter.
from tkinter import ttk

# Importa o módulo 'pandas', uma poderosa biblioteca para manipulação e 
        # análise de dados em Python. Renomeada como 'pd' para simplificar seu uso.
import pandas as pd


# Define o caminho do arquivo Excel que contém os dados. 
        # 'notas_estudantes.xlsx' é o nome do arquivo.
arquivo_excel = 'notas_estudantes.xlsx'

# Carrega os dados do arquivo Excel especificado na 
        # variável 'arquivo_excel'. 
# 'sheet_name='Dados'' especifica que a planilha (sheet) de 
        # interesse dentro do arquivo Excel se chama 'Dados'.
# A função 'read_excel()' de pandas lê a planilha e carrega seus 
        # dados em um DataFrame chamado 'df'.
df = pd.read_excel(arquivo_excel, sheet_name='Dados')


# Função para sincronizar a rolagem vertical entre duas tabelas: a 
        # tabela principal e a tabela congelada.
def sincronizar_rolagem(*args):
    
    # A função 'sincronizar_rolagem' é chamada automaticamente 
            # sempre que o usuário interage com o scrollbar vertical.
    # O parâmetro '*args' captura todos os argumentos passados pelo 
            # evento de rolagem, que incluem informações
            # sobre a posição atual da rolagem e o tipo de evento que ocorreu.

    # A linha abaixo ajusta a rolagem vertical da tabela principal 
            # (que contém todas as colunas, exceto a primeira).
    # A função 'yview' é usada para controlar a posição da rolagem 
            # vertical da tabela. Ela recebe os argumentos
            # passados pelo evento de rolagem para determinar 
            # como a tabela deve ser rolada.
    tabela.yview(*args)

    # Esta linha faz o mesmo para a tabela congelada (que contém 
            # apenas a primeira coluna).
    # Ao chamar 'yview' com os mesmos argumentos, a rolagem da 
            # tabela congelada é sincronizada com a rolagem
            # da tabela principal, garantindo que ambas se 
            # movam juntas quando o scrollbar é usado.
    tabela_congelada.yview(*args)



# Função que configura e exibe a interface gráfica 
        # principal do projeto.
def criar_interface():
    
    # Cria a janela principal da aplicação utilizando a biblioteca tkinter.
    janela = tk.Tk()
    
    # Configura o título da janela, que aparecerá na barra de 
            # título da janela do sistema operacional.
    janela.title("Projeto de Notas dos Estudantes")
    
    # Define as dimensões iniciais da janela. '800x600' estabelece a 
            # largura de 800 pixels e altura de 600 pixels.
    janela.geometry("800x600")


    # Cria um rótulo (Label) que será usado para exibir o título 
            # do projeto dentro da janela.
    label_titulo = tk.Label(janela, 
                            
                            # 'text="Notas dos Estudantes"' define o texto 
                                    # que será mostrado no rótulo.
                            text="Notas dos Estudantes", 
                            
                            # 'font=("Arial", 16)' especifica a fonte do 
                                    # texto, usando Arial tamanho 16 e estilo normal.
                            font=("Arial", 16))
    
    # Empacota o rótulo dentro da janela, o que o torna visível.
    # 'pack()' é um gerenciador de geometria que organiza os widgets em 
            # blocos antes de colocá-los na janela.
    # 'pady=10' adiciona 10 pixels de espaço vertical acima e abaixo do 
            # rótulo para dar um espaçamento agradável.
    label_titulo.pack(pady=10)


    # Criando o Frame principal
    # Cria um Frame que atuará como o contêiner principal para todos os 
            # outros widgets dentro da janela principal.
    frame_principal = tk.Frame(janela)

    # Empacota o frame principal na janela, configurando-o para expandir e 
            # preencher todo o espaço disponível.
    # 'fill=tk.BOTH' indica que o frame deve se expandir tanto vertical 
            # quanto horizontalmente.
    # 'expand=True' faz com que o frame ocupe qualquer espaço extra na 
            # janela para garantir que utilize toda a área disponível.
    frame_principal.pack(fill=tk.BOTH, expand=True)
    
    # Criando o Frame para a primeira coluna congelada
    # Cria um Frame dentro do frame principal que será usado para 
            # manter a primeira coluna da tabela sempre visível enquanto o 
            # usuário rola as demais colunas.
    frame_congelado = tk.Frame(frame_principal)

    # Empacota o frame congelado à esquerda do frame principal.
    # 'side=tk.LEFT' coloca o frame no lado esquerdo, e 'fill=tk.Y' faz 
            # com que ele se expanda verticalmente, ocupando todo o 
            # espaço vertical disponível.
    frame_congelado.pack(side=tk.LEFT, fill=tk.Y)
    
    # Criando o Frame para o restante da tabela
    # Cria outro Frame dentro do frame principal que conterá o restante 
            # da tabela, permitindo a rolagem independente das colunas 
            # que não estão congeladas.
    frame_tabela = tk.Frame(frame_principal)

    # Empacota este frame à direita, preenchendo tanto vertical 
            # quanto horizontalmente o espaço restante.
    # 'side=tk.RIGHT' coloca o frame no lado direito do 
            # frame principal.
    # 'fill=tk.BOTH' e 'expand=True' garantem que ele se expanda 
            # em ambas as direções para utilizar todo o espaço disponível.
    frame_tabela.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)


    # Define quais colunas serão congeladas. Neste caso, apenas a 
            # primeira coluna do DataFrame é selecionada.
    # 'df.columns[0]' acessa o nome da primeira coluna do 
            # DataFrame 'df', que será usada como a coluna congelada.
    colunas_congeladas = [df.columns[0]]  # Primeira coluna
    
    # Declaração global para garantir que a variável 'tabela_congelada' 
            # possa ser acessada globalmente, especialmente útil se a 
            # função modificar seu conteúdo mais tarde.
    global tabela_congelada
    
    # Cria a tabela congelada usando o widget Treeview do módulo ttk, 
            # que é colocado dentro do frame designado para colunas congeladas.
    # 'frame_congelado' é o contêiner em que a tabela será colocada.
    # 'columns=colunas_congeladas' define as colunas que serão 
            # exibidas na tabela.
    # 'show='headings'' configura a tabela para mostrar apenas os 
            # cabeçalhos das colunas, sem a coluna índice padrão do Treeview.
    # 'height=20' define a altura da tabela para exibir 20 linhas simultaneamente.
    tabela_congelada = ttk.Treeview(frame_congelado, 
                                    columns=colunas_congeladas, 
                                    show='headings',
                                    height=20)
    
    # Empacota a tabela congelada dentro do frame congelado.
    # 'side=tk.LEFT' posiciona a tabela congelada no lado 
            # esquerdo do seu contêiner (frame_congelado).
    # 'fill=tk.Y' faz com que a tabela congelada expanda verticalmente 
            # para preencher todo o espaço vertical disponível, 
            # assegurando que acompanhe a altura do frame.
    tabela_congelada.pack(side=tk.LEFT, fill=tk.Y)


    # Este laço percorre a lista de colunas congeladas 
            # para configurar cada coluna na tabela congelada.
    for coluna in colunas_congeladas:
        
        # 'tabela_congelada.heading(coluna, text=coluna)' 
                # configura o cabeçalho da coluna.
        # 'coluna' é o nome da coluna a ser configurado.
        # 'text=coluna' define o texto do cabeçalho para 
                # ser o nome da coluna.
        tabela_congelada.heading(coluna, text=coluna)
    
        # 'tabela_congelada.column(coluna, width=120, anchor='center')' 
                # configura as propriedades da coluna.
        # 'width=120' define a largura da coluna para 120 pixels, o 
                # que assegura que haja espaço suficiente para exibir 
                # os dados de forma legível.
        # 'anchor='center'' alinha o texto dentro da coluna ao 
                # centro, melhorando a estética e a legibilidade dos dados.
        tabela_congelada.column(coluna, width=120, anchor='center')


    # Este laço itera sobre cada linha do DataFrame 'df' para 
            # inserir os dados na primeira coluna congelada.
    for indice, linha in df.iterrows():
        
        # 'df.iterrows()' gera um iterador que retorna o índice 
                # da linha e a linha como uma série de dados.
        # 'tabela_congelada.insert("", tk.END, values=(linha[coluna],))' 
                # insere uma nova linha na tabela congelada.
        # '""' e 'tk.END' indicam que o novo item será adicionado ao 
                # final da lista de itens na tabela.
        # 'values=(linha[coluna],)' pega o valor da coluna especificada 
                # da linha atual e cria uma tupla com ele.
        # Isso garante que apenas os dados da coluna congelada sejam 
                # exibidos nesta parte da tabela.
        tabela_congelada.insert("", tk.END, values=(linha[coluna],))


    # Cria um Scrollbar vertical para a tabela principal, 
            # permitindo a rolagem dos dados verticalmente.
    scrollbar_vertical = ttk.Scrollbar(frame_tabela, 
                                       
                                       # 'orient="vertical"' define a orientação do 
                                               # scrollbar como vertical.
                                       orient="vertical", 
                                       
                                       # 'command=sincronizar_rolagem' vincula o comando 
                                               # de rolagem ao scrollbar,
                                               # que chama a função 'sincronizar_rolagem' 
                                               # para sincronizar a rolagem entre as duas tabelas.
                                       command=sincronizar_rolagem)
    
    # Empacota o scrollbar no lado direito do frame da tabela 
            # principal e o estende verticalmente.
    scrollbar_vertical.pack(side=tk.RIGHT, 
                            
                            # 'side=tk.RIGHT' posiciona o scrollbar no lado 
                                    # direito dentro do seu contêiner.
                            fill=tk.Y)
                            # 'fill=tk.Y' faz com que o scrollbar preencha 
                                    # todo o espaço vertical disponível no seu contêiner.


    # Define quais colunas serão exibidas na tabela principal, 
            # selecionando todas exceto a primeira.
    colunas_tabela = list(df.columns[1:])  # Demais colunas
    
    # Declaração global para a tabela principal para que possa 
            # ser acessada ou modificada globalmente.
    global tabela
    
    # Cria a tabela principal usando o widget Treeview do módulo ttk, 
            # colocada dentro do frame da tabela.
    tabela = ttk.Treeview(frame_tabela, 
                          
                          # 'columns=colunas_tabela' define as colunas que 
                                  # serão exibidas na tabela.
                          columns=colunas_tabela, 
                          
                          # 'show='headings'' configura a tabela para mostrar apenas os 
                                  # cabeçalhos das colunas, sem a coluna de índice.
                          show='headings', 
                          
                          # 'height=20' define a altura da tabela para 
                                  # exibir 20 linhas de uma vez.
                          height=20)
    
    # Empacota a tabela no lado esquerdo do frame da tabela principal, 
            # preenchendo tanto vertical quanto horizontalmente o espaço disponível.
    tabela.pack(side=tk.LEFT, 
                
                # 'side=tk.LEFT' posiciona a tabela no lado esquerdo 
                        # dentro do seu contêiner.
                fill=tk.BOTH, 
                
                # 'fill=tk.BOTH' faz com que a tabela se expanda em ambas as 
                        # direções (vertical e horizontal) para preencher 
                        # todo o espaço disponível.
                expand=True)
                # 'expand=True' indica que a tabela deve ocupar qualquer espaço 
                        # extra disponível no layout para garantir que 
                        # utilize toda a área disponível.


    # Este laço percorre a lista de colunas que serão exibidas na 
            # tabela principal, definindo suas propriedades.
    for coluna in colunas_tabela:
        
        # Configura o cabeçalho de cada coluna na tabela principal.
        # 'tabela.heading(coluna, text=coluna)' define o texto do 
                # cabeçalho da coluna como o nome da coluna do DataFrame.
        # 'coluna' representa o nome da coluna atual que está sendo configurada.
        tabela.heading(coluna, text=coluna)
    
        # Configura as propriedades de exibição de cada coluna.
        # 'tabela.column(coluna, width=100, anchor='center')' define a 
                # largura da coluna e alinha o texto no centro.
        # 'width=100' define a largura da coluna como 100 pixels, garantindo que 
                # cada coluna tenha espaço suficiente para exibir os dados.
        # 'anchor='center'' alinha o conteúdo da coluna ao centro, 
                # proporcionando uma apresentação visualmente equilibrada e agradável.
        tabela.column(coluna, width=100, anchor='center')


    # Este laço percorre cada linha do DataFrame 'df' para inserir os 
            # dados nas colunas restantes da tabela principal.
    for indice, linha in df.iterrows():
        
        # 'df.iterrows()' é um gerador que retorna tanto o índice da 
                # linha quanto a linha em si, representada como uma série pandas.
        # 'linha' contém os dados de uma linha específica do DataFrame.
    
        # Cria uma tupla com os valores das colunas selecionadas 
                # para a tabela principal.
        # 'tuple(linha[coluna] for coluna in colunas_tabela)' gera 
                # uma tupla contendo os valores de cada coluna na linha atual.
        # 'colunas_tabela' contém os nomes das colunas restantes (todas 
                # as colunas, exceto a primeira).
        valores = tuple(linha[coluna] for coluna in colunas_tabela)
    
        # Insere uma nova linha na tabela principal com os valores 
                # extraídos do DataFrame.
        # 'tabela.insert("", tk.END, values=valores)' adiciona uma 
                # nova linha à tabela.
        # O primeiro argumento '""' indica que a nova linha não tem 
                # um pai, tornando-a uma linha raiz.
        # 'tk.END' especifica que a linha deve ser inserida no final da tabela.
        # 'values=valores' atribui os valores da tupla criada 
                # anteriormente à nova linha na tabela.
        tabela.insert("", tk.END, values=valores)


    # Configura a tabela principal para usar o scrollbar vertical.
    # 'yscrollcommand=scrollbar_vertical.set' vincula o scrollbar 
            # vertical à tabela principal, garantindo que ele 
            # controle a rolagem vertical da tabela.
    tabela.configure(yscrollcommand=scrollbar_vertical.set)
    
    # Configura a tabela congelada (primeira coluna) para 
            # usar o mesmo scrollbar vertical.
    # 'yscrollcommand=scrollbar_vertical.set' assegura que o 
            # scrollbar vertical controle simultaneamente a 
            # rolagem vertical da tabela congelada.
    tabela_congelada.configure(yscrollcommand=scrollbar_vertical.set)


    # Cria um scrollbar horizontal para a tabela principal, 
            # permitindo a rolagem dos dados horizontalmente.
    scrollbar_horizontal = ttk.Scrollbar(janela, 
                                         
                                         # 'orient="horizontal"' define a orientação do 
                                                 # scrollbar como horizontal.
                                         orient="horizontal", 
                                         
                                         # 'command=tabela.xview' vincula o comando de 
                                                 # rolagem horizontal à tabela principal,
                                                 # permitindo que o scrollbar controle a 
                                                 # rolagem horizontal da tabela.
                                         command=tabela.xview)
    
    # Empacota o scrollbar horizontal na parte inferior da janela principal.
    # 'side=tk.BOTTOM' posiciona o scrollbar na parte inferior da janela.
    # 'fill=tk.X' faz com que o scrollbar se estenda horizontalmente 
            # para preencher toda a largura da janela.
    scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Configura a tabela principal para usar o scrollbar horizontal.
    # 'xscrollcommand=scrollbar_horizontal.set' vincula o 
            # scrollbar horizontal à tabela principal,
            # garantindo que ele controle a rolagem horizontal da tabela.
    tabela.configure(xscrollcommand=scrollbar_horizontal.set)


    # Inicia o loop principal da interface gráfica Tkinter, permitindo 
            # que a janela e seus componentes respondam a eventos do usuário.
    # 'janela.mainloop()' mantém a janela aberta e interativa 
            # até que o usuário a feche manualmente.
    janela.mainloop()


# Executando a Interface
criar_interface()