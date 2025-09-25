# Importa o módulo tkinter e o renomeia para tk, facilitando o 
        # acesso às suas funcionalidades.
import tkinter as tk

# Importa as submódulos filedialog, messagebox e ttk do tkinter.
from tkinter import filedialog, messagebox, ttk

# Importa o módulo pandas e o renomeia para pd, usado 
        # para manipulação de dados.
import pandas as pd

# Importa o módulo re para uso de expressões regulares.
import re


# Função para exportar o DataFrame atual para Excel
def exportar_para_excel(df, comando):
    
    # Abre uma janela para o usuário escolher o local e o nome do 
            # arquivo onde o DataFrame será salvo.
    # 'defaultextension' adiciona automaticamente a extensão ".xlsx" 
            # se o usuário não especificar.
    # 'filetypes' limita os tipos de arquivo que podem ser salvos para evitar erros.
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*.xlsx")])

    # Verifica se um caminho foi selecionado (o usuário pode cancelar a operação).
    if caminho_arquivo:
        
        try:
            
            # Tenta salvar o DataFrame no caminho especificado.
            # 'index=False' não inclui o índice do DataFrame no arquivo Excel.
            df.to_excel(caminho_arquivo, index=False)

            # Se o arquivo for exportado com sucesso, mostra uma mensagem de sucesso.
            messagebox.showinfo("Sucesso", f"Arquivo exportado com sucesso!\nComando: {comando}")
            
        except Exception as e:
            
            # Se ocorrer algum erro durante a exportação, mostra 
                    # uma mensagem de erro com a descrição.
            messagebox.showerror("Erro", f"Erro ao exportar o arquivo: {e}")



# Define a função que será chamada quando o usuário quiser 
        # carregar um arquivo Excel.
def carregar_arquivo():
    
    # Declara 'df' como uma variável global para que a alteração 
            # feita na variável seja refletida fora da função.
    global df
    
    # Abre uma janela para o usuário selecionar um arquivo, filtrando 
            # para mostrar apenas arquivos Excel (.xlsx).
    caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
    
    # Verifica se um caminho de arquivo foi selecionado (ou seja, o 
            # usuário não cancelou a operação).
    if caminho_arquivo:
        
        try:
            
            # Carrega o DataFrame do arquivo Excel especificado pelo usuário.
            df = pd.read_excel(caminho_arquivo)
            
            # Atualiza a visualização dos dados na interface gráfica para 
                    # mostrar os dados carregados.
            # 'atualizar_treeview' é uma função definida anteriormente que toma 
                    # um comando e um DataFrame como parâmetros,
                    # e atualiza a Treeview correspondente.
            atualizar_treeview("Arquivo carregado", df)
            
            # Exibe uma mensagem de sucesso informando ao usuário que o 
                    # arquivo foi carregado corretamente.
            messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")
            
        except Exception as e:
            
            # Caso ocorra um erro durante a leitura do arquivo (por exemplo, 
                    # arquivo corrompido ou formato inesperado),
                    # captura a exceção e mostra uma mensagem de erro detalhando o 
                    # problema encontrado.
            messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")



# Função definida para atualizar a exibição dos dados em uma Treeview 
        # com base no comando recebido e no DataFrame atualizado.
def atualizar_treeview(comando, data_frame):
    
    # Cria um novo frame dentro do frame principal 'frame_chat'. 
            # Um 'frame' é um contêiner que agrupa outros widgets.
    # O 'bg' é a propriedade de cor de fundo, aqui definida como 
            # uma cor cinza claro "#f0f0f0".
    frame_interacao = tk.Frame(frame_chat, bg="#f0f0f0")

    # Empacota o frame de interação com um padding vertical de 10 pixels. 
            # A propriedade 'fill' com valor 'both' indica que o frame deve
    # expandir-se para preencher todo o espaço horizontal e vertical 
            # disponível. 'expand=True' permite que o frame se expanda além do necessário
            # para ocupar qualquer espaço não usado na janela principal.
    frame_interacao.pack(pady=10, fill='both', expand=True)

    # Cria um rótulo (Label) dentro do frame de interação para mostrar o 
            # comando que está sendo processado.
    # O rótulo é formatado com fonte Arial tamanho 12 e negrito. 
            # A cor de fundo é a mesma do frame e a cor da fonte é um cinza escuro.
    label_comando = tk.Label(frame_interacao, 
                             text=f"Comando: {comando}", 
                             font=("Arial", 12, "bold"), 
                             bg="#f0f0f0", 
                             fg="#333")
    
    # Empacota o rótulo no frame de interação, ancorando-o à esquerda (anchor="w") e 
            # adicionando um padding horizontal de 5 pixels para melhor alinhamento.
    label_comando.pack(anchor="w", padx=5)

    # Cria uma Treeview, que é um widget para a exibição de dados em 
            # forma de tabela dentro do frame de interação.
    # A Treeview será usada para mostrar os dados do DataFrame de 
            # uma forma estruturada e interativa.
    tree = ttk.Treeview(frame_interacao)
    
    # Empacota a Treeview com um padding vertical de 5 pixels, 
            # permitindo que ela se expanda e preencha o espaço 
            # disponível no eixo X (horizontal).
    # 'expand=True' garante que o widget se ajuste ao tamanho do 
            # frame quando a janela é redimensionada.
    tree.pack(pady=5, fill='x', expand=True)

    # Configura as colunas da Treeview para corresponder exatamente às 
            # colunas do DataFrame. 'list(data_frame.columns)' converte o índice de colunas
            # do DataFrame em uma lista para que a Treeview possa 
            # entender e criar as colunas correspondentes.
    tree["columns"] = list(data_frame.columns)
    
    # Define que os cabeçalhos das colunas devem ser mostrados, usando a 
            # opção 'headings'. Isso significa que apenas os cabeçalhos 
            # das colunas serão visíveis, e a coluna de índice padrão 
            # da Treeview (geralmente uma coluna vazia à esquerda) será ocultada. 
    # Isso deixa a visualização mais limpa e focada nos dados.
    tree["show"] = "headings"

    # Itera sobre cada coluna no DataFrame para configurar os 
            # cabeçalhos e a largura das colunas na Treeview.
    for col in data_frame.columns:
        
        # Configura o texto do cabeçalho de cada coluna na Treeview 
                # para corresponder ao nome da coluna no DataFrame.
        tree.heading(col, text=col)
        
        # Define a largura inicial de cada coluna na Treeview para 100 pixels, 
                # garantindo que todos os cabeçalhos sejam visíveis e uniformes.
        tree.column(col, width=100)

    # Itera sobre cada linha no DataFrame para inserir os valores nas 
            # respectivas colunas da Treeview.
    for indice, linha in data_frame.iterrows():
        
        # Insere uma nova linha na Treeview, adicionando os valores de 
                # cada coluna. '""' indica que a linha é adicionada no 
                # final da lista de itens.
        tree.insert("", "end", values=list(linha))

    # Cria um botão dentro do frame de interação. Este botão é usado para 
            # exportar os dados que estão sendo visualizados na 
            # interface para um arquivo Excel.
    btn_exportar = tk.Button(frame_interacao, 
                             text="Exportar para Excel",  # Texto exibido no botão.
                             command=lambda: exportar_para_excel(data_frame, comando),  # Função chamada ao clicar no botão.
                             bg="#4CAF50",  # Cor de fundo do botão (verde).
                             fg="white",  # Cor do texto do botão (branco).
                             font=("Arial", 10))  # Fonte e tamanho do texto no botão.
    
    # Empacota o botão de exportação dentro do frame de interação. 'pack' é 
            # um método que organiza widgets em blocos antes de colocá-los na janela.
    # 'pady=5' adiciona um espaço vertical de 5 pixels acima e abaixo do 
            # botão, fazendo com que haja um espaço confortável em torno dele.
    btn_exportar.pack(pady=5)

    # Atualiza as tarefas pendentes no canvas, que é o contêiner onde os 
            # widgets são desenhados. Isso é necessário para recalcular a 
            # área necessária para os widgets após qualquer alteração no 
            # layout, como a adição de linhas ou colunas na Treeview.
    canvas.update_idletasks()
    
    # Configura a área de rolagem do canvas para garantir que todos os widgets 
            # possam ser visualizados. 'canvas.bbox("all")' calcula o retângulo delimitador
            # que engloba todos os itens no canvas, garantindo que 
            # nada fique fora da área visível.
    canvas.configure(scrollregion=canvas.bbox("all"))
    
    # Move a barra de rolagem vertical para a posição mais baixa (o final do conteúdo). 
    # Isso é útil quando itens são adicionados ao final da Treeview
            # e você deseja que o usuário veja os itens mais recentes 
            # sem precisar rolar manualmente.
    canvas.yview_moveto(1)


# Função para processar o comando de entrada do usuário
def processar_comando():

    # Declara que a variável 'df' usada aqui refere-se à variável 
            # global definida fora da função.
    global df

    # Obtém o texto inserido pelo usuário no campo de entrada 'entry_comando' e 
            # converte para letras minúsculas para padronizar a comparação de comandos.
    comando = entry_comando.get().lower()
    
    # Limpa o campo de entrada após obter o comando para que o usuário possa 
            # inserir novos comandos sem a necessidade de apagar manualmente o anterior.
    entry_comando.delete(0, 'end')

    # Tratamento para o comando "delete a coluna". Verifica se o texto 
            # inserido pelo usuário começa com essa string específica.
    if comando.startswith("delete a coluna"):
        
        # Remove a parte "delete a coluna" do comando, deixando apenas o 
                # nome da coluna a ser deletada e remove espaços em branco 
                # que possam existir antes ou depois do nome.
        coluna = comando.replace("delete a coluna", '').strip()
        
        # Cria um dicionário que mapeia os nomes das colunas do DataFrame 
                # para suas versões em minúsculas, facilitando a comparação 
                # insensível a maiúsculas/minúsculas.
        colunas_lower = {col.lower(): col for col in df.columns}  
        
        # Verifica se o nome da coluna inserido pelo usuário, convertido para 
                # minúsculas, está presente no dicionário de colunas.
        if coluna.lower() in colunas_lower:
            
            # Se a coluna existe, obtém o nome real da coluna (respeitando 
                    # maiúsculas/minúsculas) usando o dicionário criado.
            coluna_real = colunas_lower[coluna.lower()]
            
            # Remove a coluna do DataFrame. 'inplace=True' modifica o DataFrame 
                    # original sem a necessidade de criar uma cópia.
            df.drop(columns=[coluna_real], inplace=True)
            
            # Atualiza a visualização na Treeview para refletir a mudança no 
                    # DataFrame após a remoção da coluna.
            atualizar_treeview(comando, df)
            
        else:
            
            # Se a coluna não existir no DataFrame, mostra uma mensagem de erro ao usuário.
            messagebox.showerror("Erro", f"A coluna '{coluna}' não existe no DataFrame.")

    # renomear a coluna Vendedor para Vendedor_Principal

    # Tratamento para o comando "renomear a coluna", que permite ao 
            # usuário mudar o nome de uma coluna existente no DataFrame.
    elif comando.startswith("renomear a coluna"):
        
        # Remove a parte "renomear a coluna" do comando e divide o restante 
                # em duas partes com base na expressão " para ".
        # Isso é esperado para extrair o nome atual da coluna e o novo 
                # nome desejado pelo usuário.
        partes = comando.replace("renomear a coluna", '').strip().split(" para ")
        
        # Verifica se o comando foi dividido em exatamente duas partes: 
                # o nome atual da coluna e o novo nome.
        if len(partes) == 2:
            
            # Extrai o nome atual da coluna e o novo nome, removendo espaços 
                    # desnecessários antes e depois de cada parte.
            coluna_atual, novo_nome = partes[0].strip(), partes[1].strip()
            
            # Cria um dicionário para mapear os nomes de colunas do DataFrame para suas versões em minúsculas,
                    # facilitando a busca insensível a maiúsculas/minúsculas.
            colunas_lower = {col.lower(): col for col in df.columns}
            
            # Verifica se o nome atual da coluna, convertido para 
                    # minúsculas, existe no dicionário de colunas.
            if coluna_atual.lower() in colunas_lower:
                
                # Se a coluna existe, obtém o nome real da coluna (respeitando 
                        # maiúsculas/minúsculas) usando o dicionário criado.
                coluna_real = colunas_lower[coluna_atual.lower()]
                
                # Renomeia a coluna no DataFrame. 'columns' recebe um dicionário 
                        # onde a chave é o nome antigo da coluna e o valor é o novo nome.
                # 'inplace=True' modifica o DataFrame original sem a 
                        # necessidade de criar uma cópia.
                df.rename(columns={coluna_real: novo_nome}, inplace=True)
                
                # Atualiza a visualização na Treeview para refletir a 
                        # mudança no DataFrame após o renomeamento da coluna.
                atualizar_treeview(comando, df)
                
            else:
                
                # Se a coluna não existir no DataFrame, mostra uma 
                        # mensagem de erro ao usuário.
                messagebox.showerror("Erro", f"A coluna '{coluna_atual}' não existe no DataFrame.")


    # filtrar na coluna Meta pelo valor 50000

    # Tratamento para o comando "filtrar na coluna", que permite ao 
            # usuário filtrar dados em uma coluna específica do DataFrame.
    elif comando.startswith("filtrar na coluna"):
        
        # Remove a parte "filtrar na coluna" do comando e divide o 
                # restante em duas partes na frase " pelo valor ".
        # Isso é usado para separar o nome da coluna e o valor pelo qual o 
                # usuário deseja filtrar.
        partes = comando.replace("filtrar na coluna", '').strip().split(" pelo valor ")
        
        # Verifica se o comando foi dividido em exatamente duas partes: 
                # o nome da coluna e o valor de filtro.
        if len(partes) == 2:
            
            # Extrai o nome da coluna e o valor do filtro, removendo espaços 
                    # extras antes e depois de cada parte.
            coluna, valor = partes[0].strip(), partes[1].strip()
        
            # Cria um dicionário que mapeia os nomes de colunas do 
                    # DataFrame para versões em minúsculas.
            # Isso ajuda a realizar uma comparação insensível a maiúsculas/minúsculas.
            colunas_lower = {col.lower(): col for col in df.columns}
        
            # Verifica se a coluna mencionada pelo usuário, convertida 
                    # para minúsculas, existe no DataFrame.
            # Isso é crucial para evitar erros ao tentar acessar uma coluna 
                    # que não existe, o que causaria uma exceção.
            if coluna.lower() in colunas_lower:
                
                # Obtém o nome real da coluna respeitando as maiúsculas/minúsculas 
                        # originais, usando o dicionário criado.
                # O dicionário 'colunas_lower' mapeia nomes de colunas em 
                        # minúsculas para seus nomes originais,
                        # permitindo que a operação de renomeação ou manipulação 
                        # respeite o nome exato da coluna no DataFrame original.
                coluna_real = colunas_lower[coluna.lower()]
                
                # Converte todos os dados na coluna para string, remove espaços em 
                        # branco no começo e no fim e converte para minúsculas.
                # Essa padronização é vital para garantir que as comparações de 
                        # valores sejam consistentes e precisas, independente
                        # de como os dados foram originalmente formatados ou inseridos.
                # 'astype(str)': Converte todos os valores da coluna para strings, 
                        # garantindo que operações de texto possam ser realizadas.
                # 'str.strip()': Remove espaços extras do começo e do fim de cada valor.
                # 'str.lower()': Converte todas as strings para minúsculas para 
                        # uniformizar os dados e facilitar comparações.
                df[coluna_real] = df[coluna_real].astype(str).str.strip().str.lower()
                
                # Processa o valor de filtro da mesma maneira, garantindo que a 
                        # comparação seja justa e funcional.
                # O valor digitado pelo usuário também é convertido para string, 
                        # espaços são removidos e tudo é convertido para minúsculas.
                # Isso assegura que a comparação entre o valor de filtro e os 
                        # dados na coluna seja realizada de maneira coerente.
                valor = valor.strip().lower()
                
                # Filtra o DataFrame para incluir apenas as linhas onde o valor da 
                        # coluna especificada corresponde ao valor de filtro.
                # A comparação é feita após a padronização dos dados, o que 
                        # aumenta a precisão do filtro.
                df_filtrado = df[df[coluna_real] == valor]
                
                # Verifica se o DataFrame filtrado não está vazio (ou seja, 
                        # se existem linhas que correspondem ao critério).
                # Um DataFrame vazio indica que nenhum registro correspondente 
                        # foi encontrado com o valor especificado.
                if not df_filtrado.empty:
                    
                    # Se dados correspondentes foram encontrados, atualiza a 
                            # Treeview para mostrar esses dados.
                    # A Treeview é uma representação visual do DataFrame filtrado, 
                            # permitindo ao usuário ver o resultado do filtro aplicado.
                    atualizar_treeview(comando, df_filtrado)
                    
                else:
                    
                    # Se nenhum dado correspondente foi encontrado, exibe um aviso ao usuário.
                    # Isso informa que, apesar do processo ter sido realizado 
                            # corretamente, não existem dados que atendam ao critério de filtro.
                    messagebox.showwarning("Atenção", f"Nenhum dado encontrado para '{valor}' na coluna '{coluna_real}'.")

                    
            else:
                
                # Se a coluna não existir no DataFrame, exibe uma mensagem de erro ao usuário.
                messagebox.showerror("Erro", f"A coluna '{coluna}' não existe no DataFrame.")


    # ordenar o DataFrame pela coluna Meta

    # Tratamento para o comando que solicita a ordenação do DataFrame 
            # por uma coluna específica.
    elif comando.startswith("ordenar o dataframe pela coluna"):

        # Extrai o nome da coluna do comando digitado pelo usuário. 
                # Remove a parte inicial do comando e espaços extras.
        # Isso permite isolar o nome da coluna que o usuário deseja 
                # usar para ordenar os dados.
        coluna = comando.replace("ordenar o dataframe pela coluna", '').strip()
        
        # Cria um dicionário que mapeia os nomes das colunas do DataFrame 
                # para suas versões em minúsculas.
        # Isso é útil para fazer comparações insensíveis a maiúsculas e 
                # minúsculas, garantindo que o usuário
                # possa digitar o nome da coluna em qualquer capitalização.
        colunas_lower = {col.lower(): col for col in df.columns}
        
        # Verifica se o nome da coluna digitado pelo usuário, após ser 
                # convertido para minúsculas, está presente no dicionário de colunas.
        # Essa verificação é importante para assegurar que a coluna realmente 
                # existe no DataFrame antes de tentar ordená-lo por essa coluna.
        if coluna.lower() in colunas_lower:
            
            # Acessa o nome real da coluna usando o dicionário, o que permite obter o 
                    # nome exato como está no DataFrame, respeitando maiúsculas e minúsculas.
            coluna_real = colunas_lower[coluna.lower()]
            
            # Ordena o DataFrame pela coluna especificada. 'by=coluna_real' 
                    # indica a coluna pela qual ordenar.
            # 'ascending=True' significa que a ordenação será em ordem 
                    # crescente. 'inplace=True' modifica o DataFrame original,
                    # sem necessidade de criar um novo DataFrame ordenado.
            df.sort_values(by=coluna_real, ascending=True, inplace=True)
            
            # Atualiza a visualização dos dados na Treeview para refletir a 
                    # nova ordem dos dados após a ordenação.
            # Isso permite que o usuário veja imediatamente o resultado 
                    # da operação de ordenação.
            atualizar_treeview(comando, df)
            
        else:
            
            # Se a coluna especificada não existir no DataFrame, uma 
                    # mensagem de erro é exibida para o usuário.
            # Isso informa que o nome da coluna fornecido não foi encontrado, 
                    # ajudando o usuário a corrigir possíveis erros de digitação.
            messagebox.showerror("Erro", f"A coluna '{coluna}' não existe no DataFrame.")


    # preencher valores nulos na coluna Total de Vendas com 100

    # Tratamento para o comando que solicita preenchimento de valores 
            # nulos em uma coluna específica do DataFrame.
    elif comando.startswith("preencher valores nulos na coluna"):

        # Remove a parte inicial do comando "preencher valores nulos na 
                # coluna" e divide o restante em duas partes na frase " com ".
        # Isso é usado para separar o nome da coluna da qual os valores nulos 
                # devem ser preenchidos e o valor que deve ser usado para o preenchimento.
        partes = comando.replace("preencher valores nulos na coluna", '').strip().split(" com ")
        
        # Verifica se o comando foi dividido corretamente em exatamente 
                # duas partes: o nome da coluna e o valor de preenchimento.
        if len(partes) == 2:
            
            # Extrai o nome da coluna e o valor de preenchimento, removendo 
                    # espaços extras antes e depois de cada parte.
            coluna, valor = partes[0].strip(), partes[1].strip()
            
            # Cria um dicionário que mapeia os nomes de colunas do DataFrame 
                    # para suas versões em minúsculas.
            # Isso permite fazer comparações insensíveis a maiúsculas e minúsculas, 
                    # garantindo que o usuário possa digitar o nome da coluna
                    # em qualquer capitalização sem causar erros.
            colunas_lower = {col.lower(): col for col in df.columns}
            
            # Verifica se a coluna mencionada pelo usuário, convertida 
                    # para minúsculas, existe no DataFrame.
            if coluna.lower() in colunas_lower:
                
                # Acessa o nome real da coluna usando o dicionário, o que permite 
                        # obter o nome exato como está no DataFrame,
                        # respeitando maiúsculas e minúsculas originais.
                coluna_real = colunas_lower[coluna.lower()]
                
                # Preenche os valores nulos na coluna especificada com o 
                        # valor fornecido pelo usuário.
                # 'fillna' é um método do pandas que substitui todos os valores 
                        # NaN ou None na coluna especificada pelo 'value' fornecido.
                # 'inplace=True' modifica o DataFrame original sem a necessidade 
                        # de atribuir o resultado a uma nova variável.
                df[coluna_real].fillna(value=valor, inplace=True)
                
                # Atualiza a visualização dos dados na Treeview para refletir a 
                        # mudança no DataFrame após o preenchimento dos valores nulos.
                atualizar_treeview(comando, df)
                
            else:
                
                # Se a coluna não existir no DataFrame, uma mensagem de 
                        # erro é exibida para o usuário.
                # Isso informa que o nome da coluna fornecido não foi encontrado, 
                        # ajudando o usuário a corrigir possíveis erros de digitação.
                messagebox.showerror("Erro", f"A coluna '{coluna}' não existe no DataFrame.")


    # mostrar as primeiras 10 linhas

    # Tratamento para o comando que solicita mostrar as primeiras 
            # linhas do DataFrame.
    elif comando.startswith("mostrar as primeiras"):
        
        try:
            
            # Usa uma expressão regular para encontrar todos os números no 
                    # comando digitado pelo usuário.
            # A expressão regular '\d+' corresponde a uma ou mais 
                    # ocorrências de dígitos (0-9).
            numeros = re.findall(r'\d+', comando)
            
            # Verifica se algum número foi encontrado no comando. O número 
                    # esperado é o número de linhas que o usuário deseja visualizar.
            if numeros:
                
                # Converte o primeiro número encontrado de string para inteiro, 
                        # pois ele indica quantas das primeiras linhas devem ser mostradas.
                n = int(numeros[0])
                
                # Utiliza o método 'head' do pandas para obter as primeiras 'n' linhas do DataFrame.
                # O método 'head(n)' retorna um novo DataFrame que contém apenas 
                        # as primeiras 'n' linhas do DataFrame original.
                df = df.head(n)  # Atualiza o DataFrame global com apenas as primeiras 'n' linhas.
                
                # Atualiza a visualização na Treeview para mostrar apenas 
                        # as primeiras 'n' linhas.
                atualizar_treeview(comando, df)
                
            else:
                
                # Se nenhum número válido foi encontrado no comando, mostra 
                        # uma mensagem de erro informando o problema.
                messagebox.showerror("Erro", "Número de linhas não especificado ou inválido.")
                
        except Exception as e:
            
            # Captura qualquer outra exceção que possa ocorrer durante o 
                    # processo de extrair o número ou mostrar as linhas.
            # Isso é útil para tratar erros inesperados, como problemas com 
                    # conversão de tipos ou com o método 'head'.
            messagebox.showerror("Erro", f"Erro ao mostrar linhas: {e}")


    # mostrar as últimas 5 linhas

    # Tratamento para o comando que solicita mostrar as últimas linhas do DataFrame.
    elif comando.startswith("mostrar as últimas"):
        
        try:
        
            # Utiliza uma expressão regular para encontrar todos os números no 
                    # comando digitado pelo usuário.
            # A expressão '\d+' busca por uma ou mais ocorrências de dígitos 
                    # numéricos, ajudando a extrair o número de linhas que o usuário quer ver.
            numeros = re.findall(r'\d+', comando)
            
            # Verifica se algum número foi encontrado na string do comando.
            if numeros:
                
                # Converte o primeiro número encontrado de string para inteiro. 
                # Este número indica quantas das últimas linhas devem ser mostradas.
                n = int(numeros[0])
                
                # Utiliza o método 'tail' do pandas para obter as últimas 'n' linhas do DataFrame.
                # O método 'tail(n)' retorna um novo DataFrame que contém 
                        # apenas as últimas 'n' linhas do DataFrame original.
                df = df.tail(n)  # Atualiza o DataFrame global para incluir apenas as últimas 'n' linhas.
                
                # Atualiza a visualização na Treeview para mostrar as 
                        # últimas 'n' linhas do DataFrame.
                atualizar_treeview(comando, df)
                
            else:
                
                # Se nenhum número válido foi encontrado no comando, 
                        # mostra uma mensagem de erro.
                # Isso informa ao usuário que o comando para mostrar as 
                        # últimas linhas estava incompleto ou incorreto.
                messagebox.showerror("Erro", "Número de linhas não especificado ou inválido.")
                
        except Exception as e:
            
            # Captura qualquer outra exceção que possa ocorrer durante o 
                    # processo de extrair o número ou mostrar as linhas.
            # Tratar exceções aqui é importante para lidar com erros 
                    # inesperados que podem surgir, como erros de conversão 
                    # de tipo ou problemas ao acessar o DataFrame.
            messagebox.showerror("Erro", f"Erro ao mostrar linhas: {e}")

    # mostrar o Vendedor que mais vendeu na coluna de Total de Vendas

    # Tratamento para comandos que envolvem a exibição de quem mais ou 
            # menos vendeu em determinada coluna de quantidade.
    elif comando.startswith("mostrar o") and "que" in comando and "vendeu na coluna de" in comando:
        
        try:
            
            # Utiliza uma expressão regular para capturar a estrutura do 
                    # comando e extrair as partes relevantes.
            # A expressão regular é definida para captar três grupos de interesse:
            # 1. O nome da coluna pela qual os dados serão agrupados (ex: Vendedor, Produto).
            # 2. A palavra "mais" ou "menos" para determinar se estamos 
                    # buscando o valor máximo ou mínimo.
            # 3. O nome da coluna que contém os valores numéricos que 
                    # desejamos comparar (ex: Total de Vendas).
            padrao = r"mostrar o (.+) que (mais|menos) vendeu na coluna de (.+)"
            match = re.match(padrao, comando)  # Aplica a expressão regular ao comando fornecido.
    
            # Verifica se o comando inserido pelo usuário corresponde ao 
                    # padrão definido pela expressão regular.
            if match:
                
                # Extrai o nome da coluna que agrupa os dados (ex: Vendedor, Produto) 
                        # do primeiro grupo capturado pela expressão regular.
                coluna_grupo = match.group(1).strip()
                
                # Determina se a solicitação é para o valor máximo ou mínimo com 
                        # base no segundo grupo capturado ("mais" ou "menos").
                mais_ou_menos = match.group(2).strip()
                
                # Identifica a coluna que contém os valores numéricos a serem 
                        # analisados (ex: Total de Vendas) do terceiro grupo capturado.
                coluna_vendas = match.group(3).strip()
    
                # Cria um dicionário mapeando os nomes das colunas 
                        # do DataFrame para minúsculas.
                # Isso facilita a verificação de existência das colunas 
                        # independentemente de como foram digitadas no comando, 
                        # pois a comparação será insensível a maiúsculas e minúsculas.
                colunas_lower = {col.lower().strip(): col.strip() for col in df.columns}
                
                # Normaliza o nome da coluna de grupo e coluna de vendas 
                        # extraídos para minúsculas para garantir uma comparação precisa.
                coluna_grupo_key = coluna_grupo.lower().strip()
                coluna_vendas_key = coluna_vendas.lower().strip()

    
                # Verifica se as colunas especificadas existem no DataFrame, 
                        # usando as chaves mapeadas.
                # Este passo é crucial para garantir que as operações subsequentes 
                        # não falhem devido a referências a colunas inexistentes.
                if coluna_grupo_key in colunas_lower and coluna_vendas_key in colunas_lower:
                    
                    # Acessa os nomes reais das colunas a partir do dicionário 
                            # que mapeia nomes em minúsculas para seus equivalentes exatos no DataFrame.
                    coluna_grupo_real = colunas_lower[coluna_grupo_key]
                    coluna_vendas_real = colunas_lower[coluna_vendas_key]
                
                    # Converte os valores da coluna de vendas para numéricos, pois 
                            # as operações de agregação requerem dados numéricos.
                    # 'errors='coerce'' converte valores que não podem ser transformados 
                            # em números para NaN (Not a Number), garantindo que a operação não falhe.
                    df[coluna_vendas_real] = pd.to_numeric(df[coluna_vendas_real], errors='coerce')
                
                    # Agrupa o DataFrame pela coluna do grupo e soma os valores 
                            # de vendas para cada grupo.
                    # Esta operação é fundamental para determinar qual 
                            # grupo vendeu mais ou menos.
                    grupo_vendas = df.groupby(coluna_grupo_real)[coluna_vendas_real].sum()
                
                    # Decide se deve pegar o grupo com maior ou menor soma 
                            # de vendas baseado no comando.
                    # 'mais' indica a busca pelo máximo, 'menos' pelo mínimo.
                    if mais_ou_menos == 'mais':
                        
                        # 'idxmax()' retorna o índice do maior valor na série, o 
                                # que corresponde ao grupo com as maiores vendas.
                        grupo_selecionado = grupo_vendas.idxmax()
                        
                        # 'max()' retorna o maior valor encontrado na série, 
                                # que é o total de vendas desse grupo.
                        vendas = grupo_vendas.max()
                        
                    else:
                        
                        # 'grupo_vendas == grupo_vendas.min()' encontra todos os 
                                # índices onde o valor é igual ao menor valor na série,
                                # que pode ser útil se múltiplos grupos tiverem vendas mínimas iguais.
                        grupo_selecionado = grupo_vendas[grupo_vendas == grupo_vendas.min()]
                        
                        # 'min()' retorna o menor valor encontrado na série.
                        vendas = grupo_vendas.min()
                
                    # Cria um DataFrame filtrado que inclui apenas os registros 
                            # do grupo selecionado.
                    # A condição ternária verifica se 'mais_ou_menos' é 'menos'; se 
                            # sim, inclui todos os grupos com as menores vendas, 
                            # caso contrário, apenas o com mais vendas.
                    df_grupo = df[df[coluna_grupo_real].isin(grupo_selecionado.index)] if mais_ou_menos == 'menos' else df[df[coluna_grupo_real] == grupo_selecionado]
                
                    # Atualiza a visualização para mostrar os resultados. 
                    # Monta uma string que descreve o resultado e atualiza a 
                            # Treeview para refletir esses dados,
                            # permitindo ao usuário visualizar facilmente qual 
                            # grupo vendeu mais ou menos e qual foi o total de vendas.
                    atualizar_treeview(f"{coluna_grupo_real} que {mais_ou_menos} vendeu: {', '.join(grupo_selecionado.index) if mais_ou_menos == 'menos' else grupo_selecionado} (Total de vendas: {vendas})", df_grupo)

                else:
                    
                    # Se alguma das colunas especificadas não existir, mostra uma 
                            # mensagem de erro com as colunas disponíveis.
                    # Constrói uma string com os nomes de todas as colunas disponíveis no DataFrame.
                    # A função 'join' é usada para concatenar todos os elementos de 
                            # uma lista (neste caso, os nomes das colunas do DataFrame),
                            # separando-os com uma vírgula e um espaço. 
                    # Isso cria uma lista legível de colunas que o usuário pode referenciar.
                    colunas_disponiveis = ', '.join(df.columns)
                
                    # Exibe uma mensagem de erro ao usuário utilizando uma 
                            # caixa de diálogo de erro.
                    # 'messagebox.showerror' é uma função do Tkinter que cria uma 
                            # janela de mensagem de erro com um título e uma mensagem.
                    # O título aqui é "Erro", e a mensagem informa ao usuário que uma 
                            # das colunas especificadas não existe no DataFrame,
                            # e também lista todas as colunas disponíveis para 
                            # auxiliar na correção do comando.
                    messagebox.showerror("Erro", f"Uma das colunas especificadas não existe no DataFrame.\nColunas disponíveis: {colunas_disponiveis}")
                    
            else:
                
                # Se o formato do comando não corresponder ao esperado, 
                        # informa ao usuário sobre o erro de formatação.
                messagebox.showwarning("Erro", "Comando mal formatado. Tente novamente.")
                
        except Exception as e:
            
            # Captura e reporta qualquer outro erro que ocorra 
                    # durante a execução do comando.
            messagebox.showerror("Erro", f"Erro ao mostrar o {coluna_grupo_real} que {mais_ou_menos} vendeu: {e}")                

    
    # mostrar Vendedor ordenados por vendas na coluna de Total de Vendas

    # Tratamento para o comando que solicita exibir elementos de uma 
        # coluna, ordenados por vendas em outra coluna.
    elif comando.startswith("mostrar") and "ordenados por" in comando and "na coluna de" in comando:

        try:
        
            # Utiliza uma expressão regular para capturar a estrutura do 
                    # comando e extrair as partes necessárias.
            # A expressão regular é composta para corresponder a uma sequência 
                    # específica que deve conter o nome de uma coluna a ser agrupada,
                    # uma indicação de ordenação ("ordenados por"), e o nome da 
                    # coluna de vendas que será usada para essa ordenação.
            padrao = r"mostrar (.+) ordenados por (.+) na coluna de (.+)"
            match = re.match(padrao, comando)  # Aplica a expressão regular ao comando dado pelo usuário.
        
            # Se o comando corresponder ao padrão esperado pela expressão regular, 
                    # os grupos capturados representam as partes essenciais do comando.
            if match:
                
                # Captura o nome da coluna pela qual os dados serão agrupados, 
                        # como 'Vendedor' ou 'Produto'.
                # Esta é a coluna que definirá os grupos de dados sobre os quais 
                        # as vendas serão somadas e comparadas.
                coluna_grupo = match.group(1).strip()  # Extrai e remove espaços extras ao redor do nome da coluna de grupo.
                
                # Captura o nome da coluna de vendas, que é onde os valores que 
                        # indicam a quantidade de vendas estão armazenados.
                # Esta coluna será usada para somar as vendas de cada grupo e 
                        # determinar qual grupo vendeu mais ou menos, dependendo do comando.
                coluna_vendas = match.group(3).strip()  # Extrai e remove espaços extras ao redor do nome da coluna de vendas.
        
                # Cria um dicionário que mapeia todos os nomes das colunas do 
                        # DataFrame para versões em minúsculas.
                # Isso é feito para facilitar a verificação da existência 
                        # dessas colunas no DataFrame, independentemente de 
                        # como foram digitadas no comando.
                # A normalização para minúsculas ajuda a evitar problemas de 
                        # correspondência devido a diferenças de maiúsculas/minúsculas.
                colunas_lower = {col.lower().strip(): col.strip() for col in df.columns}
                coluna_grupo_real = None  # Inicializa a variável que armazenará o nome real da coluna de grupo.
                coluna_vendas_real = None  # Inicializa a variável que armazenará o nome real da coluna de vendas.

    
                # Verifica se a coluna do grupo existe no DataFrame.
                # Percorre todas as colunas do DataFrame para encontrar uma 
                        # correspondência exata com o nome da coluna do grupo 
                        # especificado no comando.
                for col in df.columns:
                
                    # Compara o nome de cada coluna no DataFrame, convertido para 
                            # minúsculas e sem espaços adicionais, com o nome da 
                            # coluna do grupo também normalizado.
                    # Essa normalização garante que a comparação seja insensível a 
                            # diferenças de maiúsculas/minúsculas e espaços acidentais 
                            # antes ou depois do nome da coluna.
                    if col.lower().strip() == coluna_grupo.lower().strip():
                    
                        # Se encontrar uma correspondência, atribui o nome exato da 
                                # coluna (como aparece no DataFrame) à variável 'coluna_grupo_real'.
                        # Isso é importante porque o nome exato é necessário para 
                                # referenciar corretamente a coluna em operações futuras.
                        coluna_grupo_real = col
                        
                        # Interrompe o loop uma vez que a coluna desejada foi encontrada, 
                                # otimizando o desempenho ao evitar verificações 
                                # desnecessárias após a descoberta.
                        break
                
                # Verifica se a coluna de vendas existe no DataFrame.
                # Assim como a verificação anterior, este loop percorre todas as 
                        # colunas do DataFrame em busca de uma correspondência 
                        # com o nome da coluna de vendas.
                for col in df.columns:
                    
                    # Realiza a mesma normalização e comparação que o loop anterior, 
                            # mas desta vez comparando com o nome da coluna de 
                            # vendas especificada no comando.
                    if col.lower().strip() == coluna_vendas.lower().strip():
                        
                        # Se a coluna de vendas for encontrada, armazena o nome exato 
                                # da coluna no DataFrame na variável 'coluna_vendas_real'.
                        # Ter o nome exato é crucial para acessar os dados corretamente nas 
                                # operações de agregação e ordenação que seguirão.
                        coluna_vendas_real = col
                        
                        # Encerra o loop, pois não é necessário continuar a busca uma 
                                # vez que a coluna de vendas foi encontrada.
                        break

    
                # Se ambas as colunas forem encontradas no DataFrame.
                if coluna_grupo_real and coluna_vendas_real:
                    
                    # Converte os valores da coluna de vendas para numérico, uma etapa 
                            # crucial porque as operações de soma e ordenação
                            # precisam ser realizadas em dados numéricos para 
                            # obter resultados corretos.
                    df[coluna_vendas_real] = pd.to_numeric(df[coluna_vendas_real], errors='coerce')
                    
                    # A opção 'errors='coerce'' converte valores que não podem ser 
                            # transformados em números para NaN (Not a Number),
                            # garantindo que a operação não falhe por dados inválidos.
                
                    # Agrupa o DataFrame pela coluna do grupo (ex: Vendedor, Produto) e 
                            # calcula a soma dos valores de vendas para cada grupo.
                    # 'groupby' é um método poderoso que agrupa dados baseados em uma ou 
                            # mais colunas, e 'sum()' soma os valores para cada grupo.
                    grupo_vendas = df.groupby(coluna_grupo_real)[coluna_vendas_real].sum().reset_index()
                    # 'reset_index()' é usado para transformar o índice de agrupamento em 
                            # uma coluna novamente, facilitando operações subsequentes.
                
                    # Ordena os grupos resultantes de acordo com o total de 
                            # vendas em ordem decrescente.
                    # 'sort_values' é o método utilizado para ordenar os dados. 
                    # 'by=coluna_vendas_real' define a coluna de ordenação,
                            # e 'ascending=False' especifica que a ordenação 
                            # deve ser feita do maior para o menor (decrescente).
                    grupo_vendas.sort_values(by=coluna_vendas_real, ascending=False, inplace=True)
                
                    # Atualiza a Treeview para exibir os grupos ordenados por vendas. 
                    # Esta visualização ajuda o usuário a entender claramente
                            # qual grupo teve o maior volume de vendas.
                    # 'atualizar_treeview' é uma função definida para atualizar a 
                            # interface gráfica com os dados processados, mostrando 
                            # os resultados em uma tabela visual.
                    atualizar_treeview(f"{coluna_grupo_real.capitalize()} ordenados por vendas na coluna {coluna_vendas_real}", grupo_vendas)
                    
                else:
                    
                    # Se alguma das colunas não existir, mesmo após a verificação 
                            # inicial, exibe uma mensagem de erro ao usuário.
                    # Isso pode ser útil se houver uma modificação inesperada no 
                            # DataFrame ou um erro na lógica anterior.
                    # Lista todas as colunas disponíveis no DataFrame para ajudar o 
                            # usuário a corrigir o comando.
                    colunas_disponiveis = ', '.join(df.columns)  
                    messagebox.showerror("Erro", f"Uma das colunas especificadas não existe no DataFrame.\nColunas disponíveis: {colunas_disponiveis}")

            else:
                
                # Se o formato do comando não for o esperado, informa o 
                        # usuário sobre a má formatação e solicita correção.
                messagebox.showerror("Erro", "Comando mal formatado. Tente novamente.")
                
        except Exception as e:
            
            # Captura qualquer outra exceção durante o processamento e 
                    # exibe uma mensagem de erro, indicando a natureza do problema.
            messagebox.showerror("Erro", f"Erro ao mostrar {coluna_grupo_real} ordenados por vendas: {e}")

        

    
    else:

        messagebox.showerror("Erro", "Comando inválido...")



# Função para exibir dicas de comandos para o usuário. Esta função cria uma 
        # janela secundária que fornece exemplos de como usar 
        # comandos específicos na aplicação.
def mostrar_dicas():
    
    # Cria uma nova janela que é filha da janela principal do aplicativo. 
    # 'tk.Toplevel' é usado para criar uma janela que é gerenciada
            # separadamente da janela principal, mas ainda faz parte da mesma aplicação.
    janela_dicas = tk.Toplevel(janela_principal)
    
    # Define o título da janela de dicas, que aparecerá na barra de título da janela.
    janela_dicas.title("Dicas de Comandos")
    
    # Configura as dimensões da janela de dicas. 'geometry' é um método 
            # que especifica o tamanho e, opcionalmente, a posição da janela
            # no formato "largura x altura + x_offset + y_offset". Aqui, 
            # definimos apenas a largura e a altura para 600x400 pixels.
    janela_dicas.geometry("600x400")

    # Define um texto longo com vários exemplos de comandos que podem ser 
            # usados na aplicação. Este texto é usado para informar ao usuário
            # como ele pode interagir com o aplicativo através de comandos específicos.
    texto_dicas = """Exemplos de Comandos:
    
1. delete a coluna Meta
2. renomear a coluna Vendedor para Vendedor_Principal
3. filtrar na coluna Meta pelo valor 50000
4. ordenar o DataFrame pela coluna Meta
5. preencher valores nulos na coluna Total de Vendas com 100
6. mostrar as primeiras 10 linhas
7. mostrar as últimas 5 linhas
8. mostrar o Vendedor que mais vendeu na coluna de Total de Vendas
9. mostrar o Produto que menos vendeu na coluna de Total de Vendas
10. mostrar Vendedor ordenados por vendas na coluna de Total de Vendas
11. mostrar Produto ordenados por vendas na coluna de Total de Vendas
"""

    # Cria um widget de texto que pode exibir múltiplas linhas de texto. 
    # 'tk.Text' é um widget que permite exibir e editar texto.
    # 'wrap='word'' faz com que as palavras não sejam cortadas ao atingir o 
            # final da linha; em vez disso, toda a palavra é movida para a próxima linha.
    texto = tk.Text(janela_dicas, 
                    wrap='word', 
                    height=20)
    
    # Insere o texto de dicas definido anteriormente no widget de texto. 
    # '1.0' indica que o texto será inserido no início do widget.
    texto.insert('1.0', texto_dicas)
    
    # Empacota o widget de texto na janela de dicas, fazendo-o expandir para 
            # preencher toda a janela e ajustar-se conforme a janela é redimensionada.
    texto.pack(expand=True, fill='both')


# Inicia a janela principal da aplicação usando Tkinter.
janela_principal = tk.Tk()

# Define o título da janela, que aparece na barra de título da janela.
janela_principal.title("Manipulação de DataFrame com Comandos")

# Cria um frame principal que atuará como o contêiner 
        # principal dentro da janela.
# Frames são usados para agrupar e organizar os 
        # componentes visuais da interface.
frame_principal = tk.Frame(janela_principal)

# Empacota o frame principal na janela. 'pady=10' adiciona um 
        # espaçamento vertical de 10 pixels para estética.
# 'fill='both'' e 'expand=True' fazem com que o frame expanda 
        # para preencher todo o espaço disponível na janela.
frame_principal.pack(pady=10, 
                     fill='both', 
                     expand=True)

# Cria um canvas dentro do frame principal. Um canvas é um espaço 
        # onde podem ser desenhados gráficos, textos e outros elementos.
# 'bg="white"' define a cor de fundo do canvas para branco.
canvas = tk.Canvas(frame_principal, 
                   bg="white")

# Empacota o canvas no lado esquerdo do frame principal e permite 
        # que ele expanda e preencha o espaço disponível.
canvas.pack(side="left", 
            fill="both", 
            expand=True)

# Adiciona uma barra de rolagem ao frame principal para permitir a 
        # navegação vertical através do canvas.
