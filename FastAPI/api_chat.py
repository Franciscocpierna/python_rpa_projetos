# Importa a classe FastAPI do módulo fastapi.
# A FastAPI é usada para criar APIs web de
#       maneira eficiente e moderna.
from fastapi import FastAPI

# Importa a classe BaseModel do módulo pydantic.
# BaseModel é usada para criar modelos de dados
#       para validação e documentação automática.
from pydantic import BaseModel

# Inicializa o aplicativo FastAPI.
# Cria uma instância do aplicativo FastAPI e configura
#       informações como título, descrição e versão da API.
# Estes metadados serão exibidos automaticamente na
#       documentação gerada pela FastAPI.
app = FastAPI(

    # Define o título da API exibido na documentação.
    title="Chat API Manual",

    # Descrição do propósito da API.
    description="API que responde perguntas usando similaridade calculada manualmente",

    # Define a versão atual da API.
    version="1.0.0"

)


# Define um modelo de dados para a entrada.
# 'Pergunta' é uma classe que herda de BaseModel e
#       representa o formato esperado dos dados de entrada.
class Pergunta(BaseModel):

    # Define que a entrada deve conter um campo
    #       chamado 'texto' do tipo string.
    texto: str


# Define um modelo de dados para a saída.
# 'Resposta' é uma classe que herda de BaseModel e
#       representa o formato dos dados que serão retornados.
class Resposta(BaseModel):

    # Define que a saída conterá um campo
    #       chamado 'resposta' do tipo string.
    resposta: str


# Base de conhecimento
base_conhecimento = {

    "qual é a capital do brasil?": "A capital do Brasil é Brasília.",
    "quem descobriu o brasil?": "O Brasil foi descoberto por Pedro Álvares Cabral em 1500.",
    "qual é o maior planeta do sistema solar?": "O maior planeta do sistema solar é Júpiter.",
    "qual é a velocidade da luz?": "A velocidade da luz é aproximadamente 299.792 km/s.",
    "quem é o autor de dom casmurro?": "O autor de Dom Casmurro é Machado de Assis.",
    "qual é o menor país do mundo?": "O menor país do mundo é o Vaticano.",
    "quem pintou a mona lisa?": "A Mona Lisa foi pintada por Leonardo da Vinci.",
    "qual é o elemento químico mais abundante no universo?": "O elemento químico mais abundante no universo é o hidrogênio.",
    "qual é o animal terrestre mais rápido do mundo?": "O animal terrestre mais rápido do mundo é o guepardo, que pode atingir até 120 km/h.",
    "quem foi o primeiro homem a pisar na lua?": "O primeiro homem a pisar na Lua foi Neil Armstrong, em 1969.",
    "qual é o maior oceano do mundo?": "O maior oceano do mundo é o Oceano Pacífico.",
    "qual é o rio mais extenso do mundo?": "O rio mais extenso do mundo é o Rio Amazonas.",
    "qual é a montanha mais alta do mundo?": "A montanha mais alta do mundo é o Monte Everest, com 8.848 metros de altitude.",
    "quem é o criador do sistema operacional linux?": "O criador do sistema operacional Linux é Linus Torvalds.",
    "qual é o significado da sigla www?": "A sigla WWW significa World Wide Web.",
    "quantos ossos tem o corpo humano?": "O corpo humano adulto possui 206 ossos.",
    "qual é a fórmula química da água?": "A fórmula química da água é H₂O.",
    "em que ano ocorreu a independência do brasil?": "A independência do Brasil ocorreu em 1822.",
    "qual é o maior deserto do mundo?": "O maior deserto do mundo é o Deserto do Saara, localizado na África.",
    "quem escreveu o livro o pequeno príncipe?": "O livro O Pequeno Príncipe foi escrito por Antoine de Saint-Exupéry.",

}


