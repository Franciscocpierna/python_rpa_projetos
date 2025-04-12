"""
11. Crie uma lista de listas que contenha o nome de alunos e suas 
notas (exemplo: [["João", 8, 7, 9], ["Ana", 10, 9, 8]]). 

Calcule e exiba a média de cada aluno e a lista ordenada 
pela média, de forma decrescente.

Objetivo: Trabalhar com listas aninhadas, calcular médias e realizar 
ordenação com base em critérios.
"""

# Cria uma lista de listas, onde cada sublista contém o nome 
        # de um aluno seguido por suas notas.
alunos = [["João", 8, 7, 9], ["Ana", 10, 9, 8], ["Paulo", 6, 5, 7], ["Clara", 9, 8, 10]]

# Calcula a média de cada aluno
for aluno in alunos:
    
    # 'aluno[1:]' acessa as notas do aluno na lista (ignorando o nome), 
            # e 'sum(aluno[1:])' soma essas notas.
    # 'len(aluno[1:])' conta quantas notas existem. A divisão 
            # desses dois valores calcula a média.
    media = sum(aluno[1:]) / len(aluno[1:])
    
    # Adiciona a média calculada ao final da sublista do aluno.
    # Isso expande a lista original do aluno para incluir sua 
            # média como último elemento.
    aluno.append(media)

# Ordena a lista 'alunos' pela média, que é agora o quinto 
        # elemento de cada sublista (índice 4),
# utilizando a função 'sorted()'. O parâmetro 'key=lambda x: x[4]' 
        # especifica que a ordenação deve
        # usar o quinto elemento das sublistas como chave de ordenação.
# 'reverse=True' especifica que a ordenação deve ser 
        # feita em ordem decrescente.
alunos_ordenados = sorted(alunos, key=lambda x: x[4], reverse=True)
print("Lista de alunos ordenada por média:")
# Exibe a lista de alunos ordenada por média.   
# A lista 'alunos_ordenados' contém as sublistas dos alunos 
        # ordenadas pela média calculada.
print(alunos_ordenados)

# Exibe os resultados de forma formatada
# Itera sobre a lista 'alunos_ordenados' e imprime o 
        # nome do aluno e sua média.
for aluno in alunos_ordenados:
    print(f"Aluno: {aluno[0]} - Média: {aluno[4]}")