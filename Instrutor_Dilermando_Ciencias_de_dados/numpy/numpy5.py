

## NumPy para Álgebra Linear e Técnicas Avançadas - Parte 5

# - 5.1 Operações com Matrizes Complexas
# - 5.2 Resolver Equações Lineares
# - 5.3 Matrizes Mascaradas
# - 5.4 Matrizes Estruturadas

# Numpy também possui uma ampla gama de funções para Álgebra Linear.

### 5.1 Operações com Matrizes Complexas



# Já vimos a criação de vetores, matrizes e as incríveis operações matriciais que podemos fazer com Numpy. 
# Aqui estão até operações matriciais complexas.

# - **Inversão de Matriz:** Você pode calcular o inverso de uma matriz usando a função NumPy `np.linalg.inv()`.
# - **Autovalores e Autovetores:** Você pode calcular autovalores e autovetores de matrizes usando 
# `np.linalg.eig()`.
# - **Normas e Distâncias Matriciais:** Calcule normas matriciais (por exemplo, norma Frobenius) usando 
#   `np.linalg.norm()`. Você também pode usá-lo para calcular distâncias entre vetores ou matrizes.
# - **Classificação da Matriz:** Encontre a classificação de uma matriz usando `np.linalg.matrix_rank()`.

### 5.2 Resolver Equações Lineares

#Você pode resolver equações lineares com recursos numpy. Para resolver sistemas de equações lineares 
# use`np.linalg.solve()`.

#importando o NumPy
import numpy as np
A = np.array([[ 2, 3 ], [ 4, 5 ]]) 
b = np.array([ 6, 7 ]) 

# Resolva Ax = b para x
x = np.linalg.solve(A, b )
print(x)
print('*'*50)


### 5.3 Matrizes Mascaradas


# Matrizes mascaradas no NumPy permitem trabalhar com dados onde certos elementos são inválidos ou ausentes. 
# Uma máscara é um array booleano que indica quais elementos devem ser considerados válidos e quais devem 
# ser mascarados (inválidos ou ausentes).

# Matrizes mascaradas permitem executar operações em dados válidos enquanto ignora os elementos mascarados.
# Importando especificamente a classe "ma" para trabalhar matrizes mascaradas (todo o pacote numpy está já importado como np)
import numpy.ma as ma 

# Conjunto de dados de temperatura com valores ausentes (-999 representa valores ausentes)
temperaturas = np.array([22, 5, 23, 0, -999, 24, 5, -999, 26, 0, 27, 2, -999, 28, 5]) 

# Calcule a temperatura média sem lidar com valores faltantes
mean_temperatura = np.mean(temperaturas) 

# Imprima o resultado
print('Temperatura Média Geral: ', mean_temperatura)

# Crie uma máscara para valores faltantes ( -999)
mask = (temperaturas == -999 ) 

# Crie uma matriz mascarada
masked_temperaturas = ma.masked_array(temperaturas, mask=mask) 

# Calcule a temperatura média (excluindo valores ausentes)
mean_temperatura = ma.mean(masked_temperaturas) 

# Imprima o novo resultado 
print("Temperatura média (excluindo valores ausentes):" , mean_temperatura)
print('*'*50)

### 5.4 Matrizes Estruturadas

#Matrizes estruturadas permitem trabalhar com dados semelhantes a uma tabela com colunas nomeadas. 
#Cada elemento de uma matriz estruturada pode ter diferentes tipos de dados. Crie seus tipos de dados 
#usando `np.dtype` e adicione o nome da coluna e o tipo de dados como uma tupla. Então você pode passá-lo 
# para o seu array.

# Defina os tipos de dados para os campos
dt = np.dtype([( 'nome' , 'S20' ), ( 'idade' , int ), ( 'salario' , float )]) 

# Criando uma matriz estruturada de Funcionários
funcionarios = np.array([('Alice', 30, 50000.0), ('Roberto', 25, 60000.0)], dtype=dt) 

# Acesse o campo 'nome' do primeiro funcionário 
print(funcionarios['nome'] [0]) 

# Acessar o campo 'idade' de todos os funcionários 
print(funcionarios['idade'])

print('*'*50)
