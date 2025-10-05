# Importa a biblioteca Dash
import dash

# Importa componentes específicos do Dash, incluindo os
# elementos da interface do usuário (dcc e html) e funções de
# callback (Input, Output, State)
from dash import dcc, html, Input, Output, State

# Inicializa o aplicativo Dash
# O parâmetro __name__ é necessário para que o Dash saiba onde
# encontrar os arquivos de recursos (como CSS)
# aplicativo é a variável que contém a instância do aplicativo Dash
aplicativo = dash.Dash(__name__)

# Configuração do layout do aplicativo
# O método layout do objeto aplicativo define a estrutura da página web
# Usamos html.Div para criar um contêiner div HTML que envolverá
# todos os elementos da página
aplicativo.layout = html.Div([

    # html.H1 cria um cabeçalho de nível 1 (h1) para a página
    # O estilo é especificado como um dicionário Python e alinha o texto ao centro
    html.H1("Adicionar Itens às Listas Ordenadas e Não Ordenadas", style={'textAlign': 'center'}),

    # html.Div cria um novo contêiner div que irá agrupar os elementos relacionados
    # O contêiner a seguir é para o campo de entrada e o botão
    html.Div([

        # dcc.Input cria um campo de entrada (input) de texto
        # 'id' é usado para identificar este elemento em callbacks
        # 'type' especifica que é um campo de texto
        # 'value' é o valor inicial, que está vazio neste caso
        dcc.Input(id='entrada_item', type='text', value=''),

        # html.Button cria um botão HTML com o texto "Adicionar"
        # 'id' é usado para identificar este elemento em callbacks
        html.Button('Adicionar', id='botao_adicionar'),
    ]),

    # html.Div para a lista ordenada (ol)
    html.Div([

        # html.H3 cria um cabeçalho de nível 3 (h3) com o texto "Lista Ordenada"
        html.H3("Lista Ordenada"),

        # html.Ol cria uma lista ordenada (ol)
        # O 'id' é usado para identificar este elemento em callbacks
        html.Ol(id='lista_ordenada')
    ]),

    # html.Div para a lista não ordenada (ul)
    html.Div([

        # html.H3 cria um cabeçalho de nível 3 (h3) com o texto "Lista Não Ordenada"
        html.H3("Lista Não Ordenada"),

        # html.Ul cria uma lista não ordenada (ul)
        # O 'id' é usado para identificar este elemento em callbacks
        html.Ul(id='lista_desordenada')
    ]),
])

# Lista para guardar os itens
lista_itens = []


# Função para adicionar itens à lista
# @aplicativo.callback é um decorador que vincula a função abaixo a elementos específicos da interface do usuário
# A função é chamada sempre que os elementos especificados na lista de Input sofrem alguma alteração
@aplicativo.callback(

    # Output especifica os elementos da interface do usuário que serão atualizados pela função
    # Neste caso, serão atualizados os conteúdos (children) das listas ordenada e não
    # ordenada e o valor do campo de entrada
    [Output('lista_ordenada', 'children'),
     Output('lista_desordenada', 'children'),
     Output('entrada_item', 'value')],

    # Input especifica quais elementos da interface do usuário
    # acionarão a função quando alterados
    # Aqui, a função é acionada quando o número de
    # cliques ('n_clicks') no botão com id 'botao_adicionar' muda
    [Input('botao_adicionar', 'n_clicks')],

    # State permite acessar o estado atual de elementos
    # específicos da interface do usuário sem desencadear a função
    # Neste caso, o estado atual do campo de entrada ('entrada_item') é usado
    [State('entrada_item', 'value')]
)

# Definição da função de callback adicionar_item_a_lista
# Esta função é chamada sempre que o botão "Adicionar" é clicado
# n_cliques é o número de vezes que o botão foi clicado
# item_entrada é o texto atual do campo de entrada
def adicionar_item_a_lista(n_cliques, item_entrada):

    # A palavra-chave global é usada para indicar que estamos usando a variável global lista_itens
    # Isso permite que modifiquemos a variável fora do escopo desta função
    global lista_itens

    # Verifica se n_cliques e item_entrada são não-nulos (ou seja, o botão foi clicado e algum texto foi inserido)
    if n_cliques and item_entrada:

        # Adiciona o item inserido à variável global lista_itens
        # lista_itens é uma lista Python que mantém todos os itens adicionados pelo usuário
        lista_itens.append(item_entrada)

    # Inicializa uma lista vazia para armazenar os elementos html.Li
    lista_ordenada_html = []

    # Ordena a lista_itens e itera através de cada item
    for i in sorted(lista_itens):

        # Cria um novo elemento html.Li com o valor de i e o adiciona à lista_ordenada_html
        lista_ordenada_html.append(html.Li(i))

    # Inicializa uma lista vazia para armazenar os elementos html.Li
    lista_desordenada_html = []

    # Itera através de cada item na lista original lista_itens
    for i in lista_itens:

        # Cria um novo elemento html.Li com o valor de i e o adiciona à lista_desordenada_html
        lista_desordenada_html.append(html.Li(i))

    # Retorna os novos estados dos elementos da interface do usuário especificados nos Outputs do callback
    # lista_ordenada_html e lista_desordenada_html atualizarão o conteúdo das listas ordenada e não ordenada, respectivamente
    # O último '' esvaziará o campo de entrada após adicionar um item
    return lista_ordenada_html, lista_desordenada_html, ''


# Inicializa e roda o servidor do Dash
# debug=True permite que o servidor recarregue automaticamente sempre que o código for alterado
# port=8070 define a porta onde o servidor estará escutando
aplicativo.run_server(debug=True, port=8070)