# Introdução à Biblioteca Matplotlib - Parte 2
## Criando Gráficos Customizados com PyLab

# **Pylab** é um módulo fornecido pela biblioteca MatplotLib que combina funcionalidades do pacote NumPy 
# com Pyplot. Fornece um ambiente de plotagem interativo para visualização rápido e fácil de gráficos
# de dados.
# Além de uma gama de tipos de gráficos, permite a personalizar as configurações de plotagem...

# Importando o pacote
import matplotlib as mpl
import matplotlib.pyplot as plt
from pylab import *
# ### 6.1 Gráfico de Linha
# Mostra a evolução do comportamento de uma variável com diferentes pontos de dados. Normalmente utilizado para variáveis contínuas. Cada ponto de dado, representa um ponto na linha. A linha conecta os pontos.
# Muito utilizado para verificação de tendências e padrões em dados ao longo de uma linha temporal.

# Definindo os dados
x = linspace(0, 5, 10)
y =  x ** 2


# Cria a figura de plotagem
fig = plt.figure()

# Define a escala dos eixos, com valores variando de 0 a 1
# [left, bottom, width, height] - [margem esquerda, margem inferior, largura, altura]
#eixos = fig.add_axes([0, 0, 0.8, 0.8]) fica fora o gráfico tanto x e y
# [margem_esquerda, margem_inferior, largura, altura]
# Aumentamos a margem de 0 para 0.1 para dar espaço aos números e labels
eixos = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Cria o plot
eixos.plot(x, y, 'r')


# Define os labels e o título
eixos.set_xlabel('x')
eixos.set_ylabel('y')
eixos.set_title('Gráfico de Linha')

# Obs: Aqui veja que não existe a necessidade de colocar plt.show() pois o Jupyter Notebook é um ambiente interativo.
# em outros ambientes (como scripts locais ou consoles locais) é necessário a inclusão do plt.show().


plt.show()


# Um gráfico dentro de outro gráfico
# Definindo os dados
x = linspace(0, 5, 10)
y =  x ** 2

# Cria a figura de plotagem
fig = plt.figure()

# Define a escala dos eixos
# Eixos da figura principal
eixos1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# Eixos da figura secundária
eixos2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])

# Cria o plot da Figura Principal
eixos1.plot(x, y, 'r')
eixos1.set_xlabel('x')
eixos1.set_ylabel('y')
eixos1.set_title('Figura Principal')

# Cria o plot da Figura Secundária
eixos2.plot(y, x, 'b')
eixos2.set_xlabel('y')
eixos2.set_ylabel('x')
eixos2.set_title('Figura Secundária')

plt.show()



# Gráfico de linha em Paralelo
# Definindo os dados
x = linspace(0, 5, 10)
y =  x ** 2

# Divide a área de plotagem em dois subplots
fig, eixos = plt.subplots(nrows = 1, ncols = 2)

# Loops pelos eixos para criar cada plot
for ex in eixos:
    ex.plot(x, y, 'r')
    ex.set_xlabel('x')
    ex.set_ylabel('y')
    ex.set_title('Título')

# Ajuste do Layout
fig.tight_layout()
plt.show()
# este gráfico pode ser utilizado para comparar o antes e o depois do comportamento de uma variável 
# após uma transformação.


# O comando `fig.tight_layout()` em Matplotlib ajusta automaticamente o layout de uma figura para garantir 
# que os elementos não se sobreponham e que haja espaço suficiente entre eles. Isso inclui ajustamentos para:

# - **Margens**: Ajusta as margens da figura para acomodar rótulos de eixos, títulos e outros elementos 
# de texto, garantindo que não sejam cortados ou sobrepostos.

# - **Subplots**: Se você tiver vários subplots (ou eixos) na figura, `tight_layout()` ajustará 
# automaticamente o espaço entre eles para evitar sobreposições e garantir um layout visualmente agradável.

# - **Padding**: Define o padding (espaçamento) entre os elementos da figura, como entre gráficos, títulos 
# e rótulos.

# ### Outras opções de ajuste de layout

# Além de `tight_layout()`, Matplotlib oferece outras opções para ajustar o layout da figura:

# - **`fig.subplots_adjust()`**: Permite ajustar manualmente as margens da figura e o espaçamento entre subplots.
#  Os parâmetros incluem:

