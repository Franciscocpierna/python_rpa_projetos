# Importação do módulo tkinter para criação de interfaces gráficas
import tkinter as tk

# Importação do módulo ttk para uso de widgets com
        # temas estilizados (parte do tkinter)
from tkinter import ttk

# Importação do módulo pandas, uma biblioteca para 
        # manipulação e análise de dados
import pandas as pd

# Definição de uma função chamada carregar_dados_excel 
        # para carregar dados de uma planilha Excel
def carregar_dados_excel():
    
    # Uso da função read_excel do pandas para carregar os 
            # dados da planilha 'Cidades.xlsx' na aba 'Dados'
    df = pd.read_excel('Cidades.xlsx', sheet_name='Dados')
    
    # Retorno do DataFrame carregado para quem chamar essa função
    return df


# Esta função é chamada para atualizar as opções nas 
        # comboboxes quando uma seleção é feita
def atualizar_combos(event=None):
    
    # Obtém o valor selecionado na combobox de países
    pais_selecionado = combo_pais.get()

    # Obtém o valor selecionado na combobox de estados
    estado_selecionado = combo_estado.get()

    # Obtém o valor selecionado na combobox de cidades
    cidade_selecionada = combo_cidade.get()

    # Começa com todos os dados disponíveis no DataFrame df
    dados_filtrados = df

    # Se um país foi selecionado...
    if pais_selecionado:
        
        # Filtra o DataFrame para incluir apenas as linhas onde a 
                # coluna 'Pais' é igual ao país selecionado
        dados_filtrados = dados_filtrados[dados_filtrados['Pais'] == pais_selecionado]
        
        # Extrai os valores únicos da coluna 'Estado' após o filtro, 
                # ordena-os e os define como valores na combobox de estados
        estados = sorted(dados_filtrados['Estado'].unique())
        combo_estado['values'] = estados

    # Se um estado foi selecionado na combobox...
    if estado_selecionado:
        
        # Filtra o DataFrame para incluir apenas as linhas onde a 
                # coluna 'Estado' é igual ao estado selecionado
        dados_filtrados = dados_filtrados[dados_filtrados['Estado'] == estado_selecionado]
        
        # Obtém uma lista única e ordenada de todas as 
                # cidades disponíveis após o filtro por estado
        cidades = sorted(dados_filtrados['Cidade'].unique())
        
        # Atualiza a combobox de cidades com as cidades 
                # filtradas pelo estado selecionado
        combo_cidade['values'] = cidades
    
    # Se uma cidade foi selecionada na combobox...
    if cidade_selecionada:
        
        # Filtra ainda mais o DataFrame para incluir apenas as 
                # linhas onde a coluna 'Cidade' é igual à cidade selecionada
        dados_filtrados = dados_filtrados[dados_filtrados['Cidade'] == cidade_selecionada]
    
    # Limpa todos os itens existentes na Treeview 
            # antes de inserir novos dados
    for item in tree.get_children():
        tree.delete(item)
    
    # Insere os dados filtrados na Treeview
    for index, row in dados_filtrados.iterrows():
        
        # Para cada linha no DataFrame filtrado, insere uma nova 
                # linha na Treeview com os dados de país, estado e cidade
        tree.insert('', tk.END, values=(row['Pais'], row['Estado'], row['Cidade']))



# Carrega os dados da planilha Excel chamando a função 
        # carregar_dados_excel definida anteriormente.
# A variável 'df' agora contém todos os dados da planilha 
        # em forma de uma tabela chamada DataFrame.
df = carregar_dados_excel()

# Cria a janela principal da interface gráfica 
        # usando a biblioteca tkinter.
# 'tk.Tk()' inicializa a janela principal para a aplicação.
janela = tk.Tk()

# Define o título da janela que aparecerá na barra de 
        # título no topo da janela.
# Este título ajuda os usuários a identificar o 
        # propósito da janela.
janela.title('Filtro de Cidades')

