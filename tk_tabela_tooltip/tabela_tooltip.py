import tkinter as tk
# Importa o módulo tkinter para utilização de interface gráfica 
        # padrão do Python. A abreviação 'tk' é usada para 
        # facilitar o acesso às classes e métodos do módulo.

from tkinter import ttk, filedialog, messagebox
# Importa especificamente os submódulos ttk, filedialog e 
        # messagebox do tkinter:
# - ttk: usado para acessar o conjunto de widgets temáticos 
        # que oferecem uma aparência melhorada.
# - filedialog: permite a abertura de diálogos de arquivo (abrir, 
        # salvar) na interface gráfica.
# - messagebox: fornece uma série de caixas de diálogo para exibir 
        # mensagens, avisos, perguntas ao usuário.

import pandas as pd
# Importa o módulo pandas, uma poderosa biblioteca para manipulação e 
        # análise de dados em Python. 'pd' é um alias comum para pandas.

# Função para carregar dados do Excel
def carregar_dados():
    
    # Carrega os dados de uma planilha do Excel especificando o 
            # nome do arquivo e a aba.
    # 'pd.read_excel' é um método do pandas que lê um arquivo Excel. 
    # 'notas_estudantes.xlsx' é o nome do arquivo Excel que contém os dados.
    # 'sheet_name='Dados'' especifica que estamos lendo a aba 
            # chamada 'Dados' neste arquivo Excel.
    df = pd.read_excel('notas_estudantes.xlsx', sheet_name='Dados')  
    
    # Calcula a média das notas dos estudantes para cada linha e 
            # armazena em uma nova coluna chamada 'Média'.
    # 'df[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1)' seleciona 
            # as colunas das notas, calcula a média (mean)
    # para cada linha (axis=1 indica que a operação é feita linha a linha), e 
            # o resultado é armazenado em uma nova coluna 'Média'.
    df['Média'] = df[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1)
    
    # Aplica uma função para classificar a situação do aluno com base 
            # em sua média e quantidade de faltas.
    # 'df.apply(lambda row: ...)' aplica uma função anônima (lambda) linha a linha.
    # 'classificar_situacao(row['Média'], row['Faltas'])' chama a função 
            # classificar_situacao, passando a média e as faltas de cada aluno.
    # A função classificar_situacao determina se o aluno está aprovado, em 
            # recuperação, ou reprovado, baseado nas regras definidas nela.
    df['Situação'] = df.apply(lambda row: classificar_situacao(row['Média'], row['Faltas']), axis=1)
    
    # Retorna o DataFrame modificado com as novas colunas de 
            # média e situação.
    # Um DataFrame é uma estrutura de dados bidimensional que 
            # pode ser pensada como uma tabela.
    return df


# Função para classificar a situação do aluno
def classificar_situacao(media, faltas):
    
    # Inicia verificando se o número de faltas do aluno é maior que 10.
    # 'if faltas > 10:' verifica se a condição (faltas serem 
            # maiores que 10) é verdadeira.
    if faltas > 10:
        
        # Se o aluno tem mais de 10 faltas, ele é automaticamente 
                # considerado reprovado por faltas.
        # 'return 'Reprovado por Faltas'' encerra a função e 
                # retorna o texto 'Reprovado por Faltas'.
        return 'Reprovado por Faltas'
    
    # Se o número de faltas não é maior que 10, verifica-se a média das notas.
    # 'elif media < 2:' verifica se a média do aluno é menor que 2.
    elif media < 2:
        
        # Se a média é menor que 2, o aluno é considerado reprovado por nota.
        # 'return 'Reprovado por Nota'' retorna o texto 'Reprovado por Nota'.
        return 'Reprovado por Nota'
    
    # Se a média está entre 2 e 7, verifica-se se o aluno está 
            # em situação de recuperação.
    # 'elif 2 <= media < 7:' verifica se a média está no 
            # intervalo de 2 a 6,99.
    elif 2 <= media < 7:
        
        # Se a média está entre 2 e 7, o aluno é considerado em recuperação.
        # 'return 'Recuperação'' retorna o texto 'Recuperação'.
        return 'Recuperação'
    
    # Se nenhuma das condições anteriores for verdadeira, o 
            # aluno é considerado aprovado.
    # 'else:' é executado se todas as condições acima forem falsas.
    else:
        
        # O aluno é considerado aprovado.
        # 'return 'Aprovado'' retorna o texto 'Aprovado'.
        return 'Aprovado'