# 'orient="vertical"' especifica que a barra de rolagem é vertical.
# 'command=canvas.yview' conecta a barra de rolagem com a 
        # visão vertical do canvas.
scrollbar_chat = ttk.Scrollbar(frame_principal, 
                               orient="vertical", 
                               command=canvas.yview)

# Empacota a barra de rolagem no lado direito do frame principal e 
        # faz com que ela preencha o espaço verticalmente.
scrollbar_chat.pack(side="right", fill="y")

# Configura o canvas para atualizar a barra de rolagem baseada 
        # em seu conteúdo vertical.
canvas.configure(yscrollcommand=scrollbar_chat.set)

# Cria um frame dentro do canvas que será usado para 
        # conter os componentes de chat.
# Esse frame é onde os elementos do chat como mensagens de 
        # texto e entradas serão adicionados.
frame_chat = tk.Frame(canvas, bg="white")

# Cria uma janela dentro do canvas onde o frame 
        # de chat será mostrado.
# 'anchor="nw"' especifica que o frame será ancorado 
        # no canto superior esquerdo.
canvas.create_window((0, 0), window=frame_chat, anchor="nw")


# Função para atualizar a área scrollable do canvas quando o 
        # conteúdo dentro do frame_chat muda.
# Isso inclui alterações de tamanho devido à adição de novos 
        # elementos ou redimensionamento dos existentes.
