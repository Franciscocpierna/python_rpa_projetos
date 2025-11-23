# pip install fastapi[all]
# Importa a classe FastAPI do módulo fastapi
# FastAPI é um framework para criar APIs rápidas e modernas em Python
from fastapi import FastAPI

# Cria uma instância da aplicação FastAPI
# Essa instância será usada para definir rotas e 
# gerenciar o comportamento da API
app = FastAPI()


# Define uma rota HTTP GET com o caminho raiz "/"
# O decorator @app.get("/") indica que a função abaixo será 
# chamada quando o cliente acessar a URL raiz da API
@app.get("/")
def boas_vindas():

    # Retorna um dicionário como resposta à solicitação GET
    # FastAPI converte automaticamente esse dicionário 
    # para JSON antes de enviá-lo ao cliente
    return {"mensagem": "Bem-vindo(a) à minha API!"}

# O código utiliza o FastAPI, um framework que facilita a 
# criação de APIs RESTful.
# A rota definida (/) é o ponto de entrada principal da API.
# Quando a API é acessada na URL raiz, o servidor retorna uma 
# mensagem no formato JSON, como {"mensagem": "Bem-vindo(a) à minha API!"}.


# Executar o servidor
# No terminal, execute: uvicorn api_simples:app --reload

# api_simples: É o nome do arquivo sem a extensão .py.
# app: É a instância do FastAPI criada no código.
# --reload: Habilita recarregamento automático para 
# facilitar o desenvolvimento (útil durante alterações).


# Documentação automática:
# FastAPI fornece uma documentação interativa e pronta:

# Acesse: http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc