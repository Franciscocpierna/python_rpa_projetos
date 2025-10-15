# Importa as classes e funções necessárias do Flask e outros módulos.
from flask import Flask, render_template, request

# Cria uma instância do Flask. Este é o ponto de partida para qualquer aplicativo Flask.
# '__name__' é uma variável Python especial que representa o nome do módulo atual.
app = Flask(__name__)

# O decorador '@app.route' associa a URL raiz ('/') à função 'index'.
# A função 'index' será chamada quando um usuário acessar a URL raiz do aplicativo.
@app.route('/')
def index():

    # A função 'render_template' renderiza um templates HTML.
    # 'calculadora.html' é o nome do arquivo de templates a ser renderizado.
    # 'etapas' e 'resultado' são variáveis passadas para o templates, inicialmente vazias.
    return render_template('calculadora.html', etapas='', resultado='')

# Define outra rota '/calcular' que aceita requisições POST.
# Esta rota será usada para processar os dados da calculadora enviados pelo usuário.
@app.route('/calcular', methods=['POST'])
def calcular():

    try:

        # Obtém os valores dos campos de formulário 'num1', 'num2' e 'operacao' enviados via POST.
        # Converte 'num1' e 'num2' para float para realizar operações matemáticas.
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacao = request.form['operacao']

        # Estrutura condicional para verificar a operação matemática a ser realizada.
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':

            # Verifica se 'num2' é zero para evitar erro de divisão por zero.
            if num2 == 0:
                resultado = 'Erro: Divisão por zero'
            else:
                resultado = num1 / num2

        else:

            # Caso a operação não seja reconhecida, define o
            # resultado como operação inválida.
            resultado = 'Operação inválida'

    except Exception as e:

        # Captura qualquer exceção que ocorra durante a
        # operação e armazena na variável 'resultado'.
        resultado = 'Erro: ' + str(e)

    # Cria uma string descrevendo as etapas da operação.
    etapas = f'{num1} {operacao} {num2} = {resultado}'

    # Renderiza novamente o templates 'calculadora.html' com as novas variáveis 'etapas' e 'resultado'.
    return render_template('calculadora.html', etapas=etapas, resultado=resultado)

# Verifica se o script é o principal e executa o aplicativo.
# 'debug=True' ativa o modo de depuração, o que é útil durante o desenvolvimento.
if __name__ == '__main__':
    app.run(debug=True)