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
'''notasAluno_DataFrame: É o DataFrame criado anteriormente, que contém as notas dos alunos.
.loc[1, "Nota 2"]: O método .loc é usado para acessar um valor específico no DataFrame. Aqui, ele seleciona a linha de índice 1 (ou seja, o segundo aluno, "Pedro") e a coluna "Nota 2".
= 50: Atribui o valor 50 para a célula selecionada.
Resumo:
Essa linha altera a nota da "Nota 2" do aluno "Pedro" (linha de índice 1) para 50. Isso sobrescreve o valor anterior (que era 9) por 50.'''

#loc = localizar
notasAluno_DataFrame.loc[1, "Nota 2"] = 50

#Substituiu a coluna Média pela nota coluna Média
notasAluno_DataFrame["Média"] = (notasAluno_DataFrame["Nota 1"] + notasAluno_DataFrame["Nota 2"] + notasAluno_DataFrame["Nota 3"] + notasAluno_DataFrame["Nota 4"]) / 4

print(notasAluno_DataFrame)