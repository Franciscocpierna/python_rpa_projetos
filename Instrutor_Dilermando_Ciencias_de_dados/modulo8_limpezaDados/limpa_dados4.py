## <font color='green'>Projeto 4 - Trabalhando com Codificação de Caracteres</font>
## <font color='green'>Instalando os Pacotes e Carregando os Dados</font>

# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada :', python_version())

print('#'*100)

# Para atualizar um pacote, execute o comando abaixo no terminal ou prompt de comando:
# pip install -U nome_pacote

# Para instalar a versão exata de um pacote, execute o comando abaixo no terminal ou prompt de comando:
# !pip install nome_pacote==versão_desejada

# Depois de instalar ou atualizar o pacote, reinicie o jupyter notebook.

# Instala o pacote watermark. 
# Esse pacote é usado para gravar as versões de outros pacotes usados neste jupyter notebook.
#!pip install -q -U watermark

# Importação dos módulos básicos


import sqlalchemy as db
import sys
import numpy as np
import pandas as pd
# Módulo muito útil para Codificação de Caracteres
import chardet
# Definição de um princípio de geração para reprodutibilidade
print(np.random.seed(0))

# Versões dos pacotes usados neste jupyter notebook
#%reload_ext watermark
#%watermark -a "pyPRO - Seja um Profissional Python!" --iversions

# Versões dos pacotes usados neste Vscode


#Lista de pacotes que você quer verificar
pacotes = {
    "Python": sys.version.split()[0],
    "Pandas": pd.__version__,
    "SQLAlchemy": db.__version__,
    "NumPy": np.__version__
}

for nome, versao in pacotes.items():
    print(f"{nome}: {versao}")

print('#'*100)
## Entendendo a Codificação de Caracteres (character encoding)

# Codificações de caracteres são conjuntos específicos de regras para mapeamento de bytes binários brutos 
# de strings  (que se parecem com isto: 0110100001101001) para caracteres que compõem texto legível por 
# humanos (como "oi").

# Como existem muitas técnicas (ou padrões) diferentes usadas para codificar tais conjuntos de dados binários 
# e se você tentar converter tais dados no texto sem conhecer a técnica de codificação em que foi originalmente 
# escrito, você acabará com o texto embaralhado ou sem sentido. Esse texto embaralhado é chamado de "mojibake" 
# (dito como mo-gee-bah-kay). Aqui está um exemplo de mojibake:

# æ–‡å—åŒ–ã??.

# Você também pode acabar com caracteres "desconhecidos". Isso ocorre quando não há mapeamento entre um byte 
# específico e um caractere na codificação que você está usando para ler sua string de bytes e eles se parecem 
# com isto:

# ����������

# Incompatibilidades de codificação de caracteres são menos comuns hoje do que costumavam ser, mas 
# definitivamente ainda são um problema. Existem muitas codificações de caracteres diferentes, mas a 
# principal que você precisa conhecer é UTF-8.

# **UTF-8 é a codificação de texto padrão. Todo o código Python está em UTF-8 e, idealmente, todos os seus 
# dados também devem estar. É quando as coisas não estão em UTF-8 que você tem problemas.**

# Foi muito difícil lidar com codificações no Python 2, mas felizmente no Python 3 é muito mais simples. 
# Existem dois tipos de dados principais que você encontrará ao trabalhar com texto em Python 3:

# Uma é a string, que é o texto por padrão. Os outros dados são do tipo de dados bytes, que é uma sequência 
# de números inteiros. 

# Vamos ver um exemplo de uma string:
# inicialize uma variável com uma string
frase = "Este é o símbolo do Euro: €"

# Verificando o tipo de dado da variável "frase"
print(type(frase))


#Vamos ver agora o outro tipo de dado: byte

# Codificando a frase para uma codificação diferente, substituindo os caracteres que geram erros
frase2 = frase.encode("utf-8", errors = "replace")

# Verificando agora o tipo de dado

print(type(frase2))
print('#'*100)

# Se analisarmos um objeto do tipo bytes, veremos que ele tem um b na frente dele e talvez algum texto depois. 

