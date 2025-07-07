# Importa as bibliotecas necessárias: tkinter para a interface 
        # gráfica e pandas para manipulação de dados
import tkinter as tk
import pandas as pd

# Função para carregar os dados do Excel na tabela Tkinter
def carregar_dados_do_excel(filtro=None):
    
    # Carrega os dados de um arquivo Excel especificado 
            # em um DataFrame pandas.
    # 'pd.read_excel("tabela_exemplo.xlsx")' lê o arquivo 
            # 'tabela_exemplo.xlsx' e armazena os dados em 'df'.
    df = pd.read_excel("tabela_exemplo.xlsx")

    # Obtém uma lista dos nomes das colunas do DataFrame.
    # 'df.columns' retorna um objeto Index contendo os 
            # nomes das colunas do DataFrame.
    # 'list(df.columns)' converte este objeto Index em 
            # uma lista chamada 'colunas'.
    colunas = list(df.columns)
    
    # Verifica se um filtro foi fornecido como argumento para a função.
    if filtro:
        
        # Filtra o DataFrame baseado no critério especificado.
        # 'df.apply(lambda ...)' aplica uma função que converte 
                # cada linha para string, 
                # torna todas as letras minúsculas e verifica se o 
                # texto do filtro está presente.
        # 'axis=1' indica que a função deve ser aplicada em 
                # cada linha (e não em cada coluna).
        # O resultado é um DataFrame 'df' atualizado que contém 
                # apenas as linhas que correspondem ao filtro.
        df = df[df.apply(lambda row: filtro.lower() in row.astype(str).str.lower().to_string(), axis=1)]
    
    # Atualiza o cabeçalho da tabela Tkinter com os nomes 
            # das colunas do DataFrame.
    # Este loop percorre a lista 'colunas', e 'enumerate(colunas)' 
            # fornece tanto o índice (j) quanto o valor (coluna).
    for j, coluna in enumerate(colunas):
        
        # Configura o texto de cada célula do cabeçalho para o 
                # nome correspondente da coluna.
        # 'cabecalho[j].config(text=coluna)' define a propriedade 'text' 
                # da célula de cabeçalho no índice 'j' para o nome da coluna.
        cabecalho[j].config(text=coluna)


    # Atualizar a tabela com os dados filtrados
    # Este bloco de código é responsável por preencher a tabela Tkinter 
            # com os dados provenientes do DataFrame pandas, que 
            # pode ter sido filtrado.
    for i in range(len(tabela)):
        # 'i' é o índice da linha na tabela Tkinter. 'len(tabela)' 
                # fornece o número total de linhas na tabela Tkinter.
        # Este loop externo percorre cada linha da tabela Tkinter.
    
        for j in range(len(tabela[i])):
            # 'j' é o índice da coluna na linha atual da tabela Tkinter. 
                    # 'len(tabela[i])' fornece o número total de 
                    # células (colunas) na linha 'i'.
            # Este loop interno percorre cada célula (coluna) em uma 
                    # linha específica da tabela Tkinter.
    
            if i < len(df):
                # Esta condição verifica se o índice da linha 'i' é menor 
                        # que o número de linhas no DataFrame 'df'.
                # Se for verdadeiro, significa que ainda há dados no DataFrame 'df' 
                        # para serem exibidos na linha atual da tabela Tkinter.
    
                # 'df.iloc[i, j]' acessa o valor na linha 'i' e coluna 'j' do DataFrame 'df'.
                # '.iloc' é um indexador para Pandas DataFrame usado para acessar 
                        # uma célula específica por índice numérico.
                # 'tabela[i][j].config(text=df.iloc[i, j])' configura o texto 
                        # da célula especificada na tabela Tkinter para o valor 
                        # correspondente do DataFrame.
                tabela[i][j].config(text=df.iloc[i, j])
    
            else:
                # Se o índice 'i' for igual ou maior que o número de linhas no 
                        # DataFrame, não há mais dados para serem exibidos.
                # Essa condição é importante para lidar com casos onde a tabela 
                        # Tkinter tem mais linhas do que há dados disponíveis 
                        # no DataFrame filtrado.
    
                # 'tabela[i][j].config(text="")' limpa o texto da célula na 
                        # linha 'i' e coluna 'j' da tabela Tkinter.
                # Isso é feito configurando o texto da célula para uma string 
                        # vazia, efetivamente "limpando" quaisquer dados antigos 
                        # que não sejam mais relevantes após o filtro.
                tabela[i][j].config(text="")
    