def on_frame_configure(event):
    
    # 'scrollregion' define a região do canvas que deve ser scrollable, 
            # ou seja, que pode ser percorrida pela barra de rolagem.
    # 'canvas.bbox("all")' calcula o retângulo delimitador que contém 
            # todos os elementos dentro do canvas, garantindo que a barra de rolagem
            # abranja toda a área necessária para visualizar todos os 
            # componentes no canvas.
    canvas.configure(scrollregion=canvas.bbox("all"))

# Vincula um evento de configuração ao frame_chat, que é disparado sempre 
        # que há uma mudança de configuração como redimensionamento 
        # ou reposicionamento.
# "<Configure>" é um tipo de evento que ocorre quando um widget é 
        # configurado (por exemplo, tamanho alterado, movido, etc.).
# 'on_frame_configure' é chamado sempre que o evento ocorrer, 
        # mantendo a área de rolagem do canvas atualizada.
frame_chat.bind("<Configure>", on_frame_configure)

# Cria um frame na parte inferior da janela principal para 
        # conter a área de entrada de comandos.
# 'bg="#333"' define a cor de fundo do frame para um cinza escuro.
frame_inferior = tk.Frame(janela_principal, bg="#333")

# Empacota o frame na parte inferior da janela, estendendo-se horizontalmente.
# 'fill="x"' faz com que o frame preencha completamente o espaço horizontal.
# 'padx=10' e 'pady=5' adicionam um padding horizontal e 
        # vertical para espaçar o frame das bordas da janela.
