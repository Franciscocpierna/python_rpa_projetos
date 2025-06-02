import pandas as pd

dadosFrameDados = pd.read_excel("C:\\python_projetos\\python_rpa_projetos\\pythonpandas\\exibicao\\Tratamento_Dados.xlsx")

#Imprimindo os dados
print(dadosFrameDados)

print('*'*50)
print('*'*50)   
print('*'*50)

'''


### Explicação passo a passo

1. **dadosFrameDados["Total Vendas"]**  
   Seleciona a coluna chamada "Total Vendas" do DataFrame `dadosFrameDados`. Essa coluna contém os valores de vendas, podendo ter valores ausentes (NaN).

2. **dadosFrameDados["Total Vendas"].mean()**  
   Calcula a média (média aritmética) dos valores presentes na coluna "Total Vendas", ignorando automaticamente os valores ausentes (NaN).

3. **fillna(...)**  
   O método `.fillna(valor)` substitui todos os valores ausentes (NaN) da coluna pelo valor informado. Neste caso, o valor informado é a média calculada no passo anterior.

4. **Atribuição de volta à coluna**  
   O resultado desse preenchimento é atribuído de volta à própria coluna "Total Vendas", substituindo a versão anterior.

### Resumindo

- Todos os valores ausentes (NaN) na coluna "Total Vendas" serão substituídos pela média dos valores existentes nessa coluna.
- Isso é útil para tratar dados faltantes antes de análises ou cálculos, evitando erros ou distorções.

### Exemplo ilustrativo

Suponha que a coluna "Total Vendas" tenha estes valores:

| Total Vendas |
|--------------|
| 100          |
| NaN          |
| 200          |
| NaN          |
| 300          |

A média dos valores existentes é (100 + 200 + 300) / 3 = 200.  
Após a linha de código, a coluna ficará assim:

| Total Vendas |
|--------------|
| 100          |
| 200          |
| 200          |
| 200          |
| 300          |

Assim, todos os NaN foram substituídos pela média (200).
'''
#fillna - Preenche os valores varios com a média
#mean - Média
#dadosFrameDados["Total Vendas"] = dadosFrameDados["Total Vendas"].fillna(dadosFrameDados["Total Vendas"].mean())

#Imprimindo os dados
print(dadosFrameDados)


print('*'*50)
print('*'*50)
print('*'*50)

#fillna - Preenche os valores vazios com um valor padrão
dadosFrameDados["Total Vendas"] = dadosFrameDados["Total Vendas"].fillna(500)

#Imprimindo os dados
print(dadosFrameDados)

