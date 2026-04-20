# Introdução a Biblioteca Seaborn

# Quando se trata de visualização de dados em Python, a biblioteca Seaborn é uma ferramenta essencial
# que oferece uma abordagem simplificada e esteticamente agradável para criar gráficos informativos e
# visualmente atraentes. Desenvolvida com base no Matplotlib, a Seaborn fornece uma interface de alto nível que simplifica a criação de visualizações complexas e sofisticadas com apenas algumas linhas de código.

# ### 6.1 O que é Seaborn?

# Seaborn é uma biblioteca de visualização de dados em Python baseada no Matplotlib. Ela oferece uma 
# interface de alto nível para criação de gráficos estatísticos atrativos e informativos. Seaborn é 
# especialmente útil para explorar conjuntos de dados complexos e entender as relações entre variáveis.

# ### 6.2 Principais recursos:

# 1. **Estilo e estética melhorados**: Seaborn vem com estilos de plotagem pré-configurados que melhoram 
# significativamente a estética dos gráficos. Além disso, oferece várias paletas de cores e opções de 
# personalização para criar visualizações visualmente impressionantes.

# 2. **Facilidade de uso**: Seaborn simplifica muitos aspectos da criação de gráficos, desde a manipulação
# de dados até a personalização de gráficos. Com poucas linhas de código, é possível criar visualizações
#  complexas, como gráficos de dispersão, de barras, de boxplot, de violino, entre outros.

# 3. **Suporte a dados estatísticos**: Seaborn integra-se perfeitamente com Pandas DataFrames e oferece 
# funcionalidades para visualizar relações estatísticas entre variáveis, como gráficos de regressão, 
# mapas de calor e matrizes de correlação.

### 6.3 Como começar a usar:

# 1. **Instalação**: Seaborn geralmente é instalado automaticamente como parte da instalação do pacote 
# Anaconda. Caso contrário, você pode instalar Seaborn usando pip: `pip install seaborn`.

# Podemos também...

# Instalar uma versão específica do seaborn ( Ex: 0.13.2 )
# !pip install -q seaborn==0.13.2

# 2. **Importação**: Importe a biblioteca Seaborn em seu script Python:
#    ```python
#    import seaborn as sns
#    ```


import seaborn as sns
# Veirificando a versão...
print(sns.__version__)

# 3. **Plotagem básica**: Comece explorando seus dados com alguns dos gráficos básicos do Seaborn. Por exemplo, para criar um gráfico de dispersão simples, use:
#    ```python
#    import matplotlib.pyplot as plt
#    import seaborn as sns

#    sns.scatterplot(x='variavel_x', y='variavel_y', data=seu_dataframe)
#    plt.show()
#    ```
#    Obviamente, para esse código funcionar, temos que ter os dados de um dataframe (seu_dataframe).
   
#    Vamos ver então o Seaborn em ação!

### 6.4 Criando Gráficos com Seaborn

# Primeiramente, vamos importar não só o Seaborn, mas também uma série de outros pacotes necessários 
# para realizarmos as nossas visualizações.

# Vamos importar alguns pacotes para realizar nossas visualizações
import random
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
#O próprio Seaborn tras alguns datasets... vamos utilizar um deles para criar alguns gráficos.

# Carregando um dos datasets que dentro do próprio Seaborn
# Dataset que contem informações de gorjetas (tips) 
dados = sns.load_dataset("tips")
print(dados.head())

# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
sns.jointplot(data = dados, x = "total_bill", y = "tip", kind = 'reg')
plt.show()


# O método lmplot() cria plot com dados e modelos de regressão
sns.lmplot(data = dados, x = "total_bill", y = "tip", col = "smoker")
plt.show()


#A área azul claro mostrada no entorno da reta de regressão é conhecido como **intervalo de confiança**.
#  O intervalo de confiança geralmente é calculado para uma confiança de 95%, indicando que há uma 
# probabilidade de 95% de que os valores reais de y estejam dentro desse intervalo para um valor dado de x. 
# Em outras palavras... indica a precisão do modelo de regressão criado.

# Construindo um dataframe com Pandas
df = pd.DataFrame()

# Alimentando o Dataframe com valores aleatórios
df['idade'] = random.sample(range(20, 100), 30)
df['peso'] = random.sample(range(55, 150), 30)

print(df.shape)

print(df.head())

# lmplot
sns.lmplot(data = df, x = "idade", y = "peso", fit_reg = True)

plt.show()

# O comando `kdeplot()` é uma função do pacote Seaborn que cria um gráfico de densidade de probabilidade
# kernel (KDE, em inglês *Kernel Density Estimate*). O gráfico KDE é uma forma de visualizar a distribuição
# de uma variável contínua.

