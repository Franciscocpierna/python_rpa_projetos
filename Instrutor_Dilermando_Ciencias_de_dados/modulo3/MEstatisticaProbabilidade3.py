## Noções de Matemática - Estatística e Probabilidade - Parte 3

## 3. Medidas de Tendência Central

# As medidas de tendência central são estatísticas que representam o centro ou a localização dos dados
#  em um conjunto. Elas ajudam a resumir e descrever a distribuição dos dados. Algumas das medidas 
# de tendência central mais comumente usadas são: média, mediana e moda.

# **3.1 Média**

# A média é calculada somando todos os valores do conjunto de dados e dividindo pelo número total de valores. 
# A média é sensível a valores extremos (outliers).

#Exemplo de criação de um conjunto de dados quantitativos contínuos utilizando a biblioteca NumPy:

import numpy as np

# Criação de um conjunto de dados de altura
alturas = np.array([165, 170, 155, 180, 160])

print(alturas)

#Cálculo da média
media = np.mean(alturas)
print(f"Média das alturas é {media}")

# Dados de exemplo (idade de uma amostra)
idade = np.array([25, 30, 35, 40, 45, 50, 63])

# Cálculo da média
media = np.mean(idade)
print("A média das idades é:", media)


# **3.2 Mediana**

# A mediana é o valor que separa a metade inferior e a metade superior de um conjunto de dados ordenados.
#  A mediana não é afetada por valores extremos (outliers). A forma de cálculo é ordenar todos os elementos.
#  Se for uma quantidade impar,
#  a mediana é o valor central. Se for uma quantidade par, a mediana é a média dos dois 
# valores centrais.

# Exemplos:
# ![title](imagens/mediana.jpg)

import numpy as np

# Dados de exemplo (idade de uma amostra)
idade = np.array([25, 30, 35, 40, 45, 50, 63])

# Cálculo da mediana
mediana = np.median(idade)
print("A mediana das idades é:", mediana)


# **3.3 Moda**

# A moda é o valor que ocorre com maior frequência em um conjunto de dados. Pode haver mais de uma moda 
# (dados bimodais ou multimodais) ou nenhum valor com frequência máxima (dados amodais).

# Exemplo: considere a seguinte amostra: [ 1,4,4,5,6,7,7,7 ]

# A moda desta amostra é: 7


from scipy import stats

# Dados de exemplo (números em uma amostra)
numeros = [2, 5, 5, 6, 6, 6, 7, 8]

# Cálculo da moda
moda = stats.mode(numeros, keepdims=False)
print("A moda dos números é:", moda.mode)

# É importante entender o contexto dos dados e considerar as características da distribuição ao escolher 
# a medida de tendência central mais adequada para um conjunto de dados específico.

# Uma forma de perceber e entender melhor os conceitos acima, seria por meio da visualização 
# desses conceitos em um gráfico.

# Para criar um gráfico que mostre visualmente as três medidas de 
# tendência central (média, mediana e moda), você pode utilizar a biblioteca *matplotlib*. 

# A seguir, um código que cria um gráfico de barras para representar as três medidas usando os 
# dados de exemplo fornecidos.


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dados de exemplo (idade de uma amostra)
idade = np.array([25, 30, 35, 40, 45, 50, 63])

# Cálculo da média, mediana e moda
media = np.mean(idade)
mediana = np.median(idade)
moda = stats.mode(idade, keepdims=True).mode[0]

# Criar um gráfico de barras para visualizar as medidas de tendência central
plt.bar(['Média', 'Mediana', 'Moda'], [media, mediana, moda])
plt.xlabel('Medida de Tendência Central')
plt.ylabel('Valor')
plt.title('Média, Mediana e Moda')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dados de exemplo (idade de uma amostra)
idade = np.array([25, 30, 35, 40, 45, 50, 63])

# Cálculo da média, mediana e moda
media = np.mean(idade)
mediana = np.median(idade)
moda = stats.mode(idade, keepdims=True).mode[0]

# Criar um gráfico de dispersão para visualizar os pontos de dados
plt.scatter(np.arange(len(idade)), idade, label='Pontos de Dados')
plt.axhline(y=media, color='r', linestyle='--', label='Média')
plt.axhline(y=mediana, color='g', linestyle='--', label='Mediana')
plt.axhline(y=moda, color='b', linestyle='--', label='Moda')

# Adicionar legendas e título
plt.xlabel('Índice do Ponto de Dados')
plt.ylabel('Idade')
plt.title('Gráfico de Dispersão com Tendências Centrais')
plt.legend()

# Mostrar o gráfico
plt.grid(True)
plt.show()



