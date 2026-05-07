
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from scipy import stats
from sklearn import preprocessing

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
df = pd.read_csv('Salary_Data.csv')
print(df.head())
print(df.shape)
print('#'*100)
print(df.info())

print('#'*100)
print(df.isna().sum())


print('#'*100)
# verifica se tem pelo menos um dado nulo no dataframe inteiro
tem_nulos = df.isna().any().any()
print("O DataFrame tem dados ausentes?", tem_nulos)

print('#'*100)
#total_nulos = df.isna().sum().sum()
#print("Total de dados ausentes:", total_nulos)
#linhas_com_nulos = df[df.isna().any(axis=1)]
#print(f'Visualizar as linhas que contêm dados ausentes: {linhas_com_nulos}')
print()

print('#'*100)
print()


print('#'*100)
print()


print('#'*100)
print()


