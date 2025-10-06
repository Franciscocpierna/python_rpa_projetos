# Importa o módulo principal da biblioteca Dash.
# Este módulo contém as classes e métodos essenciais para criar um aplicativo Dash.
import dash

# Importa componentes específicos de submódulos do Dash.
# - html: contém componentes para criar elementos HTML, como Div, H1, etc.
# - dcc: Dash Core Components, inclui componentes mais avançados como gráficos, sliders e, neste caso, o DatePicker.
# - Output, Input: São utilizados para definir as entradas e saídas
# dos callbacks, que são funções para manipular interações do usuário.
from dash import html, dcc, Output, Input

# Importa o módulo datetime para trabalhar com datas e horas.
# É utilizado aqui para definir as datas mínimas e máximas permitidas no DatePicker.
import datetime

# Inicializa a aplicação Dash.
# A classe Dash é instanciada para criar um novo aplicativo.
# O argumento '__name__' ajuda o Dash a encontrar recursos estáticos relacionados ao aplicativo.
# 'app' se torna o objeto principal para definir o layout e os callbacks do aplicativo Dash.
app = dash.Dash(__name__)


# Define o layout da aplicação Dash.
# 'app.layout' define a estrutura visual e os componentes do aplicativo.
# Utiliza-se 'html.Div' para criar uma divisão HTML que irá conter todos os elementos do layout.
app.layout = html.Div([

    # Cria um título para o aplicativo usando 'html.H1'.
    # O estilo é definido para alinhar o texto ao centro.
    html.H1("Exemplo de Data Picker", style={'textAlign': 'center'}),

    # Cria um DatePicker utilizando 'dcc.DatePickerSingle'.
    # Este é um componente que permite aos usuários escolher uma única data.
    dcc.DatePickerSingle(

        # Define um ID único para este DatePicker para referenciá-lo em callbacks.
        id='data-picker',

        # Define a data mínima permitida no DatePicker.
        # A data é definida como 5 de agosto de 1995.
        min_date_allowed=datetime.datetime(1995, 8, 5),

        # Define a data máxima permitida no DatePicker.
        # Utiliza 'datetime.datetime.now()' para definir como a data atual.
        max_date_allowed=datetime.datetime.now(),

        # Define o mês que será exibido inicialmente quando o DatePicker for aberto.
        # Está configurado para mostrar o mês atual.
        initial_visible_month=datetime.datetime.now(),

        # Define a data que será selecionada inicialmente no DatePicker.
        # Utiliza 'datetime.datetime.now().date()' para definir como a data atual.
        date=str(datetime.datetime.now().date())
    ),

    # Cria uma Div para mostrar a data selecionada pelo usuário.
    # Define o alinhamento do texto para o centro e uma margem superior de 20 pixels.
    html.Div(

        # Atribui um ID único à Div para referenciá-la em callbacks.
        id='data-selecionada',

        # Define os estilos CSS para esta Div.
        style={'textAlign': 'center', 'margin-top': '20px'}
    )
])


# Define uma função de callback usando o decorador '@app.callback'.
# Este decorador vincula uma função Python à atualização de componentes específicos do Dash.
@app.callback(

    # Define a saída (Output) da função de callback.
    # A saída é o conteúdo (children) da Div com o ID 'data-selecionada'.
    Output('data-selecionada', 'children'),

    # Define a entrada (Input) da função de callback.
    # A entrada é a data selecionada no DatePicker com o ID 'data-picker'.
    [Input('data-picker', 'date')]

)
# Define a função 'atualizar_data_selecionada' que será chamada sempre que o DatePicker for atualizado.
def atualizar_data_selecionada(data_selecionada):

    # Verifica se 'data_selecionada' não é None.
    # Se o usuário não tiver escolhido uma data, 'data_selecionada' será None.
    if data_selecionada is not None:

        # Converte a data selecionada para o formato desejado (dd/mm/aaaa).
        # 'strptime' converte a string da data para um objeto datetime.
        # 'strftime' formata o objeto datetime para uma string no formato desejado.
        data_formatada = datetime.datetime.strptime(data_selecionada.split(' ')[0], '%Y-%m-%d').strftime('%d/%m/%Y')

        # Retorna a string formatada para ser exibida na Div 'data-selecionada'.
        return f"Você selecionou a data: {data_formatada}"

# Inicia o servidor do aplicativo Dash.
# O parâmetro 'debug=True' permite o modo de depuração, e
# 'port=8065' define a porta em que o servidor será iniciado.
app.run(debug=True, port=8065)