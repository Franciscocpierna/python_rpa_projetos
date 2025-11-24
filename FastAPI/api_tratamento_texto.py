# Importa FastAPI do módulo fastapi, que é o framework
# principal para construir a API.
from fastapi import FastAPI

# Importa BaseModel do módulo pydantic, que é utilizado para 
# definir esquemas de dados e realizar validações automáticas.
from pydantic import BaseModel

# Cria uma instância da aplicação FastAPI. Essa instância 'app' 
# será usada para definir os endpoints da API e
# configurar aspectos da aplicação.
app = FastAPI()


# Define uma classe chamada TextoEntrada, que herda de BaseModel.
# Esta classe é usada para definir o esquema de dados esperado nos requests.
# Ao definir propriedades e seus tipos, o Pydantic automaticamente 
# valida os dados de entrada para garantir que eles estejam corretos,
# antes que a lógica do endpoint seja executada.
class TextoEntrada(BaseModel):

    # Define um campo obrigatório do tipo string.
    texto: str

    # Define um campo opcional do tipo string, inicializado como None.
    palavra_antiga: str = None

    # Define um segundo campo opcional do tipo string, 
    # também inicializado como None.
    palavra_nova: str = None


# Este decorador '@app.get("/")' define um endpoint 
# de HTTP GET na raiz do servidor.
# Quando acessado, este endpoint executará a 
# função 'boas_vindas' definida logo abaixo.
@app.get("/")
def boas_vindas():

    # A função retorna um dicionário que será automaticamente
    # convertido pelo FastAPI em uma resposta JSON.
    # A chave 'mensagem' do dicionário contém um texto de 
    # boas-vindas que será exibido ao usuário que
    # acessar este endpoint.
    return {"mensagem": "Bem-vindo(a) à API de Tratamento de Texto!"}


# Este decorador '@app.post("/contar")' define um endpoint
# de HTTP POST para a rota '/contar'.
# Ele espera receber dados como JSON no corpo da requisição, 
# que devem ser validados de acordo com o modelo 'TextoEntrada'.
@app.post("/contar")
def contar_elementos(dados: TextoEntrada):

    # A variável 'texto' é extraída do objeto 'dados', que é
    # uma instância do modelo 'TextoEntrada'.
    # 'dados.texto' acessa diretamente o campo 'texto' do modelo.
    texto = dados.texto

    # Calcula o número de caracteres no texto usando a 
    # função 'len()', que retorna o comprimento da string.
    numero_caracteres = len(texto)

    # Calcula o número de palavras no texto. 'texto.split()' 
    # divide a string em uma lista de palavras usando
    # espaços como delimitador padrão.
    # 'len(texto.split())' conta quantos elementos (palavras)
    # existem na lista resultante.
    numero_palavras = len(texto.split())

    # Calcula o número de frases no texto. A string é dividida em
    # uma lista usando '.' como delimitador para identificar as frases.
    # A compreensão de lista '[frase for frase in texto.split(".") 
    # if frase.strip() != ""]' é usada para filtrar e contar
    # apenas as frases que não são apenas espaços.
    numero_frases = len([frase for frase in texto.split(".") if frase.strip() != ""])

    # Retorna um dicionário com os resultados calculados. Este dicionário é 
    # convertido em JSON pelo FastAPI e enviado como resposta.
    return {
        "numero_caracteres": numero_caracteres,
        "numero_palavras": numero_palavras,
        "numero_frases": numero_frases,
    }


# Este decorador '@app.post("/maiusculas")' define um endpoint na 
# rota '/maiusculas' que aceita requisições POST.
# Ele espera receber dados que correspondam ao modelo 'TextoEntrada'.
@app.post("/maiusculas")
def converter_maiusculas(dados: TextoEntrada):

    # A função acessa o campo 'texto' do modelo de dados 'TextoEntrada'.
    # O método '.upper()' é chamado sobre a string 'dados.texto'. 
    # Este método converte todas as letras da string para maiúsculas.
    # O resultado é retornado como parte de um dicionário
    # com a chave 'texto_maiusculas'.
    # O FastAPI automaticamente converte este dicionário 
    # para JSON ao enviar a resposta ao cliente.
    return {"texto_maiusculas": dados.texto.upper()}


# Este decorador define um endpoint na rota '/minusculas' que
# também aceita requisições POST.
# Semelhante ao endpoint anterior, ele utiliza o modelo 'TextoEntrada'
# para validar os dados recebidos.
@app.post("/minusculas")
def converter_minusculas(dados: TextoEntrada):

    # Aqui, o método '.lower()' é utilizado sobre a string 'dados.texto'.
    # Este método converte todas as letras da string para minúsculas.
    # O resultado da conversão é retornado dentro de um dicionário 
    # com a chave 'texto_minusculas'.
    # Como no endpoint anterior, o FastAPI cuida da serialização 
    # do dicionário para JSON.
    return {"texto_minusculas": dados.texto.lower()}


