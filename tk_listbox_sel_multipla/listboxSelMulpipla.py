# Importa o módulo tkinter com o alias 'tk' para criar interfaces gráficas.
import tkinter as tk

# Importa 'ttk' do tkinter para usar widgets com um estilo melhorado.
from tkinter import ttk

# Importa 'filedialog' do tkinter para permitir a 
        # seleção de arquivos através de uma janela de diálogo.
from tkinter import filedialog

# Importa o pandas com o alias 'pd', usado para manipulação de dados.
import pandas as pd

# Define uma função para carregar dados de um arquivo Excel especificado.
def carregar_dados_excel():
    
    # Lê um arquivo Excel, especificamente a aba 'Dados', e 
            # armazena os dados em um DataFrame.
    df = pd.read_excel('Cidades_Expandido.xlsx', sheet_name='Dados')
    
    # Retorna o DataFrame carregado.
    return df


# Função para atualizar as ListBoxes e a Treeview
def atualizar_listboxes(event=None):
    
    # Cria uma lista dos países selecionados na ListBox de 
            # países. 'listbox_pais.curselection()'
    # retorna os índices dos itens selecionados, e 'listbox_pais.get(i)' 
            # obtém o país no índice 'i'.
    pais_selecionados = [listbox_pais.get(i) for i in listbox_pais.curselection()]

    # Filtra o DataFrame 'df' para incluir apenas os registros 
            # onde o valor na coluna 'Pais'
            # está na lista de 'pais_selecionados'. Em seguida, 
            # extrai os valores únicos da coluna 'Estado'.
    estados_filtrados = df[df['Pais'].isin(pais_selecionados)]['Estado'].unique()
    
    # Limpa todos os itens da ListBox de estados. '0' é o 
            # índice do primeiro item e 'tk.END'
            # é uma constante que representa o último item na 
            # lista, assim deletando tudo entre eles.
    listbox_estado.delete(0, tk.END)

    # Insere cada estado filtrado na ListBox de estados, 
            # ordenados alfabeticamente com 'sorted()'.
    # 'tk.END' indica que cada novo item deve ser 
            # adicionado ao final da lista.
    for estado in sorted(estados_filtrados):
        listbox_estado.insert(tk.END, estado)
    
    # Limpa a ListBox de cidades antes de atualizar, 
            # pois os estados selecionados podem ter mudado.
    listbox_cidade.delete(0, tk.END)

    # Chama a função para atualizar a Treeview com 
            # os dados filtrados baseados na 
            # nova seleção de estados.
    atualizar_treeview()


# Função para atualizar a ListBox de cidades e a 
        # Treeview quando um ou mais estados 
        # são selecionados.
def atualizar_cidades(event=None):
    
    # Cria uma lista dos estados selecionados na 
            # ListBox de estados. A função 'curselection()'
    # retorna uma lista de índices dos itens 
            # selecionados na ListBox. O método 'get(i)'
            # é usado para recuperar o estado correspondente a 
            # cada índice 'i' selecionado.
    estados_selecionados = [listbox_estado.get(i) for i in listbox_estado.curselection()]

    # Filtra o DataFrame 'df' para incluir apenas os 
            # registros onde o valor na coluna 'Estado'
            # corresponde a algum dos estados na lista 
            # 'estados_selecionados'. 
    # O método 'isin()' é usado aqui para verificar se 
            # cada valor na coluna 'Estado' está 
            # contido na lista 'estados_selecionados'.
    # Após essa filtragem, o método 'unique()' é 
            # aplicado à coluna 'Cidade' para obter um array
            # de todas as cidades únicas presentes nos 
            # estados selecionados, evitando repetições 
            # na lista final.
    cidades_filtradas = df[df['Estado'].isin(estados_selecionados)]['Cidade'].unique()

    # Limpa a ListBox de cidades removendo todos os 
            # itens presentes nela. Isso é necessário 
            # para garantir que a ListBox só contenha 
            # as cidades que pertencem aos estados 
            # atualmente selecionados.
    # '0' indica o primeiro item da lista e 'tk.END' é 
            # uma constante que representa o último item.
    listbox_cidade.delete(0, tk.END)

    # Insere cada cidade do array 'cidades_filtradas' na 
            # ListBox de cidades. As cidades são inseridas
            # após serem ordenadas alfabeticamente pelo método 
            # 'sorted()', facilitando a busca e seleção 
            # pelo usuário.
    for cidade in sorted(cidades_filtradas):
        listbox_cidade.insert(tk.END, cidade)
    
    # Atualiza a Treeview para refletir os dados 
            # filtrados com base nas cidades selecionadas.
    # Isso mantém a visualização dos dados consistente 
            # com as seleções de país e estado 
            # feitas pelo usuário.
    atualizar_treeview()
    

