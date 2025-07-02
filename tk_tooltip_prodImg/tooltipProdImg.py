# Importa o módulo tkinter para construção de interfaces gráficas. 
        # A sigla 'tk' é usada como alias para simplificar a chamada 
        # de funções deste módulo.
import tkinter as tk

# Importa o submódulo ttk do tkinter que fornece acesso a widgets temáticos 
        # que podem ser usados para construir interfaces mais atraentes.
from tkinter import ttk

# Importa o módulo pandas, uma poderosa biblioteca para manipulação de 
        # dados. 'pd' é usado como alias para simplificar seu uso.
import pandas as pd

# Importa a biblioteca Pillow para operações com imagens. 'Image' é usado 
        # para abrir/criar imagens e 'ImageTk' para integrar imagens Pillow ao tkinter.
from PIL import Image, ImageTk

# Importa o módulo os para interagir com o sistema operacional, especialmente 
        # para manipulação de caminhos de arquivos e diretórios.
import os
import unicodedata

def formatar_nome_arquivo(nome_produto):
    # Remove acentos
    nome = unicodedata.normalize('NFKD', nome_produto).encode('ASCII', 'ignore').decode('ASCII')
    
    # Substitui espaços por +
    nome = nome.replace(" ", "+")
 
    # Remove outros caracteres problemáticos (opcional)
    nome = ''.join(c for c in nome if c.isalnum() or c in ['+', '-', '_'])
 
    return f"{nome}.jpg"
# Define uma função chamada 'carregar_dados' que não recebe 
        # nenhum parâmetro externo.
