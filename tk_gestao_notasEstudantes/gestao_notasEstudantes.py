# Importa o módulo tkinter para criar interfaces gráficas.
import tkinter as tk  

# Importa classes adicionais para usar abas e diálogos de arquivos.
from tkinter import ttk, filedialog  

# Importa o pandas para manipulação de dados em formato de tabelas (DataFrames).
import pandas as pd  

# Função que recebe um DataFrame (df) como argumento e calcula a 
        # média das notas dos alunos e sua situação acadêmica.
def calcular_media_situacao(df):
    
    # Calcula a média das notas dos alunos.
    # A função seleciona as colunas correspondentes às 
            # notas ('Nota 1', 'Nota 2', 'Nota 3', 'Nota 4').
    # O método '.mean(axis=1)' calcula a média dessas notas 
            # para cada linha (cada aluno), ou seja, calcula a 
            # média horizontalmente.
    df['Média'] = df[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1)
    
    # Função interna para definir a situação do aluno baseada 
            # em sua média e quantidade de faltas.
    # Esta função será aplicada a cada linha do DataFrame.
    def definir_situacao(row):
        
        # Verifica se o número de faltas do aluno é maior que 10.
        # Se for, o aluno é automaticamente reprovado por faltas.
        if row['Faltas'] > 10:
            
            return 'Reprovado por Faltas'
            
        # Se as faltas não forem o problema, verifica a média do aluno.
        # Se a média for 7 ou superior, o aluno é considerado aprovado.
        elif row['Média'] >= 7:
            
            return 'Aprovado'
            
        # Se a média for menor que 2, o aluno é reprovado por 
                # notas, indicando um desempenho muito baixo.
        elif row['Média'] < 2:
            
            return 'Reprovado por Notas'
            
        # Caso a média esteja entre 2 e 7 (exclusivo), o 
                # aluno está em recuperação.
        else:
            
            return 'Recuperação'
    
    # Aplica a função 'definir_situacao' a cada linha do 
            # DataFrame para determinar a situação de cada aluno.
    # O método 'apply' executa uma função ao longo de um 
            # eixo do DataFrame, neste caso, linha por linha (axis=1).
    df['Situação'] = df.apply(definir_situacao, axis=1)
    
    # Retorna o DataFrame modificado com as novas 
            # colunas 'Média' e 'Situação' calculadas.
    return df
    

# Função responsável por carregar os dados dos estudantes de um 
        # arquivo Excel, calcular a média e a situação de cada 
        # estudante, e criar abas na interface gráfica para cada turma.
def carregar_dados():
    
    # Declara 'df_original' como uma variável global para que 
            # possa ser acessada e modificada em outras partes do código.
    global df_original

    # Carrega os dados do arquivo 'notas_estudantes.xlsx', especificamente 
            # da aba (sheet) chamada 'Dados'.
    # Utiliza a biblioteca pandas, que é especializada em manipulação de 
            # dados tabulares, para ler o arquivo Excel.
    # O resultado é armazenado na variável df_original, que agora contém um 
            # DataFrame com todos os dados da aba 'Dados'.
    df_original = pd.read_excel('notas_estudantes.xlsx', sheet_name='Dados')
    
    # Chama a função 'calcular_media_situacao' para calcular a média das 
            # notas de cada estudante e definir sua situação acadêmica.
    # Esta função modifica o DataFrame 'df_original' adicionando duas 
            # novas colunas: 'Média' e 'Situação'.
    df_original = calcular_media_situacao(df_original)
    
    # Extrai uma lista de turmas únicas do DataFrame. A coluna 'Turma' 
            # contém identificações de turmas às quais os estudantes pertencem.
    # O método 'unique' é usado para obter uma lista de valores 
            # únicos na coluna 'Turma', evitando repetições.
    turmas = df_original['Turma'].unique()
    
    # Itera sobre a lista de turmas únicas para criar uma aba na 
            # interface gráfica para cada turma.
    for turma in turmas:
        
        # Cria um novo Frame (quadro) dentro do widget 'caderno', que é 
                # um objeto Notebook do ttk (melhoria do Tkinter).
        # Cada Frame funcionará como uma aba contendo informações 
                # específicas de uma turma.
        aba = ttk.Frame(caderno)

        # Adiciona o Frame recém-criado ao objeto 'caderno' como uma 
                # nova aba, e define o texto da aba como o nome da turma.
        caderno.add(aba, text=turma)

        # Armazena o Frame em um dicionário 'abas', usando o nome da 
                # turma como chave. Isso permite acessar facilmente
                # o Frame correspondente a uma turma específica em 
                # outras partes do código.
        abas[turma] = aba
    
    # Após criar as abas, chama a função 'aplicar_filtro' para 
            # filtrar inicialmente os dados e exibir os resultados.
    # Esta função prepara cada aba para mostrar os dados relevantes 
            # filtrados de acordo com critérios definidos pelo usuário.
    aplicar_filtro()