#     - `left`: Espaçamento da margem esquerda.
#     - `right`: Espaçamento da margem direita.
#     - `top`: Espaçamento da margem superior.
#     - `bottom`: Espaçamento da margem inferior.
#     - `wspace`: Espaçamento horizontal entre subplots.
#     - `hspace`: Espaçamento vertical entre subplots.

# - **`plt.subplots()`**: Cria uma figura com subplots, e você pode especificar os parâmetros de ajuste 
# de layout diretamente, como `left`, `right`, `top`, `bottom`, `wspace` e `hspace`.

# - **`fig.constrained_layout`**: Um método mais recente introduzido em Matplotlib para fornecer um ajuste 
# de layout mais rigoroso e preciso do que `tight_layout()`. Para usar o `constrained_layout`, você pode 
# habilitá-lo ao criar a figura: `fig, ax = plt.subplots(constrained_layout=True)`. O `constrained_layout`
# ajusta automaticamente o layout da figura para evitar sobreposições e garantir que os elementos da figura 
# estejam bem alinhados.

# Essas opções oferecem flexibilidade para ajustar o layout da figura de acordo com suas necessidades e 
# preferências.

# Gráfico de linha com diferentes escalas
# Definindo os dados
x = linspace(0, 5, 10)
y =  x ** 2

# Divide a área de plotagem em dois subplots
fig, eixos = plt.subplots(1, 2, figsize=(10, 4))

#Cria o plot 1
eixos[0].plot(x, x**2, x, exp(x))
eixos[0].set_title("Escala Padrão")

#Cria o plot 2
eixos[1].plot(x, x**2, x, exp(x))
eixos[1].set_yscale("log")
eixos[1].set_title("Escala Logaritmica (y)")

plt.show()

# O comando `set_yscale()` em Matplotlib ajusta a escala do eixo y de um gráfico. Além de `"log"` para definir a escala logarítmica, existem outras opções de ajuste de escala que você pode usar:

# - **`"linear"`**: Esta é a escala padrão para os eixos y. A escala linear representa dados de forma linear, com incrementos constantes ao longo do eixo.

# - **`"log"`**: Define a escala logarítmica para o eixo y, o que é útil para visualizar dados que variam em várias ordens de grandeza.

# - **`"symlog"`**: Define uma escala simétrica logarítmica para o eixo y. Esta escala é uma combinação de escala linear para valores próximos de zero e escala logarítmica para valores maiores ou menores que um certo limiar.

# - **`"logit"`**: Define uma escala logit para o eixo y. Esta escala é útil para valores que variam de 0 a 1 e tem uma relação logit com a variável subjacente.

# Você pode usar essas opções conforme necessário para ajustar a escala dos eixos de acordo com as características dos dados que você está visualizando. A escolha da escala correta pode melhorar a interpretação e visualização dos dados.

# Para ajustar a escala, você pode usar o comando `set_yscale()` com um dos valores mencionados acima. Por exemplo:

# - `eixos[1].set_yscale("linear")`
# - `eixos[1].set_yscale("symlog")`
# - `eixos[1].set_yscale("logit")`


# Trabalhando com Grids

# Definindo os dados
x = linspace(0, 5, 10)
y =  x ** 2

# Divide a área de plotagem em dois subplots
fig, eixos = plt.subplots(1, 2, figsize=(10, 3))

#Cria o plot 1 com GRID PADRÃO
eixos[0].plot(x, x**2, x, x**3, lw = 2)
eixos[0].grid(True)

#Cria o plot 2 com GRID CUSTOMIZADO
eixos[1].plot(x, x**2, x, x**3, lw = 2)
eixos[1].grid(color = 'b', alpha = 0.7, linestyle = 'dashed', linewidth = 0.8)

plt.show()

# O método `grid()` em Matplotlib pode ser usado para habilitar ou desabilitar a grade (ou grades) de um gráfico, além de permitir a customização de vários aspectos da aparência da grade. Os parâmetros de customização de grid e o que cada um significa são os seguintes:

# - **`b`**: Controla a visibilidade da grade. `True` para habilitar a grade e `False` para desabilitar. Também pode ser passado como `"both"`, `"x"`, ou `"y"` para especificar quais eixos (ambos, x ou y) devem ter a grade habilitada.

