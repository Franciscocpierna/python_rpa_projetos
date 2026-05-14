# Importando as Bibliotecas/Pacotes
# Evitar mensagens de erros
import warnings 
warnings.filterwarnings('ignore')

# Manipulação de dados
import pandas as pd
import numpy as np

# Visualização de dados
import matplotlib.pyplot as plt
import seaborn as sns

# Treinamento e Métricas
import sklearn  # para registrar a versão
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

# Exportação do Modelo
import joblib  # para registrar a versão
from joblib import dump

# Carregar o módulo de funções para limpeza de dados
from limpeza_dados import *

# configuração do Seaborn
sns.set(style='white', context='notebook')

# Importando o Dataset
df = pd.read_csv('dados/adult.csv')
print(df.head())

print('#'*100)

print(df.info())

print('#'*100)
# Converte os valores desconhecidos, marcados com '?' em nulos (NA)
df.replace('?', pd.NA, inplace=True)
print()
print(df.head())
# verificando se existe algum valor nulo
calcular_porcentagem_valores_ausentes(df)
print('#'*100)
# Exibindo o relatório de valores nulos por coluna
relatorio_valores_ausentes_por_coluna(df)
print()
print('#'*100)
for col in ['workclass', 'occupation', 'native.country']:
    preencher_ausentes_com_moda(df, col)
print()

print('#'*100)
# verificando se existe algum valor nulo
calcular_porcentagem_valores_ausentes(df)

print()

print('#'*100)
# Exibindo o relatório de valores nulos por coluna
relatorio_valores_ausentes_por_coluna(df)

sns.set_style("whitegrid")
plt.figure(figsize = (8,5))
plt.title('Income Distribution of Adults', fontsize=18, fontweight='bold')
eda_percentage = df['income'].value_counts(normalize = True).rename_axis('income').reset_index(name = 'Percentage')

ax = sns.barplot(x = 'income', y = 'Percentage', data = eda_percentage.head(10), palette='Greens_r')
for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy() 
    ax.annotate(f'{height:.0%}', (x + width/2, y + height*1.02), ha='center', fontweight='bold')
plt.show()    
print()



print('#'*100)
### Engenharia dos Dados
#Para adequação dos dados para minimizar os erros de classificação.

# Transformação das idades em categorias: grupo de idades
def age_group(x):
    x = int(x)
    x = abs(x)
    if( 18 < x < 31 ):
        return "19-30"
    if( 30 < x < 41 ):
        return "31-40"
    if( 40 < x < 51 ):
        return "41-50"
    if( 50 < x < 61 ):
        return "51-60"
    if( 60 < x < 71 ):
        return "61-70"
    else:
        return "Greater than 70"

df['age_group'] = df['age'].apply(age_group)
plt.figure(figsize=(12,6))
order_list = ['19-30', '31-40', '41-50', '51-60', '61-70', 'Greater than 70']
sns.countplot(x=df['age_group'], hue=df['income'], palette='Greens_r', order=order_list)
plt.title('Income of Individuals of Different Age Groups', fontsize=18, fontweight='bold')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.show()


# Verificando a distribuição do salário por classe de trabalho
plt.figure(figsize=(12,6))
sns.countplot(x=df['workclass'], hue = df['income'], palette='Greens_r')
plt.title('Income of Individuals of Different Working CLasses', fontsize=18, fontweight='bold')
plt.xticks(fontsize=16,rotation = 90)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.tight_layout()
plt.show()


# Verificando o salário por escolaridade
plt.figure(figsize=(15,8))
order_list = ['Preschool', '1st-4th', '5th-6th', '7th-8th', '9th', '10th', '11th', '12th', 
                'HS-grad ', 'Some-college', 'Bachelors', 'Masters', 'Doctorate', 'Prof-school', 
              'Assoc-acdm', 'Assoc-voc']
sns.countplot(x=df['education'], hue = df['income'], palette='Greens_r', order= order_list)
plt.title('Income of Individuals of Different Education Levels', fontsize=18, fontweight='bold')
plt.xticks(fontsize=16,rotation = 90)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.tight_layout()
plt.show()

# Verificando o salário por Estado Civil
plt.figure(figsize=(14,6))
sns.countplot(x=df['marital.status'], hue = df['income'], palette='Greens_r')
plt.title('Income of Individuals of Different Marital Status', fontsize=18, fontweight='bold')
plt.xticks(fontsize=16,rotation = 90)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.tight_layout()
plt.show()

# Verificando o salário por tipo de ocupação
plt.figure(figsize=(18,6))
sns.countplot(x=df['occupation'], hue = df['income'], palette='Greens_r')
plt.title('Income of Individuals of Different Occupations', fontsize=18, fontweight='bold')
plt.xticks(fontsize=16,rotation = 90)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.tight_layout()
plt.show()

# Verificando o salário quanto ao tipo de relacionamento
plt.figure(figsize=(12,6))
sns.countplot(x=df['relationship'], hue = df['income'], palette='Greens_r')
plt.title('Income of Individuals of Different Relationship', fontsize=18, fontweight='bold')
plt.xticks(fontsize=14)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.show()
print()

# Verificando o salário quanto as diferentes raças
plt.figure(figsize=(12,6))
sns.countplot(x=df['race'], hue = df['income'], palette='Greens_r')
plt.title('Income of Individuals of Different Races', fontsize=18, fontweight='bold')
plt.xticks(fontsize=14)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.show()

# Verificando o salário em relação ao sexo
plt.figure(figsize=(12,6))
#order_list = ['19-30', '31-40', '41-50', '51-60', '61-70', 'Greater than 70']
sns.countplot(x=df['sex'], hue = df['income'], palette='Greens_r')
plt.title('Income of Individuals of Different Genders', fontsize=18, fontweight='bold')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.legend(fontsize=16)
plt.show()

