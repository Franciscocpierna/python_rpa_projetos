print("Operações com Conjuntos")
print()

print("\nUnião: s1 | s2 ou s1.union(s2)")
#1. Criando dois conjuntos iniciais:
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

#2. União:
#Une os elementos dos dois conjuntos, eliminando repetições.
uniao = s1 | s2
print(uniao)  # Saída: {1, 2, 3, 4, 5, 6}

print("uniao_metodo = s1.union(s2)")
# Ou usando o método union()
uniao_metodo = s1.union(s2)
print(uniao_metodo)  # Saída: {1, 2, 3, 4, 5, 6}
print("\n Intersecção interseccao = s1 & s2")
interseccao = s1 & s2
print(interseccao)  # Saída: {3, 4}

print("\nOu usando o método intersection() interseccao_method = s1.intersection(s2)")

# Ou usando o método intersection()
interseccao_method = s1.intersection(s2)
print(interseccao_method)  # Saída: {3, 4}

print("\n Diferença s1 - s2")
#Retorna os elementos que estão no primeiro conjunto, mas não no segundo.
diferenca = s1 - s2
print(diferenca)  # Saída: {1, 2}
print("\n Diferença simétrica s1 ^ s2")
# Ou usando o método difference()
diferenca_metodo = s1.difference(s2)
print(diferenca_metodo)  # Saída: {1, 2}

#Retorna os elementos que estão em um conjunto 
#ou no outro, mas não em ambos.
diferenca_simetrica = s1 ^ s2
print(diferenca_simetrica)  # Saída: {1, 2, 5, 6}

print("\n Ou usando o método symmetric_difference()")
diferenca_simetrica_metodo = s1.symmetric_difference(s2)
print(diferenca_simetrica_metodo)  # Saída: {1, 2, 5, 6}
print("\nSubset (subconjunto) is_subset = s3.issubset(s1)")
#Verifica se o primeiro conjunto é um subconjunto do segundo.
s3 = {1, 2}
is_subset = s3.issubset(s1)
print(is_subset)  # Saída: True
print("verifica se o primeiro conjunto é um superconjunto do segundo is_superset = s1.issuperset(s3)")
#Verifica se o primeiro conjunto é um superconjunto do segundo.
is_superset = s1.issuperset(s3)
print(is_superset)  # Saída: True
"""
Estes exemplos mostram o básico sobre como realizar operações 
em conjuntos em Python. Conjuntos são ferramentas poderosas, especialmente 
quando você precisa realizar operações matemáticas em grupos de dados.
"""