frame_inferior.pack(side="bottom", 
                    fill="x", 
                    padx=10, 
                    pady=5)

# Cria uma área de entrada para que o usuário possa digitar comandos.
# 'width=60' define a largura da área de entrada, 
        # 'font=("Arial", 12)' define o tipo e tamanho da fonte,
        # e 'fg="#333"' define a cor do texto para um cinza escuro, 
        # garantindo boa legibilidade em fundo claro.
entry_comando = tk.Entry(frame_inferior, 
                         width=60, 
                         font=("Arial", 12), 
                         fg="#333")

# Empacota a área de entrada no lado esquerdo do 
        # frame inferior, com um padding horizontal de 5 pixels.
entry_comando.pack(side="left", padx=5)


# Cria um botão dentro do frame inferior, que permite ao 
        # usuário executar os comandos digitados na área de entrada.
btn_comando = tk.Button(frame_inferior, 
                        text="Executar",  # Define o texto do botão que será exibido.
                        command=processar_comando,  # Associa este botão à função 'processar_comando', que será chamada quando o botão for clicado.
                        font=("Arial", 12),  # Define a fonte e o tamanho do texto no botão.
                        bg="#4CAF50",  # Define a cor de fundo do botão como um verde vibrante.
                        fg="white")  # Define a cor do texto para branco, garantindo bom contraste e legibilidade.


