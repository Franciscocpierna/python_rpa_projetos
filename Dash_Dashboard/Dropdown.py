# Importa a biblioteca 'dash' para criar o aplicativo Dash.
# Também importa 'dcc' para Dash Core Components, 'html' para Dash HTML Components,
# 'Input' e 'Output' para definir as entradas e saídas dos callbacks.
import dash
from dash import dcc, html, Input, Output

# Inicializa uma instância do aplicativo Dash.
# O argumento __name__ ajuda o Dash a encontrar automaticamente
# recursos associados ao aplicativo,
# como arquivos CSS.
aplicativo = dash.Dash(__name__)


# Define o layout do aplicativo utilizando Dash HTML Components e Dash Core Components.
# A função html.Div cria uma 'div' HTML que pode conter outros componentes.
# Tudo dentro da lista passada como argumento para html.Div será incluído dentro dessa 'div'.
aplicativo.layout = html.Div([

    # Utiliza html.H1 para criar um título de nível 1 (H1) na página web.
    # O atributo 'style' permite aplicar estilos CSS inline.
    # Neste caso, o texto será centralizado na página ('textAlign': 'center').
    html.H1("Exemplo de Caixa de Seleção com Dash", style={'textAlign': 'center'}),

    # Utiliza dcc.Dropdown para criar uma caixa de seleção (Dropdown) para escolher uma fruta.
    # 'id' é o identificador único para este componente, usado para referências em callbacks.
    dcc.Dropdown(
        id='id_selecao_fruta',

        # 'options' define a lista de opções que podem ser selecionadas.
        # Cada opção é um dicionário com um 'label' (exibido para o usuário) e um 'value' (valor interno).
        options=[
            {'label': 'Maçã', 'value': 'maca'},
            {'label': 'Banana', 'value': 'banana'},
            {'label': 'Cereja', 'value': 'cereja'}
        ],

        # 'value' define a opção que será selecionada por
        # padrão quando a aplicação for iniciada.
        value='maca'  # Valor inicial
    ),

    # Utiliza html.Div para criar uma nova divisão (Div) que irá conter o texto informativo sobre a fruta selecionada.
    # O 'id' é necessário para atualizar o conteúdo deste Div com base na seleção do usuário através de um callback.
    html.Div(id='id_info_fruta')
])


# Define uma função que será usada como callback para atualizar as informações exibidas na página.
# O decorador '@aplicativo.callback' indica que esta função é um callback que interage com o aplicativo Dash.
@aplicativo.callback(

    # Utiliza Output para especificar que a propriedade 'children' (conteúdo) do
    # elemento com 'id' igual a 'id_info_fruta' será atualizada.
    Output('id_info_fruta', 'children'),

    # Utiliza Input para indicar que a entrada (gatilho) para o callback será o
    # valor ('value') do componente com 'id' igual a 'id_selecao_fruta'.
    [Input('id_selecao_fruta', 'value')]
)

# Define a função que será chamada sempre que o valor do elemento com id 'id_selecao_fruta' for alterado.
# O parâmetro 'fruta_escolhida' receberá o valor que o usuário selecionou na caixa de seleção (Dropdown).
def atualizar_informacao(fruta_escolhida):

    # A instrução 'if' verifica se o valor de 'fruta_escolhida' é 'maca'.
    # Se for, a função retornará uma string informando sobre as características da maçã.
    if fruta_escolhida == 'maca':
        return 'A maçã é uma fruta vermelha ou verde que é excelente para a saúde.'

    # A instrução 'elif' é uma abreviação para "else if". Ela verifica se o valor de 'fruta_escolhida' é 'banana'.
    # Se for, a função retornará uma string informando sobre as características da banana.
    elif fruta_escolhida == 'banana':
        return 'A banana é uma fruta rica em potássio.'

    # Outra instrução 'elif' que verifica se o valor de 'fruta_escolhida' é 'cereja'.
    # Se for, a função retornará uma string informando sobre as características da cereja.
    elif fruta_escolhida == 'cereja':
        return 'A cereja é uma pequena fruta vermelha geralmente usada em sobremesas.'

    # A instrução 'else' captura qualquer outra situação que não foi coberta pelas condições anteriores.
    # Se o usuário não selecionou nenhuma das opções fornecidas, essa mensagem será retornada.
    else:
        return 'Selecione uma fruta para saber mais.'


# O método 'run_server' inicia o servidor web para executar o aplicativo Dash.
# O argumento 'debug=True' permite o modo de depuração, e 'port=8055' define a porta onde o aplicativo será hospedado.
aplicativo.run_server(debug=True, port=8055)