


## <font color='green'>Projeto 3 - Trabalhando com Datas</font>
## <font color='green'>Instalando os Pacotes e Carregando os Dados</font>


## Instalando e Carregando os Pacotes



# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada :', python_version())




# Para atualizar um pacote, execute o comando abaixo no terminal ou prompt de comando:
# pip install -U nome_pacote

# Para instalar a versão exata de um pacote, execute o comando abaixo no terminal ou prompt de comando:
# !pip install nome_pacote==versão_desejada

# Depois de instalar ou atualizar o pacote, reinicie o jupyter notebook.

# Instala o pacote watermark. 
# Esse pacote é usado para gravar as versões de outros pacotes usados neste jupyter notebook.
#!pip install -q -U watermark

#Importação dos módulos básicos
import numpy as np
import pandas as pd
# Importação de módulo para trabalhar com datas
import datetime
# módulos para fazer os gráficos (plotagens)
import seaborn as sns
import matplotlib.pyplot as plt
# módulo para ignorar mensagens de alerta
import warnings
warnings.filterwarnings('ignore')

## Carregando os Dados



### Dataset público: *Landslides After Rainfal*

# Neste projeto vamos trabalhar com o dataset **"Landslides After Rainfall"** que registra os deslizamentos 
# causados após as chuvas. De uma forma geral, deslizamentos de terra são um dos perigos mais difundidos no mundo
# causando mais de 11.500 mortes em 70 países desde 2007. Saturando o solo em encostas vulneráveis, chuvas 
# intensas e prolongadas são o gatilho de deslizamento de terra mais frequente.

# Neste sentido, o Catálogo Global de Deslizamentos (GLC) foi desenvolvido para identificar eventos de 
# deslizamentos desencadeados por chuvas em todo o mundo, independentemente do tamanho, impactos ou 
# localização. 

# O GLC considera todos os tipos de movimentos de massa desencadeados por chuvas, que foram relatados na 
# mídia, bancos de dados de desastres, relatórios científicos ou outras fontes.  

# Fonte: https://www.kaggle.com/code/rtatman/data-cleaning-challenge-parsing-dates/input?select=catalog.csv

# Este arquivo estará disponível como recurso dessa aula.
# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "undefined"]


# Carrega o dataset
deslizamentos = pd.read_csv("dados/deslizamentos.csv", na_values = lista_labels_valores_ausentes)

print(deslizamentos.info())


print('#'*100)

# Vamos dar uma olhada nos dados.

print(deslizamentos.head())


print(deslizamentos.shape)



print('#'*100)

contagem_valores_ausentes = deslizamentos.isnull().sum()
contagem_valores_ausentes[0:20]

print(contagem_valores_ausentes)

print('#'*100)
# Calculando os totais de celulas e de celulas com valores ausentes (total_nulos) ==>  DESLIZAMENTOS
total_celulas = np.prod(deslizamentos.shape)
total_nulos = contagem_valores_ausentes.sum()
# Calculando o percentual de dados ausentes em DESLIZAMENTOS
print(f"Percentual de Dados ausentes em DESLIZAMENTOS: {(total_nulos/total_celulas):.2%}")


## Trabalhando com Datas

# Muitos conjuntos de dados têm uma coluna de data e, às vezes, você pode ter que lidar com requisitos como 
# buscar dados transacionais para um determinado mês ou datas de um mês. Nesses casos, você deve saber como 
# analisar esse tipo de dado em específico... Vamos utilizar os datasets que importamos para estudar isso...

### Verificação do tipo de dados da coluna de data
#Para tanto, vamos trabalhar com a coluna de data do dataframe de *deslizamentos*. A primeira coisa que vamos 
# fazer é dar uma olhada nas primeiras linhas para ter certeza que o campo de data contém a informação que 
# pensamos ter.


# mostrando as primeiras linhas da coluna de data
print(deslizamentos['date'].head())


print('#'*100)

# Sim, são datas! Mas só porque eu, um humano, posso dizer que são datas não significa que Python saiba que são
# datas. Observe que na parte inferior da saída do método head(), você pode ver que ele diz que o tipo de dados desta coluna é **"objeto"**.

# O Pandas usa o tipo de dado **"objeto"** para armazenar vários tipos de dados, mas na maioria das vezes, 
# quando você vê uma coluna com o tipo de dados "objeto", ela deverá conter *strings*.

# Se você verificar a documentação do pandas sobre "dtype", notará que também há um tipo de dados específico 
# chamado de **datetime64**. Como o tipo de dados dessa coluna é *objeto* em vez de *datetime64*, podemos dizer 
# que o Python não sabe que esta coluna contém datas.

# verificando o tipo de dados dessa coluna de data
# Também podemos ver apenas o tipo de dados dessa coluna sem imprimir as primeiras linhas, se quisermos
print(deslizamentos['date'].dtype)


### Convertendo a coluna de data para *datetime*
# Agora que sabemos que nossa coluna de data não está sendo reconhecida como uma data, é hora de convertê-la 
# para que seja reconhecida como uma data. Isso é chamado de "analisar datas" porque estamos pegando uma string 
# e identificando suas partes componentes.

