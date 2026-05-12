# Os nossos pacotes tradicionais
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Os pacotes para normalização e preparação dos dados
import sklearn  #para identificação da versão
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from sklearn.model_selection import train_test_split

# Os pacotes destinados a aprendizagem de máquina (algoritmos)
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# Importando o método SMOTE da biblioteca imblearn
from imblearn.over_sampling import SMOTE

# Dentro da biblioteca <'imbalanced-learn'> existe um método <'SMOTE'> que significa: Synthetic Minority Over-sampling Technique. 
# Ou seja... O SMOTE é uma técnica de oversampling que cria novas instâncias sintéticas da classe minoritária no conjunto de dados,
# a fim de balancear a distribuição das classes.

# Os pacotes destinados a report de métricas dos modelos
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix, accuracy_score, classification_report

# para evitar mensagens de alerta/warnings.
import warnings
warnings.filterwarnings("ignore")

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *

# Importação do dataset
brca = pd.read_csv("dados/BRCA.csv")

# Visualização do cabeçalho dos dados


print(brca.head())

print('#'*100)
# verificando se existe algum valor nulo
calcular_porcentagem_valores_ausentes(brca)
# Exibindo o relatório de valores nulos por coluna
relatorio_valores_ausentes_por_coluna(brca)
print()

print('#'*100)
# limpando esses últims 4 valores nulos
brca.dropna(subset='Date_of_Last_Visit', inplace = True)
# verificando se existe algum valor nulo
calcular_porcentagem_valores_ausentes(brca)
print()

print('#'*100)
# Exibindo o relatório de valores nulos por coluna
relatorio_valores_ausentes_por_coluna(brca)
# Vamos obter as informações do dataset

print(brca.info())

print('#'*100)
# Vamos fazer uma verificação se existem apenas mulheres na base de dados

print(brca['Gender'].value_counts())

brca['Age'].hist(bins = 50, grid = False)
plt.xlabel(xlabel = "Age")
plt.ylabel(ylabel = "Count")
plt.title("Age Distribution of BRCA Patients")
plt.show()

print('#'*100)
#Vamos verificar agora a classificação única de tipo de câncer de mama nos pacientes
brca['Histology'].unique()

def plot_pie_chart(column, title):
    # define Seaborn color palette to use
    palette_color = sns.color_palette('bright')
  
    # plotting data on chart
    plt.pie(brca[column].value_counts(), labels=brca[column].unique(), colors=palette_color, autopct='%.0f%%')

    plt.title(title)
    # displaying chart
    plt.show()

plot_pie_chart("Histology", "Carincoma Classifications in Patient Dataset")    

# Vamos verificar agora uma distribuição por estágio, sabendo-se que o estágio I é o inicial e o estágio III o mais avançado.
plot_pie_chart("Tumour_Stage", "Tumour Stage Classifications in Patient Dataset")

#Vamos agora identificar no dataset a distribuição da variável alvo (Patient Status)

# Identificando a variável alvo para o modelo de predição (duas categorias: vivo (alive) ou morto (Dead))
plot_pie_chart("Patient_Status", "Patient Status (Target) in Patient Dataset")

print()
# Fazendo uma cópia do dataset original e detetando os atributos que não são representativos
brca_processed = brca.copy().drop(columns=['Patient_ID', 'Surgery_type', 'Gender', 'ER status', 'PR status'])
# Encode da coluna objetivo (target feature) para valor numérico (inteiro) para o processo de classificação
le = LabelEncoder()
brca_processed['Patient_Status_le'], brca_processed['HER2_Status_le'] = le.fit_transform(brca_processed['Patient_Status']), le.fit_transform(brca_processed['HER2 status'])

# Encode de valores ordinais para o estágio do tumor: categorico para numerico
oe = OrdinalEncoder(dtype=int)
brca_processed['Tumour_Stage_oe'] = oe.fit_transform(np.array(brca_processed['Tumour_Stage']).reshape(-1,1))
brca_processed.drop(columns=['Tumour_Stage', 'Date_of_Surgery', 'Date_of_Last_Visit'], inplace=True)

# Encode binário da coluna Histology ou seja, o tipo de cancer.
# O método get_dummies() do pandas é usado para criar variáveis dummy a partir de uma variável categórica. 
# Variáveis dummy são variáveis ​​binárias que representam categorias distintas.
brca_processed = pd.get_dummies(brca_processed, columns=['Histology'], dtype = int)
print(brca_processed.info())

# Como dito, temos 80% de pessoas que sobreviveram e apenas 20% das que morreram.
# Isso, no treinamento, causa desequilíbrio, deixando o modelo tendencioso.
# Temos que fazer o possível para equalizar os dados.... Existem muitas formas. Uma das mais utilizadas 
# é a criação de dados sintéticos para a classe minoritária.
print('#'*100)
# dividindo o dataset
X_train, X_test, y_train, y_test = train_test_split(brca_processed.drop(columns=['Patient_Status', 'Patient_Status_le', 'HER2 status']), brca_processed['Patient_Status_le'], test_size = 0.15, random_state = 42, stratify=brca_processed['Patient_Status_le'])
# reamostrar o conjunto de dados para que a característica alvo seja distribuida uniformemente
#
# Altere de:
# oversample = SMOTE(n_jobs=100, random_state=0)