# O que a função `kdeplot()` faz:

# - **Estimativa de Densidade de Probabilidade**: O gráfico KDE estima a densidade de probabilidade de 
# uma variável contínua. Ele mostra uma curva suavizada que representa a distribuição da variável com base 
# nos dados disponíveis.

# - **Kernel**: O KDE utiliza uma função de kernel para suavizar os dados. A função kernel ajuda a criar
#  uma estimativa suave da densidade de probabilidade.

# - **Visualização**: O gráfico resultante é uma curva contínua que mostra a densidade da variável em 
# diferentes valores. A altura da curva em cada ponto indica a densidade ou frequência relativa de observações 
# nesse intervalo.

# O gráfico KDE é usado para:

# - **Visualizar Distribuições**: O gráfico KDE oferece uma visão clara da distribuição de uma variável 
# contínua, mostrando onde os dados estão mais concentrados.

# - **Comparar Distribuições**: Você pode usar o gráfico KDE para comparar as distribuições de diferentes 
# variáveis ou diferentes grupos de dados.

# - **Identificar Outliers ou Anomalias**: O gráfico pode ajudar a identificar valores atípicos ou anomalias
#  na distribuição dos dados.

# - **Explorar Dados**: O gráfico KDE é uma ferramenta útil para explorar a estrutura dos dados e compreender
#  melhor sua distribuição antes de realizar análises estatísticas mais avançadas.

# Em resumo, `kdeplot()` é um comando útil para explorar dados e compreender sua distribuição.


# kdeplot
sns.kdeplot(df.idade)
plt.show()

# kdeplot
sns.kdeplot(df.peso)
plt.show()

# A função `distplot(x)` é usada para criar um gráfico de distribuição para a variável `x`. A função `distplot()` 
# é uma combinação de um histograma e um gráfico de densidade de probabilidade (KDE) para visualizar a
# distribuição de uma variável contínua.

# Aqui está o que a função `distplot()` faz e para que ela é usada:

# - **Histograma**: A função `distplot()` pode exibir um histograma dos dados, que mostra a frequência 
# de ocorrências em diferentes intervalos (ou "bins") da variável.

# - **Gráfico de Densidade de Probabilidade (KDE)**: Além do histograma, `distplot()` também pode traçar uma 
# curva de densidade de probabilidade kernel (KDE), que é uma estimativa suavizada da distribuição da variável.

# - **Personalização**: Você pode personalizar o gráfico de distribuição usando diversos parâmetros, como `bins` 
# para definir o número de intervalos no histograma, `kde` para habilitar ou desabilitar o KDE, `hist` para 
# habilitar ou desabilitar o histograma, e outras opções de estilo.

# O gráfico de distribuição é usado para:

# - **Visualizar a distribuição**: Ele oferece uma visão clara da distribuição da variável, mostrando tanto
#  a frequência de ocorrências em intervalos específicos quanto a densidade de probabilidade suavizada.

# - **Identificar padrões**: O gráfico pode ajudar a identificar padrões na distribuição, como simetria, 
# assimetria, picos ou depressões.

# - **Comparar distribuições**: Pode ser usado para comparar a distribuição de diferentes variáveis ou 
# grupos de dados.

# - **Analisar dados**: O gráfico é útil para analisar a estrutura dos dados e compreender melhor sua 
# distribuição antes de realizar análises estatísticas mais avançadas.

# Em resumo, `distplot()` é uma ferramenta útil para explorar dados e compreender sua distribuição.

# distplot
sns.distplot(df.peso)
plt.show()

# Histograma
plt.hist(df.idade, alpha = .3)
sns.rugplot(df.idade)
# o rugplot cria as rugas no gráfico indicando onde estão as idades.

plt.show()

# A função `boxplot()` do Seaborn cria um gráfico de caixa (ou gráfico de boxplot), que é uma forma de 
# visualizar a distribuição de uma variável contínua ou de comparar distribuições entre grupos.

# #### Parâmetros

# A função `boxplot()` tem vários parâmetros que você pode usar para personalizar o gráfico:

# - **`data`**: Os dados que serão usados para criar o gráfico. Pode ser um DataFrame do Pandas ou 
# outra estrutura de dados.

# - **`x`**: A variável categórica que você deseja comparar. Especifica o eixo x para agrupar os dados.

# - **`y`**: A variável contínua que você deseja visualizar. Especifica o eixo y.

# - **`hue`**: Permite agrupar os dados por outra variável categórica adicional, diferenciando as caixas
#  por cor.

# - **`order` e `hue_order`**: Definem a ordem das categorias para `x` e `hue`.

