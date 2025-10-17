# Importando módulos do Flask e outros pacotes necessários para a aplicação.
from flask import Flask  # Importa a classe Flask para criar a aplicação web.
from flask import render_template  # Permite renderizar templates HTML.
from flask import request  # Usado para obter dados de requisições HTTP (como formulários e parâmetros de URL).
from flask import session  # Facilita o uso de sessões para armazenar informações do usuário entre requisições.
from flask import redirect  # Permite redirecionar o usuário para outra rota/endpoint.
from flask import url_for  # Auxilia na geração de URLs para rotas específicas dentro da aplicação.
import pandas as pd  # Importa o módulo pandas (apelidado de 'pd'), uma biblioteca para manipulação e análise de dados.

# Criando uma instância do Flask para a aplicação web.
app = Flask(__name__)  # Cria uma instância da classe Flask, que será o objeto principal da aplicação web.
# O argumento __name__ indica ao Flask sobre onde procurar por templates, arquivos estáticos, etc.
# __name__ é uma variável especial em Python que representa o nome do módulo atual.


# Definindo uma chave secreta para a aplicação, usada para manter as sessões de usuário seguras.
app.secret_key = 'sua_chave_secreta_aqui'

# Carregando os dados dos alunos de um arquivo Excel para um DataFrame do Pandas.
# 'sheet_name' especifica a aba do Excel a ser usada, e
# 'dtype=str' garante que todos os dados sejam lidos como strings.
alunos_df = pd.read_excel('alunos.xlsx', sheet_name='alunos', dtype=str)

# Lista de dicionários representando perguntas e respostas para a prova.
perguntas = [

    # Cada dicionário contém a pergunta, as alternativas e a resposta correta.
    {"texto": "Qual é a palavra-chave para definir uma função em Python?", "alternativas": ["func", "define", "def", "function"], "resposta_correta": "def"},
    {"texto": "Como você inicia um comentário em Python?", "alternativas": ["#", "//", "/*", "--"], "resposta_correta": "#"},
    {"texto": "Qual destas opções é uma estrutura de dados em Python?", "alternativas": ["Lista", "Sequência", "Array", "Tupla"], "resposta_correta": "Lista"},
    {"texto": "Qual função é usada para imprimir algo na tela?", "alternativas": ["echo", "print", "out", "show"], "resposta_correta": "print"},
    {"texto": "Como iniciar um loop for em Python?", "alternativas": ["for x in y:", "foreach x in y:", "for x in range(y):", "for each x in y:"], "resposta_correta": "for x in y:"}

]

# Rota da aplicação para a página de login, aceitando métodos GET e POST.
@app.route('/', methods=['GET', 'POST'])
def login():

    # Verifica se a requisição atual é um POST (envio de formulário).
    if request.method == 'POST':

        # Obtendo os dados do formulário: login e senha, e removendo espaços extras com strip().
        login = request.form['login'].strip()
        senha = request.form['senha'].strip()

        # Filtrando o DataFrame para encontrar o usuário com o login e senha fornecidos.
        usuario = alunos_df[(alunos_df['Login'].str.lower() == login.lower()) & (alunos_df['Senha'] == senha)]

        # Verifica se o usuário foi encontrado.
        if not usuario.empty:

            # Armazena o login do usuário na sessão.
            session['usuario'] = usuario.iloc[0]['Login']  # Ou outro campo como 'Nome'.

            # Inicializa um dicionário vazio na sessão para armazenar as respostas do usuário.
            session['respostas'] = {}

            # Redireciona para a página da prova, iniciando na primeira pergunta.
            return redirect(url_for('prova', numero_pergunta=1))


        else:

            # Se o login falhar, retorna a página de login com uma mensagem de erro.
            erro = "Login ou senha incorretos!"
            return render_template('login.html', erro=erro)

    # Se a requisição for GET, simplesmente renderiza a página de login.
    return render_template('login.html')


# Define a rota '/prova/<int:numero_pergunta>'. O segmento '<int:numero_pergunta>' é
# uma variável dinâmica que aceita um inteiro.
# A função 'prova' será chamada com esse número como argumento. Aceita métodos GET e POST.
@app.route('/prova/<int:numero_pergunta>', methods=['GET', 'POST'])
def prova(numero_pergunta):

    # Verifica se o 'usuario' está na sessão. Se não estiver, redireciona para a página de login.
    # Isso impede o acesso à prova sem autenticação.
    if 'usuario' not in session:
        return redirect(url_for('login'))

    # Se a requisição for POST, processa a resposta enviada pelo usuário.
    if request.method == 'POST':

        # Obtém a resposta do formulário. 'resposta' é o nome do campo no
        # formulário da página 'dados_excel.html'.
        resposta = request.form.get('resposta')

        # Obtém o dicionário 'respostas' da sessão, ou um dicionário vazio se não existir.
        respostas = session.get('respostas', {})

        # Adiciona a resposta atual ao dicionário, usando o número da pergunta como chave.
        respostas[str(numero_pergunta)] = resposta

        # Atualiza o dicionário 'respostas' na sessão.
        session['respostas'] = respostas

        # Verifica se ainda há perguntas restantes. Se sim, redireciona para a próxima pergunta.
        if numero_pergunta < len(perguntas):

            return redirect(url_for('prova', numero_pergunta=numero_pergunta + 1))

        else:

            # Se todas as perguntas foram respondidas, redireciona para a página de resultado.
            return redirect(url_for('resultado'))

    # Se a requisição for GET, obtém a pergunta atual baseada no 'numero_pergunta'.
    pergunta_atual = perguntas[numero_pergunta - 1]

    # Renderiza o template 'prova.html', passando o número da pergunta atual e a pergunta em si.
    return render_template('prova.html', numero_pergunta=numero_pergunta, pergunta=pergunta_atual)


