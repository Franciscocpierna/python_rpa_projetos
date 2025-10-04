# Importa as classes e funções necessárias das bibliotecas do Dash.
# Dash é o framework, dcc (Dash Core Components) fornece componentes como gráficos,
# html permite criar elementos HTML, e Input e Output são usados para os callbacks.
from dash import Dash, dcc, html, Input, Output

# Inicia uma nova instância do aplicativo Dash.
# __name__ é um parâmetro especial que obtém o nome do script Python que está sendo executado.
# Isso é útil quando você está implantando o aplicativo em servidores como o Gunicorn.
aplicativo = Dash(__name__)


# Define um dicionário Python para armazenar os estilos CSS que serão aplicados aos componentes do Dash.
# Este dicionário será referenciado posteriormente para aplicar estilos de forma consistente e centralizada.
estilos_css = {

    # Estilos para o container principal que envolve todos os outros componentes.
    'container_principal': {
        'width': '50%',          # Define a largura do container como 50% da largura da janela do navegador.
        'margin': 'auto',        # Centraliza o container na janela do navegador (margens automáticas nos lados esquerdo e direito).
        'padding': '20px',       # Aplica um preenchimento interno de 20 pixels em todos os lados do container.
        'border': '2px solid gray',  # Adiciona uma borda cinza sólida de 2 pixels ao redor do container.
        'borderRadius': '15px'   # Arredonda os cantos da borda com um raio de 15 pixels.
    },

    # Estilos para o título principal do aplicativo.
    'titulo_principal': {
        'textAlign': 'center',    # Alinha o texto do título ao centro.
        'marginBottom': '20px'    # Adiciona uma margem inferior de 20 pixels para separá-lo dos elementos abaixo.
    },

    # Estilos para a div onde o texto exibido será colocado.
    'texto_exibicao': {
        'width': '100%',           # Define a largura da div como 100% da largura do container pai.
        'height': '100px',         # Define a altura da div como 100 pixels.
        'textAlign': 'center',     # Alinha o texto ao centro da div.
        'lineHeight': '100px',     # Define a altura da linha para que o texto seja centralizado verticalmente na div.
        'fontSize': '18px'         # Define o tamanho da fonte do texto como 18 pixels.
    },

    # Estilos para a div que contém os botões de opção (radio buttons).
    'seletores_radio': {
        'textAlign': 'center',     # Alinha os botões de opção ao centro da div.
        'marginBottom': '20px'     # Adiciona uma margem inferior de 20 pixels para separá-los dos elementos abaixo.
    }
}