# Função para filtrar os alunos dentro do painel de detalhes
def filtrar_alunos(*args):
    
    # Obtém o texto de entrada do usuário e converte para 
            # letras minúsculas para padronizar a comparação.
    # 'entrada_filtro.get()' pega o texto atual no 
            # campo de entrada do filtro.
    # '.lower()' converte o texto para minúsculas, 
            # facilitando a comparação insensível à caixa.
    filtro = entrada_filtro.get().lower()
    
    # Filtra os alunos de acordo com o texto do filtro, 
            # considerando nome e situação.
    # 'alunos_filtrados' é o DataFrame que contém os 
            # alunos já filtrados pela turma.
    # '.str.lower()' converte os valores das colunas 'Nome' 
            # e 'Situação' para minúsculas.
    # '.str.contains(filtro)' verifica se os valores contêm o 
            # texto do filtro inserido pelo usuário.
    alunos_filtrados_locais = alunos_filtrados[alunos_filtrados['Nome'].str.lower().str.contains(filtro) |
                                               alunos_filtrados['Situação'].str.lower().str.contains(filtro)]
    
    # Limpa a tabela de detalhes removendo todos os itens existentes.
    # 'tabela_detalhes.get_children()' obtém todos os itens (linhas) 
            # que estão atualmente na tabela de detalhes.
    # 'tabela_detalhes.delete(item)' remove cada item (linha) da 
            # tabela para garantir que apenas os dados filtrados sejam exibidos.
    for item in tabela_detalhes.get_children():
        tabela_detalhes.delete(item)
    
    # Insere na tabela de detalhes os alunos que correspondem ao filtro.
    # 'alunos_filtrados_locais.iterrows()' retorna um iterador que 
            # fornece index e Series (linha) para cada aluno no DataFrame filtrado.
    # 'tabela_detalhes.insert('', 'end', ...)' insere uma nova 
            # linha na tabela para cada aluno filtrado.
    # Os valores inseridos incluem o nome do aluno, sua média 
            # formatada com duas casas decimais, e sua situação.
    for _, aluno in alunos_filtrados_locais.iterrows():
        tabela_detalhes.insert('', 'end', values=(aluno['Nome'], f"{aluno['Média']:.2f}", aluno['Situação']))
        

# Função para exportar dados filtrados para Excel
def exportar_para_excel():
    
    # Aplica filtros ao DataFrame 'alunos_filtrados' para criar uma 
            # nova lista de alunos que correspondem aos critérios 
            # especificados no campo de entrada.
    # 'entrada_filtro.get().lower()' obtém o texto do filtro, 
            # converte para letras minúsculas para padronização.
    # '.str.contains(...)' verifica se os valores nas colunas 
            # 'Nome' e 'Situação' contêm o texto do filtro.
    alunos_filtrados_locais = alunos_filtrados[alunos_filtrados['Nome'].str.lower().str.contains(entrada_filtro.get().lower()) |
                                               alunos_filtrados['Situação'].str.lower().str.contains(entrada_filtro.get().lower())]
    
    # Verifica se o DataFrame filtrado não está vazio.
    # 'not alunos_filtrados_locais.empty' retorna True se houver 
            # pelo menos um registro no DataFrame.
    if not alunos_filtrados_locais.empty:
        
        # Abre uma caixa de diálogo para o usuário escolher onde 
                # salvar o arquivo.
        # 'filedialog.asksaveasfilename(...)' exibe uma janela para o 
                # usuário escolher o nome e local do arquivo a ser salvo.
        # 'defaultextension=".xlsx"' define a extensão padrão do 
                # arquivo como .xlsx (Excel).
        # 'filetypes=[("Excel files", "*.xlsx")]' limita os tipos de 
                # arquivo mostrados para apenas arquivos Excel.
        caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        
        # Verifica se um caminho de arquivo foi escolhido (o 
                # usuário não cancelou a operação).
        if caminho_arquivo:
            
            # Exporta o DataFrame para o arquivo Excel escolhido.
            # 'to_excel(caminho_arquivo, index=False)' salva o DataFrame 
                    # em um arquivo Excel, sem incluir o índice como uma coluna.
            alunos_filtrados_locais.to_excel(caminho_arquivo, index=False)
            
            # Exibe uma mensagem de confirmação para o usuário.
            # 'messagebox.showinfo(...)' mostra uma caixa de diálogo 
                    # informando que a exportação foi bem-sucedida.
            # 'f"Os dados foram exportados para {caminho_arquivo} com sucesso."' é 
                    # a mensagem mostrada ao usuário, informando o caminho 
                    # do arquivo exportado.
            messagebox.showinfo("Exportação bem-sucedida", f"Os dados foram exportados para {caminho_arquivo} com sucesso.")



