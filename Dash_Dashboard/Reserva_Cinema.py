# Importando a biblioteca principal do Dash para construir a aplicação web.
import dash

# Importando componentes específicos do Dash para construir o layout e as interações da aplicação.
# dcc contém componentes para gráficos e inputs, e html contém componentes HTML.
# Input, Output e State são usados para construir as callbacks (funnest de retorno) da aplicação.
# ALL é uma constante usada para se referir a todos os componentes de um certo tipo em uma callback.
from dash import dcc, html, Input, Output, State, ALL

# Importando a biblioteca pandas para manipulação de dados. Será usada para ler e escrever no arquivo Excel.
import pandas as pd

# Importando a biblioteca datetime para manipulação de datas e horas.
import datetime

# Inicializando um contador de ações que será usado posteriormente nas callbacks.
# Este contador ajuda a rastrear quantas ações o usuário realizou, como clicar em botões, por exemplo.
contador_acoes = 0

# Inicializando a aplicação Dash.
# O argumento __name__ é uma variável especial do Python que obtém o nome do script atual.
# É necessário para que o Dash saiba onde procurar por arquivos estáticos, se houver.
app = dash.Dash(__name__)

# Adicione algum CSS inline para estilização. Em uma aplicação real, você pode
# querer colocar isso em um arquivo CSS separado.
# Layout da aplicação
# Layout da aplicação
app.layout = html.Div([

    # Título Principal
    html.H1('Sistema de Reserva de Cadeiras de Cinema', style={'textAlign': 'center'}),

    # Este bloco cria uma divisão na interface que agrupa elementos relacionados à escolha de data
    html.Div([

        # Cria uma sub-divisão para conter o título e o seletor de data
        html.Div([

            # Cria um cabeçalho de nível 3 que serve como um rótulo para a funcionalidade de escolha de data
            html.H3('Escolha a Data:'),

            # Cria um componente de seleção de data única (datepicker) do Dash
            dcc.DatePickerSingle(

                # Define um identificador único para o datepicker para referências em callbacks
                id='data_escolhida',

                # Define a data mínima permitida como 7º de dezembro de 2023
                min_date_allowed=pd.Timestamp('2023-12-07'),

                # Define a data máxima permitida como 1º de dezembro de 2025
                max_date_allowed=pd.Timestamp('2025-12-01'),

                # Define o mês inicial visível como o mês atual
                initial_visible_month=pd.Timestamp(datetime.datetime.now().date()),

                # Define a data selecionada inicialmente como a data atual
                date=str(datetime.datetime.now().date())
            )

            # Define o estilo da sub-divisão para exibir seu conteúdo em
            # linha (inline) e ocupar 45% da largura do contêiner pai
        ], style={'display': 'inline-block', 'width': '45%'}),

        # Define o estilo da divisão principal para ter uma margem inferior de 30 pixels,
        # separando-a visualmente de outros elementos abaixo dela
    ], style={'margin-bottom': '30px'}),

    # Início de um bloco de código que cria uma seção específica na página web
    html.Div([

        # Adiciona um cabeçalho de nível 3, que serve como um título ou indicação para a seção
        # Este cabeçalho informa ao usuário que a ação esperada é a seleção de cadeiras
        html.H3('Selecione sua Cadeira:'),

        # Adiciona uma divisão (container) HTML dentro da seção. Esta divisão é destinada a conter a tabela de cadeiras.
        # Não é adicionado nenhum conteúdo diretamente a esta divisão aqui, mas ela é identificada por um ID único,
        # o que permite que outros componentes da aplicação, como callbacks, insiram conteúdo dinamicamente.
        html.Div(id='div_tabela_cadeiras')

        # A propriedade 'id' é crucial porque permite que essa divisão seja referenciada em funções de callback do Dash.
        # Os callbacks podem, por exemplo, preencher esta divisão com a representação visual das cadeiras disponíveis para reserva.
    ],

        # Define o estilo da divisão principal da seção.
        # 'width': '100%' faz com que a divisão se estenda por toda a largura disponível do contêiner pai,
        # assegurando que a seção utilize todo o espaço horizontal que pode.
        # 'margin-bottom': '30px' adiciona um espaço abaixo desta divisão,
        # separando-a visualmente de outros elementos que podem estar abaixo na página.
        style={'width': '100%', 'margin-bottom': '30px'}),


    # Inicia a criação de uma nova seção na interface do usuário dedicada aos
    # detalhes das reservas.
    html.Div([

        # Insere um cabeçalho de nível 3 que funciona como o título da seção, orientando o
        # usuário sobre a informação esperada aqui.
        html.H3('Detalhes da Reserva:'),

        # Inclui um campo de entrada de texto desabilitado que é preenchido automaticamente pelo sistema
        # quando uma cadeira é selecionada. Ele mostra ao usuário a cadeira que foi escolhida para a reserva.
        # A propriedade 'disabled=True' garante que o usuário não possa modificar manualmente o valor do campo,
        # pois ele é destinado apenas à exibição da informação.
        dcc.Input(

            # Identificador único do componente no Dash, que pode ser referenciado em callbacks.
            id='cadeira_escolhida',
            type='text',  # Define o tipo de dados que este campo deve aceitar, neste caso, texto.
            placeholder='Cadeira escolhida',  # Texto exibido no campo de entrada quando não há nenhum valor definido.
            disabled=True  # Desabilita o campo para evitar que o usuário modifique o valor.
        ),

        # Adiciona um campo de entrada de texto ativo onde o usuário pode inserir seu nome.
        # Esse campo será usado para associar o nome do usuário à reserva feita.
        dcc.Input(
            id='nome_usuario',  # Identificador único do componente no Dash.
            type='text',  # Define o tipo de dados, texto.
            placeholder='Digite seu nome'
            # Texto exibido que serve como uma dica para o usuário sobre que informação inserir.
        ),

        # Inclui um campo de entrada de texto onde o usuário pode inserir o nome do filme para o qual a reserva é feita.
        # Este campo é parte das informações de reserva e permite associar a reserva a um filme específico.
        dcc.Input(
            id='nome_filme',  # Identificador único do componente no Dash.
            type='text',  # Define o tipo de dados, texto.
            placeholder='Digite o nome do filme'  # Texto de instrução para o usuário.
        )
        # Define o estilo da divisão, especificamente uma margem inferior, para separá-la
        # visualmente de outros elementos na página.
    ], style={'margin-bottom': '30px'}),

    # Inicia a criação de uma nova seção na interface do usuário, especificamente
    # dedicada aos botões de ação.
    html.Div([

        # Adiciona um botão para confirmar a reserva.
        # Este botão é uma parte crucial da interação do usuário, permitindo
        # confirmar os detalhes da reserva feita.
        html.Button(

            'Confirmar Reserva',  # Define o texto exibido no botão, claramente indicando sua função.
            id='botao_confirmar',  # Atribui um identificador único ao botão, chamado 'botao_confirmar'.
            # Esse ID é essencial para referenciar o botão em callbacks do Dash, permitindo definir ações específicas quando o botão é clicado.
            style={'margin-right': '10px'}
            # Aplica um estilo CSS ao botão. Aqui, adiciona-se uma margem à direita de 10 pixels.
            # Isso serve para criar um espaço visual entre este botão e outros elementos ou botões adjacentes, melhorando a estética e a usabilidade.
        ),

        # Adiciona um segundo botão para cancelar a reserva.
        # Este botão permite ao usuário desfazer a seleção atual ou cancelar o processo de preenchimento dos detalhes da reserva.
        html.Button(

            'Cancelar Reserva',  # O texto do botão informa claramente sua função de cancelamento da reserva.
            id='botao_cancelar'  # Define um identificador único chamado 'botao_cancelar'.
            # Assim como no botão de confirmar, esse ID é usado para vincular o botão a callbacks no Dash,
            # permitindo implementar a lógica para cancelar uma reserva quando este botão é clicado.
        )

        # Aplica um estilo CSS à divisão que contém os botões.
        # 'margin-bottom': '30px' adiciona uma margem inferior de 30 pixels,
        # criando espaço entre esta seção de botões e outros elementos que possam estar abaixo dela na interface do usuário.
    ], style={'margin-bottom': '30px'}),

    # Inicia uma nova seção na interface do usuário dedicada a exibir
    # mensagens de status ao usuário.
    html.Div([

        # Insere um cabeçalho de nível 3 que serve como título para a seção.
        # Este cabeçalho informa o usuário que o texto abaixo irá
        # refletir o status atual da reserva de cadeiras.
        html.H3('Status da Reserva:'),

        # Cria uma sub-divisão que será usada para mostrar mensagens de status dinâmicas.
        # O conteúdo desta divisão pode mudar em resposta a ações do usuário, como confirmar ou cancelar uma reserva.
        # Inicialmente, não há conteúdo definido, mas o ID permite que este elemento seja facilmente referenciado e atualizado por callbacks.
        html.Div(id='mensagem_reserva')
        # A propriedade 'id' é crucial pois permite que essa divisão seja referenciada em funções de callback do Dash,
        # que são responsáveis por atualizar dinamicamente o conteúdo da página com base em ações do usuário.

    ],

        # Define o estilo da divisão principal da seção.
        # 'margin-bottom': '30px' adiciona um espaço abaixo desta divisão,
        # que serve para separá-la visualmente de outras seções da página.
        style={'margin-bottom': '30px'}),

    # Cria duas divisões ocultas na página que funcionam como armazenamento para informações que não precisam ser exibidas,
    # mas que são necessárias para o funcionamento interno da aplicação, como armazenamento de valores temporários ou gatilhos para callbacks.

    # A primeira divisão oculta é usada para armazenar um gatilho invisível na página.
    # Embora não seja visível para o usuário, pode ser usada para acionar callbacks quando seu conteúdo é atualizado.
    html.Div(id='gatilho', style={'display': 'none'}),
    # O estilo 'display': 'none' garante que esta divisão não seja mostrada na interface do usuário.

    # A segunda divisão oculta serve para guardar a última cadeira que foi selecionada pelo usuário.
    # Assim como a divisão anterior, ela é usada em callbacks, mas não precisa ser exibida para o usuário.
    html.Div(id='ultima_cadeira_escolhida', style={'display': 'none'})
    # Novamente, o estilo 'display': 'none' aplica-se para tornar a divisão invisível na página.

])


