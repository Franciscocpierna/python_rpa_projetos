## Noções de Matemática - Estatística e Probabilidade - Parte 2

## 2. Tipos de Dados



# Em Ciência de Dados, é fundamental entender a natureza dos dados com os quais estamos lidando. 
# Os dados podem ser qualitativos ou quantitativos:

# **2.1 Dados qualitativos**

# Também conhecidos como dados categóricos, esses dados representam atributos ou qualidades 
# que não podem ser quantificados numericamente. Existem duas categorias de dados qualitativos:

# •	**Dados Qualitativos Nominais**: São dados que representam atributos sem uma ordem específica. 
# Exemplos de dados qualitativos nominais incluem gênero, cor dos olhos ou estado civil.

# •	**Dados Qualitativos Ordinais**: São dados que representam atributos com uma ordem específica. 
# Exemplos de dados qualitativos ordinais incluem classificações como "baixo", "médio" e "alto" 
# ou níveis de satisfação como "insatisfeito", "satisfeito" e "muito satisfeito" ou ainda, 
# nível de escolaridade.

# **2.2 Dados quantitativos**

# Esses dados representam quantidades numéricas e podem ser subcategorizados em dois tipos principais:

# •	**Dados Quantitativos Discretos**: São dados que representam valores numéricos inteiros e 
# distintos. Exemplos de dados quantitativos discretos incluem o número de filhos em uma família, 
# o número de visitantes em um site ou o número de carros em um estacionamento.

# •	**Dados Quantitativos Contínuos**: São dados que podem assumir valores em uma escala contínua. 
# Exemplos de dados quantitativos contínuos incluem a altura de uma pessoa, o peso de um objeto ou 
# o tempo decorrido entre dois eventos.

# Em resumo, temos o seguinte:

# ![title](imagens/variavel.jpg)

# A seguir estão alguns exemplos de codificação em Jupyter Notebook para cada um dos tipos de dados:

#Exemplo de criação de um conjunto de dados qualitativos utilizando a biblioteca Pandas:

import pandas as pd

# Criação de um DataFrame com dados qualitativos nominais (gênero)
dados = pd.DataFrame({'Nome': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
                      'Gênero': ['Masculino', 'Feminino', 'Masculino', 'Feminino', 'Masculino']})
print(dados.head())

#Exemplo de criação de um conjunto de dados qualitativos utilizando a biblioteca Pandas:

# Criação de um DataFrame com dados qualitativos ordinais (nível de satisfação)
dados = pd.DataFrame({'Cliente': ['A', 'B', 'C', 'D', 'E'],
                      'Satisfação': ['Baixo', 'Médio', 'Alto', 'Médio', 'Alto']})
print(dados.head())


#Exemplo de criação de um conjunto de dados quantitativos discretos utilizando a biblioteca NumPy:

import numpy as np

# Criação de um conjunto de dados de número de filhos
num_filhos = np.array([0, 2, 1, 3, 2])

print(num_filhos)


#Exemplo de criação de um conjunto de dados quantitativos contínuos utilizando a biblioteca NumPy:

#import numpy as np

# Criação de um conjunto de dados de altura
altura = np.array([165, 170, 155, 180, 160])

print(altura)

#Esses são apenas alguns exemplos iniciais, mas ao longo da sua jornada em Ciência de Dados, 
# você encontrará muitos outros tipos de dados e poderá utilizar diversas bibliotecas, 
# como Pandas e NumPy, para trabalhar com eles.