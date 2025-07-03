# Importa as bibliotecas necessárias para a interface 
        # gráfica e manipulação de dados.

# Biblioteca para criar interface gráfica.
import tkinter as tk  

# Submódulo de tkinter para widgets mais estilizados.
from tkinter import ttk

# Biblioteca para manipulação e análise de dados.
import pandas as pd  

# Carrega os dados de um arquivo Excel em um DataFrame chamado 'df'.
df = pd.read_excel('dados_cidades.xlsx', sheet_name='Cidades')


# Define uma função chamada 'exportar_para_excel' para 
        # salvar os dados filtrados em um arquivo Excel.
def exportar_para_excel():
    
    # Cria uma lista chamada 'dados_exportar' que coleta todos os 
            # valores dos itens na tabela da interface gráfica.
    # 'tabela.get_children()' obtém todos os IDs dos itens na 
            # tabela, que são usados para acessar cada item.
    # 'tabela.item(item)["values"]' retorna os valores associados a 
            # cada item (linha) na tabela, como uma lista.
    # A compreensão de lista é usada para iterar sobre cada 
            # item e coletar seus valores.
    dados_exportar = [tabela.item(item)["values"] for item in tabela.get_children()]

    # Cria um DataFrame do pandas chamado 'df_exportar' 
            # usando a lista de dados coletados.
    # 'columns=["Cidade", "População", "PIB (em milhões)"]' 
            # define os nomes das colunas do DataFrame,
            # correspondendo à ordem dos dados em 'dados_exportar'.
    df_exportar = pd.DataFrame(dados_exportar, 
                               columns=["Cidade", "População", "PIB (em milhões)"])

    # Salva o DataFrame 'df_exportar' em um arquivo Excel 
            # chamado 'dados_filtrados.xlsx'.
    # 'to_excel("dados_filtrados.xlsx", index=False)' converte o 
            # DataFrame para um arquivo Excel,
            # onde 'index=False' especifica que os índices 
            # do DataFrame não devem ser incluídos no arquivo Excel.
    df_exportar.to_excel("dados_filtrados.xlsx", index=False)

    # Imprime uma mensagem no console para indicar que os 
            # dados foram exportados com sucesso.
    print("Dados exportados para dados_filtrados.xlsx")
    

# Define uma função chamada 'aplicar_filtro'. Esta função é ativada 
        # quando um evento ocorre (por exemplo, uma tecla é 
        # pressionada em um campo de entrada).
def aplicar_filtro(*args):
    
    # Cria um dicionário chamado 'filtros'. Este dicionário armazena os 
            # valores atuais dos campos de entrada após serem tratados.
    # 'filtro_cidade.get()' pega o texto do campo de entrada da 
            # cidade, 'strip()' remove espaços extras no início e no fim,
    # e 'lower()' converte o texto para letras minúsculas 
            # para padronizar o filtro.
    filtros = {
        "Cidade": filtro_cidade.get().strip().lower(),
        "População": filtro_populacao.get().strip().lower(),
        "PIB (em milhões)": filtro_pib.get().strip().lower(),
    }
    
    # Cria um DataFrame 'df_filtrado' que começa filtrando o 
            # DataFrame original 'df' pela coluna 'País'.
    # Utiliza a variável 'pais_selecionado' 
            # para filtrar as linhas que correspondem ao país selecionado.
    df_filtrado = df[df['País'] == pais_selecionado]

    # Itera sobre cada par de coluna e filtro no dicionário 'filtros'.
    # 'coluna' recebe o nome da coluna a ser filtrada (e.g., "Cidade") e
            # 'filtro' o valor específico a ser encontrado.
    for coluna, filtro in filtros.items():
        
        # Verifica se há algum valor no filtro para evitar a 
                # aplicação de filtros vazios.
        if filtro:
            
            # Atualiza 'df_filtrado' para incluir apenas as linhas onde 
                    # os valores na coluna especificada contêm o texto do filtro.
            # 'astype(str)' garante que os dados sejam tratados como 
                    # strings, 'str.lower()' converte os dados para minúsculas,
            # e 'str.contains(filtro)' verifica se a string do filtro 
                    # está contida nos dados da coluna.
            df_filtrado = df_filtrado[df_filtrado[coluna].astype(str).str.lower().str.contains(filtro)]
    
    # Chama a função 'atualizar_tabela' passando o 'df_filtrado' 
            # como argumento.
    # Esta função é responsável por atualizar a interface 
            # gráfica para mostrar os resultados do filtro.
    atualizar_tabela(df_filtrado)



# Define uma função chamada 'atualizar_tabela' que recebe um 
        # DataFrame 'dados' como argumento.
def atualizar_tabela(dados):
    
    # Itera sobre todos os elementos filhos da 'tabela', que 
            # representam as linhas da tabela na interface gráfica.
    # 'tabela.get_children()' retorna uma lista de IDs de todos os 
            # itens presentes na tabela.
    for row in tabela.get_children():
        
        # Para cada linha identificada por 'row', a linha é 
                # removida da tabela.
        # 'tabela.delete(row)' remove o item especificado, 
                # limpando a tabela para novos dados.
        tabela.delete(row)
    
    # Itera sobre cada linha no DataFrame 'dados' usando 'iterrows()', 
            # que gera pares de índice e linha.
    # 'index' contém o índice da linha, 'row' é a série de 
            # dados para a linha atual.
    for index, row in dados.iterrows():
        
        # Insere uma nova linha na tabela com os dados extraídos do DataFrame.
        # 'tabela.insert('', 'end', ...)' adiciona um novo 
                # item ao final da tabela.
        # 'values=(row['Cidade'], row['População'], row['PIB (em milhões)'])' 
                # especifica os valores a serem inseridos,
                # que são os valores das colunas 'Cidade', 'População' e
                # 'PIB (em milhões)' da linha atual do DataFrame.
        tabela.insert('', 
                      'end', 
                      values=(row['Cidade'], row['População'], row['PIB (em milhões)']))


# Define a função que será chamada quando um evento (neste caso,
        # um clique) ocorrer na Treeview que lista os países.
def exibir_informacoes_pais(event):
    
    # Usa a palavra-chave 'global' para modificar a variável 
            # global 'pais_selecionado'.
    # Isso permite que a variável seja atualizada aqui e 
            # usada em outras partes do código.
    global pais_selecionado
    
    # Obtém o item que foi selecionado na Treeview. 'arvore.selection()[0]' 
            # retorna o identificador do primeiro item selecionado.
    # Esta é a maneira padrão de acessar o item selecionado 
            # em uma Treeview usando Tkinter.
    item_selecionado = arvore.selection()[0]
    
    # 'arvore.item(item_selecionado, 'values')' acessa os 
            # valores associados ao item selecionado na Treeview.
    # Esses valores são detalhes armazenados no item, como o 
            # nome do país neste caso.
    info_pais = arvore.item(item_selecionado, 'values')
    
    # Checa se realmente há informações no item selecionado. Isso 
            # evita erros caso algo seja clicado sem ter valores associados.
    if info_pais:
        
        # Atribui o primeiro valor associado ao item selecionado (nome do país) 
                # à variável 'pais_selecionado'.
        pais_selecionado = info_pais[0]
        
        # Chama a função 'aplicar_filtro', que irá atualizar a 
                # visualização dos dados conforme os filtros aplicados.
        # Isso é feito automaticamente ao selecionar um país, filtrando 
                # os dados para mostrar apenas as cidades desse país.
        aplicar_filtro()



# Inicializa a janela principal da interface gráfica 
        # usando Tkinter. 'tk.Tk()' cria o objeto principal da janela.
janela_principal = tk.Tk()

# Define o título da janela principal, que aparecerá 
        # na barra de título da janela.
# "Exemplo de Treeview com Filtros e Exportação" é o 
        # texto que será exibido como título da janela.
janela_principal.title("Exemplo de Treeview com Filtros e Exportação")

# Define a fonte padrão que será usada em todos os 
        # widgets (elementos de interface) para manter a 
        # consistência visual.
# 'Arial' é o tipo de fonte, '12' é o tamanho da fonte. 
        # A tupla ('Arial', 12) é armazenada na variável 'fonte_padrao'.
fonte_padrao = ('Arial', 12)

# Cria um widget Treeview dentro da 'janela_principal'. Treeview é 
        # usado para exibir listas hierárquicas, como uma árvore 
        # de diretórios ou uma lista categorizada.
# O objeto 'arvore' é uma instância de 'ttk.Treeview', que 
        # proporciona um visual mais moderno e funcionalidades 
        # adicionais sobre o básico 'tk.Treeview'.
arvore = ttk.Treeview(janela_principal)

# Configura o posicionamento do widget 'arvore' dentro 
        # da 'janela_principal'.
# 'pack(side='left', fill='y')' posiciona a Treeview no 
        # lado esquerdo da janela e faz com que ela expanda 
        # verticalmente (fill='y').
# Isso significa que a Treeview se estenderá ao longo 
        # de toda a altura da janela, alinhando-se à esquerda.
arvore.pack(side='left', fill='y')


# Cria um objeto 'style' que permite configurar 
        # os temas e estilos dos widgets ttk.
style = ttk.Style()

# Configura o estilo para todos os widgets do tipo 
        # Treeview na aplicação.
# 'font=fonte_padrao' define a fonte padrão para o 
        # texto dentro da Treeview, garantindo uniformidade visual.
# 'rowheight=25' define a altura de cada linha na 
        # Treeview para 25 pixels, proporcionando espaço suficiente para legibilidade.
style.configure("Treeview", 
                font=fonte_padrao, 
                rowheight=25)

# Configura o estilo para os cabeçalhos das colunas na Treeview.
# 'font=('Arial', 14, 'bold')' define a fonte para os 
        # cabeçalhos das colunas como Arial, tamanho 14, em negrito.
# Isso destaca os cabeçalhos das colunas, tornando-os 
        # mais proeminentes e fáceis de ler.
style.configure("Treeview.Heading", 
                font=('Arial', 14, 'bold'))

# Define a configuração da coluna principal na 
        # Treeview (identificada por "#0").
# 'width=250' e 'minwidth=250' definem a largura inicial e 
        # a largura mínima da coluna para 250 pixels,
# garantindo que o conteúdo seja claramente visível e a 
        # coluna não se torne muito estreita.
arvore.column("#0", width=250, minwidth=250)

# Configura o cabeçalho da coluna principal na Treeview.
# 'text="Continente -> País"' define o texto do 
        # cabeçalho para "Continente -> País",
        # explicando que a coluna mostrará informações de 
        # continentes seguidas pelos países.
# 'anchor=tk.W' alinha o texto do cabeçalho à 
        # esquerda (West) dentro da coluna.
arvore.heading("#0", 
               text="Continente -> País", 
               anchor=tk.W)

# Agrupa os dados do DataFrame 'df' por 'Continente', o 
        # que é útil para visualizar os dados organizados 
        # por regiões geográficas.
# A função 'groupby('Continente')' agrupa os dados 
        # baseando-se na coluna 'Continente',
        # permitindo a manipulação subsequente dos dados agrupados 
        # para fins de visualização ou análise.
continentes = df.groupby('Continente')

# Inicia um loop que percorre cada grupo de dados retornado 
        # pelo agrupamento por 'Continente'.
# 'continentes' é um objeto GroupBy do pandas, onde cada iteração 
        # retorna um par 'continente' (o nome do continente) e 
        # 'grupo_continente' (dados para esse continente).
for continente, grupo_continente in continentes:
    
    # Insere um novo item na Treeview para cada continente. 
            # O item representa um continente.
    # '' indica que o item será inserido na raiz da Treeview.
    # 'end' significa que o novo item será adicionado ao 
            # final da lista de itens existentes na Treeview.
    # 'text=continente' define o texto do item como o nome do continente.
    # 'open=False' especifica que o item não estará expandido 
            # por padrão, ou seja, suas subcategorias (países) 
            # não serão visíveis imediatamente.
    id_continente = arvore.insert('', 
                                  'end', 
                                  text=continente, 
                                  open=False)
    
    # Agrupa os dados dentro de cada continente por 'País', 
            # preparando para listar os países sob cada continente na Treeview.
    paises = grupo_continente.groupby('País')
    
    # Itera sobre cada grupo de dados retornado pelo agrupamento por 'País'.
    # 'pais' é o nome do país e 'grupo_pais' são os dados 
            # para esse país dentro do continente atual.
    for pais, grupo_pais in paises:
        
        # Insere um novo item na Treeview para cada país sob o 
                # item do continente correspondente.
        # 'id_continente' é o ID do item do continente sob o qual 
                # o novo item (país) será adicionado.
        # 'end' significa que o novo item será adicionado ao final 
                # da lista de itens existentes sob o item do continente.
        # 'text=pais' define o texto do item como o nome do país.
        # 'values=(pais,)' armazena o nome do país como um valor 
                # associado ao item, que pode ser utilizado para outras operações, como filtragem.
        arvore.insert(id_continente, 
                      'end', 
                      text=pais, 
                      values=(pais,))


# Cria um 'frame' (quadro) chamado 'frame_filtros', que será 
        # usado para organizar visualmente os campos de entrada 
        # de filtro na interface.
