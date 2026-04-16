## Numpy - Trabalhando com arrays Numpy - Parte 3

# - 3.1 Combinando arrays
# - 3.2 Dividindo arrays
# - 3.3 Alias ​​vs. Visualização vs. Cópia de arrays
# - 3.4 Classificando arrays Numpy

### 3.1 Combinando arrays

#NumPy fornece a função `np.concatenate()` para concatenar arrays ao longo de um eixo 
# especificado. E o empilhamento de matrizes pode ser feito usando funções como `np.vstack()`
#  (empilhamento vertical) e `np.hstack()` (empilhamento horizontal).


#importando o NumPy
import numpy as np
arr1 = np.array([ 1 , 2 , 3 ]) 
arr2 = np.array([ 4 , 5 , 6 ]) 

# Concatenar ao longo do eixo 0 (linhas)
combinado = np.concatenate((arr1, arr2)) 
print(combinado)
print('*'*50)
# Empilhamento vertical
vertical_stack = np.vstack((arr1, arr2)) 
print(vertical_stack)
print('*'*50)
# Empilhamento horizontal
horizontal_stack = np.hstack((arr1, arr2))
print(horizontal_stack)
print('*'*50)
### 3.2 Dividindo Arrays

#Dividir arrays é o oposto de combiná-los. É o processo de dividir um único array em vários arrays menores.
#NumPy fornece funções `np.split()`, `np.hsplit()` e `np.vsplit()` para essa finalidade.

# Dividido em três partes iguais
arr = np.array([ 1 , 2 , 3 , 4 , 5 , 6 ])
print(arr)
split_arr = np.split(arr, 3 ) 
print(split_arr)

### 3.3 Alias ​​vs. Visualização vs. Cópia de Arrays
# **Alias:** Um alias refere-se a múltiplas variáveis que apontam para o mesmo objeto de matriz 
# NumPy subjacente. Eles compartilham os mesmos dados na memória. As alterações na matriz de alias 
# afetarão a matriz original.

# **Visualização:** O método `.view()` cria um novo objeto array que analisa os mesmos dados do array original,
# mas não compartilha a mesma identidade. Ele fornece uma maneira de visualizar os dados de maneira diferente 
# ou com diferentes tipos de dados, mas ainda opera com os mesmos dados subjacentes.

# **Cópia:** Uma cópia é uma duplicata completamente independente de um array NumPy. Ele possui seus próprios 
# dados na memória e as alterações feitas na cópia não afetarão o array original e vice-versa.
original_arr = np.array([ 1 , 2 , 3 ]) 
print('*'*50)
# alias do array original
alias_arr = original_arr 
print(alias_arr)

# Alterações em view_arr afetarão o array original
view_arr = original_arr.view() 
print(view_arr)
print('*'*50)

# Alterações em copy_arr não afetarão o array original
copy_arr = original_arr.copy()
print(copy_arr)
print('*'*50)
### 3.4 Classificando Arrays Numpy
#Você pode usar `np.sort(array)` para classificar o array em ordem crescente, porém para ordem 
# decrescente você tem que usar o truque de fatiar o array `[::-1]`, que inverte os elementos do array.

data = np.array([ 3 , 1 , 5 , 2 , 4 ]) 
sorted_data = np.sort(data)   # Ordem crescente
print(sorted_data)
reverse_sorted_data = np.sort(data)[::-1 ]   # Ordem decrescente 
print(reverse_sorted_data)
print('*'*50)
# Você também pode recuperar os índices que classificariam os dados. 
data = np.array([ 3 , 1 , 5 , 2 , 4 ]) 
print(data)
print('*'*50)
# Retorna índices que classificariam o array. 
indices_classificados = np.argsort(data)
print(indices_classificados)






