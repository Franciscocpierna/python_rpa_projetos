# Importa o FastAPI para criação de APIs web modernas e
#       eficientes com Python.
from fastapi import FastAPI, HTTPException

# Importa BaseModel de Pydantic para a criação de 
#       modelos de dados que também realizam validação.
from pydantic import BaseModel

# Importa datetime e timedelta da biblioteca datetime para 
#       manipulação de datas e intervalos de tempo.
from datetime import datetime, timedelta

# Importa Optional de typing para permitir tipos de dados 
#       opcionais em definições de funções e modelos.
from typing import Optional

# Importa a biblioteca calendar para operações relacionadas a
#       calendários, como identificar dias da semana e meses.
import calendar

# Cria uma instância do FastAPI, definindo os metadados da 
#       aplicação como título, versão e descrição.
# Estes metadados são usados na documentação automática da API.
app = FastAPI(
    title="API de Tratamento de Datas",
    version="1.0.0",
    description="API para cálculos e manipulação de datas."
)


# Define a classe DataEntrada, que herda de BaseModel. 
# Esta classe é usada para definir o formato de dados
#       esperado para entradas relacionadas à manipulação de 
#       datas em algumas das funcionalidades da API.
class DataEntrada(BaseModel):

    # Define um atributo 'data' do tipo string. Este atributo é
    #       obrigatório e deve ser fornecido pelo usuário.
    data: str

    # Define um atributo opcional 'formato'. Este campo é do 
    #       tipo string e tem um valor padrão de "%Y-%m-%d",
    #       que corresponde ao formato comum de data ano-mês-dia. 
    # O uso de Optional[str] indica que o formato pode
    #       ser omitido, caso em que o valor padrão é usado.
    formato: Optional[str] = "%Y-%m-%d"


# Define a classe DiferencaDatas, similar à classe DataEntrada,
#       também herdando de BaseModel.
# Esta classe é usada para definir a estrutura de dados para a 
#       entrada quando se deseja calcular a diferença
#       entre duas datas.
class DiferencaDatas(BaseModel):

    # Define os atributos 'data_inicio' e 'data_fim', ambos
    #       obrigatórios e do tipo string, representando as 
    #       datas entre as quais a diferença será calculada.
    data_inicio: str
    data_fim: str

    # Define um atributo opcional 'formato' para 
    #       especificar o formato das datas de entrada.
    # Assim como na classe DataEntrada, o valor 
    #       padrão é "%Y-%m-%d", e o campo é opcional.
    formato: Optional[str] = "%Y-%m-%d"


# Define a classe IdadeEntrada que herda de BaseModel,
#       utilizada para estruturar a entrada de dados.
class IdadeEntrada(BaseModel):

    # Define um atributo obrigatório 'data_nascimento' para
    #       armazenar a data de nascimento como uma string.
    data_nascimento: str

    # Define um atributo opcional 'formato' para especificar o 
    #       formato da data, com um valor padrão definido.
    formato: Optional[str] = "%Y-%m-%d"


# Define uma função auxiliar para validar se uma string
#       corresponde a uma data no formato especificado.
def validar_data(data: str, formato: str) -> datetime:

    try:

        # Tenta converter a string 'data' para um objeto
        #       datetime usando o formato fornecido.
        return datetime.strptime(data, formato)

    except ValueError:

        # Se a conversão falhar devido ao formato incorreto, 
        #       levanta uma exceção HTTP com o status 400.
        raise HTTPException(status_code=400, detail=f"A data '{data}' não é válida no formato '{formato}'.")


# Endpoints
# Este comentário atua como um cabeçalho para a seção do 
#       código onde os endpoints da API são definidos.
# Um endpoint é uma função que é executada em resposta a 
#       uma requisição HTTP a um determinado URL.
# Cada endpoint é associado a uma URL (ou rota) e um 
#       método HTTP (como GET ou POST).

@app.post("/calcular-idade/")
# '@app' é uma instância do aplicativo FastAPI.
# '.post()' é um decorador que especifica que este
#       endpoint responde a solicitações HTTP POST.
# '"/calcular-idade/"' é a rota que deve ser acessada 
#       para acionar este endpoint.
def calcular_idade(dados: IdadeEntrada):

    # 'calcular_idade' é o nome da função que define o que o
    #       endpoint deve fazer.
    # 'dados: IdadeEntrada' indica que esta função espera dados 
    #       no formato definido pela classe IdadeEntrada.

    """
    Documentação do endpoint que explica seu propósito e uso.
    Este endpoint calcula a idade de uma pessoa com base em sua data de nascimento.
    """

    # O corpo da função contém a lógica para calcular a idade e
    #       responder à requisição.
    # Converte a data de entrada para um objeto datetime.
    data_nascimento = validar_data(dados.data_nascimento, dados.formato)

    # Obtém a data atual.
    hoje = datetime.now()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

    # Calcula a idade.
    return {
        "data_nascimento": dados.data_nascimento,
        "idade": idade
    }
    # Retorna a idade calculada e a data de nascimento em um objeto JSON.