# Função para destacar a célula, coluna e linha ao passar o mouse
def destacar_celula(event):
    # A função é acionada quando o cursor do mouse entra em 
            # uma célula da tabela.

    # A função `grid_info()` retorna um dicionário contendo detalhes 
            # sobre a localização do widget (célula) na grade.
    # `['row']` acessa a linha em que o widget está localizado. 
            # Subtrair 3 ajusta o índice da linha porque as três primeiras
    # linhas podem estar reservadas para o cabeçalho e outros 
            # controles de interface, como caixas de entrada ou botões.
    linha = event.widget.grid_info()['row'] - 3

    # `['column']` acessa a coluna em que o widget está localizado, sem 
            # necessidade de ajuste porque começa diretamente da primeira coluna.
    coluna = event.widget.grid_info()['column']

    # A condição verifica se os índices de linha e coluna estão 
            # dentro dos limites válidos da tabela para evitar erros.
    # Isso é essencial para garantir que a função só tente destacar 
            # células que existam na matriz `tabela`.
    if 0 <= linha < len(tabela) and 0 <= coluna < len(tabela[0]):
        
        # Limpar todos os destaques anteriores na tabela.
        # Isso é necessário para remover qualquer destaque anterior 
                # quando o mouse se move para uma nova célula.
        for i in range(len(tabela)):  # Itera sobre cada linha da tabela
            
            for j in range(len(tabela[i])):  # Itera sobre cada coluna na linha
                
                # Configura o fundo para branco, o texto para preto e a 
                        # fonte para Arial tamanho 10.
                # Este passo "reseta" a aparência de cada célula para o 
                        # estado padrão antes de aplicar um novo destaque.
                tabela[i][j].config(bg="white", 
                                    fg="black", 
                                    font=("Arial", 10))


        # Destacar a célula atual com fundo amarelo e aumento de fonte
        tabela[linha][coluna].config(bg="yellow", 
                                     fg="black", 
                                     font=("Arial", 14, "bold"))
        # Esta linha altera a configuração da célula onde o 
                # mouse está atualmente posicionado.
        # 'bg="yellow"' define a cor de fundo da célula para 
                # amarelo, tornando-a claramente visível como o foco atual.
        # 'fg="black"' define a cor do texto dentro da célula para preto, 
                # garantindo boa legibilidade contra o fundo amarelo.
        # 'font=("Arial", 14, "bold")' muda a fonte para Arial, 
                # tamanho 14, e em negrito, o que aumenta a célula 
                # visualmente e destaca o texto.
        
        # Destacar a linha inteira
        for j in range(len(tabela[linha])):
            
            # Esta linha inicia um loop que passa por cada célula na 
                    # linha onde o mouse está posicionado.
            if j != coluna:  # Evitar sobrescrever o destaque da célula atual
                
                # Este 'if' verifica se a célula atual no loop é diferente 
                        # da célula onde o mouse está.
                # Isso é necessário para evitar alterar a cor de fundo da 
                        # célula já destacada em amarelo.
                tabela[linha][j].config(bg="lightgray")
                # 'bg="lightgray"' define o fundo das outras células 
                        # na linha para cinza claro.
                # Isso ajuda a destacar toda a linha, mas mantém a célula 
                        # sob o cursor em destaque com fundo amarelo.
        
        # Destacar a coluna inteira
        for i in range(len(tabela)):
            
            # Esta linha inicia um loop que passa por cada célula na 
                    # coluna onde o mouse está posicionado.
            if i != linha:  # Evitar sobrescrever o destaque da célula atual
                
                # Este 'if' verifica se a célula atual no loop é 
                        # diferente da célula onde o mouse está.
                # Assim como no loop da linha, isso evita mudar a 
                        # cor da célula já destacada em amarelo.
                tabela[i][coluna].config(bg="lightgray")
                # 'bg="lightgray"' define o fundo das outras células 
                        # na coluna para cinza claro.
                # Isso ajuda a destacar toda a coluna, enquanto a célula 
                        # sob o cursor permanece mais visível com fundo amarelo.


