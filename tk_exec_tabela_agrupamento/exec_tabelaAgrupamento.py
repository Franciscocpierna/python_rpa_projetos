# Importação das bibliotecas necessárias para a interface 
        # gráfica e para a manipulação de dados.
# 'tkinter' é usado para construir a interface gráfica, 
        # e 'pandas' para manipular dados em formato de tabelas.
import tkinter as tk
from tkinter import ttk
import pandas as pd

# Carregamento dos dados de um arquivo Excel.
# 'pd.read_excel("tabela_exemplo.xlsx")' lê o arquivo Excel 
        # especificado e carrega os dados em um DataFrame chamado 'df'.
# Um DataFrame é uma estrutura de dados bidimensional semelhante a 
        # uma tabela que facilita a manipulação de dados.
df = pd.read_excel("tabela_exemplo.xlsx")

# Conversão da coluna 'Salário' para o tipo float.
# A conversão para float é necessária para garantir que 
        # operações numéricas, como somas e médias, sejam 
        # realizadas corretamente.
# 'df["Salário"].astype(float)' converte os valores da 
        # coluna 'Salário' do DataFrame 'df' para o tipo float.
df["Salário"] = df["Salário"].astype(float)

# Definição explícita das colunas que serão utilizadas no programa.
# Esta lista 'colunas' contém os nomes das colunas como strings 
        # e é usada para referenciar especificamente essas 
        # colunas em outras partes do código.
# Manter esses nomes em uma lista ajuda a manter o código 
        # organizado e facilita alterações no conjunto de colunas usado.
colunas = ["Cidade", "Profissão", "Nome", "Idade", "Salário"]

# Criação da janela principal do aplicativo usando a 
        # biblioteca Tkinter.
# 'tk.Tk()' é o comando que inicializa a janela principal 
        # para a interface gráfica.
janela = tk.Tk()

# Definição do título da janela principal.
# 'janela.title("Tabela Interativa com Agrupamento de Colunas")' 
        # configura o texto que aparecerá na barra de título da janela.
# Isso ajuda os usuários a identificar o propósito da janela 
        # quando estiver sendo exibida.
janela.title("Tabela Interativa com Agrupamento de Colunas")

# Configuração da cor de fundo da janela principal.
# 'janela.configure(bg="white")' define o fundo da janela para 
        # branco. Isso define um padrão visual limpo e 
        # claro para a interface.
janela.configure(bg="white")

# Criação e configuração de um estilo personalizado para o 
        # componente Treeview usando o módulo ttk da biblioteca Tkinter.
# 'ttk.Style()' cria um objeto de estilo que pode ser usado 
        # para modificar a aparência dos widgets ttk.
style = ttk.Style()

# Configuração do estilo para linhas específicas dentro 
        # de um Treeview.
# 'style.configure("Cidade.Treeview", ...)' define o estilo 
        # para os itens do Treeview que usarão a tag "Cidade".
# 'background="yellow"' define o fundo dos itens com esta 
        # tag para amarelo, tornando-os mais visíveis.
# 'foreground="black"' define a cor do texto para preto, 
        # garantindo alta legibilidade contra o fundo amarelo.
# Essa personalização ajuda a destacar visualmente as linhas 
        # que representam cidades na tabela, facilitando sua identificação.
style.configure("Cidade.Treeview", 
                background="yellow", 
                foreground="black")


# Criação e configuração do título do projeto na interface 
        # gráfica usando um Label.
# 'tk.Label(janela, ...)' cria um widget de rótulo que será 
        # colocado na janela principal 'janela'.
# 'text="Projeto: Tabela Interativa com Filtros"' define o 
        # texto do rótulo que explica o propósito da interface.
# 'font=("Arial", 16)' define a fonte do texto para Arial, 
        # tamanho 16, que é grande e claro para fácil leitura.
# 'bg="white"' define a cor de fundo do rótulo como branco, 
        # mantendo a consistência com o fundo da janela principal.
titulo = tk.Label(janela, 
                  text="Projeto: Tabela Interativa com Filtros", 
                  font=("Arial", 16), 
                  bg="white")

