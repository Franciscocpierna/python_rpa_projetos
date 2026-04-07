import plotly.express as px
import plotly.io as pio
import os
import pandas as pd
import plotly.express as px
import tempfile
import webbrowser
data = pd.read_csv("dataset/train.csv")

print(data.head())
print()
print()
data.head()

#5 últimos
print(data.tail())
#informação sobre tipo
#data.info()
print("#"*50)
### Verificando se existem valores nulos no dataset
#
# A verificação de valores nulos é um dos primeiros passos no processo de análise dos dados. Neste passo verificamos a integridade dos dados e se existem muitos registros e colunas sem informações.
print(data.isnull().sum())
print("#"*50)
# ### Verificação do balanceamento das informações com relação a coluna objetivo: "Credit_Score"
print(data["Credit_Score"].value_counts())
# --- CONFIGURAÇÃO DE SEGURANÇA ---
# Em vez de depender do servidor local (127.0.0.1) que causa ERR_CONNECTION_REFUSED,
# vamos salvar o gráfico como um arquivo temporário e abri-lo.

def mostrar_grafico_estavel(fig, nome_arquivo="temp_plot"):
    # 1. Cria um caminho para um arquivo HTML na pasta temporária do Windows
    temp_dir = tempfile.gettempdir()
    caminho_arquivo = os.path.join(temp_dir, f"{nome_arquivo}.html")
    
    # 2. Salva o gráfico como HTML (contém todo o JavaScript necessário dentro dele)
    fig.write_html(caminho_arquivo)
    
    # 3. Abre o arquivo diretamente no navegador padrão
    # Isso usa o protocolo 'file://' em vez de 'http://', eliminando erros de conexão
    webbrowser.open(f"file://{caminho_arquivo}")
    print(f"Gráfico gerado em: {caminho_arquivo}")

### Conhecendo as relações que existem no dataset
# O conjunto de dados tem muitos recursos que podem treinar um modelo de aprendizado de máquina para classificação de pontuação de crédito. Vamos explorar todos os recursos um por um.
# Vamos começar explorando o recurso de ocupação (occupation) para saber se a ocupação da pessoa afeta a pontuação de crédito:
#pio.renderers.default = "browser"