# Este decorador '@app.post("/remover_espacos")' registra um 
# endpoint que aceita requisições POST na rota '/remover_espacos'.
# O endpoint usa o modelo 'TextoEntrada' para validar e
# extrair os dados de entrada.
@app.post("/remover_espacos")
def remover_espacos(dados: TextoEntrada):

    # A função 'split()' é usada para dividir a string 'dados.texto' em
    # uma lista de palavras, removendo quaisquer espaços em
    # branco excessivos.
    # 'join()' é então usado para unir essas palavras de volta em 
    # uma única string com um único espaço entre cada palavra.
    # Esse método é eficaz para normalizar espaços entre as palavras, 
    # removendo espaços extras no início, no final e entre as palavras.
    return {"texto_sem_espacos": " ".join(dados.texto.split())}


# Este decorador define um endpoint na rota '/inverter' que
# processa requisições POST.
# Ele também utiliza o modelo 'TextoEntrada' para assegurar que 
# os dados de entrada sejam corretos.
@app.post("/inverter")
def inverter_texto(dados: TextoEntrada):

    # Utiliza o fatiamento de strings em Python para inverter a
    # ordem dos caracteres da string 'dados.texto'.
    # 'dados.texto[::-1]' cria uma nova string que é a string original 
    # invertida, onde '::-1' especifica um passo de -1,
    # invertendo a string.
    return {"texto_invertido": dados.texto[::-1]}


# Define um endpoint POST na rota '/substituir' que processa a 
# substituição de palavras em um texto.
@app.post("/substituir")
def substituir_texto(dados: TextoEntrada):

    # Primeiro, verifica se as palavras necessárias para a
    # substituição ('palavra_antiga' e 'palavra_nova') foram fornecidas.
    # Se qualquer uma delas estiver ausente, retorna 
    # uma mensagem de erro.
    if not dados.palavra_antiga or not dados.palavra_nova:
        return {"erro": "Por favor, forneça as palavras para substituição."}

    # Se as palavras necessárias estão presentes, realiza a substituição 
    # utilizando o método 'replace()'.
    # 'replace()' substitui todas as ocorrências da 'palavra_antiga' 
    # pela 'palavra_nova' na string 'dados.texto'.
    texto_modificado = dados.texto.replace(dados.palavra_antiga, dados.palavra_nova)

    # Retorna o texto modificado como resultado.
    return {"texto_modificado": texto_modificado}


# Define um endpoint POST na rota '/primeiro_nome' que 
# extrai o primeiro nome de um texto.
@app.post("/primeiro_nome")
def extrair_primeiro_nome(dados: TextoEntrada):

    # Divide o texto de entrada em palavras, assumindo que
    # são separadas por espaços.
    nomes = dados.texto.split()

    # Verifica se há pelo menos um nome na lista 'nomes'.
    # Se a lista não estiver vazia, retorna o primeiro 
    # elemento como 'primeiro_nome'.
    if nomes:
        return {"primeiro_nome": nomes[0]}

    # Se a lista estiver vazia, indica que o texto de entrada não 
    # contém palavras válidas e retorna um erro.
    return {"erro": "Texto vazio ou sem nome válido"}


# Define um endpoint POST na rota '/ultimo_nome' que processa a 
# extração do último nome de uma string de texto.
@app.post("/ultimo_nome")
def extrair_ultimo_nome(dados: TextoEntrada):

    # Divide o texto em palavras usando espaços como delimitador.
    nomes = dados.texto.split()

    # Verifica se a lista de palavras (nomes) não está vazia.
    if nomes:

        # Retorna o último elemento da lista, que é assumido como o último nome.
        return {"ultimo_nome": nomes[-1]}

    # Se a lista estiver vazia, retorna uma mensagem de erro 
    # indicando que o texto não contém nomes válidos.
    return {"erro": "Texto vazio ou sem nome válido"}


# Define um endpoint POST na rota '/tamanho_palavra' para 
# encontrar a maior palavra em um texto.
@app.post("/tamanho_palavra")
def calcular_tamanho_maior_palavra(dados: TextoEntrada):

    # Divide o texto em palavras usando espaços como delimitador.
    palavras = dados.texto.split()

    # Verifica se a lista de palavras não está vazia.
    if palavras:

        # Utiliza a função 'max' com a chave 'len' para encontrar a
        # palavra mais longa na lista.
        maior_palavra = max(palavras, key=len)

        # Retorna a palavra mais longa e seu tamanho.
        return {"maior_palavra": maior_palavra, "tamanho": len(maior_palavra)}

    # Se a lista estiver vazia, retorna uma mensagem de erro
    # indicando que o texto não contém palavras.
    return {"erro": "Texto vazio ou sem palavras"}


# Define um endpoint na API que aceita requisições POST
# na rota '/capitalizar'.
# O endpoint é configurado para receber dados no formato
# especificado pela classe 'TextoEntrada'.
@app.post("/capitalizar")
def capitalizar_palavras(dados: TextoEntrada):

    # A função 'title()' é aplicada à string 'dados.texto'.
    # Este método retorna uma nova string onde a primeira letra de 
    # cada palavra é maiúscula e as demais letras são minúsculas.
    # É útil para formatar títulos de textos, nomes ou qualquer 
    # string onde esse formato seja desejado.
    # Exemplo: "hello world" se torna "Hello World".
    return {"texto_capitalizado": dados.texto.title()}



# Para executar o servidor, você deve usar o 
#       comando abaixo no terminal:
# uvicorn api_tratamento_texto:app --reload

# Acesse a Documentação Interativa:
# Acesse: http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc