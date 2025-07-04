# Importação dos módulos necessários

# Tkinter, para criação da interface gráfica
import tkinter as tk  

# ttk para widgets mais modernos e filedialog para diálogos de arquivo
from tkinter import ttk, filedialog  

# Pandas, para manipulação de dados
import pandas as pd  


# Função para carregar dados do arquivo Excel e criar abas 
        # para cada departamento na interface gráfica
def carregar_dados():
    
    # Declara 'df_original' como uma variável global, permitindo que 
            # seja acessada e modificada em outras partes do programa
    global df_original

    # Utiliza a função 'read_excel' da biblioteca pandas para carregar os 
            # dados do arquivo 'funcionarios.xlsx'.
    # Especifica que os dados devem ser lidos da aba chamada 'Dados'.
    # O resultado é armazenado na variável global 'df_original', que 
            # agora contém o DataFrame com todos os dados do arquivo.
    df_original = pd.read_excel('funcionarios.xlsx', sheet_name='Dados')
    
    # Aplica uma função de formatação à coluna 'Salário' do DataFrame.
    # Esta função transforma cada valor numérico em uma string formatada 
            # com separadores de milhar e duas casas decimais,
    # trocando o separador decimal ponto por vírgula, e o separador de 
            # milhares vírgula por ponto, adaptando ao formato monetário brasileiro.
    # Exemplo: O valor float 12345.67 será convertido para a string "12.345,67".
    df_original['Salário'] = df_original['Salário'].apply(
        lambda x: f"{x:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
    )
    
    # Utiliza a função 'unique' para extrair uma lista de valores 
            # únicos da coluna 'Departamento' do DataFrame.
    # Isso é útil para criar uma aba separada para cada departamento 
            # na interface gráfica.
    departamentos = df_original['Departamento'].unique()
    
    # Inicia um loop sobre cada departamento único extraído do DataFrame.
    for dept in departamentos:
        
        # Cria um novo 'Frame' (painel) usando a biblioteca tkinter, que 
                # será usado como aba dentro de um 'Notebook' (caderno de abas).
        aba = ttk.Frame(caderno)
        
        # Adiciona este novo 'Frame' ao 'Notebook' chamado 'caderno', 
                # configurando o nome da aba com o nome do departamento.
        caderno.add(aba, text=dept)
        
        # Armazena o objeto 'Frame' no dicionário 'abas', usando o 
                # nome do departamento como chave.
        # Isso permite acessar facilmente o 'Frame' correspondente a 
                # cada departamento posteriormente.
        abas[dept] = aba
    
    # Chama a função 'aplicar_filtro()' logo após carregar e 
            # configurar as abas.
    # Esta função é responsável por filtrar os dados exibidos em 
            # cada aba com base em critérios de busca especificados pelo usuário.
    aplicar_filtro()


# Função para aplicar o filtro em todas as abas baseadas no termo 
            # de busca inserido pelo usuário
def aplicar_filtro():
    
    # Obtém o texto inserido no campo de entrada de filtro, converte 
            # todo o texto para minúsculas para facilitar a comparação 
            # insensível a maiúsculas/minúsculas
    termo = entrada_filtro.get().lower()
    
    # Itera sobre cada departamento e a aba correspondente no 
            # dicionário 'abas'
    for dept, aba in abas.items():
        
        # Remove todos os widgets existentes na aba para preparar a 
                # aba para uma nova visualização de dados.
        # O método 'winfo_children()' retorna uma lista de todos os 
                # widgets (filhos) presentes no widget pai (aba), e 
                # 'destroy()' deleta esses widgets.
        for widget in aba.winfo_children():
            widget.destroy()
        
        # Filtra o DataFrame original para encontrar as linhas 
                # onde o termo de busca está presente.
        # O método 'apply()' aplica uma função a cada linha ('axis=1' 
                # especifica que a operação é por linha e não por coluna).
        # A função lambda é uma função anônima usada aqui para converter 
                # cada linha em uma string (sem os índices das colunas) e 
                # verificar se o termo está presente.
        # 'to_string(index=False)' converte a linha em uma string 
                # sem incluir os índices.
        # 'lower()' converte a string em minúsculas para corresponder ao 
                # termo de busca também em minúsculas.
        df_filtrado = df_original[df_original.apply(lambda row: termo in row.to_string(index=False).lower(), axis=1)]
        
        # Filtra novamente para manter apenas as linhas do departamento atual do loop.
        # Esta operação seleciona as linhas do DataFrame onde a coluna 
                # 'Departamento' é igual ao departamento da iteração atual.
        df_dept = df_filtrado[df_filtrado['Departamento'] == dept]
        
        # Cria um objeto Treeview na aba, especificando as colunas que 
                # devem ser exibidas e configurando para mostrar apenas 
                # os cabeçalhos das colunas.
        tree = ttk.Treeview(aba, columns=list(df_dept.columns), show='headings')
        
        # 'pack()' é usado para adicionar o Treeview ao layout da aba e configurá-lo 
                # para expandir e preencher o espaço disponível tanto 
                # vertical quanto horizontalmente.
        tree.pack(expand=True, fill='both')
        
        # Configura o cabeçalho e o alinhamento das colunas no Treeview.
        # Para cada coluna no DataFrame do departamento, define o 
                # texto do cabeçalho e o alinhamento central.
        for col in df_dept.columns:

            # Configura o texto do cabeçalho da coluna.
            tree.heading(col, text=col)  

            # Configura o alinhamento do texto da coluna para o centro.
            tree.column(col, anchor='center')  
        
        # Insere cada linha do DataFrame filtrado no Treeview.
        # Itera sobre cada linha e index do DataFrame do departamento e 
                # insere a linha no Treeview.
        # Cada linha é convertida em uma lista de seus valores para 
                # ser inserida no Treeview.
        for index, row in df_dept.iterrows():
            tree.insert("", "end", values=list(row))
        
        # Armazena o DataFrame filtrado para cada departamento no 
                # dicionário 'dados_filtrados'.
        # Isso é útil para funções que precisam exportar os dados 
                # filtrados, como salvar em um arquivo Excel.
        dados_filtrados[dept] = df_dept

         
# Função para exportar os dados filtrados da aba que está 
                # atualmente ativa na interface do usuário
def exportar_dados_filtrados_aba_ativa():
    
    # Obtém o título da aba atualmente selecionada no widget 'caderno', 
            # que é um objeto Notebook (caderno de abas) do tkinter.
    # 'caderno.select()' retorna o ID da aba atualmente selecionada e 
            # 'caderno.tab(..., "text")' obtém o texto (nome) dessa aba.
    aba_ativa = caderno.tab(caderno.select(), "text")

    # Tenta obter o DataFrame associado à aba ativa usando o nome da 
            # aba como chave no dicionário 'dados_filtrados'.
    # O método 'get' tenta encontrar o DataFrame no dicionário. 
            # Se não encontrar, retorna 'None' (Nenhum).
    df_exportar = dados_filtrados.get(aba_ativa)

    # Verifica se um DataFrame foi de fato encontrado. Se 'df_exportar' 
            # não for None, prossegue com a exportação.
    if df_exportar is not None:
        
        # Abre uma caixa de diálogo para salvar arquivos, permitindo ao 
                # usuário escolher onde deseja salvar o arquivo Excel.
        # 'defaultextension' garante que o arquivo seja salvo com a extensão '.xlsx'.
        # 'filetypes' especifica os tipos de arquivos que o usuário 
                # pode salvar, limitando a escolha a arquivos Excel.
        arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

        # Verifica se o usuário selecionou um caminho de arquivo 
                # válido (se ele não cancelou a operação).
        if arquivo:
            
            # Utiliza o método 'to_excel' do DataFrame para salvar os 
                    # dados no caminho especificado.
            # 'index=False' significa que os índices do DataFrame não 
                    # serão escritos no arquivo, apenas os dados.
            df_exportar.to_excel(arquivo, index=False)


# Função para exportar os dados filtrados de todas as abas para um 
        # único arquivo Excel, criando uma aba no arquivo 
        # para cada departamento
def exportar_todas_abas():
    
    # Abre uma caixa de diálogo para que o usuário escolha o local e o 
            # nome do arquivo onde deseja salvar os dados.
    # A extensão padrão é definida como '.xlsx' para garantir que o 
            # arquivo seja compatível com o Excel.
    # O tipo de arquivo é restringido a arquivos Excel para prevenir a 
            # seleção de um formato incompatível.
    arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

    # Verifica se um caminho de arquivo foi selecionado (ou seja, o 
            # usuário não cancelou a operação de salvamento).
    if arquivo:
        
        # Cria um objeto 'ExcelWriter' que é usado para escrever 
                # dados em diferentes abas de um único arquivo Excel.
        # O 'ExcelWriter' é utilizado aqui no contexto de um gerenciador 
                # de contexto 'with', que garante que o arquivo seja
        # fechado corretamente após a escrita dos dados, mesmo que 
                # ocorra um erro durante o processo.
        with pd.ExcelWriter(arquivo) as writer:
            
            # Itera sobre cada chave no dicionário 'abas', que contém 
                    # os nomes dos departamentos.
            for dept in abas.keys():
                
                # Tenta obter o DataFrame correspondente ao departamento 
                        # atual do dicionário 'dados_filtrados'.
                # Se o departamento não tiver dados filtrados associados, um 
                        # novo DataFrame vazio é criado como fallback.
                df_exportar = dados_filtrados.get(dept, pd.DataFrame())

                # Escreve o DataFrame no arquivo Excel usando o 'ExcelWriter'.
                # Cada DataFrame é escrito em uma aba separada, nomeada com o 
                        # nome do departamento ('sheet_name=dept').
                # 'index=False' indica que os índices do DataFrame não serão 
                        # incluídos no arquivo, apenas os dados das colunas.
                df_exportar.to_excel(writer, sheet_name=dept, index=False)
                

