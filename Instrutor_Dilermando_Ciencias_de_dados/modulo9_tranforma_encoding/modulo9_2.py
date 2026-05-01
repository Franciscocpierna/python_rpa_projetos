## Transformação e Codificação de Variáveis...
## Mini-Projeto 9 - Label Encoding

# A preparação dos dados é uma etapa crucial. Em meio a esse vasto campo de análise e adequação dos dados, 
# uma das tarefas fundamentais é entender e transformar as variáveis presentes nos conjuntos de dados. 
# Através de uma sequência didática cuidadosamente elaborada, podemos explorar esse processo de transformação, 
# capacitando-nos para lidar com variáveis de diferentes naturezas de forma eficiente.

# Através da importação do módulo "datetime", objetivamos focar na manipulação de datas e horários, essenciais 
# em muitos conjuntos de dados do mundo real. Utilizando a data atual como ponto de partida, criamos uma lista 
# contendo as datas dos últimos 30 dias, uma representação prática e relevante para muitos cenários de análise 
# temporal.

# Em seguida, transformamos essa lista em um DataFrame, estrutura de dados tabular, e adicionamos uma coluna 
# indicando o dia da semana correspondente a cada data. Essa etapa não apenas enriquece nosso conjunto de 
# dados com informações contextuais, mas também nos familiariza com as funcionalidades de manipulação de datas 
# do Pandas.

# Para melhorar a utilidade dessa informação, realizamos uma codificação dos dias da semana, convertendo seus 
# nomes em números correspondentes. Esse processo, conhecido como **"label encoding"**, é uma técnica comum 
# para lidar com variáveis categóricas em conjuntos de dados, tornando-as compatíveis com algoritmos de 
# Machine Learning que requerem entradas numéricas.

# Vamos trabalhar com o Pandas... e vamos importar o pacote para manipulação de data e hora (datetime)
import pandas as pd
import datetime

# Extrai a data atual do sistema
data_atual = datetime.datetime.now()

print(data_atual)

print('#'*100)
# Vamos gerar uma lista com a data dos 30 dias anteriores à data atual
lista_datas = [data_atual - datetime.timedelta(days = d) for d in range(0,30) ]
print(lista_datas)
print('#'*100)
df = pd.DataFrame(lista_datas)
print(df.head())
print('#'*100)

# Vamos adequar o nome da coluna
df.columns = ['Data']

print(df.head())
print('#'*100)
# VAmos criar mais uma coluna no dataframe, com o nome do dia da semana, de cada uma das datas.
df['Dia_da_Semana'] = df['Data'].dt.day_name()
print(df)
print('#'*100)
### Label Encoding

# Criamos um dicionário mapeando dia da semana com um número correspondente
# Obs: se o seu sistema estiver em português e se for necessário, use os dias da semana em português
dic_dia_semana = {'Monday':1, 
                   "Tuesday":2,
                   "Wednesday":3,
                   "Thursday":4,
                   "Friday":5,
                   "Saturday":6,
                   "Sunday":7}

# AGORA CHEGAMOS AO PONTO.... FAZER O ENCODING --> label Encoding
# Vamos substituir o nome da semana pelo número correspondente
df['Codigo_Dia_Semana'] = df['Dia_da_Semana'].map(dic_dia_semana)

print(df)
print('#'*100)
print()
print('#'*100)
print()
print('#'*100)
print()
print('#'*100)