# Função para restaurar o destaque ao remover o mouse da célula
def restaurar_celula(event):
    # A função é chamada quando o cursor do mouse 
            # sai de uma célula da tabela.
    
    # Este loop externo itera sobre cada linha da tabela. 
            # 'len(tabela)' fornece o número total de linhas na tabela.
    for i in range(len(tabela)):
        
        # Este loop interno itera sobre cada célula dentro de uma linha 
                # específica. 'len(tabela[i])' fornece o número de 
                # células em uma linha específica.
        for j in range(len(tabela[i])):
            
            # 'tabela[i][j].config(...)' configura as propriedades 
                    # visuais da célula na posição [i][j].
            # 'bg="white"' define a cor de fundo da célula para branco, 
                    # retornando a célula ao seu estado visual original.
            # 'fg="black"' define a cor do texto para preto, assegurando que o 
                    # texto dentro da célula seja fácil de ler contra o fundo branco.
            # 'font=("Arial", 10)' define a fonte do texto para Arial tamanho 10, 
                    # que é a fonte padrão e tamanho originalmente definido para as células.
            tabela[i][j].config(bg="white", 
                                fg="black", 
                                font=("Arial", 10))


    
# Função para aplicar filtro em tempo real
def aplicar_filtro(event):
    # Esta função é chamada sempre que ocorre um evento de liberação 
            # de tecla no campo de entrada do filtro.

    # 'entrada_filtro.get()' acessa o valor atualmente inserido no 
            # campo de entrada do filtro.
    # '.get()' é um método que retorna o conteúdo atual de um widget 
            # de entrada (Entry) em Tkinter.
    filtro = entrada_filtro.get()

    # Chama a função 'carregar_dados_do_excel' passando o filtro 
            # atual como argumento.
    # 'filtro=filtro' passa o valor do filtro para a função que 
            # carrega os dados, permitindo que ela ajuste
            # quais dados são exibidos com base no texto inserido.
    carregar_dados_do_excel(filtro=filtro)
    