# Função para calcular a média da turma e total de faltas
def calcular_estatisticas(df):
    
    # Agrupa os dados do DataFrame 'df' por 'Turma' e calcula as 
            # estatísticas agregadas para cada grupo.
    # 'df.groupby('Turma')' agrupa os dados por turma, permitindo 
            # que operações sejam realizadas por grupo.
    estatisticas = df.groupby('Turma').agg(
        
        # Calcula a média das médias de notas para cada turma. 
        # 'Média_da_Turma=('Média', 'mean')' especifica que queremos a 
                # média da coluna 'Média' para cada grupo,
                # e o resultado será armazenado na nova coluna 'Média_da_Turma'.
        Média_da_Turma=('Média', 'mean'),
        
        # Calcula a soma total das faltas para cada turma.
        # 'Total_de_Faltas=('Faltas', 'sum')' especifica que queremos a 
                # soma da coluna 'Faltas' para cada grupo,
                # e o resultado será armazenado na nova coluna 'Total_de_Faltas'.
        Total_de_Faltas=('Faltas', 'sum')

    # 'reset_index()' converte o índice de grupo em uma coluna regular, 
                # permitindo que 'Turma' seja uma coluna.
    ).reset_index()  

    # Ordena as estatísticas das turmas em ordem alfabética pelo nome da turma.
    # 'estatisticas.sort_values(by='Turma')' ordena o DataFrame 
            # 'estatisticas' pela coluna 'Turma'.
    # 'by='Turma'' especifica que a ordenação deve ser feita pela coluna 'Turma'.
    estatisticas = estatisticas.sort_values(by='Turma')

    # Retorna o DataFrame com as estatísticas calculadas e ordenadas.
    return estatisticas


# Função para exibir detalhes da turma no painel lateral
def exibir_detalhes(event):
    
    # Identifica a linha da tabela onde ocorreu o evento (normalmente 
            # um clique do mouse).
    # 'tabela.identify_row(event.y)' obtém o ID da linha com base 
            # na posição vertical do mouse 'event.y'.
    linha_id = tabela.identify_row(event.y)
    
    # Verifica se uma linha válida foi identificada.
    # 'if linha_id:' verifica se 'linha_id' não está vazio, o que 
            # indicaria que uma linha foi selecionada.
    if linha_id:
        
        # Obtém o item da tabela correspondente ao ID da linha.
        # 'tabela.item(linha_id)' retorna os dados da linha identificada, 
                # incluindo um dicionário com os valores da linha.
        item = tabela.item(linha_id)
        
        # Extrai os valores dos dados da linha, que incluem os detalhes da turma.
        # 'valores = item['values']' extrai a lista de valores 
                # associados à linha selecionada.
        valores = item['values']
        
        # O primeiro valor da lista de valores corresponde ao nome da turma.
        # 'turma = valores[0]' armazena o nome da turma na variável 'turma'.
        turma = valores[0]

        # Filtra os alunos da turma selecionada para exibição.
        # 'global alunos_filtrados' declara que 'alunos_filtrados' é 
                # uma variável global, acessível fora desta função.
        # 'df[df['Turma'] == turma]' filtra o DataFrame 'df' para linhas 
                # onde a coluna 'Turma' é igual ao nome da turma selecionada.
        global alunos_filtrados
        alunos_filtrados = df[df['Turma'] == turma]
        
        # Chama a função para atualizar a tabela de detalhes com 
                # os alunos filtrados.
        # 'atualizar_tabela_detalhes()' é uma função que limpa e preenche 
                # a tabela de detalhes com os alunos filtrados.
        atualizar_tabela_detalhes()

        # Atualiza o título no painel lateral para refletir a turma selecionada.
        # 'titulo_turma.config(text=f"Turma: {turma}")' configura o 
                # texto do widget 'titulo_turma' para incluir o nome da turma.
        titulo_turma.config(text=f"Turma: {turma}")


