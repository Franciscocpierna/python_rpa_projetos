# Importa a classe Flask do módulo flask.
# Flask é usado para criar instâncias de aplicativos web em Python.
from flask import Flask

# Cria uma instância do Flask.
# __name__ é uma variável especial que indica o nome
# do módulo ou pacote atual.
# É usado pelo Flask para saber onde procurar por
# recursos como templates e arquivos estáticos.
app = Flask(__name__)


# O decorador '@app.route' associa a função
# abaixo com a URL raiz ('/').
# Isso significa que quando alguém visitar a URL
# raiz do seu aplicativo, a função 'home' será chamada.
@app.route('/')

# Define a função 'home', que é chamada
# quando a rota raiz ('/') é acessada.
def home():

    # Retorna uma string que contém código HTML.
    # Este HTML é a estrutura básica de um currículo online.
    return '''

    <!-- Início do documento HTML. Todo documento HTML começa com esta declaração. -->
    <!DOCTYPE html>

    <!-- A tag <html> define o início do documento HTML. O
     atributo 'lang="en"' especifica que o idioma do documento é o inglês. -->
    <html lang="en">

    <!-- A tag <head> contém informações sobre o documento, como
     metadados, título, links para scripts e folhas de estilo. -->
    <head>

        <!-- A tag <meta> define metadados sobre o documento HTML. -->
        <!-- 'charset="UTF-8"' especifica a codificação de caracteres
         usada, que é UTF-8 (abrangente para a maioria dos caracteres e símbolos). -->
        <meta charset="UTF-8">
        
        <!-- - Esta tag <meta> define a viewport (área de visualização) 
            para garantir um design responsivo.     
                
            - 'width=device-width' faz a largura da página igual à 
            largura do dispositivo.        
            
            - 'initial-scale=1.0' define o nível inicial de zoom 
            quando a página é carregada. -->            
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <!-- A tag <title> especifica o título do documento, 
        que aparece na aba do navegador. -->
        <title>Meu Currículo</title>
    </head>
    
    <!-- A tag <body> contém o conteúdo principal do documento HTML. -->
    <body>
    
        <!-- A tag <h1> é usada para o título principal da página. -->
        <h1>Clevison Santos</h1>
        
        <!-- A tag <p> define um parágrafo. -->
        <!-- A tag <strong> é usada para dar ênfase (negrito) ao texto. -->
        <p><strong>Telefone:</strong> (11) 5555-5555</p>
        <p><strong>Email:</strong> clevison@gmail.com</p>
        <p><strong>LinkedIn:</strong> https://www.linkedin.com/in/clevison-s-838386a9/</p>
        
        <!-- A tag <h2> define um cabeçalho de segundo nível, usado para subtítulos. -->
        <h2>Objetivo Profissional</h2>
        
        <!-- Outro parágrafo para o texto do objetivo profissional. -->
        <p>Seu objetivo profissional aqui.</p>
        
        <!-- A tag <h2> define um cabeçalho de segundo nível, usado para subtítulos. -->
        <h2>Experiência Profissional</h2>
        
        <!-- Parágrafo para detalhes da experiência profissional. -->
        <p>Detalhes da sua experiência profissional.</p>   
        
        
        <!-- A tag <h2> define um cabeçalho de segundo nível, usado para subtítulos. -->
        <h2>Educação</h2>
        
        <!-- Parágrafo para detalhes da formação educacional. -->
        <p>Detalhes da sua formação educacional.</p>  
        
        
        <!-- A tag <h2> define um cabeçalho de segundo nível, usado para subtítulos. -->
        <h2>Habilidades</h2>
        
        <!-- A tag <ul> define uma lista não ordenada. -->
        <ul>
        
            <!-- A tag <li> define um item da lista. -->
            <li>Habilidade 1</li>
            <li>Habilidade 2</li>
            
            <!-- Comentário no HTML, não será exibido na página. Usado para orientações ou notas. -->
            <!-- Adicione mais habilidades conforme necessário -->
        </ul>
    
           
    </body>
    <!-- Fim da tag <body> -->
    
    </html>
    <!-- Fim da tag <html> -->

    '''


# Este bloco verifica se este script está
# sendo executado como o programa principal
# e não sendo importado como um módulo em outro script.
if __name__ == '__main__':

    # Inicia o servidor web do Flask.
    # 'debug=True' ativa o modo de depuração,
    # permitindo que alterações no código sejam
    # automaticamente aplicadas sem precisar
    # reiniciar o servidor.
    app.run(debug=True)