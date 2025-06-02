import pandas as pd

#Abre o arquivo de Vendas como DataFrame
vendasDF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendas_Merge.xlsx")

#Abre o arquivo de Vendedores como DataFrame
vendedoresDF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Vendedores_Merge.xlsx")

#Abre o arquivo de Produtos como DataFrame
produtosDF = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Produtos_Merge.xlsx")

#Imprimindo os dados
print(produtosDF)

print('*'*50)
print('*'*50)   
print('*'*50)
'''
 realiza uma junção (merge) entre dois DataFrames do pandas: vendasDF e vendedoresDF.

O que é um merge no pandas?
O método .merge() serve para combinar/juntar dois DataFrames com base em uma ou mais colunas que eles têm em comum (chave primária/estrangeira, como em bancos de dados relacionais).

Por padrão, o pandas tenta encontrar colunas com o mesmo nome nos dois DataFrames e faz a junção usando essas colunas.

Exemplo prático
Suponha que você tenha os seguintes DataFrames:

vendasDF:

id_venda	id_vendedor	valor
1	101	500
2	102	300
vendedoresDF:

id_vendedor	nome_vendedor
101	Ana
102	João
Ao executar:

O pandas irá procurar a coluna em comum (id_vendedor) e juntar as informações, resultando em:

id_venda	id_vendedor	valor	nome_vendedor
1	101	500	Ana
2	102	300	João
Observações importantes
Se houver mais de uma coluna em comum, todas serão usadas como chave, a menos que você especifique com o parâmetro on.
Você pode controlar o tipo de junção (inner, left, right, outer) usando o parâmetro how. O padrão é inner (apenas registros que existem nos dois DataFrames).
Exemplo especificando a chave:
Exemplo de junção à esquerda:
Resumo:
O comando faz a junção dos dados de vendas com os dados dos vendedores, agregando informações dos vendedores às vendas, usando as colunas em comum como referência.

'''
#merge - Uniu através de um denominador em comum
vendasDF = vendasDF.merge(vendedoresDF)

#Imprimindo os dados
print(vendasDF)