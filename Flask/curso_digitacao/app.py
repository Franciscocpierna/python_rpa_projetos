# Importa as funções necessárias do framework Flask.
from flask import Flask, render_template

# Cria uma nova instância do aplicativo Flask.
# '__name__' é uma variável especial do Python que indica o nome do módulo ou pacote atual.
# Flask usa isso para saber onde procurar por templates, arquivos estáticos, etc.
app = Flask(__name__)

# Define uma lista de dicionários chamada 'niveis'.
# Cada dicionário representa um nível diferente em um jogo de digitação, contendo nome, tempo e texto.
niveis = [

    # Dicionário para o nível fácil.
    {"nome": "Nível Fácil", "tempo": 60,
     "texto": "Pássaros, com suas plumagens coloridas e cantos melodiosos, simbolizam liberdade e beleza na natureza, voando graciosamente pelos céus."},

    # Dicionário para o nível médio.
    {"nome": "Nível Médio", "tempo": 60,
     "texto": "O descobrimento do Brasil ocorreu em 22 de abril de 1500, quando o navegador português Pedro Álvares Cabral chegou às terras brasileiras. Essa descoberta marcou o início da colonização europeia no país. Cabral e sua tripulação se depararam com uma terra exuberante, habitada por povos indígenas diversos. Esse evento histórico desencadeou uma série de eventos que moldaram a história do Brasil."},

    # Dicionário para o nível difícil.
    {"nome": "Nível Difícil", "tempo": 80,
     "texto": "Os efeitos climáticos globais são variados e impactantes, refletindo-se em padrões meteorológicos extremos, alterações nos ecossistemas e desafios socioeconômicos. O aquecimento global acelera o derretimento das calotas polares, elevando o nível do mar e causando inundações em áreas costeiras. Mudanças nos padrões de precipitação resultam em secas severas, afetando a agricultura e a disponibilidade de água. Ondas de calor mais frequentes e intensas exacerbam os riscos à saúde pública. Fenômenos climáticos extremos, como furacões e incêndios florestais, tornam-se mais comuns, devastando comunidades e ecossistemas. A perda de biodiversidade e deslocamento de espécies são consequências adicionais dessas mudanças climáticas."},

    # Dicionário para o nível avançado.
    {"nome": "Nível Avançado", "tempo": 90,
     "texto": "Python, uma linguagem de programação de alto nível, é renomada por sua simplicidade e legibilidade, tornando-a ideal para iniciantes e especialistas. Seu design enfatiza a legibilidade do código, com uma sintaxe que permite aos programadores expressar conceitos em menos linhas de código em comparação a outras linguagens, como C++ ou Java. Amplamente utilizada para desenvolvimento web, análise de dados, inteligência artificial e aprendizado de máquina, Python suporta múltiplos paradigmas de programação, incluindo programação orientada a objetos e funcional. Sua vasta biblioteca padrão oferece ferramentas para diversas aplicações, desde desenvolvimento web até computação científica. Python é uma linguagem interpretada, o que significa que o código é executado diretamente, facilitando a depuração e a experimentação rápida. A comunidade Python é grande e ativa, fornecendo suporte extenso, com numerosos módulos e frameworks, como Django para desenvolvimento web e Pandas para análise de dados."}
]

# Define a rota principal ('/') do aplicativo.
@app.route('/')
def curso_digitação():

    # Renderiza o template 'curso_digitação.html', passando a lista 'niveis' para o template.
    return render_template('curso_digitação.html', niveis=niveis)


# Define uma rota para jogar um nível específico.
@app.route('/jogo/<int:nivel_id>')
def jogo(nivel_id):

    # Seleciona um nível da lista 'niveis' com base no 'nivel_id' fornecido na URL.
    nivel = niveis[nivel_id]

    # Renderiza o template 'jogo.html', passando o dicionário 'nivel' selecionado para o template.
    return render_template('jogo.html', nivel=nivel)


# Verifica se o script é o ponto de entrada principal.
if __name__ == '__main__':

    # Executa o aplicativo Flask em modo de depuração.
    # Isso permite ver os erros mais detalhadamente e recarregar o servidor automaticamente durante o desenvolvimento.
    app.run(debug=True)
