# Importa o módulo 'requests', uma biblioteca HTTP para Python que
# simplifica fazer solicitações à web
import requests


# Define uma função chamada 'consumir_api_e_imprimir' que
# aceita um parâmetro 'endpoint'
def consumir_api_e_imprimir(endpoint):

    try:

        # A função 'requests.get' é usada para fazer uma
        # requisição GET para a URL fornecida.
        # O resultado é armazenado na variável 'response'
        response = requests.get(endpoint)

        # 'raise_for_status' lança uma exceção se a requisição
        # HTTP falhou (e.g., 404, 501, etc.)
        response.raise_for_status()

        # O método '.json()' converte a resposta JSON recebida em
        # um dicionário Python
        dados = response.json()

        # Verifica se a chave 'mensagem' está presente nos dados JSON
        if "mensagem" in dados:

            # Se 'mensagem' existir, imprime a mensagem formatada
            print(f"Mensagem da API: {dados['mensagem']}")

        else:

            # Se 'mensagem' não estiver presente, imprime uma mensagem padrão
            print("A resposta da API não contém a chave 'mensagem'.")

    except requests.exceptions.RequestException as e:

        # Captura qualquer exceção relacionada a requisições e
        # imprime uma mensagem de erro personalizada
        print(f"Erro ao acessar a API: {e}")


# Define uma variável 'url_api' que contém a URL da API que você deseja acessar
url_api = "http://127.0.0.1:8000/"  # Atualize com a URL correta da API

# Chama a função 'consumir_api_e_imprimir' passando a URL
# da API como argumento
consumir_api_e_imprimir(url_api)

"""
import requests: Este comando carrega a biblioteca requests, que fornece 
        ferramentas para realizar todos os tipos de operações HTTP de maneira 
        programática e simplificada.

try-except: Este bloco é usado para lidar com exceções de forma a prevenir 
        falhas na execução do programa devido a erros durante as requisições HTTP, 
        como problemas de conexão, URL inválida, ou problemas de servidor.

if-else: Essa estrutura condicional permite responder de maneira diferente dependendo 
        dos dados recebidos da API, o que torna o script mais flexível e informativo sobre o 
        que está ocorrendo com a comunicação HTTP.

Esse padrão de script é útil para testar APIs ou integrar sistemas que dependem de 
serviços web externos.
"""