# Posicionamento do título na interface gráfica usando o método grid.
# 'row=0' coloca o rótulo na primeira linha do grid da janela.
# 'column=0' coloca o rótulo na primeira coluna.
# 'columnspan=3' faz o rótulo se estender por três 
        # colunas, garantindo que ocupe um espaço amplo 
        # na parte superior da janela.
# 'pady=(10, 10)' adiciona um padding vertical de 10 pixels 
        # acima e abaixo do rótulo, criando um espaço 
        # visual entre o título e outros elementos.
titulo.grid(row=0, 
            column=0, 
            columnspan=3, 
            pady=(10, 10))

# Criação de um container usando um Frame para 
        # agrupar visualmente os campos de filtro na interface.
# 'tk.Frame(janela, bg="white")' cria um frame na 
        # janela principal com o fundo branco.
container_filtros = tk.Frame(janela, bg="white")

# Posicionamento do container de filtros na interface.
# 'grid(row=1, column=0, columnspan=3, pady=(10, 10))' 
        # posiciona o frame na segunda linha, estende-se 
        # por três colunas e adiciona padding vertical.
container_filtros.grid(row=1, 
                       column=0, 
                       columnspan=3, 
                       pady=(10, 10))

# Inicialização de um dicionário 'filtros' para armazenar 
        # os widgets de entrada de dados (Entry) para filtros.
# Este dicionário facilitará a referência e o acesso aos 
        # campos de filtro no código, especialmente durante 
        # as operações de filtragem de dados.
filtros = {}

# Este loop percorre cada coluna especificada na lista 'colunas', usando a 
        # função enumerate para obter tanto o índice quanto o nome da coluna.
for idx, col in enumerate(colunas):
    # Criação de um rótulo (label) para cada coluna. Este label 
            # serve como uma descrição para o campo de entrada correspondente.
    # 'tk.Label(container_filtros, ...)' cria o label dentro 
            # do 'container_filtros'.
    # 'text=col' define o texto do label para o nome da coluna, que 
            # ajuda o usuário a identificar o que deve ser 
            # inserido no campo de entrada.
    # 'font=("Arial", 12)' define a fonte do texto para Arial 
            # tamanho 12, que é claro e legível.
    # 'bg="white"' define a cor de fundo do label como branca, 
            # mantendo a consistência visual com o container.
    lbl = tk.Label(container_filtros, 
                   text=col, 
                   font=("Arial", 12), 
                   bg="white")

    # Posicionamento do label no grid do container de filtros.
    # 'row=0' coloca todos os labels na primeira 
            # linha do container.
    # 'column=idx' coloca cada label na coluna correspondente 
            # ao seu índice na lista 'colunas'.
    # 'padx=(5, 5)' adiciona um padding horizontal de 5 pixels à 
            # esquerda e à direita do label para separá-lo 
            # visualmente dos outros elementos.
    lbl.grid(row=0, column=idx, padx=(5, 5))

    # Criação de um campo de entrada (entry) para que os 
            # usuários possam inserir os valores de filtro 
            # para cada coluna.
    # 'tk.Entry(container_filtros, font=("Arial", 12))' cria o 
            # campo de entrada dentro do 'container_filtros' 
            # com a mesma fonte dos labels.
    filtro = tk.Entry(container_filtros, 
                      font=("Arial", 12))

    # Posicionamento do campo de entrada no grid.
    # 'row=1' coloca os campos de entrada na segunda 
            # linha do container, diretamente abaixo dos 
            # labels correspondentes.
    # 'column=idx' alinha cada campo de entrada com seu 
            # label correspondente acima.
    # 'padx=(5, 5)' aplica o mesmo padding horizontal 
            # usado nos labels, para alinhamento e 
            # consistência visual.
    filtro.grid(row=1, column=idx, padx=(5, 5))

    # Adição do campo de entrada ao dicionário 'filtros' 
            # usando o nome da coluna como chave.
    # Isso permite acessar facilmente o campo de entrada 
            # correspondente a cada coluna em outras partes 
            # do código, especialmente ao aplicar filtros.
    filtros[col] = filtro


# Criação de um componente Treeview para exibir dados de 
        # forma estruturada, permitindo visualizações hierárquicas.
