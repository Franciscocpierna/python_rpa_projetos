"""
meu_projeto_flask/
│
├── app.py
│
├── templates/
│   ├── layout.html
│   ├── home.html
│   ├── page1.html
│   └── page2.html
│
└── static/
    └── css/
        └── style.css

"""

# Importa 'Flask' e 'render_template' do módulo 'flask'.
# 'Flask' é uma classe que é usada para criar a aplicação web.
# 'render_template' é uma função usada para renderizar um templates HTML.
from flask import Flask, render_template

# Cria uma instância da classe Flask.
# '__name__' é uma variável que representa o nome do módulo ou pacote atual.
# Isso é necessário para que o Flask saiba onde encontrar
# arquivos de templates e estáticos.
app = Flask(__name__)

# Decorador que associa a função 'home' à URL raiz ('/').
# Quando o usuário acessar a URL raiz, a função 'home' será chamada.
@app.route('/')

# Define a função 'home', que será chamada quando a
# URL raiz ('/') for acessada.
def home():

    # A função 'render_template' carrega um arquivo de
    # templates HTML e o retorna ao navegador.
    # 'home.html' é o nome do arquivo de templates que será renderizado.
    return render_template('home.html')

# Decorador que associa a função 'page1' à URL '/page1'.
# Quando o usuário acessar esta URL, a função 'page1' será chamada.
@app.route('/page1')

# Define a função 'page1', que será chamada quando a
# URL '/page1' for acessada.
def page1():

    # Renderiza o arquivo de templates 'page1.html' e o
    # retorna ao navegador.
    return render_template('page1.html')

# Decorador que associa a função 'page2' à URL '/page2'.
# Quando o usuário acessar esta URL, a função 'page2' será chamada.
@app.route('/page2')

# Define a função 'page2', que será chamada quando a
# URL '/page2' for acessada.
def page2():

    # Renderiza o arquivo de templates 'page2.html' e
    # o retorna ao navegador.
    return render_template('page2.html')

# Verifica se o script está sendo executado como o script
# principal e não sendo importado como um módulo.
if __name__ == '__main__':

    # Inicia o servidor web do Flask.
    # 'debug=True' ativa o modo de depuração, o que é
    # útil durante o desenvolvimento.
    # No modo de depuração, o servidor será reiniciado
    # automaticamente em caso de mudanças no código.
    app.run(debug=True)