# Define uma função chamada 'criar_tabela', que é responsável por
# construir uma representação visual das cadeiras como uma tabela HTML.
# Esta função recebe um argumento chamado 'reservas', que é uma lista de cadeiras já reservadas.
def criar_tabela(reservas):

    # Inicializa uma lista vazia que irá armazenar as linhas da tabela como elementos HTML.
    linhas_tabela = []

    # Inicia um loop for que irá percorrer os números de 1 a 10 (inclusive),
    # correspondendo a 10 linhas de cadeiras no cinema.
    for i in range(1, 11):

        # Cria uma linha de tabela HTML (tr) para cada iteração do
        # loop, representando uma linha de cadeiras.
        linha_tabela = html.Tr([

            # Dentro de cada linha, cria células de tabela (td) utilizando
            # uma compreensão de lista para gerar 5 cadeiras por linha.
            html.Td([

                # Cada célula contém um botão que representa uma cadeira individual.
                # O texto do botão é formatado para mostrar qual linha e
                # cadeira ele representa, por exemplo, "Linha-1_Cadeira-1".
                html.Button(

                    # Define o texto do botão com a linha e número da cadeira.
                    f"Linha-{i}_Cadeira-{j}",

                    # Atribui um ID único ao botão, que será usado em callbacks (funções de retorno).
                    id={'type': 'cadeira', 'index': f"Linha-{i}_Cadeira-{j}"},

                    # O ID é um dicionário que contém dois campos: 'type' e 'index'.
                    # 'type' é uma constante que identifica todos os botões dessa natureza como 'cadeira'.
                    # 'index' é um identificador único para cada cadeira, composto pelo número da linha e da cadeira.
                    # Esse ID único permite que ações específicas sejam tomadas em resposta a eventos em cadeiras específicas dentro dos callbacks.

                    style={

                        # Define a cor de fundo do botão.
                        # Se a cadeira (botão) atual não estiver na lista de reservas, a cor de fundo será verde, indicando disponibilidade.
                        # Se a cadeira estiver na lista de reservas, a cor de fundo muda para amarelo, indicando que está reservada.
                        "background-color": "green" if f"Linha-{i}_Cadeira-{j}" not in reservas else "yellow",

                        # Define a cor do texto do botão.
                        # Se a cadeira estiver reservada (cor de fundo amarela), a cor do texto será preta para contraste.
                        # Se a cadeira não estiver reservada (cor de fundo verde), a cor do texto será branca.
                        "color": "black" if f"Linha-{i}_Cadeira-{j}" in reservas else "white",

                        # Define o estilo de exibição do botão como 'block', o que faz com que o botão preencha a linha inteira na célula da tabela.
                        # Isso ajuda a garantir que o botão seja facilmente clicável e ocupe uma área maior, melhorando a usabilidade.
                        "display": "block",

                        # Define a largura do botão para ocupar 100% da largura da célula da tabela em que está contido.
                        # Isso assegura que o botão se estenda por toda a largura disponível, criando uma interface mais limpa e consistente.
                        "width": "100%",

                        # Remove qualquer borda do botão para uma aparência mais limpa e integrada.
                        # Isso evita distrações visuais desnecessárias e mantém o foco no conteúdo do botão.
                        "border": "none",

                        # Remove qualquer margem externa do botão, permitindo que os botões se alinhem perfeitamente uns com os outros sem espaços indesejados.
                        "margin": "0",

                        # Adiciona um preenchimento interno de 10 pixels no botão.
                        # Isso cria espaço ao redor do texto dentro do botão, tornando-o mais legível e esteticamente agradável.
                        "padding": "10px",

                        # Centraliza o texto dentro do botão.
                        # Essa propriedade garante que o texto esteja alinhado no meio do botão, tanto horizontal quanto verticalmente, melhorando a clareza.
                        "text-align": "center",
                    },

                    # O botão está habilitado e pode ser clicado pelo usuário.
                    disabled=False

                )

                # Aplica estilo para remover o preenchimento e a margem das células, permitindo que o botão ocupe todo o espaço disponível.
            ], style={"padding": "0", "margin": "0"}) for j in range(1, 6)  # Repete para criar cinco botões por linha.

        ])

        # Adiciona a linha completa de cadeiras à lista 'linhas_tabela'.
        linhas_tabela.append(linha_tabela)

    # Após construir todas as linhas de cadeiras, a função retorna um elemento de tabela HTML completo.
    # Este passo finaliza a construção da tabela de cadeiras, agrupando todas
    # as linhas de cadeiras criadas anteriormente em um único elemento de tabela.
    return html.Table(linhas_tabela,

                      # Define um dicionário de estilos CSS para a tabela completa.
                      style={

                          # Define a largura da tabela.
                          # 'width': '100%' faz com que a tabela ocupe toda a largura disponível do contêiner em que está inserida.
                          # Isso garante que a tabela se ajuste adequadamente ao espaço disponível, independentemente do tamanho da tela ou janela do navegador.
                          'width': '100%',

                          # Define o layout da tabela.
                          # 'table-layout': 'fixed' especifica que todas as colunas da tabela devem ter a mesma largura.
                          # Isso é importante para garantir que a tabela tenha uma aparência uniforme e organizada.
                          # Com um layout fixo, a largura de cada coluna é a mesma, proporcionando consistência visual em toda a tabela.
                          'table-layout': 'fixed',

                          # Define a margem da tabela.
                          # 'margin': '0' remove qualquer margem externa da tabela.
                          # Isso é útil para garantir que a tabela se alinhe perfeitamente com outros elementos na página, sem espaços indesejados em torno dela.
                          'margin': '0',
                      })


