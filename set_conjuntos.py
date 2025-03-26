"""
Definição e Características
        - Um "set" é uma coleção desordenada de elementos únicos. Isso 
        significa que não permite duplicatas.
        
        Sets são mutáveis, mas os elementos contidos neles devem 
        ser imutáveis (por exemplo, números, strings e tuplas).
"""
#Exemplo 1: Removendo Duplicatas de uma Lista

#Uma aplicação comum do set é a remoção de duplicatas de uma lista.

# Dada a seguinte lista:
lista = [1, 2, 2, 3, 4, 4, 5, 5, 5]
print(lista)

# Convertendo a lista para um conjunto, as duplicatas são automaticamente removidas
conjunto = set(lista)
print(conjunto)  # Saída: {1, 2, 3, 4, 5}

print()
#Exemplo 2: Verificando a Imutabilidade dos Elementos

#Enquanto o próprio conjunto é mutável (o que significa que você pode 
#adicionar ou remover elementos dele), os elementos dentro do conjunto devem ser imutáveis.

# Criando um conjunto com elementos imutáveis
conjunto = {1, 2, "Python", (4, 5)}
print(conjunto)  # Saída: {1, (4, 5), 2, 'Python'}

"""
Em Python, um conjunto é uma coleção não ordenada de 
elementos únicos. Isso significa que a ordem dos elementos 
dentro de um conjunto não é garantida. Quando você imprime um 
conjunto, os elementos podem ser exibidos em qualquer ordem, pois 
a estrutura subjacente de dados (geralmente uma tabela hash) não 
mantém uma ordem específica.

Os elementos {1, 2, "Python", (4, 5)} foram inseridos no 
conjunto, mas a ordem em que eles aparecem na saída não 
é previsível. A ordem que você vê 1, (4, 5), 2, 'Python' pode ser 
resultado da implementação interna do conjunto ou de como o Python 
decide exibir os elementos no momento da impressão.

Portanto, não há um motivo específico para o texto "Python" ter 
ido para o final. Trata-se apenas de como o Python decidiu exibir 
os elementos no conjunto no momento da impressão, e essa ordem pode 
variar entre diferentes execuções ou versões do Python.
"""

# Tentando adicionar uma lista (que é mutável) a um conjunto resultará em um erro
try:
    conjunto.add([6, 7])
except TypeError as e:
    print(f"Erro: {e}")  # Saída: Erro: unhashable type: 'list
"""
Neste exemplo, ao tentar adicionar uma lista ao conjunto, recebemos 
um erro "unhashable type". Isso acontece porque os elementos dentro de 
um conjunto devem ser de um tipo que não pode ser alterado após serem 
criados (ou seja, imutáveis), como números, strings e tuplas. Por outro 
lado, listas e dicionários são mutáveis e, portanto, não podem ser 
adicionados a conjuntos.

Esses exemplos demonstram algumas das características fundamentais 
dos sets em Python: sua capacidade de armazenar elementos únicos e 
a exigência de que esses elementos sejam imutáveis.
"""
print()
s_chaves = {1, 2, 3, 3, 4}
print(s_chaves)  # Saída: {1, 2, 3, 4}

# Note que adicionamos o número 3 duas vezes ao conjunto acima, mas na saída ele aparece apenas uma vez.
# Isso ocorre porque os conjuntos não permitem elementos duplicados.


#Criando um conjunto usando a função set()

#2. Usando a função set():

# Criando um conjunto a partir de uma lista usando a função set()
s_funcao = set([1, 2, 3, 3, 4])
print(s_funcao)  # Saída: {1, 2, 3, 4}

print(s_chaves == s_funcao)  # Saída: True

# Como esperado, ambos os métodos produzem o mesmo resultado.
frutas_chaves = {"maçã", "banana", "cereja", "pera"}

print(frutas_chaves)
frutas_lista = ["uva", "manga", "manga", "uva", "maçã", "pera"]

print(frutas_lista)

frutas_funcao = set(frutas_lista)

print(frutas_funcao)
"""
3. Comparação:
        Verifique se os conjuntos frutas_chaves e frutas_funcao possuem 
        alguma fruta em comum. Se sim, imprima a fruta em comum. Caso contrário, 
        imprima "Os conjuntos não têm frutas em comum".
"""

interseccao = frutas_chaves.intersection(frutas_funcao)
if interseccao:
    print(f"Fruta(s) em comum: {interseccao}")
else:
    print("Os conjuntos não têm frutas em comum.")
"""
O método intersection() é um dos vários métodos disponíveis para 
conjuntos (set) em Python. Ele é usado para obter a intersecção de dois ou 
mais conjuntos, o que significa que ele retornará um novo conjunto contendo apenas 
os elementos que estão presentes em todos os conjuntos envolvidos na operação.
"""

