# Importa a biblioteca pandas com o apelido 'opcoesPandas'
import pandas as opcoesPandas
# Importa a biblioteca numpy com o apelido 'opcoesNumpy'
import numpy as opcoesNumpy

# Cria um DataFrame com os nomes dos alunos e suas médias
notasAlunos_DF = opcoesPandas.DataFrame({
    "Nome": ["Ana", "Pedro", "João"],  # Lista com os nomes dos alunos
    "Média": [9, 7, 10]                # Lista com as médias correspondentes
})

# Exibe o DataFrame criado no console
print(notasAlunos_DF)

'''O pandas faz a correspondência entre nomes e médias utilizando o conceito de DataFrame, que funciona como uma tabela. Cada coluna tem um nome (por exemplo, "Nome" e "Média") e cada linha representa um registro, ou seja, um aluno e sua respectiva média.

coluna têm a mesma ordem, então:

"Ana" está na posição 0 da lista "Nome" e sua média (9) está na posição 0 da lista "Média".
"Pedro" está na posição 1 e sua média (7) também está na posição 1.
"João" está na posição 2 e sua média (10) está na posição 2.
Assim, pandas associa cada nome à média correspondente pela posição nas listas.'''