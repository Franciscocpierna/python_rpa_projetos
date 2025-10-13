"""
├── app.py
└── templates/
    └── home.html

"""

# Importa a classe 'Flask' e a função 'render_template' do módulo 'flask'.
# 'Flask' é usado para criar instâncias de aplicativos web.
# 'render_template' é usado para renderizar templates HTML.
from flask import Flask, render_template

# Cria uma instância da classe Flask.
# '__name__' é uma variável especial do Python que é
# usada para determinar o nome do módulo atual.
# Isso é necessário para que o Flask saiba onde
# encontrar arquivos de templates e estáticos.
app = Flask(__name__)

# O decorador '@app.route' é usado para associar a função abaixo a uma URL.
# Neste caso, associa a função 'home' à URL raiz do site ('/').
@app.route('/')

# Define a função 'home' que será chamada quando
# a URL raiz ('/') for acessada.
def home():

    # A função 'render_template' renderiza um templates HTML.
    # 'home.html' é o nome do arquivo de templates a ser renderizado.
    # Este arquivo deve estar no diretório 'templates' dentro do diretório do aplicativo.
    return render_template('home.html')

# Esta condição verifica se este arquivo está sendo
# executado como o script principal
# e não sendo importado como um módulo.
if __name__ == '__main__':

    # Inicia o servidor web do Flask.
    # 'debug=True' ativa o modo de depuração, permitindo que alterações no código sejam
    # automaticamente aplicadas sem reiniciar o servidor e fornecendo um depurador no navegador.
    app.run(debug=True)

    # É o mesmo que fazer:
    # app.run(host='127.0.0.1', port=5000)