# 'tk.Frame(janela_principal)' cria um novo frame dentro da 
        # janela principal definida anteriormente como 'janela_principal'.
frame_filtros = tk.Frame(janela_principal)

# Configura o posicionamento do 'frame_filtros' dentro 
        # da 'janela_principal'.
# 'pack(side='top', fill='x', ...)' é usado para adicionar o 
        # frame ao layout da janela.
# 'side='top'' posiciona o frame na parte superior da janela principal, 
        # fazendo com que seja um dos primeiros elementos visíveis.
# 'fill='x'' faz com que o frame se estenda horizontalmente ao 
        # longo da janela, ocupando toda a largura disponível.
# 'padx=10' e 'pady=5' adicionam um espaçamento interno de 10 pixels 
        # na horizontal e 5 pixels na vertical entre os bordos 
        # do frame e os widgets contidos nele.
frame_filtros.pack(side='top', 
                   fill='x', 
                   padx=10, 
                   pady=5)

# Cria um rótulo (label) dentro do 'frame_filtros', que foi 
        # configurado para conter os campos de filtro.
# 'text="Filtrar Cidade:"' define o texto que aparecerá no rótulo, 
        # indicando que este campo é usado para inserir um filtro de cidade.
# 'font=fonte_padrao' aplica a fonte padrão definida anteriormente, 
        # mantendo a consistência visual em toda a interface.
# 'grid(row=0, column=0, ...)' posiciona o rótulo na primeira 
        # linha (row=0) e na primeira coluna (column=0) do 
        # layout de grade dentro do 'frame_filtros'.
# 'padx=5' e 'pady=5' adicionam um espaçamento de 5 pixels ao 
        # redor do rótulo para separá-lo visualmente dos outros 
        # elementos e evitar uma aparência amontoada.
# 'sticky=tk.W' faz com que o texto do rótulo alinhe à esquerda 
        # dentro de sua célula na grade.
tk.Label(frame_filtros, 
         text="Filtrar Cidade:", 
         font=fonte_padrao).grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Cria um campo de entrada (Entry) dentro do 'frame_filtros', 
        # onde o usuário pode digitar um filtro para cidades.
# 'font=fonte_padrao' é usado novamente para aplicar a fonte padrão, 
        # assegurando que o texto digitado tenha a mesma aparência 
        # dos outros textos na interface.
# O método 'grid' posiciona o campo de entrada ao lado do rótulo "Filtrar Cidade:".
# Posicionado na primeira linha (row=0) e na segunda coluna (column=1).
# 'padx=5' e 'pady=5' adicionam espaçamento ao redor do 
        # campo de entrada, similar ao espaçamento ao redor do 
        # rótulo, para manter a interface organizada e visualmente agradável.
filtro_cidade = tk.Entry(frame_filtros, font=fonte_padrao)
filtro_cidade.grid(row=0, column=1, padx=5, pady=5)

# Vincula um evento ao campo de entrada 'filtro_cidade' para que, 
        # sempre que uma tecla for solta (key release), a 
        # função 'aplicar_filtro' seja chamada.
# "<KeyRelease>" é o tipo de evento que ocorre quando uma 
        # tecla é solta após ser pressionada no campo de entrada.
# 'aplicar_filtro' é a função chamada sempre que o evento ocorre, 
        # permitindo atualizar a tabela de dados com base no 
        # texto digitado pelo usuário.
filtro_cidade.bind("<KeyRelease>", aplicar_filtro)


# Cria um rótulo (label) dentro do 'frame_filtros'. Este 
        # rótulo é para o campo destinado ao filtro de população.
# 'text="Filtrar População:"' especifica o texto que aparecerá no 
        # rótulo, orientando o usuário sobre o propósito do campo adjacente.
# 'font=fonte_padrao' aplica a fonte padrão definida anteriormente, 
        # assegurando a consistência visual dos textos na interface.
# 'grid(row=0, column=2, ...)' posiciona o rótulo na primeira 
        # linha (row=0) e na terceira coluna (column=2) do layout 
        # de grade dentro do 'frame_filtros'.
# 'padx=5' e 'pady=5' adicionam espaçamento de 5 pixels ao redor 
        # do rótulo, melhorando a legibilidade e a estética geral 
        # ao evitar uma aparência de elementos amontoados.
# 'sticky=tk.W' alinha o texto do rótulo à esquerda (West), o 
        # que ajuda na clareza e organização visual, associando-o 
        # de forma direta ao campo de entrada à sua direita.
