# Importar a biblioteca Dash para criar o aplicativo web interativo
import dash

# Importar componentes específicos de Dash, como
# dcc para componentes interativos e html para marcação HTML
from dash import dcc, html, Input, Output

# Importar Plotly Express para criar gráficos interativos
import plotly.express as px

# Importar a biblioteca Pandas para manipulação e análise de dados
import pandas as pd

# Criar um DataFrame usando Pandas para armazenar os dados de exemplo
# 'Frutas' representa os tipos de frutas e 'Quantidade' suas respectivas quantidades
# O DataFrame será composto por três linhas e duas colunas
df = pd.DataFrame({
    'Frutas': ['Maçã', 'Banana', 'Laranja'],  # Coluna 'Frutas' com os nomes das frutas
    'Quantidade': [10, 20, 30]  # Coluna 'Quantidade' com a quantidade de cada fruta
})

# Definir um dicionário chamado 'estilos' para armazenar vários
# conjuntos de estilos CSS que serão usados no layout do aplicativo Dash
estilos = {

    # Definir o estilo para o elemento que servirá como painel lateral do aplicativo
    'painel': {
        'width': '25%',  # Define a largura do painel como 25% da largura total disponível
        'display': 'inline-block',  # Faz o elemento ser exibido inline, mas permite o uso de propriedades de bloco
        'verticalAlign': 'top',  # Alinha o elemento verticalmente ao topo
        'backgroundColor': '#f7f7f7',  # Define a cor de fundo do painel como um cinza claro
        'borderRadius': '15px',  # Arredonda os cantos do painel com um raio de 15 pixels
        'padding': '15px'  # Adiciona um preenchimento interno de 15 pixels em todos os lados do painel
    },

    # Definir o estilo para o elemento que servirá como conteúdo principal do aplicativo
    'conteudo': {
        'width': '70%',  # Define a largura do conteúdo como 70% da largura total disponível
        'display': 'inline-block',  # Similar ao 'painel', faz com que o elemento seja exibido inline, mas permite o uso de propriedades de bloco
        'borderRadius': '15px',  # Arredonda os cantos do conteúdo com um raio de 15 pixels
        'padding': '15px'  # Adiciona um preenchimento interno de 15 pixels em todos os lados do conteúdo
    },

    # Definir o estilo para o elemento que servirá como cabeçalho do aplicativo
    'cabecalho': {
        'textAlign': 'center',  # Alinha o texto do cabeçalho ao centro
        'marginBottom': 50,  # Adiciona uma margem inferior de 50 pixels para separá-lo dos elementos abaixo
        'marginTop': 50  # Adiciona uma margem superior de 50 pixels para separá-lo dos elementos acima
    },
}

# Inicializar o aplicativo
app = dash.Dash(__name__)

# O layout geral do aplicativo é definido através de uma Div HTML
# principal que irá conter todos os outros elementos.
app.layout = html.Div([

    # PRIMEIRA DIV: Cabeçalho
    # Uma Div é usada para encapsular o cabeçalho do aplicativo.
    html.Div([

        # O cabeçalho é composto por um título de nível 1 (H1).
        # O atributo 'id' é definido como 'titulo' para permitir manipulações
        # futuras através de callbacks.
        # O atributo 'children' contém o texto que será exibido como título.
        html.H1(id='titulo', children="Dashboard Estilizado"),
    ],

        # O estilo para esta Div é puxado do dicionário 'estilos' usando a chave 'cabecalho'.
        # Isso define a aparência do cabeçalho com alinhamento de texto, margens etc.
        style=estilos['cabecalho']),

    # SEGUNDA DIV: Painel lateral
    # Outra Div encapsula o painel lateral.
    html.Div([  # Abre uma nova Div

        # Um rótulo (Label) orienta o usuário a fazer uma seleção de cor.
        html.Label("Escolha uma cor:"),

        # O Dropdown permite que o usuário selecione uma cor.
        # A biblioteca Dash Component Collection (dcc) contém o componente Dropdown que estamos utilizando aqui.
        # Este componente cria um menu suspenso no frontend que permite ao usuário selecionar entre várias opções.
        dcc.Dropdown(

            # 'id' é definido para que possamos referenciar este elemento em callbacks.
            # O valor 'cor-dropdown' serve como um identificador único para este componente específico dentro da aplicação Dash.
            # Isso é crucial para quando você desejar referenciar este Dropdown em funções callback para atualizações dinâmicas.
            id='cor-dropdown',

            # 'options' define os pares de rótulos e valores que serão exibidos no dropdown.
            # A lista de dicionários fornecida aqui especifica quais opções serão exibidas
            # para o usuário e que valores serão retornados quando uma opção for selecionada.
            # 'label' é o que o usuário vê (por exemplo, "Vermelho"), e
            # 'value' é o valor correspondente que o backend recebe (por exemplo, "red").
            options=[
                {'label': 'Vermelho', 'value': 'red'},
                {'label': 'Verde', 'value': 'green'},
                {'label': 'Azul', 'value': 'blue'},
            ],

            # 'value' define a seleção padrão inicial do dropdown.
            # Quando o aplicativo é carregado pela primeira vez, o valor padrão
            # selecionado neste Dropdown será 'red'.
            # Isso pode ser usado, por exemplo, para definir um estado inicial para
            # o aplicativo ou um gráfico associado.
            value='red'
        ),

    ], style=estilos['painel']),  # Fecha a Div e aplica o estilo

    # TERCEIRA DIV: Conteúdo principal
    # A última Div encapsula o conteúdo principal da aplicação.
    html.Div([

        # Um espaço reservado para o gráfico é criado aqui.
        # 'id' é definido para que possamos atualizar este gráfico dinamicamente através de callbacks.
        dcc.Graph(
            id='barra-grafico'
        ),
    ],

        # O estilo para esta Div é puxado do dicionário 'estilos' usando a chave 'conteudo'.
        # Isso aplica várias propriedades de estilo ao conteúdo principal.
        style=estilos['conteudo'])
])


