"""
Imutabilidade e Frozensets
        Como mencionado, os elementos de um set devem ser imutáveis. No entanto, o 
        próprio set é mutável. Se você precisar de um conjunto imutável, pode usar um frozenset.
"""

print("Imutabilidade e Frozensets dos elementos do conjunto")
#Imutabilidade dos elementos do conjunto

#Os conjuntos (set) em Python exigem que seus elementos sejam imutáveis. 
#Isso significa que você pode ter uma string, int, float ou tuple como elemento 
#de um conjunto, mas não pode ter tipos mutáveis, como list ou outro set.
# Isto é válido
conjunto_valido = {1, 2.5, "string", (10, 20)}
# Isto não é válido e causará um erro
# conjunto_invalido = {1, 2.5, "string", [10, 20]}
# conjunto_invalido2 = {1, 2, {3, 4}}
#Frozensets

#O frozenset é uma versão imutável de um conjunto Python. Uma vez que 
#você cria um frozenset, não pode mais adicionar ou remover elementos dele.

# Criando um frozenset
fs = frozenset([1, 2, 3, 4])

print(fs)  # frozenset({1, 2, 3, 4})
# Como os frozensets são imutáveis, você não pode adicionar ou remover elementos
# fs.add(5)  # Isso causará um erro
# fs.remove(1)  # Isso também causará um erro

#A principal utilidade de um frozenset é que ele pode ser usado como 
#elemento de outro conjunto, devido à sua imutabilidade:
conjunto_contendo_frozenset = {frozenset([1, 2, 3]), frozenset([4, 5, 6])}
print(conjunto_contendo_frozenset)  # {frozenset({1, 2, 3}), frozenset({4, 5, 6})}

"""
Conclusão

A imutabilidade é um conceito importante em Python, especialmente quando 
se trabalha com estruturas de dados, como conjuntos. Usar um frozenset permite ter 
um conjunto imutável, o que é útil em situações que exigem tal garantia, como quando 
se deseja usar um conjunto como elemento de outro conjunto.
"""
print()


#Solução

"""
1. Conjunto com Elementos Imutáveis:
        Crie um conjunto chamado conjunto_a contendo os seguintes elementos 
        imutáveis: 1, "Python", (10, 20).
        
        Tente adicionar uma lista [3, 4, 5] a este conjunto. O que acontece?
"""

conjunto_a = {1, "Python", (10, 20)}
print(conjunto_a)
# Ao tentar adicionar uma lista, ocorrerá um erro:
# conjunto_a.add([3, 4, 5]) 

print()

"""
2. Mutabilidade do Conjunto:
        Adicione o número 5 ao conjunto_a.
        Remova o número 1 do conjunto_a.
        Imprima o conjunto_a após essas operações.
"""

conjunto_a.add(5)
print(conjunto_a)

conjunto_a.remove(1)
print(conjunto_a)

print()


"""
3. Trabalhando com Frozensets:
        Crie dois frozensets: fs1 com os números 1, 2, 3 e fs2 com os números 4, 5, 6.
        Crie um conjunto chamado conjunto_b e adicione fs1 e fs2 a ele.
        Imprima o conjunto_b.
        Tente adicionar um novo número ao fs1. O que acontece?
"""

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6])

conjunto_b = {fs1, fs2}

print(conjunto_b)  # Saída: {frozenset({1, 2, 3}), frozenset({4, 5, 6})}
# Tentando adicionar um novo número ao fs1 resultará em um erro:
#fs1.add(7)

# 4. Resposta extra: Um frozenset é imutável, então não viola a exigência do conjunto 
# de ter apenas elementos imutáveis. Listas e conjuntos regulares são mutáveis, por isso 
# não podem ser adicionados a conjuntos.