# Função para atualizar a tabela de detalhes com os alunos filtrados
def atualizar_tabela_detalhes():
    
    # Limpa a tabela de detalhes removendo todos os itens existentes.
    # 'tabela_detalhes.get_children()' obtém todos os itens (linhas) 
            # que estão atualmente na tabela de detalhes.
    # O loop 'for' percorre cada item na lista de itens retornada.
    for item in tabela_detalhes.get_children():
        
        # 'tabela_detalhes.delete(item)' remove o item da tabela.
        # Cada 'item' é uma linha na tabela, e esta linha é removida 
                # para limpar a tabela antes de adicionar novos dados.
        tabela_detalhes.delete(item)
    
    # Adiciona novos itens à tabela de detalhes com dados dos alunos filtrados.
    # 'alunos_filtrados.iterrows()' gera um iterador que retorna 
            # cada linha do DataFrame 'alunos_filtrados' como 
            # uma tupla de índice e série.
    # O loop 'for' percorre cada aluno no DataFrame 'alunos_filtrados'.
    for _, aluno in alunos_filtrados.iterrows():
        
        # 'tabela_detalhes.insert('', 'end', values=(aluno['Nome'], f"{aluno['Média']:.2f}", aluno['Situação"]))'
        # insere uma nova linha no final da tabela 'tabela_detalhes'.
        # A linha inserida contém valores especificados no argumento 'values':
        # 'aluno['Nome']' é o nome do aluno,
        # 'f"{aluno['Média']:.2f}"' é a média do aluno formatada com duas casas decimais,
        # 'aluno['Situação']' é a situação atual do aluno (Aprovado, Reprovado, etc.).
        tabela_detalhes.insert('', 
                               'end', 
                               values=(aluno['Nome'], f"{aluno['Média']:.2f}", aluno['Situação']))
        

# Função para exibir tooltip com informações do aluno
def exibir_tooltip_aluno(event):
    
    # Identifica a linha da tabela onde o evento de mouse ocorreu.
    # 'tabela_detalhes.identify_row(event.y)' usa a posição vertical 
            # do mouse (event.y) para identificar a linha.
    # 'linha_id' armazena o ID da linha que foi identificada, que é 
            # essencial para acessar os dados dessa linha específica.
    linha_id = tabela_detalhes.identify_row(event.y)
    
    # Verifica se uma linha válida foi identificada.
    # 'if linha_id:' verifica se 'linha_id' não está vazio, o que 
            # indicaria que uma linha foi selecionada.
    if linha_id:
        
        # Obtém os dados do item da linha identificada.
        # 'tabela_detalhes.item(linha_id)' retorna os dados da linha 
                # identificada, incluindo um dicionário com os valores da linha.
        # 'item' contém os dados da linha, que incluem o nome do 
                # aluno e outros detalhes.
        item = tabela_detalhes.item(linha_id)
        
        # Extrai o nome do aluno da primeira posição dos valores da linha.
        # 'nome_aluno = item['values'][0]' extrai o primeiro valor 
                # dos valores armazenados na linha, que é o nome do aluno.
        nome_aluno = item['values'][0]

        # Obter dados do aluno para mostrar no tooltip.
        # 'df[df['Nome'] == nome_aluno]' filtra o DataFrame 'df' para 
                # encontrar a linha que contém o nome do aluno.
        # '.iloc[0]' seleciona a primeira linha do DataFrame filtrado, pois o 
                # nome deve ser único ou estamos assumindo a primeira ocorrência.
        # 'aluno' agora contém a linha completa de dados para o aluno selecionado, 
                # que pode incluir notas, média, situação, entre outros.
        aluno = df[df['Nome'] == nome_aluno].iloc[0]


        # Configurar texto do tooltip do aluno
        # Cria uma string formatada que contém todas as informações relevantes do aluno.
        # Utiliza a sintaxe f-string para interpolação de variáveis diretamente dentro da string.
        # '\n' é usado para inserir quebras de linha entre os itens, para melhorar a legibilidade.
        texto_aluno = (f"Nome: {aluno['Nome']}\n"
                       f"Nota 1: {aluno['Nota 1']}\n"  # Inclui a primeira nota do aluno.
                       f"Nota 2: {aluno['Nota 2']}\n"  # Inclui a segunda nota do aluno.
                       f"Nota 3: {aluno['Nota 3']}\n"  # Inclui a terceira nota do aluno.
                       f"Nota 4: {aluno['Nota 4']}\n"  # Inclui a quarta nota do aluno.
                       f"Média: {aluno['Média']:.2f}\n"  # Inclui a média do aluno, formatada com duas casas decimais.
                       f"Faltas: {aluno['Faltas']}\n"  # Inclui o número total de faltas do aluno.
                       f"Situação: {aluno['Situação']}")  # Inclui a situação acadêmica do aluno (Aprovado, Reprovado, etc.).
        
        # Configura o texto do widget 'label_tooltip_aluno' para 
                # exibir as informações formatadas.
        # 'label_tooltip_aluno.config(text=texto_aluno)' atualiza a 
                # configuração do texto do label para mostrar as informações do aluno.
        label_tooltip_aluno.config(text=texto_aluno)
        
        # Define a posição do tooltip baseada na posição atual do cursor do mouse.
        # 'tooltip_aluno.wm_geometry(f"+{event.x_root + 10}+{event.y_root + 10}")' 
                # define a geometria da janela do tooltip.
        # 'event.x_root' e 'event.y_root' fornecem as coordenadas 
                # absolutas do mouse na tela.
        # '+10' em ambos os eixos x e y desloca o tooltip ligeiramente 
                # para a direita e para baixo, evitando que o cursor cubra o conteúdo.
        tooltip_aluno.wm_geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
        
        # Torna o tooltip visível.
        # 'tooltip_aluno.deiconify()' faz com que a janela do tooltip, 
                # que pode ter sido previamente ocultada, torne-se visível.
        tooltip_aluno.deiconify()