# 'ttk.Treeview(janela, columns=colunas, show="tree headings")' 
        # cria um Treeview na janela principal.
# 'columns=colunas' especifica as colunas do DataFrame 
        # que serão usadas no Treeview.
# 'show="tree headings"' configura o Treeview para mostrar 
        # apenas os cabeçalhos das colunas, sem a coluna de índice padrão.
tree = ttk.Treeview(janela, 
                    columns=colunas, 
                    show="tree headings")

# Configuração do cabeçalho da coluna primária no Treeview, 
        # que não faz parte das colunas do DataFrame, mas é 
        # usada para agrupamento ou identificação principal.
# 'tree.heading("#0", text="Cidade")' define o cabeçalho 
        # da coluna "#0" (primeira coluna à esquerda) para "Cidade".
# Esta coluna será usada para mostrar um agrupamento ou 
        # categorização principal dos dados, neste caso, pela cidade.
tree.heading("#0", text="Cidade")

# Loop que configura os cabeçalhos das colunas adicionais de 
        # acordo com as colunas definidas no DataFrame.
# Este loop percorre cada nome de coluna fornecido na lista 'colunas'.
for col in colunas:
    
    # 'tree.heading(col, text=col)' configura o texto do 
            # cabeçalho de cada coluna para ser igual ao nome da coluna.
    # Isso garante que cada coluna no Treeview seja claramente 
            # identificada pelo seu nome correspondente no DataFrame.
    tree.heading(col, text=col)

# Posicionamento do Treeview na interface gráfica.
# 'tree.grid(row=3, column=0, columnspan=3, pady=10)' posiciona o 
        # Treeview no grid da janela.
# 'row=3' coloca o Treeview na quarta linha da janela 
        # (contando a partir de 0).
# 'column=0' inicia o Treeview na primeira coluna.
# 'columnspan=3' faz o Treeview se estender por três 
        # colunas, ocupando um espaço amplo horizontalmente.
# 'pady=10' adiciona um padding vertical de 10 pixels acima e 
        # abaixo do Treeview para separação dos outros elementos.
tree.grid(row=3, column=0, columnspan=3, pady=10)


# Definição de uma função chamada 'formatar_salario' para 
        # formatar valores numéricos de salário, incluindo 
        # os separadores de milhares.
def formatar_salario(valor):
    # A função recebe um argumento 'valor', que é o 
            # número (salário) a ser formatado.
    
    # Formatação do número para incluir dois dígitos após o 
            # ponto decimal e separadores de milhares.
    # 'f"{valor:,.2f}"' converte o número em uma string formatada:
    # ':,' adiciona o separador de milhares,
    # '.2f' garante que o número seja mostrado com duas 
            # casas decimais.
    # Por padrão, em Python, o separador de milhares é a 
            # vírgula e o separador decimal é o ponto.
    formatted = f"{valor:,.2f}"
    
    # Substituição dos separadores para se adequarem ao formato 
            # europeu/latino-americano:
    # '.replace(",", "X")' substitui temporariamente as 
            # vírgulas (separador de milhares original) por 'X' 
            # para evitar conflitos na próxima substituição.
    # '.replace(".", ",")' substitui pontos (separador decimal original) por 
            # vírgulas, adaptando para o formato decimal desejado.
    # '.replace("X", ".")' substitui 'X' por pontos, finalizando a 
            # substituição para o separador de milhares.
    # Este processo garante que os milhares sejam separados por pontos e os 
            # decimais por vírgulas, conforme usado em muitos países 
            # fora do padrão americano.
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


# Definição de uma função chamada 'carregar_dados' que 
        # carrega e exibe dados no componente Treeview.
