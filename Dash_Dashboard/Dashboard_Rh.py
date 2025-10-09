# Importando a biblioteca Dash principal. Dash é uma biblioteca Python para criar aplicações web.
import dash

# Importando módulos e componentes específicos do Dash.
# dcc: Dash Core Components para componentes como gráficos.
# html: Para usar tags HTML.
# Input, Output e State: Para definir entradas, saídas e estados em callbacks.
# dash_table: Para criar tabelas.
from dash import dcc, html, Input, Output, State, dash_table

# Importando o pandas, uma biblioteca de manipulação e análise de dados.
import pandas as pd

# Importando o Plotly Express, uma biblioteca de visualização de dados.
import plotly.express as px

# Lendo um arquivo Excel que contém dados de funcionários.
# 'sheet_name='Dados'' especifica que estamos lendo a aba chamada 'Dados' no arquivo Excel.
# Armazenamos esses dados em uma variável chamada dados_funcionarios.
dados_funcionarios = pd.read_excel('Arquivo_RH.xlsx', sheet_name='Dados')

# Convertendo os dados lidos em um DataFrame do pandas para facilitar a manipulação e análise de dados.
# Armazenamos esse DataFrame em uma variável chamada df_funcionarios.
df_funcionarios = pd.DataFrame(dados_funcionarios)

# Inicializar o aplicativo
app = dash.Dash(__name__)