# Função para aplicar cores específicas às linhas de 
        # uma Treeview com base na situação dos alunos.
def colorir_situacao(tree, col_index):
    
    # Itera sobre cada item (linha) na Treeview.
    for item in tree.get_children():
        
        # Obtém o valor da coluna específica que contém a situação do aluno.
        # 'tree.item(item, "values")' acessa os dados da linha especificada,
        # e '[col_index]' seleciona a coluna que contém a situação do aluno.
        situacao = tree.item(item, "values")[col_index]

        # Aplica tags com base na situação para posterior 
                # configuração de cores.
        if situacao == "Aprovado":

            # Atribui a tag "aprovado" ao item.
            tree.item(item, tags=("aprovado",))  
            
        elif situacao == "Recuperação":

            # Atribui a tag "recuperacao" ao item.
            tree.item(item, tags=("recuperacao",))  
            
        elif situacao == "Reprovado por Notas":

            # Atribui a tag "reprovado_notas" ao item.
            tree.item(item, tags=("reprovado_notas",))  
            
        elif situacao == "Reprovado por Faltas":

            # Atribui a tag "reprovado_faltas" ao item.
            tree.item(item, tags=("reprovado_faltas",))  

    # Configura a aparência das tags definidas anteriormente.
    # Cada chamada 'tree.tag_configure' configura a cor de 
            # fundo e a cor do texto para os itens com a 
            # tag correspondente.

    # Verde claro para aprovados.
    tree.tag_configure("aprovado", background="#d4edda", foreground="#155724")  

    # Amarelo para recuperação.
    tree.tag_configure("recuperacao", background="#fff3cd", foreground="#856404")  

    # Rosa para reprovado por notas.
    tree.tag_configure("reprovado_notas", background="#f8d7da", foreground="#721c24")  

    # Rosa claro para reprovado por faltas.
    tree.tag_configure("reprovado_faltas", background="#f5c6cb", foreground="#721c24")


# Função destinada a aplicar um filtro de texto em todas as abas da 
        # interface gráfica, atualizando os dados exibidos com 
        # base no termo inserido pelo usuário.