# Isso ocorre porque os bytes são impressos como se fossem caracteres codificados em ASCII. 

# **ASCII é uma codificação de caracteres mais antiga que realmente não funciona para escrever qualquer 
# idioma além do inglês.**

# Aqui você pode ver que nosso símbolo do euro e também os caracteres com acentuação ("é" e "í") foram 
# substituídos por "mojibakes" que se parece com "\xc3\xa9", "\xc3\xad" e "\xe2\x82\xac" quando impressos 
# como se fossem uma string ASCII.

# verificando como os caracteres bytes são representados
print(frase2)

#Quando convertemos nossos bytes de volta em uma string com a codificação correta, podemos ver que nosso 
# texto está correto.
# convertendo de volta para utf-8
print(frase2.decode("utf-8"))


# No entanto, quando tentamos usar uma codificação diferente para mapear nossos bytes em uma string, 
# obtemos um erro. 

# Isso ocorre porque a codificação que estamos tentando usar não sabe o que fazer com os bytes que estamos 
# tentando passar. 

# Você precisa informar ao Python a codificação em que a string de bytes realmente deveria estar.

# Você pode pensar em diferentes codificações como diferentes formas de gravar música. Você pode gravar a 
# mesma música em um CD, fita cassete ou 8 faixas. Embora a música possa soar mais ou menos igual, 
# você precisa usar o equipamento certo para reproduzir a música de cada formato de gravação. O decodificador 
# correto é como um toca-fitas ou um toca-CD. Se você tentar reproduzir uma fita cassete em um CD player, 
# simplesmente não funcionará.

# tentando codificar nossa string de bytes para a codificação ascii
#print(frase2.decode("ascii")) apresenta erro

# Também podemos ter problemas se tentarmos usar a codificação errada para mapear uma string para bytes. 

# Como já foi mencionado, as strings são UTF-8 por padrão no Python 3, portanto, se tentarmos tratá-las como 
# se estivessem em outra codificação, criaremos problemas.

# Por exemplo, se tentarmos converter uma string em bytes para ascii usando encode(), podemos pedir que os 
# bytes sejam o que seriam se o texto estivesse em ASCII. Como nosso texto não está em ASCII, haverá alguns 
# caracteres que ele não pode manipular. Podemos substituir automaticamente os caracteres que o ASCII não 
# suporta. Se fizermos isso, no entanto, quaisquer caracteres que não estejam em ASCII serão substituídos 
# apenas pelo caractere desconhecido. Então, quando convertermos os bytes de volta para uma string, o 
# caractere será substituído pelo caractere desconhecido. A parte perigosa disso é que não há como 
# saber qual caracter deveria ser. Isso significa que podemos ter tornado nossos dados inutilizáveis!

# declarando novamente a frase...
frase = "Este é o símbolo do Euro: €"

# Codificando a frase para uma codificação diferente, substituindo os caracteres que geram erros
frase2 = frase.encode("ascii", errors = "replace")

# Convertendo a frase de volta
print(frase2.decode("ascii"))

# Perdemos a cadeia de bytes subjacente original! 
# Ela foi substituída pela cadeia de bytes subjacente para o caractere desconhecido!


# Isso é ruim e como analista de dados você deve evitar fazê-lo! 

# É muito melhor converter todo o nosso texto para UTF-8 o mais rápido possível e mantê-lo nessa codificação. 
# O melhor momento para converter entrada não UTF-8 em UTF-8 é quando você lê os arquivos.

# A maioria dos conjuntos de dados (datasets) provavelmente será codificada com UTF-8. 

# Isso é o que o Python espera por padrão, portanto, na maioria das vezes, você não terá problemas. No 
# entanto, às vezes você receberá um erro como este: 

# *UnicodeDecodeError: o codec 'utf-8' não pode decodificar o byte 0x99 na posição 11: byte inicial inválido*

## Carregando os Dados com Problemas de Codificação

### Dataset público: *Kickstarter Projects*

# Vamos retomar o Dataset do Kickstarter Projects que já trabalhamos anteriormente. Vamos pegar uma versão do dataset que corresponde aos dados desde 2016.