# Função para exportar os dados da tabela para um novo arquivo Excel
def exportar_para_excel():
    # Esta função é responsável por coletar os dados exibidos na 
            # tabela Tkinter e salvar em um arquivo Excel.

    # Cria uma lista vazia chamada 'dados' que irá armazenar todas as 
            # linhas da tabela, onde cada linha é uma lista de valores de células.
    dados = []
    
    # 'len(tabela)' fornece o número total de linhas na tabela Tkinter.
    # Este loop externo itera por cada linha da tabela Tkinter.
    for i in range(len(tabela)):
        
        # Cria uma lista vazia chamada 'linha' que irá armazenar os 
                # valores de cada célula da linha atual.
        linha = []
        
        # 'len(tabela[i])' fornece o número total de 
                # células (colunas) na linha 'i'.
        # Este loop interno itera por cada célula (coluna) na 
                # linha atual da tabela Tkinter.
        for j in range(len(tabela[i])):
            
            # 'tabela[i][j].cget("text")' obtém o texto atualmente 
                    # exibido na célula na posição [i][j] da tabela.
            # '.cget("text")' é um método para obter o valor de uma opção 
                    # configurável para um widget Tkinter, neste caso, a opção 'text'.
            valor = tabela[i][j].cget("text")
            
            # Adiciona o valor obtido à lista 'linha'.
            linha.append(valor)
        
        # Após coletar todos os valores de uma linha, adiciona a 
                # lista 'linha' à lista 'dados'.
        # Agora, 'dados' contém mais uma linha de valores 
                # da tabela Tkinter.
        dados.append(linha)

    
    # Transforma a lista de listas 'dados' em um DataFrame pandas.
    # 'pd.DataFrame()' é a função usada para criar um DataFrame a 
            # partir de dados estruturados.
    # 'dados' é a lista de listas onde cada lista interna representa 
            # uma linha de dados da tabela Tkinter.
    df = pd.DataFrame(dados,
                      
                      # 'columns' define os nomes das colunas do DataFrame.
                      # Este código cria uma lista dos nomes das colunas, obtendo o 
                              # texto de cada célula do cabeçalho da tabela Tkinter.
                      # '[cabecalho[j].cget("text") for j in range(len(cabecalho))]' é 
                              # uma compreensão de lista que percorre cada célula do cabeçalho,
                      # usa '.cget("text")' para obter o nome da coluna armazenado em 
                              # cada cabeçalho, e cria uma lista com esses nomes.
                      columns=[cabecalho[j].cget("text") for j in range(len(cabecalho))])
    
    # Exporta o DataFrame 'df' para um arquivo Excel.
    # 'df.to_excel("tabela_exportada.xlsx", index=False)' é o método 
            # usado para salvar o DataFrame em um arquivo Excel.
    # 'tabela_exportada.xlsx' é o nome do arquivo para o qual os dados serão salvos.
    # 'index=False' é uma opção que impede que pandas crie uma coluna 
            # adicional no Excel para armazenar os índices de linha do DataFrame.
    df.to_excel("tabela_exportada.xlsx", index=False)
    
    # Imprime uma mensagem no console para informar que os dados 
            # foram exportados com sucesso.
    # 'print("Dados exportados para tabela_exportada.xlsx")' simplesmente 
            # mostra uma mensagem indicando que a operação foi concluída,
            # o que é útil para feedback em scripts que podem levar 
            # algum tempo para processar.
    print("Dados exportados para tabela_exportada.xlsx")


# Janela principal
# 'tk.Tk()' cria a janela raiz do aplicativo Tkinter, que serve como o 
        # contêiner principal para todos os outros widgets.
janela = tk.Tk()

# 'janela.title("Tabela Interativa com Dados de Excel")' 
        # define o título da janela.
# Este título aparece na barra de título da janela e ajuda a identificar o 
        # propósito da interface para o usuário.
janela.title("Tabela Interativa com Dados de Excel")

# Cria um widget de rótulo (Label) que serve como título 
        # para a tabela na interface gráfica.
titulo = tk.Label(janela, 
                  
                  # 'text="Tabela de Informações"' define o texto que 
                          # será exibido no rótulo, servindo como título da tabela.
                  text="Tabela de Informações", 
                  
                  # 'font=("Arial", 16, "bold")' configura a fonte do 
                          # texto no rótulo. "Arial" é o tipo de fonte,
                          # 16 é o tamanho da fonte, e "bold" indica que o 
                          # texto será em negrito.
                  font=("Arial", 16, "bold"))

# Posiciona o rótulo do título na janela principal usando o 
        # gerenciador de layout 'grid'.
titulo.grid(row=0, 
            
            # 'row=0' posiciona o rótulo na primeira linha da grade.
            column=0, 
            
            # 'column=0' posiciona o rótulo na primeira coluna.
            columnspan=5, 
            
            # 'columnspan=5' faz com que o rótulo se estenda por cinco 
                    # colunas, garantindo que ele ocupe a largura 
                    # necessária para ser visível.
            pady=10)
            # 'pady=10' adiciona um espaço vertical de 10 pixels acima e 
                    # abaixo do título para separá-lo visualmente dos 
                    # outros elementos da interface.