# Define um endpoint no aplicativo FastAPI que aceita requisições POST
#       para o caminho '/diferenca-entre-datas/'
@app.post("/diferenca-entre-datas/")
def diferenca_entre_datas(dados: DiferencaDatas):

    """
    Endpoint que calcula a diferença em dias, meses e anos 
            entre duas datas fornecidas.
    Aceita um objeto 'dados' do tipo 'DiferencaDatas' que contém as
            datas de início e fim e o formato em que essas datas são fornecidas.
    """

    # Valida e converte a data de início fornecida pelo usuário para um 
    #       objeto datetime usando a função 'validar_data'.
    data_inicio = validar_data(dados.data_inicio, dados.formato)

    # Valida e converte a data de fim fornecida pelo usuário para um 
    #       objeto datetime usando a função 'validar_data'.
    data_fim = validar_data(dados.data_fim, dados.formato)

    # Calcula a diferença absoluta em dias entre as duas datas.
    # 'days' extrai o número de dias do objeto timedelta gerado pela 
    #       subtração de 'data_fim' por 'data_inicio'.
    delta_dias = abs((data_fim - data_inicio).days)

    # Calcula a diferença absoluta em anos entre as duas datas 
    #       comparando os anos das duas datas.
    delta_anos = abs(data_fim.year - data_inicio.year)

    # Calcula a diferença absoluta em meses.
    # Converte o ano e o mês de cada data em um total de meses 
    #       antes de fazer a subtração para obter a diferença.
    delta_meses = abs((data_fim.year * 12 + data_fim.month) - (data_inicio.year * 12 + data_inicio.month))

    # Retorna um dicionário contendo as datas originais e a diferença 
    #       calculada entre elas em dias, meses e anos.
    # Isso é útil para aplicações que necessitam de uma apresentação 
    #       detalhada da diferença entre duas datas.
    return {
        "data_inicio": dados.data_inicio,
        "data_fim": dados.data_fim,
        "diferenca": {
            "dias": delta_dias,
            "meses": delta_meses,
            "anos": delta_anos
        }
    }


# Define um endpoint no aplicativo FastAPI que aceita requisições POST 
#       para o caminho '/data-por-extenso/'
@app.post("/data-por-extenso/")
def data_por_extenso(dados: DataEntrada):

    """
    Endpoint que converte uma data fornecida em um formato especificado
            para sua representação por extenso.
    Aceita um objeto 'dados' do tipo 'DataEntrada' que contém a data e 
            o formato em que essa data é fornecida.
    """

    # Valida e converte a data fornecida para um objeto datetime 
    #       usando a função 'validar_data'.
    # Esta função também garante que a data esteja no formato correto e 
    #       lançará uma exceção HTTP se não estiver.
    data = validar_data(dados.data, dados.formato)

    # Obtém o nome do dia da semana em inglês usando a função 'weekday()' 
    #       que retorna um índice (0-6, segunda a domingo)
    #       e 'day_name' que retorna o nome completo do dia 
    #       da semana correspondente ao índice.
    dia_semana = calendar.day_name[data.weekday()]

    # Obtém o nome do mês em inglês usando 'month_name' que 
    #       retorna o nome completo do mês
    #       correspondente ao número do mês (1-12).
    mes_extenso = calendar.month_name[data.month]

    # Retorna um dicionário contendo a data original e a data formatada por extenso.
    # Formata a data usando o dia da semana, o dia do mês, o nome do mês e o ano.
    return {
        "data_original": dados.data,
        "data_por_extenso": f"{dia_semana}, {data.day} de {mes_extenso} de {data.year}"
    }


# Decorador FastAPI que define uma rota GET com um parâmetro dinâmico 'ano' na URL.
# Exemplo de acesso: /ano-bissexto/2024
@app.get("/ano-bissexto/{ano}")
def ano_bissexto(ano: int):

    """
    Endpoint para verificar se um ano específico é bissexto.
    Este endpoint aceita um ano como parâmetro na URL e usa a
            biblioteca 'calendar' para determinar
            se o ano é bissexto ou não.

    Parâmetros:
    - ano: Um inteiro representando o ano que será verificado.

    Retorna:
    - Um dicionário com o ano verificado e um booleano
            indicando se é bissexto.

    """

    # Utiliza a função 'isleap' do módulo 'calendar' 
    #       para verificar se o ano é bissexto.
    # 'isleap' retorna True se o ano for bissexto, caso 
    #       contrário, retorna False.
    bissexto = calendar.isleap(ano)

    # Retorna um dicionário contendo o ano consultado e se 
    #       ele é bissexto ou não.
    # O resultado é um booleano que será verdadeiro para 
    #       anos bissextos e falso para não bissextos.
    return {"ano": ano, "bissexto": bissexto}

# uvicorn api_data:app --reload

# Acesse: http://127.0.0.1:8000/docs

# Interface interativa para explorar as rotas e testar endpoints.

# Redoc: http://127.0.0.1:8000/redoc