# Define o tamanho da janela em pixels. '700x500' significa que a 
        # janela terá 700 pixels de largura e 500 pixels de altura.
# Esta dimensão é importante para garantir que todos os 
        # elementos internos caibam adequadamente.
janela.geometry('700x500')

# Configura a cor de fundo da janela principal para um 
        # tom de cinza claro ('#f0f0f0').
# Isso é feito para melhorar a estética da interface e 
        # torná-la agradável visualmente.
janela.configure(bg='#f0f0f0')

# Cria um frame (quadro) dentro da janela principal. 
        # Um frame é um contêiner que pode agrupar 
        # vários widgets juntos,
        # como comboboxes (caixas de seleção 
        # que têm uma lista suspensa de opções).
# O frame é criado com a mesma cor de fundo da 
        # janela para manter a consistência visual.
frame_filtros = tk.Frame(janela, bg='#f0f0f0')

# Adiciona o frame à janela principal com um 
        # espaçamento vertical (pady) de 10 pixels.
# 'pack' é um gerenciador de geometria que 
        # organiza widgets em blocos antes de 
        # colocá-los na janela.
# 'pady=10' cria um espaço de 10 pixels acima e 
        # abaixo do frame para separá-lo 
        # visualmente de outros elementos na janela,
        # ajudando a reduzir a sensação de desordem.
frame_filtros.pack(pady=10)



# Cria um rótulo (label) para identificar a 
        # combobox de seleção de país.
# Este label é adicionado ao frame de filtros 
        # criado anteriormente.
# 'text='País:'' define o texto que aparece no 
        # label, indicando ao usuário que este 
        # campo é para selecionar um país.
# 'bg='#f0f0f0'' define a cor de fundo do 
        # label para combinar com o fundo do 
        # frame, mantendo a consistência visual.
# 'font=('Arial', 12)' define o tipo e tamanho 
        # da fonte usada no texto do label.
label_pais = tk.Label(frame_filtros, 
                      text='País:', 
                      bg='#f0f0f0', 
                      font=('Arial', 12))

# Posiciona o label dentro do frame usando o 
        # gerenciador de geometria 'grid'.
# 'row=0' e 'column=0' colocam o label na 
        # primeira linha e primeira coluna da grade.
# 'padx=10' e 'pady=5' adicionam espaço 
        # horizontal de 10 pixels e vertical 
        # de 5 pixels ao redor do label para 
        # evitar que ele fique muito próximo 
        # de outros elementos.
# 'sticky='e'' faz com que o label alinhe à 
        # direita dentro de sua célula na 
        # grade, garantindo uma aparência ordenada.
label_pais.grid(row=0, 
                column=0, 
                padx=10, 
                pady=5, 
                sticky='e')

# Cria uma combobox para seleção de país.
# 'values=sorted(df['Pais'].unique())' 
        # extrai uma lista única de países 
        # do DataFrame, ordena-os e usa 
        # como opções na combobox.
# Isso permite que o usuário escolha entre 
        # diferentes países disponíveis nos 
        # dados carregados.
# 'font=('Arial', 12)' define a mesma fonte e 
        # tamanho do label para manter a 
        # consistência visual.
combo_pais = ttk.Combobox(frame_filtros, 
                          values=sorted(df['Pais'].unique()), 
                          font=('Arial', 12))

# Posiciona a combobox na grade ao lado do 
        # label de país.
# 'row=0' e 'column=1' colocam a combobox na 
        # primeira linha e segunda coluna, 
        # ao lado do label.
# 'padx=10' e 'pady=5' mantêm o mesmo espaçamento 
        # utilizado para o label, mantendo a 
        # simetria e o espaçamento adequado.
combo_pais.grid(row=0, column=1, padx=10, pady=5)

# Associa um evento à combobox que, quando um 
        # país é selecionado, chama a função 
        # 'atualizar_combos'.