print("#"*50)
fig = px.box(data, 
             x="Occupation",  
             color="Credit_Score", 
             title="Score de Crédito baseado na Ocupação", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
#fig.show()
#pio.show(fig, renderer="browser")
#fig.show(renderer="browser")
mostrar_grafico_estavel(fig)

# Assim como a renda anual, quanto mais salário mensal você ganhar, melhor será sua pontuação de crédito. 
# Agora vamos ver se ter mais contas bancárias impacta a pontuação de crédito ou não:

fig = px.box(data, 
             x="Credit_Score", 
             y="Num_Bank_Accounts", 
             color="Credit_Score",
             title="Score de Crédito baseado no Número de Contas Bancárias", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
mostrar_grafico_estavel(fig)
# De acordo com a visualização acima, quanto mais você ganha anualmente, melhor é sua pontuação de crédito. 
# Agora vamos explorar se o salário mensal líquido (in-hand) afeta as pontuações de crédito ou não:

fig = px.box(data, 
             x="Credit_Score", 
             y="Monthly_Inhand_Salary", 
             color="Credit_Score",
             title="Score de Crédito baseado no Salário Líquido Mensal", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
mostrar_grafico_estavel(fig)

# Assim como a renda anual, quanto mais salário mensal você ganhar, melhor será sua pontuação de crédito. 
# Agora vamos ver se ter mais contas bancárias impacta a pontuação de crédito ou não:

fig = px.box(data, 
             x="Credit_Score", 
             y="Num_Bank_Accounts", 
             color="Credit_Score",
             title="Score de Crédito baseado no Número de Contas Bancárias", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
mostrar_grafico_estavel(fig)

# Manter mais de cinco contas não é bom para ter uma boa pontuação de crédito. 
# Uma pessoa deve ter apenas 2 a 3 contas bancárias. Portanto, ter mais contas bancárias não afeta positivamente a pontuação de crédito. 

# Agora vamos ver o impacto nas pontuações de crédito com base no número de cartões de crédito que você possui:

fig = px.box(data, 
             x="Credit_Score", 
             y="Num_Credit_Card", 
             color="Credit_Score",
             title="Score de Crédito Baseado no Número de Cartões de Crédito", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
#pio.show(fig, renderer="browser")
#fig.show(renderer="browser")
mostrar_grafico_estavel(fig)

# Assim como o número de contas bancárias, ter mais cartões de crédito não afetará positivamente sua pontuação de crédito. 
# Ter de 3 a 5 cartões de crédito é bom para sua pontuação de crédito. 

# Agora vamos ver o impacto nas pontuações de crédito com base em quanto você paga de juros médios em empréstimos e EMIs (total da prestação mensal de cada pessoa):
fig = px.box(data, 
             x="Credit_Score", 
             y="Interest_Rate", 
             color="Credit_Score",
             title="Score de Crédito Baseado nas Taxas de Juros Médios", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
#pio.show(fig, renderer="browser")
mostrar_grafico_estavel(fig)

# Se a taxa média de juros for de 4 a 11%, a pontuação de crédito é boa. 
# Ter uma taxa de juros média de mais de 15% é ruim para sua pontuação de crédito. 

# Agora vamos ver quantos empréstimos você pode tomar por vez para uma boa pontuação de crédito:

fig = px.box(data, 
             x="Credit_Score", 
             y="Num_of_Loan", 
             color="Credit_Score", 
             title="Score de Crédito baseado no número de Emprestimos Tomados por Pessoa",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()


# EM VEZ DE fig.show(), use a nossa nova função:
mostrar_grafico_estavel(fig)


# Para ter uma boa pontuação de crédito, você não deve fazer mais de 1 a 3 empréstimos por vez. 
# Ter mais de três empréstimos por vez afetará negativamente sua pontuação de crédito. 

# Agora vamos ver se atrasar os pagamentos na data de vencimento afeta sua pontuação de crédito ou não:

fig = px.box(data, 
             x="Credit_Score", 
             y="Delay_from_due_date", 
             color="Credit_Score",
             title="Score de Crédito baseado na média de números de dias atrasado no pagamentos de Cartão de Crédito", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
mostrar_grafico_estavel(fig)

# Assim, você pode atrasar o pagamento do cartão de crédito de 5 a 14 dias a partir da data de vencimento. 
# Atrasar seus pagamentos por mais de 17 dias a partir da data de vencimento afetará negativamente sua pontuação de crédito. 

# Agora vamos dar uma olhada se os atrasos frequentes nos pagamentos afetarão as pontuações de crédito ou não:

fig = px.box(data, 
             x="Credit_Score", 
             y="Num_of_Delayed_Payment", 
             color="Credit_Score", 
             title="Score de Crédito Baseado no Número de Pagamentos Atrasados",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
mostrar_grafico_estavel(fig)

# Portanto, atrasar de 4 a 12 pagamentos a partir da data de vencimento não afetará sua pontuação de crédito. 
# Mas atrasar mais de 12 pagamentos a partir da data de vencimento afetará negativamente sua pontuação de crédito. 

# Agora vamos ver se ter mais dívidas afetará a pontuação de crédito ou não:

fig = px.box(data, 
             x="Credit_Score", 
             y="Outstanding_Debt", 
             color="Credit_Score", 
             title="Score de Crédito Baseado em Débitos Pendentes",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
mostrar_grafico_estavel(fig)

# Uma dívida pendente de $ 380 – $ 1150 não afetará sua pontuação de crédito. 
# Mas sempre ter uma dívida de mais de $ 1338 afetará negativamente sua pontuação de crédito. 

# Agora vamos ver se ter um alto índice de utilização de crédito afetará as pontuações de crédito ou não:

fig = px.box(data, 
             x="Credit_Score", 
             y="Credit_Utilization_Ratio", 
             color="Credit_Score",
             title="Score de Crédito Baseado no Índice de Utilização de Crédito", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
mostrar_grafico_estavel(fig)

# Taxa de utilização de crédito significa sua dívida total dividida pelo crédito total disponível.  
# De acordo com a figura acima, sua taxa de utilização de crédito não afeta sua pontuação de crédito. 

# Agora vamos ver como a idade do histórico de crédito de uma pessoa afeta as pontuações de crédito:

fig = px.box(data, 
             x="Credit_Score", 
             y="Credit_History_Age", 
             color="Credit_Score", 
             title="Score de Crédito Baseado na Idade do Histórico de Crédito",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
mostrar_grafico_estavel(fig)

# Portanto, ter um longo histórico de crédito resulta em melhores pontuações de crédito.

# Agora vamos ver se ter um valor baixo no final do mês afeta a pontuação de crédito ou não:

fig = px.box(data, 
             x="Credit_Score", 
             y="Monthly_Balance", 
             color="Credit_Score", 
             title="Score de Crédito Baseado no Valor Restante no Final do Mês",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
#fig.show()
mostrar_grafico_estavel(fig)

# Portanto, ter um saldo mensal alto em sua conta no final do mês é bom para sua pontuação de crédito. 
# Um saldo mensal inferior a US $ 250 é ruim para a pontuação de crédito.

#Mapa de Correlação

#Fazendo uma cópia dos dados
dados = data.copy()

# Adequação dos dados para mostrar o mapa de correlação
numeric_columns = data.select_dtypes(include=['float64', 'int64'])

# Calcular a correlação de Spearman
spearman_corr = numeric_columns.corr(method='spearman')
print(spearman_corr)

plt.figure(figsize=(21,21))

sns.heatmap(spearman_corr, annot=True)


## Modelo de Classificação de Pontuação de Crédito

# Depois de analisar....

# Mais um recurso importante (mix de crédito) no conjunto de dados é valioso para determinar pontuações de crédito.
# O recurso mix de crédito informa sobre os tipos de créditos e empréstimos que você tomou.

# Como a coluna Credit_Mix é categórica, vou transformá-la em um recurso numérico para que possamos 
# usá-la para treinar um modelo de Machine Learning para a tarefa de classificação de pontuação de crédito:


### Transformação de dados
#Transformação de uma coluna categógica em numérica

data["Credit_Mix"] = data["Credit_Mix"].map({"Standard": 1, 
                               "Good": 2, 
                               "Bad": 0})


# Agora vou dividir os dados em recursos e rótulos selecionando os recursos 
# que consideramos importantes para nosso modelo:

x = np.array(data[["Annual_Income", "Monthly_Inhand_Salary", 
                   "Num_Bank_Accounts", "Num_Credit_Card", 
                   "Interest_Rate", "Num_of_Loan", 
                   "Delay_from_due_date", "Num_of_Delayed_Payment", 
                   "Credit_Mix", "Outstanding_Debt", 
                   "Credit_History_Age", "Monthly_Balance"]])
y = np.array(data["Credit_Score"])


# Agora, vamos dividir os dados em conjuntos de treinamento e teste e continuar treinando 
# um modelo de classificação de pontuação de crédito:

#dividindo a base em treinamento e teste. Teste ocupará 33% da base (aleatoriamente)
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                    test_size=0.33, 
                                                    random_state=42)

#Instanciando o Classificador do Random Forest no objeto model
model = RandomForestClassifier()

#Realizando a classificação, passando como parâmetro a base de treinamento x e y
model.fit(xtrain, ytrain)



# Fazer previsões usando o modelo nos dados de teste
ypred = model.predict(xtest)

# Calcular a acurácia comparando as previsões com os valores reais
accuracy = accuracy_score(ytest, ypred)*100

print(f"Acurácia do modelo: {accuracy:5.2f}%")


print("Credit Score Prediction : ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))

features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
print("Predicted Credit Score = ", model.predict(features))

