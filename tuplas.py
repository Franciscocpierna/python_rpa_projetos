dimensoes_bagagem = (55, 35, 25)
itens_proibidos = ["líquidos acima de 100ml", "objetos cortantes", "material explosivo"]
regras_bagagem = (dimensoes_bagagem, itens_proibidos)

# que uma nova regra seja implementada e agora é proibido transportar 
#baterias de lítio na bagagem de mão. Mesmo que a tupla regras_bagagem 
#seja imutável, o elemento itens_proibidos é uma lista, que é mutável. 

#Portanto, você pode adicionar à lista:

regras_bagagem[1].append("baterias de lítio")
print(regras_bagagem[1])
contato = ("João Silva", "123-456-7890", "joao.silva@email.com")
armazena = contato[1:3]
print(armazena)
nova = contato[:2]
print(nova)

print("tuplas sao imutáveis")

dimensoes_bagagem = (55, 35, 25)

#Agora, por alguma razão, você decide tentar alterar a altura máxima permitida:
# Isto causará um erro!

#dimensoes_bagagem[0] = 60

dimensoes_bagagem = (55,[1,2], 25)
print(dimensoes_bagagem)
dimensoes_bagagem[1].append(7) 
print(dimensoes_bagagem)#como lista é mutável (55.[1,2,7],25])

"""
Operações com Tuplas:
        Concatenação: (1, 2) + (3, 4)
        Repetição: (1, 2) * 3
        Verificar se um elemento está na tupla: 2 in (1, 2, 3)
"""

tuplas1=(1,2) + (3,4)#concatena (1,2,3,4)
print(tuplas1)
tuplas1=(1, 2) * 3 #(1, 2, 1, 2, 1, 2)
print(tuplas1)
print(2 in (1, 2, 3))
if 2 in tuplas1:
    print(tuplas1)
for x in tuplas1:
    print(x) 
    
"""
Métodos de Tuplas:
        count(): conta o número de vezes que um elemento aparece na tupla.
        index(): retorna o índice do primeiro elemento que corresponde ao valor especificado.
"""    
print("Métodos de Tuplas:")
tuplas2=(2,3,3,3,4,5,6,2)
tuplas3=tuplas2.count(3)
print(tuplas3)
print(tuplas2.index(6))

print("Desempacotamento de Tuplas")
a, b, c = (1, 2, 3)
print("a, b, c = (1, 2, 3) a,b,c = ",a,b,c)
estudante_info = ("João", 20, 85.5) # onde "João" é o nome do estudante, 20 
                                    #é sua idade e 85.5 é sua nota média.
print(estudante_info)                                    
print(f"o nome é {estudante_info[0]} idade {estudante_info[1]} sua nota {estudante_info[2]} ")                                    


nome, idade, nota_media = estudante_info

print(f"\nNome do Estudante: {nome}")
print(f"Idade: {idade}")
print(f"Nota Média: {nota_media}")

# Dados fornecidos
pacote_viagem = ("Paris", 5, 1500)

# Desempacotamento da tupla
destino, noites, preco = pacote_viagem

# Imprimir as informações do pacote
print(f"\na) Destino: {destino}")
print(f"a) Número de Noites: {noites}")
print(f"a) Preço: R$ {preco}")

#1. Retornando múltiplos valores de uma função usando tuplas

#Você quer criar uma função que retorna o total vendido e o produto mais vendido do dia.
def analisar_vendas(vendas_A, vendas_B):
    
    total_vendido = vendas_A + vendas_B
    mais_vendido = "A" if vendas_A > vendas_B else "B"
    return total_vendido, mais_vendido

total, top_produto = analisar_vendas(100, 85)
print(f"Total Vendido: {total}")
print(f"Produto Mais Vendido: {top_produto}")

print()
#Suponha que você tenha uma lista de vendas de ambos os produtos em 
#pares para alguns dias, e você quer imprimir as vendas de cada dia.
vendas = [(100, 90), (110, 115), (105, 100)]

for vendas_A, vendas_B in vendas:
    print(f"Vendas de A: {vendas_A}, Vendas de B: {vendas_B}")
    
