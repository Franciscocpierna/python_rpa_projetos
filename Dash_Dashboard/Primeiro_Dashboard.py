# Importa a biblioteca Dash principal. Dash é um framework Python para criar aplicativos web.
import dash

# Importa elementos HTML e gráficos (dcc) da biblioteca Dash. Isso nos permite usar tags HTML e componentes gráficos.
from dash import html, dcc

# Importa a biblioteca dash-bootstrap-components. Essa biblioteca fornece componentes do Bootstrap para serem usados no Dash.
import dash_bootstrap_components as dbc

# Inicializa o aplicativo Dash. 
# O argumento `__name__` é necessário para que o Dash saiba onde encontrar os arquivos do aplicativo.
# `external_stylesheets` nos permite adicionar folhas de estilo externas, neste caso, estamos adicionando o Bootstrap.
aplicativo = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define o layout do aplicativo.
# Usamos `dbc.Container` para criar um container que irá conter todos os elementos do layout.
# O argumento `fluid=True` faz com que o container ocupe todo o espaço disponível horizontalmente.
aplicativo.layout = dbc.Container([

    # Cria uma linha usando `dbc.Row`. As linhas são usadas para conter colunas.
    # Dentro dessa linha, temos uma coluna única `dbc.Col`.
    # A tag `html.H1` define o título do aplicativo como "Meu Primeiro Dashboard".
    dbc.Row(dbc.Col(html.H1("Meu Primeiro Dashboard"))),

    # Adiciona um espaço entre os elementos usando `html.Br()`,
    # que representa uma quebra de linha no HTML.
    html.Br(),

    # Cria uma linha contendo uma coluna única com um parágrafo.
    # `dbc.Row` define uma nova linha no layout do Bootstrap.
    # `dbc.Col` cria uma coluna dentro dessa linha.
    # `html.P` é usado para inserir um parágrafo de texto dentro dessa coluna.
    dbc.Row(dbc.Col(html.P("Este é um parágrafo de texto."))),

    # Adiciona outro espaço entre os elementos com outra quebra de linha.
    html.Br(),

    # Cria uma linha contendo duas colunas para listar itens.
    dbc.Row([

        # Primeira coluna contendo uma lista não ordenada.
        # `html.Ul` cria uma lista não ordenada (Unordered List).
        # `html.Li` são os itens de lista (List Items) que ficam dentro da lista não ordenada.
        # `width={"size": 6}` define que essa coluna deve ocupar 6 das 12 colunas disponíveis no sistema de grid do Bootstrap.
        dbc.Col(html.Ul([
            html.Li("Primeiro item da lista"),
            html.Li("Segundo item da lista"),
            html.Li("Terceiro item da lista"),
        ]), width={"size": 6}),

        # Segunda coluna contendo uma lista ordenada.
        # `html.Ol` cria uma lista ordenada (Ordered List).
        # `html.Li` são os itens de lista (List Items) que ficam dentro da lista ordenada.
        # `width={"size": 6}` define que essa coluna deve ocupar 6 das 12 colunas disponíveis no sistema de grid do Bootstrap.
        dbc.Col(html.Ol([
            html.Li("Item numerado 1"),
            html.Li("Item numerado 2"),
        ]), width={"size": 6}),

    ]),  # Fim da dbc.Row

    # Adiciona um espaço entre os elementos anteriores e os
    # próximos usando `html.Br()`, que representa uma quebra de linha no HTML.
    html.Br(),

    # Cria uma linha com uma coluna única para abrigar um link externo.
    # `dbc.Row` cria uma nova linha no layout.
    # `dbc.Col` define uma coluna dentro dessa linha.
    # `html.A` cria uma âncora, ou seja, um link, com o texto "Clique
    # aqui para ir ao Google" e o atributo `href` definido para o URL do Google.
    dbc.Row(dbc.Col(html.A("Clique aqui para ir ao Google", href="https://www.google.com"))),

    # Adiciona outro espaço entre os elementos com uma quebra de linha usando `html.Br()`.
    html.Br(),

    # Cria uma linha com uma coluna única para um botão clicável.
    # `dbc.Row` e `dbc.Col` são usados para criar a linha e a coluna, respectivamente.
    # `html.Button` cria um botão com o texto "Clique em mim" e um
    # identificador (id) "botao_clicavel" para eventuais manipulações via callback.
    dbc.Row(dbc.Col(html.Button("Clique em mim", id="botao_clicavel"))),

    # Adiciona um último espaço entre os elementos usando
    # `html.Br()` para uma quebra de linha.
    html.Br(),

    # Cria uma tabela de dados usando `dbc.Table`.
    # `dbc.Table` é um componente da biblioteca dash-bootstrap-components
    # que nos permite criar uma tabela de forma mais simplificada, aproveitando o
    # estilo do Bootstrap.
    dbc.Table([

        # Cria o cabeçalho da tabela usando `html.Thead`, que
        # representa o elemento <thead> em HTML.
        # Este elemento é usado para agrupar as células de cabeçalho em uma tabela.
        html.Thead([

            # Cria uma linha de cabeçalho usando `html.Tr`, que representa
            # o elemento <tr> (table row) em HTML.
            # Este elemento é usado para definir uma linha na tabela.
            html.Tr([

                # Cria células de cabeçalho usando `html.Th`, que representa o
                # elemento <th> (table header cell) em HTML.
                # Estas células aparecem como cabeçalhos das colunas na tabela.
                html.Th("Cabeçalho 1"),
                html.Th("Cabeçalho 2"),
            ]),
        ]),

        # Cria o corpo da tabela usando `html.Tbody`, que
        # representa o elemento <tbody> em HTML.
        # Este elemento é usado para agrupar as células do corpo em uma tabela.
        html.Tbody([

            # Cria uma linha de corpo usando `html.Tr`.
            # Esta linha contém as células de dados da tabela.
            html.Tr([

                # Cria células de dados usando `html.Td`, que
                # representa o elemento <td> (table data cell) em HTML.
                # Estas células contêm os dados da tabela.
                html.Td("Célula 1"),
                html.Td("Célula 2"),
            ]),
        ]),
    ]),


], fluid = True)  # Fim do dbc.Container, o argumento `fluid=True` faz
# com que o container ocupe todo o espaço horizontal disponível.


# Verifica se este script é o arquivo principal que está sendo executado.
# Se for o caso, o bloco de código abaixo será executado.
if __name__ == '__main__':
    # aplicativo.run_server(debug=True)

    # Inicializa e executa o servidor web do Dash.
    # O método `run_server` é chamado no objeto `aplicativo`, que
    # é uma instância da classe Dash.
    # Isso coloca o aplicativo Dash em execução.

    # O argumento `debug=True` ativa o modo de depuração. Isso permite
    # que o servidor recarregue automaticamente sempre que o código for alterado.
    # O argumento `port=8051` define a porta em que o servidor web será hospedado.
    # O padrão geralmente é 8050, mas aqui é definido como 8051 para evitar
    # conflitos ou para especificar uma porta.
    #aplicativo.run_server(debug=True, port=8051)A função run_server foi descontinuada e substituída pela função mais curta run.
    aplicativo.run(debug=True, port=8051)