# Link para o Dataset: 
# https://www.kaggle.com/code/rtatman/data-cleaning-challenge-character-encodings/input?select=ks-projects-201612.csv
# Fonte: Kaggle.com

# Este arquivo estará disponível como recurso dessa aula.
# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "undefined"]


# Tentando carregar o dataset com codificação diferente de UTF-8
#dataset = pd.read_csv("dados/ks-projects-201612.csv", na_values = lista_labels_valores_ausentes) gera erro

# Observe que obtemos o mesmo *UnicodeDecodeError* que obtivemos quando tentamos decodificar bytes UTF-8 como se 
# fossem ASCII! 

# Isso nos diz que esse arquivo não é realmente UTF-8. Não sabemos qual codificação realmente é. Uma maneira de 
# descobrir isso é tentar testar várias codificações de caracteres diferentes e ver se alguma delas funciona. 

# Uma maneira melhor, porém, é usar o **módulo chardet** para tentar descobrir automaticamente qual é a 
# codificação correta. 

# Não é 100% garantido que esteja certo, mas geralmente é mais rápido do que apenas tentar adivinhar.

# Vou apenas olhar para os primeiros dez mil bytes deste arquivo. Isso geralmente é suficiente para um bom 
# palpite sobre qual é a codificação e é muito mais rápido do que tentar examinar o arquivo inteiro. 

# (Especialmente com um arquivo grande, isso pode ser muito lento.) 

# Outro motivo para examinar apenas a primeira parte do arquivo é que podemos ver, observando a mensagem de erro,
#  que o primeiro problema é o 11º caractere. Portanto, provavelmente só precisamos olhar para a primeira 
# parte do arquivo para descobrir o que está acontecendo.


# Olhando os primeiros 10 mil bytes para tentar determinar a codificação
with open("dados/ks-projects-201612.csv", 'rb') as dados:
    resultado = chardet.detect(dados.read(10000))

# Verificando qual é a codificação de caracteres que foi determinada pelo método detect
print(resultado)

# Como pode ser observado, o grau de confiança que o método detect do pacote chardet retornou é de 73% que seja 
# a codificação "Windows-1252".

# Portanto, se abrirmos o arquivo agora com essa codificação, teremos uma maior garantia que dê certo. 
# Vamos ver:
print('#'*100)
# Lendo o mesmo arquivo agora definindo que a codificação a ser utilizada é a "Windows-1252"
dataset = pd.read_csv("dados/ks-projects-201612.csv", na_values = lista_labels_valores_ausentes, encoding='Windows-1252', low_memory=False)

# Olhando as primeiras linhas do dataset que agora foi carregado sem erro...
print(dataset.head())
print('#'*100)
# Agora sim!!  Parece que chardet estava certo! 

# O arquivo é lido sem problemas (embora recebamos um aviso sobre tipos de dados) e, quando olhamos para as primeiras linhas, parece estar 
# tudo bem.

# E se a codificação indicada pelo chardet não estiver certa? 

# Como o chardet é basicamente apenas um "adivinho" sofisticado, às vezes ele adivinhará a codificação errada. 

# Uma coisa que você pode tentar é olhar mais ou menos do arquivo e ver se obtém um resultado diferente e depois tentar.


## Carregando outro Dataset

### Dataset público: *Fatal Police Shootings in the US*

# O assassinato de Michael Brown em 2014 em Ferguson, Missouri, deu início ao movimento de protesto que culminou no Black Lives Matter e 
# um foco maior na responsabilidade policial em todo o país (Estados Unidos).

# Desde 1º de janeiro de 2015, o **The Washington Post** vem compilando um banco de dados de todos os tiroteios fatais cometidos por 
# policiais no cumprimento do dever nos EUA.

# É difícil encontrar dados confiáveis anteriores a esse período, pois as mortes cometidas pela polícia não foram documentadas de forma 
# abrangente e as estatísticas sobre a brutalidade policial estão muito menos disponíveis. Como resultado, um grande número de casos não 
# são notificados.