# Callback para atualizar o gráfico e o título
# A função de callback é uma das funcionalidades mais poderosas do Dash.
# Ela permite atualizar componentes na página web com base nas interações do usuário.
# Esta função é decorada com o decorador @app.callback.
@app.callback(

    # 'Output' especifica quais componentes da página serão atualizados quando
    # a função de callback for acionada.
    # Neste caso, estamos especificando que queremos atualizar a
    # propriedade 'figure' do componente com ID 'barra-grafico'
    # e a propriedade 'style' do componente com ID 'titulo'.
    # A propriedade 'figure' representa os dados e layout do gráfico,
    # e 'style' representa o estilo CSS do título.
    [Output('barra-grafico', 'figure'),
     Output('titulo', 'style')],

    # 'Input' define quais componentes da página irão acionar a função
    # de callback quando suas propriedades são alteradas.
    # Neste caso, estamos dizendo que a função de callback deve ser acionada
    # sempre que o valor do Dropdown com ID 'cor-dropdown' for alterado.
    # Isso permite que o gráfico e o título sejam atualizados em resposta
    # a uma mudança na seleção do Dropdown.
    [Input('cor-dropdown', 'value')]
)

# Define uma função chamada 'atualizar_grafico' que será chamada sempre que
# o usuário mudar a seleção do Dropdown.
# A variável 'cor_selecionada' contém o valor da cor selecionada pelo usuário no Dropdown.
def atualizar_grafico(cor_selecionada):

    # Utiliza a biblioteca Plotly Express para criar um gráfico de barras.
    # Os dados para o gráfico vêm do DataFrame 'df'.
    # O eixo x será preenchido com valores da coluna 'Frutas' e o eixo y com
    # valores da coluna 'Quantidade'.
    grafico_barra = px.bar(df, x='Frutas', y='Quantidade')

    # Atualiza a cor das barras do gráfico para corresponder à cor selecionada pelo usuário.
    # A função 'update_traces' é usada para atualizar atributos específicos das barras.
    grafico_barra.update_traces(marker_color=cor_selecionada)

    # Define o estilo do título do Dashboard, que inclui a cor selecionada.
    # Isso vai alinhar o texto ao centro e aplicar uma margem superior e inferior de 50 pixels.
    # A cor do texto será a mesma que o usuário selecionou.
    estilo_titulo = {'textAlign': 'center', 'marginBottom': 50, 'marginTop': 50, 'color': cor_selecionada}

    # Retorna dois valores: o objeto 'figure' atualizado que será renderizado como gráfico,
    # e o estilo atualizado do título. Esses valores correspondem às saídas definidas no 'callback'.
    return grafico_barra, estilo_titulo

# Inicia o servidor do aplicativo Dash
# O parâmetro 'debug=True' permite que o servidor seja reiniciado automaticamente sempre que o código fonte for alterado.
# Isso é útil durante o desenvolvimento para ver as mudanças em tempo real.
# O parâmetro 'port=8054' define que o servidor será executado na porta 8054 do localhost.
app.run(debug=True, port=8054)

