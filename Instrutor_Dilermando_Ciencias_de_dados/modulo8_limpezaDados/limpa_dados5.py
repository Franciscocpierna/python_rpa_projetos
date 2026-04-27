
## <font color='green'>Projeto 5 - Limpando Dados Inconsistentes</font>
## <font color='green'>Instalando os Pacotes e Carregando os Dados</font>
#pip install -q -U fuzzywuzzy



# Importação dos módulos básicos
import numpy as np
import pandas as pd
# Módulo muito útil para Codificação de Caracteres
# módulo para ignorar mensagens de alerta
import warnings
warnings.filterwarnings('ignore')
import chardet
# Módulo muito útil para Buscar Texto por Aproximação
import fuzzywuzzy
from fuzzywuzzy import process 
# módulo para ignorar mensagens de alerta
np.random.seed(0)

## Carregando os Dados
### Dataset público: *Pakistan Suicide Bombing Attacks*

# Ataques suicidas com bombas no Paquistão (1995-2016)

# O atentado suicida é um método operacional no qual o próprio ato do ataque depende da morte do perpetrador. Embora apenas 3% de todos 
# os ataques terroristas em todo o mundo possam ser classificados como ataques suicidas, eles representam 48% das vítimas. Explosões e
# atentados suicidas tornaram-se o *modus operandi* de organizações terroristas em todo o mundo. O mundo está cheio de explosivos indesejados, 
# bombardeios brutais, acidentes e conflitos violentos, e é necessário entender o impacto desses atos no ambiente, no meio ambiente e, 
# principalmente, nos seres humanos. 

# De 1980 a 2001 (excluindo 11 de setembro de 2001), o número médio de mortes por incidente em ataques suicidas foi de 13. Esse número está 
# muito acima da média de menos de uma morte por incidente em todos os tipos de ataques terroristas no mesmo período. Os homens-bomba, ao 
# contrário de qualquer outro dispositivo ou meio de destruição, podem pensar e, portanto, detonar a carga em um local ideal com tempo perfeito para causar o máximo de carnificina e destruição. Os homens-bomba são adaptáveis e podem mudar de alvo rapidamente 
# se forem forçados por riscos de segurança ou pela disponibilidade de alvos melhores. Os ataques suicidas são relativamente baratos para 
# financiar e tecnologicamente primitivos, pois os dispositivos podem ser facilmente construídos.

# O mundo já viu mais de 3.600 ataques suicidas em mais de 40 países desde 1982. Os atentados suicidas causaram 
# estragos no Paquistão na última 
# década. De apenas alguns ataques antes de 2000, continuou aumentando após a Operação Liberdade Duradoura dos EUA
# no Afeganistão, matando 
# promiscuamente centenas de pessoas a cada ano, elevando-se como uma das ameaças de segurança mais proeminentes 
# que todos os paquistaneses 
# enfrentam hoje. O dilema dos atentados suicidas no Paquistão matou 6.982 civis de mãos limpas e feriu outros 
# 17.624 em um total de 475 
# ataques desde 1995. Mais de 94% desses ataques ocorreram após o ano de 2006. De 2007 a 2013, o país testemunhou 
# uma explosão dos 
# suicídios... que foi de um a cada 6 dias em 2007, aumentando para um a cada 4 dias em 2013. Contando os mortos 
# e feridos, cada ataque 
# vitimou 48 pessoas no Paquistão.

# A Contagem de Corpos do Paquistão (www.PakistanBodyCount.org) é a contagem mais antiga e precisa de 
# homens-bomba no Paquistão. O banco de 
# dados fornecido (PakistanSuicideAttacks.CSV) foi preenchido usando a maioria dos dados do Pakistan 
# Body Count e ampliando-o por meio de 
# pesquisas em jornais de código aberto, relatórios da mídia, análises e contatos pessoais na mídia 
# e agências de aplicação da lei. No dataset existe uma contagem das pessoas mortas e feridas em ataques 
# suicidas, incluindo aquelas que morreram posteriormente em hospitais ou residências devido a ferimentos 
# causados ou agravados por esses ataques (ferimentos de segunda e terceira explosão), tornando-a a fonte 
# mais autêntica de ataques suicidas dados relacionados nesta região.

# Link para o Dataset: 
# https://www.kaggle.com/code/rtatman/data-cleaning-challenge-inconsistent-data-entry/input?select=PakistanSuicideAttacks+Ver+11+%2830-November-2017%29.csv
# Fonte: Kaggle.com

