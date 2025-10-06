# Importar a biblioteca Dash para construção de aplicações web interativas
import dash

# Importar componentes específicos do Dash para o layout e interatividade
from dash import dcc, html, Input, Output

# Importar Plotly para criação de gráficos
import plotly.express as px

# Importar Pandas para manipulação de dados
import pandas as pd

# Criar um DataFrame do Pandas com dados fictícios para exemplificar o dashboard
# A coluna 'Data' é gerada como uma série temporal desde 01/01/2025, com 12 períodos mensais
# A coluna 'Categoria' contém repetições das categorias 'Eletrônicos', 'Roupas' e 'Alimentos'
# A coluna 'Vendas' contém números arbitrários representando o volume de vendas
# A coluna 'Estado' contém repetições dos estados 'SP', 'RJ' e 'MG'
dados_vendas = pd.DataFrame({
    'Data': pd.date_range(start='2025-01-01', periods=12, freq='M'),  # Geração de datas
    'Categoria': ['Eletrônicos', 'Roupas', 'Alimentos'] * 4,  # Categorias de produtos
    'Vendas': [200, 150, 50, 220, 130, 60, 250, 100, 75, 230, 110, 80],  # Valores fictícios de vendas
    'Estado': ['SP', 'RJ', 'MG', 'SP', 'RJ', 'MG', 'SP', 'RJ', 'MG', 'SP', 'RJ', 'MG']  # Estados onde as vendas ocorreram
})


# Inicializar o aplicativo Dash
# O parâmetro __name__ é utilizado para que o Dash saiba onde
# encontrar os recursos estáticos da aplicação, caso haja algum
aplicativo = dash.Dash(__name__)

# Configuração do layout do aplicativo Dash
# A função html.Div() cria uma div HTML que atuará como contêiner para os
# outros elementos da interface
aplicativo.layout = html.Div([

    # Cria um cabeçalho H1 HTML com o texto "Dashboard de Vendas"
    # Este cabeçalho atua como o título principal da página web
    html.H1("Dashboard de Vendas"),  # Título

    # Cria um elemento Dropdown (menu suspenso) para seleção de categorias de produtos
    # dcc.Dropdown é um componente de Dash Core Components que gera
    # um elemento de menu suspenso na interface do usuário.
    dcc.Dropdown(

        # id é um identificador único para este componente Dropdown.
        # Este ID será usado para referenciar este elemento em funções de callback mais tarde.
        id='dropdown_categoria',

        # 'options' define as opções que serão exibidas no menu suspenso.
        # Utilizamos uma compreensão de lista para gerar dinamicamente essas opções com base nos dados.
        # 'dados_vendas['Categoria'].unique()' extrai todas as categorias únicas do DataFrame.
        # Cada categoria única se torna um dicionário com 'label' e 'value' iguais, que representam
        # o texto mostrado ao usuário e o valor real a ser usado no back-end, respectivamente.
        options=[{'label': i, 'value': i} for i in dados_vendas['Categoria'].unique()],

        # 'value' define o valor inicial para o Dropdown.
        # Quando o aplicativo é carregado, "Eletrônicos" será a categoria selecionada por padrão.
        value='Eletrônicos'  # Valor inicial
    ),

    # Cria um elemento Graph para exibir um gráfico de linha
    # O ID 'grafico_linha' é usado para referência em callbacks, para atualizar os dados do gráfico
    dcc.Graph(
        id='grafico_linha'
    ),

    # Cria um segundo elemento Graph para exibir um gráfico de barras
    # O ID 'grafico_barras' também é usado para referência em
    # callbacks, para atualizar os dados do gráfico
    dcc.Graph(
        id='grafico_barras'
    )
])


# Callback para atualizar os gráficos com base no valor selecionado no dropdown de categorias
# A anotação '@aplicativo.callback' é uma forma de definir uma função de
# retorno de chamada (callback) em Dash.

# 'Output' define os elementos da página que serão atualizados pelo callback.
# Neste caso, dois gráficos serão atualizados: 'grafico_linha' e 'grafico_barras'.
# O parâmetro 'figure' significa que estamos atualizando os dados e o layout desses gráficos.
@aplicativo.callback(

    [Output('grafico_linha', 'figure'),
     Output('grafico_barras', 'figure')],

    # 'Input' define o gatilho para o callback, ou seja, a mudança que aciona esta função.
    # Aqui, o gatilho é qualquer mudança no valor do Dropdown com ID 'dropdown_categoria'.
    [Input('dropdown_categoria', 'value')]
)
# Definição da função 'atualizar_graficos' que é chamada quando o valor do dropdown 'dropdown_categoria' é alterado.
# O parâmetro 'categoria_selecionada' recebe o valor atual selecionado no dropdown.
def atualizar_graficos(categoria_selecionada):

    # Filtrar o DataFrame 'dados_vendas' para incluir apenas as linhas
    # onde a 'Categoria' é igual ao valor selecionado no dropdown.
    # O resultado é armazenado no DataFrame 'dados_filtrados'.
    dados_filtrados = dados_vendas[dados_vendas['Categoria'] == categoria_selecionada]

    # Utilizar o Plotly Express para criar um gráfico de linha com os dados filtrados.
    # O eixo X mostra a 'Data', o eixo Y mostra as 'Vendas', e diferentes 'Estados'
    # são representados por cores diferentes.
    # O título do gráfico é gerado dinamicamente com base na 'categoria_selecionada'.
    grafico_linha = px.line(dados_filtrados, x='Data', y='Vendas', color='Estado',
                            title=f'Tendência de Vendas: {categoria_selecionada}')

    # Utilizar o Plotly Express para criar um gráfico de barras agrupadas com o
    # DataFrame original 'dados_vendas'.
    # O eixo X mostra o 'Estado', o eixo Y mostra as 'Vendas', e diferentes 'Categorias'
    # são representadas por cores diferentes.
    # O título do gráfico é 'Distribuição de Vendas por Estado e Categoria'.
    grafico_barras = px.bar(dados_vendas, x='Estado', y='Vendas', color='Categoria',
                            title='Distribuição de Vendas por Estado e Categoria')

    # A função retorna dois objetos de figura: 'grafico_linha' e 'grafico_barras'.
    # Estes objetos de figura serão usados para atualizar os gráficos no layout do aplicativo Dash.
    return grafico_linha, grafico_barras

# Inicia o servidor do aplicativo Dash
# O parâmetro 'debug=True' permite que o servidor seja reiniciado automaticamente sempre que o código fonte for alterado.
# Isso é útil durante o desenvolvimento para ver as mudanças em tempo real.
# O parâmetro 'port=8050' define que o servidor será executado na porta 8050 do localhost.
aplicativo.run(debug=True, port=8052)