# Define a rota '/resultado' para a aplicação Flask. Esta rota
# só aceita o método GET por padrão.
@app.route('/resultado')
def resultado():

    # Verifica se 'usuario' está armazenado na sessão. Se não
    # estiver, redireciona para a página de login.
    # Isso assegura que somente usuários autenticados possam acessar seus resultados.
    if 'usuario' not in session:
        return redirect(url_for('login'))

    # Obtém o dicionário de respostas armazenado na sessão ou um
    # dicionário vazio se não existir.
    respostas = session.get('respostas', {})

    # Inicializa a pontuação do usuário como 0.
    pontuacao = 0

    # Itera sobre a lista de perguntas, com um contador começando de 1.
    for i, pergunta in enumerate(perguntas, start=1):

        # Obtém a resposta correta da pergunta atual.
        resposta_correta = pergunta["resposta_correta"]

        # Obtém a resposta do usuário para a pergunta atual do dicionário 'respostas'.
        resposta_usuario = respostas.get(str(i))

        # Verifica se a resposta do usuário existe e é igual à resposta correta.
        if resposta_usuario and resposta_usuario == resposta_correta:

            # Se a resposta estiver correta, incrementa a pontuação em 1.
            pontuacao += 1

    # Calcula a porcentagem de acertos dividindo a pontuação pelo número total de perguntas.
    porcentagem_acertos = (pontuacao / len(perguntas)) * 100

    # Determina se o usuário está aprovado com base em um critério (por exemplo, 60% de acertos).
    aprovado = porcentagem_acertos >= 60

    # Gera uma mensagem de aprovação baseada no critério de aprovação.
    mensagem_aprovacao = "Aprovado" if aprovado else "Reprovado"

    # Renderiza o templates 'resultado.html', passando a pontuação, a porcentagem de acertos, a mensagem de aprovação e o nome do usuário.
    return render_template('resultado.html', pontuacao=pontuacao, porcentagem_acertos=porcentagem_acertos, mensagem_aprovacao=mensagem_aprovacao, usuario=session['usuario'])

# Define a rota '/salvar_resultado' para a aplicação Flask.
@app.route('/salvar_resultado')
def salvar_resultado():

    # Verifica se o usuário está logado. Se não estiver, redireciona para a página de login.
    if 'usuario' not in session:
        return redirect(url_for('login'))

    # Obtém as respostas armazenadas na sessão. Se não houver respostas, usa um dicionário vazio.
    respostas = session.get('respostas', {})

    # Inicializa a variável de pontuação com 0.
    pontuacao = 0

    # Itera sobre cada pergunta da lista de perguntas.
    for i, pergunta in enumerate(perguntas, start=1):

        # Obtém a resposta correta da pergunta atual.
        resposta_correta = pergunta["resposta_correta"]

        # Obtém a resposta do usuário para essa pergunta.
        resposta_usuario = respostas.get(str(i))

        # Compara a resposta do usuário com a resposta correta.
        if resposta_usuario and resposta_usuario == resposta_correta:

            # Se estiverem corretas, incrementa a pontuação.
            pontuacao += 1

    # Calcula a porcentagem de acertos baseada na pontuação e no total de perguntas.
    porcentagem_acertos = (pontuacao / len(perguntas)) * 100

    # Determina se o usuário foi aprovado (por exemplo, se
    # acertou pelo menos 60% das perguntas).
    aprovado = porcentagem_acertos >= 60

    # Obtém o nome do usuário da sessão.
    usuario = session['usuario']

    # Abre o arquivo Excel 'resultados.xlsx' e carrega os dados em um DataFrame.
    resultados = pd.read_excel('resultados.xlsx', sheet_name='respostas', dtype=str)

    # Cria um novo DataFrame com as informações do resultado do usuário.
    novo_resultado = pd.DataFrame({'Nome': [usuario],
                                   # Inclui as respostas de cada pergunta, obtidas da sessão.
                                   'Pergunta 1': [respostas.get('1', '')],
                                   'Pergunta 2': [respostas.get('2', '')],
                                   'Pergunta 3': [respostas.get('3', '')],
                                   'Pergunta 4': [respostas.get('4', '')],
                                   'Pergunta 5': [respostas.get('5', '')],
                                   'Porcentagem de Acertos': [f'{porcentagem_acertos:.2f}%'],
                                   'Resultado': ['Aprovado' if aprovado else 'Reprovado']})

    # Concatena o novo resultado com os resultados existentes.
    resultados = pd.concat([resultados, novo_resultado], ignore_index=True)

    # Salva o DataFrame atualizado de volta no arquivo Excel.
    resultados.to_excel('resultados.xlsx', index=False, sheet_name='respostas')

    # Remove as respostas da sessão para limpar dados da prova do usuário.
    session.pop('respostas', None)

    # Redireciona o usuário de volta para a página de login.
    return redirect(url_for('login'))

# Verifica se este script está sendo executado como o principal e não como um módulo importado.
if __name__ == '__main__':

    # Inicia a aplicação Flask com o modo de depuração ativado.
    app.run(debug=True)