# Função para ocultar o tooltip do aluno
def ocultar_tooltip_aluno(event):
    
    # 'tooltip_aluno.withdraw()' é um método que oculta a janela do tooltip.
    # Este método é útil para garantir que o tooltip desapareça quando 
            # não for mais necessário, como ao mover o mouse para 
            # fora da área relevante.
    tooltip_aluno.withdraw()
    

# Configuração da janela principal
# Cria uma nova instância de uma janela Tkinter.
# 'tk.Tk()' inicializa uma nova janela ou, no contexto de Tkinter, 
        # uma instância 'root' que serve como a janela principal da aplicação.
janela = tk.Tk()

# Define o título da janela.
# 'janela.title("Resumo de Turmas")' configura o texto que 
        # aparecerá na barra de título da janela.
# Este título ajuda os usuários a identificar o propósito 
        # da janela na interface gráfica.
janela.title("Resumo de Turmas")

# Carregar dados
# 'carregar_dados()' é chamada para carregar os dados necessários 
        # para a aplicação a partir de uma fonte específica, 
        # neste caso, um arquivo Excel.
# O DataFrame 'df' resultante contém os dados carregados.
df = carregar_dados()

# 'calcular_estatisticas(df)' é chamada para processar o DataFrame 'df' e 
        # calcular estatísticas adicionais necessárias.
# 'estatisticas' recebe o DataFrame retornado, que inclui 
        # estatísticas agregadas como médias da turma e totais de faltas.
estatisticas = calcular_estatisticas(df)

# Configurações de fonte
# Define uma fonte padrão para ser usada na interface gráfica.
# 'fonte_padrao = ("Arial", 12)' configura a fonte Arial 
        # com tamanho 12 para texto regular.
fonte_padrao = ("Arial", 12)

# Define uma fonte em negrito para destacar certos 
        # detalhes na interface gráfica.
# 'fonte_detalhes = ("Arial", 12, "bold")' configura a 
        # mesma fonte Arial com tamanho 12, mas em negrito.
# Isso é útil para destacar títulos ou informações importantes.
fonte_detalhes = ("Arial", 12, "bold")


# Tabela principal
# Define uma tupla com os nomes das colunas que serão usadas na tabela.
colunas = ('Turma', 'Média da Turma', 'Total de Faltas')

# Cria uma tabela (TreeView) que será usada para exibir dados.
# 'ttk.Treeview(janela, columns=colunas, show='headings', style="mystyle.Treeview")' 
        # cria um widget Treeview na janela principal.
# 'columns=colunas' define as colunas da tabela baseadas na 
        # tupla definida anteriormente.
# 'show='headings'' configura a tabela para mostrar apenas os 
        # cabeçalhos das colunas, sem a coluna de índice padrão.
# 'style="mystyle.Treeview"' aplica um estilo personalizado chamado 
        # 'mystyle.Treeview', que pode ser definido em outro lugar no 
        # código para alterar a aparência da tabela.
tabela = ttk.Treeview(janela, 
                      columns=colunas, 
                      show='headings', 
                      style="mystyle.Treeview")

# Posiciona a tabela na janela.
# 'tabela.pack(side='left', fill='both', expand=True)' usa o 
        # gerenciador de geometria 'pack' para posicionar a tabela.
# 'side='left'' posiciona a tabela à esquerda da janela.
# 'fill='both'' faz com que a tabela expanda tanto horizontal 
        # quanto verticalmente para preencher o espaço disponível.
