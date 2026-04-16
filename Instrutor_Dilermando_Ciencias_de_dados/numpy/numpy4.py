## NumPy para limpeza de dados e análise estatística - Parte 4

# - 4.1 Identificando valores ausentes
# - 4.2 Removendo linhas ou colunas com valores ausentes
# - 4.3 Transformação de dados
# - 4.4 Amostragem aleatória

#Se você tem seus dados em um array numérico numpy e deseja observar valores ausentes e removê-los rapidamente, 
# nesse caso, você não precisa converter o array em série pandas para lidar com isso! Podemos fazer isso dentro 
# do próprio Numpy. Veja como fazemos isso.

### 4.1 Identificando valores ausentes

#NumPy fornece funções para verificar valores ausentes em uma matriz numérica, representada como 
# NaN (Not a Number).

# Importando o pacote Numpy
import numpy as np

# Crie uma matriz NumPy com valores ausentes
data = np.array([ 1 , 2 , np.nan, 4 , np.nan, 6 ]) 

# Verifique se há valores ausentes
has_missing = np.isnan(data) 
print (has_missing)
print('*'*50)
### 4.2 Removendo linhas ou colunas com valores ausentes

#Podemos usar np.isnan para obter uma matriz booleana com True para os índices onde há um valor ausente.
# E quando passarmos para np.any, ele retornará um array 1D com True para o índice onde qualquer item de linha 
# é True. E finalmente nós ~ (não) e passamos o booleano para a Matriz original, que removerá as linhas com 
# valores ausentes.

# Criando uma matriz 2D com valores ausentes
data = np.array([[1, 2, 3], [4, np.nan, 6], [7, 8, 9]]) 

# Removendo linhas com quaisquer valores ausentes
cleaned_data = data[~np.any(np.isnan(data), axis= 0)] 
print(cleaned_data)
print('*'*50)

### 4.3 Transformação de dados
# Numpy não possui os recursos de transformação de dados diretamente, mas podemos utilizar os recursos
#  existentes para realizá-los.

# **Centralização de dados:** centralizar os dados envolve subtrair a média de cada ponto de dados. 
# Isso geralmente é feito para remover o efeito de um termo constante ou para facilitar a convergência 
# do modelo.

# Dados de centralização de dados
data = np.array([ 10, 20, 30, 40, 50]) 
media = np.mean(data) 
dados_centralizados = data - media 
print('Média: ', media)
print('Centralização: ', dados_centralizados)

#**Padronização:** Trata-se de transformar dados numéricos de forma que tenham média 0 e desvio padrão 1.
# Esse processo facilita a comparação e análise de dados em diferentes escalas.
print('*'*50)
# Padronização
std_dev = np.std(data)  #desvio padrão
standardized_data = (data - media) / std_dev
print('Desvio Padrão: ', std_dev)
print("Padronização: ", standardized_data)



#**Transformação Log:** A transformação logarítmica é usada para tornar os dados mais simétricos ou 
# para estabilizar a variância em casos de crescimento exponencial.

print('*'*50)
# Transformação Log
log_transformed_data = np.log(data)
print(log_transformed_data)


### 4.4 Amostragem Aleatória
# A amostragem aleatória envolve a seleção de um subconjunto de pontos de dados de um conjunto de dados maior.
# NumPy também fornece ferramentas para gerar números aleatórios a partir de várias distribuições 
# de probabilidade.

# **Amostragem:**

# - Amostragem Aleatória Simples: Selecione uma amostra aleatória de um tamanho especificado de um conjunto 
# de dados. Na amostragem sem reposição, cada item selecionado não é devolvido à população.
# - Amostragem Bootstrap: A amostragem Bootstrap envolve amostragem com substituição para criar 
# vários conjuntos de dados. Isso é frequentemente usado para estimar a variabilidade das estatísticas.

# Amostragem aleatória simples sem dados de substituição 
print('*'*50)
data = np.array([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
random_samples = np.random.choice(data, size= 5 , replace=False) 
print(random_samples)

print('*'*50)

# Amostragem de Bootstrap
num_samples = 1000
bootstrap_samples = np.random.choice(data, size=(num_samples, len(data)), replace=True)
print('Tamanho: ', bootstrap_samples.shape)
print(bootstrap_samples)
#### Outras funções:

# **Gerando números aleatórios**: Aqui estão algumas maneiras de gerar números aleatórios com a distribuição 
# desejada.

# - Inteiros: Gerar um número inteiro aleatório dentro de uma faixa especificada usando `np.random.randint()`
# - Distribuição Uniforme: Gerar valores aleatórios de uma distribuição uniforme usando `np.random.uniform()`
# - Distribuição Normal: Amostrar valores aleatórios de uma distribuição normal usando `np.random.normal()`
# - Distribuição Binomial: Simular experimentos binomiais com `np.random.binomial()`
# - Distribuição de Poisson: Modelar eventos raros com a distribuição de Poisson usando `np.random.poisson()`