# - **`which`**: Controla para quais escalas a grade será exibida. Pode ser `"major"`, `"minor"`, ou `"both"` para exibir a grade para os ticks maiores, menores, ou ambos.

# - **`axis`**: Especifica o eixo para o qual a grade deve ser exibida. Pode ser `"both"`, `"x"`, ou `"y"` para especificar quais eixos (ambos, x ou y) devem ter a grade habilitada.

# - **`color`**: Define a cor das linhas da grade. Pode ser especificado com uma string que representa a cor (`'b'` para azul, `'g'` para verde, etc.) ou com valores de RGB.

# - **`alpha`**: Define a opacidade das linhas da grade. É um valor entre 0 (transparente) e 1 (opaco).

# - **`linestyle`**: Define o estilo das linhas da grade. Pode ser uma das seguintes opções:
#     - `'solid'`
#     - `'dashed'`
#     - `'dashdot'`
#     - `'dotted'`
#     - Ou uma sequência de números (por exemplo, `[2, 2]` para alternar linhas e espaços com comprimento 2).

# - **`linewidth`**: Define a espessura das linhas da grade.

# - **`zorder`**: Define a ordem z das linhas da grade, influenciando sua sobreposição com outros elementos 
# do gráfico. Elementos com valores mais altos de zorder ficam por cima dos elementos com valores mais baixos.

# Você pode personalizar a grade com base nesses parâmetros para ajustar sua aparência de acordo com suas
# preferências ou necessidades específicas. No último comando, a grade está sendo habilitada com uma cor azul
# (`'b'`), opacidade de 0.7 (`alpha`), estilo de linha tracejada (`'dashed'`) e espessura de linha de 0.8 
# (`linewidth`).


import numpy as np
# Diferentes estilos de plots

# Definindo os dados
x = np.linspace(-0.75, 1., 100)
n = np.array([0,1,2,3,4,5])

# Divide a área de plotagem em quatro subplots
fig, eixos = plt.subplots(1, 4, figsize=(12, 3))

#Cria o plot 1 
eixos[0].scatter(x, x+0.25 * randn(len(x)), color = 'black')
eixos[0].set_title('scatter')

#Cria o plot 2 
eixos[1].step(n, n ** 2, lw = 2, color = 'blue')
eixos[1].set_title('step')

#Cria o plot 3 
eixos[2].bar(n, n ** 2, align = 'center', width = 0.5, alpha = 0.5, color = 'magenta')
eixos[2].set_title('bar')

#Cria o plot 4 
eixos[3].fill_between(x, x**2, x**3, alpha = 0.5, color = 'green')
eixos[3].set_title('fill_between')
plt.show()

### Exemplo: step()

# O método `step()` em Matplotlib cria um gráfico de degraus. Além dos parâmetros `lw` (largura da linha) e `color` (cor da linha) que foram utilizados acima, existem outros parâmetros que você pode usar para personalizar o gráfico de degraus. Aqui estão os principais parâmetros disponíveis e o que cada um significa:

# - **`x`**: Os valores de x para os pontos de dados.

# - **`y`**: Os valores de y para os pontos de dados.

# - **`color`**: Define a cor para a linha. Pode ser uma string que representa a cor (`'b'` para azul, `'g'` para verde, etc.), um código hexadecimal ou uma tupla de RGB.

# - **`lw` ou `linewidth`**: Define a largura da linha. Pode ser um número indicando a espessura da linha.

# - **`linestyle`**: Define o estilo da linha. Pode ser `'solid'`, `'dashed'`, `'dashdot'`, ou `'dotted'`, ou uma sequência personalizada de números (por exemplo, `[2, 2]` para alternar linhas e espaços com comprimento 2).

# - **`marker`**: Define o estilo do marcador nos pontos de dados. Pode ser `'o'` (círculo), `'s'` (quadrado), `'^'` (triângulo para cima), entre outros.

# - **`markersize`**: Define o tamanho do marcador.

# - **`markeredgewidth`**: Define a largura da borda do marcador.

# - **`markeredgecolor`**: Define a cor da borda do marcador.