def carregar_dados():
    
    # Carrega um arquivo Excel chamado 'Vendedor.xlsx', especificamente a 
            # aba 'Dados', em um DataFrame pandas.
    # A função 'read_excel' do pandas é usada aqui para ler o arquivo Excel.
    df = pd.read_excel('C:\\python_projetos\\python_rpa_projetos\\tk_tooltip_prodImg\\Vendedor.xlsx', sheet_name='Dados')
    
    # Atualiza a coluna 'Total' do DataFrame para formatar os valores 
            # financeiros em formato de real brasileiro.
    # A função 'apply' é usada para aplicar uma função lambda a 
            # cada elemento da coluna 'Total'.
    # A função lambda formata cada valor 'x' como um valor monetário, 
            # primeiro formatando 'x' como uma string com duas casas 
            # decimais e separador de milhar, em seguida, substituindo vírgulas 
            # por 'v', pontos por vírgulas (adequando ao formato brasileiro), e 
            # finalmente substituindo 'v' por ponto.
    df['Total'] = df['Total'].apply(lambda x: f"R$ {x:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.'))
    
    # Retorna o DataFrame 'df' com os dados carregados e a 
            # coluna 'Total' já formatada.
    return df


# Define a função 'filtrar_dados' que aceita argumentos 
        # arbitrários (não usados explicitamente na função).
def filtrar_dados(*args):
    
    # Obtém o texto do campo de entrada associado ao filtro de 
            # vendedor, converte para minúsculas para padronizar a comparação.
    filtro_vendedor = entrada_filtro_vendedor.get().lower()
    
    # Obtém o texto do campo de entrada associado ao filtro de 
            # produto, também convertendo para minúsculas.
    filtro_produto = entrada_filtro_produto.get().lower()
    
    # Obtém o texto do campo de entrada associado ao filtro de 
            # total, e converte para minúsculas.
    filtro_total = entrada_filtro_total.get().lower()
    
    # Filtra o DataFrame 'df' com base nos textos inseridos nos campos de filtro.
    # 'df['Vendedor'].str.lower().str.contains(filtro_vendedor)' 
            # verifica se a coluna 'Vendedor', em minúsculas,
            # contém a string fornecida no filtro de vendedor.
    # 'df['Produto'].str.lower().str.contains(filtro_produto)' faz o 
            # mesmo para a coluna 'Produto'.
    # 'df['Total'].astype(str).str.lower().str.contains(filtro_total)' 
            # converte a coluna 'Total' para string, coloca em minúsculas,
            # e verifica se contém a string de filtro para total.
    # O operador '&' é usado para garantir que todos os critérios 
            # de filtro sejam verdadeiros simultaneamente.
    dados_filtrados = df[
        df['Vendedor'].str.lower().str.contains(filtro_vendedor) &
        df['Produto'].str.lower().str.contains(filtro_produto) &
        df['Total'].astype(str).str.lower().str.contains(filtro_total)
    ]
    
    # Chama a função 'atualizar_tabela' passando o DataFrame 
            # 'dados_filtrados' como argumento.
    # Essa função será responsável por atualizar a visualização da 
            # tabela com os dados que atendem aos critérios de filtro.
    atualizar_tabela(dados_filtrados)


# Define a função 'atualizar_tabela' que aceita um parâmetro 'dados', 
        # que é um DataFrame do pandas contendo os dados que 
        # devem ser exibidos na tabela.
def atualizar_tabela(dados):
    
    # Inicia um loop que itera sobre todos os itens (linhas) 
            # atualmente presentes na tabela.
    # 'tabela.get_children()' retorna uma lista de identificadores de 
            # todos os itens que estão atualmente na tabela.
    for item in tabela.get_children():
        
        # 'tabela.delete(item)' remove o item (linha) especificado da 
                # tabela. Este passo limpa a tabela antes de adicionar 
                # os novos dados filtrados.
        tabela.delete(item)
    
    # Inicia um segundo loop que itera sobre cada linha do DataFrame 'dados'.
    # 'dados.iterrows()' retorna um iterador que gera pares de índice e a 
            # linha correspondente do DataFrame como uma série.
    for index, row in dados.iterrows():
        
        # 'tabela.insert('', 'end', values=(row['Vendedor'], row['Produto'], row['Total']))' 
                # adiciona uma nova linha ao final da tabela.
        # O primeiro argumento '' indica que a linha é adicionada na 
                # raiz da árvore de dados da tabela.
        # O segundo argumento 'end' especifica que a nova linha deve ser 
                # colocada no final da lista de itens existentes.
        # O argumento 'values' define os valores que devem ser colocados em 
                # cada coluna da nova linha; estes são tirados da linha atual do DataFrame.
        tabela.insert('', 'end', 
                    values=(row['Vendedor'], 
                    row['Produto'], 
                    row['Total']))


# Define a função que mostra informações adicionais quando o 
        # usuário passa o mouse sobre uma linha da tabela.
def exibir_tooltip(evento):
    
    # Identifica a linha da tabela onde o mouse está posicionado 
            # usando a coordenada y do evento.
    id_linha = tabela.identify_row(evento.y)
    
    # Verifica se um identificador de linha foi encontrado (ou seja, 
            # se o mouse está sobre uma linha da tabela).
    if id_linha:
        
        # Obtém os dados da linha identificada.
        item = tabela.item(id_linha)
        
        # Recupera os valores armazenados na linha, que são: 
                # vendedor, produto e total.
        valores = item['values']
        
        # Desempacota os valores nas respectivas variáveis.
        vendedor, produto, total = valores
        nome = formatar_nome_arquivo(produto)
        ##
        
        
        ##

        # Define o caminho para o arquivo de imagem do produto, utilizando o 
                # nome do produto para localizar a imagem correspondente no diretório 'imagem'.
        # A função 'os.path.join' é utilizada para construir o caminho do 
                # arquivo de forma que seja compatível com qualquer sistema operacional.
        #caminho_imagem = os.path.join('imagem', f"{produto}.jpg")
        caminho_imagem = os.path.join('C:\\python_projetos\\python_rpa_projetos\\tk_tooltip_prodImg\\imagem', nome )
        #f"{produto}.jpg"
         #Vestido+Infantil 
        
        # Verifica se o arquivo de imagem existe no caminho especificado.
        # A função 'os.path.exists' retorna True se o arquivo existir, garantindo 
                # que o código seguinte só será executado se houver uma imagem correspondente.
        if os.path.exists(caminho_imagem):
        
            # Abre a imagem utilizando a biblioteca Pillow (PIL). A função 
                    # 'Image.open' carrega a imagem do disco para a memória.
            #imagem = Image.open(caminho_imagem)
            imagem = Image.open(caminho_imagem)
            
            #Vestido Infantil.jpg
            # Redimensiona a imagem para as dimensões de 200x200 pixels. 
            # 'Image.Resampling.LANCZOS' é especificado como o método de resampling, 
                    # que é um dos métodos de alta qualidade para redimensionar imagens,
                    # proporcionando resultados visuais superiores para imagens redimensionadas.
            imagem = imagem.resize((200, 200), Image.Resampling.LANCZOS)
            
            # Converte a imagem do formato Pillow para um formato compatível com 
                    # Tkinter, para que possa ser exibida em um widget de imagem.
            # 'ImageTk.PhotoImage' cria um objeto de imagem Tkinter a 
                    # partir da imagem Pillow.
            imagem_tk = ImageTk.PhotoImage(imagem)
            
            # Configura o widget 'label_imagem' para exibir a imagem redimensionada.
            # O método 'config' é usado para definir a propriedade 'image' 
                    # do widget de label, permitindo a exibição da imagem.
            label_imagem.config(image=imagem_tk)
            
            # Armazena uma referência à imagem em uma propriedade do widget 'label_imagem'.
            # Isso é necessário porque o Tkinter não mantém uma 
                    # referência interna às imagens,
            # o que pode fazer com que elas sejam coletadas como lixo se 
                    # não forem explicitamente retidas.
            label_imagem.image = imagem_tk
            
        else:
            
            # Configura o widget 'label_imagem' para não mostrar nenhuma 
                    # imagem e exibir uma mensagem de erro,
            # informando que a imagem correspondente ao produto não foi encontrada.
            # Isso é útil para informar ao usuário que a visualização 
                    # da imagem não está disponível.
            label_imagem.config(image='', text="Imagem não encontrada")


        # Atualiza o texto do tooltip com as informações da linha 
                # sobre a qual o mouse está posicionado.
        # Aqui, é criada uma string formatada contendo o nome do 
                # vendedor, o produto e o total da transação.
        # Essa string é preparada para ser exibida no tooltip.
        texto_tooltip = f"Vendedor: {vendedor}\nProduto: {produto}\nTotal: {total}"
        
        # Configura o widget 'label_tooltip' para exibir o texto formatado.
        # O método 'config' é usado para alterar a configuração de 
                # texto do widget de label, neste caso, atualizando o texto exibido.
        label_tooltip.config(text=texto_tooltip)
        
        # Ajusta a posição do tooltip para que ele seja exibido próximo 
                # ao cursor, mas ligeiramente deslocado.
        # O método 'wm_geometry' define a geometria da janela do 
                # tooltip, especificando sua posição relativa.
        # Aqui, 'evento.x_root + 10' e 'evento.y_root + 10' calculam a 
                # posição do tooltip para que apareça 10 pixels à direita
        # e 10 pixels abaixo da posição atual do cursor do mouse. Isso ajuda a 
                # evitar que o tooltip obstrua a visão do cursor ou do conteúdo sob ele.
        tooltip.wm_geometry(f"+{evento.x_root + 10}+{evento.y_root + 10}")
        
        # Torna o tooltip visível caso ele esteja oculto.
        # O método 'deiconify' é usado para exibir o tooltip, tornando-o 
                # visível na tela caso esteja oculto.
        # Isso é útil porque o tooltip pode ser configurado para se 
                # esconder ('withdraw') quando o mouse sai da tabela,
                # então ele precisa ser explicitamente tornado visível novamente 
                # quando o mouse se move sobre uma nova linha.
        tooltip.deiconify()


# Define a função responsável por ocultar o tooltip.
def ocultar_tooltip(evento):
    
    # Utiliza o método 'withdraw' para esconder a janela 'tooltip'. Este 
            # método é usado para ocultar temporariamente o tooltip sem destruí-lo,
    # permitindo que seja reexibido rapidamente quando necessário.
    tooltip.withdraw()
    
    

# Cria a janela principal da aplicação usando o Tkinter.
janela = tk.Tk()

# Configura o título da janela principal, que aparecerá na 
        # barra de título da janela.
janela.title("Tabela de Vendas")

# Chama a função 'carregar_dados' para carregar os dados de vendas a 
        # partir de um arquivo Excel e armazená-los em um DataFrame pandas.
df = carregar_dados()

# Define as configurações de fonte que serão usadas nos widgets da 
        # interface. 'fonte_padrao' é usada para texto regular,
        # enquanto 'fonte_tooltip' é usada para o texto exibido nos 
        # tooltips, sendo um pouco maior e em negrito para destaque.
fonte_padrao = ("Arial", 12)
fonte_tooltip = ("Arial", 14, "bold")

# Cria um frame dentro da janela principal para conter os campos de 
        # filtro. Um frame é um container que agrupa elementos visuais.
filtros_frame = tk.Frame(janela)

# Empacota o frame na janela principal. O parâmetro 'fill='x'' faz com 
        # que o frame se expanda horizontalmente para preencher toda a largura da janela,
        # ajudando a organizar visualmente os campos de filtro em uma única linha.
filtros_frame.pack(fill='x')


# Cria um rótulo (label) no 'filtros_frame' com o texto "Filtrar por 
        # Vendedor:". Este rótulo serve como uma descrição para o campo 
        # de entrada que virá a seguir.
# 'font=fonte_padrao' define a fonte do texto do rótulo conforme a 
        # variável 'fonte_padrao' especificada anteriormente.
tk.Label(filtros_frame, text="Filtrar por Vendedor:", font=fonte_padrao).grid(row=0, column=0, padx=5, pady=5)
# Configura a posição do rótulo na grid (grade) do 'filtros_frame'. 'row=0' e 'column=0' 
        # colocam o rótulo na primeira linha e na primeira coluna.
# 'padx=5' e 'pady=5' adicionam um espaçamento interno de 5 pixels em todas as 
        # direções ao redor do rótulo para evitar que o texto fique muito 
        # justo aos bordos do frame.

# Cria um campo de entrada (Entry) para o usuário inserir o filtro por vendedor.
entrada_filtro_vendedor = tk.Entry(filtros_frame, 
                                   font=fonte_padrao)

# Posiciona o campo de entrada na grid do 'filtros_frame'. 'row=0' e 'column=1' 
        # colocam o campo de entrada na primeira linha e segunda coluna.
entrada_filtro_vendedor.grid(row=0, 
                             column=1, 
                             padx=5, 
                             pady=5)

# Associa um evento de liberação de tecla (quando o usuário solta 
        # uma tecla) ao campo de entrada.
# 'filtrar_dados' é a função chamada sempre que uma tecla é liberada, 
        # permitindo filtrar os dados dinamicamente conforme o usuário digita.
entrada_filtro_vendedor.bind('<KeyRelease>', filtrar_dados)


# Cria um rótulo no frame de filtros, especificamente para orientar o 
        # usuário onde filtrar por produtos.
tk.Label(filtros_frame, text="Filtrar por Produto:", 
                 font=fonte_padrao).grid(row=0, column=2, padx=5, pady=5)
# .grid(row=0, column=2, padx=5, pady=5): Posiciona o 
        # rótulo na grid do frame de filtros.
# 'row=0' coloca o rótulo na primeira linha.
# 'column=2' coloca o rótulo na terceira coluna, ajustando a 
        # posição horizontal.
# 'padx=5' e 'pady=5' adicionam um espaço de 5 pixels ao redor 
        # do rótulo para não ficar visualmente apertado.

# Cria um campo de entrada (Entry) para o usuário inserir o 
        # termo de busca que filtrará a lista de produtos.
entrada_filtro_produto = tk.Entry(filtros_frame, font=fonte_padrao)
# .grid(row=0, column=3, padx=5, pady=5): Posiciona o campo 
        # de entrada ao lado do rótulo na mesma linha.
# 'row=0' indica que está na primeira linha, alinhado com o rótulo.
# 'column=3' coloca o campo de entrada na quarta coluna.
# 'padx=5' e 'pady=5' garantem o mesmo espaçamento ao redor do 
        # campo de entrada, mantendo a consistência visual.

# Posiciona o campo de entrada 'entrada_filtro_produto' na 
        # grade do frame 'filtros_frame'.
entrada_filtro_produto.grid(row=0, column=3, padx=5, pady=5)
# 'row=0' coloca o campo de entrada na primeira linha do grid, 
        # garantindo que ele fique alinhado horizontalmente com 
        # os rótulos e outros campos de entrada.
# 'column=3' coloca o campo de entrada na quarta coluna, imediatamente 
        # após o rótulo "Filtrar por Produto", para que o rótulo e o 
        # campo de entrada estejam próximos, facilitando a associação 
        # visual pelo usuário.
# 'padx=5' e 'pady=5' adicionam um padding de 5 pixels tanto na 
        # horizontal (padx) quanto na vertical (pady). Isso evita que o 
        # campo de entrada fique visualmente colado aos elementos ao seu 
        # redor, melhorando a estética e tornando a interface mais fácil de usar.

# Associa um evento de liberação de tecla (quando o usuário solta 
        # uma tecla) ao campo de entrada.
# '<KeyRelease>': Evento que ocorre quando uma tecla pressionada é liberada.
# 'filtrar_dados': Função que é chamada sempre que o evento ocorre, 
        # permitindo filtrar os dados dinamicamente conforme o usuário digita.
entrada_filtro_produto.bind('<KeyRelease>', filtrar_dados)



# Cria um rótulo (Label) no frame de filtros (filtros_frame) 
        # com o texto "Filtrar por Total:".
# Este rótulo serve para indicar ao usuário que o campo de entrada ao 
        # lado é para inserir critérios de busca pelo valor total.
tk.Label(filtros_frame, 
                 text="Filtrar por Total:", 
                 font=fonte_padrao).grid(row=0, column=4, padx=5, pady=5)
    # A função .grid é utilizada para posicionar o rótulo na 
            # grade (grid layout) do frame de filtros:
    # - row=0: posiciona o rótulo na primeira linha da grade.
    # - column=4: posiciona o rótulo na quinta coluna (as colunas são 
            # contadas a partir do zero).
    # - padx=5 e pady=5: adicionam um padding (espaço) de 5 pixels em todas 
            # as direções ao redor do rótulo para garantir que o texto 
            # não fique apertado.
    

# Cria um campo de entrada (Entry) para que o usuário possa 
            # digitar o valor total que deseja filtrar na tabela.
entrada_filtro_total = tk.Entry(filtros_frame, 
                                font=fonte_padrao)

    
entrada_filtro_total.grid(row=0, column=5, padx=5, pady=5)
    # Posiciona o campo de entrada utilizando a função .grid 
            # dentro do frame de filtros:
    # - row=0: alinha o campo de entrada na mesma linha do rótulo, 
            # mantendo a consistência visual e facilitando a usabilidade.
    # - column=5: coloca o campo de entrada na sexta coluna, logo 
            # após o rótulo do filtro por total.
    # - padx=5 e pady=5: adicionam um espaço de 5 pixels ao redor do 
            # campo de entrada, evitando que ele fique muito colado a 
            # outros elementos, melhorando a estética e usabilidade.

# Associa um evento de liberação de tecla ao campo de entrada de total.
# Este evento é ativado cada vez que o usuário solta uma tecla ao 
            # digitar no campo de entrada, disparando a função de filtragem.
entrada_filtro_total.bind('<KeyRelease>', filtrar_dados)
    # '<KeyRelease>': o evento detectado é a liberação de uma tecla.
    # 'filtrar_dados': é a função chamada sempre que o evento ocorre. Ela 
            # executa o processo de filtragem baseado no que foi digitado nos 
            # campos de entrada, atualizando dinamicamente a visualização dos dados na tabela.


# Define as colunas que serão usadas na tabela.
colunas = ('Vendedor', 'Produto', 'Total')


# Cria uma tabela (TreeView) na janela principal 'janela', especificando as 
            # colunas, o estilo e configurando para mostrar apenas os 
            # cabeçalhos das colunas.
tabela = ttk.Treeview(janela, 
                      columns=colunas, 
                      show='headings', 
                      style="mystyle.Treeview")

    # 'columns=colunas' especifica as colunas que a tabela deve ter 
            # com base na tupla definida anteriormente.
    # 'show="headings"' configura a tabela para mostrar apenas os cabeçalhos, 
            # ou seja, não mostrará a coluna da árvore (primeira coluna de indentação).
    # 'style="mystyle.Treeview"' aplica um estilo personalizado que será 
            # configurado abaixo, para definir a aparência das linhas e cabeçalhos.
    # Empacota a tabela na janela para que ocupe todo o espaço disponível.
tabela.pack(fill='both', expand=True)
    # 'fill="both"' faz com que a tabela expanda tanto na horizontal quanto 
            # na vertical para ocupar todo o espaço disponível na janela.
    # 'expand=True' permite que a tabela expanda além do seu tamanho mínimo, 
            # ocupando qualquer espaço extra disponível na janela.

# Cria um objeto de estilo para customizar widgets de ttk.
style = ttk.Style()

# Configura o estilo 'mystyle.Treeview' para os elementos da tabela.
style.configure("mystyle.Treeview", 
                font=fonte_padrao, 
                rowheight=30)
    # 'font=fonte_padrao' define a fonte das linhas da tabela. A variável 
            # 'fonte_padrao' foi configurada anteriormente para definir o 
            # tipo e o tamanho da fonte.
    # 'rowheight=30' define a altura de cada linha da tabela em 30 pixels, 
            # proporcionando mais espaço entre as linhas para uma leitura mais confortável.

# Configura o estilo 'mystyle.Treeview.Heading' para os cabeçalhos das colunas da tabela.
style.configure("mystyle.Treeview.Heading", 
                font=("Arial", 14, "bold"))
    # 'font=("Arial", 14, "bold")' define a fonte dos cabeçalhos das 
            # colunas como Arial, tamanho 14 e em negrito, destacando-os das linhas da tabela.
    # Esta configuração faz com que os cabeçalhos sejam mais 
            # proeminentes e fáceis de identificar.


# Inicia um loop que percorre cada item na tupla 'colunas' que 
            # contém os nomes das colunas da tabela.
for col in colunas:
    
    # Configura o cabeçalho de cada coluna na tabela 'tabela'.
    # 'tabela.heading(col, text=col)': Define que o texto do cabeçalho 
                # de cada coluna será o nome da coluna correspondente.
    # 'col' é o identificador da coluna e 'text=col' define o texto do 
                # cabeçalho como o nome da coluna.
    tabela.heading(col, text=col)


# Criação de uma nova janela de nível superior que será usada como tooltip. 
            # Esta janela é associada à janela principal 'janela'.
tooltip = tk.Toplevel(janela)
    # 'tk.Toplevel(janela)': Cria um novo objeto de janela de nível superior 
            # que pode ser usado para diálogos, popups ou outras informações flutuantes.

# Inicialmente oculta o tooltip. Isso garante que o tooltip não 
            # apareça até que seja especificamente solicitado.
tooltip.withdraw()
    # 'withdraw()': Método que torna a janela 'tooltip' invisível a 
            # princípio. Ela será exibida somente quando necessário.

# Desativa a decoração da janela do tooltip, como a barra de título e 
            # bordas da janela, tornando-a uma janela flutuante limpa.
tooltip.overrideredirect(True)
    # 'overrideredirect(True)': Método que, quando configurado como True, 
            # faz com que a janela ignore o gerenciador de janelas.
    # Isso permite que a janela do tooltip seja exibida sem qualquer decoração de 
            # janela, como bordas ou barra de título, ideal para tooltips.


# Cria um frame dentro do objeto tooltip, que serve como container para os 
            # elementos dentro do tooltip.
tooltip_frame = tk.Frame(tooltip, 
                         bg='lightblue', 
                         relief='solid', 
                         borderwidth=2)
    # 'bg='lightblue'': Define a cor de fundo do frame como azul claro, 
            # proporcionando uma aparência distinta e agradável.
    # 'relief='solid'': Define o tipo de relevo do frame como sólido, o 
            # que dá ao frame uma borda visível e um pouco de profundidade visual.
    # 'borderwidth=2': Define a largura da borda do frame em 2 pixels, 
            # garantindo que as bordas sejam claramente visíveis.

# Empacota o frame dentro do tooltip para que ele ocupe todo o espaço 
            # disponível dentro do tooltip.
tooltip_frame.pack(fill='both', expand=True)
    # 'fill='both'': Especifica que o frame deve expandir tanto na horizontal 
            # quanto na vertical para preencher todo o espaço disponível 
            # no seu contêiner pai.
    # 'expand=True': Permite que o frame expanda para ocupar qualquer espaço 
            # extra não usado no layout, assegurando que o frame preencha todo o tooltip.

# Cria um rótulo (label) dentro do frame do tooltip, inicialmente sem texto.
label_tooltip = tk.Label(tooltip_frame, text="", justify='left', background='lightblue', font=fonte_tooltip)
    # 'text=""': Inicia o label sem texto, que será configurado 
            # dinamicamente conforme necessário.
    # 'justify='left'': Configura o alinhamento do texto dentro do label 
            # para ser alinhado à esquerda, facilitando a leitura.
    # 'background='lightblue'': Define a cor de fundo do label para coincidir 
            # com o frame, mantendo a consistência visual.
    # 'font=fonte_tooltip': Aplica a fonte definida para tooltips, que é 
            # ligeiramente maior e em negrito para destacar as informações do tooltip.

# Empacota o label dentro do frame do tooltip, configurando o padding interno.
label_tooltip.pack(padx=10, pady=5)
    # 'padx=10' e 'pady=5': Define o padding interno horizontal de 10 pixels e 
            # vertical de 5 pixels para o label, proporcionando espaço ao redor do 
            # texto para evitar que ele fique muito próximo às bordas do label, 
            # melhorando a legibilidade e a estética.


# Cria um rótulo (label) dentro do frame do tooltip que será 
            # usado para exibir imagens.
label_imagem = tk.Label(tooltip_frame, background='lightblue')
    # 'background='lightblue'': Define a cor de fundo do label como azul 
            # claro, mantendo a consistência visual com o resto do tooltip.

# Empacota o rótulo na interface, ajustando o espaçamento vertical.
label_imagem.pack(pady=5)
    # 'pady=5': Aplica um espaçamento vertical de 5 pixels acima e abaixo 
            # do label, proporcionando um layout visualmente agradável e evitando 
            # que a imagem fique muito próxima de outros elementos no tooltip.

# Associa eventos de movimento do mouse à tabela para controle de 
            # exibição do tooltip.
tabela.bind('<Motion>', exibir_tooltip)
    # '<Motion>': Evento que é disparado sempre que o mouse se move sobre a tabela.
    # 'exibir_tooltip': Função chamada sempre que o evento ocorre, 
            # mostrando o tooltip com informações adicionais sobre a 
            # linha sob o cursor.

tabela.bind('<Leave>', ocultar_tooltip)
    # '<Leave>': Evento que é disparado quando o mouse sai da área da tabela.
    # 'ocultar_tooltip': Função chamada para ocultar o tooltip quando o 
            # mouse deixa a tabela, mantendo a interface limpa.

# Chama a função para carregar os dados na tabela, usando o DataFrame 'df' 
            # previamente carregado e processado.
atualizar_tabela(df)
    # 'atualizar_tabela(df)': Esta função preenche a tabela com os dados do 
            # DataFrame, assegurando que a tabela exiba as informações mais recentes.

# Inicia o loop principal da aplicação Tkinter, que mantém a janela 'janela' 
            # aberta e responsiva a eventos de usuário.
janela.mainloop()
    # 'mainloop()': Este método entra no loop de eventos da janela, essencial 
            # para manter a aplicação executando e responder a interações como 
            # cliques e movimentos do mouse.