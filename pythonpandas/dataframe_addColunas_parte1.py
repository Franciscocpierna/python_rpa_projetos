# Importa a biblioteca pandas com o apelido 'opcoesPanda'
import pandas as opcoesPanda

# Cria um DataFrame com os nomes dos alunos e suas notas em 4 avaliações
notasAluno_DataFrame = opcoesPanda.DataFrame({
    "Nome": ["Ana", "Pedro", "João"],      # Lista com os nomes dos alunos
    "Nota 1": [9, 7, 10],                  # Notas da primeira avaliação
    "Nota 2": [6, 9, 8],                   # Notas da segunda avaliação
    "Nota 3": [7, 5, 10],                  # Notas da terceira avaliação
    "Nota 4": [10, 10, 6]                  # Notas da quarta avaliação
})

# Exibe o DataFrame criado no console
print(notasAluno_DataFrame)