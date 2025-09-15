"""
Exemplo 2

Vamos explorar o problema de calcular o fatorial de um número
usando dois métodos diferentes.

Algoritmo 1: Fatorial Iterativo

    Calculamos o fatorial de um número multiplicando-o por cada número 
        menor até 1, de forma iterativa.

Algoritmo 2: Fatorial Recursivo

    Usamos a propriedade recursiva do fatorial: n!=n×(n−1)

Implementação dos Algoritmos:
"""

# Algoritmo 1: Fatorial Iterativo

# Define a função 'fatorial_iterativo', a qual calcula o 
# fatorial de um número inteiro 'n'.
# O fatorial de um número é o produto de todos os números 
# inteiros positivos de 1 até esse número.
# Por exemplo, fatorial de 5 (representado por 5!) é 5 x 4 x 3 x 2 x 1 = 120.
def fatorial_iterativo(n):
    
    # Inicializa a variável 'resultado' com 1. 
    # Este é o valor inicial pois multiplicar qualquer número 
    # por 1 não altera seu valor.
    # Esta variável irá armazenar os valores intermediários e 
    # o resultado final do cálculo do fatorial.
    resultado = 1
    
    # O loop 'for' começa em 1 e vai até 'n' (inclusive).
    # A função 'range(1, n + 1)' produz uma sequência de números de 1 até 'n'.
    # Em cada iteração do loop, a variável 'i' assume um valor dentro dessa sequência.
    for i in range(1, n + 1):
        
        # Multiplica o valor atual de 'resultado' pelo valor atual de 'i'.
        # Atribui esse produto de volta à variável 'resultado'.
        # Esta linha efetivamente acumula o produto de todos os números de 1 até 'n'.
        resultado *= i
    
    # Retorna o valor final do fatorial de 'n' após o término do loop.
    return resultado


# Algoritmo 2: Fatorial Recursivo

# Define a função 'fatorial_recursivo', a qual calcula o 
# fatorial de um número inteiro 'n' usando recursividade.
# A recursividade é uma abordagem onde a função chama a si 
# mesma com um argumento modificado até atingir uma condição base.
# Para o fatorial, a ideia é expressar o fatorial de 'n' como 'n' 
# multiplicado pelo fatorial de 'n-1'.
def fatorial_recursivo(n):
    
    # Caso base da recursividade.
    # Se 'n' for 0 ou 1, o fatorial é 1.
    # Esta condição serve para interromper a recursão e fornecer uma 
    # resposta direta para esses valores.
    if n == 0 or n == 1:
        return 1
    
    # Caso recursivo.
    # Se 'n' não é 0 ou 1, o fatorial de 'n' é calculado 
    # multiplicando 'n' pelo fatorial de 'n-1'.
    # Aqui, a função 'fatorial_recursivo' é chamada novamente, 
    # mas com 'n-1' como argumento.
    # Esta chamada recursiva continuará até que 'n' se torne 0 
    # ou 1, atingindo assim o caso base.
    return n * fatorial_recursivo(n - 1)



# Teste de Desempenho:

# Importa o módulo 'time'. 
# Esse módulo fornece várias funções relacionadas ao tempo, e 
# será usado aqui para medir o tempo de execução dos algoritmos.
import time

# Define uma variável chamada 'numero' e atribui o valor 10 a ela. 
# Este valor será usado para testar a eficiência dos algoritmos de fatorial.
numero = 10  # teste com fatorial de 10

# Medindo o tempo de execução do Algoritmo 1 (Fatorial Iterativo):

# Armazena o tempo atual (em segundos desde a época) na variável 'inicio'. 
# Isso marca o início da medição de tempo.
inicio = time.time()

# Calcula o fatorial do número usando a função 'fatorial_iterativo' e imprime o resultado.
print(fatorial_iterativo(numero))

# Armazena o tempo atual (em segundos desde a época) na variável 'fim'. 
# Isso marca o fim da medição de tempo.
fim = time.time()

# Imprime o tempo total que o Algoritmo 1 levou para executar.
# Isso é calculado subtraindo o tempo 'inicio' do tempo 'fim' e formatando
# o resultado para mostrar até 5 casas decimais.
print(f"Tempo do Algoritmo 1 (Iterativo): {fim - inicio:.5f} segundos")

# Medindo o tempo de execução do Algoritmo 2 (Fatorial Recursivo):

# Armazena o tempo atual (em segundos desde a época) na variável 'inicio'. 
# Isso marca o início da medição de tempo para o Algoritmo 2.
inicio = time.time()

# Calcula o fatorial do número usando a função 'fatorial_recursivo' e imprime o resultado.
print(fatorial_recursivo(numero))

# Armazena o tempo atual (em segundos desde a época) na variável 'fim'. 
# Isso marca o fim da medição de tempo para o Algoritmo 2.
fim = time.time()

# Imprime o tempo total que o Algoritmo 2 levou para executar.
# Novamente, isso é calculado subtraindo o tempo 'inicio' do tempo 'fim' e 
# formatando o resultado.
print(f"Tempo do Algoritmo 2 (Recursivo): {fim - inicio:.5f} segundos")


"""
Análise de Big O:

    Algoritmo 1 (Fatorial Iterativo): O(n) - pois ele percorre 
        cada número de 1 até n.
    
    Algoritmo 2 (Fatorial Recursivo): O(n) - embora utilize recursividade, ele 
        ainda tem que computar o fatorial de cada número de n até 1, uma vez.

Conclusão:

    Ambos os algoritmos têm uma complexidade de tempo de O(n). A diferença
real entre eles é a abordagem: o Algoritmo 1 usa um loop para calcular o 
fatorial, enquanto o Algoritmo 2 usa recursividade. Em máquinas e tamanhos 
de entradas pequenas, a diferença de tempo de execução entre os dois pode 
não ser significativa. No entanto, para entradas maiores, o fatorial recursivo 
pode atingir o limite de recursão do Python, enquanto o iterativo continua 
funcionando. Por outro lado, o algoritmo recursivo pode ser mais legível e 
intuitivo para algumas pessoas.
"""
print()