# 'expand=True' permite que a tabela se expanda adicionalmente 
        # para preencher qualquer espaço extra na janela.
tabela.pack(side='left', fill='both', expand=True)

# Configura os cabeçalhos das colunas da tabela.
# Este loop percorre cada nome de coluna definido na tupla 'colunas'.
for col in colunas:
    
    # 'tabela.heading(col, text=col)' define o texto do 
            # cabeçalho de cada coluna para corresponder 
            # ao nome da coluna.
    tabela.heading(col, text=col)

# Painel lateral para exibir detalhes
# Cria um frame que será usado como um painel lateral 
        # para exibir informações adicionais.
# 'tk.Frame(janela, bg='lightyellow', relief='solid', borderwidth=2, 
        # width=300)' cria um frame na janela principal.
# 'bg='lightyellow'' define a cor de fundo do painel como amarelo claro.
# 'relief='solid'' dá ao painel um tipo de borda sólida, 
        # que pode ajudar visualmente a distinguir o painel 
        # do resto da interface.
# 'borderwidth=2' define a largura da borda do painel.
# 'width=300' define a largura fixa do painel em pixels.
painel_lateral = tk.Frame(janela, 
                          bg='lightyellow', 
                          relief='solid', 
                          borderwidth=2, 
                          width=300)

# Posiciona o painel lateral na janela.
# 'painel_lateral.pack(side='right', fill='y')' usa o 
        # gerenciador de geometria 'pack' para posicionar o painel lateral.
# 'side='right'' posiciona o painel à direita da janela.
# 'fill='y'' faz com que o painel expanda verticalmente 
        # para preencher o espaço vertical disponível.
painel_lateral.pack(side='right', fill='y')


# Título no painel lateral
# Cria um widget de label (etiqueta) que serve como 
        # título para o painel lateral.
# 'tk.Label(painel_lateral, text="Selecione uma turma", 
        # font=fonte_detalhes, bg='lightyellow')' cria um 
        # label dentro do painel lateral.
# 'text="Selecione uma turma"' define o texto do label 
        # para instruir o usuário a selecionar uma turma.
# 'font=fonte_detalhes' aplica a fonte em negrito definida 
        # anteriormente, destacando visualmente o título.
# 'bg='lightyellow'' define a cor de fundo do label para 
        # ser a mesma do painel, garantindo uma aparência consistente.
titulo_turma = tk.Label(painel_lateral, 
                        text="Selecione uma turma", 
                        font=fonte_detalhes, 
                        bg='lightyellow')

# Posiciona o título dentro do painel lateral.
# 'titulo_turma.pack(padx=10, pady=10)' usa o gerenciador 
        # de geometria 'pack' para adicionar o label ao painel.
# 'padx=10, pady=10' adiciona um espaço de 10 pixels de 
        # preenchimento em torno do label tanto na 
        # horizontal (x) quanto na vertical (y), 
# proporcionando um espaçamento visual agradável 
        # entre o título e outros elementos.
titulo_turma.pack(padx=10, pady=10)

# Campo de filtro no painel lateral
# Cria um widget de entrada (campo de texto) para 
        # filtrar alunos por nome ou situação.
# 'tk.Entry(painel_lateral, font=fonte_padrao)' cria 
        # uma caixa de entrada no painel lateral.
# 'font=fonte_padrao' aplica a fonte padrão definida 
        # anteriormente, garantindo que o texto digitado seja facilmente legível.
entrada_filtro = tk.Entry(painel_lateral, font=fonte_padrao)

# Posiciona o campo de entrada dentro do painel lateral.
# 'entrada_filtro.pack(fill='x', padx=10, pady=5)' 
        # posiciona o widget usando o gerenciador 'pack'.
# 'fill='x'' faz com que o campo de entrada expanda horizontalmente 
        # para preencher todo o espaço disponível no painel lateral.
# 'padx=10, pady=5' adiciona preenchimento de 10 pixels na 
        # horizontal e 5 pixels na vertical em torno do campo de entrada.
entrada_filtro.pack(fill='x', padx=10, pady=5)

# Associa um evento ao campo de entrada.
# 'entrada_filtro.bind('<KeyRelease>', filtrar_alunos)' liga o 
        # evento de liberação de tecla no campo de entrada à função 'filtrar_alunos'.
# Isso significa que cada vez que uma tecla for solta, a 
        # função 'filtrar_alunos' será chamada automaticamente, 
# permitindo a atualização dinâmica dos dados filtrados 
        # conforme o usuário digita.