def aplicar_filtro():
    
    # Obtém o texto do campo de entrada do filtro, convertendo-o 
            # para minúsculas para garantir uma comparação 
            # insensível a maiúsculas/minúsculas.
    termo = entrada_filtro.get().lower()
    
    # Itera sobre cada par de turma e aba armazenados no 
            # dicionário 'abas'.
    for turma, aba in abas.items():
        
        # Remove todos os widgets existentes na aba atual.
        # 'winfo_children()' retorna uma lista de todos os 
                # widgets (componentes) filhos presentes na aba,
                # e 'destroy()' é chamado em cada um para limpar a 
                # aba antes de adicionar novos elementos.
        for widget in aba.winfo_children():
            
            widget.destroy()
        
        # Filtra o DataFrame original para encontrar entradas que 
                # contêm o termo de busca em qualquer coluna.
        # 'df_original.apply(lambda...)' aplica uma função anônima (lambda) 
                # que converte cada linha do DataFrame em uma string
                # e verifica se o termo de busca está contido nessa 
                # string. O filtro é aplicado a todas as linhas.
        df_filtrado = df_original[df_original.apply(lambda row: termo in row.to_string(index=False).lower(), axis=1)]
        
        # Dentro do DataFrame filtrado, seleciona apenas as 
                # linhas que pertencem à turma atual da iteração.
        # Isso assegura que cada aba exibirá apenas os dados 
                # relevantes para sua respectiva turma.
        df_turma = df_filtrado[df_filtrado['Turma'] == turma]
        
        # Cria uma Treeview na aba atual, que é um componente para 
                # visualização de dados em formato de tabela.
        # 'columns=list(df_turma.columns)' define as colunas da 
                # Treeview com base nas colunas do DataFrame da turma.
        # 'show='headings'' configura a Treeview para mostrar apenas os 
                # cabeçalhos das colunas, sem a coluna de índice padrão.
        tree = ttk.Treeview(aba, 
                            columns=list(df_turma.columns), 
                            show='headings')
        
        # Adiciona a Treeview à aba usando o gerenciador de geometria 'pack()'.
        # 'expand=True' e 'fill='both'' fazem com que a Treeview 
                # expanda para preencher todo o espaço disponível na aba,
        # tanto vertical quanto horizontalmente, adaptando-se ao 
                # redimensionamento da janela.
        tree.pack(expand=True, fill='both')

        
        # Define um dicionário para mapear o nome de cada coluna 
                # para uma largura específica na Treeview.
        # Isso permite que a visualização dos dados seja clara e 
                # organizada, com cada coluna tendo espaço suficiente 
                # para exibir seu conteúdo.
        largura_colunas = {
            'Nome': 150,  # Largura para a coluna "Nome".
            'Turma': 80,  # Largura para a coluna "Turma".
            'Nota 1': 60,  # Largura para a coluna "Nota 1".
            'Nota 2': 60,  # Largura para a coluna "Nota 2".
            'Nota 3': 60,  # Largura para a coluna "Nota 3".
            'Nota 4': 60,  # Largura para a coluna "Nota 4".
            'Faltas': 60,  # Largura para a coluna "Faltas".
            'Média': 80,  # Largura para a coluna "Média".
            'Situação': 120  # Largura para a coluna "Situação".
        }
        
        # Itera sobre cada coluna do DataFrame da turma para 
                # configurar a exibição na Treeview.
        for col in df_turma.columns:
            
            # Configura o cabeçalho de cada coluna com o nome da coluna.
            tree.heading(col, text=col)
            
            # Configura a largura e alinhamento de cada coluna na Treeview.
            # 'anchor='center'' centraliza o texto dentro da coluna.
            # 'width=largura_colunas.get(col, 100)' define a largura da 
                    # coluna, usando o valor do dicionário ou 100 como 
                    # padrão se a coluna não estiver listada.
            tree.column(col, 
                        anchor='center', 
                        width=largura_colunas.get(col, 100))

        
       # Itera sobre cada linha do DataFrame filtrado para 
                    # inserir os dados na Treeview.
        for indice, linha in df_turma.iterrows():
            
            # Insere cada linha do DataFrame na Treeview.
            # Cada linha é adicionada ao final da lista de entradas ('end'), e 
                    # os valores são convertidos em uma lista para serem 
                    # compatíveis com a Treeview.
            tree.insert("", 
                        "end", 
                        values=list(linha))

        
        # Chama a função 'colorir_situacao' para aplicar cores diferentes às 
                # linhas da Treeview com base na situação dos alunos.
        # A função é detalhada em outra parte do código e é usada 
                # aqui para realçar visualmente a situação dos alunos.
        colorir_situacao(tree, 
                         list(df_turma.columns).index('Situação'))


        # Armazena o DataFrame filtrado no dicionário 'dados_filtrados' 
                # com a chave sendo o nome da turma.
        # Isso permite que os dados filtrados sejam facilmente acessados 
                # para operações futuras, como a exportação de dados.
        dados_filtrados[turma] = df_turma


