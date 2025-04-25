'''
Exemplo: Como extrair a cotação do dólar com uma API
Abaixo está um exemplo prático de código em Python, utilizando a biblioteca requests e a API do site AwesomeAPI, que retorna a cotação atual do dólar em relação ao real brasileiro:
'''

# Importa a biblioteca necessária
import requests
 
# Função para obter a cotação do dólar usando a API AwesomeAPI
def obter_cotacao_dolar():
    # URL da API para dólar em relação ao real
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
 
    try:
        # Envia uma requisição GET para a API
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na resposta
 
        # Converte o conteúdo da resposta para JSON
        dados = resposta.json()
 
        # Extrai o valor da cotação de compra (bid)
        cotacao = dados['USDBRL']['bid']
 
        # Exibe a cotação
        print(f"Cotação atual do dólar: R$ {cotacao}")
        return cotacao
 
    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API:", erro)
    except Exception as erro:
        print("Erro ao processar os dados:", erro)
 
# Chamada da função
obter_cotacao_dolar()