def carregar_dados():
    
    # Limpeza de todos os dados existentes na Treeview antes 
            # de carregar novos dados.
    # 'tree.delete(*tree.get_children())' remove todos os 
            # itens (filhos) da Treeview, garantindo que a 
            # visualização esteja limpa para os novos dados.
    tree.delete(*tree.get_children())
    
    # Agrupamento dos dados por cidade e cálculo da soma dos 
            # valores numéricos para cada grupo.
    # 'df.groupby('Cidade', as_index=False)' agrupa os dados 
            # no DataFrame 'df' pela coluna 'Cidade', 
    # e 'as_index=False' mantém 'Cidade' como uma coluna 
            # regular, não como índice.
    # '.sum()' calcula a soma de todas as colunas numéricas para 
            # cada grupo, útil para obter o salário total por cidade.
    df_grouped = df.groupby('Cidade', as_index=False).sum()

    # Iteração sobre cada linha dos dados agrupados 
            # para inserir na Treeview.
    for _, row in df_grouped.iterrows():
        
        # Acessando o nome da cidade e o salário total da 
                # cidade atualmente iterada.
        cidade = row['Cidade']

        # Formatação do salário total usando a função 
                # definida anteriormente.
        salario_total = formatar_salario(row['Salário'])

        # Inserção do agrupamento principal na Treeview.
        # 'tree.insert("", "end", text=cidade, ...)' insere um novo 
                # item na Treeview com o nome da cidade como texto principal.
        # 'values=[...]'' define os valores para as outras colunas na 
                # Treeview. Como é o agrupamento principal, a maioria é 
                # deixada em branco, exceto o salário.
        # 'open=False' inicia o agrupamento como fechado, o usuário 
                # pode expandi-lo para ver detalhes.
        # 'tags=("cidade",)' aplica uma tag para estilização 
                # condicional, definida anteriormente.
        cidade_id = tree.insert("", 
                                "end", 
                                text=cidade, 
                                values=["", "", "", "", salario_total], open=False, tags=("cidade",))
        
        # Busca dos registros individuais que correspondem à cidade 
                # atual para adicionar como filhos do item de 
                # cidade na Treeview.
        # 'df[df['Cidade'] == cidade]' filtra o DataFrame original 
                # para obter todos os registros que pertencem à cidade atual.
        registros_cidade = df[df['Cidade'] == cidade]

        # Continuação da inserção de dados na Treeview para cada cidade.
        for _, detalhe in registros_cidade.iterrows():
            
            # Conversão dos dados de cada registro individual 
                    # em uma lista para fácil manipulação.
            # 'list(detalhe)' converte a série de dados do pandas (cada 
                    # linha do DataFrame) em uma lista de valores.
            valores = list(detalhe)
            
            # Formatação do salário, que está no índice 4 da lista, 
                    # para incluir separadores de milhares.
            # 'formatar_salario(valores[4])' aplica a função de 
                    # formatação de salário ao quinto elemento da 
                    # lista (índice 4).
            valores[4] = formatar_salario(valores[4])
            
            # Limpeza do valor da cidade para os registros 
                    # detalhados para evitar redundância, 
            # já que a cidade já está indicada no item pai na Treeview.
            # 'valores[0] = ""' define o primeiro elemento da 
                    # lista (índice 0, cidade) como uma string vazia.
            valores[0] = ""
            
            # Inserção de cada registro detalhado como um filho do item 
                    # de cidade correspondente na Treeview.
            # 'tree.insert(cidade_id, "end", values=valores)' insere os 
                    # detalhes do registro como um item filho do item de cidade,
            # usando 'cidade_id' como o identificador do pai, 'end' indica 
                    # que o item será adicionado ao final da lista de filhos.
            tree.insert(cidade_id, "end", values=valores)
        
        # Configuração do estilo para as linhas que têm a tag 'cidade'.
        # 'tree.tag_configure("cidade", background="yellow")' configura o 
                # fundo das linhas com a tag 'cidade' para amarelo,
        # permitindo uma distinção visual clara entre as linhas de 
                # agrupamento de cidades e as linhas de detalhes individuais.
        tree.tag_configure("cidade", 
                           background="yellow")
        
        # Chamada de função para atualizar a visibilidade das colunas com 
                # base em configurações de exibição especificadas.
        # 'atualizar_visibilidade_colunas()' é uma função definida 
                # anteriormente que controla quais colunas são visíveis
                # baseado em uma configuração de colunas ocultas ou mostradas.
        atualizar_visibilidade_colunas()


# Definição da função 'filtrar_dados' que é chamada para filtrar os 
        # dados exibidos na Treeview com base nos valores 
        # inseridos nos campos de filtro.
def filtrar_dados(*args):
    
    # Primeiramente, todos os dados existentes na Treeview são 
            # removidos para preparar para uma nova exibição 
            # de dados filtrados.
    # 'tree.delete(*tree.get_children())' limpa todos os 
            # itens filhos da Treeview, removendo qualquer 
            # dado anteriormente exibido.
    tree.delete(*tree.get_children())

    # Criação de uma cópia do DataFrame original para não 
            # alterar os dados originais durante o processo de filtragem.
    # 'df.copy()' cria uma cópia independente do DataFrame 'df'.
    df_filtrado = df.copy()

    # Loop para verificar cada campo de entrada de filtro e 
            # aplicar o filtro correspondente ao DataFrame.
    for col, entry in filtros.items():
        
        # Obtém o valor digitado no campo de entrada, remove 
                # espaços extras e converte para minúsculas 
                # para padronização.
        # 'entry.get().strip().lower()' extrai o texto do 
                # campo de entrada, remove espaços em branco no 
                # início e no fim e converte para minúsculas.
        filtro_valor = entry.get().strip().lower()
        
        # Se um valor de filtro foi inserido, aplicar esse 
                # filtro ao DataFrame.
        # Checa se 'filtro_valor' não está vazio, o que indica 
                # que um filtro deve ser aplicado.
        if filtro_valor:
            
            # Filtra o DataFrame 'df_filtrado' para incluir apenas 
                    # linhas que contêm o texto de filtro na coluna especificada.
            # 'df_filtrado[col].astype(str).str.lower().str.contains(filtro_valor)' 
                    # converte os valores da coluna 'col' para string e minúsculas,
            # e verifica se eles contêm o 'filtro_valor'. O DataFrame é atualizado 
                    # apenas com as linhas que correspondem ao critério de filtro.
            df_filtrado = df_filtrado[df_filtrado[col].astype(str).str.lower().str.contains(filtro_valor)]


    # Agrupamento dos dados filtrados por cidade e cálculo da soma dos 
            # valores numéricos para cada grupo.
    # 'df_filtrado.groupby('Cidade', as_index=False).sum()' agrupa os 
            # dados no DataFrame 'df_filtrado' pela coluna 'Cidade',
    # 'as_index=False' mantém 'Cidade' como uma coluna regular, não como 
            # índice, e 'sum()' calcula a soma de todas as colunas 
            # numéricas para cada grupo.
    df_grouped = df_filtrado.groupby('Cidade', as_index=False).sum()
    
    # Iteração sobre cada linha dos dados agrupados para inserir os 
            # resultados na Treeview.
    for _, linha in df_grouped.iterrows():
        
        # Acessando o nome da cidade e o salário total da 
                # cidade atualmente iterada.
        cidade = linha['Cidade']
        
        # Formatação do salário total usando a função definida 
                # anteriormente para incluir separadores de milhares.
        salario_total = formatar_salario(linha['Salário'])
        
        # Inserção do agrupamento principal na Treeview. Este item agirá 
                # como um nó pai para os detalhes individuais de cada cidade.
        # 'tree.insert("", "end", text=cidade, ...)' insere um novo item na 
                # Treeview com o nome da cidade como texto principal.
        # 'values=["", "", "", "", salario_total]' define os valores para as 
                # outras colunas na Treeview. A maioria é deixada em 
                # branco, exceto o salário.
        # 'open=False' define o item para iniciar fechado, e 'tags=("cidade",)' 
                # aplica uma tag para estilização condicional, 
                # definida anteriormente.
        cidade_id = tree.insert("", 
                                "end", 
                                text=cidade, 
                                values=["", "", "", "", 
                                salario_total], 
                                open=False, 
                                tags=("cidade",))

        
        # Continuação do loop para adicionar detalhes dos registros 
                # individuais de cada cidade na Treeview como itens 
                # filhos do nó da cidade correspondente.
        # Filtragem dos registros do DataFrame que pertencem à 
                # cidade atual iterada.
        # 'df_filtrado[df_filtrado['Cidade'] == cidade]' seleciona 
                # somente os registros no DataFrame 'df_filtrado' que 
                # têm a mesma cidade que a cidade atual.
        registros_cidade = df_filtrado[df_filtrado['Cidade'] == cidade]
        
        # Iteração sobre cada registro (detalhe) da cidade para 
                # adicionar como um item filho na Treeview sob o item da cidade.
        for _, detalhe in registros_cidade.iterrows():
            
            # Conversão do registro (linha do DataFrame) em uma 
                    # lista para manipulação mais fácil dos valores.
            valores = list(detalhe)
            
            # Formatação do salário, que está na quinta posição da 
                    # lista (índice 4), para incluir separadores de milhares.
            # 'formatar_salario(valores[4])' aplica a função de formatação 
                    # de salário ao valor na quinta coluna, melhorando a legibilidade.
            valores[4] = formatar_salario(valores[4])
            
            # Limpeza da coluna da cidade nos detalhes para evitar 
                    # redundância visual, já que o nome da cidade já está no item pai.
            # 'valores[0] = ""' define o primeiro valor da 
                    # lista (cidade) como uma string vazia.
            valores[0] = ""
            
            # Inserção do registro detalhado como um item filho na 
                    # Treeview sob o item correspondente à cidade.
            # 'tree.insert(cidade_id, "end", values=valores)' insere 
                    # os detalhes do registro na Treeview.
            # 'cidade_id' é o identificador do item pai na Treeview, 'end' 
                    # indica que o item será adicionado ao final da 
                    # lista de itens filhos.
            # 'values=valores' passa a lista de valores modificada para 
                    # ser exibida nas colunas da Treeview.
            tree.insert(cidade_id, "end", values=valores)


    # Aplicar o estilo às linhas com a tag 'cidade'
    tree.tag_configure("cidade", background="yellow")

    # Atualizar visibilidade das colunas
    atualizar_visibilidade_colunas()
        