# O Washington Post está rastreando mais de uma dúzia de detalhes sobre cada assassinato - incluindo a raça, idade e sexo do falecido, se 
# a pessoa estava armada e se a vítima estava passando por uma crise de saúde mental. Eles coletaram essas informações de sites de aplicação 
# da lei, novos relatórios locais, mídia social e monitorando bancos de dados independentes, como "Morto pela polícia" e "Encontros fatais". 
# O Washington Post também realizou relatórios adicionais em muitos casos.

# Existem quatro conjuntos de dados adicionais. Estes são dados do censo dos EUA sobre taxa de pobreza, taxa de conclusão do ensino médio, 
# renda familiar média e demografia racial.

# Fonte dos dados do censo:
# https://factfinder.census.gov/faces/nav/jsf/pages/community_facts.xhtml

# Vamos trabalhar com o dataset "Mortes por Policiais nos Estados Unidos". 
# Link para o Dataset: https://www.kaggle.com/code/rtatman/data-cleaning-challenge-character-encodings/input?select=PoliceKillingsUS.csv
# Fonte: Kaggle.com

# Este arquivo estará disponível como recurso dessa aula.

# Criamos uma lista para identificar valores ausentes
lista_labels_valores_ausentes = ["n/a", "na", "undefined"]

# Tentando carregar o dataset com codificação diferente de UTF-8
#dataset = pd.read_csv("dados/PoliceKillingsUS.csv", na_values = lista_labels_valores_ausentes) gera erro

#Vamos descobrir a codificação desse arquivo...

# Olhando os primeiros 10 mil bytes para tentar determinar a codificação
with open("dados/PoliceKillingsUS.csv", 'rb') as dados:
    resultado = chardet.detect(dados.read(10000))

# Verificando qual é a codificação de caracteres que foi determinada pelo método detect
print(resultado)


#Vejam que agora o método detect do pacote chardet nos deu 100% de confiança que os dados estão com a codificação ascii. Assim, 
# vamos tentar carregar o dataset com essa codificação.

# Tentando carregar o dataset com codificação "ascii"
# dataset = pd.read_csv("dados/PoliceKillingsUS.csv", na_values = lista_labels_valores_ausentes, encoding='ascii')

# print(dataset) gera erro

# Opa!!!  Parece que os 10 mil primeiros bytes não foram suficientes para determinar a codificação correta.

# Vamos aumentar para 100 mil, e ver o que acontece!

# Olhando agora os primeiros 100 mil bytes para tentar determinar a codificação de forma mais correta
with open("dados/PoliceKillingsUS.csv", 'rb') as dados:
    resultado = chardet.detect(dados.read(100000))

# Verificando qual é a codificação de caracteres que foi determinada pelo método detect
print(resultado)

print('#'*100)

dataset = pd.read_csv("dados/PoliceKillingsUS.csv", na_values = lista_labels_valores_ausentes, encoding='Windows-1252')
print(dataset)

print(dataset.info())
print('#'*100)
print(dataset.head())
print()

print()

print(dataset.shape)
print('#'*100)
contagem_valores_ausentes = dataset.isnull().sum()
contagem_valores_ausentes[0:20]

print(contagem_valores_ausentes)
print('#'*100)
# Calculando os totais de celulas e de celulas com valores ausentes (total_nulos) 
total_celulas = np.prod(dataset.shape)
total_nulos = contagem_valores_ausentes.sum()
# Calculando o percentual de dados ausentes em DESLIZAMENTOS
print(f"Percentual de Dados ausentes no dataset: {(total_nulos/total_celulas):.2%}")

## Salvando o Dataset com codificação UTF-8

# Por fim, depois de passar por todo o trabalho de colocar seu arquivo em UTF-8, você provavelmente desejará mantê-lo assim. 

# A maneira mais fácil de fazer isso é salvar seus arquivos com codificação UTF-8. 

# A boa notícia é que, como UTF-8 é a codificação padrão em Python, quando você salva um arquivo, ele é salvo como UTF-8 por padrão:

# Salvando o dataset no formato UTF-8 (padrão de gravação)
dataset.to_csv("dados/PoliceKillingsUS-utf8.csv")

#E aí está!! Agora com os dados salvos no formato UTF-8 não precisamos mais realizar identificação e novas parametrizações para a 
# abertura desse dataset.

