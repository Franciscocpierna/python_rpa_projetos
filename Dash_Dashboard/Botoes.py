# Importar a classe Image da biblioteca PIL (Python Imaging Library) para manipular imagens.
from PIL import Image

# Importar a biblioteca base64 para codificar e decodificar
# dados usando o esquema de codificação base64.
import base64

# Importar BytesIO da biblioteca io para trabalhar com 
# streams de bytes em memória.
from io import BytesIO

# Importar a biblioteca dash para criar aplicativos da web interativos.
import dash

# Importar classes específicas da biblioteca dash para criar o
# layout e habilitar a interatividade.
from dash import html, Output, Input


# Definição da função que converte uma imagem para uma string Base64.
# Esta função é útil para incorporar imagens diretamente no HTML.
def converter_imagem_para_base64(caminho_imagem):

    # Cria um buffer em memória para armazenar os bytes da imagem.
    buffer = BytesIO()

    # Abre a imagem usando a classe Image da biblioteca PIL.
    # O caminho da imagem é passado como argumento para a função open.
    imagem = Image.open(caminho_imagem)

    # Salva a imagem no buffer em memória no formato PNG.
    # Outros formatos como JPEG também podem ser usados.
    imagem.save(buffer, format="PNG")

    # Pega os bytes armazenados no buffer e os codifica para Base64.
    # Depois, decodifica o resultado para uma string para torná-lo compatível com HTML.
    return base64.b64encode(buffer.getvalue()).decode()

# Definir a variável 'caminho_imagem' com o caminho completo para a
# imagem que você quer usar no aplicativo.
# Aqui, é usado um caminho específico do sistema de arquivos.
caminho_imagem = r"C:\python_projetos\python_rpa_projetos\Dash_Dashboard\hotel.jpeg"


# Chamar a função 'converter_imagem_para_base64' definida anteriormente
# para converter a imagem em uma string Base64.
# O resultado é armazenado na variável 'imagem_base64'.
imagem_base64 = converter_imagem_para_base64(caminho_imagem)


# Inicializar o aplicativo Dash, criando uma instância da classe Dash e
# armazenando-a na variável 'aplicativo'.
aplicativo = dash.Dash(__name__)

# Definir um dicionário 'estilo_comum' que contém estilos CSS que serão usados
# de forma recorrente nos botões do aplicativo.
# A chave 'width' define a largura,
# 'height' define a altura,
# 'margin' define a margem,
# e 'display' define como o elemento será exibido.
estilo_comum = {'width': '200px', 'height': '50px', 'margin': '10px auto', 'display': 'block'}

# Define o layout geral do aplicativo Dash.
# Uma div HTML é criada para conter todos os elementos.
aplicativo.layout = html.Div([

    # Cria um título de nível 1 (H1) para a página e centraliza o texto.
    html.H1("Título: Botões Diversos", style={'textAlign': 'center'}),

    # Cria uma nova div HTML para conter os botões.
    # Os botões ficarão dentro dessa div.
    html.Div([

        # Cria um botão simples com o texto "Botão Simples" e um ID para referenciá-lo nos callbacks.
        # Aplica o estilo CSS definido na variável 'estilo_comum'.
        html.Button('Botão Simples', id='botao_simples', style=estilo_comum),

        # Cria um botão colorido com o texto "Botão Colorido".
        # Usa a função Python ** para mesclar o estilo comum com cores específicas (fundo verde e texto branco).
        html.Button('Botão Colorido', id='botao_colorido',
                    style={**estilo_comum, 'background-color': 'green', 'color': 'white'}),

        # Cria um botão com um ícone.
        # Usa uma tag de imagem HTML dentro do botão para exibir o ícone.
        # O ícone é carregado como uma string Base64.
        # Cria um botão HTML que contém um ícone e um texto.
        html.Button(

            # O conteúdo interno do botão é definido como uma lista de elementos.
            [
                # Primeiro elemento da lista: Uma tag de imagem HTML (Img).
                # O src (fonte da imagem) é definido como uma string Base64 da
                # imagem que queremos exibir.
                # O estilo da imagem é definido para ter altura e largura de 24 pixels.
                html.Img(src=f'data:image/png;base64,{imagem_base64}',
                         style={'height': '24px', 'width': '24px'}),

                # Segundo elemento da lista: Um espaço em branco e o texto "Com Ícone".
                # Isso é feito para separar a imagem e o texto dentro do botão.
                " Com Ícone"
            ],

            # Atribui um ID ao botão para que possamos referenciá-lo em
            # callbacks ou outras partes do código.
            id='botao_icone',

            # Aplica o estilo CSS armazenado na variável 'estilo_comum' ao botão.
            # Isso afeta a largura, altura, margem e outros aspectos visuais do botão.
            style=estilo_comum

        ),  # Finaliza a definição do botão.

    ], style={'textAlign': 'center'}),  # Centraliza os botões dentro da div.

    # Cria uma div HTML para exibir mensagens dinâmicas.
    # O ID 'div_mensagem' é usado para atualizar o conteúdo da div usando callbacks.
    html.Div(id='div_mensagem', style={'textAlign': 'center', 'margin-top': '20px'})
])