tk.Label(frame_filtros, 
         text="Filtrar População:", 
         font=fonte_padrao).grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

# Cria um campo de entrada (Entry) no 'frame_filtros' para que 
        # os usuários possam digitar um filtro para população.
# 'font=fonte_padrao' é usado para manter a uniformidade da 
        # fonte com outros elementos interativos na interface.
# O método 'grid' posiciona o campo de entrada diretamente ao 
        # lado do rótulo "Filtrar População:".
# Localizado na primeira linha (row=0) e na quarta coluna (column=3), 
        # este posicionamento facilita a associação do campo com seu rótulo.
# 'padx=5' e 'pady=5' estabelecem um espaçamento adequado em torno 
        # do campo de entrada, contribuindo para uma interface 
        # organizada e acessível.
filtro_populacao = tk.Entry(frame_filtros, font=fonte_padrao)
filtro_populacao.grid(row=0, column=3, padx=5, pady=5)

# Associa um evento ao campo de entrada 'filtro_populacao' que 
        # ativa a função 'aplicar_filtro' sempre que uma tecla é 
        # solta após ser pressionada.
# '<KeyRelease>' é o evento que detecta quando o usuário solta 
        # uma tecla, permitindo que o filtro seja aplicado 
        # imediatamente após a alteração do texto.
# 'aplicar_filtro' é chamada sempre que este evento ocorre, atualizando 
        # dinamicamente a exibição dos dados conforme o usuário 
        # digita no campo de entrada.
filtro_populacao.bind("<KeyRelease>", aplicar_filtro)

# Cria um rótulo (label) dentro do 'frame_filtros', que é utilizado 
        # para organizar visualmente os campos de filtro.
# 'text="Filtrar PIB:"' define o texto do rótulo, que indica ao 
        # usuário que este campo é destinado ao filtro por valores de PIB.
# 'font=fonte_padrao' aplica a fonte padrão estabelecida para a 
        # interface, mantendo a uniformidade visual dos textos exibidos.
# O método 'grid' é usado para posicionar o rótulo na primeira 
        # linha (row=0) e na quinta coluna (column=4) do layout 
        # de grade do 'frame_filtros'.
# 'padx=5' e 'pady=5' adicionam um espaçamento de 5 pixels ao 
        # redor do rótulo para criar uma margem visual clara entre 
        # ele e outros elementos, evitando uma interface apertada.
# 'sticky=tk.W' garante que o texto do rótulo esteja alinhado à 
        # esquerda (West), facilitando a leitura e a compreensão 
        # visual da função do campo adjacente.
tk.Label(frame_filtros, 
         text="Filtrar PIB:", 
         font=fonte_padrao).grid(row=0, column=4, padx=5, pady=5, sticky=tk.W)

# Cria um campo de entrada (Entry) que permite aos usuários 
        # inserir critérios para filtrar dados de PIB.
# 'font=fonte_padrao' assegura que o texto dentro do campo de 
        # entrada seja consistente com o restante da interface.
# 'grid' posiciona o campo de entrada diretamente ao lado 
        # do rótulo "Filtrar PIB:".
# Colocado na primeira linha (row=0) e na sexta coluna (column=5), 
        # este arranjo assegura que o campo esteja visualmente 
        # ligado ao rótulo correspondente.
# 'padx=5' e 'pady=5' estabelecem um espaçamento adequado ao 
        # redor do campo, contribuindo para uma disposição 
        # clara e acessível dos elementos na interface.
filtro_pib = tk.Entry(frame_filtros, font=fonte_padrao)
filtro_pib.grid(row=0, column=5, padx=5, pady=5)

# Associa um evento ao campo de entrada 'filtro_pib' que 
        # ativa a função 'aplicar_filtro' sempre que uma 
        # tecla é liberada após ser pressionada.
# '<KeyRelease>' é o evento que detecta quando o usuário solta 
        # uma tecla, permitindo que o filtro seja aplicado 
        # imediatamente após a alteração do texto.
# 'aplicar_filtro' é chamada sempre que esse evento ocorre, 
        # atualizando dinamicamente a exibição dos dados 
        # conforme o usuário digita no campo de entrada.
filtro_pib.bind("<KeyRelease>", aplicar_filtro)

# Cria um novo 'frame' (quadro) chamado 'frame_tabela', 
        # que será usado para conter a tabela com os dados.
# 'tk.Frame(janela_principal)' cria o frame dentro da 
        # janela principal da aplicação.
frame_tabela = tk.Frame(janela_principal)

