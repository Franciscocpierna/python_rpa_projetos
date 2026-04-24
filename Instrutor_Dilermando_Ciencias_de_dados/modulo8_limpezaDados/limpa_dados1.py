## Instalando e Carregando os Pacotes


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada VScode :', python_version())

# Para atualizar um pacote, execute o comando abaixo no terminal ou prompt de comando:
# pip install -U nome_pacote

# Para instalar a versão exata de um pacote, execute o comando abaixo no terminal ou prompt de comando:
# !pip install nome_pacote==versão_desejada

# Depois de instalar ou atualizar o pacote

# Instala o pacote watermark. 
# Esse pacote é usado para gravar as versões de outros pacotes usados 
# pip install -q -U watermark


import math
import sys, os
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 100)

## Carregando os Dados


### Dataset publico: National Football League (NFL) - 2009 a 2028
# Disponível em: https://www.kaggle.com/datasets/maxhorowitz/nflplaybyplay2009to2016

# Os três arquivos utilizados neste projeto estão disponíveis em:

# NFL Play by Play - 2009 - 2017 --> 
# https://www.kaggle.com/code/rtatman/data-cleaning-challenge-handling-missing-values/input?select=NFL+Play+by+Play+2009-2016+%28v3%29.csv

# Building_Permits --> https://www.kaggle.com/code/rtatman/data-cleaning-challenge-handling-missing-values/input?select=Building_Permits.csv

# Dicionário de dados do arquivo: Building_Permits --> 
# https://www.kaggle.com/code/rtatman/data-cleaning-challenge-handling-missing-values/input?select=DataDictionaryBuildingPermit.xlsx

# Com exceção do dicinário de dados, os outros dois arquivos estão compactados (.zip). Descompacte-os e utilize os arquivos descompactados.

# Estes arquivos (prontos para uso) estarão disponíveis como recursos dessa aula.

# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "undefined"]

# Carrega os datasets 
# Jogos
dataset = pd.read_csv("dados/dataset_NFL2009-2017_v4.csv", na_values = lista_labels_valores_ausentes, low_memory=False)
# Licenças de Construção
building_permits = pd.read_csv("dados/building_permits.csv", na_values = lista_labels_valores_ausentes, low_memory=False)

### Atenção: low_memory = False
#Essa opção é necessária, pois a função read_csv() precisa ler o arquivo inteiro para só então determinar o 
# tipo de dado de cada coluna. 
# Como o arquivo de dados da NFL é muito grande, ocorre um erro, se não o fizermos dessa forma. 
# Isso faz com que o Pandas não determine automaticamente os tipos de dados. Você pode ver que isso é verdade, 
# ao buscar as informações do datasetm como mostrado no próximo comando: 

print(dataset.info())

# Vamos dar uma olhada nos dados. Nós já fizemos várias vezes com o método head(). Vamos utilizar o método 
# sample, para variar.
# Com ele, temos que informar a quantidade de amostra que queremos.
print(dataset.sample(6))


print(dataset.shape)

# Os dados são exibidos em formato tabular com algumas colunas com valores NaN.
# Esses valores são chamados de valores ausentes (Not a Number).

# Vamos aplicar a mesma função no dataframe **building_permits** conforme mostrado a seguir



print(f'building_permits.sample(6) = {building_permits.sample(6)}')

# Como pode ser observado, em ambos os casos existem valores nulos (NaN).

# Depois de ler os dados, descobrimos que ambos os conjuntos de dados têm valores ausentes. 

# Nosso próximo passo será calcular o número de valores ausentes que temos em cada coluna. 

# Para contar os valores nulos, o Pandas têm a função **isnull()**. Como o dataset principal 
# possui 102 colunas, analisaremos as primeiras dez colunas contendo valores ausentes.

contagem_valores_ausentes = dataset.isnull().sum()
contagem_valores_ausentes[0:20]
print('#'*100)
print(contagem_valores_ausentes) 

# Cada nome de coluna e o número associado indicam o número de valores ausentes – isso parece muito! 