# Modificando a saída (salário) para calcular a correlação
df['income']=df['income'].map({'<=50K': 0, '>50K': 1})

# Selecionar apenas as colunas numéricas
numeric_df = df.select_dtypes(include=['float64', 'int64'])
# # Mostrando o mapa de correlação
# plt.figure(figsize=(11, 10))
# plt.title("Correlation between different features of the dataset", fontsize=18, fontweight='bold')
# sns.heatmap(numeric_df.corr(), cmap='Greens_r', annot=True)
# plt.xticks(fontsize=12, rotation=90)
# plt.yticks(fontsize=12, rotation=90)
# plt.tight_layout()
# plt.show()

# esse gráfico ficou melhor ajustado 
plt.figure(figsize=(11, 10))
plt.title("Correlation between different features", fontsize=18, fontweight='bold')

# annot_kws diminui o tamanho do texto dentro do gráfico
#sns.heatmap(numeric_df.corr(), cmap='Greens_r', annot=True, annot_kws={"size": 9})
sns.heatmap(numeric_df.corr(), cmap='Greens_r', annot=True, annot_kws={"size": 8}) # Diminuí para 8
# rotation=45 com ha='right' evita que o texto saia da tela
plt.xticks(fontsize=8, rotation=45, ha='right')
plt.yticks(fontsize=8)

# Ajusta manualmente as margens caso o tight_layout não seja suficiente
plt.subplots_adjust(bottom=0.2) 

plt.show()

correlation_matrix = numeric_df.corr()

# Exibir a matriz de correlação
print(correlation_matrix)

print('#'*100)

# Distribuindo a coluna de Idade em 3 partes significativas 
# e plotando-a correspondente à característica de saída (salário)
# Combinando os graus mais baixos de educação juntos

df.drop(['education.num'], axis = 1, inplace = True)
df['education'].replace(['11th', '9th', '7th-8th', '5th-6th', '10th', '1st-4th', 'Preschool', '12th'],
                             ' School', inplace = True)
df['race'].replace(['Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'],' Other', inplace = True)

# Deletando o agrupamento criado para criação dos gráficos
df.drop('age_group', inplace = True, axis = 1)

### Preparando os dados para criação dos modelos

# Fazendo o Encoder para poder gerar um modelo
categorical = ['workclass','education', 'marital.status', 'occupation', 'relationship',
               'race', 'sex','native.country']
label_encoder = LabelEncoder()
for col in categorical:
    label_encoder.fit(df[col])
    df[col] = label_encoder.transform(df[col])
    
# Dividindo em treino e teste
x = df[['workclass','education', 'marital.status', 'occupation', 'relationship',
               'race', 'sex','native.country', 'age', 'fnlwgt', 'capital.gain', 'capital.loss', 'hours.per.week']]
y = df['income']
    
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0)
# Padronização da escala de valores
scaler = StandardScaler()

x_train = pd.DataFrame(scaler.fit_transform(x_train), columns = x.columns)
x_test = pd.DataFrame(scaler.transform(x_test), columns = x.columns)

### Gerando o Modelo com Regressão Logística

# Treinando o Modelo
logreg = LogisticRegression()
logreg.fit(x_train, y_train)

# Fazendo as Previsões
Y_pred_log = logreg.predict(x_test)

# Medindo a acurácia
acc_log = accuracy_score(y_test, Y_pred_log)
print("Logistic Regression", acc_log)


print()

print('#'*100)
# Treinando o Modelo
dectree = DecisionTreeClassifier(criterion = "gini", random_state = 100, max_depth = 5, min_samples_leaf = 5)
dectree.fit(x_train, y_train)

# Fazendo as Previsões
Y_pred_tree = dectree.predict(x_test)
# Medindo a acurácia
acc_tree = accuracy_score(y_test, Y_pred_tree)
print("Decision Tree", acc_tree)

print()
#Pela maior acurácia do segundo modelo, vamos utilizá-lo para fazer o deploy.

#### Salvando o Segundo Modelo no formato Joblib (model.joblib)
dump(dectree, open('model.joblib','wb'))

print('#'*100)
### Parte 2 - Deploy do Modelo
#**Formulário HTML**

# Primeiro, precisamos coletar os dados (novos valores de atributos) para prever a renda a partir de vários 
# atributos e depois usar o modelo de árvore de decisão que construímos acima para prever se a renda é 
# superior a 50 mil ou não. 

# Portanto, para coletar os dados, criamos um formulário HTML que conteria todas as diferentes opções para 
# selecionar de cada atributo. Aqui, criamos um formulário simples usando apenas HTML. Se você tiver 
# conhecimento e desejar tornar o formulário mais interativo, fique a vontade para fazer isso.

#**Carregando o Modelo Salvo**

# joblib --> load  (from joblib import load)

#loaded_model = load(open('model.joblib','rb'))

#Isso dentro do código Flask ficaria da seguinte forma:
# libraries installation
# pip install scikit-learn==1.2.2
# pip install numpy==1.26.4
# pip install joblib==1.2.0

#importing libraries
import os
import numpy as np
import flask
from joblib import load
from flask import Flask, render_template, request
loaded_model = load(open('model.joblib','rb'))
#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html')
    #return "Hello World"

#prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,13)
    loaded_model = load(open("model.joblib","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/result',methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        
        if int(result)==1:
            prediction='Renda superior a 50K'
        else:
            prediction='Renda inferior a 50K'
            
        return render_template("result.html",prediction=prediction)

if __name__ == "__main__":
	app.run(debug=True)

print()

#### Basta executar e acessar a página que será indicada...
print('#'*100)

print()

print('#'*100)

print()