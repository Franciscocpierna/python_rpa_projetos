## Noções de Matemática - Estatística e Probabilidade - Parte 4

## 4. Medidas de Dispersão

# As medidas de dispersão são estatísticas que indicam o quão dispersos ou espalhados estão os valores
#  em um conjunto de dados. Elas fornecem informações sobre a variabilidade dos dados. Algumas das medidas 
# de dispersão mais comumente usadas são: amplitude, variância, desvio padrão e intervalo interquartil.

# **4.1 Amplitude**

# A amplitude representa a diferença entre o maior e o menor valor da série de observações.
#  Representa a medida de dispersão/variabilidade mais simples, fácil de entender e intuitiva.

# Importar as bibliotecas necessárias
import numpy as np

# Dados de exemplo (série de observações)
dados = np.array([10, 15, 20, 25, 30, 35, 40])

# Cálculo da amplitude
amplitude = np.max(dados) - np.min(dados)
print("A amplitude é:", amplitude)

# Dados de exemplo (idade de uma amostra)
idade = np.array([25, 30, 35, 40, 45, 50, 63])

# Cálculo da média
media = np.mean(idade)
print("A média das idades é:", media)

# Neste exemplo, a variável dados contém a série de observações para a qual queremos calcular a amplitude. 
# A amplitude é simplesmente a diferença entre o maior valor (obtido usando np.max) e o menor valor 
# (obtido usando np.min) da série. 


# **4.2 Variância**

# A variância mede o quão distantes os valores estão da média em um conjunto de dados. Valores maiores 
# de variância indicam maior dispersão dos dados.

# ![title](imagens/varianca.jpg).

import numpy as np

# Dados de exemplo (pontuações de um teste)
pontuacoes = np.array([80, 85, 90, 95, 100])

# Cálculo da variância
variancia = np.var(pontuacoes)
print("A variância das pontuações é:", variancia)

import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo (pontuações de um teste)
pontuacoes = np.array([80, 85, 90, 95, 100])

# Cálculo da média
media = np.mean(pontuacoes)

# Cálculo da variância
variancia = np.var(pontuacoes)

# Plotar os dados e a média
plt.scatter(np.arange(len(pontuacoes)), pontuacoes, label='Pontuações')
plt.axhline(y=media, color='r', linestyle='--', label='Média')

# Adicionar linhas para mostrar a variação em relação à média
for i, ponto in enumerate(pontuacoes):
    distancia_media = ponto - media
    plt.plot([i, i], [media, ponto], color='gray', linestyle='-', linewidth=2, alpha=0.7)
    plt.text(i + 0.1, ponto, f'{distancia_media:.2f}', color='black', fontsize=8)

# Adicionar legenda e título
plt.xlabel('Índice do Ponto de Dados')
plt.ylabel('Pontuação')
plt.title('Gráfico de Dispersão com Média e Variação')
plt.legend()

# Mostrar o gráfico
plt.grid(True)
plt.show()

print("A variância das pontuações é:", variancia)


#**4.3 Desvio Padrão**

#O desvio padrão é a raiz quadrada da variância. Ele indica o grau médio de dispersão dos dados em relação à média. 
# O desvio padrão é uma medida comumente usada, pois está na mesma unidade dos dados originais.

import numpy as np

# Dados de exemplo (pontuações de um teste)
pontuacoes = np.array([80, 85, 90, 95, 100])

# Cálculo do desvio padrão
desvio_padrao = np.std(pontuacoes)
print("O desvio padrão das pontuações é:", desvio_padrao)


# Quando os dados da população se ajustam à distribuição normal:

# •	68% dos valores estariam compreendidos no intervalo de média ±1 desvio padrão;

# •	95% dos valores estariam compreendidos no intervalo de média ± 2 desvios padrões; e

# •	99% dos valores estariam compreendidos no intervalo de média ± 3 desvios padrões.

# Uma figura que ilustra esses intervalos, seria:

# ![title](imagens/desviopadrao.jpg).

# **4.4 Intervalo Interquartil**

# Os quartis dividem os dados em quatro partes iguais, quando estes estão ordenados. O princípio é 
# o mesmo da mediana, onde primeiramente coloca-se os dados em ordem crescente.

# •	O 1º quartil (Q1) é o número que deixa 25% das observações abaixo e 75% acima.

# •	O 2º quartil (Q2) deixa 50% das observações abaixo e 50% acima. Representa também a mediana.

# •	O 3º quartil (Q3) deixa 75% das observações abaixo e 25% acima.

# Graficamente teríamos:

# ![title](imagens/quartil.jpg)

# O intervalo interquartil (IQR) é uma medida que descreve a variação dos valores em torno da mediana. 
# É calculado como a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1). O IQR é menos 
# sensível a valores extremos (outliers) em comparação com a variância e o desvio padrão.

# import numpy as np

# Dados de exemplo (idade de uma amostra)
idade = np.array([11, 16, 25, 44, 46, 55, 71, 88, 91])

# Cálculo do intervalo interquartil
Q1 = np.percentile(idade, 25)
Q3 = np.percentile(idade, 71)
IQR = Q3 - Q1
print("O intervalo interquartil das idades é:", IQR)


#O código abaixo, exibe o gráfico chamado de boxplot, ou seja, os quartis da distribuição de idades 
# do código acima.

# Criação do boxplot
plt.boxplot(idade, vert=False, showfliers=False)
plt.title("Boxplot das Idades")
plt.xlabel("Idade")
plt.ylabel("Amostra")
plt.axvline(Q1, color='r', linestyle='--', label='Q1')
plt.axvline(Q3, color='g', linestyle='--', label='Q3')
plt.axvline(Q1 - 1.5 * IQR, color='b', linestyle='--', label='Limite Inferior')
plt.axvline(Q3 + 1.5 * IQR, color='b', linestyle='--', label='Limite Superior')
plt.legend()
plt.show()

#Ao analisar a dispersão dos dados, é importante considerar o contexto do problema e escolher 
# a medida de dispersão mais apropriada para fornecer insights relevantes sobre os dados.