# Podemos definir qual é o formato de nossas datas com um guia chamado *"strftime directive"*. Para mais 
# informações sobre diretivas de *strftime*, veja: https://strftime.org/. 

# A ideia básica é que você precisa apontar quais partes da data estão onde e qual pontuação está entre elas. 
# Existem muitas partes possíveis de uma data, mas as mais comuns são %d para dia, %m para mês, %y para um ano 
# de dois dígitos e %Y para um ano de quatro dígitos.

# Alguns exemplos:

# 17/01/07 tem o formato "%m/%d/%y"

# 17-1-2007 tem o formato "%d-%m-%Y"

# Olhando para o início da coluna de data no conjunto de dados de **deslizamentos**, podemos ver que está no 
# formato "mês/dia/ano de dois dígitos" ou seja "%m/%d/%y"...

# criando uma nova coluna, nova_data, com o processo de análise (parsing) de datas 
deslizamentos['nova_data'] = pd.to_datetime(deslizamentos['date'], format = "%m/%d/%y")


# Agora, ao fazer a verificação das primeiras linhas da nova coluna, podemos ver que o tipo de dado é 
# *datetime64*. 

# Também podemos ver que as datas foram ligeiramente reorganizadas para que se encaixem nos objetos de 
# data e hora padrão (ano-mês-dia).


# Mostrando as primeiras linhas da nova coluna de data
print(deslizamentos['nova_data'].head())

print('#'*100)

# Agora que as datas foram analisadas e corrigidas corretamente, podemos interagir com elas de maneira mais 
# efetiva.

# Eis uma questão que é comum que encontramos quando analisamos campos desse tipo de dados:

# **E se eu encontrar um erro com vários formatos de data?**

# Embora estejamos especificando o formato de data aqui, às vezes você encontrará um erro quando houver 
# vários formatos de data em uma única coluna. Se isso acontecer, você poderá utilizar o pandas para inferir 
# qual deve ser o formato de data correto. Você pode fazer isso assim:

# deslizamentos['nova_data'] = pd.to_datetime(deslizamentos['date'], infer_datetime_format=True)

# Você pode estar se perguntando... 

# **Por que então não utilizar sempre infer_datetime_format = True? ***

# Existem dois grandes motivos para evitar que o Pandas adivinhe o formato da data/hora: 

# A primeira é que o Pandas nem sempre será capaz de descobrir o formato de data correto, especialmente se 
# alguém for criativo com a entrada de dados. 

# A segunda é que é muito mais lento do que especificar o formato exato das datas.

### Selecionando apenas o dia do mês na coluna de data

# Por quê precisamos fazer todos esses ajustes nesse tipo de dados?
# Para responder a essa pergunta, vamos tentar obter informações sobre o dia do mês em que ocorreu um 
# deslizamento de terra da coluna "date" original, que possui um dtype "objeto":


# Tentando obter o dia de um mês da coluna "date" original
# dia_do_mes_deslizamentos = deslizamentos['date'].dt.day


#print(dia_do_mes_deslizamentos)


# Como pode ser observado, ao fazermos isso, um erro é gerado! 

# A parte importante a ser observada aqui é a parte no final que diz **AttributeError: Só pode usar o acessador .dt com valores semelhantes a data e hora.** 

# Estamos recebendo este erro porque a função **dt.day()** não sabe como lidar com uma coluna com o tipo de dados "objeto". Mesmo que nosso dataframe tenha datas nele, porque eles não foram analisados, não podemos interagir com eles de uma forma útil.

# Felizmente, temos uma coluna que analisamos anteriormente e que nos permite obter o dia do mês sem problemas ("nova_data"):


# Obtendo o dia de um mês da coluna "nova_data" que foi transformada para o tipo datetime
dia_do_mes_deslizamentos = deslizamentos['nova_data'].dt.day
# Mostrando os dias do mês
print(dia_do_mes_deslizamentos)

print('#'*100)

### Plotando o dia do mês - uma análise da data
# Um dos maiores perigos na análise de datas é misturar os meses e os dias. 

# A função **to_datetime()** tem mensagens de erro muito úteis, mas não custa nada verificar se os dias 
# do mês que extraímos fazem sentido.

# Para fazer isso, vamos plotar um histograma dos dias do mês. 

# Esperamos que tenha valores entre 1 e 31 e, como não há razão para supor que os deslizamentos de terra 
# sejam mais comuns em alguns dias do mês do que em outros, uma distribuição relativamente uniforme. 
# (Com uma queda em 31 porque nem todos os meses têm 31 dias.) 

# Vejamos se é esse o caso:

qtd_na = dia_do_mes_deslizamentos.isnull().sum()
total_deslizamentos = len(dia_do_mes_deslizamentos)
percentual_na = qtd_na / total_deslizamentos
print(f"Do total de {total_deslizamentos} deslizamentos, {qtd_na} estão vazios, ou seja {percentual_na:.2%} !")


print('#'*100)

# Removendo todos os NaN
dia_do_mes_deslizamentos = dia_do_mes_deslizamentos.dropna()

# Plotando os dias do mês
sns.distplot(dia_do_mes_deslizamentos, kde=False, bins=31)

plt.show()


# Sim, parece que analisamos nossas datas corretamente e este gráfico faz sentido!
