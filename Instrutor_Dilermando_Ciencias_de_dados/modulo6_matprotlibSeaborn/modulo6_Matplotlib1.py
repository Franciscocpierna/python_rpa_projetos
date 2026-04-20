# Introdução à Biblioteca Matplotlib - Parte 1

# Se você já se aventurou pelo vasto mundo da visualização de dados, provavelmente já ouviu falar da biblioteca
# Matplotlib. Ela é uma ferramenta poderosa e flexível para criar gráficos e visualizações em Python, e é 
# amplamente utilizada por cientistas de dados, pesquisadores e profissionais em áreas diversas.

### 6.1 O que é Matplotlib?

# Matplotlib é uma biblioteca de plotagem 2D em Python que produz figuras de alta qualidade em uma variedade
# de formatos e ambientes. Desenvolvida por John D. Hunter em 2003, ela foi criada para emular as capacidades
# de plotagem do MATLAB, tornando-a uma escolha popular para aqueles que estão familiarizados com o ambiente
# MATLAB.

# ### 6.2 Principais recursos:

# 1. **Flexibilidade**: Uma das maiores vantagens da Matplotlib é sua flexibilidade. Ela permite que você 
# Controle praticamente todos os aspectos de uma figura, desde o tamanho e a escala até os detalhes mais 
# minuciosos da estilização.

# 2. **Suporte a diversos tipos de gráficos**: Matplotlib suporta uma ampla variedade de tipos de gráficos,
# incluindo gráficos de dispersão, linhas, barras, histogramas, gráficos de contorno, gráficos de superfície 
# e muito mais. Não importa qual seja o seu conjunto de dados, há uma opção de visualização disponível.

# 3. **Integração com NumPy e Pandas**: Por ser compatível com NumPy e Pandas, a Matplotlib funciona 
# perfeitamente com os arrays e estruturas de dados dessas bibliotecas, o que facilita a plotagem de dados 
# armazenados nesses formatos.

# ### 6.3 Como começar a usar:

# 1. **Instalação**: Se você ainda não tem o Matplotlib instalado, pode instalá-lo facilmente usando pip, o 
# gerenciador de pacotes do Python. Basta executar o comando `pip install matplotlib` no seu terminal ou 
# prompt de comando.

# Você também pode:

# Instalar uma versão específica do MatPlotLib, no caso, vamos instalar a versão 3.8.4
# !pip install -q matplotlib==3.8.4


# 2. **Importação**: Após a instalação, você pode importar a biblioteca em seu script Python usando a seguinte 
# linha de código:

# Importando o pacote
import matplotlib as mpl

# Verificando a versão
print(mpl.__version__)

# Podemos também só importar uma classe de métodos específicos para realizar as plotagens de gráficos
# Por exemplo: o pyplot (pacote dentro da biblioteca Matplotlib --> matplotlib.pyplot) 
# é uma coleção de funções e estilos do Matplotlib
import matplotlib.pyplot as plt

# 3. **Plotagem básica**: Para criar um gráfico simples, basta passar os dados que deseja plotar para a função
# `plot()` e, em seguida, chamar a função `show()` para exibir o gráfico:

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

print('#'*50)

x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)

# Forçar o eixo X a mostrar apenas os teus números
plt.xticks(x)

# Forçar o eixo Y a mostrar apenas os teus números
plt.yticks(y)

plt.show()
print('#'*50)
# ### 6.4 Visualização de Plots
# Plots são representações visuais (gráficos) de dados. 

# De forma bem objetiva, plots, são gráficos que mostram a relação entre uma ou mais variáveis. 

# Existem vários tips de plots: linhas, dispersão, histogramas, pizza, barras etc. Cada tipo de plot é 
# utilizado para se obter um tipo específico de visualização dos dados.

# Para a exibição de um plot, temos que seguir três passos básicos: 
# 1. Escolha dos dados a serem plotados
# 2. Escolha do tipo de visualização (do gráfico)
# 3. Configuração das opções de plotagem (tamanho, cores, rótulos etc.)

# Já importamos o pyplot acima... Vamos fazê-lo novamente para reforço...
# Como já dito, o pyplot (pacote dentro da biblioteca Matplotlib --> matplotlib.pyplot) 
# é uma coleção de funções e estilos do Matplotlib

import matplotlib.pyplot as plt

# Dependendo da versão do Jupyter Notebook, você terá que dizer explicitamente que deseja que os gráficos 
# sejam mostrados dentro do Jupyter Notebook. O comando para isso:
# %matplotlib inline

