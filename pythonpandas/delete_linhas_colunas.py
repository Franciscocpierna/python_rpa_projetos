#
import pandas as opcoesPandas

#Configurando / abrindo o arquivo
dataFrameDados = opcoesPandas.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Deletar_Linhas_Colunas.xlsx")

print(dataFrameDados)

print()
print()
print()

#dropna - Deleta linhas que tem pelo menos um valor em branco
deletandoLinhasEmBranco = dataFrameDados.dropna()

print(deletandoLinhasEmBranco)

print()
print()
print()
#del - Deleta a coluna que especificarmos
#del deletandoLinhasEmBranco["Produto"]
#print(deletandoLinhasEmBranco)

#drop - Deletamos uma ou mais colunas
deletarDuasColunas = deletandoLinhasEmBranco.drop(columns=["Produto", "Data Venda"])

print(deletarDuasColunas)
print()
print()
print()

'''drop(2, axis=0): O método drop remove elementos do DataFrame.
O primeiro argumento (2) indica o índice da linha a ser removida (no caso, a linha de índice 2).
axis=0 especifica que a remoção será feita em linhas (não em colunas).
Resultado: Cria um novo DataFrame chamado exluirLinha3, igual ao anterior, mas sem a linha de índice 2.'''

#axis - eixo(1 - coluna, 0 - linha)
#drop - deletar
exluirLinha3 = deletarDuasColunas.drop(2, axis=0)
'''Remove as linhas de índice 0 e 1 do DataFrame exluirLinha3.
Não é necessário passar axis=0 porque, por padrão, o drop remove linhas.
Resultado: Agora, exluirLinha3 é um DataFrame sem as linhas de índice 0, 1 e 2 (essas três linhas foram removidas).'''
exluirLinha3 = exluirLinha3.drop([0, 1])

print(exluirLinha3)
