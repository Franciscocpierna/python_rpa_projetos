# Importa FastAPI para criar o aplicativo e HTTPException 
#       para tratar erros e respostas HTTP específicas.
from fastapi import FastAPI, HTTPException

# Inicializa uma instância do aplicativo FastAPI.
# Aqui são configurados o título, descrição e versão da 
#       API para documentação automática no FastAPI.
app = FastAPI(

    # Título exibido na documentação da API.
    title="API de Gerador de Tabuadas",

    # Descrição da funcionalidade da API.
    description="Gera a tabuada de qualquer número fornecido.",

    # Versão da API, útil para controle de alterações.
    version="1.0.0"

)


# Define uma rota GET na API que aceita um número
#       como parte da URL.
# O parâmetro "numero" é extraído da URL e "ate" é um
#       parâmetro de consulta opcional com valor padrão de 10.
@app.get("/tabuada/{numero}")
def gerar_tabuada(numero: int, ate: int = 10):

    """
    Gera a tabuada de um número fornecido até um limite especificado.

    Parâmetros:
    - numero (int): O número para o qual a tabuada 
            será gerada (extraído da URL).
    - ate (int): Limite superior para a tabuada (padrão é 10, 
            recebido como parâmetro de consulta).

    Retorno:
    - Um dicionário contendo o número, o limite, e
            a tabuada gerada.

    """

    # Valida se o limite fornecido ('ate') é maior que zero.
    # Se 'ate' for menor ou igual a zero, levanta uma 
    #       exceção HTTP com código 400 (Bad Request).
    if ate <= 0:
        raise HTTPException(status_code=400, detail="O valor de 'ate' deve ser maior que 0.")

    # Gera a tabuada do número fornecido usando uma 
    #       compreensão de dicionário.
    # Para cada número de 1 até 'ate', calcula o
    #       produto de 'numero' com o índice.
    tabuada = {f"{numero} x {i}": numero * i for i in range(1, ate + 1)}

    # Retorna um dicionário contendo:
    # - O número fornecido.
    # - O limite superior 'ate'.
    # - A tabuada gerada como um dicionário.
    return {
        "numero": numero,
        "limite": ate,
        "tabuada": tabuada,
    }

# Para executar o servidor, você deve usar o
#       comando abaixo no terminal:
# uvicorn api_tabuada:app --reload

# Acesse a Documentação Interativa:
# http://127.0.0.1:8000/docs

# Acesse a Documentação Interativa:
# http://127.0.0.1:8000/redoc