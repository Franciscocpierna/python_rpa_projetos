# Importa o módulo tkinter para criar interfaces 
        # gráficas de usuário (GUIs) em Python.
import tkinter as tk

# Importa componentes adicionais de tkinter, incluindo ttk 
        # para widgets estilizados e filedialog para diálogos de arquivo.
from tkinter import ttk, filedialog

# Importa a biblioteca pandas, uma ferramenta poderosa para 
        # análise de dados e manipulação de tabelas.
import pandas as pd


# Define a função 'exportar_dados_filtrados' para permitir ao 
            # usuário salvar os dados filtrados em um arquivo Excel.
def exportar_dados_filtrados():
    
    # Usa a função 'asksaveasfilename' do módulo 'filedialog' para abrir 
            # uma janela de diálogo onde o usuário pode escolher o nome 
            # do arquivo e o local para salvar.
    # 'defaultextension=".xlsx"' garante que o arquivo seja salvo com a 
            # extensão .xlsx, padrão dos arquivos Excel modernos.
    # 'filetypes=[("Excel files", "*.xlsx")]' limita os tipos de arquivos no 
            # diálogo para arquivos Excel (.xlsx), facilitando para o 
            # usuário encontrar o formato correto.
    arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", 
                                           filetypes=[("Excel files", "*.xlsx")])

    # Verifica se um nome de arquivo foi fornecido. A variável 'arquivo' 
            # será False se o usuário cancelar a operação de salvar.
    if arquivo:
        
        # Se um arquivo foi especificado, os dados do DataFrame 'df_filtrado' 
                # são salvos neste arquivo.
        # 'df_filtrado.to_excel(arquivo, index=False)' salva o DataFrame no 
                # arquivo escolhido, com a opção 'index=False' para não incluir 
                # os índices do DataFrame como uma coluna extra no arquivo Excel.
        df_filtrado.to_excel(arquivo, index=False)
        

# Define uma função chamada 'calcular_media_situacao' que 
        # aceita um DataFrame 'df' como argumento.
def calcular_media_situacao(df):
    
    # Calcula a média das colunas especificadas para cada linha. 
    # 'df[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']]' seleciona 
            # essas colunas do DataFrame.
    # '.mean(axis=1)' calcula a média ao longo do eixo das 
            # colunas (axis=1 significa operação linha por linha).
    # '.round(2)' arredonda o resultado para duas casas decimais.
    df['Média'] = df[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1).round(2)
    
    # Define uma função interna 'definir_situacao' para 
            # avaliar a situação de cada aluno.
    def definir_situacao(linha):
        
        # Avalia se o número de faltas na linha é maior que 10. 
                # Se sim, retorna 'Reprovado por Faltas'.
        if linha['Faltas'] > 10:
            return 'Reprovado por Faltas'
            
        # Verifica se a média calculada é maior ou igual a 7. 
                # Se verdadeiro, retorna 'Aprovado'.
        elif linha['Média'] >= 7:
            return 'Aprovado'
            
        # Verifica se a média é menor que 2. Se verdadeiro, 
                # retorna 'Reprovado por Notas'.
        elif linha['Média'] < 2:
            return 'Reprovado por Notas'
            
        # Se nenhuma das condições acima for atendida, 
                # retorna 'Recuperação'.
        else:
            return 'Recuperação'
    
    # Aplica a função 'definir_situacao' a cada linha do DataFrame 
            # para determinar a situação do aluno.
    # 'df.apply(func, axis=1)' aplica a função 'func' em 
            # cada linha do DataFrame.
    df['Situação'] = df.apply(definir_situacao, axis=1)
    
    # Retorna o DataFrame atualizado com as novas 
            # colunas 'Média' e 'Situação'.
    return df


# Define uma função chamada 'carregar_dados' para carregar e 
            # processar os dados de um arquivo Excel.