# '<<ComboboxSelected>>' é um evento que ocorre 
        # quando uma seleção é feita na combobox.
# 'atualizar_combos' é a função chamada, que 
        # atualiza as comboboxes de estado e 
        # cidade e atualiza os dados exibidos na Treeview.
combo_pais.bind("<<ComboboxSelected>>", atualizar_combos)


# Cria um rótulo (label) para identificar a 
        # combobox de seleção de Estado.
# Este label é adicionado ao mesmo frame de filtros 
        # onde os outros elementos estão sendo adicionados.
# 'text='Estado:'' define o texto que aparece no 
        # label, indicando ao usuário que este campo é 
        # para selecionar um estado.
# 'bg='#f0f0f0'' define a cor de fundo do label 
        # igual ao do frame, mantendo a consistência 
        # estética da interface.
# 'font=('Arial', 12)' especifica a fonte e o tamanho 
        # do texto, mantendo a uniformidade com 
        # outros textos na interface.
label_estado = tk.Label(frame_filtros, 
                        text='Estado:', 
                        bg='#f0f0f0', 
                        font=('Arial', 12))

# Posiciona o label dentro do frame usando o
        # gerenciador de geometria 'grid'.
# 'row=1' coloca o label na segunda linha da 
        # grade (a contagem começa em 0).
# 'column=0' coloca o label na primeira 
        # coluna da grade.
# 'padx=10' e 'pady=5' adicionam espaçamento em 
        # torno do label para evitar que os 
        # elementos fiquem muito juntos.
# 'sticky='e'' alinha o label à direita na 
        # sua célula na grade, garantindo que o 
        # texto esteja alinhado com outros rótulos.
label_estado.grid(row=1, 
                  column=0, 
                  padx=10, 
                  pady=5, 
                  sticky='e')

# Cria uma combobox para seleção de Estado.
# Neste ponto, a combobox é criada sem 
        # valores porque os valores dependerão 
        # do país selecionado na combobox de país.
# 'font=('Arial', 12)' mantém o mesmo estilo e 
        # tamanho de fonte que o label, garantindo 
        # consistência visual.
combo_estado = ttk.Combobox(frame_filtros, 
                            font=('Arial', 12))

# Posiciona a combobox na grade, ao lado do 
        # label de Estado.
# 'row=1' e 'column=1' colocam a combobox na 
        # segunda linha e segunda coluna, diretamente 
        # ao lado do seu label correspondente.
# 'padx=10' e 'pady=5' são usados para manter a 
        # combobox alinhada com o label e proporcionar 
        # espaço suficiente em torno dela para fácil interação.
combo_estado.grid(row=1, 
                  column=1, 
                  padx=10, 
                  pady=5)

# Associa um evento à combobox que, quando um 
        # estado é selecionado, chama a função 'atualizar_combos'.
# '<<ComboboxSelected>>' é um evento específico 
        # do Tkinter que é acionado quando uma 
        # opção é escolhida na combobox.
# 'atualizar_combos' é a função que será chamada, 
        # que irá atualizar as opções disponíveis nas 
        # comboboxes de cidade e atualizar os dados na Treeview.
combo_estado.bind("<<ComboboxSelected>>", atualizar_combos)


# Cria um rótulo (label) para identificar a combobox 
        # de seleção de Cidade.
# Este label é adicionado ao mesmo frame de filtros 
        # que os outros elementos.
# 'text='Cidade:'' define o texto que aparece no 
        # label, indicando ao usuário que este 
        # campo é para selecionar uma cidade.
# 'bg='#f0f0f0'' ajusta a cor de fundo do label 
        # para combinar com o fundo do frame, mantendo a 
        # consistência visual.
# 'font=('Arial', 12)' especifica o tipo e o tamanho da 
        # fonte, mantendo a uniformidade visual com 
        # outros componentes.
label_cidade = tk.Label(frame_filtros, 
                        text='Cidade:', 
                        bg='#f0f0f0', 
                        font=('Arial', 12))