# - **`markerfacecolor`**: Define a cor do interior do marcador.

# - **`drawstyle`**: Define o estilo da linha de degraus. Pode ser `'default'`, `'steps-pre'`, `'steps-mid'`, ou `'steps-post'` para controlar onde os degraus começam e terminam.

# - **`label`**: Define o rótulo da linha, que pode ser usado em uma legenda.

# - **`alpha`**: Define a opacidade da linha. É um valor entre 0 (transparente) e 1 (opaco).

# - **`zorder`**: Define a ordem z da linha, influenciando sua sobreposição com outros elementos do gráfico. Elementos com valores mais altos de zorder ficam por cima dos elementos com valores mais baixos.

# Você pode usar esses parâmetros para personalizar o gráfico de degraus de acordo com suas preferências ou necessidades específicas. Ajuste os valores conforme necessário para obter a aparência desejada para o seu gráfico.

# Tudo que você precisa está na DOCUMENTAÇÃO: https://matplotlib.org/stable/plot_types/index.html



### 6.2 Histogramas
# São gráficos utilizados para verificar a distribuição de uma variável contínua. A variável é dividida em 
# faixa de valores (intervalos de classe). Uteis para verificar a dispersão dos dados em uma população/amostra 
# de dados.

# Definindo os dados - Gera um array de 100.000 valores aleatórios, com média zero e desvio padrão 1
n = np.random.randn(100000)

# Divide a área de plotagem em dois subplots
fig, eixos = plt.subplots(1, 2, figsize=(12, 4))

#Cria o plot 1 
eixos[0].hist(n)
eixos[0].set_title('Histograma Padrão')
eixos[0].set_xlim((min(n), max(n)))

#Cria o plot 2 
eixos[1].hist(n, cumulative = True, bins = 50)
eixos[1].set_title('Histograma Cumulativo')
eixos[1].set_xlim((min(n), max(n)))
plt.show()
# Um histograma cumulativo exibe a soma acumulada das frequências ao longo dos intervalos.
# Isso significa que, em vez de mostrar a frequência de dados em cada intervalo de forma isolada, 
# ele mostra a soma acumulada dos dados até aquele intervalo.
# O gráfico é uma curva que mostra como a frequência total cresce à medida que os intervalos aumentam.
# serve para identificar quantos dados estão abaixo ou acima de um determinado valor.

### 6.3 Gráficos 3D

# Carregando o pacote 3D do mpl_toolkits do matplotlib
from mpl_toolkits.mplot3d.axes3d import Axes3D

#Definindo os dados
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

#Função para um mapa de cores
def ColorMap(phi_m, phi_p):
    return ( + alpha - 2 * np.cos(phi_p) * cos(phi_m) - alpha * np.cos(phi_ext - 2 * phi_p))

# Mais dados
phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X, Y = np.meshgrid(phi_p, phi_m)
Z = ColorMap(X, Y).T

# Esta célula acima cria uma função para um mapa de cores baseado em variáveis definidas e usa essa função 
# para gerar dados que serão usados para criar um gráfico em 3D na próxima célula.

# Aqui está uma explicação detalhada do que o código faz:

# - **Definindo os dados**:
#     - `alpha = 0.7`: Define uma variável `alpha` com o valor de 0.7.
#     - `phi_ext = 2 * np.pi * 0.5`: Calcula `phi_ext` como 0.5 vezes `2 * np.pi`, ou seja, 0.5 voltas 
# completas em um círculo (radiano).

# - **Função para um mapa de cores**:
#     - `def ColorMap(phi_m, phi_p)`: Define uma função chamada `ColorMap` que recebe dois argumentos, 
# `phi_m` e `phi_p`.
#     - A função retorna um cálculo baseado em `alpha`, `phi_p`, `phi_m` e `phi_ext`. A função utiliza 
# funções `cos` para calcular uma expressão com `alpha`, `phi_p`, `phi_m` e `phi_ext`. Ela retornará o valor calculado, que pode ser usado para gerar um mapa de cores.