# Esta linha inicia a definição de uma função 
        # chamada 'atualizar_treeview'. 
# Esta função é chamada quando um evento (como 
        # uma seleção em uma ListBox) acontece. 
# 'event=None' significa que a função
        # pode ser chamada sem um evento 
        # associado, ou seja, pode ser invocada diretamente.
def atualizar_treeview(event=None):
    
    # A função 'curselection()' é chamada sobre 'listbox_pais', 
            # que é uma instância de ListBox.
    # 'curselection()' retorna uma lista de índices 
            # dos itens atualmente selecionados na ListBox.
    # Por exemplo, se os três primeiros itens estão 
            # selecionados, 'curselection()' 
            # retorna [0, 1, 2].
    pais_selecionados = [
        
        # 'get(i)' é usado para obter o valor (neste caso, o 
                # nome do país) armazenado no índice 'i'
                # da ListBox. O uso de 'listbox_pais.get(i)' 
                # retorna o país correspondente ao índice 'i'.
        # A compreensão de lista (list comprehension) 
                # aqui itera sobre cada índice retornado 
                # por 'curselection()' e coleta todos os 
                # países selecionados em uma lista.
        listbox_pais.get(i) for i in listbox_pais.curselection()
        
    ]

    # Este processo é similar ao acima, mas aplicado à 
            # ListBox de estados. 'listbox_estado' contém
            # uma lista de estados, e 'curselection()' retorna 
            # os índices dos estados selecionados.
    # 'listbox_estado.get(i)' é chamado para cada índice, 
            # retornando o estado correspondente.
    # O resultado é uma lista de estados selecionados.
    estados_selecionados = [
        listbox_estado.get(i) for i in listbox_estado.curselection()
    ]

    # Similarmente, esta linha trata das cidades 
            # selecionadas na ListBox de cidades.
    # 'listbox_cidade.curselection()' fornece os 
            # índices das cidades selecionadas,
            # e 'listbox_cidade.get(i)' é usado para 
            # recuperar cada cidade correspondente a 
            # esses índices.
    # O resultado final é uma lista de cidades selecionadas.
    cidades_selecionadas = [
        listbox_cidade.get(i) for i in listbox_cidade.curselection()
    ]


    # Inicia com o DataFrame original 
            # contendo todos os dados.
    dados_filtrados = df

    # Verifica se a lista 'pais_selecionados' não está 
            # vazia. Se houver países selecionados, 
            # procede com o filtro.
    if pais_selecionados:
        
        # Filtra o DataFrame 'dados_filtrados' para incluir 
                # apenas as linhas onde os valores na coluna 'Pais'
                # estão na lista de países selecionados. 
        # O método 'isin()' cria uma série booleana que é True
        # para linhas cujo valor na coluna 'Pais' está 
                # contido na lista 'pais_selecionados'. 
        # Isso efetivamente restringe 'dados_filtrados' 
                # aos registros que correspondem aos 
                # países escolhidos.
        dados_filtrados = dados_filtrados[dados_filtrados['Pais'].isin(pais_selecionados)]
    
    # Verifica se a lista 'estados_selecionados' não 
            # está vazia para proceder com o próximo 
            # nível de filtragem.
    if estados_selecionados:
        
        # Aplica um filtro similar ao anterior, mas desta 
                # vez usando a coluna 'Estado'. 
        # Somente as linhas que têm seu valor em 'Estado' 
                # presente na lista 'estados_selecionados' 
                # são mantidas em 'dados_filtrados'.
        dados_filtrados = dados_filtrados[dados_filtrados['Estado'].isin(estados_selecionados)]
    
    # Verifica se há cidades selecionadas para 
            # aplicar o último nível de filtragem.
    if cidades_selecionadas:
        
        # Filtra 'dados_filtrados' para incluir apenas as 
                # linhas onde os valores na coluna 'Cidade' estão na
        # lista 'cidades_selecionadas', reduzindo ainda 
                # mais o conjunto de dados com base nas 
                # cidades selecionadas.
        dados_filtrados = dados_filtrados[dados_filtrados['Cidade'].isin(cidades_selecionadas)]
    
    # Remove todos os itens existentes na Treeview para 
            # preparar a interface para novos dados.
    for item in tree.get_children():
        
        # Para cada item já presente na Treeview, remove o 
                # item. 'tree.get_children()' retorna uma lista
                # de identificadores dos itens presentes, e 
                # 'tree.delete(item)' remove cada um deles.
        tree.delete(item)
    
    # Insere os dados filtrados na Treeview, atualizando a 
            # visualização para o usuário.
    for index, row in dados_filtrados.iterrows():
        
        # Itera sobre cada linha dos dados filtrados. 'iterrows()' 
                # retorna o índice da linha e a própria linha como
                # uma série. 'tree.insert()' adiciona uma nova 
                # linha na Treeview, onde 'values' 
                # contém os valores a serem mostrados, que 
                # são os valores das colunas 'Pais', 'Estado' e 
                # 'Cidade' da linha atual.
        tree.insert('', 
                    tk.END, 
                    values=(row['Pais'], row['Estado'], row['Cidade']))