# - **`orient`**: Especifica a orientação do gráfico, podendo ser `'v'` para vertical ou `'h'` para horizontal.

# - **`color`**: Define uma cor para o gráfico.

# - **`palette`**: Especifica a paleta de cores para diferenciar grupos de `hue`.

# - **`linewidth`**: Define a espessura das linhas nas caixas.

# - **`width`**: Controla a largura das caixas.

# - **`dodge`**: Se verdadeiro, as caixas serão deslocadas para evitar sobreposição ao usar o parâmetro `hue`.

# - **`whis`**: Controla a extensão das linhas de ligação dos valores mínimos e máximos (bigodes ou *whiskers*)
#  na plotagem.

# - **`capprops`, `boxprops`, `whiskerprops`, `flierprops`, `medianprops`**: Permitem personalizar a aparência 
# de diferentes partes do gráfico (cap, caixa, bigodes, outliers e linha mediana).

# #### Usos do Gráfico de Caixa

# - **Visualizar a Distribuição**: O boxplot fornece uma visão resumida da distribuição de uma variável,
#  mostrando o quartil inferior, a mediana, o quartil superior, e os valores mínimos e máximos.

# - **Comparar Grupos**: É útil para comparar distribuições entre diferentes grupos, identificando 
# diferenças nos valores centrais e nas variações.

# - **Identificar Outliers**: Os outliers são representados por pontos individuais fora dos bigodes, 
# o que ajuda a identificar valores atípicos na distribuição.

# - **Visualizar a Variabilidade**: O boxplot ajuda a visualizar a dispersão dos dados ao exibir o 
# intervalo interquartil (IQR).

# Em resumo, o gráfico de caixa é uma ferramenta poderosa para visualizar distribuições e comparações 
# entre grupos, fornecendo uma visão clara dos valores centrais, variações e possíveis outliers nos dados.

# Box Plot
sns.boxplot(df.idade, color = 'm')
# a linha do meio é a mediana (segundo quartil). A linha de baixo da caixa é o primeiro quartil. 
# E a linha de cima o terceiro quartil

plt.show()

# Box Plot
sns.boxplot(df.peso, color = 'y')
plt.show()

# O gráfico `violinplot()` do Seaborn cria um gráfico de violino, que é uma maneira de visualizar a 
# distribuição de uma variável contínua, semelhante ao boxplot, mas com informações adicionais sobre 
# a densidade de probabilidade.

# #### Parâmetros

# A função `violinplot()` tem vários parâmetros que você pode usar para personalizar o gráfico:

# - **`data`**: Os dados que serão usados para criar o gráfico. Pode ser um DataFrame do Pandas ou 
# outra estrutura de dados.

# - **`x`**: A variável categórica que você deseja comparar. Especifica o eixo x para agrupar os dados.

# - **`y`**: A variável contínua que você deseja visualizar. Especifica o eixo y.

# - **`hue`**: Permite agrupar os dados por outra variável categórica adicional, diferenciando os violinos
#  por cor.

# - **`order` e `hue_order`**: Definem a ordem das categorias para `x` e `hue`.

# - **`orient`**: Especifica a orientação do gráfico, podendo ser `'v'` para vertical ou `'h'` para horizontal.

# - **`bw` ou `bw_method`**: Controla o fator de suavização usado para criar a estimativa de densidade de 
# probabilidade.

# - **`cut`**: Controla a extensão dos violinos além dos valores mínimos e máximos dos dados.

# - **`scale`**: Controla o dimensionamento dos violinos. Pode ser `'width'`, `'area'`, ou `'count'`.

# - **`inner`**: Controla a exibição de estatísticas adicionais dentro do violino, como mediana e quartis. 
# Pode ser `'box'`, `'quartile'`, `'point'`, `'stick'`, ou `None`.

# - **`linewidth`**: Define a espessura das linhas dos violinos.

# - **`gridsize`**: Controla a resolução da malha para a estimativa de densidade.

# - **`split`**: Se `True`, divide o violino ao longo do eixo x para diferentes grupos de `hue`.

# #### Usos do Gráfico de Violino

# - **Visualizar a Distribuição**: O gráfico de violino oferece uma visão mais completa da distribuição 
# de uma variável, mostrando a densidade de probabilidade ao longo da variável contínua.

# - **Comparar Grupos**: O gráfico é útil para comparar distribuições entre diferentes grupos, similar 
# ao boxplot, mas com informações mais detalhadas sobre a forma da distribuição.

# - **Visualizar a Densidade**: O violino mostra a densidade de probabilidade da variável contínua, 
# indicando onde os dados estão mais concentrados.

# - **Identificar Padrões e Outliers**: O gráfico pode ajudar a identificar padrões ou valores atípicos na 
# distribuição.

