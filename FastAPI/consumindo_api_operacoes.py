# Importa o módulo 'requests', que é uma biblioteca Python
# para fazer requisições HTTP.
# Este módulo facilita enviar requisições para APIs e
# receber respostas através da internet.
import requests

# Define uma constante 'URL_BASE' que armazena a URL base
# da API que você está usando.
# Essa URL é o endereço base no qual a API está hospedada.
# Neste caso, 'http://127.0.0.1:8000' indica que a API está
# rodando localmente no seu computador na porta 8000.
URL_BASE = "http://127.0.0.1:8000"


# Define uma função chamada 'consumir_soma' que é usada para realizar a
# operação de soma através da API.
# A função recebe dois parâmetros: 'numero1' e 'numero2', que
# são os números que você deseja somar.
def consumir_soma(numero1, numero2):

    # Constrói a URL completa para acessar o endpoint específico
    # da API que realiza a soma.
    # 'f"{URL_BASE}/soma"' usa formatação de string para
    # adicionar '/soma' ao final da URL base.
    url = f"{URL_BASE}/soma"

    # Cria um dicionário chamado 'parametros' que contém os
    # parâmetros a serem enviados para a API.
    # Neste caso, os parâmetros são 'numero1' e 'numero2'.
    # Os parâmetros são passados à API através da URL para
    # especificar os números a serem somados.
    parametros = {"numero1": numero1, "numero2": numero2}

    # Faz uma requisição GET à URL construída, passando os parâmetros.
    # 'requests.get()' é a função que envia a requisição HTTP GET
    # ao servidor da API.
    # O argumento 'params=parametros' indica que os parâmetros
    # definidos devem ser enviados junto com a requisição.
    resposta = requests.get(url, params=parametros)

    # Verifica se o código de status da resposta é 200, o que
    # indica sucesso na operação HTTP.
    # O código de status 200 significa que a requisição foi bem-sucedida e
    # a API retornou uma resposta válida.
    if resposta.status_code == 200:

        # 'resposta.json()' converte a resposta JSON recebida
        # da API em um dicionário Python.
        # Retorna esse dicionário, que deve incluir o resultado da soma.
        return resposta.json()

    else:

        # Se o código de status não for 200, retorna um dicionário
        # contendo o código de erro e a mensagem de erro.
        # 'resposta.status_code' contém o código de status HTTP da
        # resposta (ex., 404, 500).
        # 'resposta.text' contém o corpo da resposta como texto, que
        # geralmente inclui uma mensagem de erro.
        return {"erro": resposta.status_code, "mensagem": resposta.text}


# Define uma função chamada 'consumir_subtracao' para interagir com
# uma API que realiza operações de subtração.
# Esta função é projetada para enviar dois números à API e
# receber o resultado da subtração desses números.
# Os parâmetros 'numero1' e 'numero2' são os números que
# serão subtraídos, respectivamente.
def consumir_subtracao(numero1, numero2):

    # Constrói a URL para acessar o endpoint de subtração na API.
    # Utiliza a variável 'URL_BASE', que contém a URL base da API, e
    # adiciona '/subtracao' ao final.
    # Isso especifica o caminho no servidor da API que é configurado
    # para aceitar requisições de subtração.
    url = f"{URL_BASE}/subtracao"

    # Cria um dicionário chamado 'parametros' que mapeia os nomes
    # dos parâmetros esperados pela API aos valores que
    # queremos passar. Aqui, 'numero1' e 'numero2'
    # são as chaves do dicionário, e os valores são os
    # números fornecidos à função. Esses parâmetros serão
    # enviados na URL da requisição.
    parametros = {"numero1": numero1, "numero2": numero2}

    # Envia uma requisição GET para a URL especificada, incluindo os
    # parâmetros definidos.
    # 'requests.get()' é o método utilizado para realizar a requisição HTTP GET.
    # A função retorna um objeto de resposta que inclui todas as
    # informações retornadas pela API.
    resposta = requests.get(url, params=parametros)

    # Verifica se o código de status HTTP da resposta é 200, indicando sucesso.
    # O código de status 200 é padrão para indicar que a requisição foi
    # bem-sucedida e que a API processou a operação sem erros.
    if resposta.status_code == 200:

        # Converte a resposta da API, que é um JSON, para um dicionário
        # Python usando o método 'json()'.
        # Esse dicionário contém o resultado da subtração e qualquer
        # outra informação adicional fornecida pela API.
        return resposta.json()

    else:

        # Se o código de status não for 200, significa que ocorreu
        # algum erro com a requisição.
        # Neste caso, a função retorna um dicionário contendo o código
        # de erro e uma mensagem de erro.
        # 'resposta.status_code' fornece o código de erro HTTP (ex., 404
        # para "Não encontrado", 500 para "Erro interno do servidor", etc.).
        # 'resposta.text' contém a resposta completa em texto, que pode
        # incluir detalhes sobre o que deu errado.
        return {"erro": resposta.status_code, "mensagem": resposta.text}