# Define a função exportar_para_excel, que será 
        # chamada para salvar os dados filtrados 
        # em um arquivo Excel.
def exportar_para_excel():
    
    # A função 'curselection()' retorna uma lista de 
            # índices que representam os itens selecionados 
            # na ListBox de países.
    # Por exemplo, se o primeiro e o terceiro país 
            # na lista estiverem selecionados, 
            # 'curselection()' retornará [0, 2].
    # A função 'get(i)' é então usada para recuperar o 
            # nome do país no índice 'i' dentro da ListBox.
    # Essa operação é realizada para cada índice na 
            # lista retornada por 'curselection()', e 
            # cada nome de país
            # recuperado é armazenado na lista 'pais_selecionados'.
    pais_selecionados = [listbox_pais.get(i) for i in listbox_pais.curselection()]
    
    # Similar ao processo de seleção de países, 'curselection()' é 
            # usado para obter uma lista de índices
            # dos estados selecionados na ListBox de estados. 
    # Cada índice é usado com o método 'get(i)' para recuperar
            # o nome do estado correspondente, e esses 
            # nomes são coletados na lista 'estados_selecionados'.
    # Este processo assegura que apenas os estados 
            # efetivamente escolhidos pelo usuário sejam 
            # considerados nos filtros subsequentes.
    estados_selecionados = [listbox_estado.get(i) for i in listbox_estado.curselection()]
    
    # De forma análoga aos países e estados, 'curselection()' 
            # fornece os índices das cidades selecionadas 
            # na ListBox de cidades.
    # O método 'get(i)' é então utilizado para extrair o 
            # nome de cada cidade correspondente a 
            # esses índices.
    # Todos os nomes das cidades selecionadas são 
            # armazenados na lista 'cidades_selecionadas', 
            # que será utilizada para filtrar os 
            # dados no DataFrame.
    cidades_selecionadas = [listbox_cidade.get(i) for i in listbox_cidade.curselection()]
    
    # A variável 'dados_filtrados' é inicialmente 
            # igualada ao DataFrame 'df', que 
            # contém todos os dados.
    # Isso prepara 'dados_filtrados' para ser filtrado 
            # com base nas seleções feitas nas ListBoxes.
    dados_filtrados = df
    
    # Esta condição verifica se a lista 'pais_selecionados' 
            # contém algum elemento. Se sim, o DataFrame 
            # 'dados_filtrados' é filtrado para incluir 
            # apenas as linhas onde os valores na coluna 'Pais' 
            # correspondem a algum dos países na lista 'pais_selecionados'. 
    # O método 'isin()' cria uma máscara booleana 
            # onde cada posição é True se o
            # valor na coluna 'Pais' estiver na 
            # lista 'pais_selecionados', permitindo 
            # essa filtragem.
    if pais_selecionados:
        dados_filtrados = dados_filtrados[dados_filtrados['Pais'].isin(pais_selecionados)]
    
    # Um procedimento similar é seguido para filtrar 'dados_filtrados' 
            # baseado na seleção de estados.
    # A lista 'estados_selecionados' é usada com o 
            # método 'isin()' para reter apenas as 
            # linhas do DataFrame onde a coluna 'Estado' 
            # contém valores presentes na lista 'estados_selecionados'.
    if estados_selecionados:
        dados_filtrados = dados_filtrados[dados_filtrados['Estado'].isin(estados_selecionados)]
    
    # Finalmente, a lista 'cidades_selecionadas' é usada 
                # para filtrar ainda mais 'dados_filtrados'.
    # Apenas as linhas onde a coluna 'Cidade' contém 
            # valores que estão presentes na lista 
            # 'cidades_selecionadas' são mantidas após 
            # esta filtragem, resultando em um conjunto de 
            # dados restrito às cidades selecionadas.
    if cidades_selecionadas:
        dados_filtrados = dados_filtrados[dados_filtrados['Cidade'].isin(cidades_selecionadas)]


    # Abre uma janela de diálogo para salvar arquivos, 
            # pedindo ao usuário para escolher o local e 
            # o nome do arquivo.
    # 'defaultextension' assegura que o arquivo seja 
            # salvo com a extensão .xlsx, e 'filetypes' define que
            # apenas arquivos do tipo Excel (*.xlsx) são permitidos.
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension='.xlsx', 
                                                   filetypes=[('Excel files', '*.xlsx')])

    # Verifica se um caminho de arquivo foi escolhido (ou seja, o 
            # usuário não cancelou a operação).
    if caminho_arquivo:
        
        # Salva os dados filtrados no caminho escolhido. 
        # 'index=False' significa que o índice do DataFrame
                # não será escrito no arquivo, apenas os dados das colunas.
        dados_filtrados.to_excel(caminho_arquivo, index=False)
        
    

# Carregar dados do Excel
df = carregar_dados_excel()

# A função Tk() é chamada para criar a janela 
        # principal da aplicação GUI usando Tkinter.
# Essa janela servirá como o contêiner principal 
        # para todos os outros widgets GUI.
janela = tk.Tk()

# Define o título da janela principal. Esta string 
        # aparece na barra de título da janela,
        # ajudando os usuários a identificar o propósito 
        # da aplicação visualmente.
janela.title('Seleção Múltipla com Listbox')

# Configura as dimensões da janela principal. 
# O método 'geometry()' aceita uma string
        # no formato 'largura x altura', definindo 
        # assim o tamanho da janela quando é exibida.
# Neste caso, a janela será de 800 pixels de 
        # largura por 600 pixels de altura.
janela.geometry('800x600')

# Cria um Frame, que é um contêiner widget no 
        # Tkinter usado para agrupar e organizar 
        # outros widgets.
# 'tk.Frame(janela)' cria um frame na janela 
        # principal que acabou de ser definida.
# Frames são úteis para controlar o layout dos 
        # widgets de interface do usuário em uma aplicação.
frame_listboxes = tk.Frame(janela)

# Posiciona o frame dentro da janela principal. 
# O método 'pack()' é usado para adicionar o frame à janela.
# 'pady=10' adiciona um preenchimento vertical 
        # de 10 pixels acima e abaixo do frame, 
        # e 'padx=10' adiciona um preenchimento 
        # horizontal de 10 pixels aos lados do frame. 