# Em resumo, o gráfico de violino é útil para comparar distribuições entre grupos e visualizar a forma e 
# a variabilidade dos dados.


# Violin Plot
sns.violinplot(df.idade, color = 'g')
plt.show()

# Violin Plot
sns.violinplot(df.peso, color = 'cyan')
plt.show()

# A função `clustermap()` do Seaborn cria um mapa de clusters (ou mapa de calor com agrupamento de clusters), 
# que é uma visualização que combina um mapa de calor com dendrogramas (diagramas na forma de árvores com 
# agrupamento hierárquico) para visualizar a similaridade entre variáveis ou observações e identificar
# agrupamentos de dados.

# #### Parâmetros

# - **`data`**: Os dados que serão usados para criar o mapa de clusters. Pode ser um DataFrame do Pandas, 
# uma matriz NumPy ou outra estrutura de dados bidimensional.

# - **`metric`**: A métrica usada para calcular a distância entre as observações ou variáveis. Pode ser uma 
# string ou uma função que especifica a métrica de distância a ser usada.

# - **`method`**: O método de agrupamento hierárquico a ser usado. Pode ser `'single'`, `'complete'`, `'average'`
# , `'ward'`, entre outros.

# - **`z_score`**: Controla a padronização dos dados. Pode ser `'none'`, `'rows'` ou `'cols'`.

# - **`cmap`**: A paleta de cores usada para o mapa de calor. Pode ser uma string com o nome da paleta ou um 
# objeto de paleta de cores.

# - **`row_cluster` e `col_cluster`**: Controlam se o agrupamento deve ser realizado nas linhas e colunas, 
# respectivamente.

# - **`standard_scale`**: Controla a escala padrão dos dados. Pode ser `'none'`, `'rows'` ou `'cols'`.

# - **`linewidths`**: Define a espessura das linhas entre as células do mapa de calor.

# - **`figsize`**: Controla o tamanho da figura.

# - **`cbar`**: Controla a exibição da barra de cores.

# - **`row_colors` e `col_colors`**: Permitem adicionar cores para indicar grupos ou categorias nas linhas 
# e colunas.

# - **`dendrogram_ratio`**: Controla a proporção de espaço dedicada aos dendrogramas nas linhas e colunas.

# #### Usos do Mapa de Clusters

# - **Visualizar Similaridades**: O mapa de clusters é útil para visualizar a similaridade entre variáveis ou 
# observações com base nas métricas de distância e métodos de agrupamento.

# - **Identificar Agrupamentos**: Permite identificar agrupamentos naturais nos dados, facilitando a análise 
# de padrões.

# - **Comparar Dados**: Você pode usar o mapa de clusters para comparar diferentes partes de um conjunto de dados,
# identificando grupos de observações ou variáveis que têm comportamento semelhante.

# - **Explorar Dados**: O gráfico ajuda a explorar e compreender a estrutura dos dados, permitindo ver padrões 
# de agrupamento e tendências.

# Em resumo, o mapa de clusters é uma visualização poderosa para analisar e entender agrupamentos e 
# similaridades em um conjunto de dados. Ele combina um mapa de calor com dendrogramas para mostrar como 
# variáveis ou observações se agrupam com base em métricas de similaridade.

# Clustermap
sns.clustermap(df)
plt.show()

### 6.5 Juntando tudo... Matplotlib, Seaborn, Numpy e Pandas (gráficos estatísticos)

# Valores randômicos
np.random.seed(42)
n = 1000
pct_diabetes = 0.07

# Variáveis
flag_diabetes = np.random.rand(n) < pct_diabetes
idade = np.random.normal(40, 10, n)
altura = np.random.normal(170, 10, n)
peso = np.random.normal(70, 10, n)

# Dataframe
dados = pd.DataFrame({'altura': altura, 'peso': peso, 'flag_diabetes': flag_diabetes})

# Cria os dados para a variável flag_diabetes
dados['flag_diabetes'] = dados['flag_diabetes'].map({True: 'Tem Diabetes', False: 'Não tem Diabetes'})

print(dados.shape)

print(dados.head())
plt.show()

# Style
sns.set(style = "ticks")

# lmplot
sns.lmplot(x = 'altura', 
           y = 'peso', 
           data = dados, 
           hue = 'flag_diabetes', 
           palette = ['tab:blue', 'tab:red'], 
           height = 7)

# Labels e título
plt.xlabel('Altura (cm)')
plt.ylabel('Peso (kg)')
plt.title('Relação Entre Altura e Peso de pessoas com e sem Diabetes')

# Remove as bordas
sns.despine()

# Show
plt.show()

