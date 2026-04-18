
# Pandas - Noções básicas do pacote Pandas - Parte 5
# Mesclar, Juntar, e Concatenar


# Existem três maneiras principais de combinar os DataFrames: mesclando, juntando e concatenando
#  (merge, join e concat). Vamos ver esses 3 métodos com exemplos.

# ### 6.1 Introdução aos Comandos

# **merge:**

# Combina DataFrames com base em colunas comuns.
# Funciona como um “join” no SQL.

# **join:**

# Combina DataFrames com base em índices ou colunas.
# Pode ser usado para combinar DataFrames verticalmente ou horizontalmente.

# **concat:**

### 6.2 Criando um Dataframe de exemplo

# Importando o Pandas
import pandas as pd

# DataFrame 1
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Nome': ['Alice', 'Bob', 'Carol']})
print(df1)
# DataFrame 2
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Salário': [5000, 6000, 7000]})
print('#'*50)
# Concatena DataFrames verticalmente ou horizontalmente.
# Útil para empilhar ou mesclar dados.
print(df2)


print('#'*50)
### 6.3 Mesclar (merge)

# A função ** mesclar ** permite que você mescle os quadros de dados juntos usando uma lógica semelhante à 
# mesclagem de tabelas SQL juntas. Por exemplo:

#Inner Join:

df_inner = pd.merge(df1, df2, on='ID')
print(df_inner)
print('#'*50)
#Left Join:
df_left = pd.merge(df1, df2, on='ID', how='left')
print(df_left)
print('#'*50)
### 6.4 Juntar (join)
#Juntar (join) é um método conveniente para combinar as colunas de dois DataFrames indexados potencialmente 
# diferentes em um único resultado DataFrame.

#Join por Índice
df_index_join = df1.set_index('ID').join(df2.set_index('ID'))
print(df_index_join)
print('#'*50)
#Join por Coluna
print('#'*50)
df_col_join = df1.join(df2.set_index('ID'), on='ID')
print(df_col_join)
print('#'*50)
### 6.5 Concatenação (concat)

#Concatenação basicamente cola DataFrames.  Tenha em mente que as dimensões devem corresponder ao longo 
#do eixo que você está concatenando. Você pode usar `pd.concat` e passar uma lista de DataFrames para 
# concatenar juntos:

#Concatenação Horizontal
df_horizontal = pd.concat([df1, df2], axis=1)
print(df_horizontal)

print('#'*50)

#Concatenação Vertical

df_vertical = pd.concat([df1, df2])
print(df_vertical)