# Não podemos ignorar um número tão alto de valores ausentes. Pode ser útil ver qual porcentagem dos
# valores em nosso conjunto de dados estava faltando para nos dar uma noção melhor da escala desse problema. 

# Para este cálculo de porcentagem, usaremos a combinação das funções **prod()** do Numpy e **shape** do Pandas, 
# conforme mostrado a seguir:

# Calculando os totais de celulas e de celulas com valores ausentes (total_nulos)
total_celulas = np.prod(dataset.shape)
total_nulos = contagem_valores_ausentes.sum()
# Calculando o percentual de dados ausentes
print(f"Percentual de Dados ausentes: {(total_nulos/total_celulas):.2%}")

# Isso é incrível, quase um quarto das células neste conjunto de dados estão vazios! 

# Agora é sua vez de aplicar as mesmas etapas no conjunto de dados building_permits e 
# verificar a porcentagem de valores ausentes.

contagem_valores_ausentes2 = building_permits.isnull().sum()
contagem_valores_ausentes2[0:20]

print(f'contagem_valores_ausentes2 = {contagem_valores_ausentes2}')

# Calculando os totais de celulas e de celulas com valores ausentes (total_nulos)
total_celulas2 = np.prod(building_permits.shape)
total_nulos2 = contagem_valores_ausentes2.sum()
# Calculando o percentual de dados ausentes
print(f"Percentual de Dados ausentes: {(total_nulos2/total_celulas2):.2%}")

# Em seguida, examinaremos mais de perto algumas das colunas com valores ausentes e tentaremos descobrir o 
# que pode estar acontecendo com elas. 

# Esse processo na ciência de dados significa observar atentamente seus dados e tentar descobrir por que são 
# do jeito que são e como isso afetará sua análise. 

# Para lidar com valores ausentes, você precisará usar sua intuição para descobrir por que o valor está desta
# forma. Recomendamos que você vá até a fonte dos dados e verifique o que pode ter ocorrido. Só use a intuição quando não tiver acesso a fonte dos dados. Lembre-se... é ciência de dados e não achismo de dados.

# Para ajudar a descobrir isso, a próxima pergunta que um cientista de dados deve se fazer - *esse valor 
# está faltando porque não foi registrado ou porque não existe?*

# No primeiro caso, se falta um valor porque não existe (por exemplo a altura do filho mais velho de alguém que
# não tem filhos), então não faz sentido tentar adivinhar qual pode ser esse valor. Para esses casos, você 
# provavelmente vai ter que excluir tais registros.

# No segundo caso, se um valor estiver faltando porque não foi registrado, você pode tentar adivinhar qual 
# valor poderia ter sido registrado com base nos outros valores nessa coluna e linha. Isso é chamado de 
# imputação de dados, o que veremos mais a frente.

# Em nosso conjunto de dados nfl_data, se você verificar a coluna *TimeSecs*, há um total de 224 valores 
# ausentes porque não foram registrados. Portanto, faria sentido tentarmos adivinhar o que deveriam ser, 
# em vez de apenas deixá-los como NA ou NaN ou simplesmente excluirmos. Por outro lado, existem outros campos,
# como *PenalizedTeam*, que também têm muitos campos ausentes. Nesse caso, porém, falta o campo porque se não houve pênalti, não faz sentido dizer qual time foi penalizado. Para esta coluna, faria mais sentido deixá-la vazia ou adicionar um terceiro valor como "nenhum" e usá-lo para substituir os NA.

# Até agora você deve ter entendido que ler e entender seus dados pode ser um processo tedioso. 

# Imagine fazer uma análise de dados tão cuidadosamente quanto possível, em que você precisa examinar 
# cada coluna individualmente até descobrir a melhor estratégia para preencher os valores ausentes. 

# Agora é sua vez de examinar as colunas *street_number_suffix* e *zipcode* (o sufixo do número da rua e o código postal) do dataset building_permits com uma abordagem semelhante. Ambos contêm valores ausentes. Qual deles está faltando? Porque não existe? Quais estão faltando porque não foram gravados?


