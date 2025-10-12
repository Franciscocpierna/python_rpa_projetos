# Importa a classe Flask do módulo flask.
# Flask é a classe principal do framework Flask, utilizada para
# criar instâncias de aplicativos web.
from flask import Flask

# Cria uma instância da classe Flask.
# __name__ é uma variável especial do Python que é usada
# para determinar o nome do módulo atual.
# Neste caso, serve para que o Flask saiba onde procurar por
# templates, arquivos estáticos, etc.
app = Flask(__name__)

# O decorador '@app.route' é usado para registrar uma
# função como uma rota em seu aplicativo.
# '/' indica a rota raiz do site.
# Quando um usuário acessar a URL base do seu
# site (ex.: http://localhost:5000/), essa função será chamada.
@app.route('/')

# Define uma função chamada 'home'. Esta função será chamada
# quando a rota '/' for acessada.
def home():

    # A função retorna a string 'Olá, Mundo!', que será
    # exibida no navegador do usuário
    # quando eles acessarem a rota raiz ('/').
    return 'Olá, Mundo!'

# Essa condição verifica se o script está sendo
# executado como o script principal
# e não sendo importado como um módulo.
# __name__ é uma variável especial do Python que é
# definida como "__main__" se o script está sendo executado diretamente.
if __name__ == '__main__':

    # Chama o método run da instância 'app' do Flask.
    # debug=True ativa o modo de depuração do Flask.
    # Isso faz com que o servidor reinicie automaticamente em
    # caso de mudanças no código e fornece um debugger no navegador.
    app.run(debug=True)