# Cria um widget de entrada (Entry) que permite aos usuários 
        # digitar um filtro para os dados da tabela.
entrada_filtro = tk.Entry(janela, 
                          
                          # 'font=("Arial", 12)' configura a fonte do 
                                  # texto dentro da entrada. "Arial" é o 
                                  # tipo de fonte e 12 é o tamanho.
                          font=("Arial", 12))

# Posiciona o campo de entrada na janela principal usando o 
        # gerenciador de layout 'grid'.
entrada_filtro.grid(row=1, 
                    
                    # 'row=1' posiciona o campo de entrada na 
                            # segunda linha da grade.
                    column=0, 
                    
                    # 'column=0' posiciona o campo na primeira coluna.
                    columnspan=4, 
                    
                    # 'columnspan=4' faz com que o campo de entrada 
                            # se estenda por quatro colunas.
                    padx=5, 
                    
                    # 'padx=5' adiciona um espaço horizontal de 5 pixels à 
                            # esquerda e à direita do campo de entrada.
                    pady=5, 
                    
                    # 'pady=5' adiciona um espaço vertical de 5 pixels 
                            # acima e abaixo do campo de entrada.
                    sticky="ew")
                    # 'sticky="ew"' faz com que o campo de entrada se estique 
                            # para preencher toda a largura disponível, garantindo 
                            # que use todo o espaço horizontal das colunas que ocupa.

# Vincula um evento ao campo de entrada para que a função 'aplicar_filtro' 
        # seja chamada sempre que o usuário liberar uma tecla.
entrada_filtro.bind("<KeyRelease>", 
                    
                    # "<KeyRelease>" é o evento que é disparado sempre 
                            # que uma tecla é liberada.
                    aplicar_filtro)
                    # 'aplicar_filtro' é a função que será chamada quando o 
                            # evento ocorrer, permitindo atualizar os dados exibidos 
                            # na tabela com base no texto digitado no campo de entrada.


# Cria um widget de botão que permitirá aos usuários exportar os dados da 
        # tabela para um arquivo Excel.
btn_exportar = tk.Button(janela, 
                         
                         # 'text="Exportar para Excel"' define o texto que será 
                                 # exibido no botão, orientando o usuário 
                                 # sobre sua funcionalidade.
                         text="Exportar para Excel", 
                         
                         # 'command=exportar_para_excel' vincula o botão à função 
                                 # 'exportar_para_excel', que será chamada quando o 
                                 # botão for clicado.
                         command=exportar_para_excel, 
                         
                         # 'font=("Arial", 12)' define a fonte do texto no 
                                 # botão para Arial, tamanho 12.
                         font=("Arial", 12))

# Posiciona o botão na janela principal usando o 
        # gerenciador de layout 'grid'.
btn_exportar.grid(row=1, 
                  
                  # 'row=1' posiciona o botão na mesma linha que o 
                          # campo de entrada de filtro.
                  column=4, 
                  
                  # 'column=4' coloca o botão na quinta coluna.
                  padx=5, 
                  
                  # 'padx=5' adiciona um espaço horizontal de 5 
                          # pixels à esquerda e à direita do botão.
                  pady=5)
                  # 'pady=5' adiciona um espaço vertical de 5 pixels 
                            # acima e abaixo do botão.


# Carrega dados de um arquivo Excel especificado em 
        # um DataFrame pandas.
df = pd.read_excel("tabela_exemplo.xlsx")
# 'pd.read_excel("tabela_exemplo.xlsx")' lê o arquivo 'tabela_exemplo.xlsx' e 
        # armazena os dados no DataFrame 'df'.

# Determina o número de colunas e linhas com base 
        # nos dados carregados.
colunas = len(df.columns)

# 'len(df.columns)' conta o número total de 
        # colunas no DataFrame 'df'.