# Este arquivo estará disponível como recurso dessa aula.

# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "undefined"]
# Tentando carregar o dataset com codificação diferente de UTF-8
# dataset = pd.read_csv("dados/PakistanSuicideAttacks.csv", na_values = lista_labels_valores_ausentes)
# print(dataset) gerou erro


# Observe que obtemos o mesmo *UnicodeDecodeError*. Como já sabemos, isso indica que o arquivo deve estar 
# em um outro padrão de codificação, diferente do UTF-8.

# Vamos usar o **módulo chardet** para tentar descobrir automaticamente qual é a codificação correta. 

# Olhando os primeiros 100 mil bytes para tentar determinar a codificação
with open("dados/PakistanSuicideAttacks.csv", 'rb') as dados:
    resultado = chardet.detect(dados.read(100000))

# Verificando qual é a codificação de caracteres que foi determinada pelo método detect
print(resultado)

# Como pode ser observado, o grau de confiança que o método detect do pacote chardet retornou é de 73% que 
# seja a codificação "Windows-1252", observando os primeiros 100 mil bytes.

# Portanto, se abrirmos o arquivo agora com essa codificação, teremos uma maior garantia que dê certo. 
# Vamos ver:
# Tentando carregar o dataset com codificação diferente de UTF-8
dataset = pd.read_csv("dados/PakistanSuicideAttacks.csv", na_values = lista_labels_valores_ausentes, encoding='Windows-1252')
print(dataset)
print('#'*100)

# Agora sim!!  Parece que chardet estava certo! 

# Vamos dar uma olhada nos dados...

print(dataset.info())

print('#'*100)

print(dataset.head())

print(dataset.shape)
print('#'*100)

contagem_valores_ausentes = dataset.isnull().sum()
contagem_valores_ausentes[0:20]

print(contagem_valores_ausentes)
print('#'*100)
# Calculando os totais de celulas e de celulas com valores ausentes (total_nulos) 
total_celulas = np.prod(dataset.shape)
total_nulos = contagem_valores_ausentes.sum()
# Calculando o percentual de dados ausentes no dataset
print(f"Percentual de Dados ausentes no dataset: {(total_nulos/total_celulas):.2%}")

## Pré-processamento preliminar

# Ao analisarmos os dados, podemos observar algumas inconsistências no processo de digitação. Especificamente no 
# campo "City" (cidade). Vamos então limpar essa coluna para garantir que não haja inconsistências de entrada de 
# dados nela. 

# Poderíamos examinar e verificar cada linha manualmente, é claro, e corrigir manualmente as inconsistências 
# quando as encontrarmos. 

# Mas existe uma maneira mais eficiente de fazer isso!


print('#'*100)
# Obtendo dos os valores únicos da coluna 'City' 
cidades = dataset['City'].unique()

# Vamos agora, ordenar esses valores alfabeticamente e então vamos ver o resultado
cidades.sort()
print(cidades)

# Apenas olhando para isso, posso ver alguns problemas devido à entrada inconsistente de dados: 'ATTOCK' e 
# 'Attock ' ou 'Lahore' e 'Lahore ', ou 'Lakki Marwat' e 'Lakki marwat', são alguns exemplos.

# A primeira coisa que vamos fazer é colocar tudo em letras minúsculas 
# (posso mudar de volta no final, se quiser) e remover todos os espaços em branco no início e no final das 
# células. 

# Inconsistências em letras maiúsculas e espaços em branco à direita são muito comuns em dados de texto e 
# você pode corrigir cerca de 80% das inconsistências de entrada de dados de texto fazendo isso.
print('#'*100)
# convertendo os dados para letras Minusculas
dataset['City'] = dataset['City'].str.lower()
# removendo os espaços em branco no início e no final dos nomes.
dataset['City'] = dataset['City'].str.strip()


# Dando uma nova olhada na coluna 'City'...
# Obtendo dos os valores únicos da coluna 'City' 
cidades = dataset['City'].unique()

# Vamos agora, ordenar esses valores alfabeticamente e então vamos ver o resultado
cidades.sort()
print(cidades)

#Veja que já melhorou bem!!   Agora vamos abordar inconsistências mais difíceis...

## Correspondência difusa (Fuzzy matching) para corrigir entradas de dados inconsistentes