# Definindo o layout geral da aplicação Dash.
# html.Div cria uma nova divisão ou uma "caixa" onde colocaremos todos os elementos do layout.
app.layout = html.Div([

    # Criando uma nova divisão para o menu lateral dentro da divisão principal.
    # O objetivo é agrupar logicamente os componentes relacionados aos filtros.
    html.Div([

        # Adicionando um título de nível 2 (semelhante a <h2> em HTML) para a seção de filtros.
        html.H2('Filtros'),

        # Criando um menu suspenso (dropdown) para filtrar por departamento.

        dcc.Dropdown(

            # O ID 'filtro-departamento' é único e será usado para referenciar este componente em callbacks.
            id='filtro-departamento',  # Identificador único para este dropdown.

            # As opções do dropdown são criadas dinamicamente com base nos departamentos únicos do DataFrame.
            # Cada opção é um dicionário com um 'label' (texto exibido) e um 'value' (valor real).
            options=[{'label': dept, 'value': dept} for dept in df_funcionarios['Departamento'].unique()],

            value=[],  # Valor inicial é uma lista vazia, ou seja, nenhum departamento selecionado.
            multi=True,  # Permite seleção múltipla.

            # Placeholder é o texto exibido quando nenhuma opção está selecionada.
            placeholder='Selecione o Departamento'

        ),

        # Criando um segundo dropdown para filtrar por cargo.
        # Semelhante ao dropdown de departamento, mas as opções são baseadas nos cargos únicos do DataFrame.
        dcc.Dropdown(
            id='filtro-cargo',  # Identificador único para este dropdown.
            options=[{'label': cargo, 'value': cargo} for cargo in df_funcionarios['Cargo'].unique()],
            # Opções baseadas nos cargos únicos.
            value=[],  # Valor inicial é uma lista vazia, ou seja, nenhum cargo selecionado.
            multi=True,  # Permite seleção múltipla.
            placeholder='Selecione o Cargo'  # Texto exibido quando nenhuma opção está selecionada.
        ),

        # Adicionando uma linha horizontal para separar visualmente os componentes acima dos componentes abaixo.
        html.Hr(),

        # Adicionando um título de nível 3 (semelhante a <h3> em HTML) que diz "Total de Salários:".
        html.H3('Total de Salários:'),

        # Adicionando uma divisão que terá o ID 'soma-salarios'.
        # Este ID será usado para atualizar o conteúdo desta divisão com o total de salários através de um callback.
        html.Div(id='soma-salarios')

    ],  # Fim da Div do menu lateral.

    # Adicionando estilos à Div do menu lateral.
    # Definindo a largura como 20%, exibição como 'inline-block' e alinhamento vertical como 'top'.
    id='menu-lateral', style={'width': '20%', 'display': 'inline-block', 'vertical-align': 'top'}),

    # Iniciando uma nova Div para o conteúdo principal do aplicativo.
    html.Div([

        # Adicionando um título de nível 1 (semelhante a <h1> em HTML) que diz "Dashboard de RH".
        html.H1('Dashboard de RH'),

        # Adicionando um título de nível 2 para a seção da tabela, dizendo "Resumo dos Funcionários".
        html.H2('Resumo dos Funcionários'),

        # Criando uma tabela usando o componente dash_table.DataTable.
        dash_table.DataTable(

            id='tabela-funcionarios',  # Identificador único para esta tabela.

            # As colunas são criadas com base nas colunas do DataFrame, exceto a coluna 'ID'.
            # Utilizamos uma compreensão de lista para percorrer todas as colunas do
            # DataFrame original (df_funcionarios)
            # e criar um dicionário para cada coluna que não seja 'ID'.
            columns=[{'name': col, 'id': col, 'hideable': True} for col in df_funcionarios.columns if col != 'ID'],

            # Os dados para a tabela são extraídos do DataFrame df_funcionarios.
            # O método to_dict('records') converte o DataFrame em uma lista de dicionários,
            # onde cada dicionário representa uma linha da tabela.
            data=df_funcionarios.to_dict('records'),

            # O estilo da tabela é definido para permitir rolagem tanto
            # na horizontal ('overflowX') como na vertical ('overflowY').
            # Isso é útil caso a tabela seja muito grande para ser exibida em uma única tela.
            style_table={'overflowX': 'auto', 'overflowY': 'auto'},

            # Condições de estilo específicas são aplicadas aos dados da tabela.
            # No nosso caso, estamos formatando os números na coluna 'Salário'
            # para que apareçam como uma string de moeda.
            # O 'if': {'column_id': 'Salário'} especifica que a condição se aplica à coluna 'Salário'.
            # O 'type': 'numeric' e 'format': 'R$ {:,.0f}' são utilizados para
            # formatar os números como strings de moeda em reais.
            style_data_conditional=[
                {
                    'if': {'column_id': 'Salário'},
                    'type': 'numeric',
                    'format': 'R$ {:,.0f}'
                }
            ],

            # Limitando a exibição para 10 linhas por página na tabela.
            page_size=10,

            # Adicionando a opção de exportar os dados da tabela para um arquivo Excel.
            export_format='xlsx'
        ),

        # Iniciando uma nova Div para abrigar os gráficos.
        html.Div([

            # Adicionando um título de nível 2 (semelhante a <h2> em HTML) que
            # diz "Análise dos Funcionários".
            html.H2('Análise dos Funcionários'),

            # Incluindo o primeiro gráfico usando o componente dcc.Graph.
            # O ID 'grafico-departamento' será usado para atualizar o
            # conteúdo do gráfico através de um callback.
            dcc.Graph(

                # Identificador único para este gráfico.
                id='grafico-departamento',

                # Definindo estilos CSS inline para este gráfico.
                # 'width' controla a largura do gráfico como 49% da Div pai.
                # 'display' define que ele deve ser mostrado na mesma linha que o próximo gráfico.
                style={'width': '49%', 'display': 'inline-block'}
            ),

            # Incluindo o segundo gráfico usando o componente dcc.Graph.
            # O ID 'grafico-cargo' será usado para atualizar o conteúdo do gráfico através de um callback.
            dcc.Graph(
                id='grafico-cargo',  # Identificador único para este gráfico.

                # Definindo estilos CSS inline para este gráfico.
                # Similar ao primeiro gráfico, com 49% da largura da Div pai e exibição na mesma linha.
                style={'width': '49%', 'display': 'inline-block'}
            )

        ]),  # Fim da Div que abriga os gráficos.

    ],  # Fim da Div do conteúdo principal.

        # Adicionando estilos à Div do conteúdo principal.
        # A largura é definida como 75% e ela é exibida como um bloco inline.
        # 'marginLeft' é usado para adicionar um pequeno espaço à esquerda da Div.
        id='conteudo-principal', style={'width': '75%', 'display': 'inline-block', 'marginLeft': 20})

])  # Fim da Div raiz que encapsula todo o layout.


# Define um callback que será ativado com base nos valores dos
# componentes de entrada (Dropdowns de departamento e cargo).
# O callback atualiza vários componentes de saída: os dados
# da tabela, as figuras dos gráficos e o total de salários.
@app.callback(

    # Lista de componentes de saída que serão atualizados pelo callback.
    # 'tabela-funcionarios' terá seus dados ('data') atualizados.
    # 'grafico-departamento' e 'grafico-cargo' terão suas figuras ('figure') atualizadas.
    # 'soma-salarios' terá seu conteúdo textual ('children') atualizado.
    [Output('tabela-funcionarios', 'data'),
     Output('grafico-departamento', 'figure'),
     Output('grafico-cargo', 'figure'),
     Output('soma-salarios', 'children')],

    # Lista de componentes de entrada que ativam o callback.
    # 'filtro-departamento' e 'filtro-cargo' são os IDs dos componentes Dropdown.
    # 'value' é a propriedade que armazena o(s) valor(es) selecionado(s) em cada Dropdown.
    [Input('filtro-departamento', 'value'),
     Input('filtro-cargo', 'value')]
)