linhas = len(df)
# 'len(df)' conta o número total de linhas no DataFrame 'df'.


# Inicia uma lista vazia chamada 'cabecalho' para armazenar 
        # referências aos widgets de cabeçalho de coluna.
cabecalho = []
# Esta lista será preenchida com widgets Label que exibirão os 
        # nomes das colunas na interface gráfica.

# Este laço itera através do número de colunas determinado 
        # anteriormente pelos dados carregados do Excel.
for j in range(colunas):
    
    # Cria um widget Label para cada coluna. Este rótulo servirá 
            # como cabeçalho de coluna na tabela.
    celula_cabecalho = tk.Label(janela, 
                                
                                # 'text=""' inicialmente, o texto do cabeçalho está vazio. 
                                        # Será configurado depois, com base nos nomes 
                                        # das colunas do DataFrame.
                                text="", 
                                
                                # 'bg="lightblue"' define a cor de fundo do cabeçalho 
                                        # para azul claro, ajudando a diferenciá-lo 
                                        # visualmente das células de dados.
                                bg="lightblue", 
                                
                                # 'fg="black"' define a cor do texto para preto, 
                                        # garantindo boa legibilidade contra o fundo claro.
                                fg="black", 
                                
                                # 'width=12' e 'height=2' definem a largura e altura 
                                        # do cabeçalho, respectivamente.
                                width=12, height=2, 
                                
                                # 'borderwidth=1' e 'relief="solid"' definem a espessura da 
                                        # borda e o estilo de relevo para o rótulo, 
                                        # tornando-o mais destacado.
                                borderwidth=1, relief="solid", 
                                
                                # 'font=("Arial", 12, "bold")' define a fonte do texto 
                                        # para Arial, tamanho 12, em negrito, tornando o 
                                        # texto do cabeçalho mais proeminente.
                                font=("Arial", 12, "bold"))

    # Posiciona cada célula de cabeçalho na segunda linha da janela 
            # principal usando o gerenciador de layout 'grid'.
    celula_cabecalho.grid(row=2, 
                          
                          # 'row=2' posiciona o cabeçalho na terceira linha 
                                  # da janela (contando a partir de 0).
                          column=j, 
                          
                          # 'column=j' coloca cada cabeçalho de coluna na 
                                  # coluna correspondente a seu índice no laço.
                          sticky="nsew")
                          # 'sticky="nsew"' faz com que o cabeçalho se expanda e adira a 
                                    # todas as direções (norte, sul, leste, oeste) dentro de 
                                    # sua célula de grade, preenchendo completamente o espaço disponível.

    # Adiciona o widget Label recém-criado à lista 'cabecalho', 
            # que armazena todas as células de cabeçalho.
    cabecalho.append(celula_cabecalho)


# Inicia uma lista vazia chamada 'tabela' que irá armazenar todas 
        # as linhas da tabela, onde cada linha é uma lista de 
        # células (widgets Label).
tabela = []

# Este laço externo itera sobre o número de linhas determinado 
        # anteriormente pelos dados carregados do Excel.
