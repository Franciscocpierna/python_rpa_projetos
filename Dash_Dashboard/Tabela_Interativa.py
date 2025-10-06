# Importar a biblioteca Dash principal e seus componentes

# Importa o módulo principal da biblioteca Dash, que contém funcionalidades básicas para iniciar e executar o aplicativo.
import dash

# Importa vários componentes específicos de diferentes submódulos do Dash:
# - dash_table: Componentes para criar tabelas interativas no Dash.
# - dcc: Dash Core Components, que inclui uma variedade de componentes de entrada e saída, como sliders, botões e gráficos.
# - html: Componentes para gerar elementos HTML básicos, como divs, h1, h2, etc.
# - Input, Output, State: Funcionalidades para definir entradas, saídas e estados
# em callbacks, que são funções que atualizam partes do aplicativo com base
# nas interações do usuário.
from dash import dash_table, dcc, html, Input, Output, State

# Importar a biblioteca pandas para manipulação de dados
import pandas as pd

# Criar um dicionário para armazenar dados da tabela. 
# O dicionário tem três chaves: "Nome", "Idade" e "Profissão", cada
# uma contendo uma lista de valores.
dados_tabela = {
    'Nome': ['Alice', 'Andy', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Henry', 'Ivy', 'Igor'],
    'Idade': [24, 24, 27, 22, 32, 29, 45, 39, 50, 50, 29, 29],
    'Profissão': ['Engenheiro', 'Engenheiro', 'Designer', 'Médico', 'Programador', 'Artista', 'Advogado', 'Arquiteto', 'Músico', 'Músico', 'Artista', 'Artista']
}

# Transforma o dicionário 'dados_tabela' em um DataFrame do Pandas.
# Um DataFrame é uma estrutura de dados tabular bidimensional, que é basicamente
# como uma planilha do Excel.
# 'dados_formatados' agora contém os dados em um formato que pode
# ser facilmente manipulado e analisado usando Pandas.
dados_formatados = pd.DataFrame(dados_tabela)

# Inicializa a aplicação Dash, criando uma instância do objeto Dash.
# O argumento '__name__' é utilizado para ajudar o Dash a encontrar
# recursos estáticos para a aplicação, como arquivos CSS.
# 'aplicativo' torna-se o objeto principal da nossa aplicação
# Dash e é usado para definir o layout, callbacks, etc.
aplicativo = dash.Dash(__name__)

# Define o layout do aplicativo Dash.
# O layout é uma propriedade crucial do objeto Dash que determina
# como o aplicativo web vai aparecer.
# O método 'html.Div()' é usado para criar uma divisão na
# qual todos os elementos da interface do usuário serão colocados.
aplicativo.layout = html.Div([

    # Cria um título para a aplicação, alinhado ao centro.
    # 'html.H1()' cria um cabeçalho de primeiro nível.
    html.H1("Exemplo de Tabela Interativa com Filtros Múltiplos", style={'textAlign': 'center'}),

    # Cria uma divisão para agrupar os elementos de filtragem.
    # Esta divisão contém rótulos e campos de entrada para filtros e um
    # botão para aplicar os filtros.
    html.Div([

        # Cria um rótulo para o campo de entrada de idade.
        html.Label('Filtrar por Idade:'),

        # Cria um campo de entrada numérico com o ID 'entrada_idade'.
        dcc.Input(id='entrada_idade', type='number'),

        # Cria um rótulo para o campo de entrada de nome.
        html.Label('Filtrar por Nome:'),

        # Cria um campo de entrada de texto com o ID 'entrada_nome'.
        dcc.Input(id='entrada_nome', type='text'),

        # Cria um rótulo para o campo de entrada de profissão.
        html.Label('Filtrar por Profissão:'),

        # Cria um campo de entrada de texto com o ID 'entrada_profissao'.
        dcc.Input(id='entrada_profissao', type='text'),

        # Cria um botão para aplicar os filtros, com o ID 'botao_aplicar_filtros'.
        html.Button('Aplicar Filtros', id='botao_aplicar_filtros')

    ], style={'marginBottom': 20}),  # Define um estilo para a divisão, adicionando uma margem inferior de 20 pixels.

    # Cria uma tabela interativa usando o componente 'dash_table.DataTable'.
    dash_table.DataTable(

        # Atribui um identificador único para esta tabela. Esse ID
        # pode ser usado para referenciar a tabela em callbacks.
        id='tabela_interativa',

        # Define as colunas da tabela com base nas colunas do DataFrame 'dados_formatados'.
        # 'name' é o texto do cabeçalho da coluna e 'id' é o identificador usado internamente.
        columns=[{"name": i, "id": i} for i in dados_formatados.columns],

        # Popula a tabela com os dados do DataFrame 'dados_formatados'.
        # O método 'to_dict('records')' converte o DataFrame em uma lista
        # de dicionários, onde cada dicionário representa uma linha.
        data=dados_formatados.to_dict('records'),

        # Define a propriedade 'editable' como True, tornando as células da tabela editáveis.
        editable=True,

        # Define o número de linhas visíveis por página na tabela.
        # Isso é útil para navegação quando há um grande número de linhas.
        page_size=10
    ),
])


# Utiliza o decorador '@aplicativo.callback' para definir uma função callback.
# Este callback é ativado quando o botão 'botao_aplicar_filtros' é clicado.
# Os estados de 'entrada_idade', 'entrada_nome' e 'entrada_profissao' são passados como argumentos,
# mas não acionam o callback.
@aplicativo.callback(

    # O Output define que a propriedade 'data' da 'tabela_interativa' será atualizada.
    Output('tabela_interativa', 'data'),

    # O Input define que o callback será ativado quando o número de
    # cliques ('n_clicks') no 'botao_aplicar_filtros' mudar.
    Input('botao_aplicar_filtros', 'n_clicks'),

    # State captura o valor atual de 'entrada_idade' mas não ativa o callback.
    State('entrada_idade', 'value'),

    # State captura o valor atual de 'entrada_nome' mas não ativa o callback.
    State('entrada_nome', 'value'),

    # State captura o valor atual de 'entrada_profissao' mas não ativa o callback.
    State('entrada_profissao', 'value')
)
# Definindo a função 'atualizar_tabela', que é chamada pelo callback sempre
# que o botão "Aplicar Filtros" é clicado.
# Esta função recebe quatro parâmetros:
# - num_cliques: o número de vezes que o botão "Aplicar Filtros" foi clicado.
# - filtro_idade: o valor atual do campo de entrada para filtrar por "Idade".
# - filtro_nome: o valor atual do campo de entrada para filtrar por "Nome".
# - filtro_profissao: o valor atual do campo de entrada para filtrar por "Profissão".
def atualizar_tabela(num_cliques, filtro_idade, filtro_nome, filtro_profissao):

    # Criando uma cópia profunda do DataFrame 'dados_formatados'.
    # Isso é feito para evitar alterações no DataFrame original quando aplicamos os filtros.
    dados_filtrados = dados_formatados.copy()

    # Verifica se o 'filtro_idade' contém algum valor. Se sim, aplica o filtro no DataFrame.
    if filtro_idade is not None:
        dados_filtrados = dados_filtrados[dados_filtrados['Idade'] == filtro_idade]

    # Verifica se o 'filtro_nome' contém algum valor. Se sim, aplica um filtro case-insensitive para o campo "Nome".
    if filtro_nome is not None:
        dados_filtrados = dados_filtrados[dados_filtrados['Nome'].str.contains(filtro_nome, case=False)]

    # Verifica se o 'filtro_profissao' contém algum valor. Se sim, aplica um filtro case-insensitive para o campo "Profissão".
    if filtro_profissao is not None:
        dados_filtrados = dados_filtrados[dados_filtrados['Profissão'].str.contains(filtro_profissao, case=False)]

    # Converte o DataFrame 'dados_filtrados' para um formato que possa ser utilizado
    # para atualizar a propriedade 'data' da tabela interativa.
    # O método 'to_dict('records')' converte cada linha do DataFrame em um
    # dicionário, e todos esses dicionários são colocados em uma lista.
    return dados_filtrados.to_dict('records')


# Verifica se este script é o ponto de entrada para a execução do programa.
# Em outras palavras, o código abaixo só será executado se este script for
# executado diretamente (e não importado como um módulo).
if __name__ == '__main__':

    # Executa o servidor do aplicativo Dash.
    # O argumento 'debug=True' permite que o servidor reinicie automaticamente
    # sempre que detectar mudanças no código.
    # O argumento 'port=8074' define que o servidor será acessado na porta 8074 do localhost.
    aplicativo.run(debug=True, port=8074)