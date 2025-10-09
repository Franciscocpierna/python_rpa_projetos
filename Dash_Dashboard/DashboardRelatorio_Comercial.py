# Importa o módulo "dash" para criar o aplicativo web.
import dash

# Importa os componentes específicos necessários para construir
# o layout e as interações do aplicativo.
from dash import dcc, html, Input, Output

# Importa a biblioteca "plotly.express" para criar gráficos.
import plotly.express as px

# Importa a biblioteca "pandas" para manipulação e análise de dados.
import pandas as pd

# Para mais controle sobre o gráfico
import plotly.graph_objects as go

# Cria uma nova instância do aplicativo Dash.
# O argumento "__name__" é uma variável especial do Python que obtém o nome do script atual.
# É comumente usado para iniciar o servidor web interno do Dash.
aplicativo = dash.Dash(__name__)

# Define o caminho do arquivo Excel que será carregado.
# O 'r' antes da string indica uma string "crua", o que significa que
# os caracteres de escape (como o '\') são tratados como caracteres comuns.
caminho_arquivo = r"Relatorio_Comercial.xlsx"

# Usa a função "read_excel" da biblioteca Pandas para carregar a planilha Excel no DataFrame.
# O argumento "sheet_name='Dados'" especifica qual aba da planilha será carregada.
dataframe = pd.read_excel(caminho_arquivo, sheet_name='Dados')

# Converte a coluna "Mês" do DataFrame para uma lista.
# O método "tolist()" converte os valores da série Pandas em uma lista padrão do Python.
# "dataframe['Mês']" seleciona a coluna chamada "Mês" no DataFrame.
# O resultado é uma lista de meses que será usada para alimentar um componente de dropdown, por exemplo.
# lista_meses = dataframe['Mês'].tolist()
lista_meses = dataframe['Mês'].unique().tolist()

# Pega todas as colunas do DataFrame, exceto a primeira (que é "Mês"), e as converte em uma lista.
# "dataframe.columns" retorna um objeto indexável com os nomes de todas as colunas.
# "[1:]" é uma fatia que exclui o primeiro elemento (a coluna "Mês").
# O método "tolist()" converte esses nomes de coluna em uma lista padrão do Python.
# Essa lista será usada para representar diferentes "canais" em nosso conjunto de dados.
lista_canais = dataframe.columns[1:].tolist()

# Cria um dicionário para armazenar informações de vendas.
# A chave do dicionário é o "Mês" e o valor é uma lista de vendas para cada canal.
# "dataframe.iterrows()" é uma função que retorna um iterador produzindo pares
# índice (não usado aqui, portanto, "_") e linha como Series do Pandas.
# "linha[1:].tolist()" pega todos os elementos da linha, exceto o primeiro (que é o "Mês"), e os converte em uma lista.
# Isso é feito para cada linha do DataFrame, resultando em um dicionário de vendas organizado por mês.
# dicionario_vendas = {linha['Mês']: linha[1:].tolist() for _, linha in dataframe.iterrows()}

# Inicia um dicionário vazio para armazenar os dados que serão usados nos gráficos.
# A chave deste dicionário será o mês e o valor será uma lista das vendas nos diferentes canais para aquele mês.
dicionario_vendas = {}

# Utiliza o método 'iterrows()' para iterar por todas as linhas do DataFrame 'dataframe'.
# Este método retorna dois valores a cada iteração: o índice da linha e os dados da linha como uma Series do Pandas.
# O índice é descartado aqui usando '_', pois não é necessário para esta operação.
for _, linha in dataframe.iterrows():

    # 'linha' é uma Series do Pandas contendo os dados de uma linha do DataFrame.
    # Aqui, pegamos o valor na coluna 'Mês' dessa linha e armazenamos na variável 'chave'.
    # Essa 'chave' será usada para inserir dados no dicionário 'dicionario_vendas'.
    chave = linha['Mês']

    # Utiliza a fatia [1:] na Series 'linha' para ignorar o primeiro elemento (que é o valor da coluna 'Mês').
    # O resultado é uma Series contendo apenas os valores das vendas nos diferentes canais para o mês em questão.
    # O método 'tolist()' converte essa Series em uma lista de Python, que é armazenada na variável 'valor'.
    valor = linha[1:].tolist()

    # Insere o par (chave, valor) no dicionário 'dicionario_vendas'.
    # Isso associa o mês (chave) com a lista das vendas nos diferentes canais (valor).
    dicionario_vendas[chave] = valor