entrada_filtro.bind('<KeyRelease>', filtrar_alunos)


# Botão de exportação para Excel
# Cria um widget de botão que permite ao usuário exportar 
        # dados filtrados para um arquivo Excel.
# 'tk.Button(painel_lateral, text="Exportar para Excel", 
        # command=exportar_para_excel, font=fonte_padrao)' 
        # cria um botão no painel lateral.
# 'text="Exportar para Excel"' define o texto exibido no 
        # botão, indicando sua função.
# 'command=exportar_para_excel' associa o botão à função 
        # 'exportar_para_excel', que será chamada quando o 
        # botão for pressionado.
# 'font=fonte_padrao' aplica a fonte padrão ao texto do 
        # botão, mantendo a consistência visual.
botao_exportar = tk.Button(painel_lateral, 
                           text="Exportar para Excel", 
                           command=exportar_para_excel, 
                           font=fonte_padrao)

# Posiciona o botão dentro do painel lateral.
# 'botao_exportar.pack(padx=10, pady=5)' usa o gerenciador 
        # de geometria 'pack' para adicionar o botão ao painel.
# 'padx=10, pady=5' adiciona preenchimento de 10 pixels na 
        # horizontal e 5 pixels na vertical em torno do botão,
# proporcionando um espaçamento adequado e melhorando a acessibilidade.
botao_exportar.pack(padx=10, pady=5)

# Tabela no painel lateral
# Cria uma tabela detalhada para exibir informações adicionais 
        # dos alunos, como nome, média e situação.
# 'ttk.Treeview(painel_lateral, columns=('Nome', 'Média', 'Situação'), 
        # show='headings', style="mystyle.Treeview")' cria um widget Treeview.
# 'columns=('Nome', 'Média', 'Situação')' define as colunas da tabela.
# 'show='headings'' configura a tabela para exibir apenas os 
        # cabeçalhos das colunas, sem a coluna de índice padrão.
# 'style="mystyle.Treeview"' aplica um estilo personalizado definido 
        # para alterar a aparência da tabela.
tabela_detalhes = ttk.Treeview(painel_lateral, 
                               columns=('Nome', 'Média', 'Situação'), 
                               show='headings', 
                               style="mystyle.Treeview")

# Posiciona a tabela de detalhes no painel lateral.
# 'tabela_detalhes.pack(fill='both', expand=True)' usa o 
        # gerenciador de geometria 'pack' para adicionar a tabela ao painel.
# 'fill='both'' faz com que a tabela expanda tanto horizontal 
        # quanto verticalmente para preencher o espaço disponível.
# 'expand=True' permite que a tabela se expanda adicionalmente 
        # para preencher qualquer espaço extra no painel lateral.
tabela_detalhes.pack(fill='both', expand=True)


# Configurando os cabeçalhos das colunas para a 
        # tabela de detalhes no painel lateral.
# Este loop percorre cada nome de coluna na 
        # tupla ('Nome', 'Média', 'Situação').
for col in ('Nome', 'Média', 'Situação'):
    
    # 'tabela_detalhes.heading(col, text=col)' configura o 
            # texto do cabeçalho para cada coluna na tabela de detalhes.
    # 'col' é o nome da coluna, e 'text=col' define que o 
            # texto do cabeçalho será o próprio nome da coluna.
    # Isso garante que cada coluna seja claramente identificada 
            # por seu propósito (exibir nome, média e situação do aluno).
    tabela_detalhes.heading(col, text=col)


# Tooltip para exibir detalhes do aluno
# Cria uma nova janela 'tooltip' que flutuará acima da 
        # janela principal para mostrar detalhes sobre um aluno.
# 'tk.Toplevel(janela)' cria uma nova janela que é um 
        # nível acima da janela principal 'janela'.
tooltip_aluno = tk.Toplevel(janela)

# Oculta inicialmente o tooltip até que seja necessário.
# 'tooltip_aluno.withdraw()' retira a janela do tooltip 
        # do display, fazendo com que ela não apareça 
        # até ser explicitamente mostrada.
tooltip_aluno.withdraw()

# Desativa a decoração da janela para o tooltip, como a 
        # barra de título e bordas.
# 'tooltip_aluno.overrideredirect(True)' remove a barra de 
        # título e quaisquer bordas da janela do tooltip,
# tornando-a uma janela flutuante pura que pode ser usada 
        # para exibir apenas as informações necessárias sem distrações.
tooltip_aluno.overrideredirect(True)