# o método plot() define os eixos do gráfico
plt.plot([1, 3, 5], [2, 4, 9])
# e o método show() exibe o gráfico (faz a plotagem)
plt.show()
print('#'*50)

x = [1, 3, 5]
y = [2, 4, 9]

plt.plot(x,y)

# Forçar o eixo X a mostrar apenas os teus números
plt.xticks(x)

# Forçar o eixo Y a mostrar apenas os teus números
plt.yticks(y)

plt.show()
print('#'*50)
# Podemos fazer a mesma coisa, utilizando variáveis
l1 = [1, 3, 5]
l2 = [2, 4, 9]

plt.plot(l1, l2)
# Definindo o rótulo do eixo X
plt.xlabel('Lista 1')
# Definindo o rótulo do eixo Y
plt.ylabel('Lista 2')
# Definindo um título para o gráfico
plt.title('Visualização com Plot')
plt.show()
print('#'*50)

l3 = [1, 2, 3]
l4 = [12, 14, 18]
plt.plot(l3, l4, label = 'Outra Visualização com Plot')
plt.legend()
plt.show()


### 6.5 Criação de Gráficos de Barras

#**Gráficos de Barras** é um tipo específico de plotagem, geralmente utilizado para mostrar dados categóricos 
#com barras retangulares. Cada barra representa uma categoria e sua altura, sua quantidade ou frequência.
# Geralmente utilizamos esse tipo de gráfico para realizar a comparação entre as categorias.

x1 = [2, 4, 6, 8, 10]
y1 = [9, 3, 7, 8, 2]

plt.bar(x1, y1, label = 'Barras', color = 'blue')
plt.legend()
plt.show()


x2 = [1, 3, 5, 7, 9]
y2 = [8, 4, 2, 7, 1]

plt.bar(x1, y1, label = 'Lista1', color = 'blue')
plt.bar(x2, y2, label = 'Lista2', color = 'green')
plt.plot(x1, y1, color = 'blue')
plt.legend()
plt.show()


idades = [18, 23, 73, 89, 22, 18, 23, 34, 40, 52, 54, 19, 100, 34, 23, 19, 34, 41, 18, 34, 51, 43]

indice = [x for x in range(len(idades))]

print(indice)


plt.bar(indice, idades)
plt.show()


# intervalos - bins
bins = [0, 10, 20, 30, 40, 50 ,60, 70, 80, 90, 100, 110]

# Vamos criar um gráfico de histograma  -> rwidth - row width - largura da linha
plt.hist(idades, bins, histtype = 'bar', rwidth = 0.8)
plt.show()


# Vamos criar um outro gráfico de histograma  agora como área (espaços preenchidos --> stepfilled)
plt.hist(idades, bins, histtype = 'stepfilled', rwidth = 0.8)
plt.show()

# Como saber quais são os parâmetros e os valores de cada parâmetro?
# Visitar a documentação oficial do Matplotlib!!!
### 6.6 Gráfico de Dispersão (scatter plot)
#Gráfico de pontos... utilizado para representar a relação entre duas variáveis contínuas 
#(análise bivariada - duas variáveis)

x = [1,2,3,4,5,6,7,8,9]
y = [7,2,4,2,5,7,8,2,4]

plt.scatter(x, y, label = 'Pontos', color = 'black', marker = 'o')
plt.legend()
plt.show()

### 6.7 Gráfico de Área Empilhada (stack plot)
#Utilizado para verificar a mudança de várias variáveis ao longo do tempo. Várias áreas coloridas sobrepostas.
#Mostram como cada parte contribui para o todo ao longo do tempo.
dias = [1,2,3,4,5,6,7]
dormir = [7,8,6,9,6,7,5]
comer = [2,1,3,2,1,1,3]
trabalhar = [9,8,6,7,8,8,7]
passear = [6,7,9,6,9,8,9]

plt.stackplot(dias, dormir, comer, trabalhar, passear, colors = ['m', 'c', 'r', 'k', 'b'])
plt.show()

### 6.8 Gráfico de Pizza (pie)
#Utilizado para mostrar a relação de uma variável categógica em relação ao todo. Um circulo, 
#dividido em fatias. Cada fatia, corresponde a uma categoria.

fatias = [7, 2, 4, 11]
atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores = ['olive', 'lime', 'violet', 'royalblue']

plt.pie(fatias, labels = atividades, colors = cores, startangle = 90, shadow = True, explode = (0, 0, 0.2, 0))
plt.show()