# Função responsável por exportar os dados filtrados da aba 
                # atualmente ativa na interface gráfica do usuário.
def exportar_dados_filtrados_aba_ativa():
    
    # Obtém o nome da aba atualmente selecionada no caderno (Notebook widget). 
            # 'caderno.tab()' é usado para acessar informações sobre a aba,
            # 'caderno.select()' retorna a referência da aba ativa e '"text"' 
            # especifica que queremos o texto (nome) da aba.
    aba_ativa = caderno.tab(caderno.select(), "text")

    # Tenta obter o DataFrame associado à aba ativa a partir 
            # do dicionário 'dados_filtrados'.
    # 'dados_filtrados.get(aba_ativa)' tenta recuperar o 
            # DataFrame usando o nome da aba ativa como chave.
    # Se a aba ativa não tiver dados associados, 'get' retorna 'None'.
    df_exportar = dados_filtrados.get(aba_ativa)

    # Verifica se existe um DataFrame para exportar. Se 'df_exportar' 
            # não for 'None', procede com a exportação.
    if df_exportar is not None:
        
        # Abre uma janela de diálogo para salvar arquivos, permitindo ao 
                # usuário escolher onde salvar o arquivo Excel.
        # 'defaultextension=".xlsx"' garante que o arquivo seja salvo com a 
                # extensão .xlsx, padrão de arquivos Excel modernos.
        # 'filetypes=[("Excel files", "*.xlsx")]' limita os tipos de arquivos 
                # que o usuário pode salvar para garantir que seja um arquivo Excel.
        arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", 
                                               filetypes=[("Excel files", "*.xlsx")])

        # Verifica se o usuário escolheu um local e nome para o 
                # arquivo (se ele não cancelou a operação de salvamento).
        if arquivo:
            
            # Exporta o DataFrame para o arquivo Excel especificado.
            # 'to_excel(arquivo, index=False)' exporta o DataFrame para o 
                    # arquivo escolhido, com 'index=False' para não 
                    # incluir o índice do DataFrame no arquivo.
            df_exportar.to_excel(arquivo, index=False)
            

# Função destinada a exportar os dados de todas as abas 
        # para um único arquivo Excel.
def exportar_todas_abas():
    
    # Abre uma janela de diálogo para que o usuário escolha o 
            # local e o nome do arquivo onde deseja salvar os dados.
    # 'defaultextension=".xlsx"' garante que o arquivo seja salvo 
            # com a extensão .xlsx, que é a extensão padrão para arquivos Excel.
    # 'filetypes=[("Excel files", "*.xlsx")]' restringe os tipos 
            # de arquivo que podem ser salvos para arquivos Excel, 
            # facilitando a utilização correta do arquivo gerado.
    arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", 
                                           filetypes=[("Excel files", "*.xlsx")])

    # Verifica se um caminho de arquivo foi realmente escolhido (se o 
            # usuário não cancelou a operação de salvar).
    if arquivo:
        
        # Cria um objeto 'ExcelWriter' que é utilizado para escrever 
                # dados em um arquivo Excel. Esse objeto permite escrever 
                # múltiplos DataFrames em diferentes abas do arquivo.
        with pd.ExcelWriter(arquivo) as writer:
            
            # Itera sobre cada chave no dicionário 'abas', que 
                    # contém os nomes das turmas.
            for turma in abas.keys():
                
                # Tenta recuperar o DataFrame associado à turma do 
                        # dicionário 'dados_filtrados'.
                # Se não existirem dados filtrados para uma turma (key), um 
                        # novo DataFrame vazio é usado como padrão para evitar erros.
                df_exportar = dados_filtrados.get(turma, 
                                                  pd.DataFrame())

                # Escreve o DataFrame no arquivo Excel usando o 'ExcelWriter'.
                # 'sheet_name=turma' define o nome da aba dentro do 
                        # arquivo Excel como o nome da turma,
                        # e 'index=False' significa que o índice do DataFrame 
                        # não será incluído no arquivo, apenas os dados das colunas.
                df_exportar.to_excel(writer, 
                                     sheet_name=turma, 
                                     index=False)