# Posiciona o label dentro do frame usando o 
        # gerenciador de geometria 'grid'.
# 'row=2' coloca o label na terceira linha da 
        # grade (lembre-se, a contagem começa em 0).
# 'column=0' coloca o label na primeira coluna da grade.
# 'padx=10' e 'pady=5' adicionam um espaçamento 
        # adequado em torno do label para evitar 
        # aglomeração e facilitar a leitura.
# 'sticky='e'' alinha o label à direita dentro de 
        # sua célula na grade, criando um 
        # alinhamento visual com outros rótulos acima.
label_cidade.grid(row=2, 
                  column=0, 
                  padx=10, 
                  pady=5, 
                  sticky='e')

# Cria uma combobox para seleção de Cidade.
# A combobox é inicialmente criada sem valores 
        # definidos, pois os valores dependerão 
        # das seleções de país e estado.
# 'font=('Arial', 12)' é usado para manter a 
        # combobox visualmente consistente 
        # com os outros campos de entrada.
combo_cidade = ttk.Combobox(frame_filtros, 
                            font=('Arial', 12))


# Posiciona a combobox na grade, ao lado do 
        # label de Cidade.
# 'row=2' e 'column=1' colocam a combobox na 
        # terceira linha e segunda coluna, alinhando-a 
        # ao lado do seu label correspondente.
# 'padx=10' e 'pady=5' mantêm o mesmo padrão de 
        # espaçamento usado para os outros componentes, 
        # garantindo uniformidade e espaço 
        # adequado para interação.
combo_cidade.grid(row=2, column=1, padx=10, pady=5)

# Associa um evento à combobox que, quando uma 
        # cidade é selecionada, chama a 
        # função 'atualizar_combos'.
# '<<ComboboxSelected>>' é um evento específico 
        # do Tkinter que é disparado quando uma 
        # seleção é feita na combobox.
# 'atualizar_combos' é a função que será chamada 
        # para atualizar os dados mostrados na 
        # Treeview com base na cidade selecionada.
combo_cidade.bind("<<ComboboxSelected>>", atualizar_combos)


# Cria um frame que servirá como contêiner para a Treeview.
# Este frame é adicionado à janela principal 
        # da aplicação.
# 'bg='#f0f0f0'' configura a cor de fundo do 
        # frame para combinar com a cor de fundo 
        # geral da janela, mantendo a consistência visual.
tree_frame = tk.Frame(janela, bg='#f0f0f0')

# Posiciona o frame dentro da janela principal.
# 'expand=True' permite que o frame expanda para 
        # preencher qualquer espaço extra 
        # disponível na janela.
# 'fill='both'' faz com que o frame se expanda 
        # tanto vertical quanto horizontalmente.
# 'padx=10' e 'pady=10' adicionam um espaçamento de 10 
        # pixels em todas as direções ao redor do 
        # frame, evitando que os elementos gráficos 
        # fiquem muito juntos das bordas da janela.
tree_frame.pack(expand=True, 
                fill='both', 
                padx=10, 
                pady=10)

# Cria a Treeview dentro do frame.
# 'columns=('Pais', 'Estado', 'Cidade')' define as 
        # colunas que a Treeview deve ter, correspondendo 
        # aos dados que serão exibidos.
# 'show='headings'' configura a Treeview para mostrar 
        # apenas os cabeçalhos das colunas, e não 
        # uma coluna extra de índice à esquerda.
# 'height=15' define a altura da Treeview para 
        # exibir 15 linhas de uma vez.
tree = ttk.Treeview(tree_frame, 
                    columns=('Pais', 'Estado', 'Cidade'), 
                    show='headings', 
                    height=15)

# Configura os cabeçalhos das colunas na Treeview.
# Estas linhas definem o texto que aparecerá 
        # em cada cabeçalho de coluna, que 
        # são 'País', 'Estado' e 'Cidade'.
