# Importação de módulos necessários do Flask.
from flask import Flask, render_template

# Criação de uma nova instância da classe Flask.
# '__name__' é uma variável especial do Python que indica o nome do módulo ou pacote atual.
# Flask usa isso para determinar onde estão os templates e arquivos estáticos.
app = Flask(__name__)

# Definição da classe Foto.
# Esta classe serve como um modelo para criar objetos Foto, cada um representando uma imagem diferente.
class Foto:

    # O método __init__ é o construtor da classe.
    # Ele é chamado automaticamente quando um novo objeto Foto é criado.
    def __init__(self, id, titulo, descricao, url):

        self.id = id             # Identificador único para a foto.
        self.titulo = titulo     # Título da foto.
        self.descricao = descricao # Descrição da foto.
        self.url = url           # URL da imagem (caminho para o arquivo de imagem).

# Criação de uma lista de objetos Foto.
# Cada objeto Foto é criado com um ID único, título, descrição e URL da imagem.
lista_de_fotos = [
    Foto(1, "Foto 1", "Descrição da Foto 1", "images/foto1.jpg"),  # Certifique-se de que o caminho está correto
    Foto(2, "Foto 2", "Descrição da Foto 2", "images/foto2.jpg"),  # Certifique-se de que o caminho está correto
    Foto(3, "Foto 3", "Descrição da Foto 3", "images/foto3.jpg"),  # Certifique-se de que o caminho está correto
    Foto(4, "Foto 4", "Descrição da Foto 4", "images/foto4.jpg"),  # Certifique-se de que o caminho está correto
    Foto(5, "Foto 5", "Descrição da Foto 5", "images/foto5.jpg"),  # Certifique-se de que o caminho está correto
    Foto(6, "Foto 6", "Descrição da Foto 6", "images/foto6.jpg"),  # Certifique-se de que o caminho está correto
    Foto(7, "Foto 7", "Descrição da Foto 7", "images/foto7.jpg"),  # Certifique-se de que o caminho está correto
    Foto(8, "Foto 8", "Descrição da Foto 8", "images/foto8.jpg"),
    Foto(9, "Foto 9", "Descrição da Foto 9", "images/foto9.jpg"),
    Foto(10, "Foto 10", "Descrição da Foto 10", "images/foto10.jpg"),
    Foto(11, "Foto 11", "Descrição da Foto 11", "images/foto11.jpg"),
    Foto(12, "Foto 12", "Descrição da Foto 12", "images/foto12.jpg"),
    Foto(13, "Foto 13", "Descrição da Foto 13", "images/foto13.jpg"),
    Foto(14, "Foto 14", "Descrição da Foto 14", "images/foto14.jpg"),
    Foto(15, "Foto 15", "Descrição da Foto 15", "images/foto15.jpg"),
    # Mais objetos Foto são adicionados aqui.
    # As URLs devem apontar para o local correto dos arquivos de imagem no servidor.
]

# Definição da rota principal ('/') do aplicativo.
# Quando um usuário acessa o endereço raiz do site, esta função é chamada.
@app.route('/')
def fotos():

    # A função 'render_template' é usada para renderizar o template HTML 'fotos.html'.
    # A lista 'lista_de_fotos' é passada para o template como uma variável chamada 'fotos'.
    return render_template('fotos.html', fotos=lista_de_fotos)


# Definição de uma rota para visualizar detalhes de uma foto específica.
# '<int:id>' é um parâmetro na URL que determina o ID da foto a ser exibida.
# Esta linha define uma rota no Flask usando um decorador. Um decorador em Python é uma função especial que modifica o comportamento de outra função.
# '@app' refere-se à instância do aplicativo Flask criado anteriormente.
# '.route' é um método que associa uma URL a uma função específica no aplicativo Flask.
# '/foto/<int:id>' define o padrão da URL. Aqui, '<int:id>' é um placeholder para um valor inteiro que representa o ID da foto.
# Quando um usuário acessa uma URL como '/foto/1', o Flask chama a função 'foto' com '1' como o argumento 'id'.
@app.route('/foto/<int:id>')
def foto(id):

    # Busca a primeira foto na lista que tem o mesmo ID que o parâmetro.
    # Se não encontrar, retorna 'None'.
    # 'next' é uma função integrada do Python que retorna o próximo item de um iterador.
    # Aqui, estamos usando uma expressão geradora dentro de 'next' para iterar sobre 'lista_de_fotos' e encontrar a foto com o ID correspondente.
    # 'foto for foto in lista_de_fotos if foto.id == id' é uma expressão geradora que percorre cada 'foto' em 'lista_de_fotos' e verifica se o 'id' da 'foto' é igual ao 'id' fornecido na URL.
    # Se uma foto correspondente for encontrada, ela é retornada; caso contrário, 'next' retorna 'None', indicando que nenhuma foto com o ID especificado foi encontrada.
    foto = next((foto for foto in lista_de_fotos if foto.id == id), None)


    # Renderiza o template 'foto.html', passando o objeto Foto encontrado.
    # 'render_template' é uma função do Flask que renderiza um template HTML.
    # 'foto.html' é o nome do template que será renderizado.
    # O argumento 'foto=foto' passa o objeto 'foto' encontrado para o template.
    # Dentro do template 'foto.html', você pode acessar e exibir os detalhes dessa foto.
    return render_template('foto.html', foto=foto)

# Verifica se o script é o ponto de entrada principal.
if __name__ == '__main__':

    # Executa o aplicativo Flask em modo de depuração.
    # Isso permite que erros sejam exibidos no navegador e que o servidor
    # reinicie automaticamente durante o desenvolvimento.
    app.run(debug=True)