# Definição da função atualizar_conteudo que é chamada pelo callback.
# Recebe dois argumentos: departamentos_selecionados e cargos_selecionados,
# que vêm dos componentes Dropdown da interface.
def atualizar_conteudo(departamentos_selecionados, cargos_selecionados):

    # Cria uma cópia do DataFrame original para evitar alterações no DataFrame original.
    df_filtrado = df_funcionarios.copy()

    # Verifica se a lista departamentos_selecionados contém algum item.
    # Essa lista é preenchida com base na seleção do usuário no Dropdown de departamentos na interface.
    # Se a lista estiver vazia, isso significa que o usuário não fez nenhuma seleção,
    # e nesse caso, essa condição não será atendida.
    if departamentos_selecionados:

        # Utiliza o método .isin() do Pandas para filtrar o DataFrame.
        # Este método retorna uma Series de booleanos que identifica se cada elemento da coluna 'Departamento'
        # está presente na lista departamentos_selecionados.
        # O DataFrame df_filtrado é atualizado para incluir apenas as linhas onde o valor na coluna 'Departamento'
        # corresponde a algum valor na lista departamentos_selecionados.
        df_filtrado = df_filtrado[df_filtrado['Departamento'].isin(departamentos_selecionados)]

    # Verifica se a lista cargos_selecionados contém algum item.
    # Essa lista é preenchida com base na seleção do usuário no Dropdown de cargos na interface.
    # Se a lista estiver vazia, isso significa que o usuário não fez nenhuma seleção,
    # e nesse caso, essa condição não será atendida.
    if cargos_selecionados:

        # Utiliza o método .isin() do Pandas para filtrar o DataFrame.
        # Este método retorna uma Series de booleanos que identifica se cada elemento da coluna 'Cargo'
        # está presente na lista cargos_selecionados.
        # O DataFrame df_filtrado é atualizado para incluir apenas as linhas onde o valor na coluna 'Cargo'
        # corresponde a algum valor na lista cargos_selecionados.
        df_filtrado = df_filtrado[df_filtrado['Cargo'].isin(cargos_selecionados)]

    # Calcula a soma dos salários após o filtro e formata como uma string de moeda.
    soma_salarios = f"R$ {df_filtrado['Salário'].sum():,.2f}"

    # Utiliza o método .map() do Pandas para aplicar uma função lambda a cada elemento da coluna 'Salário'.
    # A função lambda formata cada valor numérico como uma string de moeda no formato "R$ X,XXX.XX".
    # Isso é feito utilizando f-strings e a formatação de números para incluir vírgulas como separadores de milhar e duas casas decimais.
    df_filtrado['Salário'] = df_filtrado['Salário'].map(lambda x: f"R$ {x:,.2f}")

    # Utiliza a biblioteca Plotly Express para criar um gráfico de barras.
    # O eixo X será preenchido com os valores da coluna 'Departamento' do DataFrame df_filtrado.
    # O título do gráfico é definido como 'Funcionários por Departamento'.
    # A variável fig1 armazena essa figura do gráfico para ser usada mais tarde.
    fig1 = px.bar(df_filtrado, x='Departamento', title='Funcionários por Departamento')

    # Utiliza a biblioteca Plotly Express para criar um gráfico de pizza.
    # O gráfico irá mostrar a distribuição de cargos com base nos valores da coluna 'Cargo' do DataFrame df_filtrado.
    # O título do gráfico é definido como 'Distribuição de Cargos'.
    # A variável fig2 armazena essa figura do gráfico para ser usada mais tarde.
    fig2 = px.pie(df_filtrado, names='Cargo', title='Distribuição de Cargos')

    # Retorna quatro elementos como saída do callback:
    # 1. Os dados da tabela filtrada, convertidos para um dicionário de registros para alimentar a tabela Dash.
    # 2. A figura do gráfico de barras (fig1).
    # 3. A figura do gráfico de pizza (fig2).
    # 4. A soma dos salários, previamente calculada e formatada como uma string de moeda.
    return df_filtrado.to_dict('records'), fig1, fig2, soma_salarios


# Executa o aplicativo Dash.
# O parâmetro debug=True permite o modo de depuração, e port=8075
# define a porta onde o app será hospedado.
app.run(debug=True, port=8075)