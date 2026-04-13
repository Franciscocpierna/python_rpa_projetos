## Noções de Matemática - Estatística e Probabilidade - Parte 7

## 7. Amostragem e Estimação

# **7.1 Amostragem Aleatória Simples**

# A amostragem aleatória simples é um método de seleção de amostras em que cada elemento da população tem a mesma chance de ser escolhido. Esse método é amplamente utilizado em Ciência de Dados para extrair informações sobre uma população maior. 

# ![title](imagens/PopAmo.jpg)

# Aqui estão os passos para realizar uma amostragem aleatória simples:

# •	**Definir a população**: Identifique a população de interesse para a sua análise.

# •	**Determinar o tamanho da amostra**: Decida o tamanho da amostra que você deseja selecionar.
#  Lembre-se de que o tamanho da amostra afeta a precisão da estimativa.

# •	**Atribuir um número a cada elemento**: Atribua um número a cada elemento da população, de 
# forma que cada elemento tenha um número exclusivo.

# •	**Selecionar elementos aleatoriamente**: Use um método aleatório 
# (por exemplo, gerador de números aleatórios) para selecionar os números 
# correspondentes aos elementos da amostra.

# •	**Coletar os dados**: Uma vez que a amostra tenha sido selecionada, colete os dados relevantes para 
# análise.

# Exemplo de amostragem aleatória simples utilizando a biblioteca Pandas:

import pandas as pd

# Dados de exemplo (idade de uma população)
populacao = pd.DataFrame({'Idade': [25, 30, 35, 40, 45, 50]})

# Amostragem aleatória simples de tamanho 3
amostra = populacao.sample(n=3)
print("Amostra:", amostra)


# **7.2 Estimativa de Parâmetros Populacionais**

# A estimativa de parâmetros populacionais envolve o uso de estatísticas amostrais para estimar características da população 
# maior. As estatísticas amostrais, como a média e o desvio padrão, são usadas como estimadores para os parâmetros populacionais 
# correspondentes. Aqui estão alguns exemplos de estimadores comuns:

# •	**Estimativa da média populacional**: A média da amostra (x̄) é usada como estimativa da média populacional (µ).

# •	**Estimativa da proporção populacional**: A proporção da amostra (p) é usada como estimativa da proporção populacional (P).

# •	**Estimativa da variância populacional**: A variância da amostra (s²) é usada como estimativa da variância populacional (σ²).

# É importante lembrar que as estimativas amostrais podem conter erros, chamados de erros de estimativa, devido à variabilidade 
# natural dos dados. Quanto maior o tamanho da amostra, menor será o erro de estimativa.

# Exemplo de estimativa de média populacional utilizando a biblioteca NumPy:



import numpy as np

# Dados de exemplo (idade de uma amostra)
amostra = np.array([25, 30, 35, 40, 45, 50])

# Estimativa da média populacional
media_estimada = np.mean(amostra)
print("A média populacional estimada é:", media_estimada)


import numpy as np
# Amostragem aleatória simples de tamanho 3
amostra1 = np.array([25, 40, 50])
media_estimada1 = np.mean(amostra1)
print("A média dessa nova amostra é: ", media_estimada1)

# Erro de estimativa
erro = media_estimada - media_estimada1
print("Erro de Estimativa: ", erro)


# **7.3 Intervalo de Confiança**

# O intervalo de confiança é uma faixa de valores dentro da qual acredita-se que um parâmetro populacional esteja 
# contido com um determinado nível de confiança. O intervalo de confiança fornece uma medida de incerteza sobre 
# a estimativa pontual do parâmetro populacional. Aqui estão os passos para calcular um intervalo de confiança:

# •	**Determinar o nível de confiança**: Escolha um nível de confiança desejado, que represente a probabilidade
# de que o intervalo contenha o verdadeiro valor do parâmetro populacional. Exemplos comuns de nível de confiança são 95% e 99%.

# •	**Calcular a estimativa pontual**: Calcule a estimativa pontual do parâmetro populacional com base na amostra.

# •	**Determinar o erro padrão**: Calcule o erro padrão da estimativa utilizando a variabilidade dos dados da amostra e o tamanho da amostra.

# •	**Calcular o intervalo de confiança**: Utilize a estimativa pontual, o erro padrão e o nível de confiança para calcular
#  o intervalo de confiança. O intervalo de confiança é tipicamente simétrico em torno da estimativa pontual.


# Exemplo de cálculo do intervalo de confiança para a média populacional utilizando a biblioteca SciPy:

from scipy import stats

# Dados de exemplo (idade de uma amostra)
amostra = np.array([25, 30, 35, 40, 45, 50])

# Intervalo de confiança de 95% para a média populacional
intervalo = stats.t.interval(0.95, len(amostra)-1, loc=np.mean(amostra), scale=stats.sem(amostra))
print("O intervalo de confiança de 95% para a média populacional é:", intervalo)