# Configura a janela principal
janela = tk.Tk()  
# Esta linha cria uma nova janela principal usando Tkinter. 'Tk()' é o 
        # construtor da classe que inicializa uma nova janela.
# A variável 'janela' agora se refere a esta janela principal do aplicativo.

janela.title("Gestão de Funcionários")  
# Configura o título da janela principal. O texto "Gestão de Funcionários" 
        # aparecerá na barra de título da janela.

# Título do projeto
titulo = tk.Label(janela, text="Projeto: Gestão de Funcionários", font=("Arial", 16, "bold"))  
# Cria um widget de texto (rótulo) que será usado para exibir o 
        # título do projeto dentro da janela.
# 'tk.Label' cria um rótulo, e os parâmetros incluem a janela 
        # onde o rótulo será exibido,
# o texto a ser mostrado e a fonte do texto, que neste caso é Arial, 
        # tamanho 16 e em negrito.

titulo.pack(pady=10)  
# Empacota o rótulo 'titulo' na janela, tornando-o visível.
# 'pack()' é um gerenciador de geometria em Tkinter que organiza 
        # widgets em blocos antes de colocá-los na janela.
# 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e abaixo 
        # do rótulo para separá-lo de outros elementos.

# Campo de filtro
frame_filtro = tk.Frame(janela)  
# Cria um frame (quadro) dentro da janela principal. Frames são 
        # contêineres usados para agrupar outros widgets.
# Este frame específico será usado para conter o campo de filtro e 
        # qualquer outro widget relacionado ao filtro.

frame_filtro.pack(pady=5)  
# Empacota o frame 'frame_filtro' na janela principal. Assim como o 
        # rótulo, ele usa o gerenciador de geometria 'pack()'.
# 'pady=5' proporciona um espaçamento vertical de 5 pixels acima e abaixo do 
        # frame para evitar que os elementos fiquem muito juntos.


# Cria um rótulo (label) dentro do frame de filtro
label_filtro = tk.Label(frame_filtro, text="Filtrar:")
# Este comando cria um widget de rótulo chamado 'label_filtro' 
        # dentro do 'frame_filtro'.
# O texto "Filtrar:" é definido como o conteúdo do rótulo, que serve para 
        # indicar ao usuário que o campo ao lado é um campo de filtro.

label_filtro.pack(side='left', padx=5)
# Organiza o 'label_filtro' dentro de seu contêiner (frame_filtro) 
        # usando o gerenciador de geometria 'pack()'.
# O argumento 'side='left'' faz com que o rótulo seja posicionado no 
        # lado esquerdo dentro do frame.
# 'padx=5' adiciona um espaço horizontal de 5 pixels entre a borda do 
        # frame e o rótulo para evitar que o texto fique colado nas bordas.

# Cria um campo de entrada (entry) para inserção de texto 
        # dentro do frame de filtro
entrada_filtro = tk.Entry(frame_filtro)
# Este comando cria um widget de entrada de texto chamado 
        # 'entrada_filtro' dentro do 'frame_filtro'.
# O widget Entry permite ao usuário inserir uma linha de texto, 
        # sendo aqui utilizado para receber o termo de filtro.

entrada_filtro.pack(side='left', padx=5, fill='x', expand=True)
# Organiza o 'entrada_filtro' ao lado do 'label_filtro' usando o 
        # gerenciador de geometria 'pack()'.
# 'side='left'' faz com que o campo de entrada fique à esquerda 
        # dentro do frame, imediatamente após o rótulo.
# 'padx=5' adiciona um espaço horizontal de 5 pixels entre o 
        # rótulo e o campo de entrada.
# 'fill='x'' faz com que o campo de entrada expanda horizontalmente 
        # para preencher todo o espaço horizontal disponível no frame.
# 'expand=True' permite que o widget de entrada expanda além de seu 
        # tamanho de conteúdo para ocupar qualquer espaço extra disponível no frame.

# Associa um evento de liberação de tecla ao campo de entrada
entrada_filtro.bind("<KeyRelease>", lambda event: aplicar_filtro())
# Este comando vincula um evento ao widget 'entrada_filtro' de 
        # forma que sempre que uma tecla for solta após ser pressionada,
        # a função 'aplicar_filtro()' será chamada.
# O evento 'KeyRelease' é acionado sempre que o usuário libera uma 
        # tecla que foi pressionada no campo de entrada.
# 'lambda event: aplicar_filtro()' é uma função anônima que é 
        # chamada quando o evento ocorre; ela ignora o evento em si
# e simplesmente chama 'aplicar_filtro()' para atualizar os 
        # dados exibidos com base no texto inserido.


# Cria o caderno de abas
caderno = ttk.Notebook(janela)
# Este comando cria um objeto 'Notebook', que é um widget que 
        # permite a organização de interfaces em abas separadas.
# 'ttk.Notebook(janela)' cria o caderno dentro da janela 
        # principal definida anteriormente.
# O objeto 'caderno' será usado para adicionar abas individuais, 
        # cada uma potencialmente contendo diferentes interfaces ou dados.

caderno.pack(expand=True, fill='both')
# Este comando organiza o 'caderno' dentro da janela principal 
        # usando o gerenciador de geometria 'pack()'.
# 'expand=True' faz com que o caderno se expanda para ocupar qualquer 
        # espaço adicional na janela, adaptando-se ao tamanho da janela.
# 'fill='both'' faz com que o caderno preencha tanto o espaço horizontal 
        # quanto o vertical disponível na janela.
# Isso garante que o caderno utilize efetivamente o espaço 
        # disponível na interface.

# Dicionário para armazenar as abas e os dados filtrados
abas = {}
# Cria um dicionário vazio chamado 'abas'. Este dicionário será 
        # usado para armazenar e acessar facilmente os objetos de aba
# associados a cada departamento ou categoria de dados dentro do 
        # caderno. A chave será o nome do departamento e o valor será o 
        # objeto Frame da aba correspondente.

dados_filtrados = {}
# Cria um dicionário vazio chamado 'dados_filtrados'. Este dicionário 
        # armazenará os DataFrames filtrados associados a cada aba.
# Isso permite manipular e acessar os dados filtrados conforme necessário, 
        # como durante operações de exportação.

# Botões para exportar as abas
frame_botoes = tk.Frame(janela)
# Cria um novo frame (container) chamado 'frame_botoes' dentro 
        # da janela principal.
# Este frame será utilizado para agrupar botões relacionados a 
        # operações como exportar dados.

frame_botoes.pack(pady=10)
# Organiza o 'frame_botoes' na janela principal usando o 
        # gerenciador de geometria 'pack()'.
# 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e 
        # abaixo do frame para separá-lo de outros elementos na interface.
# Isso ajuda a manter a interface organizada e visualmente agradável, 
        # proporcionando espaço suficiente entre diferentes componentes.


# Cria um botão para exportar os dados da aba atualmente ativa
botao_exportar_aba = tk.Button(frame_botoes, 
                               text="Exportar Dados Filtrados da Aba Ativa", 
                               command=exportar_dados_filtrados_aba_ativa)
# 'tk.Button' cria um novo botão dentro do 'frame_botoes'.
# 'text' define o texto que aparecerá no botão, informando ao 
        # usuário sua função.
# 'command' define a função que será executada quando o botão for 
        # clicado, neste caso, 'exportar_dados_filtrados_aba_ativa',
        # que exporta os dados da aba que está atualmente ativa na interface.

botao_exportar_aba.pack(side='left', padx=5)
# Organiza o botão 'botao_exportar_aba' dentro do frame 'frame_botoes' 
        # usando o gerenciador de geometria 'pack()'.
# 'side='left'' coloca o botão à esquerda dentro do frame, alinhando-o 
        # horizontalmente com outros elementos que possam estar no frame.
# 'padx=5' adiciona um espaçamento horizontal de 5 pixels à esquerda e à 
        # direita do botão, evitando que ele fique muito próximo de outros elementos.

# Cria um botão para exportar os dados de todas as abas
botao_exportar_todas = tk.Button(frame_botoes, 
                                 text="Exportar Todas as Abas", 
                                 command=exportar_todas_abas)
# Este botão tem uma função similar ao botão anterior, mas sua ação é 
        # exportar os dados de todas as abas.
# A função 'exportar_todas_abas' é chamada quando este botão é clicado, 
        # permitindo ao usuário salvar os dados de todas as abas em um único arquivo Excel.

botao_exportar_todas.pack(side='left', padx=5)
# Organiza o botão 'botao_exportar_todas' no 'frame_botoes' 
        # ao lado do botão anterior.
# Usar 'side='left'' e 'padx=5' assegura que os botões estejam 
        # alinhados horizontalmente e adequadamente espaçados.

# Carrega os dados e cria as abas
carregar_dados()
# Esta chamada de função executa 'carregar_dados()', que é 
        # responsável por carregar os dados do arquivo Excel,
# formatar os dados conforme necessário, e criar abas dinâmicas 
        # no 'caderno' de acordo com categorias ou departamentos dos dados.

# Executa a aplicação
janela.mainloop()
# 'mainloop()' é um método de 'tk.Tk()' que executa a 
# janela principal da aplicação.