# Isso ajuda os usuários a entender o 
        # que os dados em cada coluna representam.
tree.heading('Pais', text='País')
tree.heading('Estado', text='Estado')
tree.heading('Cidade', text='Cidade')


# Cria um objeto de estilo para personalizar a 
        # aparência dos widgets do ttk.
# A biblioteca ttk permite a personalização de 
        # temas e estilos dos componentes da interface.
style = ttk.Style()

# Configura o estilo dos cabeçalhos das 
        # colunas da Treeview.
# 'Treeview.Heading' é o nome do estilo para 
        # os cabeçalhos das colunas na Treeview.
# 'font=('Arial', 12, 'bold')' define a fonte 
        # dos cabeçalhos para Arial, tamanho 12, em negrito.
# Isso faz com que os cabeçalhos sejam mais 
        # proeminentes e fáceis de ler.
style.configure("Treeview.Heading", 
                font=('Arial', 12, 'bold'))

# Configura o estilo para as células da 
        # Treeview (não os cabeçalhos).
# 'Treeview' é o nome do estilo aplicado às 
        # linhas da Treeview.
# 'font=('Arial', 12)' define a fonte das 
        # células para Arial, tamanho 12, 
        # garantindo que os dados sejam legíveis.
style.configure("Treeview", font=('Arial', 12))

# Cria uma barra de rolagem vertical para a Treeview.
# 'tree_frame' é o frame que contém a 
        # Treeview, e a barra de rolagem é 
        # adicionada a esse frame.
# 'orient="vertical"' configura a barra de 
        # rolagem para ser vertical.
# 'command=tree.yview' conecta a barra de 
        # rolagem com a visão vertical da Treeview, 
        # permitindo que ela controle o deslocamento 
        # dos dados na Treeview.
scrollbar = ttk.Scrollbar(tree_frame, 
                          orient="vertical", 
                          command=tree.yview)

# Configura a Treeview para responder ao 
        # controle da barra de rolagem.
# 'yscrollcommand=scrollbar.set' conecta o 
        # movimento da barra de rolagem com a Treeview.
tree.configure(yscrollcommand=scrollbar.set)

# Posiciona a barra de rolagem na Treeview.
# 'side='right'' posiciona a barra de rolagem 
        # no lado direito da Treeview.
# 'fill='y'' faz com que a barra de rolagem 
        # preencha todo o espaço vertical do 
        # frame, de cima a baixo.
scrollbar.pack(side='right', fill='y')

# Posiciona a Treeview dentro do frame.
# 'expand=True' permite que a Treeview expanda 
        # para preencher qualquer espaço extra 
        # disponível no frame.
# 'fill='both'' faz com que a Treeview se 
        # expanda tanto vertical quanto horizontalmente, 
        # ocupando todo o espaço disponível no frame.
tree.pack(expand=True, fill='both')


# Carrega todos os dados do DataFrame na Treeview.
# Este loop percorre cada linha (row) do DataFrame 'df'.
# 'df.iterrows()' é uma função que permite 
        # iterar sobre cada linha do DataFrame 
        # como pares de índice (index) e linha (row).
for index, row in df.iterrows():
    
    # Insere cada linha de dados na Treeview.
    # O primeiro argumento '' indica que a nova 
            # linha será adicionada ao final da Treeview.
    # 'tk.END' é uma constante que especifica que o 
            # novo item deve ser inserido no final da 
            # lista de itens já presentes na Treeview.
    # 'values=(row['Pais'], row['Estado'], row['Cidade'])' 
            # define os valores a serem inseridos para 
            # cada coluna especificada na Treeview.
    # Estes valores são extraídos das colunas 'Pais', 
            # 'Estado' e 'Cidade' do DataFrame 
            # para a linha atual.
    tree.insert('', 
                tk.END, 
                values=(row['Pais'], row['Estado'], row['Cidade']))


# Iniciar o loop principal do Tkinter
janela.mainloop()