# Isso ajuda a evitar que os widgets fiquem
        # muito juntos, melhorando a estética 
        # da interface do usuário.
frame_listboxes.pack(pady=10, padx=10)


# Cria um Label, que é um widget usado para 
        # exibir texto ou imagens. O Label 
        # será usado aqui para indicar que a 
        # ListBox subsequente é para a seleção de 
        # países. 
# O primeiro argumento, 'frame_listboxes',
        # indica que este Label está sendo colocado 
        # dentro do frame definido anteriormente.
# O parâmetro 'text="País:"' define o texto 
        # que aparecerá no Label.
label_pais = tk.Label(frame_listboxes, text="País:")

# Posiciona o Label no grid dentro de 'frame_listboxes'. 
# O método 'grid()' é usado para gerenciar o layout
        # em uma forma tabular. 
# 'row=0' e 'column=0' posicionam o Label na 
        # primeira linha e primeira coluna do grid.
# 'padx=5' adiciona um preenchimento horizontal 
        # de 5 pixels em ambos os lados do Label, 
        # ajudando a separar visualmente este 
        # texto dos outros elementos da interface.
label_pais.grid(row=0, column=0, padx=5)

# Cria uma ListBox dentro do 'frame_listboxes'. 
# Uma ListBox é um widget que permite aos usuários
        # selecionar um ou mais itens de uma lista. 
# 'selectmode=tk.MULTIPLE' permite múltiplas seleções.
# 'exportselection=False' impede que a seleção na 
        # ListBox interfira com a seleção em outros widgets
        # de seleção (como outras ListBoxes). 
# 'width=20' define a largura da ListBox para 
        # acomodar 20 caracteres, e 'height=10' define a 
        # altura para mostrar 10 linhas de itens 
        # ao mesmo tempo.
listbox_pais = tk.Listbox(frame_listboxes, 
                          selectmode=tk.MULTIPLE, 
                          exportselection=False, 
                          width=20, 
                          height=10)

# Posiciona a ListBox no grid. Ela é colocada 
        # abaixo do Label do país, usando 'row=1' 
        # para colocá-la na segunda linha do grid 
        # na mesma coluna ('column=0') que o Label. 
# 'padx=5' adiciona o mesmo preenchimento
        # horizontal que foi usado para o Label, 
        # mantendo a consistência visual.
listbox_pais.grid(row=1, column=0, padx=5)


# Cria um widget Label dentro do frame destinado 
        # às ListBoxes. 
# Este Label serve para identificar a próxima ListBox, 
        # que será usada para selecionar estados. 
# O texto "Estado:" ajuda os usuários a
        # entenderem o que eles devem selecionar
        # na ListBox correspondente.
label_estado = tk.Label(frame_listboxes, 
                        text="Estado:")

# Posiciona o Label para estados no grid do frame. 
# O Label é colocado na primeira linha (row=0)
        # e na segunda coluna (column=1), diretamente 
        # ao lado do Label de países, mas em uma 
        # coluna diferente.
# O 'padx=5' adiciona um espaçamento horizontal 
        # de 5 pixels, criando uma margem entre 
        # este Label e outros elementos para 
        # evitar um visual amontoado.
label_estado.grid(row=0, column=1, padx=5)

# Cria uma ListBox para a seleção de estados. 
# A configuração é similar à da ListBox de países:
        # 'selectmode=tk.MULTIPLE' permite que múltiplos 
        # estados sejam selecionados simultaneamente,
# 'exportselection=False' evita que a seleção 
        # interfira com a seleção em outras ListBoxes,
# 'width=20' define a largura suficiente para 
        # exibir os nomes dos estados de forma legível.
# 'height=10' permite visualizar até 10 itens 
        # sem a necessidade de rolagem.
listbox_estado = tk.Listbox(frame_listboxes, 
                            selectmode=tk.MULTIPLE, 
                            exportselection=False, 
                            width=20, 
                            height=10)

# Posiciona a ListBox de estados no grid. 
# A ListBox é colocada imediatamente abaixo 
        # do Label de estados, alinhando-se 
        # com ele na segunda coluna (column=1) e 
        # na segunda linha (row=1). 
# O 'padx=5' mantém a consistência
        # do espaçamento horizontal com o 
        # Label acima, proporcionando uma 
        # aparência uniforme e organizada.
listbox_estado.grid(row=1, 
                    column=1, 
                    padx=5)


# Cria um widget Label, que é um componente 
        # visual simples destinado a exibir texto 
        # estático na interface gráfica.
# Este Label específico é usado para 
        # identificar a ListBox de cidades 
        # que será criada a seguir.
# O texto "Cidade:" é definido para 
        # indicar aos usuários que nesta 
        # ListBox eles podem selecionar 
        # uma ou mais cidades.
label_cidade = tk.Label(frame_listboxes, 
                        text="Cidade:")

# Posiciona o Label para cidades no grid dentro 
        # do frame que organiza as ListBoxes. 
# O método 'grid()' é usado para colocar o 
        # Label na posição definida pela 
        # linha 'row=0' (primeira linha do grid) e 
        # pela coluna 'column=2' (terceira coluna), 
        # o que coloca este Label ao lado dos Labels 
        # de país e estado. 'padx=5' adiciona 
        # um espaçamento
        # horizontal de 5 pixels em ambos os lados 
        # do Label, ajudando a separá-lo 
        # visualmente dos outros elementos.
label_cidade.grid(row=0, column=2, padx=5)

# Cria uma ListBox, que é um widget usado para 
        # listar opções selecionáveis. 
# Neste caso, a ListBox permite a seleção
        # múltipla de cidades, configurada através 
        # de 'selectmode=tk.MULTIPLE'. 
# Isso permite que os usuários escolham mais de
        # uma cidade simultaneamente para ações 
        # como filtragem de dados. 'exportselection=False' é 
        # configurado para evitar que
        # a seleção nesta ListBox interfira com a 
        # seleção em outras caixas de listagem
        # que possam existir na aplicação.
# 'width=20' define a largura da ListBox em 
        # caracteres, garantindo que os nomes 
        # das cidades sejam visíveis claramente,
        # e 'height=10' define a altura da ListBox 
        # em linhas, permitindo que seja visualizada 
        # uma lista de até 10 cidades sem a 
        # necessidade de rolagem.
listbox_cidade = tk.Listbox(frame_listboxes, 
                            selectmode=tk.MULTIPLE, 
                            exportselection=False, 
                            width=20, 
                            height=10)

# Posiciona a ListBox de cidades no grid. 
# O método 'grid()' é novamente usado para 
        # organizar a ListBox na interface,
        # colocando-a abaixo do Label de cidades 
        # correspondente. 
# Ela é configurada para estar na segunda 
        # linha 'row=1' e na terceira coluna 'column=2', 
        # alinhada diretamente abaixo do Label 
        # de cidades. 
# O uso de 'padx=5' continua a padrão
        # de espaçamento lateral encontrado 
        # nas outras ListBoxes, mantendo um 
        # layout consistente e visualmente agradável.
listbox_cidade.grid(row=1, column=2, padx=5)


# Vincula eventos de seleção nas ListBoxes a 
        # funções específicas. 
# Quando um item é selecionado em qualquer
        # uma das ListBoxes, o evento 
        # correspondente é disparado. 
# O método 'bind()' associa um evento de seleção,
        # identificado por "<<ListboxSelect>>", a 
        # uma função que será chamada sempre 
        # que o evento ocorrer.
# Esta linha associa o evento de seleção na 
        # ListBox de países à função 'atualizar_listboxes', 
        # que é responsável por atualizar as 
        # ListBoxes de estados e cidades com 
        # base na seleção de país.
listbox_pais.bind("<<ListboxSelect>>", atualizar_listboxes)

# Similarmente, esta linha associa o evento de 
        # seleção na ListBox de estados à função 
        # 'atualizar_cidades'.
# Essa função atualiza a ListBox de cidades 
        # com base nos estados selecionados.
listbox_estado.bind("<<ListboxSelect>>", atualizar_cidades)

# Associa o evento de seleção na ListBox de 
        # cidades à função 'atualizar_treeview'. 
# Esta função atualiza a Treeview com dados filtrados 
        # com base nas cidades selecionadas.
listbox_cidade.bind("<<ListboxSelect>>", atualizar_treeview)

# Cria um widget Treeview, que é um componente 
        # para exibir dados em formato de tabela 
        # com linhas e colunas.
# Configura a Treeview na janela principal com 
        # três colunas identificadas pelos títulos 
        # 'Pais', 'Estado' e 'Cidade'. 
# 'show='headings'' instrui a Treeview a 
        # exibir apenas os cabeçalhos das colunas, 
        # sem a coluna de identificação padrão à esquerda.
tree = ttk.Treeview(janela, 
                    columns=('Pais', 'Estado', 'Cidade'), 
                    show='headings')

# Configura os cabeçalhos de cada coluna na 
        # Treeview. 
# 'tree.heading()' define o texto do cabeçalho 
        # para cada coluna.
# Aqui, a coluna 'Pais' terá o cabeçalho 
        # 'País', 'Estado' terá 'Estado' e 'Cidade' 
        # terá 'Cidade'.
# Isso rotula claramente as colunas para os 
        # usuários, tornando os dados exibidos 
        # fáceis de entender.
tree.heading('Pais', text='País')
tree.heading('Estado', text='Estado')
tree.heading('Cidade', text='Cidade')

# Posiciona a Treeview na janela principal. 
# O método 'pack()' é usado para adicionar a 
        # Treeview à janela, com 'expand=True' 
        # e 'fill='both'' instruindo a Treeview a 
        # expandir e preencher todo o espaço disponível
        # horizontal e verticalmente. 
# Isso garante que a Treeview utilize 
        # eficientemente o espaço da janela,
        # adaptando-se ao redimensionamento 
        # da janela pelo usuário.
tree.pack(expand=True, fill='both')


# Cria um botão na janela principal para 
        # permitir que o usuário exporte os 
        # dados filtrados para um arquivo Excel.
# 'tk.Button()' é usado para criar o botão, 
        # com 'janela' como o contêiner pai, 
        # indicando que o botão será exibido
        # dentro da janela principal. 
# O texto exibido no botão é "Exportar para Excel", o 
        # que indica claramente sua funcionalidade.
# O parâmetro 'command=exportar_para_excel' vincula a 
        # ação do botão à função 'exportar_para_excel'.
# Quando o usuário clica no botão, a função 'exportar_para_excel' é 
        # chamada, iniciando o processo de exportação 
        # dos dados filtrados.
btn_exportar = tk.Button(janela, 
                         text="Exportar para Excel", 
                         command=exportar_para_excel)

# Posiciona o botão na janela usando o método 'pack()'. 
# 'pady=10' adiciona um preenchimento 
        # vertical de 10 pixels acima e abaixo 
        # do botão, criando um espaçamento que
        # melhora a aparência e a usabilidade 
        # da interface, evitando que o botão 
        # fique muito próximo de outros elementos.
btn_exportar.pack(pady=10)

# Preenche a ListBox de países com os nomes 
        # únicos dos países disponíveis no DataFrame.
# A função 'sorted()' organiza os países em 
        # ordem alfabética para uma navegação 
        # mais fácil.
# 'df['Pais'].unique()' retorna um array com os 
        # nomes dos países únicos presentes na 
        # coluna 'Pais' do DataFrame.
# A linha 'for pais in sorted(df['Pais'].unique())' 
        # itera por cada nome de país único, que é 
        # então inserido na ListBox
        # através do método 'insert()'. 
# 'tk.END' garante que cada novo país seja 
        # adicionado ao final da lista na ListBox.
for pais in sorted(df['Pais'].unique()):
    listbox_pais.insert(tk.END, pais)


# Iniciar o loop principal do Tkinter
janela.mainloop()