# Define um dicionário chamado "estilos" para armazenar os estilos CSS que serão
# aplicados aos elementos do layout do Dash.
# Isso facilita a manutenção e alteração dos estilos, já que eles estão centralizados em um único lugar.
estilos = {

    # Define o estilo para os rótulos dos filtros (dropdowns ou outros componentes interativos).
    # 'display': 'block' garante que o rótulo ocupe toda a linha horizontal, facilitando
    # o posicionamento de elementos subsequentes.
    # 'color': '#fff' define a cor do texto do rótulo como branco.
    'rotulo_filtro': {'display': 'block', 'color': '#fff'},

    # Define o estilo para as caixas de seleção (dropdowns) que servirão como filtros.
    # 'width': '90%' define a largura da caixa de seleção como 90% da largura do
    # contêiner pai, proporcionando algum espaço à direita.
    # 'color': '#000' define a cor do texto dentro da caixa de seleção como preto.
    # 'marginBottom': '10px' adiciona uma margem inferior de 10 pixels, ajudando
    # a separar visualmente cada caixa de seleção uma da outra.
    'caixa_selecao_filtro': {'width': '90%', 'color': '#000', 'marginBottom': '10px'}

}

# Define o layout geral do aplicativo Dash, que é essencialmente o esqueleto HTML da página da web.
# Utilizamos o método 'html.Div' para criar um contêiner div HTML.
aplicativo.layout = html.Div([

    # Dentro do contêiner geral, criamos outro contêiner div para conter o título do relatório.
    html.Div([

        # O título do relatório é "RELATÓRIO COMERCIAL".
        # Usamos o componente 'html.H1' para criar um cabeçalho de nível 1.
        # A propriedade 'style' é usada para aplicar estilos CSS ao cabeçalho.
        # 'textAlign': 'center' alinha o texto ao centro da div.
        # 'color': '#fff' torna a cor do texto branco.
        # 'marginBottom': '20px' adiciona uma margem inferior de 20 pixels,
        # separando visualmente o cabeçalho de outros elementos abaixo dele.
        html.H1("RELATÓRIO COMERCIAL", style={'textAlign': 'center',
                                              'color': '#fff',
                                              'marginBottom': '20px'}),

        # Estilos para o contêiner div que envolve o cabeçalho.
        # 'background-color': '#2B3E50' define a cor de fundo do contêiner como um tom de azul escuro.
        # 'padding': '20px' adiciona um preenchimento de 20 pixels ao redor do
        # contêiner, separando o cabeçalho das bordas da div.
    ], style={'background-color': '#2B3E50', 'padding': '20px'}),

    # Cria um novo contêiner div HTML que servirá como a seção onde os filtros serão colocados.
    html.Div([

        # Dentro deste contêiner, cria outro contêiner div para conter os
        # elementos individuais do filtro.
        html.Div([

            # Cria um rótulo HTML para o filtro do mês com o texto "Mês".
            # Utiliza a propriedade 'style' para aplicar os estilos definidos
            # na variável 'estilos' sob a chave 'rotulo_filtro'.
            html.Label("Mês", style=estilos['rotulo_filtro']),

            # Cria um menu suspenso (Dropdown) para a seleção do mês.
            # 'id' é usado para identificar este elemento para futuras interações programáticas.
            # 'options' define as opções disponíveis no menu suspenso, que são os meses
            # retirados da variável 'lista_meses'.
            # 'value' define o valor padrão selecionado, que é o primeiro item em 'lista_meses'.
            # 'style' aplica estilos ao menu suspenso, que são retirados da variável 'estilos'
            # sob a chave 'caixa_selecao_filtro'.
            dcc.Dropdown(id='filtro_mes', options=[{'label': mes, 'value': mes} for mes in lista_meses],
                         value=lista_meses[0], style=estilos['caixa_selecao_filtro']),


            # Estilos para o contêiner div que envolve os elementos do filtro.
            # 'width': '20%' define a largura do contêiner como 20% da largura do contêiner pai.
            # 'backgroundColor': '#2B3E50' define a cor de fundo como um tom de azul escuro.
            # 'padding': '20px' adiciona um preenchimento de 20 pixels ao redor do contêiner.
            # 'color': '#fff' torna a cor do texto branco.
        ], style={'width': '20%', 'backgroundColor': '#2B3E50', 'padding': '20px', 'color': '#fff'}),

        # Cria um contêiner div HTML que serve como a seção principal para conter os gráficos.
        html.Div([

            # Dentro deste contêiner div, adiciona um gráfico com o identificador 'grafico_mes'.
            # A propriedade 'style' é usada para definir a altura do gráfico como 300 pixels.
            dcc.Graph(id='grafico_mes', style={'height': '300px'}),

            # Adiciona um contêiner div para criar um espaço vertical de 20 pixels entre os dois gráficos.
            # Isso é feito definindo a propriedade 'height' como '20px'.
            html.Div(style={'height': '20px'}),

            # Semelhante ao primeiro gráfico, adiciona outro gráfico com o identificador 'grafico_canal'.
            # Também define a altura do gráfico como 300 pixels.
            dcc.Graph(id='grafico_canal', style={'height': '300px'}),

            # Define os estilos para este contêiner div que envolve os gráficos.
        ], style={'width': '78%',  # faz com que este contêiner ocupe 78% da largura do contêiner pai
                  'display': 'inline-block',  # permite que outros elementos sejam alinhados ao lado deste contêiner
                  'padding': '20px',  # adiciona um preenchimento de 20 pixels ao redor do contêiner
                  'backgroundColor': '#1A2633'  # define a cor de fundo como um tom de azul escuro
                  }),

        # Estilos para o contêiner div que engloba tanto os filtros quanto os gráficos.
    ], style={'display': 'flex'}),  # permite que os elementos filho sejam organizados em um layout flexível

    #  Estilos para o contêiner div geral, que é o nível mais alto e engloba tudo.
    ], style={'fontFamily': 'Arial',  # define a família de fontes para todo o contêiner como Arial
                   'backgroundColor': '#1A2633',  # define a cor de fundo como um tom de azul escuro
                   'color': '#fff',  # define a cor do texto como branco
                   'width': '100%',  # faz com que o contêiner ocupe 100% da largura da tela
                   'height': '100vh',  # faz com que o contêiner ocupe 100% da altura da tela
                   'margin': '0',  # remove as margens ao redor do contêiner
                   'padding': '0'  # remove o preenchimento ao redor do contêiner
                  })


# Atualizando os gráficos com base nos filtros selecionados
@aplicativo.callback(  # Define um callback que atualiza componentes da interface
    [Output('grafico_mes', 'figure'),  # Primeiro componente a ser atualizado (um gráfico)
     Output('grafico_canal', 'figure')],  # Segundo componente a ser atualizado (outro gráfico)
    [Input('filtro_mes', 'value')]  # Primeiro input: valor do filtro de mês

)

# Define a função 'atualizar_graficos' que toma 'mes_selecionado' como argumento.
# Essa função será usada para atualizar os gráficos com base no mês selecionado.
def atualizar_graficos(mes_selecionado):

    # Inicializa uma nova figura de gráfico usando a classe 'Figure' do módulo 'plotly.graph_objects'.
    # Esta figura servirá como a base para qualquer gráfico subsequente.
    figura_receita_por_produto_e_mes = go.Figure()

    # A próxima parte do código verifica se um mês foi selecionado pelo usuário.
    # Se 'mes_selecionado' for None, isso significa que nenhum mês foi selecionado.
    if mes_selecionado is None:

        # Nesse caso, 'df_filtrado' é definido como o dataframe completo, ou seja,
        # a função usará todos os dados disponíveis para criar o gráfico.
        df_filtrado = dataframe

    else:

        # Se um mês foi selecionado (ou seja, 'mes_selecionado' não é None),
        # o código filtra o dataframe para incluir apenas os registros que correspondem a esse mês.
        # Isso é feito usando uma operação de filtragem no dataframe original.
        df_filtrado = dataframe[dataframe['Mês'] == mes_selecionado]

    # O código começa agrupando o dataframe filtrado 'df_filtrado' por duas colunas: 'Produto' e 'Mês'.
    # A função 'groupby' é usada para isso. Além disso, a coluna 'Receita' é somada para cada grupo.
    # Isso resulta em um novo dataframe onde você terá a receita total para cada combinação de produto e mês.
    # A função 'reset_index()' é chamada para redefinir o índice do novo dataframe,
    # tornando-o mais fácil de manipular posteriormente.
    df_agrupado_por_produto_e_mes = df_filtrado.groupby(['Produto', 'Mês'])['Receita'].sum().reset_index()

    # Aqui, uma nova figura de gráfico é inicializada usando a classe 'Figure' do módulo 'plotly.graph_objects'.
    # Esta figura servirá como a tela em branco onde os dados do gráfico serão plotados.
    # É uma boa prática inicializar uma nova figura sempre que você estiver criando
    # um novo gráfico para evitar sobreposição ou confusão com gráficos anteriores.
    figura_receita_por_produto_e_mes = go.Figure()

    # O loop 'for' começa iterando sobre os valores únicos na
    # coluna 'Mês' do dataframe 'df_agrupado_por_produto_e_mes'.
    # Isso significa que para cada mês único no dataframe, um novo
    # 'trace' (linha) será adicionado ao gráfico.
    for mes in df_agrupado_por_produto_e_mes['Mês'].unique():

        # Filtra o dataframe 'df_agrupado_por_produto_e_mes' para incluir apenas as
        # linhas que correspondem ao mês atual na iteração.
        # Isso nos dá um sub-dataframe 'df_mes' contendo apenas os dados para esse mês específico.
        df_mes = df_agrupado_por_produto_e_mes[df_agrupado_por_produto_e_mes['Mês'] == mes]

        # A função 'add_trace' é chamada para adicionar um novo 'trace' ao gráfico.
        # O tipo de trace é um gráfico de dispersão ('Scatter') com linhas, marcadores e texto.
        figura_receita_por_produto_e_mes.add_trace(
            go.Scatter(
                x=df_mes['Produto'],  # Eixo x representará os produtos.
                y=df_mes['Receita'],  # Eixo y representará a receita.
                mode='lines+markers+text',  # O gráfico terá linhas, marcadores e texto.
                name=str(mes),  # O nome do trace, que aparecerá na legenda, será o mês.
                text=[f'R${val:,.2f}' for val in df_mes['Receita']],
                # Texto formatado para aparecer acima de cada marcador.
                textposition='top center'  # A posição do texto será no topo e ao centro em relação ao marcador.
            )
        )

        # A função '.max()' é chamada na coluna 'Receita' do dataframe 'df_agrupado_por_produto_e_mes'.
        # Isso retornará o valor mais alto dessa coluna, que representa o pico de receita
        # alcançado em qualquer mês e produto.
        # Este valor será usado mais tarde para definir o alcance do eixo y
        # do gráfico, garantindo que todos os pontos de dados possam ser visualizados claramente.
        maximo_receita = df_agrupado_por_produto_e_mes['Receita'].max()

        # A função 'update_layout' é um método da classe 'Figure' do módulo 'plotly.graph_objects'.
        # Este método é usado para personalizar a aparência e o layout do gráfico, tornando-o mais
        # informativo e fácil de ler.
        figura_receita_por_produto_e_mes.update_layout(

            # O argumento 'title' recebe uma string que será usada como o título principal do gráfico.
            # Este título aparecerá na parte superior do gráfico e fornecerá uma
            # descrição geral do que o gráfico representa.
            title="Variação da Receita Total por Mês para Cada Produto",

            # O argumento 'xaxis' recebe um dicionário que contém várias configurações para o eixo x.
            # Aqui, estamos definindo a cor da grade do eixo x como cinza através da chave 'gridcolor'.
            xaxis=dict(gridcolor='gray'),

            # O argumento 'yaxis' também recebe um dicionário com várias configurações para o eixo y.
            yaxis=dict(

                # A cor da grade do eixo y também é definida como cinza.
                gridcolor='gray',

                # A chave 'range' define o intervalo do eixo y.
                # O valor mínimo do intervalo é definido como 0 para começar a partir do ponto de origem.
                # O valor máximo é definido como 'maximo_receita * 1.2', ou seja, 20% a mais que o valor máximo de receita.
                # Isso é feito para garantir que o gráfico tenha um pouco de espaço extra acima do ponto de dados
                # mais alto, tornando-o mais fácil de ler.
                range=[0, maximo_receita * 1.2]
            ),

            # A chave 'showlegend' é definida como 'False', o que significa que a legenda do gráfico será ocultada.
            # Isso pode ser útil quando a legenda não oferece informações adicionais úteis e pode distrair ou confundir o espectador.
            showlegend=False,

            # O argumento 'margin' recebe um dicionário para definir as margens ao redor do gráfico.
            # Isso é útil para controlar o espaço em branco ao redor do gráfico, tornando-o
            # mais esteticamente agradável e bem ajustado ao espaço disponível.
            # As margens superior (t),
            # inferior (b),
            # esquerda (l) e
            # direita (r) são todas definidas como 40 unidades de espaço.
            margin=dict(t=40, b=40, l=40, r=40)
        )

        # A primeira linha agrupa o dataframe 'df_filtrado' pela coluna 'Produto' e soma a receita para cada produto.
        # A função 'reset_index()' é chamada para redefinir o índice do dataframe resultante.
        # Além disso, 'sort_values' é usado para ordenar os produtos em ordem decrescente de receita.
        # Isso significa que o produto com a maior receita aparecerá primeiro no gráfico de barras.
        df_grouped_by_product = df_filtrado.groupby('Produto')['Receita'].sum().reset_index().sort_values(by='Receita',
                                                                                                          ascending=False)

        # A função 'px.bar' é chamada para criar um gráfico de barras usando 'plotly.express'.
        # Vários argumentos são passados para personalizar o gráfico:
        figura_receita_por_produto = px.bar(

            # O dataframe agrupado e ordenado é passado como o conjunto de dados de origem.
            df_grouped_by_product,

            # A coluna 'Produto' será usada para o eixo x, representando diferentes produtos.
            x='Produto',

            # A coluna 'Receita' será usada para o eixo y, representando a receita total para cada produto.
            y='Receita',

            # O título do gráfico é configurado para mostrar qual mês está sendo considerado.
            # O operador ternário é usado para verificar se 'mes_selecionado' é None ou não.
            # Se for None, o título mostrará 'Todos os Meses'; caso contrário, ele mostrará o mês específico.
            title=f"Receita Total por Produto em {mes_selecionado if mes_selecionado else 'Todos os Meses'}",

            # A coluna 'Receita' também será usada para adicionar rótulos de texto às barras.
            text='Receita',

            # A coluna 'Receita' será usada para colorir as barras, criando uma escala de cores baseada na receita.
            color='Receita'
        )

        # O método 'update_traces' é usado para atualizar as propriedades das barras no gráfico de barras.
        # Este método é útil quando você quer personalizar o aspecto visual ou adicionar anotações
        # aos elementos de traço (barras, neste caso) já existentes no gráfico.
        figura_receita_por_produto.update_traces(

            # O argumento 'texttemplate' é usado para formatar o texto que aparecerá dentro das barras.
            # O template '%{text}' indica que o texto original (definido anteriormente pelo
            # argumento 'text' em 'px.bar') será usado sem modificações.
            texttemplate='%{text}',

            # O argumento 'textposition' define a posição do texto dentro das barras.
            # Neste caso, o texto será posicionado 'inside', ou seja, dentro das barras.
            textposition='inside'
        )

        # O método 'update_layout' é chamado novamente, mas desta vez para atualizar apenas o eixo y do gráfico de barras.
        # Um dicionário é passado para o argumento 'yaxis' para definir a cor da grade como cinza.
        figura_receita_por_produto.update_layout(yaxis=dict(gridcolor='gray'))

        # Finalmente, as duas figuras 'figura_receita_por_produto_e_mes' e 'figura_receita_por_produto' são retornadas.
        # Isso sugere que este trecho de código faz parte de uma função que cria
        # ou atualiza esses dois gráficos e os retorna como saída.
        return figura_receita_por_produto_e_mes, figura_receita_por_produto

# 'debug=True' ativa o modo de depuração, permitindo atualizações em tempo real
# durante o desenvolvimento.
# 'port=8086' define a porta do servidor como 8086.
aplicativo.run(debug=True, port=8086)