# Para:
oversample = SMOTE(random_state=0)
#
#oversample = SMOTE(n_jobs=100, random_state=0)
X_train, y_train = oversample.fit_resample(X_train, y_train)

# Colocando os dados já reamostrados em um plot
plt.pie(y_train.value_counts(), labels=brca_processed['Patient_Status'].unique(), colors='bright', autopct='%.0f%%')

plt.title("Resampled Patient Status")
# Exibindo o plot (gráfico)
plt.show()
print()

print('#'*100)
#Agora que temos o dataset devidamente balanceado, vamos fazer o treinamento utilizando quatro algoritmos 
# de regressão: Support Vector Classification (SVC), Regressão Logística (Logistic Regression), Random 
# Forest e Árvore de Decisão.

## Support Vector Classification (SVC)
# instancia o módulo SVC e indica que o modelo deve calcular as probabilidades das previsões ('probability=True')
svc = SVC(probability=True)
# Definição dos parâmetros que serão testados durante o processo de GridSearchCV. 
# Serão testados dois tipos de kernel: linear e rbf
# O parâmetro c identifica o processo de regularização. Dois serão testados: 1 que é o padrão e um mais elevado com 10.
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
# instanciamento do GrudSearch, utilizando o estimador svc, com os parâmetros definidos acima 
# e n_jobs define a quantidade de processos serão realizados em paralelo (50).
clf = GridSearchCV(svc, parameters, n_jobs=50)
# ajuste do modelo com os dados do treinamento
clf.fit(X_train, y_train)
# GridSearchCV(estimator=SVC(), param_grid={'C': [1, 100], 'kernel': ('linear', 'rbf')})
# o parâmetro "best_estimator_", com base na validação cruzada, seleciona a combinação de parâmetros que produz o melhor desempenho do modelo
clf.best_estimator_

## Regressão Logística (Logistic Regression)
# instancia o Modelo de Regressão Logistica com os parâmetros: max_iter: número máximo de iterações.
# Tipo de penalidade utilizada: "elasticnet" --> combina penalidade L1 (lasso) e L2 (Ridge).
# solver = 'saga' --> algoritmo de otimização utlizado. Adequado para elasticnet e funciona bem com grandes volumes de dados esparsos.
# l1_ratio = 1 --> especifica que na mistura entre L1 e L2 no cálculo da penalidade, terá prioridade o L1.
logit = LogisticRegression(max_iter=3500, penalty='elasticnet', solver = 'saga', l1_ratio=1)
# ajuste do modelo aos dados de treinamento
logit.fit(X_train, y_train)
# extraimos as importâncias dos coeficientes ajustados do modelo. Trata-se de um vetor pois estamos lidando com uma classificação binária.
logit_importances = logit.coef_[0]
# criamos uma série para armazenar os coeficientes
logit_feature_importances = pd.Series(index = X_train.columns, data= np.abs(logit_importances))
# ordenamos os coeficientes em orde crescente
logit_feature_importances = logit_feature_importances.sort_values(ascending=True)
# criamos aqui um gráfico de barras horizontais mostrando as importâncias das características
logit_feature_importances.plot(kind='barh', title = 'Logisitic Regression Feature Importances', xlabel = 'Importance', ylabel = 'Features')
plt.show()
print()

print('#'*100)
#Após o treinamento do modelo de Regressão Logística no conjunto de dados, as características mais importantes 
#que contribuem para a classificação do Status do Paciente incluem Histologia de ILC, carcinomas IDC e o 
# paciente ser HER2+/-. Características que não parecem contribuir para a previsão do modelo incluem idade e 
# estágio do tumor. Surpreendentemente, o estágio de um tumor não parece contribuir muito informativamente 
# para a previsão do modelo, apesar do conhecimento de domínio desta característica. Isso pode ser devido à 
# assimetria dos dados em direção ao câncer de estágio III, já que isso é prevalente em ~60% dos pacientes 
# no conjunto de dados. O status HER2 também é uma característica informativa para o modelo, como entendemos 
# pelo HER2++ normalmente como um preditor de casos de câncer.

## Random Forest

# Inicializa o classificaro RandomForest, utilizando um total de 500 árvores na floresta
plt.figure(figsize=(10, 6)) # Aumentar a largura (10) e altura (6)
forest = RandomForestClassifier(n_estimators=500)
# Ajusta o modelo aos dados de treinamento
forest.fit(X_train, y_train)
# cria um dataframe com a extração das importâncias das características
forest_feature_importance = pd.DataFrame(index = forest.feature_names_in_, data=forest.feature_importances_, columns = ['Feature_Importance'])
# exibe um heatmap com a importância das características
sns.heatmap(forest_feature_importance, annot=True).set(title = "Random Classifier Feature Importance Heatmap", ylabel='Features')
plt.tight_layout()
plt.show()