# Definição da função 'atualizar_visibilidade_colunas' que 
            # controla quais colunas são visíveis na Treeview.
def atualizar_visibilidade_colunas():
    
    # Verifica se as colunas devem ser ocultadas ou mostradas 
            # com base no valor da variável 'colunas_ocultas'.
    if colunas_ocultas:
        
        # Se 'colunas_ocultas' é verdadeiro, mostra todas as 
                # colunas exceto a primeira.
        # 'tree["displaycolumns"] = colunas[1:]' configura as 
                # colunas visíveis para serem todas as colunas do 
                # DataFrame exceto a primeira ('Cidade').
        # Isso é feito ao especificar um slice da lista 'colunas' 
                # começando do segundo item até o final.
        tree["displaycolumns"] = colunas[1:]
        
        # Configuração do texto do botão 'btn_agrupar_colunas' para "-".
        # Isso indica que um clique no botão agora irá ocultar as 
                # colunas, já que atualmente todas as colunas 
                # adicionais estão sendo mostradas.
        btn_agrupar_colunas.config(text="-")
        
    else:
        
        # Se 'colunas_ocultas' é falso, mostra apenas a coluna 'Salário'.
        # 'tree["displaycolumns"] = ("Salário",)' configura a 
                # Treeview para mostrar apenas a coluna 'Salário'.
        # Esta linha define explicitamente quais colunas são 
                # visíveis passando uma tupla com o nome da coluna desejada.
        tree["displaycolumns"] = ("Salário",)
        
        # Configuração do texto do botão 'btn_agrupar_colunas' para "+".
        # Isso indica que um clique no botão agora irá mostrar 
                # mais colunas, já que atualmente apenas a coluna 
                # 'Salário' está sendo exibida.
        btn_agrupar_colunas.config(text="+")


# Definição da função 'toggle_colunas', que alterna a 
        # visibilidade das colunas na Treeview.