# Empacota o botão no lado esquerdo do frame inferior, 
        # adicionando um padding horizontal de 5 pixels para 
        # espaçar o botão do campo de entrada.
btn_comando.pack(side="left", padx=5)

# Cria outro botão no frame inferior que permite ao usuário 
        # carregar um arquivo Excel.
# Este botão é útil para iniciar a carga de dados de um arquivo 
        # Excel para ser processado ou visualizado na aplicação.
btn_carregar = tk.Button(frame_inferior, 
                         text="Carregar Arquivo Excel",  # Texto no botão que indica sua função.
                         command=carregar_arquivo,  # Vincula este botão à função 'carregar_arquivo', que carrega dados de um arquivo Excel.
                         font=("Arial", 12),  # Usa a mesma fonte e tamanho de texto que o botão anterior para consistência visual.
                         bg="#2196F3",  # Define a cor de fundo do botão como um azul vibrante.
                         fg="white")  # Mantém o texto em branco para consistência e legibilidade.

# Empacota este botão ao lado do botão "Executar", também 
        # com um padding horizontal de 5 pixels.
btn_carregar.pack(side="left", padx=5)


# Cria um botão dentro do frame inferior, que quando clicado, 
        # mostrará uma janela com dicas úteis para o usuário.
btn_dicas = tk.Button(frame_inferior, 
                      text="Dicas",  # Texto que aparece no botão. "Dicas" indica que o botão fornecerá informações úteis quando pressionado.
                      command=mostrar_dicas,  # Associa este botão à função 'mostrar_dicas', que abrirá uma nova janela com dicas de comandos.
                      font=("Arial", 12),  # Define a fonte e o tamanho do texto no botão.
                      bg="#FF5722",  # A cor de fundo do botão é um laranja vibrante, ajudando a destacá-lo visualmente no layout.
                      fg="white")  # A cor do texto é branca para garantir contraste suficiente com o fundo laranja para boa legibilidade.

# Empacota o botão no frame inferior, alinhado à esquerda com os outros 
        # botões e com um espaçamento horizontal de 5 pixels.
btn_dicas.pack(side="left", padx=5)

# Cria um DataFrame vazio que será usado para manipulação de 
        # dados dentro da aplicação.
# 'pd.DataFrame()' é uma construção do pandas que cria 
        # um novo DataFrame vazio.
# Este DataFrame pode ser posteriormente preenchido com dados 
        # de um arquivo, entrada do usuário, ou qualquer outra fonte.
df = pd.DataFrame()

# Define a geometria da janela principal. "900x600" define a 
        # largura e altura da janela em pixels.
# Isso especifica o tamanho inicial da janela quando a 
        # aplicação é executada.
janela_principal.geometry("900x600")

# Inicia o loop principal da interface gráfica.
# 'mainloop()' é um método de Tkinter que precisa ser chamado 
        # para que a janela apareça na tela e comece a responder a eventos.
# Este loop mantém a janela aberta e gerencia todos os eventos 
        # de interface, como cliques de botão e entradas de teclado.
janela_principal.mainloop()