print()

print("3. Trocando valores entre duas variáveis")

#No final do dia, você percebeu que confundiu as vendas dos 
#produtos A e B e precisa trocar os valores para corrigir.
vendas_A = 100
vendas_B = 85
vendas_A, vendas_B = vendas_B, vendas_A

print("vendas_A, vendas_B = vendas_B, vendas_A")
print(f"\nVendas Corrigidas - A: {vendas_A}, B: {vendas_B}")

print("\n1. Retornando múltiplos valores de uma função usando tuplas.")

def resumo_vendas(vendas_smartphones, vendas_smartwatches):
    
    total_vendas = vendas_smartphones + vendas_smartwatches
    mais_vendido = "smartphone" if vendas_smartphones > vendas_smartwatches else "smartwatch"
    

    return total_vendas, mais_vendido


total, top_produto = resumo_vendas(80, 70)

print(f"Total de Vendas: {total}")
print(f"Produto Mais Vendido: {top_produto}")

print()

print("2. Uso de tuplas em loops for.")

vendas_semana = [(70, 65), (80, 82), (90, 88)]

for smartphones, smartwatches in vendas_semana:
    print(f"Vendas de smartphones: {smartphones}, Vendas de smartwatches: {smartwatches}")
    
print()
print("3. Trocando valores entre duas variáveis.")

vendas_segunda = (65, 70)

print("utiliza um recurso do Python chamado fatiamento (slicing).vendas_segunda = (65, 70)") 
print("Especificamente, o [::-1] é um atalho para inverter a ordem vendas_segunda = (65, 70)") 
#elementos dentro de uma sequência (que pode ser uma lista, string, tupla, etc.).
vendas_segunda = vendas_segunda[::-1]

print(f"Vendas corrigidas de segunda-feira - Smartphones: {vendas_segunda[0]}, Smartwatches: {vendas_segunda[1]}")

"""
Comparando Tuplas:
        Tuplas podem ser comparadas usando operadores de comparação: (1, 2) < (1, 3)
"""

"""
Exemplo Prático: Comparando Tuplas

No Python, quando duas tuplas são comparadas, a comparação é realizada 
elemento por elemento, começando pelo primeiro. Assim que um par de 
elementos é encontrado onde um é menor (ou maior) que o outro, a comparação 
retorna True ou False e não prossegue para os próximos elementos. 

Se todos os elementos comparados forem iguais e uma das tuplas for mais curta 
que a outra, a tupla mais curta é considerada menor.

Aqui estão alguns exemplos para ilustrar isso:
"""
print("\n",(1, 2) < (1, 3))

print((1, 2) == (1, 2)) 

print("1. Comparando o Primeiro Elemento:")
t1 = (1, 2)
t2 = (1, 3)
print(t1 < t2)  # Isso imprimirá True, porque 2 (de t1) é menor que 3 (de t2).
#2. Ignorando Elementos Iguais:
t1 = (1, 2, 3)
t2 = (1, 2, 4)
print(t1 < t2)  # Isso imprimirá True, porque, apesar de 1 e 2 
                #serem iguais em ambas as tuplas, 3 (de t1) é menor que 4 (de t2).
print("\n3. Comparando Tuplas de Diferentes tamanhos: t1 = (1, 2) e t2 = (1, 2, 3)")
t1 = (1, 2)
t2 = (1, 2, 3)
print(t1 < t2)  # Isso imprimirá True, porque t1 é mais curta 
                #que t2, mesmo que todos os seus elementos correspondentes sejam iguais.
                #  Isso imprimirá True, porque t1 é mais curta
print()                
t1 = (1, "apple")
t2 = (2, "banana")
print(t1 < t2)  # Isso imprimirá True porque 1 é menor que 2
t1=("apple",) 
t2=("banana",)
print(t1<t2)             
                
t1 = (3, 5)
t2 = (3, 4, 10)
t3 = (3, 6)
t4 = (2, 100)
t5 = (3, 5)
print()
print(t1>t2)#False
print(t3>t2)#true
print(t5==t1)# true
print(t4<t1)#true