# Vamos dar uma olhada na coluna da cidade após o processo executado acima e ver se há mais alguma 
# limpeza de dados que precisamos fazer.

# Parece que ainda existem algumas inconsistências: 'd. i khan' e 'd.i khan' provavelmente devem ser iguais. 
# (Pesquisei e 'd.g khan' é uma outra cidade, então não devemos combiná-los.)

# Vou usar o pacote fuzzywuzzy para ajudar a identificar quais strings estão mais próximas umas das outras. 

# Esse conjunto de dados é pequeno o suficiente para que possamos corrigir os erros manualmente, mas essa 
# abordagem não é a mais produtiva. (Você gostaria de corrigir mil erros manualmente? Que tal dez mil? 
# Automatizar as coisas o mais cedo possível geralmente é uma boa ideia. Além disso, é divertido!)

# **Correspondência difusa (Fuzzy Matching)**: o processo de localizar automaticamente sequências de texto 
# muito semelhantes à sequência de destino. Em geral, uma string é considerada "mais próxima" de outra 
# quanto menos caracteres você precisar alterar se estiver transformando uma string em outra. 

# Portanto, "apple" e "snapple" são duas mudanças um do outro (adicione "s" e "n") enquanto "in" e "on" e 
# uma mudança de distância (troque "i" por "o"). Você nem sempre poderá confiar 100% na correspondência 
# difusa, mas geralmente acabará economizando pelo menos um pouco de tempo.

#Fuzzywuzzy retorna uma proporção, dada duas strings. Quanto mais próxima a proporção estiver de 100, 
# menor será a distância de edição entre as duas strings. Aqui, vamos pegar as dez strings de nossa 
# lista de cidades que têm a distância mais próxima de "d.i khan".

print('#'*100)
# Obtendo as 10 correspondencias mais próximas de "d.i khan"
corr = fuzzywuzzy.process.extract("d.i khan", cidades, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

# Vamos olhar as correspondências
corr
print(corr)

# Podemos ver que dois dos itens nas cidades estão muito próximos de "d.i khan": "d.i khan" e "d.i khan". 

# Também podemos ver que "d.g khan", que é uma outra cidade, tem uma proporção de 88. Como não queremos 
# substituir "d.g khan" por "d.i khan", vamos substituir todas as linhas em nossa coluna 'City' que têm 
# uma proporção maior que 90% com "d. i khan".

# Para fazer isso, vamos escrever uma função. 

# (É uma boa ideia escrever uma função de uso geral que você possa reutilizar se achar que precisa executar 
# uma tarefa específica mais de uma ou duas vezes. Isso evita que você tenha que copiar e colar o código 
# com muita frequência, o que economiza tempo e pode ajudar evitar erros.)

print('#'*100)


# função para substituir as linhas de uma coluna específica do dataframe fornecido como parâmetro 
# que correspondem à string fornecida acima da proporção, também fornecida como parâmetro

def substitui_corr_na_coluna(df, coluna, string_corr, min_proporcao = 90):
    # Obtenha uma lista de strings únicas
    strings = df[coluna].unique()
    
    # Obtenha as 10 correspondências mais próximas da string_corr, fornecida como entrada.
    corr = fuzzywuzzy.process.extract(string_corr, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # Obtendo apenas as 10 correspondências com proporção > 90
    maiores_corr = [corr[0] for corr in corr if corr[1] >= min_proporcao]

    # Obtendo as linhas de todos as correspondências no dataset
    linhas_corr = df[coluna].isin(maiores_corr)

    # Substituindo todas as linhas com as maiores correspondencias pela string_corr  
    df.loc[linhas_corr, coluna] = string_corr
    
    # Informando que a função terminou!
    print("Feito!")

    #Agora vamos testar a nova função!
# Usando a função para substituir todas as correspondências com "d.i khan"
substitui_corr_na_coluna(df=dataset, coluna='City', string_corr="d.i khan")

#Vamos verificar novamente os valores exclusivos em nossa coluna 'City' e garantir que arrumamos "d.i khan" 
# corretamente.

# Obtendo dos os valores únicos da coluna 'City' 
cidades = dataset['City'].unique()

# Vamos agora, ordenar esses valores alfabeticamente e então vamos ver o resultado
cidades.sort()
print(cidades)

#Excelente! Agora temos apenas "d.i khan" em nosso dataset e não precisamos alterar nada manualmente.