# Inicializa o modulo de Árvore de Decisão, indicando que o critério de decisão levará em conta o índice gini como medida de pureza
# e terá uma profundidade máxima de 15 nós.
tree_gini = DecisionTreeClassifier(criterion='gini',max_depth=15)
# Faz o ajuste do modelo aos dados de treinamento
tree_gini.fit(X_train, y_train)
# extrai as importância das características em uma Série
tree_gini_feature_importances = pd.Series(tree_gini.feature_importances_, index=tree_gini.feature_names_in_)
# Exibe um gráfico de barras mostrando as importâncias das características.
sns.barplot(x = tree_gini.feature_names_in_, y = tree_gini.feature_importances_).set(title = "Decision Tree Feature Importance", xlabel='Features', ylabel='Importance')
plt.xticks(rotation = 90) 
plt.tight_layout()
plt.show()
print()

print('#'*100)
# Função para plotar a curva ROC
def plot_ROC(model, title, X, Y): 
    # ROC curve
    fpr, tpr, thresholds = roc_curve(y_true=Y, y_score=model.predict_proba(X)[:, 1])
    roc_auc = roc_auc_score(y_true=Y, y_score=model.predict_proba(X)[:, 1])
    plt.plot(fpr, tpr, color="blue", label="AUC = %0.3f" % roc_auc)
    plt.plot([0, 1], [0, 1], color="red", linestyle="--", lw=1)
    plt.title(title)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.legend(loc="lower right")
    plt.show()

### Plotando as curvas ROC com base nos dados de treinamento
# 
# 
# Plotando a curva ROC para Regressão Logistica
plot_ROC(logit, "Logisitic Regression ROC Curve", X_train, y_train)
print(f"Accuracy Score: {accuracy_score(y_true=y_train, y_pred=logit.predict(X_train))}")
print(f"Confusion Matrix:\n {confusion_matrix(y_true=y_train, y_pred=logit.predict(X_train))}")
print(f"Classification Report:\n {classification_report(y_true=y_train, y_pred=logit.predict(X_train))}")    
print()

# Plotando a curva ROC para SVC/SVM
plot_ROC(clf, "Support Vector Machine Classifier ROC Curve", X_train, y_train)
print(f"Accuracy Score: {accuracy_score(y_true=y_train, y_pred=clf.predict(X_train))}")
print(f"Confusion Matrix:\n {confusion_matrix(y_true=y_train, y_pred=clf.predict(X_train))}")
print(f"Classification Report:\n {classification_report(y_true=y_train, y_pred=clf.predict(X_train))}")

# Plotando a curva ROC para Random Forest
plot_ROC(forest, "Random Forest Classifier ROC Curve", X_train, y_train)
print(f"Accuracy Score: {accuracy_score(y_true=y_train, y_pred=forest.predict(X_train))}")
print(f"Confusion Matrix:\n {confusion_matrix(y_true=y_train, y_pred=forest.predict(X_train))}")
print(f"Classification Report:\n {classification_report(y_true=y_train, y_pred=forest.predict(X_train))}")

# Plotando a curva ROC para Árvore de Decisão
plot_ROC(tree_gini, "Decision Tree Classifier ROC Curve", X_train, y_train)
print(f"Accuracy Score: {accuracy_score(y_true=y_train, y_pred=tree_gini.predict(X_train))}")
print(f"Confusion Matrix:\n {confusion_matrix(y_true=y_train, y_pred=tree_gini.predict(X_train))}")
print(f"Classification Report:\n {classification_report(y_true=y_train, y_pred=tree_gini.predict(X_train))}")

### Vamos agora selecionar apenas os dois melhores algoritmos classificadores e plotar a curva ROC 
# com os dados de Teste

# Curva ROC Random Forest com dados de Teste
plot_ROC(forest, "Random Forest Classifier ROC Curve", X_test, y_test)
print(f"Accuracy Score: {accuracy_score(y_true=y_test, y_pred=forest.predict(X_test))}")
print(f"Confusion Matrix:\n {confusion_matrix(y_true=y_test, y_pred=forest.predict(X_test))}")
print(f"Classification Report:\n {classification_report(y_true=y_test, y_pred=forest.predict(X_test))}")

# Curva ROC da Arvore de Decisão dos dados de Teste
plot_ROC(tree_gini, "Decision Tree Classifier ROC Curve", X_test, y_test)
print(f"Accuracy Score: {accuracy_score(y_true=y_test, y_pred=tree_gini.predict(X_test))}")
print(f"Confusion Matrix:\n {confusion_matrix(y_true=y_test, y_pred=tree_gini.predict(X_test))}")
print(f"Classification Report:\n {classification_report(y_true=y_test, y_pred=tree_gini.predict(X_test))}")

# Previsão
# features = [['Age', 'Protein1',	'Protein2',	'Protein3',	'Protein4',	'HER2_Status_le', 'Tumour_Stage_oe', 'Histology_Infiltrating Ductal Carcinoma', 'Histology_Infiltrating', 'Lobular Carcinoma', 'Histology_Mucinous Carcinom']]
features = np.array([[37.0, 0.080353, 0.42638, 0.54715, 0.273680, 1, 3, 1, 0, 0]])
print(forest.predict(features))

