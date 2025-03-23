"""
Iterando Sobre Dicionários
        Usando loops for
        Iterando sobre chaves, valores e itens
"""
print("Iterando Sobre Dicionários")

#Exemplo Prático:

#Imagine que temos um dicionário que representa as notas de um aluno
#em diferentes matérias. Queremos iterar sobre esse dicionário para 
#exibir as matérias, as notas e também calcular a média das notas.

# Definindo um dicionário chamado 'notas' que armazena 
# as notas do aluno em diferentes matérias
notas = {
    "Matemática": 8.5,  # Matemática: 8.5
    "Português": 9.0,   # Português: 9.0
    "História": 7.5,    # História: 7.5
    "Geografia": 8.0,   # Geografia: 8.0
    "Química": 9.5      # Química: 9.5
}
for materia,nota in notas.items():
    print(f"a materia: {materia} com nota: {nota}")

media_das_notas=0    
for nota in notas.values():
     media_das_notas +=nota 
media_das_notas=media_das_notas/len(notas)             
print(f"\nnumero de materia são {len(notas)} e a média é {media_das_notas}") 


print("Matérias cursadas pelo aluno:")

# Usando um loop 'for' para iterar sobre as chaves do 
#dicionário 'notas' (por padrão, a iteração é feita sobre as chaves)
for materia in notas:
    print(materia)
    
# Outra forma de iterar sobre as chaves de um 
# dicionário é usar o método .keys()

# Imprimindo um cabeçalho para identificar a nova seção de saída
print("\nMatérias (usando .keys()):")

# Iterando sobre as chaves do dicionário 'notas' usando o 
#método .keys() e imprimindo cada chave
for materia in notas.keys():
    print(materia)


   
'''
Exercício sobre Iterando Sobre Dicionários

Objetivo: Você tem um dicionário que representa o número de livros vendidos 
em uma livraria em diferentes meses. Sua tarefa é iterar sobre esse dicionário 
para realizar diferentes análises.

Instruções:

    1. Iterando sobre as chaves (meses):
        - Imprima todos os meses em que a livraria registrou vendas.

    2. Iterando apenas sobre os valores (número de livros vendidos):
        - Calcule e imprima a venda total nos 5 meses.
        - Determine e imprima o mês com as vendas mais baixas.

    3. Iterando sobre chaves e valores simultaneamente (itens):
        - Para cada mês, imprima uma mensagem no seguinte 
        formato: "Em [mês], [número] livros foram vendidos".
        


Dicionário fornecido:
'''
vendas = {
    "Janeiro": 120,
    "Fevereiro": 150,
    "Março": 80,
    "Abril": 190,
    "Maio": 210
}

for venda in vendas.keys():
     print(f"mes {venda}")
     
for venda in vendas.values():
     print(f"vendidos {venda}")     
     
for mes,numero in vendas.items():     
     print(f"Em mês {mes}, número {numero} livros foram vendidos")     
     
# Itera através das chaves do dicionário 'vendas' (que são os meses)
for mes in vendas:
    
    # Imprime o nome do mês
    print(mes)


# 2. Iterando sobre valores

#- Calcule e imprima a venda total nos 5 meses.
#- Determine e imprima o mês com as vendas mais baixas.

print("\n2. Iterando sobre valores")
total_vendas = 0
vendas_mais_baixas = float('inf')
print("\nvendas_mais_baixas = float('inf')",vendas_mais_baixas)
mes_vendas_mais_baixas = ""
print(f"\nvendas_mais_baixas = {mes_vendas_mais_baixas}")
print(type(vendas_mais_baixas))  # Isso mostrará <class 'float'>

# Para cada 'venda' dentro dos valores do dicionário 'vendas'
for venda in vendas.values():
    
    # Adiciona o valor da venda atual ao total de vendas
    total_vendas += venda
    
    # Verifica se a venda atual é menor do que o valor armazenado em 'vendas_mais_baixas'
    if venda < vendas_mais_baixas:
        
        # Se for, atualiza 'vendas_mais_baixas' com o valor da venda atual
        vendas_mais_baixas = venda


# Para cada par 'mes' e 'venda' no dicionário 'vendas'
for mes, venda in vendas.items():
    
    # Verifica se a venda atual é igual ao valor mais baixo registrado
    if venda == vendas_mais_baixas:
        
        # Se for, armazena o mês correspondente em 'mes_vendas_mais_baixas'
        mes_vendas_mais_baixas = mes
        
        # Encerra o loop (não precisa continuar a busca)
        break     
    
print("\nTotal de livros vendidos:", total_vendas)
print(f"Mês com as vendas mais baixas: {mes_vendas_mais_baixas} com {vendas_mais_baixas} livros vendidos.") 
# 3. Iterando sobre chaves e valores simultaneamente
print("\n3. Iterando sobre chaves e valores simultaneamente")
print("\nResumo das vendas:")

# Para cada par 'mes' e 'venda' no dicionário 'vendas'
for mes, venda in vendas.items():
    
    # Imprime uma mensagem formatada com o mês e a quantidade de livros vendidos
    print(f"Em {mes}, {venda} livros foram vendidos.")