# Função para calcular a similaridade entre duas strings
# Esta função calcula o índice de similaridade entre duas
#       strings, baseado na interseção e união dos caracteres.
# Retorna um valor entre 0 e 1, onde 0 indica nenhuma
#       similaridade e 1 significa igualdade completa.
def calcular_similaridade(texto1: str, texto2: str) -> float:

    """
    Calcula a similaridade entre duas strings usando
            interseção de caracteres.

    :param texto1: Primeira string para comparação.
    :param texto2: Segunda string para comparação.
    :return: Índice de similaridade entre 0 e 1.
    """

    # Remove espaços extras no início e no final de ambas as strings.
    # Converte todas as letras para minúsculas para
    #       garantir que a comparação seja case-insensitive.
    # Exemplo: "Brasil " e "brasil" serão tratados como iguais.
    texto1 = texto1.lower().strip()
    texto2 = texto2.lower().strip()

    # Divide as strings em conjuntos de caracteres únicos.
    # 'set(texto1)' cria um conjunto contendo os
    #       caracteres únicos da string texto1.
    # Exemplo: "brasil" se transforma em {'b', 'r', 'a', 's', 'i', 'l'}.
    set1 = set(texto1)
    set2 = set(texto2)

    # Calcula a interseção dos conjuntos.
    # A interseção contém os caracteres que aparecem
    #       em ambos os conjuntos.
    # Exemplo: {'b', 'r', 'a', 's', 'i', 'l'} ∩ {'r', 'a', 's'} = {'r', 'a', 's'}.
    interseccao = set1.intersection(set2)

    # Calcula a união dos conjuntos.
    # A união contém todos os caracteres únicos presentes
    #       em ambos os conjuntos.
    # Exemplo: {'b', 'r', 'a', 's', 'i', 'l'} ∪ {'r', 'a', 's'} = {'b', 'r', 'a', 's', 'i', 'l'}.
    uniao = set1.union(set2)

    # Retorna o índice de similaridade.
    # O índice é calculado como o tamanho da interseção
    #       dividido pelo tamanho da união.
    # Se a união estiver vazia (strings vazias),
    #       retorna 0 para evitar divisão por zero.
    # Exemplo: len({'r', 'a', 's'}) / len({'b', 'r', 'a', 's', 'i', 'l'}) = 3 / 6 = 0.5.
    return len(interseccao) / len(uniao) if len(uniao) > 0 else 0


# Define um endpoint POST na rota "/perguntar".
# A função 'perguntar' será executada quando uma
#       solicitação POST for enviada para esta rota.
# O parâmetro 'response_model=Resposta' especifica que
#       a resposta da função deve ser estruturada no formato
#       definido pelo modelo 'Resposta'.
@app.post("/perguntar", response_model=Resposta)
async def perguntar(pergunta: Pergunta):

    """
    Endpoint que responde perguntas usando similaridade manual.
    """

    # Declara a função 'perguntar', que aceita um
    #       objeto do tipo 'Pergunta' como entrada.
    # A entrada será validada automaticamente pelo FastAPI
    #       com base no modelo definido.

    # Normaliza o texto da pergunta recebida:
    # - Remove espaços extras no início e no final ('strip()').
    # - Converte todo o texto para letras minúsculas ('lower()')
    #       para garantir que a comparação seja case-insensitive.
    texto = pergunta.texto.strip().lower()

    # Cria uma lista de todas as perguntas existentes
    #       na base de conhecimento.
    # As chaves do dicionário 'base_conhecimento'
    #       representam as perguntas disponíveis.
    perguntas = list(base_conhecimento.keys())

    # Calcula a similaridade de cada pergunta da base com a
    #       pergunta recebida.
    # Usa a função 'calcular_similaridade' para medir o quão
    #       similar a pergunta do usuário é em relação a
    #       cada pergunta da base.
    # O resultado é armazenado em um dicionário, onde:
    # - A chave é a pergunta da base.
    # - O valor é a similaridade calculada.
    similaridades = {p: calcular_similaridade(texto, p) for p in perguntas}

    # Encontra a pergunta mais similar da base.
    # 'max()' é usado para encontrar a chave (pergunta)
    #       com o maior valor de similaridade.
    pergunta_mais_similar = max(similaridades, key=similaridades.get)

    # Obtém o valor máximo de similaridade encontrado.
    # Esse valor indica o grau de similaridade entre a
    #       pergunta do usuário e a pergunta mais próxima da base.
    similaridade_maxima = similaridades[pergunta_mais_similar]

    # Define um limite mínimo de similaridade para
    #       considerar a resposta válida.
    # O valor padrão é 0.5, mas pode ser ajustado
    #       com base na precisão desejada.
    limite_similaridade = 0.5

    if similaridade_maxima >= limite_similaridade:

        # Se a similaridade máxima for maior ou igual ao limite definido:
        # Busca a resposta correspondente à pergunta mais
        #       similar na base de conhecimento.
        resposta = base_conhecimento[pergunta_mais_similar]

    else:

        # Caso contrário, retorna uma resposta genérica
        #       indicando que a pergunta não foi compreendida.
        resposta = "Desculpe, não sei responder a essa pergunta no momento."

    # Retorna a resposta no formato do modelo 'Resposta'.
    # O modelo adiciona estrutura à saída e garante
    #       consistência na resposta JSON.
    return Resposta(resposta=resposta)

# Para rodar o servidor
# Use: uvicorn api_chat:app --reload

# Acesse a Documentação Interativa:
# http://127.0.0.1:8000/docs

# Acesse a Documentação Interativa:
# http://127.0.0.1:8000/redoc