# Define o layout do aplicativo Dash. Este é o ponto de partida
# para a exibição dos componentes na página da web.
aplicativo.layout = html.Div([

    # Adiciona um título usando o componente HTML H1 (título de nível 1).
    # Aplica os estilos CSS definidos em 'titulo_principal' do dicionário estilos_css.
    html.H1("Exemplo de Botões de Rádio com Dash", style=estilos_css['titulo_principal']),

    # Cria um container Div (divisão) para envolver os elementos restantes do layout.
    # Aplica os estilos CSS definidos em 'container_principal' do dicionário estilos_css.
    html.Div([

        # Cria uma Div para envolver os botões de rádio.
        # Aplica os estilos CSS definidos em 'seletores_radio' do dicionário estilos_css.
        html.Div([

            # Utiliza o componente RadioItems da biblioteca Dash Core Components (dcc) para criar botões de rádio.
            # Esse componente permite que os usuários escolham uma entre várias opções.
            dcc.RadioItems(

                # 'id' é um identificador único para este componente.
                # Ele é crucial quando você deseja referenciar este
                # conjunto de botões de rádio em um callback para criar interatividade.
                id='seletor_cor',

                # 'options' define as opções que serão exibidas como botões de rádio.
                # Cada opção é um dicionário contendo um 'label' e um 'value'.
                # 'label' é o texto que será exibido ao lado do botão de rádio.
                # 'value' é o valor que será usado em callbacks quando esta opção for selecionada.
                options=[
                    {'label': 'Vermelho', 'value': 'red'},
                    {'label': 'Verde', 'value': 'green'},
                    {'label': 'Azul', 'value': 'blue'}
                ],

                # 'value' define qual dos botões de rádio deve ser selecionado inicialmente.
                # Neste caso, o botão de rádio 'Vermelho' estará selecionado por padrão quando a página for carregada.
                value='red',  # valor inicial

                # 'labelStyle' permite personalizar o estilo dos rótulos dos botões de rádio.
                # Neste caso, estamos usando 'display: block' para garantir que cada botão de rádio apareça em uma nova linha,
                # em vez de todos em uma única linha.
                labelStyle={'display': 'block'}

            )

            # Fecha a Div que contém os botões de rádio.
            # Aplica os estilos CSS definidos em 'seletores_radio' no dicionário estilos_css.
        ], style=estilos_css['seletores_radio']),

        # Utiliza o componente 'Div' de Dash HTML Components para criar uma nova divisão (Div).
        # Esta Div funcionará como um contêiner para o texto que será exibido na página.

        # Abre uma nova Div cujo ID é 'texto_cor_fundo'.
        html.Div(

            # 'id' é um identificador único para este componente HTML.
            # É crucial para referenciar este componente em callbacks,
            # permitindo que você o atualize com base nas interações do usuário.
            id='texto_cor_fundo',

            # 'children' define o conteúdo dentro desta Div.
            # Neste caso, é uma string de texto que informa ao usuário sobre o comportamento deste componente.
            children="A cor de fundo deste texto mudará",

            # 'style' aplica os estilos CSS ao contêiner Div.
            # Os estilos são retirados do dicionário 'estilos_css', especificamente da chave 'texto_exibicao'.
            style=estilos_css['texto_exibicao']
        )

        # Fecha a Div que funciona como o contêiner principal para todos os elementos da página.
        # Aplica os estilos CSS definidos em 'container_principal' do dicionário estilos_css.
    ], style=estilos_css['container_principal'])

    # Fecha a Div raiz que contém todo o layout do aplicativo Dash.
])


# Define um callback usando o decorador '@aplicativo.callback'.
# Um callback é basicamente uma função que é chamada automaticamente quando algum evento ocorre,
# como um valor de entrada sendo alterado.
@aplicativo.callback(

    # 'Output' especifica qual componente e propriedade serão alterados como resultado deste callback.
    # Neste caso, o componente com o ID 'texto_cor_fundo' terá sua propriedade 'style' (estilo) atualizada.
    Output('texto_cor_fundo', 'style'),

    # 'Input' especifica qual componente e propriedade serão observados para desencadear este callback.
    # Quando o valor do componente com o ID 'seletor_cor' for alterado, este callback será acionado.
    [Input('seletor_cor', 'value')]
)


# Define uma função chamada 'atualizar_cor', que será usada no callback.
# Esta função leva um argumento 'cor_escolhida', que é a cor selecionada pelo usuário através dos botões de rádio.
def atualizar_cor(cor_escolhida):

    # Cria um novo dicionário 'estilo_atualizado' para atualizar o estilo CSS da Div que contém o texto.
    # O operador '**' é usado para desempacotar e copiar todo o conteúdo do dicionário 'estilos_css['texto_exibicao']'.
    # Em seguida, atualizamos algumas propriedades específicas, como a cor de fundo, a cor do texto e o tamanho da fonte.
    estilo_atualizado = {
        **estilos_css['texto_exibicao'],
        'backgroundColor': cor_escolhida,  # Define a cor de fundo para a cor escolhida pelo usuário.
        'color': 'white',  # Define a cor do texto como branco.
        'fontSize': '24px'  # Aumenta o tamanho da fonte para 24 pixels.
    }

    # Retorna o dicionário de estilos atualizados.
    # Este dicionário será usado para atualizar a propriedade 'style' da Div com o ID 'texto_cor_fundo' no callback.
    return estilo_atualizado


# Verifica se este script é o ponto de entrada principal.
# Isso é útil quando você quer ter certeza de que o servidor só será iniciado quando este script for executado diretamente,
# e não quando for importado como um módulo em outros scripts.
if __name__ == '__main__':

    # Executa o servidor do Dash.
    # 'debug=True' habilita o modo de depuração, que fornece mais informações sobre erros e atualizações em tempo real.
    # 'port=8054' define a porta do servidor web como 8054.
    aplicativo.run(debug=True, port=8054)