# Configura a janela principal
janela = tk.Tk()
# Inicializa a janela principal para a aplicação utilizando o 
        # Tkinter. 'Tk()' é um construtor que cria a janela raiz.

janela.title("Exercício - Gestão de Notas dos Estudantes")
# Define o título da janela, que é exibido na barra de título no 
        # topo da janela. Isso ajuda os usuários a entenderem o 
        # propósito da aplicação.

janela.geometry("1024x400")
# Configura as dimensões iniciais da janela. "1024x400" define a 
        # largura e a altura da janela em pixels,
        # proporcionando espaço suficiente para exibir todos os 
        # componentes da interface de usuário de forma confortável.

# Título do projeto
titulo = tk.Label(janela, text="Exercício - Projeto Gestão de Notas dos Estudantes", 
                  font=("Arial", 18, "bold"), 
                  bg="#343a40", 
                  fg="white")
# Cria um rótulo para o título do projeto dentro da janela principal.
# 'text' configura o texto que aparece no rótulo.
# 'font' especifica a fonte do texto (Arial, tamanho 18, em 
        # negrito), fazendo com que o título seja facilmente legível.
# 'bg' define a cor de fundo do rótulo (#343a40, um cinza escuro).
# 'fg' define a cor do texto (branco), criando um contraste alto 
        # com o fundo para melhor legibilidade.

titulo.pack(fill='x')
# Empacota o rótulo do título dentro da janela principal. 
        # O método 'pack' é usado para adicionar o widget ao layout da janela.
# 'fill='x'' faz com que o rótulo se expanda horizontalmente para 
        # preencher toda a largura da janela, garantindo que o título 
        # seja claramente visível.

# Campo de filtro
frame_filtro = tk.Frame(janela, bg="#f8f9fa")
# Cria um frame (quadro) para conter o campo de filtro. Frames 
        # são usados para organizar o layout da interface.
# 'bg' define a cor de fundo do frame (#f8f9fa, um cinza claro).

frame_filtro.pack(pady=10, fill='x')
# Empacota o frame de filtro dentro da janela principal.
# 'pady=10' adiciona um espaçamento vertical de 10 pixels 
        # acima e abaixo do frame para separá-lo visualmente 
        # de outros elementos.
# 'fill='x'' faz com que o frame se expanda horizontalmente 
        # para ocupar toda a largura da janela, alinhando-se 
        # com o título acima.

# Criação de um rótulo para indicar onde o usuário deve inserir o termo de filtro.
label_filtro = tk.Label(frame_filtro, 
                        text="Filtrar:", 
                        bg="#f8f9fa", 
                        font=("Arial", 12))
# 'tk.Label' cria um rótulo (componente textual) no frame 
        # destinado ao filtro.
# 'text="Filtrar:"' define o texto que aparecerá no rótulo, 
        # orientando o usuário sobre a função da caixa de entrada ao lado.
# 'bg="#f8f9fa"' define a cor de fundo do rótulo como um cinza claro, 
        # correspondendo ao fundo do frame para um design consistente.
# 'font=("Arial", 12)' define a fonte do texto no rótulo, usando 
        # Arial tamanho 12, para clareza e legibilidade.

