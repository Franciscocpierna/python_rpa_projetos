## Noções de Matemática - Estatística e Probabilidade - Parte 5

## 5. Distribuição de Probabilidade

# **5.1 Distribuição Normal**

# OBSERVE O SEGUINTE EXEMPLO:

# - Imagine que você está medindo a altura de todos os alunos de uma escola. Se você plotar um gráfico
#  com o número de alunos no eixo vertical e a altura no eixo horizontal, é provável que obtenha
#  uma curva suave e simétrica, parecida com um sino. Essa é a distribuição normal.
# - 
# Um exemplo seria a distribuição das alturas da população adulta. A maioria das pessoas tende a
#  ter uma altura média, e poucas pessoas têm alturas muito altas ou muito baixas.


# A distribuição normal, também conhecida como distribuição de Gauss ou distribuição em forma de sino,
#  é uma das distribuições de probabilidade mais importantes e amplamente utilizadas em Ciência de Dados. Ela tem as seguintes características:


# •	É simétrica e possui uma forma de sino.

# •	É definida por sua média (µ) e desvio padrão (σ).

# •	A média é o centro da distribuição e a maior concentração de valores está em torno dela.

# •	A área sob a curva é igual a 1.

# ![title](imagens/curvanormal.jpg).

# A distribuição normal é amplamente aplicada em problemas de inferência estatística, análise de dados 
# e modelagem de fenômenos naturais. Para calcular probabilidades e realizar análises com a distribuição 
# normal, utilizamos a tabela Z ou funções específicas disponíveis em bibliotecas estatísticas.

# Análises estatísticas inferenciais ditas **paramétricas** têm como premissa (pré-requisito) que os dados
#  (resíduos) sigam a distribuição normal.

# Em casos de violação dessa premissa de normalidade, recomenda-se o uso de análises 
# **não paramétricas**, pois estas não apresentam esse pré-requisito de normalidade.

# De forma geral, para cada análise paramétrica há uma não paramétrica equivalente.

# O teste U de Mann-Whitney, por exemplo, seria uma análise não paramétrica correspondente à análise 
# paramétrica teste t de Student.

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Definir os parâmetros da distribuição normal
media = 50
desvio_padrao = 10
tamanho_amostra = 1000

# Gerar dados seguindo uma distribuição normal
dados_normal = np.random.normal(loc=media, scale=desvio_padrao, size=tamanho_amostra)

# Calcular a média e o desvio padrão dos dados gerados (para conferência)
media_amostra = np.mean(dados_normal)
desvio_padrao_amostra = np.std(dados_normal)

# Criar um gráfico com histograma e curva normal
plt.figure(figsize=(8, 6))
plt.hist(dados_normal, bins=30, density=True, alpha=0.6, label='Histograma')
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
curva_normal = norm.pdf(x, media_amostra, desvio_padrao_amostra)
plt.plot(x, curva_normal, 'r', label='Distribuição Normal')
plt.xlabel('Valores')
plt.ylabel('Densidade de Probabilidade')
plt.title('Exemplo de Distribuição Normal')
plt.legend()
plt.show()

#O gráfico resultante apresenta o histograma dos dados gerados e a curva da distribuição normal com a média e o desvio
#  padrão calculados. O histograma representa a frequência dos valores na amostra, enquanto a curva normal 
# representa a distribuição teórica esperada.


# **5.2 Distribuição Binomial**

# OBSERVE O SEGUINTE EXEMPLO: 

# - Suponha que você esteja jogando uma moeda e quer saber a probabilidade de obter cara em 5 lançamentos. Cada lançamento é independente e tem apenas duas possibilidades: cara ou coroa. Esse é um exemplo de uma distribuição binomial.
# - 
# Um exemplo prático seria calcular a probabilidade de obter exatamente 3 caras em 5 lançamentos de uma moeda justa


# A distribuição binomial é uma distribuição de probabilidade discreta que modela eventos que têm dois resultados
#  possíveis: sucesso (evento de interesse) ou falha. Ela possui as seguintes características:

# - Consiste em um número fixo de ensaios independentes e idênticos.
# - Cada ensaio possui apenas dois resultados possíveis: sucesso ou falha.
# - A probabilidade de sucesso (p) é a mesma para cada ensaio.
# - O número de sucessos em um determinado número de ensaios segue a distribuição binomial.