def toggle_colunas():
    
    # Uso da palavra-chave 'global' para modificar a 
            # variável global 'colunas_ocultas'.
    # Isso permite que a função altere o estado dessa 
            # variável global, que controla quais colunas 
            # são mostradas ou ocultadas.
    global colunas_ocultas
    
    # Alterna o valor booleano da variável 'colunas_ocultas'.
    # Se 'colunas_ocultas' for True, será definido como 
            # False, e vice-versa.
    # Isso efetivamente alterna o estado entre mostrar todas as 
            # colunas relevantes e mostrar apenas uma coluna 
            # específica (geralmente 'Salário').
    colunas_ocultas = not colunas_ocultas
    
    # Chamada da função 'atualizar_visibilidade_colunas' para 
            # aplicar a mudança de visibilidade na Treeview.
    # Essa função ajusta quais colunas são visíveis baseadas no 
            # estado atual de 'colunas_ocultas'.
    # Por exemplo, se 'colunas_ocultas' agora é True, a 
            # função configurará a Treeview para mostrar mais colunas.
    atualizar_visibilidade_colunas()


# Definição de uma variável 'colunas_ocultas' para controlar o 
        # estado inicial das colunas na Treeview.
# 'colunas_ocultas = False' inicializa a variável como 
        # False, indicando que, inicialmente, todas as 
        # colunas serão mostradas.
colunas_ocultas = False

# Criação de um botão que permitirá ao usuário alternar 
        # entre mostrar e ocultar colunas.
# 'tk.Button(janela, text="+", ...)' cria um botão 
        # na janela principal.
# 'text="+"' define o texto inicial do botão como "+", 
        # indicando que um clique inicial mostrará mais colunas (expandir).
# 'command=toggle_colunas' associa este botão à função 'toggle_colunas', 
        # que é chamada sempre que o botão é clicado.
# 'font=("Arial", 12)' define a fonte do texto do botão para Arial, 
        # tamanho 12, garantindo que o texto seja legível.
# 'width=3' define a largura do botão suficiente para acomodar o 
        # texto '+', assegurando que o botão tenha uma aparência uniforme.
btn_agrupar_colunas = tk.Button(janela, 
                                text="+", 
                                command=toggle_colunas, 
                                font=("Arial", 12), width=3)

# Posicionamento do botão na interface gráfica.
# 'btn_agrupar_colunas.grid(row=2, column=2, pady=(5, 10))' 
        # coloca o botão na terceira linha (row=2) e 
        # terceira coluna (column=2) da grid.
# 'pady=(5, 10)' adiciona um espaço vertical acima e abaixo 
        # do botão, melhorando a separação visual do botão em 
        # relação a outros elementos da interface.
btn_agrupar_colunas.grid(row=2, 
                         column=2, 
                         pady=(5, 10))

# Configuração do comportamento de redimensionamento da 
        # janela para garantir que a interface seja responsiva.
# 'janela.grid_columnconfigure(0, weight=1)' configura a primeira 
        # coluna da grid na janela principal para ter um peso de 1.
# Isso significa que essa coluna vai expandir e contrair 
        # proporcionalmente conforme a janela é redimensionada, 
        # ajudando a manter a proporção visual dos elementos.
janela.grid_columnconfigure(0, weight=1)

# 'janela.grid_rowconfigure(3, weight=1)' faz o mesmo 
        # para a quarta linha da janela principal (índice 3).
# Definindo o peso como 1, essa linha também se ajustará 
        # dinamicamente com o redimensionamento da janela.
janela.grid_rowconfigure(3, weight=1)

# Configuração dos campos de entrada (filtros) para acionar a 
        # função de filtragem sempre que uma tecla for liberada.
# Este loop percorre todos os campos de entrada armazenados 
        # no dicionário 'filtros'.
for entry in filtros.values():
    
    # 'entry.bind("<KeyRelease>", filtrar_dados)' associa o evento 
            # de liberação de tecla (KeyRelease) à função 'filtrar_dados'.
    # Isso significa que cada vez que uma tecla for solta após ser 
            # pressionada em qualquer um dos campos de entrada, a 
            # função 'filtrar_dados' será chamada.
    # Isso permite uma resposta imediata do aplicativo ao input 
            # do usuário, atualizando os dados filtrados conforme 
            # o usuário digita.
    entry.bind("<KeyRelease>", filtrar_dados)

    
# Chamada inicial à função 'carregar_dados' para preencher a 
        # Treeview com os dados do DataFrame ao iniciar o aplicativo.
carregar_dados()

# Início do loop principal da interface gráfica que mantém a 
        # janela aberta e responsiva a eventos do usuário.
janela.mainloop()