# ## Eliminar (Drop) valores ausentes


# Se você estiver com pressa ou não tiver um motivo para descobrir por que seus valores estão ausentes, 
# uma opção é simplesmente remover quaisquer linhas ou colunas que contenham valores ausentes. Mas veja... 
# o impacto será muito grande se decidir fazer isso... Não é recomendado.

# ### Observação: 
# *Geralmente essa abordagem não é recomendada para projetos importantes! 
# Vale a pena dedicar um tempo para examinar seus dados e realmente examinar todas as colunas com valores 
# ausentes, uma a uma, para realmente conhecer seu conjunto de dados*

# Se você tem certeza de que deseja descartar linhas com valores ausentes, o pandas tem uma função útil, 
# **dropna()** para ajudá-lo a fazer isso. Vamos experimentá-lo em nosso conjunto de dados da NFL!

# ### Atenção:
# Se utilizar o comando: **dataset.dropna()** ele removerá todas as linhas que contém valores ausentes. 
# Neste caso especificamente, resultará em um dataset vazio, pois todas a linhas possuem ao menos um valor 
# ausente.
# Assim, é mais interessante, indicarmos que sejam apagados apenas as colunas que possuem dados ausentes. 
# Isso é possível, passando um parâmetro para esta função, indicando o eixo: no caso axis="columns".

# Vamos salvar esse novo dataset resultante em uma outra variável, para podermos fazer a comparação...
print('#'*100)
dataset_semNA = dataset.dropna(axis='columns')
print(dataset_semNA.head())

print('#'*100)
# Fazendo a comparação entre os datasets
print(f"Colunas no dataset original {dataset.shape[1]}")
print(f"Colunas no dataset sem NA   {dataset_semNA.shape[1]}")

# Neste ponto, pode-se verificar que perdemos muitas informações do nosso dataset original.
# Todavia, temos um dataset agora sem valores ausentes!!

# ## Preenchendo valores ausentes automaticamente
# Outra opção é tentar preencher os valores que faltam. 
# Para fins didáticos, estou recortando apenas uma parte do dataset original, para que nosso processo fique mais elucidativo.

# Obtendo uma pequena parte do dataset original
print('#'*100)
subconjuntoNFL = dataset.loc[:, "EPA":"Season"].head()
print(subconjuntoNFL)

# Podemos usar a função **fillna()** do Panda para preencher os valores ausentes em um dataframe para nós. 
# Uma opção que temos é especificar o que queremos que os valores *NaN* sejam substituídos. 
# Vamos fazer a substituição de todos os valores NaN por 0 (zero).

print('#'*100)
# substituindo todos os valores NaN por 0
print(subconjuntoNFL.fillna(0))

# Poderiamos também, ser um pouco mais precisos e substituir os valores ausentes por qualquer valor que vier 
# diretamente depois dele na mesma coluna. (Isso faz muito sentido para conjuntos de dados em que as observações
# têm algum tipo de ordem lógica.)
# preenchendo os valores ausentes com os valores que vem logo a seguir dos NaN

# bfill(axis=0): Este método preenche valores ausentes utilizando o preenchimento para trás (backward fill). 
# Isso significa que, para cada célula que tem um valor ausente (NaN), ela será preenchida com o valor da célula 
# imediatamente posterior (considerando o eixo 0, ou seja, as linhas). 
# Se uma célula não tiver um valor posterior, ela permanecerá como NaN.
# fillna(0): Após a aplicação do bfill, o método fillna é chamado para preencher todos os valores ausentes 
# restantes com zero (0). Assim, se ainda houver células com valores ausentes após o preenchimento para trás, 
# essas células serão substituídas pelo valor zero.
print('#'*100)
print(subconjuntoNFL.bfill(axis=0).fillna(0))

print('#'*100)

# Salvando os dados
subconjuntoNFL.to_csv('dados/dataset_NFL_limpo.csv')









