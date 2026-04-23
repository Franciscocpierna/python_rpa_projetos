# Obtendo Dados - Parte 2

# Nesta parte específica do curso, vamos ver como podemos fazer a importação de dados.

# No mundo real, os dados estão dispersos e em vários formatos: **txt, csv, excel, json, zip, etc.**

# Nesta sessão, vamos ver como podemos fazer a importação de dados de diversos formatos para o *Pandas*.

### Importando Dados no formato Texto (.txt)

# A forma mais simples de dados que vamos trabalhar são os **arquivos .txt**. Para importar dados de texto, 
# precisamos de um conjunto de dados neste formato. 

# A título de exemplo, vamos importar um conjunto de dados do mundo real. Vamos utilizar os dados do índice 
# de preços ao consumidor obtidos no site do Departamento do Trabalho dos EUA. Você pode baixar os dados 
# clicando no seguinte link: [Departamento do Trabalho dos EUA: indice de preço ao consumidor]
# (https://download.bls.gov/pub/time.series/ap/ap.data.0.Current). 

# O arquivo estará disponível como recurso dessa aula (*dados_txt.txt*)

# Importando o Pandas
import pandas as pd
# verificando a versão
print(pd.__version__)

# Importando os dados do arquivo txt.
dados = pd.read_table('dataset/dados_txt.txt')
print(dados.head())

# verificando o tipo de dados importado
print(type(dados))

# Podemos, por exemplo, fazer a importação apenas de determinadas colunas.
dados = pd.read_table('dataset/dados_txt.txt', usecols = ['year', 'period'])
print(dados.head())

### Importando Dados no formato CSV (Valores Separados por Vírgula)

# CSV ou valores separados por vírgula é um dos formatos mais utilizados para salvar dados. Você verá que a 
# maioria dos conjuntos de dados disponíveis publicamente para análise/aprendizado de máquina está no 
# formato .csv. 

# No próximo exemplo, vamos utilizar dados de crime para analisar os incidentes criminais ocorridos na cidade 
# de Chicago. 

# Você pode baixar esses dados clicando no link a seguir: [Incidentes Criminais ocorridos na cidade de 
# Chicago-USA de 2001 até a presente data]
# (https://data.cityofchicago.org/api/views/ijzp-q8t2/rows.csv?accessType=DOWNLOAD). O arquivo estará disponível
# como recurso dessa aula (dados_csv.csv)

#     Importando o arquivo CSV utilizando a função read_csv() comentei o tamanho do arquivo da erro no git
#     dados = pd.read_csv('dataset/dados_csv.csv')
#     print(dados.head())

#print(dados.shape)
### Importando Dados do Excel

# Arquivos em Excel é um outro formato muito utilizado na área de Ciência de Dados. Você pode usar a função
# pandas **read_excel()** com seu argumento sheet_name para ler os dados de uma planilha específica de dados 
# do Excel. 

# Para demostrar a importação de dados no formato Excel, vamos utilizar uma planilha **Superstore Excel** 
# com três guias - Pedidos, Devoluções, Pessoas, que você pode baixar clicando no seguinte link:
# [Planilha Superstore - Excel]
# (https://community.tableau.com/s/question/0D54T00000CWeX8SAL/sample-superstore-sales-excelxls). 

# Essa planilha estará disponível como recurso dessa aula (dados_excel.xls).
# pip install xlrd==2.0.1
# Importando o arquivo EXCEL utilizando a função read_excel()
dados = pd.read_excel('dataset/dados_excel.xls')
print(dados.head())

# Convertendo o DataFrame acima para JSON e salvando em um arquivo 
dados.to_json("dataset/dados_json.json", orient='columns')
### Importando Dados em JSON (Java Script Notation)
# O formato JSON é a forma preferida de troca de dados no mundo das APIs. Para lidar com dados estruturados JSON, 
# você pode usar a função pandas **read_json()** para ler os argumentos e dados de um arquivo nesse formato.

# Para tanto, vamos utilizar os mesmos dados que utilizamos para importação de dados no formato do Excel 
# (Planilha: SuperStore), que salvamos no formato Json.

# Esse arquivo estará disponível como recurso dessa aula (dados_json.json)

# Importando o arquivo no formato JSON utilizando a função read_json()
dados = pd.read_json('dataset/dados_json.json', orient='columns')
print(dados.head())

### Importanto Dados Pickled (Serializados)
# Qualquer objeto em Python pode ser serializado para que possa ser salvo no disco. **O processo de serialização
# é conhecido como "pickle"**. Portanto, *"Pickling"* é o processo pelo qual uma hierarquia de objetos Python 
# é convertida em um fluxo de bytes. E *"Unpickling"* é a operação inversa, em que um fluxo de bytes 
# (de um arquivo binário ou objeto byte ou similar) é convertido de volta em uma hierarquia de objetos. 
# Esse processo também é conhecido como serialização ou achatamento ("flattening").

# A ideia é que esse fluxo de caracteres contenha todas as informações necessárias para reconstruir o objeto em 
# outro script Python. Quando você trabalhar com aprendizado de máquina, precisará treinar seu modelo várias 
# vezes, e a serialização ajudará você a economizar tempo de treinamento. Depois de selecionar seu modelo 
# treinado, você pode compartilhar esse modelo treinado com outras pessoas; eles não precisam perder tempo com 
# o retreinamento do modelo. Abordaremos essa parte mais tarde.

# Vamos aprender a ler um arquivo em Pickled (serializado). Para tanto, você pode utilizar a função Pandas: 
# read_pickle.
# Para tanto, vamos utilizar um arquivo serializado do Famoso DataSet Mnist (que possui imagens 28x28x1 
# de números escritos a mão). Você pode baixar esse arquivo em: [Kaggle - Mnist Pickled]
# (https://www.kaggle.com/datasets/pablotab/mnistpklgz?resource=download).



# Este arquivo arquivo estará disponível como recurso dessa aula (mnist.pkl)

# Importando um arquivo serializado (Pickled)
#   dados = pd.read_pickle('dataset/mnist.pkl')
#   print("Tipo de dados: ", type(dados))
#   for indice, digitos in enumerate(dados):
#      print(indice, ":", digitos)

### Importando dados comprimidos (ZIP)
# O formato de arquivo ZIP é um padrão comum de compactação e arquivamento. O processo de compactação 
# é utilizado para reduzir o espaço de armazenamento e também poder realizar as transferências de arquivos
#  mais rapidamente.

# Assim, como você pode descompactar um arquivo para poder ler os dados? Em linguagem Python existe um módulo 
# "zipfile" que fornece ferramentas para criar, ler, escrever, anexar e listar um arquivo ZIP. 

# Para exemplificar, descompactaremos dados de solo da região africana que você vai encontrar como recurso 
# dessa aula (africa_soil_train.zip)    

# Importanto o Módulo ZIPFILE
import zipfile as zip

dataset = "dataset/africa_soil_train.zip"
with zip.ZipFile(dataset, "r") as z:
    z.extractall()


# Neste exemplo, o arquivo extraido ficará no diretório corrente. O nome do arquivo é training.csv. 

# Uma vez extraido, basta realizar a importação de um arquivo CSV.    