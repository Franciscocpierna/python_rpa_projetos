# Importa a classe FastAPI e a classe HTTPException do módulo fastapi.
# FastAPI é utilizado para criar a aplicação web com 
#        funcionalidades de API.
# HTTPException é usado para gerenciar exceções específicas 
# de HTTP, permitindo retornar erros de estado HTTP específicos.
from fastapi import FastAPI, HTTPException

# Cria uma nova instância do objeto FastAPI.
# Este objeto 'app' é o núcleo da nossa aplicação, sendo usado 
# para criar rotas e lidar com solicitações HTTP.
app = FastAPI()


# O decorador '@app.get("/")' é usado para definir uma rota na aplicação.
# Ele especifica que a função abaixo será chamada quando houver 
# uma solicitação GET para a URL raiz '/'.
@app.get("/")
def boas_vindas():

    # A função 'boas_vindas' é definida para responder às
    # solicitações para a rota raiz.
    # Ela não recebe nenhum parâmetro e retorna um dicionário Python.
    # Este dicionário é automaticamente convertido pelo FastAPI 
    # em uma resposta JSON.
    # O dicionário contém uma chave 'mensagem' com uma saudação como valor.
    return {"mensagem": "Bem-vindo(a) à API de Operações Matemáticas!"}


# Decorador para a rota "/soma" que especifica uma operação GET.
# Este decorador define que a função 'soma' será chamada 
# quando a rota '/soma' for acessada via GET.
# A função 'soma' aceita dois parâmetros float, 'numero1' e 'numero2', 
# que devem ser fornecidos como parâmetros de consulta na URL.
@app.get("/soma")
def soma(numero1: float, numero2: float):

    # Realiza a soma dos dois números fornecidos.
    # Os valores 'numero1' e 'numero2' são convertidos para float 
    # pelo FastAPI baseando-se na anotação de tipo e depois somados.
    resultado = numero1 + numero2

    # Retorna um dicionário contendo a descrição da operação, 
    # os números usados e o resultado.
    # Esse dicionário é automaticamente convertido em JSON 
    # pelo FastAPI e enviado ao cliente como resposta.
    return {"operacao": "soma", "numero1": numero1, "numero2": numero2, "resultado": resultado}


# Decorador para a rota "/subtracao" que também especifica
# uma operação GET.
# Semelhante à rota de soma, esta função é chamada quando '/subtracao' é 
# acessada com método GET.
# Ela também requer dois parâmetros float 'numero1' e 'numero2', 
# fornecidos via parâmetros de consulta.
@app.get("/subtracao")
def subtracao(numero1: float, numero2: float):

    # Realiza a subtração de 'numero1' por 'numero2'.
    # A subtração é feita diretamente aqui, e o resultado é 
    # armazenado na variável 'resultado'.
    resultado = numero1 - numero2

    # Retorna um dicionário que inclui os detalhes da operação matemática.
    # A resposta inclui tanto os números utilizados quanto o 
    # resultado da operação de subtração.
    return {"operacao": "subtração", "numero1": numero1, "numero2": numero2, "resultado": resultado}


# Decorador para definir uma rota GET em "/multiplicacao".
# Esta função é chamada quando a URL '/multiplicacao' é 
# acessada com o método GET.
# Os parâmetros 'numero1' e 'numero2' são esperados na URL 
# como query parameters e devem ser do tipo float.
@app.get("/multiplicacao")
def multiplicacao(numero1: float, numero2: float):

    # Multiplica os dois números fornecidos.
    # 'numero1' e 'numero2' são multiplicados, e o resultado é 
    # armazenado na variável 'resultado'.
    resultado = numero1 * numero2

    # Retorna um dicionário contendo a operação realizada, os 
    # números envolvidos e o resultado.
    # Este dicionário é automaticamente convertido em JSON 
    # pelo FastAPI ao enviar a resposta ao cliente.
    return {"operacao": "multiplicação", "numero1": numero1, "numero2": numero2, "resultado": resultado}


# O decorador '@app.get("/divisao")' é usado para criar 
# uma rota GET na URL '/divisao'.
# FastAPI usará essa rota para encaminhar as requisições GET 
# recebidas para a função 'divisao'.
# Os parâmetros 'numero1' e 'numero2' são especificados como 
# parte da URL de consulta e devem ser do tipo float.
@app.get("/divisao")
def divisao(numero1: float, numero2: float):

    # Início do bloco de verificação do valor do divisor.
    # Esta condição checa se o valor do 'numero2', que atua 
    # como divisor na operação de divisão, é igual a zero.
    # Dividir por zero é uma operação indefinida na matemática e
    # pode causar erros de execução.
    if numero2 == 0:

        # Levanta uma exceção HTTP usando a classe HTTPException,
        # que é parte do FastAPI.
        # A exceção interrompe o fluxo normal da função e retorna uma 
        # resposta HTTP com o código 400, que significa "Bad Request".
        # O detalhe "Divisão por zero não é permitida" é uma mensagem 
        # explicativa que acompanha o código de erro, informando o
        # usuário sobre o problema.
        raise HTTPException(status_code=400, detail="Divisão por zero não é permitida")

    # Calcula o resultado da divisão de 'numero1' por 'numero2'.
    # Esta linha é executada somente se a condição acima não for verdadeira,
    # ou seja, se 'numero2' não for zero.
    # O resultado da divisão é armazenado na variável 'resultado'.
    resultado = numero1 / numero2

    # Prepara a resposta para a requisição.
    # Cria um dicionário que inclui a operação realizada ("divisão"), 
    # os valores de 'numero1' e 'numero2', e o 'resultado' da divisão.
    # Este dicionário é retornado pela função e o FastAPI cuida 
    # de serializá-lo em JSON.
    # O JSON é o formato de resposta que será enviado de volta ao
    # cliente que fez a requisição HTTP.
    return {"operacao": "divisão", "numero1": numero1, "numero2": numero2, "resultado": resultado}

# uvicorn api_operacoes:app --reload

# Acesse a Documentação Interativa:
# Acesse: http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc