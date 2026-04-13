## Noções de Matemática - Estatística e Probabilidade - Parte 6

## 6. Probabilidade e Estatística Inferencial


# **6.1 Conceitos Básicos**

# A probabilidade é uma medida numérica que descreve a *chance de um evento ocorrer*. É amplamente utilizada 
# em Ciência de Dados para analisar incertezas e tomar decisões informadas. Alguns conceitos básicos 
# da probabilidade são:

# •	**Experimento**: É uma ação ou processo que leva a um resultado observável. Exemplos de experimentos 
# incluem lançar uma moeda, rolar um dado ou medir a altura de uma pessoa.

# •	**Espaço Amostral**: É o conjunto de todos os resultados possíveis de um experimento. Por exemplo, 
# o espaço amostral para o lançamento de um dado é {1, 2, 3, 4, 5, 6}.

# •	**Evento**: É um conjunto de resultados do espaço amostral. Os eventos podem ser simples (um único resultado)
#  ou compostos (mais de um resultado). Por exemplo, o evento "obter um número par" ao lançar um dado inclui 
# os resultados {2, 4, 6}.

# •	**Probabilidade**: É uma medida numérica que quantifica a chance de um evento ocorrer. A probabilidade 
# varia de 0 a 1, onde 0 indica impossibilidade e 1 indica certeza. A probabilidade de um evento A 
# é denotada por P(A).

# A probabilidade faz parte de uma parte da Estatística, chamada de Inferencial. A Estatística Inferencial 
# é representada por um conjunto de métodos de análise que nos permite estimar parâmetros e tirar 
# conclusões (inferir) sobre a população com base em apenas parte dela (amostra).  Assim, podemos tomar decisões mais adequadas e ainda fazer previsões.  Alguns exemplos de análises inferenciais ou testes de hipóteses são: (a) qui-quadrado; (b) anova; (c) teste t; (d) correlação; (e) regressão linear; (f) regressão logística entre outros.

# **6.2 O Cálculo da Probabilidade e a teoria dos grandes números**

# A teoria dos grandes números é um conceito fundamental na estatística e na teoria da probabilidade, e está relacionada ao cálculo da probabilidade
#  de eventos em amostras grandes. 
# A teoria dos grandes números estuda o comportamento das médias de uma grande quantidade de observações 
# aleatórias de uma mesma variável, à medida que o tamanho da amostra aumenta. Ela busca entender como essas
#  médias se aproximam das propriedades características da população subjacente à medida que a amostra cresce.
# Para exemplificar, vamos ver o caso do lançamento de moedas, e a determinação do cálculo da probabilidade 
# ao longo da quantidade de lançamentos...

import numpy as np
import matplotlib.pyplot as plt

# Função para simular lançamento de moedas
def simulacao_lancamento_moedas(n_lancamentos):
    resultados = np.random.choice(['cara', 'coroa'], size=n_lancamentos)
    proporcao_caras = np.cumsum(resultados == 'cara') / np.arange(1, n_lancamentos + 1)
    return proporcao_caras

# Número total de lançamentos
n_lancamentos = 1000

# Simulação dos lançamentos
proporcoes = simulacao_lancamento_moedas(n_lancamentos)

# Plot da evolução da proporção de caras
plt.figure(figsize=(10, 6))
plt.plot(range(1, n_lancamentos + 1), proporcoes, label='Proporção de Caras')
plt.axhline(y=0.5, color='r', linestyle='--', label='Valor Real: 0.5')
plt.xlabel('Número de Lançamentos')
plt.ylabel('Proporção de Caras')
plt.title('Simulação de Lançamento de Moedas')
plt.legend()
plt.grid(True)
plt.show()

# Este código cria uma função simulacao_lancamento_moedas que simula o lançamento de uma moeda honesta para determinar a proporção 
# de caras ao longo do tempo. Em seguida, ele plota um gráfico que mostra como a proporção de caras **converge para o valor real de 0.5 
# à medida que aumentamos o número de lançamentos** (como é ilustrado no gráfico resultante acima).

# **6.3 Regra da Adição (OU)**

# A regra da adição é usada para calcular a probabilidade da ocorrência de pelo menos um de dois eventos mutuamente exclusivos.
#  A regra pode ser aplicada da seguinte forma:

# Se A e B são dois eventos mutuamente exclusivos (não podem ocorrer simultaneamente), então a probabilidade de que ocorra pelo 
# menos um deles é dada por:

# ### P(A ou B) = P(A) + P(B)

# Exemplo de cálculo de probabilidade utilizando a regra da adição:
# Probabilidade de obter um número par ou um número ímpar ao lançar um dado
p_par = 3/6  # Probabilidade de obter um número par
p_impar = 3/6  # Probabilidade de obter um número ímpar

p_total = p_par + p_impar
print("A probabilidade de obter um número par ou ímpar é:", p_total)

# **6.4 Regra da Multiplicação (E)**

# A regra da multiplicação é usada para calcular a probabilidade da ocorrência de dois eventos em sequência. A regra pode 
# ser aplicada da seguinte forma:

# Se A e B são dois eventos independentes, então a probabilidade de que ocorram ambos é dada por:

# ### P(A e B) = P(A) * P(B)

# Exemplo de cálculo de probabilidade usando a regra da multiplicação:

# Probabilidade de obter um número par ao lançar um dado e depois obter um número maior que 3 ao lançar outro dado
p_par = 3/6  # Probabilidade de obter um número par
p_maior_3 = 3/6  # Probabilidade de obter um número maior que 3

p_total = p_par * p_maior_3
print("A probabilidade de obter um número par e depois um número maior que 3 é:", p_total)

# **6.5 Eventos Independentes e Dependentes**

# Dois eventos são independentes se a ocorrência ou não ocorrência de um evento não influencia a ocorrência do outro evento.
# Dois eventos são dependentes se a ocorrência ou não ocorrência de um evento afeta a probabilidade de ocorrência do 
# outro evento.

# Exemplo de cálculo de probabilidade com eventos independentes e dependentes:

# Probabilidade de obter uma carta de baralho vermelha e, em seguida, 
# uma carta de copas (dependentes)
p_vermelha = 26/52  # Probabilidade de obter uma carta vermelha
p_copas = 13/51  # Probabilidade de obter uma carta de copas após obter uma carta vermelha

p_total = p_vermelha * p_copas
print("A probabilidade de obter uma carta vermelha e, em seguida, uma carta de copas é:", p_total)

# Probabilidade de obter um número par ao lançar um dado e, em seguida, obter um 
# número ímpar ao lançar outro dado (independentes)
p_par = 3/6  # Probabilidade de obter um número par
pímpar = 3/6  # Probabilidade de obter um número ímpar

p_total = p_par * p_impar
print("A probabilidade de obter um número par e, em seguida, um número ímpar é:", p_total)