# Definindo um callback para atualizar a interface do usuário
# com base em alguma ação do usuário
@aplicativo.callback(

    # O Output especifica que queremos atualizar a propriedade 'children' do
    # elemento HTML com ID 'div_mensagem'
    # Isso é o que será alterado quando o callback for acionado
    Output('div_mensagem', 'children'),

    # Os Inputs definem quais elementos da interface do usuário irão
    # acionar o callback quando interagidos
    # Neste caso, estamos observando os cliques ('n_clicks') em três botões diferentes
    [Input('botao_simples', 'n_clicks'),
     Input('botao_colorido', 'n_clicks'),
     Input('botao_icone', 'n_clicks')]
)
# Definição da função 'mostrar_mensagem' que será chamada quando o callback for ativado
def mostrar_mensagem(n1, n2, n3):

    # Obtém o contexto do callback para saber qual botão foi clicado
    contexto = dash.callback_context

    # Verifica se o callback foi acionado por algum evento
    if not contexto.triggered:

        # Se nenhum botão foi clicado para ativar o callback, retorna uma mensagem padrão
        return "Clique em um botão."

    else:

        # Obtém o ID do botão que disparou o evento
        # - 'contexto.triggered' é uma lista de dicionários que contêm informações sobre os eventos que dispararam o callback.
        # - Usamos [0] para pegar o primeiro evento, pois estamos interessados apenas no evento que disparou o callback mais recentemente.
        # - 'prop_id' contém o ID do botão e o nome da propriedade ('n_clicks') separados por um ponto.
        # - '.split('.')[0]' separa a string pelo ponto e pega a primeira parte, que é o ID do botão.
        id_botao = contexto.triggered[0]['prop_id'].split('.')[0]

        # Retorna uma mensagem indicando qual botão foi clicado
        # - 'id_botao.replace("_", " ")' substitui os sublinhados por espaços para tornar o ID mais legível.
        # - '.title()' torna a primeira letra de cada palavra maiúscula.
        # - A f-string é usada para inserir o ID formatado na mensagem que será exibida.
        return f'Você clicou no {id_botao.replace("_", " ").title()}!'


# Execução do aplicativo
# - Este bloco garante que o aplicativo só será executado se
# este script for o ponto de entrada (não foi importado como um módulo).
if __name__ == '__main__':

    # Inicia o servidor do aplicativo Dash
    # - 'debug=True' permite o modo de depuração, o que facilita o
    # desenvolvimento pois o servidor se atualiza automaticamente com mudanças no código.
    # - 'port=8053' especifica que o servidor deve rodar na porta 8053. Você
    # pode escolher outra porta se essa estiver ocupada.
    aplicativo.run(debug=True, port=8053)