# O decorador '@app.callback' do Dash é usado para definir uma função de callback.
# Esta função será chamada sempre que seus Inputs ou States (descritos abaixo) forem atualizados.
@app.callback(

    # Output: Define o componente e a propriedade que serão atualizados pelo callback.
    # Neste caso, o conteúdo (children) da 'div_tabela_cadeiras' será atualizado.
    Output('div_tabela_cadeiras', 'children'),

    # Input: Define os componentes e propriedades que, quando alterados, acionam o callback.
    # A data do DatePicker (data_escolhida) e o conteúdo da 'div' com id 'gatilho' são os Inputs aqui.
    [Input('data_escolhida', 'date'),
     Input('gatilho', 'children')],

    # State: Define as propriedades que serão lidas quando o callback for ativado, mas que não acionam o callback quando alteradas.
    # Neste caso, o conteúdo da 'div' com id 'gatilho' é o State.
    State('gatilho', 'children'),

    # prevent_initial_call=False: Este argumento especifica se o callback deve ser chamado na inicialização da página.
    # False significa que ele será chamado imediatamente na inicialização.
    prevent_initial_call=False
)


# Definição da função 'atualizar_tabela', que é chamada como uma função de callback no Dash.
# Esta função aceita três argumentos: 'data', 'gatilho', e 'ultimo_gatilho'.
def atualizar_tabela(data, gatilho, ultimo_gatilho):

    # Utilizamos a palavra-chave 'global' para indicar que a variável 'contador_acoes' é uma variável global.
    # Isso significa que estamos modificando a variável global, e não criando uma nova variável local.
    global contador_acoes

    # Verifica se o valor de 'gatilho' é igual ao de 'ultimo_gatilho'.
    # Se for verdade, incrementa o 'contador_acoes' em 1.
    if gatilho == ultimo_gatilho:
        contador_acoes += 1

    # Tenta ler o arquivo Excel 'reservas.xlsx' e filtrar as linhas com base na data fornecida.
    try:

        # Lê o arquivo 'reservas.xlsx' em um DataFrame do pandas.
        df_reservas = pd.read_excel('reservas.xlsx')

        # Filtra o DataFrame para incluir apenas as linhas onde a coluna 'Data' corresponde à data fornecida.
        df_filtrado = df_reservas[df_reservas['Data'] == pd.Timestamp(data)]

        # Converte a coluna 'Cadeira' do DataFrame filtrado em uma lista e a armazena na variável 'reservas'.
        reservas = df_filtrado['Cadeira'].tolist()

    # Caso o arquivo 'reservas.xlsx' não seja encontrado, define 'reservas' como uma lista vazia.
    except FileNotFoundError:
        reservas = []

    # Chama a função 'criar_tabela' passando a lista 'reservas' como argumento.
    # O retorno dessa função será o novo conteúdo da 'div_tabela_cadeiras'.
    return criar_tabela(reservas)


