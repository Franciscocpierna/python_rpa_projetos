## Noções de Matemática - Estatística e Probabilidade - Parte 8

## 8. Teste de Hipóteses

# **8.1 Conceitos Básicos de Teste de Hipóteses**

# O teste de hipóteses é uma técnica estatística usada para tomar decisões sobre uma afirmação 
# (hipótese) feita sobre uma população com base em evidências de uma amostra. Os principais conceitos 
# envolvidos em um teste de hipóteses são:

# •	**Hipótese Nula (H0)**: É a afirmação que se assume como verdadeira e é testada. Representa a 
# situação em que não há efeito ou diferença significativa.

# •	**Hipótese Alternativa (Ha)**: É a afirmação oposta à hipótese nula. Representa a situação
#  em que há um efeito ou diferença significativa.

# •	**Nível de Significância (α)**: É a probabilidade de rejeitar a hipótese nula quando ela é verdadeira.
#  Geralmente, é fixado em um valor pequeno, como 0,05 ou 0,01.

# •	**Valor-P (p-value)**: É a probabilidade de obter uma estatística de teste igual ou mais extrema do que
#  a observada, assumindo que a hipótese nula seja verdadeira. É usado para tomar a decisão de aceitar ou 
# rejeitar a hipótese nula.

# •	**Decisão**: Com base no valor-p e no nível de significância, decide-se rejeitar ou não rejeitar a
#  hipótese nula. Se o valor-p for menor que o nível de significância, rejeita-se a hipótese nula;
#  caso contrário, não se tem evidências suficientes para rejeitá-la.

# **8.2 Teste de Hipóteses para uma Média Populacional**

# O teste de hipóteses para uma média populacional é usado quando se deseja fazer afirmações sobre
#  a média de uma população com base em uma amostra. Os passos gerais para realizar um teste de hipóteses
#  para uma média populacional são:

# •	**Formular as hipóteses nula e alternativa**: Definir as hipóteses nula (H0) e alternativa (Ha) com 
# base na afirmação que se deseja testar.

# •	**Determinar o nível de significância**: Escolher o nível de significância (α) para o teste. 
# Geralmente, é utilizado o valor de 0,05.

# •	**Calcular a estatística de teste**: Calcular a estatística de teste apropriada para o teste de 
# hipóteses. Por exemplo, se a amostra é grande e a variância populacional é conhecida, pode-se 
# utilizar o teste z; caso contrário, se a amostra é pequena ou a variância populacional é desconhecida,
#  pode-se utilizar o teste t de Student.

# •	**Calcular o valor-p**: Calcular o valor-p correspondente à estatística de teste.

# •	**Tomar a decisão**: Comparar o valor-p com o nível de significância e tomar a decisão de aceitar
#  ou rejeitar a hipótese nula. Se o valor-p for menor que o nível de significância, rejeita-se H0; 
# caso contrário, não se tem evidências suficientes para rejeitá-la.

# Teste de Hipóteses para uma Média Populacional

import numpy as np
from scipy import stats

# Dados de exemplo (amostra)
amostra = np.array([25, 30, 35, 40, 45, 50])

# Teste de hipóteses para a média populacional
# Hipótese nula: média populacional = 30
# Hipótese alternativa: média populacional != 30

# Realizar o teste de hipóteses
valor_p = stats.ttest_1samp(amostra, 30).pvalue
print(f"valor_p: {valor_p}")

# Comparar o valor-p com o nível de significância (α = 0.05)
nivel_significancia = 0.05
if valor_p < nivel_significancia:
    print("Rejeitar H0: a média populacional é diferente de 30.")
else:
    print("Aceitar H0: não há evidências suficientes para afirmar que a média populacional é diferente de 30.")


# **8.3 Teste de Hipóteses para Duas Médias Populacionais**

# O teste de hipóteses para duas médias populacionais é usado quando se deseja fazer afirmações sobre a diferença 
# entre duas médias de duas populações diferentes com base em duas amostras independentes. Os passos gerais para 
# realizar um teste de hipóteses para duas médias populacionais são:

# •	**Formular as hipóteses nula e alternativa**: Definir as hipóteses nula (H0) e alternativa (Ha) com base na afirmação 
# que se deseja testar.

# •	**Determinar o nível de significância**: Escolher o nível de significância (α) para o teste. Geralmente, é utilizado o valor de 0,05.

# •	**Calcular a estatística de teste**: Calcular a estatística de teste apropriada para o teste de hipóteses. Pode-se utilizar
#  o teste t de Student, assumindo a igualdade ou a diferença das variâncias populacionais, dependendo do caso.

# •	**Calcular o valor-p**: Calcular o valor-p correspondente à estatística de teste.

# •	**Tomar a decisão**: Comparar o valor-p com o nível de significância e tomar a decisão de aceitar ou rejeitar a hipótese nula.
#  Se o valor-p for menor que o nível de significância, rejeita-se H0; caso contrário, não se tem evidências 
# suficientes para rejeitá-la.

# Teste de Hipóteses para Duas Médias Populacionais


import numpy as np
from scipy import stats

#Dados de exemplo (amostras independentes)
amostra1 = np.array([25, 30, 35, 40, 45])
amostra2 = np.array([20, 28, 33, 38, 42])

# Teste de hipóteses para a diferença de médias populacionais
# Hipótese nula: média populacional1 - média populacional2 = 0
# Hipótese alternativa: média populacional1 - média populacional2 != 0

# Realizar o teste de hipóteses
valor_p = stats.ttest_ind(amostra1, amostra2).pvalue
print("valor_p: ", valor_p)

# Comparar o valor-p com o nível de significância (α = 0.05)
nivel_significancia = 0.05
if valor_p < nivel_significancia:
    print("Rejeitar H0: há diferença significativa entre as médias populacionais.")
else:
    print("Aceitar H0: não há evidências suficientes para afirmar que há diferença significativa entre as médias populacionais.")