# - **Mais dados**:
#     - `phi_m = np.linspace(0, 2*np.pi, 100)`: Gera um array de `phi_m` com 100 valores linearmente 
# espaçados entre 0 e `2 * np.pi` (uma volta completa em um círculo).
#     - `phi_p = np.linspace(0, 2*np.pi, 100)`: Gera um array de `phi_p` com 100 valores linearmente 
# espaçados entre 0 e `2 * np.pi`.
#     - `X, Y = np.meshgrid(phi_p, phi_m)`: Cria uma grade de valores `X` e `Y` usando `phi_p` e `phi_m`. 
# `np.meshgrid` gera uma grade bidimensional combinando `phi_p` e `phi_m`.
#     - `Z = ColorMap(X, Y).T`: Calcula o mapa de cores usando a função `ColorMap` com `X` e `Y` 
# como argumentos, e transposta a matriz resultante (`.T`). O resultado é armazenado em `Z`, que pode ser 
# usado para criar um gráfico de cores.

# Em resumo, o código define uma função para criar um mapa de cores com base em algumas variáveis 
# (`alpha` e `phi_ext`) e usa essa função para calcular uma matriz `Z` de valores de cores com base nos valores 
# `X` e `Y`. Os valores de `Z` serão utilizados para visualizar um gráfico de cores na próxima célula.


# Cria a figura
fig = plt.figure(figsize = (14, 6))

#Adiciona o subplot 1 com projeção 3D
ax = fig.add_subplot(1, 2, 1, projection = '3d')
p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth = 0)

#Adiciona o subplot 2 com projeção 3D
ax = fig.add_subplot(1, 2, 2, projection = '3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth = 0, antialiased=False)

# Cria a barra de cores com legenda
cb = fig.colorbar(p, shrink=0.5)

plt.show()

# O trecho de código complementa o código anterior e cria uma figura (`fig`) com dois subplots, 
# ambos com projeção 3D:

# - **Cria a figura**:
#     - `fig = plt.figure(figsize = (14, 6))`: Cria uma figura com o tamanho especificado 
# (`14` de largura e `6` de altura).

# - **Adiciona o subplot 1 com projeção 3D**:
#     - `ax = fig.add_subplot(1, 2, 1, projection = '3d')`: Adiciona um subplot com projeção 3D à figura 
# na posição `(1, 2, 1)`. Isso significa que há 1 linha, 2 colunas, e este é o primeiro subplot.
#     - `p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth = 0)`: Plota uma superfície 3D no 
# subplot usando os dados `X`, `Y`, e `Z`. Os parâmetros `rstride=4` e `cstride=4` controlam o espaçamento
# entre as linhas e colunas da grade na superfície plotada. `linewidth = 0` significa que as linhas da grade 
# não têm espessura, ou seja, não são visíveis.

# - **Adiciona o subplot 2 com projeção 3D**:
#     - `ax = fig.add_subplot(1, 2, 2, projection = '3d')`: Adiciona outro subplot com projeção 3D à figura 
# na posição `(1, 2, 2)`, o que significa que este é o segundo subplot em uma linha com duas colunas.
#     - `p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth = 0, antialiased=False)`
# : Plota outra superfície 3D no segundo subplot usando os dados `X`, `Y`, e `Z`. Os parâmetros `rstride=1` e `
# cstride=1` definem o espaçamento entre as linhas e colunas da grade na superfície plotada como `1`, 
# criando uma superfície mais detalhada. `cmap=cm.coolwarm` define o mapa de cores `coolwarm` para colorir 
# a superfície. `antialiased=False` desabilita a suavização das bordas da superfície.

# - **Cria a barra de cores com legenda**:
#     - `cb = fig.colorbar(p, shrink=0.5)`: Cria uma barra de cores (ou colorbar) para a figura.
#  A barra de cores é associada à superfície plotada (`p`). O parâmetro `shrink=0.5` redimensiona a
#  barra de cores para 50% do tamanho original, tornando-a menor.

# Este código visualiza duas superfícies 3D com configurações diferentes em uma mesma figura, uma com 
# um padrão de grade espaçado e outra com uma superfície mais detalhada usando um mapa de cores específico. 
# A barra de cores associada à superfície oferece uma legenda visual para os valores de `Z` na superfície.


# Wire frame

# cria a figura
fig = plt.figure(figsize = (8,6))

# subplot
ax = fig.add_subplot(1,1,1,projection='3d')

#wireframe
p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)

plt.show()