# A anotação '@app.callback' define uma função de callback que será chamada
# quando uma das entradas especificadas mudar. Os valores retornados pela função
# serão usados para atualizar os componentes da interface de usuário especificados
# como saídas (Outputs).
@app.callback(

    # A lista de saídas especifica que dois componentes da interface de usuário serão atualizados:
    # o campo de texto com o ID 'cadeira_escolhida' terá seu valor ('value') atualizado,
    # e a div com o ID 'ultima_cadeira_escolhida' terá seu conteúdo ('children') atualizado.
    [Output('cadeira_escolhida', 'value'),
     Output('ultima_cadeira_escolhida', 'children')],

    # A entrada especificada é qualquer clique ('n_clicks') em um botão cujo tipo é 'cadeira'.
    # O uso de ALL para o índice significa que esta função de callback responderá a cliques em qualquer
    # botão do tipo 'cadeira'.
    [Input({'type': 'cadeira', 'index': ALL}, 'n_clicks')],

    # O parâmetro 'prevent_initial_call=True' impede que a função de callback seja executada
    # imediatamente após o carregamento da página.
    prevent_initial_call=True
)

# Define a função escolher_cadeira que será chamada pelo callback.
# A função recebe um argumento, contador_cliques_cadeira, que é o número de cliques no botão da cadeira.
def escolher_cadeira(contador_cliques_cadeira):

    # Utiliza o contexto do callback do Dash para obter informações sobre quais componentes
    # desencadearam a função de callback.
    contexto = dash.callback_context

    # Verifica se a função de callback foi desencadeada por alguma ação do usuário.
    # Se não foi, a função retorna 'dash.no_update' para ambas as saídas, indicando que nada deve ser atualizado.
    if not contexto.triggered:
        return dash.no_update, dash.no_update

    # Obtém o ID do elemento que desencadeou a função de callback.
    # Isso é feito pegando a primeira ação disparada (triggered) e isolando a propriedade 'prop_id'.
    # Em seguida, divide essa string no ponto '.' e pega o primeiro elemento para obter o ID.
    id_cadeira_clicada = contexto.triggered[0]['prop_id'].split('.')[0]

    # Converte a string do ID do elemento em um dicionário usando a função eval().
    # Isso é útil porque o ID é armazenado como uma string que representa um dicionário.
    dicionario_id = eval(id_cadeira_clicada)

    # Extrai o valor do campo 'index' do dicionário.
    # Isso nos dá o identificador específico da cadeira que foi clicada.
    indice_clicado = dicionario_id['index']

    # Retorna o índice da cadeira clicada para ambas as saídas definidas no callback.
    # O primeiro valor retornado atualizará o campo 'value' do elemento com ID 'cadeira_escolhida',
    # e o segundo valor retornado atualizará o conteúdo ('children') do elemento com ID 'ultima_cadeira_escolhida'.
    return indice_clicado, indice_clicado