def carregar_dados():
    
    # Declara 'df_original', 'num_paginas', e 'pagina_atual' como variáveis globais.
    # Isso permite que essas variáveis sejam acessadas e modificadas fora da função.
    global df_original, num_paginas, pagina_atual

    # Carrega os dados do arquivo Excel 'notas_estudantes.xlsx' 
            # na aba (sheet) chamada 'Dados'.
    # O método 'pd.read_excel()' é usado para ler o arquivo, onde 
            # 'sheet_name' especifica a aba a ser lida.
    df_original = pd.read_excel('notas_estudantes.xlsx', 
                                sheet_name='Dados')

    # Aplica a função 'calcular_media_situacao' ao DataFrame 'df_original'.
    # Esta função calcula a média das notas e determina a situação de cada aluno,
    # adicionando colunas 'Média' e 'Situação' ao DataFrame.
    df_original = calcular_media_situacao(df_original)
    
    # Chama a função 'aplicar_filtro()', que filtra os dados baseados 
            # em um critério de pesquisa, se fornecido.
    # Este passo é importante para inicializar a visualização dos 
            # dados de acordo com algum filtro pré-definido.
    aplicar_filtro()

    

# Define a função 'aplicar_filtro' que não recebe 
            # argumentos externos.
def aplicar_filtro():
    
    # Declara 'df_filtrado', 'num_paginas' e 'pagina_atual' 
            # como variáveis globais.
    # Essa declaração permite que essas variáveis sejam acessadas e 
            # modificadas em todo o programa.
    global df_filtrado, num_paginas, pagina_atual

    # Obtém o termo de pesquisa digitado no campo de entrada, 
            # converte para letras minúsculas com '.lower()'.
    # 'entrada_filtro.get()' pega o texto atual do campo 
            # de entrada 'entrada_filtro'.
    termo = entrada_filtro.get().lower()

    # Filtra o DataFrame 'df_original' para incluir apenas as 
            # linhas que contêm o termo de pesquisa.
    # 'df_original.apply(lambda row: termo in row.to_string(index=False).lower(), axis=1)' verifica cada linha:
    #   - 'row.to_string(index=False)' converte a linha para uma string
            # sem incluir os índices.
    #   - 'termo in ... .lower()' verifica se o termo convertido em 
            # minúsculas está na string da linha também em minúsculas.
    df_filtrado = df_original[df_original.apply(lambda row: termo in row.to_string(index=False).lower(), axis=1)]
    
    # Calcula o número total de páginas necessárias para exibir os 
            # dados filtrados, assumindo 5 linhas por página.
    # '(len(df_filtrado) // 5)' realiza uma divisão inteira do 
            # número de linhas filtradas por 5.
    # '+ (1 if len(df_filtrado) % 5 != 0 else 0)' adiciona uma página 
            # extra se houver um resto na divisão, indicando que há 
            # linhas adicionais que precisam de uma página extra.
    num_paginas = (len(df_filtrado) // 5) + (1 if len(df_filtrado) % 5 != 0 else 0)

    # Define a página atual como 1, reiniciando a visualização 
            # para a primeira página após aplicar um novo filtro.
    pagina_atual = 1
    
    # Chama a função 'exibir_pagina' para atualizar a visualização 
            # dos dados conforme o filtro aplicado.
    exibir_pagina()


# Define a função 'exibir_pagina' que não recebe argumentos e é 
        # responsável por mostrar a página atual dos dados na interface gráfica.
def exibir_pagina():
    
    # Calcula o índice de início para a paginação, baseado na página atual.
    # 'pagina_atual - 1' transforma o número da página em índice base-0, 
            # multiplicado por 5 para obter o índice inicial.
    inicio_idx = (pagina_atual - 1) * 5

    # Calcula o índice de fim para a paginação, que é o índice de 
            # início mais 5, para mostrar cinco itens por página.
    fim_idx = inicio_idx + 5

    # Utiliza 'iloc' para selecionar as linhas do DataFrame 
            # 'df_filtrado' correspondentes à página atual.
    # 'iloc' é uma função de indexação baseada em localização 
            # que aceita índices numéricos.
    df_pagina = df_filtrado.iloc[inicio_idx:fim_idx]
    
    # Limpa a Treeview atual para preparar para um novo conjunto de dados.
    # 'frame_tree.winfo_children()' retorna uma lista de todos 
            # os widgets contidos dentro de 'frame_tree'.
    # O loop 'for' passa por cada widget, chamando 'destroy()' 
            # para remover cada widget da interface.
    for widget in frame_tree.winfo_children():
        widget.destroy()
    
    # Cria um novo widget Treeview dentro do 'frame_tree' 
            # para exibir os dados.
    # 'columns=list(df_pagina.columns)' define as colunas 
            # que serão mostradas na Treeview.
    # 'show='headings'' configura a Treeview para mostrar 
            # apenas os cabeçalhos das colunas.
    # 'style="Custom.Treeview"' aplica um estilo personalizado 
            # definido anteriormente.
    tree = ttk.Treeview(frame_tree, 
                        columns=list(df_pagina.columns), 
                        show='headings', 
                        style="Custom.Treeview")

    # Configura a Treeview para expandir e preencher todo o 
            # espaço disponível dentro de seu container.
    # 'expand=True' faz com que o widget expanda para preencher 
            # qualquer espaço não utilizado na geometria do pai.
    # 'fill='both'' faz com que o widget expanda tanto 
            # vertical quanto horizontalmente.
    tree.pack(expand=True, fill='both')
    
    # Define um dicionário 'largura_colunas' que mapeia os 
            # nomes das colunas para suas respectivas larguras em pixels.
    # Esse dicionário é usado para controlar a largura 
            # de cada coluna na Treeview.
    largura_colunas = {

        # Define a largura da coluna 'Nome' como 150 pixels.
        'Nome': 150,       

        # Define a largura da coluna 'Turma' como 100 pixels.
        'Turma': 100,      

        # Define a largura das colunas 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4' e 'Faltas' como 60 pixels.
        'Nota 1': 60,      
        'Nota 2': 60,
        'Nota 3': 60,
        'Nota 4': 60,
        'Faltas': 60,

        # Define a largura da coluna 'Média' como 80 pixels.
        'Média': 80,       

        # Define a largura da coluna 'Situação' como 140 pixels.
        'Situação': 140    
        
    }

    
    # Itera sobre as colunas do DataFrame 'df_pagina' para configurar os 
            # cabeçalhos e as propriedades das colunas na Treeview.
    for col in df_pagina.columns:
        
        # Configura o texto do cabeçalho da coluna na Treeview 
                # para ser o nome da coluna.
        tree.heading(col, text=col)
        
        # Define as propriedades da coluna na Treeview.
        # 'anchor='center'' alinha o texto de cada célula da coluna ao centro.
        # 'width=largura_colunas.get(col, 100)' define a largura da coluna.
        # Se o nome da coluna não estiver especificado em 'largura_colunas', 
                # usa 100 pixels como largura padrão.
        tree.column(col, 
                    anchor='center', 
                    width=largura_colunas.get(col, 100))
        
    # Itera sobre as linhas do DataFrame 'df_pagina' para 
            # inserir os dados na Treeview.
    for indice, linha in df_pagina.iterrows():
        
        # Insere uma nova linha na Treeview no final da lista de entradas.
        # 'values=list(row)' converte os valores da linha do DataFrame 
                # em uma lista para serem exibidos na Treeview.
        tree.insert("", "end", values=list(linha))
        
    # Chama a função 'colorir_situacao' para aplicar cores diferenciadas às 
            # linhas da Treeview baseadas na situação do aluno.
    # A função utiliza o índice da coluna 'Situação' para acessar os 
            # valores relevantes em cada linha da Treeview.
    colorir_situacao(tree, list(df_pagina.columns).index('Situação'))


    # Atualiza o rótulo de status da página
    # 'label_status.config()' é usado para configurar as 
            # propriedades do widget label_status.
    # 'text=f"Página {pagina_atual} de {num_paginas}"' define o 
            # texto do rótulo para mostrar a página atual e o número total de páginas.
    label_status.config(text=f"Página {pagina_atual} de {num_paginas}")
    
    # Configura o estilo dos cabeçalhos da Treeview quando são 
            # pressionados ou estão ativos.
    # 'style.map("Custom.Treeview.Heading")' altera o mapa de 
            # estilo para 'Custom.Treeview.Heading'.
    # 'background' e 'foreground' definem as propriedades de cor 
            # de fundo e texto, respectivamente.
    # '[('pressed', "#003366"), ('active', "#003366")]' define a cor de 
            # fundo dos cabeçalhos para um azul escuro (#003366) quando 
            # estão pressionados ou ativos.
    # '[('pressed', "white"), ('active', "white")]' define a cor do 
            # texto dos cabeçalhos para branco quando estão pressionados ou ativos.
    style.map("Custom.Treeview.Heading",
              background=[('pressed', "#003366"), ('active', "#003366")],
              foreground=[('pressed', "white"), ('active', "white")])



# Define a função 'colorir_situacao', que é responsável por aplicar 
                # cores diferenciadas às linhas de uma Treeview baseadas 
        # na situação dos alunos.
def colorir_situacao(tree, col_index):
    
    # Itera sobre todos os itens (linhas) na Treeview.
    for item in tree.get_children():
        
        # 'tree.item(item, "values")[col_index]' obtém o valor da 
                # coluna especificada (situação do aluno) para o item atual.
        # 'col_index' é o índice da coluna que contém as informações 
                # sobre a situação do aluno.
        situacao = tree.item(item, "values")[col_index]
        
        # Verifica o valor da situação e aplica uma tag 
                # correspondente ao item.
        if situacao == "Aprovado":
            
            # Aplica a tag "aprovado" ao item se a situação for "Aprovado".
            tree.item(item, tags=("aprovado",))
            
        elif situacao == "Recuperação":
            
            # Aplica a tag "recuperacao" ao item se a situação for "Recuperação".
            tree.item(item, tags=("recuperacao",))
            
        elif situacao == "Reprovado por Notas":
            
            # Aplica a tag "reprovado_notas" ao item se a 
                    # situação for "Reprovado por Notas".
            tree.item(item, tags=("reprovado_notas",))
            
        elif situacao == "Reprovado por Faltas":
            
            # Aplica a tag "reprovado_faltas" ao item se a 
                    # situação for "Reprovado por Faltas".
            tree.item(item, tags=("reprovado_faltas",))

    # Configura as cores de fundo e texto para cada tag definida acima.
    # 'tree.tag_configure' é usado para definir as propriedades visuais para cada tag.
    # Verde claro para aprovados.
    tree.tag_configure("aprovado", background="#d4edda", foreground="#155724")       

    # Amarelo para recuperação.
    tree.tag_configure("recuperacao", background="#fff3cd", foreground="#856404")    

    # Rosa para reprovados por notas.
    tree.tag_configure("reprovado_notas", background="#f8d7da", foreground="#721c24") 

    # Rosa mais claro para reprovados por faltas.
    tree.tag_configure("reprovado_faltas", background="#f5c6cb", foreground="#721c24")


# Define a função 'primeira_pagina', que permite ao usuário navegar 
            # diretamente para a primeira página dos dados.
def primeira_pagina():
    
    # Declara 'pagina_atual' como uma variável global, permitindo 
            # que esta função modifique seu valor.
    global pagina_atual

    # Define 'pagina_atual' para 1, garantindo que a visualização 
            # seja ajustada para a primeira página.
    pagina_atual = 1

    # Chama a função 'exibir_pagina' para atualizar a interface e 
            # mostrar os dados da primeira página.
    exibir_pagina()


# Define a função 'voltar_pagina', que permite ao usuário 
        # navegar para a página anterior.
def voltar_pagina():
    
    # Declara 'pagina_atual' como uma variável global, permitindo 
            # que esta função modifique seu valor.
    global pagina_atual

    # Verifica se a página atual é maior que 1, indicando 
            # que não está na primeira página.
    if pagina_atual > 1:
        
        # Decrementa o valor de 'pagina_atual' por 1, movendo 
                # para a página anterior.
        pagina_atual -= 1

        # Chama a função 'exibir_pagina' para atualizar a exibição 
                # dos dados conforme a nova página atual.
        exibir_pagina()


# Funções de navegação entre as páginas
# Define a função 'avancar_pagina', que é responsável por 
            # mover a visualização dos dados para a próxima página.
def avancar_pagina():
    
    # Declara 'pagina_atual' como uma variável global para que a 
            # função possa modificar seu valor globalmente.
    global pagina_atual

    # Verifica se a página atual é menor que o número total de páginas disponíveis.
    # Isso assegura que o usuário não tente avançar além da última página.
    if pagina_atual < num_paginas:
        
        # Incrementa o valor de 'pagina_atual' por 1 para 
                # mover para a próxima página.
        pagina_atual += 1

        # Chama a função 'exibir_pagina' para atualizar a 
                # exibição dos dados para a nova página atual.
        exibir_pagina()


# Define a função 'ultima_pagina', que permite ao usuário 
            # navegar diretamente para a última página dos dados.
def ultima_pagina():
    
    # Declara 'pagina_atual' e 'num_paginas' como variáveis 
            # globais para modificar e acessar seus valores.
    global pagina_atual

    # Define 'pagina_atual' para o valor de 'num_paginas', que é o 
            # número total de páginas disponíveis.
    pagina_atual = num_paginas

    # Chama a função 'exibir_pagina' para atualizar a interface e 
            # mostrar os dados da última página.
    exibir_pagina()
    

# Configura a janela principal da aplicação utilizando Tkinter.
janela = tk.Tk()  # Cria o objeto 'janela' que é a janela principal da GUI.

# Define o título da janela, que é exibido na barra de título da janela.
# "Gestão de Notas dos Estudantes" é o texto que aparece 
        # na barra de título.
janela.title("Gestão de Notas dos Estudantes")  

# Define as dimensões da janela principal.
# "1024x400" especifica a largura (1024 pixels) e a 
        # altura (400 pixels) da janela.
janela.geometry("1024x400")  

# Cria e configura um estilo personalizado para a Treeview 
        # utilizando o módulo 'ttk' (parte do Tkinter).
# 'ttk.Style()' é usado para criar um objeto de estilo que 
        # pode ser usado para customizar os widgets.
style = ttk.Style()  

# Configura o estilo para os cabeçalhos das colunas da Treeview.
# "Custom.Treeview.Heading" é o nome do estilo aplicado aos cabeçalhos.
style.configure("Custom.Treeview.Heading",  

                # Define a fonte como Arial, tamanho 12, em negrito.
                font=('Arial', 12, 'bold'))  

# Configura o estilo para o corpo da Treeview.
# "Custom.Treeview" é o nome do estilo aplicado ao corpo da Treeview.
style.configure("Custom.Treeview",  

                # Define a espessura da borda de destaque como 0, 
                        # removendo qualquer destaque visual.
                highlightthickness=0,

                # Define a espessura da borda geral da Treeview 
                        # como 0, para um visual mais limpo.
                bd=0,  

                # Define a fonte do texto no corpo da Treeview 
                        # como Arial, tamanho 12.
                font=('Arial', 12))  


# Cria um widget de rótulo (Label) para exibir o título do projeto na interface gráfica.
# 'janela' é o container onde o rótulo será adicionado, 
        # nesse caso, a janela principal.
titulo = tk.Label(janela,  

                  # 'text' define o conteúdo textual do rótulo.
                  text="Projeto: Gestão de Notas dos Estudantes",  

                  # 'font' especifica a família da fonte, tamanho e estilo (negrito).
                  font=("Arial", 18, "bold"),  

                  # 'bg' (background) define a cor de fundo do rótulo 
                          # como um cinza escuro (#343a40).
                  bg="#343a40",

                  # 'fg' (foreground) define a cor do texto do rótulo como branco.
                  fg="white")  


# 'pack()' é um gerenciador de geometria que organiza o rótulo na janela. 
# 'fill='x'' faz com que o rótulo preencha todo o espaço horizontal disponível.
titulo.pack(fill='x')  


# Cria um frame (quadro) para conter o campo de filtro. Um frame é 
        # um container que pode conter outros widgets.
# 'janela' é o container onde o frame será adicionado.
frame_filtro = tk.Frame(janela,  

                        # 'bg' define a cor de fundo do frame como um cinza claro (#f8f9fa).
                        bg="#f8f9fa")  


# 'pack()' organiza o frame dentro da janela. 'pady=10' adiciona um 
        # espaçamento vertical de 10 pixels acima e abaixo do frame.
frame_filtro.pack(pady=10,  

                  # 'fill='x'' faz com que o frame preencha todo o 
                          # espaço horizontal disponível.
                  fill='x')  

# Cria um rótulo (label) para identificar o campo de filtro na interface gráfica.
# Adiciona o rótulo ao 'frame_filtro', que é um container 
        # para elementos de filtro.
label_filtro = tk.Label(frame_filtro,  

                        # Define o texto do rótulo como "Filtrar:".
                        text="Filtrar:",

                        # Define a cor de fundo do rótulo como cinza claro, 
                                # igual ao do frame para consistência.
                        bg="#f8f9fa",  

                        # Define a fonte do texto no rótulo como Arial de tamanho 12.
                        font=("Arial", 12))  

# Usa o gerenciador de geometria 'pack' para posicionar o 
        # rótulo à esquerda dentro do frame.
label_filtro.pack(side='left',

                  # Adiciona um preenchimento horizontal de 10 pixels 
                          # para separar o rótulo dos outros elementos.
                  padx=10)  

# Cria um campo de entrada para permitir ao usuário digitar o termo de filtro.
# Adiciona o campo de entrada ao mesmo 'frame_filtro'.
entrada_filtro = tk.Entry(frame_filtro,  

                          # Define a fonte do texto no campo de entrada 
                                  # como Arial de tamanho 12.
                          font=("Arial", 12))  

# Posiciona o campo de entrada à esquerda, ao lado do rótulo.
entrada_filtro.pack(side='left', 

                    # Adiciona um preenchimento horizontal de 10 
                            # pixels para espaçamento.
                    padx=10,  

                    # Permite que o campo de entrada expanda para 
                            # preencher o espaço horizontal.
                    fill='x',  

                    # Habilita a expansão do campo de entrada para 
                            # usar todo o espaço disponível.
                    expand=True)  

# Vincula um evento de liberação de tecla ao campo de entrada.
# Vincula o evento de liberação de qualquer tecla.
entrada_filtro.bind("<KeyRelease>",  

                    # Chama a função 'aplicar_filtro' sempre que uma tecla for liberada.
                    lambda event: aplicar_filtro())  


# Cria um frame para conter a Treeview, que exibirá os dados tabelados.
# Adiciona o frame à janela principal 'janela'.
frame_tree = tk.Frame(janela) 

# Configura o frame para expandir e preencher qualquer 
        # espaço extra na janela.
frame_tree.pack(expand=True,  

                # 'fill='both'' permite que o frame se expanda tanto 
                        # vertical quanto horizontalmente.
                fill='both')  

# Cria um frame para conter os botões de navegação e exportação dos dados.
# Adiciona este frame à janela principal 'janela'.
frame_botoes = tk.Frame(janela,  

                        # Define a cor de fundo do frame como cinza claro (#f8f9fa) 
                                # para manter a consistência visual.
                        bg="#f8f9fa")  

# 'fill='x'' configura o frame para expandir horizontalmente, 
        # preenchendo o espaço disponível.
frame_botoes.pack(fill='x',  

                  # 'pady=10' adiciona um espaçamento vertical de 10 
                          # pixels acima e abaixo do frame para separação visual.
                  pady=10)  


# Cria um botão para navegar diretamente para a primeira 
        # página, configurado com o texto "<< Primeira",
# a função 'primeira_pagina' como comando a ser executado 
        # ao clicar, um fundo azul (#007bff),
# texto branco e fonte Arial em negrito tamanho 12.
btn_primeira = tk.Button(frame_botoes, 
                         text="<< Primeira", 
                         command=primeira_pagina, 
                         bg="#007bff", 
                         fg="white", 
                         font=("Arial", 12, "bold"))

# Organiza o botão 'btn_primeira' no frame 'frame_botoes' no 
        # lado esquerdo, com um preenchimento horizontal de 5 pixels.
btn_primeira.pack(side='left', padx=5)

# Cria um botão para retornar à página anterior, com o texto "< Voltar", 
        # a função 'voltar_pagina' como comando,
# um fundo azul (#007bff), texto branco e fonte Arial 
        # em negrito tamanho 12.
btn_voltar = tk.Button(frame_botoes, 
                       text="< Voltar", 
                       command=voltar_pagina, 
                       bg="#007bff", 
                       fg="white", 
                       font=("Arial", 12, "bold"))

# Organiza o botão 'btn_voltar' no frame 'frame_botoes' ao 
        # lado do botão anterior, à esquerda, com um 
        # preenchimento horizontal de 5 pixels.
btn_voltar.pack(side='left', 
                padx=5)


# Cria um botão para avançar para a próxima página. 
        # O botão é adicionado ao 'frame_botoes'.
# O texto "Avançar >" é exibido no botão, a função 
        # 'avancar_pagina' é chamada ao clicar,
        # a cor de fundo é definida como azul (#007bff), o 
        # texto em branco, e a fonte Arial de tamanho 12 em negrito.
btn_avancar = tk.Button(frame_botoes, 
                        text="Avançar >", 
                        command=avancar_pagina, 
                        bg="#007bff", 
                        fg="white", 
                        font=("Arial", 12, "bold"))

# Organiza o botão 'btn_avancar' dentro do 'frame_botoes' à 
        # esquerda, com um espaçamento horizontal (padx) de 5 pixels.
btn_avancar.pack(side='left', padx=5)


# Cria um botão chamado 'btn_ultima' no 'frame_botoes'. 
        # Este botão é usado para navegar diretamente para a última página dos dados.
# O texto "Última >>" é exibido no botão, indicando sua função.
# A função 'ultima_pagina', que move a visualização de dados 
        # para a última página, é chamada quando o botão é clicado.
# A cor de fundo do botão é azul (#007bff), o texto é branco, e 
        # a fonte é Arial tamanho 12 em negrito, para fácil 
        # leitura e consistência visual com outros botões.
btn_ultima = tk.Button(frame_botoes, 
                       text="Última >>", 
                       command=ultima_pagina, 
                       bg="#007bff", 
                       fg="white", 
                       font=("Arial", 12, "bold"))

# Posiciona o botão 'btn_ultima' à esquerda dentro do 'frame_botoes', 
        # com um espaçamento horizontal de 5 pixels (padx),
        # o que ajuda a separar visualmente este botão 
        # de outros botões adjacentes.
btn_ultima.pack(side='left', padx=5)

# Cria um botão chamado 'btn_exportar' no 'frame_botoes'. 
        # Este botão permite ao usuário exportar os dados 
        # filtrados para um arquivo Excel.
# O texto "Exportar Dados Filtrados" claramente indica sua função.
# A função 'exportar_dados_filtrados', que salva os dados 
        # filtrados em um arquivo Excel, é ativada quando o botão é clicado.
# A cor de fundo é verde (#28a745), simbolizando ação/ir em 
        # frente, com texto branco e fonte Arial tamanho 12 em 
        # negrito para manter a legibilidade e a coerência com o design.
btn_exportar = tk.Button(frame_botoes, 
                         text="Exportar Dados Filtrados", 
                         command=exportar_dados_filtrados, 
                         bg="#28a745", 
                         fg="white", 
                         font=("Arial", 12, "bold"))

# Posiciona o botão 'btn_exportar' à direita dentro do 
        # 'frame_botoes', com um espaçamento horizontal de 10 pixels (padx).
# Esta posição e o espaçamento ajudam a diferenciar este botão 
        # de outros botões de navegação, destacando sua 
        # função única de exportação.
btn_exportar.pack(side='right', padx=10)

# Cria um rótulo chamado 'label_status' na janela principal. 
        # Este rótulo é usado para exibir informações sobre o 
        # status da página, como qual página está 
        # sendo visualizada no momento.
# 'janela' é o container principal onde o rótulo será adicionado.
label_status = tk.Label(janela,  

                        # Inicialmente, o texto do rótulo é definido como 
                                # vazio, porque será atualizado dinamicamente.
                        text="",  

                        # Define a fonte do texto no rótulo como Arial 
                                # tamanho 14 para fácil leitura.
                        font=("Arial", 14),

                        # Define a cor de fundo do rótulo como um cinza muito 
                                # claro (#f8f9fa) para manter a consistência visual.
                        bg="#f8f9fa")  

# Posiciona o rótulo 'label_status' na janela usando o 
        # gerenciador de geometria 'pack'.
# 'pady=5' adiciona um espaçamento vertical de 5 pixels 
        # acima e abaixo do rótulo para separá-lo visualmente 
        # de outros elementos da interface.
label_status.pack(pady=5)

# Chama a função 'carregar_dados' para carregar os dados do 
        # arquivo Excel especificado e preparar a visualização inicial dos dados.
# Esta função também inicializa as configurações de paginação e 
        # aplica qualquer filtro inicial se necessário.
carregar_dados()

# Inicia o loop principal da interface gráfica. Este loop é 
        # necessário para manter a janela aberta,
        # respondendo a eventos como cliques de botão e entradas de teclado.
# 'janela.mainloop()' entra no loop de eventos da Tkinter, que 
        # aguarda ações do usuário e as processa conforme ocorrem.
janela.mainloop()