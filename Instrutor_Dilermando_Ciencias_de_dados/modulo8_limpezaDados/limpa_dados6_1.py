# Importação dos Pacotes necessários para este projeto
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
## Carregando os Dados

# Neste projeto vamos trabalhar com um *data set modificado* do seguinte repositório:
# **UCI - Machine Learning Repository (Center of Machine Learning and Intelligent Systems)**
# Link: https://archive.ics.uci.edu/ml/datasets/bank+marketing

# Trata-se de um data set onde os dados estão relacionados com campanhas de marketing direto de uma 
# instituição bancária portuguesa. As campanhas de marketing foram baseadas em telefonemas. Muitas vezes, 
# era necessário mais do que um contacto para o mesmo cliente, para saber se o produto 
# (depósito bancário a prazo) seria ('sim') ou não ('não') confirmado (subscrito).

# Os dados foram modificados para fosse possível realizarmos operações as limpeza de dados que vamos trabalhar 
# neste projeto.
# O data set (arquivo csv pronto para uso) estará disponíveis como recurso dessa aula.


# Carrega o dataset
df = pd.read_csv("dados/bank-full.csv") 

print(df.shape)

print(df.head())


print('#'*100)