# A distribuição binomial é frequentemente usada para modelar experimentos com resultados binários, como lançamento de
#  uma moeda, sucesso ou falha em testes, entre outros. Podemos calcular probabilidades específicas e realizar análises 
# com a distribuição binomial usando funções estatísticas disponíveis em bibliotecas como SciPy e NumPy.

import numpy as np
from numpy.random import binomial

# Geração de uma amostra de tamanho n com p=0.3 e n=1000
amostra = binomial(n=100, p=0.3, size=1000)
print("Amostra:", amostra)
#Para mostrar o gráfico da amostra gerada acima, seguindo a distribuição binomial:

import numpy as np
from numpy.random import binomial
import matplotlib.pyplot as plt

# Geração de uma amostra de tamanho n com p=0.3 e n=100
amostra = binomial(n=100, p=0.3, size=1000)

# Criar um gráfico com histograma da amostra
plt.figure(figsize=(8, 6))
plt.hist(amostra, bins=20, density=True, alpha=0.6)
plt.xlabel('Número de Sucessos')
plt.ylabel('Densidade de Probabilidade')
plt.title('Amostra Gerada com Distribuição Binomial')
plt.show()

# Neste exemplo, estamos gerando 1000 amostras, cada uma com 100 ensaios independentes, probabilidade de sucesso (p) de 0.3 e número total de ensaios (n) igual a 100. O gráfico gerado será um histograma que representa a frequência de ocorrência de diferentes números de sucessos na amostra.

# **5.3 Distribuição de Poisson**

# OBSERVE O SEGUINTE EXEMPLO: 

# - Imagine que você está monitorando o número de carros que passam por um cruzamento em uma determinada hora do dia. 
# Você pode notar que o número de carros que passa é relativamente constante em média, mas pode variar de hora em hora. 
# A distribuição de Poisson descreve esse tipo de situação, onde eventos ocorrem de forma independente a uma taxa média 
# constante ao longo do tempo ou espaço.
# - 
# Um exemplo seria o número de chamadas recebidas por um centro de atendimento em uma hora. A média de chamadas por hora 
# pode ser constante, mas o número real de chamadas em qualquer hora específica pode variar.


# A distribuição de Poisson é uma distribuição de probabilidade discreta que modela a ocorrência de eventos em um intervalo 
# de tempo fixo ou em uma região fixa do espaço. Ela possui as seguintes características:

# - Modela eventos que ocorrem de forma aleatória e independente no tempo ou no espaço.
# - A média (λ) da distribuição de Poisson é o número médio de ocorrências em um determinado intervalo.
# - A probabilidade de ocorrência de um número específico de eventos é dada pela função de massa de probabilidade de Poisson.

# A distribuição de Poisson é amplamente utilizada para modelar eventos raros, como o número de chamadas recebidas por uma central
#  telefônica em um determinado período ou o número de acidentes em uma estrada em um determinado trecho. 
# Podemos calcular probabilidades e realizar análises com a distribuição de Poisson usando funções estatísticas disponíveis 
# em bibliotecas como SciPy e NumPy.

# O código a seguir, gerar uma amostra e criar o gráfico da distribuição de Poisson:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Geração de uma amostra de tamanho 1000 seguindo a distribuição de Poisson com lambda=5
amostra = np.random.poisson(lam=5, size=1000)

# Criar um gráfico com a curva da distribuição de Poisson
plt.figure(figsize=(8, 6))
plt.hist(amostra, bins=20, density=True, alpha=0.6, label='Amostra')
x = np.arange(0, 20)
curva_poisson = poisson.pmf(x, mu=5)
plt.plot(x, curva_poisson, 'r', marker='o', linestyle='-', label='Distribuição de Poisson')
plt.xlabel('Número de Ocorrências')
plt.ylabel('Probabilidade')
plt.title('Amostra Gerada com Distribuição de Poisson')
plt.legend()
plt.show()

# Neste exemplo, estamos gerando uma amostra de 1000 números seguindo uma distribuição de Poisson com parâmetro lambda igual a 5.
# O gráfico gerado apresenta o histograma da amostra (frequência de ocorrência dos valores) e a curva da distribuição de Poisson 
# com o mesmo parâmetro lambda.