# Define uma função chamada 'consumir_multiplicacao' para solicitar
# uma operação de multiplicação de uma API.
# Esta função aceita dois argumentos, 'numero1' e 'numero2', que
# são os números a serem multiplicados.
def consumir_multiplicacao(numero1, numero2):

    # Monta a URL para o endpoint de multiplicação na API.
    # A variável 'URL_BASE' contém a URL base da API, e '/multiplicacao' é
    # o caminho específico no servidor da API que trata as
    # requisições de multiplicação.
    url = f"{URL_BASE}/multiplicacao"

    # Cria um dicionário chamado 'parametros' que mapeia os nomes
    # dos parâmetros da API ('numero1' e 'numero2')
    # para os valores que serão passados para a API, que
    # são os números que queremos multiplicar.
    parametros = {"numero1": numero1, "numero2": numero2}

    # Faz uma requisição GET ao servidor da API utilizando a URL
    # especificada e passando os parâmetros.
    # O método 'requests.get()' é utilizado para enviar a requisição e
    # espera-se que a API responda com uma resposta.
    resposta = requests.get(url, params=parametros)

    # Checa o código de status HTTP da resposta para ver se a
    # requisição foi bem-sucedida.
    # O código '200' indica que a requisição foi bem-sucedida e a
    # resposta contém o resultado esperado.
    if resposta.status_code == 200:

        # Se o código de status é 200, a resposta da API é convertida
        # de JSON para um dicionário Python usando 'resposta.json()'.
        # Isso torna mais fácil acessar o resultado da multiplicação e
        # outras informações retornadas pela API.
        return resposta.json()

    else:

        # Se o código de status não for 200, algo deu errado com a requisição.
        # A função então retorna um dicionário contendo o código de
        # erro e a mensagem associada ao erro,
        # o que pode ajudar na depuração e no tratamento de erros.
        # 'resposta.status_code' fornece o código de erro, e
        # 'resposta.text' fornece a descrição do erro.
        return {"erro": resposta.status_code, "mensagem": resposta.text}


# Define uma função chamada 'consumir_divisao' que é responsável
# por interagir com uma API para realizar divisões.
# A função aceita dois argumentos: 'numero1' e 'numero2',
# que são os números a serem divididos.
def consumir_divisao(numero1, numero2):

    # Monta a URL completa que será utilizada para enviar a requisição à API.
    # A URL é composta pela URL base armazenada em 'URL_BASE' e o
    # caminho específico '/divisao' para o endpoint de divisão.
    url = f"{URL_BASE}/divisao"

    # Cria um dicionário chamado 'parametros'. Este dicionário contém
    # as chaves 'numero1' e 'numero2', correspondentes aos
    # números que a API espera receber como parte da
    # requisição para realizar a operação de divisão.
    parametros = {"numero1": numero1, "numero2": numero2}

    # Utiliza a função 'get' do módulo 'requests' para enviar uma
    # requisição HTTP GET ao servidor.
    # A URL é especificada como primeiro argumento e os parâmetros da
    # requisição são passados através do argumento 'params'.
    resposta = requests.get(url, params=parametros)

    # Verifica o código de status da resposta HTTP. Um código de
    # status 200 indica que a requisição foi bem-sucedida.
    if resposta.status_code == 200:

        # Se o código de status for 200, a resposta da API é convertida
        # de JSON para um dicionário Python usando o método 'json'.
        # Este dicionário contém os resultados da operação de
        # divisão e é retornado pela função.
        return resposta.json()

    else:

        # Se o código de status não for 200, indica que houve algum
        # erro com a requisição.
        # A função então retorna um dicionário contendo o código de
        # erro e a mensagem de erro associada.
        # 'resposta.status_code' fornece o código de erro HTTP, e
        # 'resposta.text' fornece a descrição do erro como texto.
        return {"erro": resposta.status_code, "mensagem": resposta.text}


# A condição '__name__ == "__main__"' é usada para garantir que
# este bloco de código só será executado
# se o script for executado diretamente. Isso previne a
# execução do código quando o script é importado como um módulo.
if __name__ == "__main__":

    # Imprime uma linha de texto para indicar que o script começou a consumir a API.
    print("=== Consumindo a API de Operações Matemáticas ===")

    # Chama a função 'consumir_soma' com os números 10 e 5 como argumentos.
    # A função envia uma requisição para a API para calcular a soma de 10 e 5.
    # O resultado da operação é armazenado na variável 'resultado'.
    resultado = consumir_soma(10, 5)

    # Imprime o resultado da soma. 'resultado' deve conter o
    # resultado da operação ou uma mensagem de erro,
    # dependendo da resposta da API.
    print("Soma:", resultado)

    # Similar ao passo anterior, mas chama a função 'consumir_subtracao'
    # para calcular a subtração de 10 por 5.
    resultado = consumir_subtracao(10, 5)

    # Imprime o resultado da subtração.
    print("Subtração:", resultado)

    # Chama a função 'consumir_multiplicacao' para calcular a
    # multiplicação de 10 por 5.
    resultado = consumir_multiplicacao(15, 5)

    # Imprime o resultado da multiplicação.
    print("Multiplicação:", resultado)

    # Chama a função 'consumir_divisao' para calcular a divisão de 10 por 5.
    resultado = consumir_divisao(10, 5)

    # Imprime o resultado da divisão.
    print("Divisão:", resultado)

    # Realiza um teste adicional de divisão para um caso especial: divisão por zero.
    # Chama a função 'consumir_divisao' com os números 10 e 0.
    resultado = consumir_divisao(10, 0)

    # Imprime o resultado da tentativa de divisão por zero.
    # Este teste é importante pois divisão por zero é uma operação
    # indefinida e deve ser tratada adequadamente pela API.
    print("Divisão por zero:", resultado)