# Posicionamento do rótulo dentro do frame.
label_filtro.pack(side='left', padx=10)
# 'pack(side='left')' posiciona o rótulo no lado esquerdo 
        # dentro do frame, garantindo que apareça antes da caixa de entrada.
# 'padx=10' adiciona 10 pixels de espaçamento horizontal em ambos os 
        # lados do rótulo, separando-o visualmente de outros elementos.

# Criação de uma caixa de entrada para inserção do 
        # termo de filtro pelo usuário.
entrada_filtro = tk.Entry(frame_filtro, font=("Arial", 12))
# 'tk.Entry' cria um widget de entrada de texto onde os 
        # usuários podem digitar o texto.
# 'font=("Arial", 12)' especifica a fonte do texto dentro da 
        # caixa de entrada, mantendo consistência com o rótulo.

# Posicionamento da caixa de entrada no frame.
entrada_filtro.pack(side='left', padx=10, fill='x', expand=True)
# 'pack(side='left')' posiciona a caixa de entrada ao 
        # lado (à direita) do rótulo.
# 'padx=10' adiciona espaçamento horizontal, separando a 
        # caixa de entrada do rótulo e de outros elementos potenciais.
# 'fill='x'' permite que a caixa de entrada se expanda 
        # horizontalmente conforme o espaço disponível no frame.
# 'expand=True' permite que o widget cresça para ocupar 
        # qualquer espaço adicional no layout, maximizando 
        # sua acessibilidade.

# Vinculação de um evento à caixa de entrada.
entrada_filtro.bind("<KeyRelease>", lambda event: aplicar_filtro())
# 'bind("<KeyRelease>", ...)' associa um evento de liberação 
        # de tecla à função que deve ser chamada, permitindo a 
        # filtragem dinâmica.
# 'lambda event: aplicar_filtro()' é uma função anônima que 
        # chama 'aplicar_filtro' sempre que o usuário solta uma tecla,
        # atualizando a exibição dos dados conforme o usuário digita o filtro.


# Inicializa o caderno de abas, que é um componente do ttk (themed tkinter) 
        # usado para criar abas separadas na interface gráfica.
caderno = ttk.Notebook(janela)
# Aqui, 'ttk.Notebook(janela)' cria um novo caderno 
        # dentro da janela principal. 
# Este caderno servirá como o contêiner principal para várias 
        # abas, permitindo uma navegação eficiente entre 
        # diferentes seções da interface.

# Configura o caderno para expandir e preencher todo o 
        # espaço disponível na janela.
caderno.pack(expand=True, fill='both')
# 'expand=True' permite que o caderno expanda para utilizar 
        # qualquer espaço adicional disponível, 
        # enquanto 'fill='both'' faz com que ele preencha 
        # completamente o espaço horizontal e vertical disponível,
        # garantindo que o caderno ocupe toda a área da janela principal.

# Cria um dicionário para armazenar as abas individuais e os dados 
        # filtrados associados a cada uma delas.
abas = {}
dados_filtrados = {}
# 'abas' será usado para manter uma referência direta às abas criadas, 
        # permitindo fácil acesso e manipulação das mesmas.
# 'dados_filtrados' armazenará os DataFrames filtrados correspondentes a 
        # cada aba, permitindo uma recuperação eficiente dos dados para 
        # operações como exportação.

# Cria um frame para conter os botões que permitirão a 
        # exportação dos dados das abas.
frame_botoes = tk.Frame(janela, 
                        bg="#f8f9fa")
# 'tk.Frame(janela, bg="#f8f9fa")' cria um novo frame 
        # dentro da janela principal com um fundo 
        # cinza claro (#f8f9fa), proporcionando uma separação 
        # visual clara entre as abas e os botões de ação.

# Configura o frame dos botões para expandir horizontalmente e 
        # ter um espaçamento vertical adequado.
frame_botoes.pack(pady=10, fill='x')
# 'pack(pady=10, fill='x')' posiciona o frame na janela, permitindo 
        # que ele expanda apenas horizontalmente (fill='x')
        # e adicionando um espaçamento vertical (pady=10) para 
        # garantir que não fique visualmente comprimido contra 
        # outros elementos na interface.


# Criação do botão para exportar os dados da aba ativa.
botao_exportar_aba = tk.Button(frame_botoes, 
                               text="Exportar Dados Filtrados da Aba Ativa", 
                               command=exportar_dados_filtrados_aba_ativa, 
                               bg="#007bff", 
                               fg="white", 
                               font=("Arial", 12, "bold"))
# 'tk.Button' cria um novo botão dentro do 'frame_botoes'.
# 'text="Exportar Dados Filtrados da Aba Ativa"' define o texto 
        # que aparecerá no botão, indicando sua função.
# 'command=exportar_dados_filtrados_aba_ativa' associa o botão à 
        # função que será executada quando ele for clicado. Esta função 
        # exporta os dados da aba atualmente ativa.
# 'bg="#007bff"' define a cor de fundo do botão como um azul vibrante, 
        # e 'fg="white"' define a cor do texto para branco, criando um 
        # contraste alto para facilitar a leitura.
# 'font=("Arial", 12, "bold")' especifica que o texto do botão deve 
        # usar a fonte Arial, tamanho 12, em negrito, para garantir 
        # que o texto seja visível e impactante.

# Posicionamento do botão dentro do frame.
botao_exportar_aba.pack(side='left', padx=10, pady=5)
# 'pack(side='left')' posiciona o botão no lado esquerdo dentro do 
        # frame, mantendo a ordem de leitura da esquerda para a direita.
# 'padx=10' e 'pady=5' adicionam um espaçamento horizontal de 10 pixels e 
        # um espaçamento vertical de 5 pixels em torno do botão.
# Esses espaçamentos ajudam a separar visualmente o botão de outros elementos 
        # ou botões no mesmo frame, evitando uma aparência amontoada e 
        # melhorando a acessibilidade.


# Criação do botão para exportar os dados de todas as abas.
botao_exportar_todas = tk.Button(frame_botoes, 
                                 text="Exportar Todas as Abas", 
                                 command=exportar_todas_abas, 
                                 bg="#28a745", 
                                 fg="white", 
                                 font=("Arial", 12, "bold"))
# 'tk.Button' cria um novo botão dentro do frame 'frame_botoes'.
# 'text="Exportar Todas as Abas"' define o texto que será exibido 
        # no botão, claramente indicando sua função.
# 'command=exportar_todas_abas' associa este botão à função que 
        # exportará os dados de todas as abas quando o botão for clicado, 
        # aumentando a eficiência de uso para operações em grande escala.
# 'bg="#28a745"' define a cor de fundo do botão como verde, simbolizando 
        # ação ou 'ir em frente', e 'fg="white"' estabelece a cor do 
        # texto para branco, garantindo alta legibilidade.
# 'font=("Arial", 12, "bold")' especifica a fonte do texto no botão, 
        # usando Arial tamanho 12 e em negrito para dar destaque e 
        # assegurar facilidade de leitura.

# Posicionamento do botão dentro do frame.
botao_exportar_todas.pack(side='left', padx=10, pady=5)
# 'pack(side='left')' coloca o botão à esquerda dentro do frame, 
        # seguindo o botão de exportação da aba ativa, para manter 
        # uma interface organizada e intuitiva.
# 'padx=10' e 'pady=5' adicionam espaçamento horizontal e vertical 
        # em torno do botão, respectivamente.
# Este espaçamento evita que os botões fiquem visualmente comprimidos e 
        # melhora a interação do usuário, permitindo fácil clique sem 
        # acionar botões adjacentes acidentalmente.

# Carrega os dados e cria as abas
carregar_dados()

# Executa a aplicação
janela.mainloop()