import pandas as opcoesPanda

notasAluno_DataFrame = opcoesPanda.DataFrame({
    "Nome": ["Ana", "Pedro", "João"],
    "Nota 1": [9, 7, 10],
    "Nota 2": [6, 9, 8],
    "Nota 3": [7, 5, 10],
    "Nota 4": [10, 10, 6]
})

#Adicionando nova coluna e calculando a média
notasAluno_DataFrame["Média"] = (notasAluno_DataFrame["Nota 1"] + notasAluno_DataFrame["Nota 2"] + notasAluno_DataFrame["Nota 3"] + notasAluno_DataFrame["Nota 4"]) / 4

#Coluna com faltas
novaColunaFaltas = [2, 5, 3]

#Criando uma coluna com o valor padrão
notasAluno_DataFrame["Faltas"] = novaColunaFaltas


print(notasAluno_DataFrame)