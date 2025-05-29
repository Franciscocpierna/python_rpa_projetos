import pandas as opcoesPanda

notasAluno_DataFrame = opcoesPanda.DataFrame({
    "Nome": ["Ana", "Pedro", "João"],
    "Nota 1": [9, 7, 10],
    "Nota 2": [6, 9, 8],
    "Nota 3": [7, 5, 10],
    "Nota 4": [10, 10, 6]
})

''' Detalhamento:

notasAluno_DataFrame["Nota 1"], ["Nota 2"], etc.: acessam as colunas das notas no DataFrame, retornando uma série (coluna) para cada aluno.
Os valores dessas quatro colunas são somados elemento a elemento (linha a linha).
O resultado da soma é dividido por 4, calculando a média aritmética das quatro notas para cada aluno.
O resultado final é uma nova coluna chamada "Média" adicionada ao DataFrame, contendo a média das notas de cada aluno.
Exemplo prático: Se um aluno tem as notas 9, 6, 7 e 10, a média será (9+6+7+10)/4 = 8.0. Essa média será armazenada na coluna "Média" correspondente a esse aluno.'''

#Adicionando nova coluna e calculando a média
notasAluno_DataFrame["Média"] = (notasAluno_DataFrame["Nota 1"] + notasAluno_DataFrame["Nota 2"] + notasAluno_DataFrame["Nota 3"] + notasAluno_DataFrame["Nota 4"]) / 4

print(notasAluno_DataFrame)