for i in range(linhas):
    
    # Inicia uma lista vazia chamada 'linha' que irá armazenar os 
            # widgets Label para cada célula da linha atual.
    linha = []
    
    # Este laço interno itera sobre o número de colunas 
            # determinado anteriormente.
    for j in range(colunas):
        
        # Cria um widget Label para cada célula da tabela.
        celula = tk.Label(janela, 
                          
                          # 'text=""' inicialmente, o texto da célula está vazio. 
                                  # Ele será configurado posteriormente com os dados do Excel.
                          text="", 
                          
                          # 'bg="white"' define a cor de fundo da célula para branco, 
                                  # garantindo um fundo neutro para os dados.
                          bg="white", 
                          
                          # 'fg="black"' define a cor do texto para preto, garantindo 
                                  # boa legibilidade contra o fundo branco.
                          fg="black", 
                          
                          # 'width=12', 'height=3' definem a largura e altura da célula, 
                                  # respectivamente, para manter uma apresentação uniforme.
                          width=12, height=3, 
                          
                          # 'borderwidth=1', 'relief="solid"' definem a espessura da borda e o 
                                  # estilo de relevo para a célula, dando uma aparência 
                                  # clara e delimitada.
                          borderwidth=1, relief="solid", 
                          
                          # 'font=("Arial", 10)' define a fonte do texto para Arial, 
                                  # tamanho 10, o que é adequado para a maioria das 
                                  # informações tabulares.
                          font=("Arial", 10))
        
        # Posiciona a célula na janela principal usando o gerenciador de layout 'grid'.
        celula.grid(row=i+3, 
                    
                    # 'row=i+3' posiciona a célula na linha correta, começando na quarta 
                            # linha da janela (considerando que as três primeiras linhas 
                            # podem ser usadas para título, filtros, etc.).
                    column=j, 
                    
                    # 'column=j' coloca a célula na coluna correspondente.
                    sticky="nsew")
                    # 'sticky="nsew"' faz com que a célula se expanda e adira a 
                            # todas as direções dentro de sua célula de grade, 
                            # preenchendo completamente o espaço disponível.

        # Vincula eventos às células para destacar ao passar o mouse e 
                # restaurar ao retirar o mouse.
        celula.bind("<Enter>", destacar_celula)
        
        # '<Enter>' é um evento que é disparado quando o cursor 
                # do mouse entra em uma célula.
        celula.bind("<Leave>", restaurar_celula)
        # '<Leave>' é um evento que é disparado quando o cursor 
                # do mouse sai de uma célula.

        # Adiciona o widget Label recém-criado à lista 'linha'.
        linha.append(celula)
    
    # Após criar todas as células de uma linha, adiciona a 
            # lista 'linha' à lista 'tabela'.
    # Isso constrói a tabela como uma lista de listas, onde cada 
            # lista interna representa uma linha da tabela.
    tabela.append(linha)


# Configurar as colunas para ajustar o tamanho conforme a 
        # tabela é redimensionada.
for j in range(colunas):
    # Este laço percorre cada coluna definida anteriormente a 
            # partir do número de colunas do DataFrame.

    # 'grid_columnconfigure(j, weight=1)' configura o comportamento de 
            # redimensionamento da coluna 'j'.
    # 'j' é o índice da coluna na grade da janela.
    # 'weight=1' atribui um peso de redimensionamento para a coluna, 
            # permitindo que ela cresça ou encolha proporcionalmente 
            # quando a janela é redimensionada.
    # Um 'weight' maior que 0 permite que a coluna se ajuste dinamicamente 
            # ao tamanho da janela, contribuindo para uma interface responsiva.
    janela.grid_columnconfigure(j, weight=1)


# Configurar as linhas para ajustar o tamanho conforme a 
        # tabela é redimensionada.
for i in range(linhas):
    # Este laço percorre cada linha a partir do número de 
            # linhas do DataFrame.

    # 'grid_rowconfigure(i+3, weight=1)' configura o comportamento de 
            # redimensionamento da linha 'i+3'.
    # 'i+3' é o índice da linha na grade da janela, começando da quarta 
            # linha, pois as três primeiras podem ser usadas para 
            # outros controles, como título e filtros.
    # 'weight=1' atribui um peso de redimensionamento para a linha, 
            # similar ao das colunas, permitindo que ela se ajuste dinamicamente.
    # Isso assegura que as linhas da tabela também cresçam ou encolham 
            # proporcionalmente com mudanças no tamanho da janela.
    janela.grid_rowconfigure(i+3, weight=1)


# Carregar os dados do Excel na tabela. Esta função foi definida anteriormente 
        # e é responsável por extrair os dados de um arquivo Excel e 
        # populá-los na tabela Tkinter.
carregar_dados_do_excel()

# Iniciar o loop principal da interface
janela.mainloop()