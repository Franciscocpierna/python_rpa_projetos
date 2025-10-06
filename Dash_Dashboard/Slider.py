# Importa o módulo 'dash' para criar o aplicativo web
import dash

# Importa componentes específicos de 'dash' para a criação do layout e interatividade
# dcc: Dash Core Components, para componentes interativos como sliders, gráficos etc.
# html: para criar elementos HTML básicos como Divs, títulos etc.
# Input, Output: para especificar entradas e saídas de callbacks (funções interativas)
from dash import dcc, html, Input, Output

# Inicia o aplicativo Dash
# '__name__' é uma variável especial que obtém o nome do script Python atual
# Isso é necessário para o Dash saber onde procurar por recursos estáticos, arquivos CSS etc.
aplicativo = dash.Dash(__name__)

# Define o layout do aplicativo, que é a estrutura visual da página web
aplicativo.layout = html.Div([  # Div é um container geral que engloba todos os elementos do layout

    # Cria um título (H1) para a página web e o centraliza usando estilo CSS
    html.H1("Exemplo de Slider com Dash", style={'textAlign': 'center'}),

    # Adiciona um Slider usando Dash Core Components (dcc)
    # O Slider permite selecionar um número entre 1 e 10
    dcc.Slider(
        id='id_slider_numero',  # Identificador único para o Slider, usado em callbacks
        min=1,  # Valor mínimo que o Slider pode ter
        max=10,  # Valor máximo que o Slider pode ter
        value=5,  # Valor inicial do Slider
        marks={i: str(i) for i in range(1, 11)},  # Marcadores no Slider, aqui numerados de 1 a 10
        step=1  # O valor mínimo pelo qual o Slider pode mudar
    ),

    # Adiciona uma Div para exibir o resultado do cálculo
    # O resultado será o quadrado do número selecionado no Slider
    # Utiliza estilo CSS para definir o tamanho da fonte como 24 e centralizar o texto
    html.Div(
        id='id_resultado_quadrado',  # Identificador único para a Div, usado em callbacks
        style={'fontSize': 24, 'textAlign': 'center'}
    )
])


# Define uma função de callback para atualizar o resultado na página
# As funções de callback são usadas no Dash para tornar o aplicativo interativo
@aplicativo.callback(

    # Especifica a saída (Output) da função de callback
    # 'id_resultado_quadrado' é o ID do elemento HTML que será atualizado
    # 'children' é a propriedade que será alterada (o conteúdo interno do elemento)
    Output('id_resultado_quadrado', 'children'),

    # Especifica a entrada (Input) para a função de callback
    # 'id_slider_numero' é o ID do Slider que estamos monitorando
    # 'value' é a propriedade que estamos observando (o valor atual do Slider)
    [Input('id_slider_numero', 'value')]

)
# Define a função que será chamada sempre que o valor do Slider mudar
def calcular_quadrado(numero_selecionado):

    # Calcula o quadrado do número selecionado no Slider
    quadrado = numero_selecionado ** 2

    # Retorna uma string formatada que será inserida como o conteúdo (children)
    # do elemento HTML com ID 'id_resultado_quadrado'
    return f'O quadrado de {numero_selecionado} é {quadrado}.'


# Inicia o servidor do aplicativo Dash
# O método run_server é responsável por iniciar o servidor web que hospedará o aplicativo
aplicativo.run(
    debug=True,  # Ativa o modo de depuração, útil durante o desenvolvimento
    port=8055  # Define a porta onde o servidor será iniciado, neste caso é a 8055
)