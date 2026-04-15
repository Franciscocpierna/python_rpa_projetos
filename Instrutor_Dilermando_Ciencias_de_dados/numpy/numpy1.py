# Numpy - Uma introdução ao Pacote Numpy - Parte 1

#Seja bem-vindo ao universo do NumPy! Aqui, você transcende as limitações das listas Python e adquire
# o poder de executar operações de array complexas de maneira eficiente, graças à robusta biblioteca NumPy
# uma abreviação para "Python Numérico". Neste módulo abrangente e objetivo, embarque conosco para d
# esvendar os segredos do NumPy e desbloquear todo o seu potencial extraordinário.

### Índice

# #### Parte1: Noções básicas de array Numpy
# - 1.1 Compreendendo tipos de dados Numpy
# - 1.2 Criando arrays Numpy
# - 1.3 Indexação em Arrays NumPy
# - 1.4 Funções/Métodos NumPy

# #### Parte 2: Operações com Arrays
# - 2.1 Operações entre elementos
# - 2.2 Anexar e excluir
# - 2.3 Funções de agregação e ufuncs
# - 2.4 Remodelando arrays

# #### Parte3: Trabalhando com Arrays Numpy
# - 3.1 Combinando arrays
# - 3.2 Dividindo arrays
# - 3.3 Alias ​​vs. Visualização vs. Cópia de arrays
# - 3.4 Classificando arrays Numpy

# #### Parte4: NumPy para limpeza de dados e análise estatística
# - 4.1 Identificando valores ausentes
# - 4.2 Removendo linhas ou colunas com valores ausentes
# - 4.3 Transformação de dados
# - 4.4 Amostragem aleatória

# #### Parte5: NumPy para Álgebra Linear e Técnicas Avançadas
# - 5.1 Operações de Matrizes Complexas
# - 5.2 Resolver Equações Lineares
# - 5.3 Matrizes Mascaradas
# - 5.4 Matrizes Estruturadas

## Parte1: Noções básicas de array Numpy
#Os arrays NumPy são projetados para computação numérica e científica , tornando-os ideais para 
# tarefas como análise de dados, aprendizado de máquina e operações matemáticas.


### 1.1 Compreendendo tipos de dados Numpy

# Em Numpy Arrays, todos os elementos dentro de um único array devem ter o mesmo tipo de dados. 
# Essa homogeneidade é um dos principais recursos que tornam os arrays NumPy eficientes e adequados
# para computação numérica, e alguns outros motivos são os seguintes:

# - **Eficiência:** Nos bastidores, o NumPy é implementado em C e Fortran, tornando as operações
#  em grandes arrays extremamente rápidas em comparação com o código Python equivalente.
# - **Poder matemático:** você não acreditaria na ampla variedade de funções e operações 
# matemáticas disponíveis no Numpy, facilitando tarefas como álgebra linear, estatística e cálculos 
# matemáticos complexos.
# - **Interoperabilidade:** NumPy integra-se perfeitamente com outras bibliotecas Python, como Pandas,
#  SciPy e Matplotlib.

#importando o NumPy
import numpy as np
#verificando a versão do numpy
print(f'versão do numpy {np.__version__}')

# Para instalação de uma versão exata de um pacote Python
# Este módulo foi executado utilizando a versão 1.26.4 do Numpy
# pip install numpy==1.26.4


### 1.2 Criando arrays Numpy

#Criando um Array a partir de uma lista Python
array1 = np.array([2, 5, 10, 34, 23, 9, 73, 21, 6])
print(array1)

#Conformando o tipo de dados do array criado
print(f'tipo de dado {type(array1)}')


#ndarray - n dimensional array - array de dimensão n

#Vamos ver o formato (shape) desse array
print(f'vamos ver o formato (shape) desse array =  {array1.shape}')

# Os arrays são estruturas de dados muito mais eficientes do que os tipos básicos da linguagem Python.

# Criando um array inteiro com dtype explícito, o que não é necessário.
int_array = np.array([ 1 , 2 , 3 ], dtype=np.int32) 

### 1.3 Indexação em Arrays NumPy

print(array1)
print(f'array na posição 5 =  {array1[5]}')

# A indexação em Python, com qualquer interável, inicia com ZERO.

# Também posso fazer o fatiamento:
print(f'fatiamento array1[1:4] = {array1[1:4]}')

print(array1)
# criando uma lista de índices
indices = [1, 3, 6, 8]

print(f'indices = {indices}')

# Imprimindo os elementos com os respectivos índices:
print(f'elementos com os respectivos índices no array1[indices] = {array1[indices]}')
array1[indices]


# Criando uma máscara (no caso vamos criar uma máscara booleana para os elementos pares)
mascara = (array1 % 2 == 0)
# Vamos ver a máscara criada...
print(f'mascara criada = {mascara}')

# Vamos utilizar a máscara criada como indexador. No caso, ele vai retornar os elementos cujos índices forem verdadeiros.
# Ou seja... vai retornar todos os valores que são pares.
print(f'resultado com mascara criada array1[mascara] = {array1[mascara]}')


# Utilizamos a indexação também para fazer a substituição de valores...
array1[0] = 200
print(f'array1[0] = 200 => {array1[0] }')

print(f'array1 depois de atribuir 200 => {array1}')

#array1[0] = 'c'

#print(f'array1[0] = "c" =>  {array1[0]}')

#### Atenção!!! #array1[0] = 'c'
# Não é possível incluir elementos de outros tipos de dados.
# Arrays NumPy são todos do mesmo tipo de dado.

### 1.4 Funções/Métodos NumPy

# A função array() cria um array NumPy
array2 = np.array([1,2,3,4,5])
print(f'array2 = {array2}')

print(f'vamos ver o formato (shape) array2.shape desse array =  {array2.shape}')


# array2 agora é um objeto do tipo nd.array... e portanto possuem uma série de métodos associados a este objeto.
# para visualizar os métodos... digite o nome... ponto... e tecle tab.
#array2.
# 

#Usando os métodos do array NumPy...
#cumsum --> soma acumulada
print(f'array2.cumsum() = {array2.cumsum()}')

#cumprod --> produto acumulado
print(f'array2.cumprod() = {array2.cumprod()}')

# 1. Usando dir(): Lista todos os atributos e métodos
atributos = dir(np)
print(atributos)

# Filtramos para não mostrar métodos "mágicos" (que começam com __) por agora
metodos_publicos = [a for a in atributos if not a.startswith('_')]
print(metodos_publicos)








