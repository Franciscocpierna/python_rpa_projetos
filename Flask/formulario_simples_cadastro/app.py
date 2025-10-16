# Importa a classe Flask do módulo flask. Flask é usado para criar a aplicação web.
from flask import Flask, render_template, request, redirect, url_for

# Importa o módulo pandas e dá a ele o apelido 'pd'. Pandas é uma
# biblioteca para manipulação de dados e análise.
import pandas as pd

# Importa o módulo os, que fornece uma maneira portátil de usar
# funcionalidades dependentes do sistema operacional.
import os

# Cria uma instância da classe Flask. O argumento __name__ ajuda o
# Flask a determinar a localização do aplicativo.
app = Flask(__name__)

# Define uma variável 'excel_file' que armazena o caminho para o arquivo Excel a ser usado.
excel_file = 'cadastros.xlsx'

# Decorador que indica a rota URL na qual a função seguinte será acessível.
# Aqui, '@app.route('/')' significa que esta será a rota raiz do site.
@app.route('/')

# Define a função 'index', que será chamada quando a rota raiz ('/') for acessada.
def index():

    # A função 'redirect' redireciona o usuário para uma rota
    # diferente, neste caso, para a rota '/registrar'.
    # 'url_for' é uma função do Flask que gera a URL para uma
    # rota específica. Aqui, gera a URL para a rota 'registrar'.
    return redirect(url_for('registrar'))


# Este decorador associa a função 'registrar' com a URL '/registrar'.
# 'methods=['GET', 'POST']' indica que esta rota aceita tanto requisições GET quanto POST.
@app.route('/registrar', methods=['GET', 'POST'])

# Define a função 'registrar', que será chamada quando a rota '/registrar' for acessada.
def registrar():

    # Verifica se o método da requisição atual é POST, o que
    # indica que dados foram enviados pelo usuário.
    if request.method == 'POST':

        # Obtém o valor do campo 'nome' do formulário enviado, usando o objeto 'request.form'.
        nome = request.form.get('nome')

        # Da mesma forma, obtém o valor do campo 'email' do formulário.
        email = request.form.get('email')

        # E obtém o valor do campo 'senha' do formulário.
        senha = request.form.get('senha')

        # Verifica se o arquivo Excel definido pela variável 'excel_file' já existe no sistema.
        if os.path.exists(excel_file):

            # Se o arquivo existir, lê o arquivo Excel para um DataFrame do Pandas.
            df = pd.read_excel(excel_file)

        else:

            # Se o arquivo não existir, cria um novo DataFrame com
            # colunas específicas: 'Nome', 'Email' e 'Senha'.
            df = pd.DataFrame(columns=['Nome', 'Email', 'Senha'])

        # Cria um novo DataFrame 'new_data' com os dados do usuário atual.
        new_data = pd.DataFrame([[nome, email, senha]], columns=['Nome', 'Email', 'Senha'])

        # Concatena o novo DataFrame com o DataFrame existente, ignorando o
        # índice para não duplicar índices.
        df = pd.concat([df, new_data], ignore_index=True)

        # Salva o DataFrame atualizado de volta no arquivo Excel,
        # sem incluir o índice do DataFrame.
        df.to_excel(excel_file, index=False)

        # Após salvar os dados, renderiza e retorna o template HTML 'sucesso.html'.
        return render_template('sucesso.html')

    # Se o método da requisição for GET, renderiza e retorna o template HTML 'registrar.html'.
    # Isso geralmente acontece quando o usuário acessa a rota '/registrar' pela primeira vez.
    return render_template('registrar.html')

# Verifica se o script está sendo executado como o script
# principal e não importado como um módulo.
if __name__ == '__main__':

    # Executa o aplicativo Flask. O parâmetro 'debug=True' ativa o modo de depuração,
    # que fornece informações úteis de erro e recarrega o servidor
    # automaticamente em caso de mudanças no código.
    app.run(debug=True)