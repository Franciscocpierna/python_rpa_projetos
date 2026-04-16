## Numpy - Operações com Arrays - Parte 2


# - 2.1 Operações entre elementos
# - 2.2 Anexar e excluir
# - 2.3 Funções de agregação e ufuncs
# - 2.4 Remodelando arrays

# ### 2.1 Operações elementares

# As operações elemento a elemento aplicam uma determinada operação a cada elemento da matriz 
# de forma independente. Você também pode realizar adição, subtração, até multiplicação e 
# divisão nas matrizes.

# **Transmissão**: NumPy permite operações entre arrays de diferentes formatos e tamanhos, 
# o que é chamado de transmissão. A transmissão ajusta automaticamente o formato do array menor 
# para corresponder ao array maior, tornando-o compatível com operações elemento a elemento.

#importando o NumPy
import numpy as np

# Criando vetores NumPy 1D
arr1 = np.array([ 1 , 2 , 3 ]) 
arr2 = np.array([ 4 , 5 , 6 ]) 
escalar = 2 

# Adição
result_add = arr1 + arr2
print(result_add)

# Multiplicação, da mesma forma subração e divisão também. 
result_mul = arr1 * arr2  
print(result_mul)

# Criando vetores NumPy 2D (matrizes)
matriz1 = np.array([[ 1 , 2 ], [ 3 , 4 ]]) 
matriz2 = np.array([[ 5 , 6 ] , [ 7 , 8 ]]) 

# Multiplicação (por elemento, não multiplicação de matriz)
result_mul = matriz1 * matriz2  
print(result_mul)

# Multiplicação de matriz real usando np.dot
matriz_multiplicacao = np.dot(matriz1,matriz2) 
print(matriz_multiplicacao)

# Broadcasting: Multiplique o array por um resultado escalar
result = arr1 * escalar 
print(result)


### 2.2 Anexar e Excluir

# Para acrescentar matrizes no NumPy, você pode usar a `numpy.append()` função. Esta função permite 
# adicionar elementos ao final de um array existente ao longo de um eixo especificado.

# Tenha em mente que `np.append()` retorna um novo array com os elementos anexados; portanto, não 
# modifica os arrays originais. Se quiser modificar uma matriz existente no local, você pode usar
#  métodos como `np.concatenate()` ou usar instruções de atribuição.

# Podemos usar `np.delete` para remover os itens de um array.
# Crie um array

original_array = np.array([ 1 , 2 , 3 ]) 
print(original_array)

# Anexar elementos no local
original_array = np.append(original_array, [ 4 , 5 , 6 ]) 
print('#'*50)
# Crie um array NumPy
arr = np.array ([ 1 , 2 , 3 , 4 , 5 ]) 
print(arr)
print('#'*50)
# Remova o item no índice 2 (valor 3)
new_arr = np.delete(arr, 2 ) 
print(new_arr)

# Crie um array NumPy 2D
arr = np.array([[ 1 , 2 , 3 ], [ 4 , 5 , 6 ], [ 7 , 8 , 9 ]]) 
print('#'*50)
print(arr)

# Remova a segunda linha (índice 1)
new_arr = np.delete(arr, 1 , axis= 0 )
print(new_arr)

### 2.3 Funções de Agregação de ufuncs (funções universais)
#NumPy fornece funções integradas para operações de agregação comuns em matrizes, incluindo média,
# soma, mínimo, máximo, etc. NumPy também fornece funções universais (ufuncs) que operam 
# em elementos em matrizes, incluindo funções matemáticas, trigonométricas e exponenciais.
print('#'*50)
# Criando um array NumPy
arr = np.array([ 1 , 2 , 3 , 4 , 5 ]) 
print(arr)

# Funções de agregação
mean_value = np.mean(arr)        # média
median_value = np.median(arr)    # mediana
variance = np.var(arr)           # variância
standard_deviation = np.std(arr) # desvio padrão
print('Valor médio: ', mean_value)
print('Mediana: ', median_value)
print('Variância: ', variance)
print('Desvio Padrão: ', standard_deviation)
print('#'*50)
sum_value = np.sum(arr)    
min_value = np.min(arr)    
max_value = np.max(arr)    
print('Soma:', sum_value)
print('Mínimo:', min_value)
print('Máximo:', max_value)
print('#'*50)
# Funções universais
sqrt_arr = np.sqrt(arr)
exp_arr = np.exp(arr)
print('Raiz quadrada: ', sqrt_arr)
print('Exponencial..: ', exp_arr)

print('#'*50)

### 2.4 Remodelando Arrays

# Você pode alterar a forma de um array sem alterar seus dados usando o método `reshape`, por exemplo,
# para achatar um array (convertê-lo em um array 1D) ou alterá-lo para um array de dimensão superior 
# (por exemplo, de 1D para 2D ou de 2D para 3D).

# O método `reshape` pode ser particularmente útil quando você precisa preparar dados para diversas
#  operações, como multiplicação de matrizes, convolução ou exibição de imagens.

# Para remodelar o método, você pode passar a forma do resultado esperado que deseja. O número total 
# de elementos na matriz original deve corresponder ao número total de elementos na nova forma. 
# Em outras palavras, o produto das dimensões na nova forma deve ser igual ao número total de elementos
#  na matriz original. NumPy gerará um erro se esta condição não for atendida.


# Criando array 2D
arr_2d = np.array([[ 1 , 2 , 3 ], [ 4 , 5 , 6 ]]) 
print(arr_2d)

# Aqui como estamos passando apenas 6, ele irá converter o array 2d em 1d array 
# com 6 elementos, você não pode passar nada além de 6, 
# pois não corresponde ao array original! 
arr_1d = arr_2d.reshape( 6 )
print(arr_1d)

print('#'*50)
# Criando array 1D
arr_1d = np.array([ 1 , 2 , 3 , 4 , 5 , 6 ]) 
print(arr_1d)

# convertendo array 1D em 2D
arr_2d = arr_1d.reshape( 2 , 3 )
print(arr_2d)

print('#'*50)

#**Entendendo como usar -1**: Simplificando, você pode usar -1 como espaço reservado em qualquer
# dimensão da nova forma e o NumPy calculará automaticamente o tamanho dessa dimensão.

# Importando imagens de teste e conjuntos de dados.
# O módulo 'data' é um conjunto selecionado de imagens de propósito geral e científicas 
# usadas em testes, exemplos e documentação.
# mais informações em: https://scikit-image.org/docs/stable/api/skimage.data.html

from skimage import data 

# Carrega uma amostra de imagem em tons de cinza
image = data.coins() 

# Forma original da imagem 
print("Forma original da imagem:", image.shape) 

print('#'*50)
# Então, se você deseja convertê-lo para 1D, você deve passar 116352 (303*384) 
# Em vez disso, se você não quiser calcular isso e deixar o numpy lidar com isso, 
# Nesses casos, você pode simplesmente passar -1, e ele calculará 116352

reformed_image = image.reshape(-1) 
print('Nova forma da imagem: ', reformed_image.shape)

print('#'*50)
# Criando um array 1D com 12 elementos
arr = np.arange(12) 
print(arr.shape)

# Remodelando em um array 2D com um número desconhecido de colunas (-1)
reformed_arr = arr.reshape(4, -1)
print(reformed_arr.shape)