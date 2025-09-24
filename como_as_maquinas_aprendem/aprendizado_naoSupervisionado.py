"""
Aprendizado não supervisionado


No aprendizado não supervisionado, os modelos são treinados em 
um conjunto de dados que não tem rótulos ou categorias pré-definidas. 

Um exemplo prático desse tipo de aprendizado é o agrupamento de clientes 
com base em suas características, sem usar nenhuma informação prévia sobre os grupos.

Vamos considerar um exemplo onde uma empresa deseja segmentar seus clientes
com base em duas características: a idade e o valor anual gasto em suas lojas.

Dados para Exemplo

    - Idade:                     [25  ,45    ,35 ,50   ,23  ]
    - Valor Anual Gasto (em R$): [5000,10000,7500,15000,4000]

Código com scikit-learn
"""

# Importando as bibliotecas necessárias
import matplotlib.pyplot as plt  # Para gráficos

# Importando a biblioteca NumPy para manipulação de arrays
import numpy as np

# Importando a classe KMeans do pacote sklearn.cluster para realizar o agrupamento
from sklearn.cluster import KMeans

# Criando um array de idades dos clientes como exemplo de dados
# O array contém idades como 25, 45, 35, 50 e 23 anos.
idades = np.array([25, 45, 35, 50, 23])

# Criando um array de gastos anuais dos clientes como exemplo de dados
# O array contém gastos anuais como 5000, 10000, 7500, 15000 e 4000 reais.
gastos_anuais = np.array([5000, 10000, 7500, 15000, 4000])

# Combinando os dois arrays em uma matriz, onde cada linha representa um cliente
# A primeira coluna contém idades e a segunda contém gastos anuais.
dados_clientes = np.column_stack((idades, gastos_anuais))

# Inicializando o modelo KMeans com 2 grupos (clusters)
# O objetivo é agrupar os dados em 2 grupos com base em suas características
modelo_kmeans = KMeans(n_clusters=2)


# Treinando o modelo KMeans com os dados dos clientes
# O modelo tentará encontrar os centros dos grupos que 
# minimizam a soma das distâncias quadradas entre os pontos e os centros dos grupos
modelo_kmeans.fit(dados_clientes)

# Obtendo os rótulos dos grupos para cada ponto de dados
# Os rótulos indicam a qual grupo cada ponto (cliente) pertence
grupos_formados = modelo_kmeans.labels_

# Criando rótulos para os pontos que serão exibidos no gráfico
# Cada ponto será rotulado como "Cliente 1", "Cliente 2", etc., com 
# base em sua posição no array original
rotulos_clientes = [f"Cliente {i+1}" for i in range(len(idades))]


# Inicializando uma nova figura para o gráfico com um tamanho específico
# O tamanho da figura será 10x6 polegadas
plt.figure(figsize=(10, 6))

# Criando um gráfico de dispersão (scatter plot) para visualizar os grupos
# - idades: são as coordenadas x dos pontos
# - gastos_anuais: são as coordenadas y dos pontos
# - c=grupos_formados: cores os pontos com base nos grupos aos quais pertencem
# - cmap='viridis': usa o mapa de cores 'viridis' para representar os diferentes grupos
# - s=100: define o tamanho dos marcadores como 100
# - edgecolors='k': define a cor da borda dos marcadores como preto ('k')
pontos_grafico = plt.scatter(idades, gastos_anuais, c=grupos_formados, cmap='viridis', s=100, edgecolors='k')

# Definindo o rótulo do eixo X como 'Idade'
plt.xlabel('Idade')

# Definindo o rótulo do eixo Y como 'Gasto Anual (R$)'
plt.ylabel('Gasto Anual (R$)')

# Definindo o título do gráfico como 'Grupos de Clientes'
plt.title('Grupos de Clientes')


# Adicionando rótulos aos pontos no gráfico
# O loop 'for' percorre cada rótulo e sua posição na lista 'rotulos_clientes'
for i, rotulo in enumerate(rotulos_clientes):
    
    # plt.annotate é usado para adicionar anotações (neste caso, rótulos) aos pontos
    # - rotulo: o texto que será exibido
    # - (idades[i], gastos_anuais[i]): as coordenadas x e y do ponto onde o rótulo será colocado
    # - textcoords="offset points": especifica que o deslocamento xytext será aplicado em pontos a partir da coordenada xy
    # - xytext=(0,10): move o rótulo 10 pontos acima da coordenada y do ponto
    # - ha='center': alinha horizontalmente o rótulo ao centro
    plt.annotate(rotulo, (idades[i], gastos_anuais[i]), textcoords="offset points", xytext=(0,10), ha='center')
    

# Adicionando legenda para os grupos
# plt.legend cria uma legenda para o gráfico
# - *pontos_grafico.legend_elements(): extrai elementos da legenda do gráfico de dispersão
# - title="Grupos": define o título da legenda como "Grupos"
legenda = plt.legend(*pontos_grafico.legend_elements(), title="Grupos")


# Exibindo o gráfico
plt.show()


"""
Neste exemplo, usamos o algoritmo K-means do scikit-learn para 
criar 2 grupos (ou clusters) de clientes. O algoritmo agrupa os clientes
de forma que a soma das distâncias quadradas entre os pontos de dados e o
centro do cluster seja minimizada.

Os clientes nos diferentes clusters podem ser direcionados para diferentes
estratégias de marketing. Por exemplo, o primeiro grupo (cluster 0) pode
ser jovens que gastam menos, e o segundo grupo (cluster 1) pode ser pessoas
mais velhas que gastam mais.

Note que este é um exemplo simplificado e, na prática, você teria um conjunto
de dados muito maior e possivelmente mais características para considerar.


- Idade:                     [25  ,45    ,35 ,50   ,23  ]
    - Valor Anual Gasto (em R$): [5000,10000,7500,15000,4000]
"""
print()