# Este decorador @app.callback vincula entradas, estados e saídas para uma função de callback no Dash.
# Quando uma entrada muda, a função de callback associada é chamada e a saída é atualizada.
@app.callback(

    # Define os elementos da interface do usuário cujos valores serão atualizados pelo callback.
    # São definidos quatro saídas: 'mensagem_reserva', 'nome_usuario', 'nome_filme' e 'gatilho'.
    [Output('mensagem_reserva', 'children'),
     Output('nome_usuario', 'value'),
     Output('nome_filme', 'value'),
     Output('gatilho', 'children')],

    # Define os elementos da interface do usuário que disparam o callback.
    # São dois botões neste caso: 'botao_confirmar' e 'botao_cancelar'.
    [Input('botao_confirmar', 'n_clicks'),
     Input('botao_cancelar', 'n_clicks')],

    # Define os elementos da interface do usuário cujos valores atuais serão passados para a função de callback como estados.
    # São quatro estados: 'data_escolhida', 'ultima_cadeira_escolhida', 'nome_usuario' e 'nome_filme'.
    [State('data_escolhida', 'date'),
     State('ultima_cadeira_escolhida', 'children'),
     State('nome_usuario', 'value'),
     State('nome_filme', 'value')],

    # Impede que a função de callback seja chamada quando a página é carregada.
    prevent_initial_call=True
)

