# Importa as classes e funções necessárias do Flask.
from flask import Flask, render_template

# Cria uma instância da classe Flask.
# '__name__' é uma variável especial do Python que representa o nome do módulo atual.
# Flask usa esta variável para saber onde encontrar os recursos como templates.
app = Flask(__name__)

# Decorador do Flask que associa a URL raiz ('/') à função 'pagina_inicial'.
@app.route('/')
def pagina_inicial():

    # A função 'render_template' é usada para renderizar um template HTML.
    # 'pagina_inicial.html' é o nome do arquivo de template HTML a
    # ser renderizado quando esta rota for acessada.
    return render_template('pagina_inicial.html')

# Decorador do Flask que associa a URL '/sobre' à função 'sobre_nos'.
@app.route('/sobre')

# Cria a função sobre_nos
def sobre_nos():

    # Renderiza o template 'sobre_nos.html' quando a URL '/sobre' for acessada.
    return render_template('sobre_nos.html')

# Decorador do Flask que associa a URL '/contato' à função 'contato'.
@app.route('/contato')

# Cria a função contato
def contato():

    # Renderiza o template 'contato.html' quando a URL '/contato' for acessada.
    return render_template('contato.html')

# Verifica se este script está sendo executado diretamente e não importado como um módulo.
if __name__ == '__main__':

    # Inicia o servidor web do Flask.
    # 'debug=True' ativa o modo de depuração, permitindo que erros
    # sejam exibidos no navegador e que o servidor reinicie automaticamente ao modificar o código.
    app.run(debug=True)