# Configuração do rótulo dentro do tooltip
# Cria um widget de rótulo (label) dentro da janela do 
        # tooltip para exibir informações do aluno.
# 'tk.Label(tooltip_aluno, text="", justify='left', background='lightblue', 
        # font=fonte_detalhes)' cria um label no tooltip_aluno.
# 'text=""' inicializa o label sem texto, que será configurado 
        # dinamicamente quando o tooltip for exibido.
# 'justify='left'' alinha o texto do label à esquerda, facilitando a 
        # leitura de informações detalhadas.
# 'background='lightblue'' define a cor de fundo do label como 
        # azul claro, proporcionando uma visualização clara e agradável do texto.
# 'font=fonte_detalhes' aplica uma fonte em negrito ao texto do 
        # label para destacar as informações exibidas.
label_tooltip_aluno = tk.Label(tooltip_aluno, 
                               text="", 
                               justify='left', 
                               background='lightblue', 
                               font=fonte_detalhes)

# Posiciona o rótulo dentro do tooltip.
# 'label_tooltip_aluno.pack(padx=10, pady=5)' usa o gerenciador 
        # de geometria 'pack' para adicionar o label ao tooltip.
# 'padx=10, pady=5' adiciona preenchimento de 10 pixels na 
        # horizontal e 5 pixels na vertical em torno do label,
        # garantindo que o texto não fique muito próximo 
        # das bordas do tooltip, melhorando a legibilidade.
label_tooltip_aluno.pack(padx=10, pady=5)

# Eventos para exibir e ocultar detalhes no painel lateral e tooltip
# Associa eventos de movimento do mouse às funções de 
        # exibição e ocultação de detalhes.
# 'tabela.bind('<Motion>', exibir_detalhes)' vincula o evento 
        # de movimento do mouse sobre a tabela principal à 
        # função 'exibir_detalhes'.
# Isso permite que detalhes da turma sejam exibidos dinamicamente 
        # no painel lateral à medida que o usuário move o 
        # mouse sobre diferentes turmas.
tabela.bind('<Motion>', exibir_detalhes)

# 'tabela_detalhes.bind('<Motion>', exibir_tooltip_aluno)' vincula o 
        # evento de movimento do mouse sobre a tabela de detalhes à 
        # função 'exibir_tooltip_aluno'.
# Quando o mouse passa sobre os itens da tabela de detalhes, o 
        # tooltip é exibido, mostrando informações adicionais 
        # do aluno sob o cursor.
tabela_detalhes.bind('<Motion>', exibir_tooltip_aluno)

# 'tabela_detalhes.bind('<Leave>', ocultar_tooltip_aluno)' vincula o 
        # evento de saída do mouse da tabela de detalhes à função 'ocultar_tooltip_aluno'.
# Isso garante que o tooltip seja ocultado quando o mouse deixar a 
        # área da tabela de detalhes, evitando que informações 
        # desatualizadas permaneçam visíveis.
tabela_detalhes.bind('<Leave>', ocultar_tooltip_aluno)


# Carregar dados na tabela principal
# Este loop percorre cada linha do DataFrame 'estatisticas', 
        # que contém as estatísticas calculadas para cada turma.
for _, row in estatisticas.iterrows():
    
    # 'estatisticas.iterrows()' gera um iterador sobre as linhas do 
            # DataFrame 'estatisticas', retornando o índice (_) e 
            # a linha (row) para cada iteração.
    # O underscore (_) é usado para descartar o índice, 
            # pois não é necessário aqui.

    # 'tabela.insert('', 'end', values=(row['Turma'], f"{row['Média_da_Turma']:.2f}", 
            # row['Total_de_Faltas']))' insere uma nova linha na tabela.
    # O primeiro argumento '', indica que o item será inserido 
            # na raiz da árvore da tabela.
    # 'end' indica que a nova linha será adicionada ao final 
            # da lista de linhas já existentes.
    # 'values=(...)' define os valores a serem inseridos na nova linha:
    # 'row['Turma']' obtém o valor da coluna 'Turma' para a linha atual.
    # 'f"{row['Média_da_Turma']:.2f}"' formata o valor da 
            # coluna 'Média da Turma' como uma string com duas casas decimais.
    # 'row['Total_de_Faltas']' obtém o valor da coluna 
            # 'Total de Faltas' para a linha atual.
    tabela.insert('', 
                  'end', 
                  values=(row['Turma'], f"{row['Média_da_Turma']:.2f}", row['Total_de_Faltas']))

# janela.mainloop() é o método que inicia o loop principal da janela Tkinter.
janela.mainloop()