# Define a função 'gerenciar_reserva' que é chamada pelo callback associado.
def gerenciar_reserva(n_confirma, n_cancela, data, ultima_cadeira, nome_usuario, nome_do_filme):

    # A variável global 'contador_acoes' é acessada e redefinida para zero.
    # Isso pode ser usado para rastrear o número de ações realizadas durante a execução do aplicativo.
    global contador_acoes
    contador_acoes = 0

    # 'dash.callback_context' é usado para obter informações sobre o componente que disparou o callback.
    # Isso é útil para determinar qual botão foi clicado (confirmar ou cancelar) ou qualquer outro evento que tenha disparado o callback.
    contexto = dash.callback_context

    # Verifica se algum componente realmente disparou o callback.
    # Se nenhum componente disparou o callback, retorna 'dash.no_update' para todas as saídas,
    # indicando que nenhuma delas deve ser atualizada.
    if not contexto.triggered:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update

    # 'contexto.triggered[0]['prop_id']' contém a ID do componente que disparou o callback.
    # O método 'split' é usado para isolar o nome da propriedade (neste caso, estamos apenas interessados na ID do componente, e não na propriedade que mudou).
    acao_realizada = contexto.triggered[0]['prop_id'].split('.')[0]

    # Tenta ler o arquivo 'reservas.xlsx' para obter informações sobre as reservas existentes.
    # Se o arquivo não existir, cria um novo DataFrame vazio com as colunas especificadas.
    try:
        df_reservas = pd.read_excel('reservas.xlsx')
    except FileNotFoundError:
        df_reservas = pd.DataFrame(columns=['Cadeira', 'Nome', 'Data', 'Filme'])

    # Verifica se o botão de confirmação ("botao_confirmar") foi clicado
    if acao_realizada == 'botao_confirmar':

        # Cria um novo DataFrame para armazenar os detalhes da nova reserva
        # pd.Timestamp(data) converte a data em um objeto de carimbo de tempo do pandas
        # ultima_cadeira, nome_usuario, nome_do_filme armazenam o estado atual desses campos
        nova_reserva = pd.DataFrame([[pd.Timestamp(data), ultima_cadeira, nome_usuario, nome_do_filme]],
                                        columns=['Data', 'Cadeira', 'Nome', 'Filme'])

        # Concatena o DataFrame da nova reserva com o DataFrame existente
        df_reservas = pd.concat([df_reservas, nova_reserva])

        # Define a mensagem a ser retornada como 'Reserva confirmada!'
        mensagem_retorno = 'Reserva confirmada!'

    # Verifica se o botão de cancelamento ("botao_cancelar") foi clicado
    elif acao_realizada == 'botao_cancelar':

        # Remove a reserva que corresponde à data e à cadeira selecionadas
        # Utiliza o método `.drop` para remover linhas que atendem a certas condições
        df_reservas = df_reservas.drop(
            df_reservas[
                (df_reservas['Data'] == pd.Timestamp(data)) & (df_reservas['Cadeira'] == ultima_cadeira)].index)

        # Define a mensagem a ser retornada como 'Reserva cancelada!'
        mensagem_retorno = 'Reserva cancelada!'

    # Caso nenhum dos botões tenha sido clicado, retorna 'no_update' para todos os campos de saída
    else:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update

    # Salva o DataFrame atualizado como um arquivo Excel
    # index=False impede que os índices do DataFrame sejam salvos no arquivo Excel
    df_reservas.to_excel('reservas.xlsx', index=False)

    # Retorna a mensagem adequada e limpa os campos de entrada
    # O último valor retornado atualiza o 'gatilho' com a data atual, que pode ser usada
    # para atualizar outros elementos da interface
    return mensagem_retorno, '', '', str(pd.Timestamp(data))

# Verifica se este script está sendo executado como o programa principal
# Se sim, o valor de __name__ será '__main__'
if __name__ == '__main__':

    # Inicia o servidor da aplicação Dash
    # debug=True permite que a aplicação atualize automaticamente sempre que o código for alterado
    # port=8054 define que a aplicação estará rodando na porta 8054 do servidor local
    app.run(debug=True, port=8054)