# Importa a biblioteca 'requests', que é usada para 
# realizar requisições HTTP.
# Aqui será utilizada para se conectar à API que gera a tabuada.
import requests


def gerar_tabuada_simples(numero, limite=10):

    """
    Gera a tabuada de um número de forma simples.

    :param numero: Número para o qual a tabuada será gerada.
    :param limite: Limite superior da tabuada (padrão é 10).
    :return: Tabuada formatada ou mensagem de erro.
    """

    # Define a função 'gerar_tabuada_simples', que realiza o
    # consumo da API para gerar uma tabuada.
    # Recebe dois parâmetros:
    # - 'numero': o número base da tabuada.
    # - 'limite': o número até onde a tabuada será calculada (valor padrão é 10).

    try:

        # Define a URL base da API
        # Constrói a URL para realizar a requisição à API.
        # Utiliza o número e o limite fornecidos para completar o endpoint.
        # Exemplo: Para numero=5 e limite=12, a URL gerada será:
        # "http://127.0.0.1:8000/tabuada/5?ate=12"
        URL_API = f"http://127.0.0.1:8000/tabuada/{numero}?ate={limite}"

        # Faz a requisição GET para a API
        # Usa a função 'requests.get()' para enviar uma 
        # requisição HTTP do tipo GET à URL gerada.
        # A API deve retornar a tabuada no formato JSON.
        resposta = requests.get(URL_API)

        # Verifica se houve erros HTTP
        # O método 'raise_for_status()' verifica o código de status HTTP da resposta.
        # Caso o código de status seja um erro (4xx ou 5xx), ele levanta uma exceção.
        resposta.raise_for_status()

        # Processa a resposta da API
        # A resposta da API é convertida de JSON para um
        # dicionário Python usando 'resposta.json()'.
        # O método '.get("tabuada", {})' obtém a chave "tabuada" 
        # do dicionário retornado.
        # Caso a chave não exista (o que é improvável se a API 
        # estiver correta), retorna um dicionário vazio como padrão.
        tabuada = resposta.json().get("tabuada", {})

        # Retorna a tabuada formatada como string
        # Converte o dicionário 'tabuada' em uma string formatada.
        # Para cada par chave-valor no dicionário, cria uma 
        # linha no formato "chave = valor".
        # Exemplo: Se a tabuada contém {"5 x 1": 5, "5 x 2": 10}, o 
        # resultado será:
        # "5 x 1 = 5\n5 x 2 = 10"
        return "\n".join([f"{chave} = {valor}" for chave, valor in tabuada.items()])

    except requests.exceptions.RequestException as e:

        # Captura exceções relacionadas à requisição HTTP, 
        # como erros de conexão ou tempo limite.
        # Retorna uma mensagem de erro detalhando o problema.
        return f"Erro: {e}"


# Exemplo de uso
# Chama a função 'gerar_tabuada_simples' com o número 5 e limite 12.
# O resultado da função será exibido diretamente no terminal.
print(gerar_tabuada_simples(8, 10))  # Tabuada do número 5 até 12