# Configura o posicionamento e o dimensionamento do 
        # 'frame_tabela' dentro da 'janela_principal'.
# 'pack(side='top', fill='both', expand=True, ...)' adiciona 
        # o frame ao layout da janela.
# 'side='top'' posiciona o frame na parte superior dentro da 
        # janela, logo após qualquer outro elemento que também 
        # esteja alinhado ao topo.
# 'fill='both'' faz com que o frame expanda tanto vertical 
        # quanto horizontalmente para preencher o espaço disponível.
# 'expand=True' permite que o frame se expanda adicionalmente 
        # para ocupar qualquer espaço extra disponível na janela.
# 'padx=10' e 'pady=10' adicionam espaçamento interno de 10 pixels 
        # em todas as direções dentro do frame, evitando que os 
        # elementos internos toquem diretamente as bordas do frame.
frame_tabela.pack(side='top', 
                  fill='both', 
                  expand=True, 
                  padx=10, 
                  pady=10)

# Define as colunas da tabela que será usada para 
        # exibir os dados filtrados.
# '("Cidade", "População", "PIB (em milhões)")' é uma 
        # tupla que especifica os títulos das colunas da tabela.
colunas = ("Cidade", "População", "PIB (em milhões)")

# Cria uma 'treeview' (vista de árvore) chamada 'tabela' 
        # dentro do 'frame_tabela', usada para exibir os 
        # dados em formato de tabela.
# 'columns=colunas' define as colunas da tabela conforme 
        # especificado na variável 'colunas'.
# 'show='headings'' configura a treeview para mostrar apenas 
        # os cabeçalhos das colunas, sem a coluna de 
        # identificação padrão do Tkinter.
# 'height=20' define a altura da tabela para mostrar 20 
        # linhas de uma vez.
tabela = ttk.Treeview(frame_tabela, 
                      columns=colunas, 
                      show='headings', 
                      height=20)

# Configura o posicionamento da 'tabela' dentro do 'frame_tabela'.
# 'fill='both'' faz com que a tabela expanda em ambas as 
        # direções (vertical e horizontal) para ocupar o 
        # espaço disponível.
# 'expand=True' permite que a tabela se expanda adicionalmente 
        # para ocupar qualquer espaço extra disponível no frame.
tabela.pack(fill='both', expand=True)


# Itera sobre cada nome de coluna definido na tupla 'colunas'.
for col in colunas:
    
    # Configura o cabeçalho de cada coluna na tabela 'tabela'.
    # 'tabela.heading(col, text=col)' define o texto do 
            # cabeçalho da coluna, usando o nome da coluna como texto.
    tabela.heading(col, text=col)
    
    # Define a largura de cada coluna na tabela.
    # 'tabela.column(col, width=150)' define a largura de 
            # cada coluna para 150 pixels,
    # garantindo que todas as colunas tenham tamanho uniforme e 
            # adequado para a visualização dos dados.
    tabela.column(col, width=150)

# Cria um botão dentro da 'janela_principal'.
# 'text="Exportar para Excel"' define o texto que aparecerá 
            # no botão, indicando sua função.
# 'font=fonte_padrao' aplica a fonte padrão ao texto do botão, 
            # mantendo a consistência visual.
# 'command=exportar_para_excel' vincula o botão à função 'exportar_para_excel', 
        # que será executada quando o botão for clicado.
btn_exportar = tk.Button(janela_principal, 
                         text="Exportar para Excel", 
                         font=fonte_padrao, 
                         command=exportar_para_excel)

# Configura o posicionamento do botão dentro da 'janela_principal'.
# 'pack(side='top', pady=10)' posiciona o botão na parte 
        # superior da janela e adiciona um espaçamento 
        # vertical de 10 pixels acima e abaixo do botão,
        # ajudando a separá-lo visualmente de outros elementos 
        # na interface.
btn_exportar.pack(side='top', pady=10)

# Vincula um evento de seleção (clique) na Treeview 'arvore' à 
        # função 'exibir_informacoes_pais'.
# '<<TreeviewSelect>>' é um evento padrão do Tkinter que é 
        # disparado quando a seleção na Treeview muda.
# 'exibir_informacoes_pais' é a função que será chamada sempre 
        # que esse evento ocorrer,
# atualizando a interface com informações sobre o país 
        # selecionado e aplicando os filtros pertinentes.
arvore.bind("<<TreeviewSelect>>", exibir_informacoes_pais)

# Iniciar o loop da interface
janela_principal.mainloop()