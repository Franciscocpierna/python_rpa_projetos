# Importa o módulo tkinter e o renomeia como 'tk' para 
        # simplificar as chamadas a funções e classes do tkinter.
import tkinter as tk

# Importa o módulo 'ttk' do tkinter, que fornece widgets com 
        # uma aparência melhorada e mais funcionalidades 
        # que os widgets padrão do tkinter.
from tkinter import ttk

# Importa o módulo 'messagebox' do tkinter, que é usado para 
        # exibir mensagens de alerta, erro e informação ao usuário.
from tkinter import messagebox

# Importa o módulo 'pandas', uma biblioteca poderosa para 
        # manipulação e análise de dados. Renomeada como 'pd' 
        # para simplificar seu uso.
import pandas as pd

# Importa a função 'asksaveasfilename' do módulo 'filedialog' do 
        # tkinter, utilizada para abrir uma janela de diálogo 
        # que permite ao usuário selecionar o nome e local 
        # para salvar um arquivo.
from tkinter.filedialog import asksaveasfilename

# Define o caminho para o arquivo Excel que contém os 
        # dados que serão carregados.
arquivo_excel = 'notas_estudantes.xlsx'

# Utiliza a biblioteca pandas para carregar os dados do Excel 
        # especificado na variável 'arquivo_excel'.
# 'sheet_name='Dados'' especifica que a planilha (sheet) de 
        # interesse dentro do arquivo Excel se chama 'Dados'.
df_original = pd.read_excel(arquivo_excel, sheet_name='Dados')

# Cria uma cópia dos dados originais carregados para 'df_original'. 
        # Isso é feito para manter os dados originais intactos
        # enquanto manipulações, como filtros e alterações, são aplicadas 
        # sobre 'df', permitindo restaurar 'df' para o estado original se necessário.
df = df_original.copy()



# Função para atualizar as tabelas com os dados que podem ter 
        # sido alterados por filtros ou outras operações.
def atualizar_tabelas():
    
    # Limpa todos os itens existentes na tabela principal. Isso 
            # garante que dados antigos não sejam exibidos junto aos novos.
    tabela.delete(*tabela.get_children())
    
    # Realiza a mesma operação de limpeza para a primeira tabela congelada.
    tabela_congelada1.delete(*tabela_congelada1.get_children())
    
    # Realiza a operação de limpeza para a segunda tabela congelada.
    tabela_congelada2.delete(*tabela_congelada2.get_children())

    # Itera sobre cada linha do DataFrame filtrado para 
            # inserir os dados nas tabelas.
    for indice, linha in df.iterrows():
        
        # Cria uma tupla contendo o valor da coluna para a 
                # primeira tabela congelada.
        valores_congelada1 = (linha[colunas_congeladas1[0]],)
        
        # Cria uma tupla contendo o valor da coluna para a 
                # segunda tabela congelada.
        valores_congelada2 = (linha[colunas_congeladas2[0]],)
        
        # Cria uma tupla com os valores das colunas para a tabela principal.
        valores_tabela = tuple(linha[coluna] for coluna in colunas_tabela)
        
        # Insere os dados na primeira tabela congelada.
        tabela_congelada1.insert("", tk.END, values=valores_congelada1)
        
        # Insere os dados na segunda tabela congelada.
        tabela_congelada2.insert("", tk.END, values=valores_congelada2)
        
        # Insere os dados na tabela principal.
        tabela.insert("", tk.END, values=valores_tabela)

    # Atualiza a contagem de registros que estão sendo exibidos 
            # após a aplicação de filtros.
    # 'len(df)' conta o número de linhas no DataFrame filtrado e atualiza o 
            # texto de um label para mostrar essa contagem.
    label_contagem.config(text=f"Registros exibidos: {len(df)}")
    

# Função para aplicar filtros de texto aos dados exibidos nas tabelas.
def aplicar_filtro(*args):
    
    # A palavra-chave 'global' é usada para indicar que a variável 'df' a 
            # ser usada é a variável global definida fora desta função.
    global df
    
    # Cria uma nova cópia do DataFrame original para garantir que qualquer 
            # filtro aplicado seja feito sobre os dados originais.
    # Isso é importante porque permite que os filtros sejam removidos 
            # ou alterados sem perder os dados originais.
    df = df_original.copy()

    # Este loop passa por cada coluna das tabelas – principal e congeladas.
    # 'colunas_tabela' contém os nomes das colunas da tabela principal.
    # 'colunas_congeladas1' e 'colunas_congeladas2' contêm os 
            # nomes das colunas das tabelas congeladas.
    for coluna in colunas_tabela + colunas_congeladas1 + colunas_congeladas2:
        
        # Para cada coluna, acessa o campo de filtro correspondente e 
                # obtém o valor digitado pelo usuário.
        # 'filtros' é um dicionário onde cada chave é o nome de uma coluna e 
                # cada valor é um widget de entrada (Entry) que contém o filtro.
        valor_filtro = filtros[coluna].get()
        
        # Checa se algum valor foi realmente inserido no campo de filtro.
        # Se houver algum valor, o código dentro do if será executado.
        if valor_filtro:
            
            # Filtra o DataFrame 'df' para incluir apenas as linhas que 
                    # contêm o texto do filtro na coluna especificada.
            # 'astype(str)' garante que os dados sejam tratados como 
                    # strings, permitindo a aplicação do método 'contains'.
            # 'str.contains(valor_filtro, case=False, na=False, regex=False)' 
                    # verifica se a coluna contém o valor do filtro.
            # 'case=False' faz a busca ser insensível a maiúsculas ou minúsculas.
            # 'na=False' trata valores NaN como falsos, ou seja, eles 
                    # não serão incluídos se não atenderem ao filtro.
            # 'regex=False' especifica que o filtro deve ser tratado como 
                    # texto simples, não como uma expressão regular.
            df = df[df[coluna].astype(str).str.contains(valor_filtro, 
                                                        case=False, 
                                                        na=False, 
                                                        regex=False)]
    
    # Após aplicar os filtros em todas as colunas, a função 
            # 'atualizar_tabelas' é chamada.
    # Esta função é responsável por atualizar as visualizações nas 
            # tabelas com os dados que agora estão filtrados.
    atualizar_tabelas()


# Função para exportar os dados filtrados para diferentes formatos de 
        # arquivo, como Excel ou CSV.
def exportar_para_arquivo():
    
    # Solicita ao usuário que escolha um nome e local para salvar o 
            # arquivo, e define o tipo de arquivo padrão como .xlsx.
    # 'asksaveasfilename' é uma função do tkinter que abre uma 
            # janela de diálogo para salvar arquivos.
    # 'defaultextension=".xlsx"' define a extensão de arquivo 
            # padrão para .xlsx (Excel).
    # 'filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")]' 
            # especifica os tipos de arquivo que o usuário pode 
            # escolher para salvar os dados.
    tipo_arquivo = asksaveasfilename(defaultextension=".xlsx", 
                                     filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")])
    
    # Verifica se um nome de arquivo foi fornecido. Se o usuário 
            # cancelar a operação, 'tipo_arquivo' será uma string vazia.
    if tipo_arquivo:
        
        # Verifica se o arquivo escolhido deve ser salvo 
                # como um arquivo Excel.
        if tipo_arquivo.endswith(".xlsx"):
            
            # Exporta o DataFrame 'df' para um arquivo Excel. 'index=False' 
                    # não inclui o índice do DataFrame no arquivo.
            df.to_excel(tipo_arquivo, index=False)
            
        # Verifica se o arquivo escolhido deve ser salvo 
                # como um arquivo CSV.
        elif tipo_arquivo.endswith(".csv"):
            
            # Exporta o DataFrame 'df' para um arquivo CSV. 'index=False' 
            # não inclui o índice do DataFrame no arquivo.
            # 'encoding="utf-8-sig"' especifica que o arquivo deve ser salvo
            # com codificação UTF-8, garantindo que caracteres acentuados sejam
            # corretamente representados no arquivo.
            df.to_csv(tipo_arquivo, index=False, encoding="utf-8-sig")
        
        # Exibe uma mensagem de informação confirmando a exportação dos dados.
        # 'messagebox.showinfo' exibe uma caixa de diálogo de informação 
                # com a mensagem especificada.
        # "Exportação", f"Dados exportados com sucesso para {tipo_arquivo}" 
                # define o título e a mensagem da caixa de diálogo.
        messagebox.showinfo("Exportação", 
                            f"Dados exportados com sucesso para {tipo_arquivo}")


# Função para sincronizar a rolagem vertical entre três componentes: 
        # a tabela principal e duas tabelas com colunas congeladas.
def sincronizar_rolagem(*args):
    # O parâmetro '*args' coleta todos os argumentos fornecidos, que 
            # neste caso são típicos para eventos de rolagem. 
    # Estes argumentos indicam a nova posição da barra de rolagem vertical.

    # Ajusta a visão da rolagem vertical na tabela principal para 
            # corresponder à posição atual da barra de rolagem.
    # 'tabela.yview(*args)' aplica os argumentos do evento de rolagem à 
            # tabela principal, atualizando sua posição de rolagem vertical.
    tabela.yview(*args)

    # Sincroniza a primeira tabela congelada (tabela_congelada1) com a 
            # rolagem vertical da tabela principal.
    # 'tabela_congelada1.yview(*args)' aplica a mesma posição de rolagem 
            # da tabela principal à primeira tabela congelada.
    # Isso garante que, quando a tabela principal é rolada verticalmente, 
            # a primeira coluna congelada acompanha seu movimento.
    tabela_congelada1.yview(*args)

    # Sincroniza a segunda tabela congelada (tabela_congelada2) com a 
            # rolagem vertical da tabela principal.
    # 'tabela_congelada2.yview(*args)' assegura que a segunda coluna 
            # congelada também acompanhe a rolagem da tabela principal.
    # Esse passo é essencial para manter todas as partes da interface 
            # visualmente alinhadas durante a rolagem, 
            # permitindo uma visualização consistente dos dados que estão 
            # espacialmente relacionados nas diferentes partes da interface.
    tabela_congelada2.yview(*args)


# Variável global para controlar a sincronização de seleção
# A variável 'sincronizando' é utilizada para evitar 
        # que eventos de sincronização de seleção entre as 
        # tabelas gerem loops infinitos. Ela atua como um "bloqueio"
        # que impede que o código de sincronização seja executado 
        # várias vezes de forma recursiva.
global sincronizando


sincronizando = False  # Inicialmente, essa variável é definida como False,
                               # indicando que não estamos em processo de sincronização.

# Função para sincronizar a seleção entre as três tabelas
# Esta função é chamada sempre que o usuário clica em 
        # uma linha de qualquer tabela.
# Ela garante que, ao selecionar uma linha em uma tabela, a 
        # mesma linha seja selecionada
        # nas outras duas tabelas, mantendo a sincronização entre elas.
def sincronizar_selecao(event):
    
    # Declaração da variável global 'sincronizando' para permitir
    # que a função modifique seu valor globalmente.
    global sincronizando
    
    # Verifica se já estamos sincronizando as tabelas.
    # Isso impede que um loop recursivo de sincronização seja iniciado.
    # Se 'sincronizando' for True, significa que uma sincronização 
            # já está em andamento, então a função retorna 
            # imediatamente sem fazer nada.
    if sincronizando:
        return

    # Define 'sincronizando' como True para indicar que uma 
            # sincronização está em andamento.
    # Isso impede que outras tentativas de sincronização ocorram 
            # até que a atual seja concluída.
    sincronizando = True

    # Identifica qual tabela disparou o evento de seleção.
    # 'event.widget' se refere ao widget (neste caso, a 
            # tabela) que gerou o evento.
    tabela_selecionada = event.widget
    
    # Obtém a seleção atual da tabela que disparou o evento.
    # 'selection()' retorna uma tupla com os IDs das linhas selecionadas.
    selecionado = tabela_selecionada.selection()

    # Verifica se alguma linha foi selecionada.
    # Se a tupla 'selecionado' não estiver vazia, isso significa 
            # que há uma linha selecionada.
    if selecionado:
        
        # Obtém o índice da linha selecionada.
        # 'index(selecionado[0])' retorna a posição da linha 
                # selecionada dentro da tabela.
        indice = tabela_selecionada.index(selecionado[0])

        # Sincroniza a seleção para a primeira tabela congelada, se a 
                # tabela que disparou o evento não for a primeira tabela congelada.
        # Isso evita que a tabela tente sincronizar a seleção com ela mesma.
        if tabela_selecionada != tabela_congelada1:
            
            # Define a linha correspondente na primeira tabela congelada como selecionada.
            tabela_congelada1.selection_set(tabela_congelada1.get_children()[indice])
            
            # Garante que a linha selecionada esteja visível na 
                    # primeira tabela congelada.
            # 'see()' faz com que a linha selecionada seja rolada para 
                    # dentro da área visível da tabela.
            tabela_congelada1.see(tabela_congelada1.get_children()[indice])

        # Sincroniza a seleção para a segunda tabela congelada, se a tabela que 
                    # disparou o evento não for a segunda tabela congelada.
        # Da mesma forma, isso evita loops recursivos.
        if tabela_selecionada != tabela_congelada2:
            
            # Define a linha correspondente na segunda tabela 
                    # congelada como selecionada.
            tabela_congelada2.selection_set(tabela_congelada2.get_children()[indice])
            
            # Garante que a linha selecionada esteja visível na 
                    # segunda tabela congelada.
            tabela_congelada2.see(tabela_congelada2.get_children()[indice])

        # Sincroniza a seleção para a tabela principal, se a tabela que 
                # disparou o evento não for a tabela principal.
        if tabela_selecionada != tabela:
            
            # Define a linha correspondente na tabela principal como selecionada.
            tabela.selection_set(tabela.get_children()[indice])
            
            # Garante que a linha selecionada esteja visível na tabela principal.
            tabela.see(tabela.get_children()[indice])

    # Após sincronizar as seleções em todas as tabelas, 
            # define 'sincronizando' como False.
    # Isso indica que a sincronização foi concluída e 
            # outras sincronizações podem ocorrer.
    sincronizando = False
    

# Função para alternar o modo de exibição da janela 
            # entre tela cheia e modo janela.
def alternar_tela_cheia(janela):
    
    # A função 'attributes' do objeto 'janela' do tkinter é usada 
            # para modificar atributos da janela, incluindo o modo tela cheia.
    # '-fullscreen' é um atributo que, quando True, coloca a janela 
            # em tela cheia; quando False, a janela retorna ao modo janela.

    # 'not janela.attributes('-fullscreen')' pega o estado atual 
            # do modo tela cheia (True ou False) e inverte o valor.
    # Se a janela estiver em tela cheia (True), 'not' 
            # muda para False, e vice-versa.
    estado_tela_cheia = not janela.attributes('-fullscreen')

    # 'janela.attributes('-fullscreen', estado_tela_cheia)' 
            # define o novo estado do modo tela cheia.
    # Se 'estado_tela_cheia' for True, a janela muda para 
            # tela cheia; se for False, ela retorna ao modo janela normal.
    janela.attributes('-fullscreen', estado_tela_cheia)



# Função para criar a interface gráfica principal 
            # onde serão exibidos os dados.
def criar_interface():
    
    # Cria a janela principal da aplicação utilizando a 
            # biblioteca tkinter.
    janela = tk.Tk()
    
    # Define o título da janela, que aparecerá na barra de 
            # título da janela do sistema operacional.
    janela.title("Projeto de Notas dos Estudantes")
    
    # Inicialmente, coloca a janela em modo tela cheia. O atributo '-fullscreen' 
            # setado como True ativa o modo tela cheia.
    # janela.attributes('-fullscreen', False)

    janela.geometry("900x600")
    
    # Configura a janela para que, ao pressionar a tecla 'Escape', 
            # ela alterne entre tela cheia e modo janela normal.
    # 'bind' associa um evento (pressionar a tecla 'Escape') a 
            # uma função (lambda que chama 'alternar_tela_cheia').
    # A função 'lambda' é usada aqui para passar a 'janela' 
            # atual como argumento para 'alternar_tela_cheia'.
    janela.bind('<Escape>', lambda event: alternar_tela_cheia(janela))

    # Cria um rótulo (Label) que será usado para exibir o 
            # título do projeto dentro da janela.
    label_titulo = tk.Label(janela, 
                            
                            # 'text="Notas dos Estudantes"' define o 
                                    # texto que será mostrado no rótulo.
                            text="Notas dos Estudantes", 
                            
                            # 'font=("Arial", 20, "bold")' especifica a fonte 
                                    # do texto, usando Arial tamanho 20 e em negrito.
                            font=("Arial", 20, "bold"), 
                            
                            # 'bg="lightblue"' define a cor de fundo do 
                                    # rótulo como azul claro.
                            bg="lightblue", 
                            
                            # 'fg="white"' define a cor do texto como branco, 
                                    # proporcionando um bom contraste com o fundo azul claro.
                            fg="white")
    
    # Empacota o rótulo dentro da janela, o que o torna visível.
    # 'pack()' é um gerenciador de geometria que organiza os widgets 
            # em blocos antes de colocá-los na janela.
    # 'fill=tk.X' faz com que o rótulo preencha completamente o 
            # eixo horizontal da janela, estendendo-se de lado a lado.
    label_titulo.pack(fill=tk.X)


    # Cria um Frame que contém os filtros, usando um LabelFrame que permite 
            # um título e bordas para organização visual.
    # 'janela' é a janela principal onde este frame será colocado.
    frame_filtros = tk.LabelFrame(janela,  

                                  # O texto no título do frame para indicar que este contém os filtros.
                                  text="Filtros",  

                                  # Padding horizontal interno de 10 pixels para 
                                          # separar o conteúdo das bordas do frame.
                                  padx=10,  

                                  # Padding vertical interno de 5 pixels.
                                  pady=5,  

                                  # Cor de fundo do frame é cinza claro.
                                  bg="lightgray")  
    
    # Cria um canvas dentro do frame de filtros. O Canvas é usado para 
            # permitir a rolagem dos widgets contidos nele.
    # 'frame_filtros' é o contêiner para o canvas.
    canvas_filtros = tk.Canvas(frame_filtros,  

                               # A cor de fundo do canvas é definida como cinza 
                                       # claro para combinar com o frame.
                               bg="lightgray",

                               # Altura fixa do canvas de 50 pixels.
                               height=50)  
    
    # Cria uma barra de rolagem horizontal para o canvas.
    # 'frame_filtros' é o contêiner para a scrollbar.
    scrollbar_filtros = ttk.Scrollbar(frame_filtros,  

                                      # A orientação da scrollbar é horizontal.
                                      orient="horizontal",  

                                      # Conecta a scrollbar com a visão horizontal do canvas.
                                      command=canvas_filtros.xview)  
    
    # Cria um frame interior dentro do canvas para conter os widgets de filtro.
    # 'canvas_filtros' é o contêiner para este frame.
    frame_filtros_interior = tk.Frame(canvas_filtros,  

                                      # A cor de fundo do frame interior é cinza claro.
                                      bg="lightgray")  
    
    # Configura o evento de configuração para o frame interior 
            # para ajustar a região de rolagem do canvas.
    frame_filtros_interior.bind(

        # O evento que ocorre quando há mudanças na configuração/layout do frame.
        "<Configure>",  
        
        lambda e: canvas_filtros.configure(scrollregion=canvas_filtros.bbox("all"))
        # A função lambda é chamada com o evento 'e'.
        # 'canvas_filtros.configure(scrollregion=...)' ajusta a região de 
                # rolagem para incluir todo o conteúdo do canvas.
        # 'canvas_filtros.bbox("all")' calcula a caixa delimitadora de todo o 
                # conteúdo do canvas, que define a região de rolagem necessária.
        
    )


    # Cria uma "janela" dentro do canvas, que é um contêiner 
            # para o frame_filtros_interior.
    # Isso permite que os componentes dentro do frame_filtros_interior 
            # sejam roláveis dentro do canvas.
    canvas_filtros.create_window((0, 0), 
                                 window=frame_filtros_interior, 
                                 anchor="nw")
    
    # Configura o canvas para que a scrollbar horizontal possa 
            # controlar a visualização horizontal do conteúdo do canvas.
    canvas_filtros.configure(xscrollcommand=scrollbar_filtros.set)
    
    # Adiciona o canvas ao frame dos filtros, posicionando-o no 
            # topo e permitindo que ele expanda horizontalmente 
            # para preencher o espaço disponível.
    canvas_filtros.pack(side=tk.TOP, fill=tk.X, expand=True)
    
    # Adiciona a scrollbar horizontal abaixo do canvas, 
            # ocupando toda a largura horizontal disponível.
    scrollbar_filtros.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Empacota o frame dos filtros na janela principal, permitindo 
            # que ele se expanda horizontalmente e tenha um 
            # pequeno espaçamento vertical.
    frame_filtros.pack(fill=tk.X, pady=5)
    
    # Inicializa o dicionário global 'filtros' que armazenará 
            # os widgets de entrada para cada filtro.
    global filtros
    filtros = {}

    # Itera sobre cada coluna no DataFrame para criar 
            # interfaces de filtro para cada uma
    for coluna in df.columns:
        
        # Cria um rótulo para cada coluna no frame de filtros
        label_filtro = tk.Label(frame_filtros_interior, 
                                text=coluna, 
                                bg="lightgray")
        
        # Adiciona o rótulo ao layout do frame de filtros, 
                # alinhando-o à esquerda com espaçamento horizontal
        label_filtro.pack(side=tk.LEFT, padx=5)
    
        # Cria um campo de entrada para inserção de filtros 
                # associado a cada coluna
        entrada_filtro = tk.Entry(frame_filtros_interior, width=10)
        
        # Adiciona o campo de entrada ao lado do rótulo correspondente, 
                # alinhando-o à esquerda com espaçamento horizontal
        entrada_filtro.pack(side=tk.LEFT, padx=5)
    
        # Associa um evento que ativa a função de aplicar filtro sempre 
                # que uma tecla é liberada enquanto o campo está focado
        entrada_filtro.bind("<KeyRelease>", aplicar_filtro)
    
        # Armazena o campo de entrada no dicionário de 
                # filtros para acesso posterior
        filtros[coluna] = entrada_filtro


    # Cria um frame para hospedar o label de contagem de 
            # registros e o botão de exportação.
    # 'janela' é a janela principal onde este frame será colocado.
    frame_contagem_exportar = tk.Frame(janela, bg="white")  
    
    # Adiciona o frame ao layout da janela principal, preenchendo 
            # horizontalmente e com um espaçamento vertical.
    frame_contagem_exportar.pack(fill=tk.X, pady=5)
    
    # Declaração global para que a variável 'label_contagem' 
            # possa ser acessada fora desta função.
    global label_contagem
    
    # Cria um label dentro do frame para mostrar a 
            # contagem de registros exibidos.
    # 'frame_contagem_exportar' é o contêiner para este label.
    label_contagem = tk.Label(frame_contagem_exportar,  
                              text="",  # Texto inicial vazio; será atualizado dinamicamente.
                              bg="white",  # Cor de fundo do label.
                              fg="blue",  # Cor do texto do label.
                              font=("Arial", 12))  # Fonte do texto.
    
    # Adiciona o label ao layout do frame, alinhando-o à esquerda com um espaçamento horizontal.
    label_contagem.pack(side=tk.LEFT, padx=10)
    
    # Cria um botão dentro do frame para permitir a 
            # exportação dos dados filtrados.
    # 'frame_contagem_exportar' é o contêiner para este botão.
    botao_exportar = tk.Button(frame_contagem_exportar,  
                               text="Exportar para Arquivo",  # Texto exibido no botão.
                               command=exportar_para_arquivo,  # Função que será chamada quando o botão for clicado.
                               bg="green",  # Cor de fundo do botão.
                               fg="white")  # Cor do texto do botão.
    
    # Adiciona o botão ao layout do frame, alinhando-o à 
            # direita com um espaçamento horizontal.
    botao_exportar.pack(side=tk.RIGHT, padx=10)


    # Adicionando um botão para sair do programa
    # Cria um botão que permite ao usuário fechar a janela 
            # principal e sair da aplicação.
    # 'frame_contagem_exportar' é o contêiner onde este botão é colocado.
    botao_sair = tk.Button(frame_contagem_exportar, 
                           text="Sair",  # Texto exibido no botão.
                           command=janela.destroy,  # Ação realizada ao clicar no botão, neste caso, fecha a janela.
                           bg="red",  # Define a cor de fundo do botão como vermelho.
                           fg="white")  # Define a cor do texto no botão como branco.
    
    # Posiciona o botão à direita dentro do frame, com um 
            # espaçamento horizontal.
    botao_sair.pack(side=tk.RIGHT, padx=10)
    
    # Criando o Frame principal
    # Inicia a criação de um frame que serve como contêiner 
            # principal para a interface da janela.
    frame_principal = tk.Frame(janela,  # 'janela' é a janela principal da aplicação.
                               bg="white")  # A cor de fundo do frame é definida como branca.
    
    # Configura o frame para expandir e preencher tanto vertical 
            # quanto horizontalmente o espaço disponível.
    frame_principal.pack(fill=tk.BOTH, expand=True)
    
    # Criando o Frame para as primeiras colunas congeladas
    # Cria outro frame dentro do frame principal destinado a 
            # conter colunas congeladas da tabela.
    frame_congelado1 = tk.Frame(frame_principal,  # 'frame_principal' é o contêiner para este frame.
                                bg="white")  # A cor de fundo do frame é branca.
    
    # Empacota o frame à esquerda do frame principal, 
            # preenchendo todo o espaço vertical disponível.
    frame_congelado1.pack(side=tk.LEFT, fill=tk.Y)


    # Cria um segundo frame para conter a segunda 
            # coluna congelada da tabela.
    frame_congelado2 = tk.Frame(frame_principal)
    
    # Empacota o segundo frame congelado à esquerda do frame 
            # principal, preenchendo todo o espaço vertical disponível.
    frame_congelado2.pack(side=tk.LEFT, fill=tk.Y)
    
    # Cria um frame para conter o restante da tabela 
            # que não está congelada.
    frame_tabela = tk.Frame(frame_principal)
    
    # Empacota o frame da tabela à direita no frame principal, 
            # permitindo que ele expanda e preencha tanto vertical 
            # quanto horizontalmente o espaço disponível.
    frame_tabela.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    # Declaração global para as variáveis que 
            # armazenam as colunas congeladas.
    global colunas_congeladas1, colunas_congeladas2
    
    # Define quais são as primeiras colunas a serem congeladas na visualização da tabela.
    colunas_congeladas1 = [df.columns[0]]  # Armazena a primeira coluna do DataFrame.
    colunas_congeladas2 = [df.columns[1]]  # Armazena a segunda coluna do DataFrame.


    # Declara as variáveis globalmente para que possam ser 
            # acessadas fora desta função, especificamente 
            # para as tabelas congeladas.
    global tabela_congelada1, tabela_congelada2
    
    # Cria a primeira tabela congelada dentro do primeiro frame congelado.
    # Esta tabela mostrará apenas as informações da 
            # primeira coluna congelada.
    tabela_congelada1 = ttk.Treeview(frame_congelado1,  # Frame onde a tabela será inserida.
                                     columns=colunas_congeladas1,  # Colunas a serem exibidas, definidas anteriormente.
                                     show='headings',  # Mostra apenas os cabeçalhos das colunas, sem a coluna de índice padrão.
                                     height=15)  # Define a altura da tabela, limitando o número de linhas visíveis antes da rolagem.
    
    # Empacota a primeira tabela congelada à esquerda no seu 
            # frame, permitindo que ela se expanda verticalmente 
            # para preencher o espaço disponível.
    tabela_congelada1.pack(side=tk.LEFT, fill=tk.Y)
    
    # Cria a segunda tabela congelada no segundo frame 
            # congelado, semelhante à primeira.
    tabela_congelada2 = ttk.Treeview(frame_congelado2,  # Frame onde a tabela será inserida.
                                     columns=colunas_congeladas2,  # Colunas a serem exibidas, definidas anteriormente.
                                     show='headings',  # Configuração para mostrar apenas os cabeçalhos das colunas.
                                     height=15)  # Altura da tabela, que determina quantas linhas são visíveis.
    
    # Empacota a segunda tabela congelada à esquerda 
            # no seu frame, enchendo o espaço vertical.
    tabela_congelada2.pack(side=tk.LEFT, fill=tk.Y)


    # Itera sobre cada coluna listada para a primeira tabela congelada.
    for coluna in colunas_congeladas1:
        
        # Configura o cabeçalho da coluna, definindo o 
                # texto do cabeçalho como o nome da coluna.
        tabela_congelada1.heading(coluna, text=coluna)
        
        # Configura a largura e o alinhamento da coluna na tabela.
        tabela_congelada1.column(coluna, width=120, anchor='center')
    
    # Itera sobre cada coluna listada para a 
            # segunda tabela congelada.
    for coluna in colunas_congeladas2:
        
        # Configura o cabeçalho da coluna, definindo o texto do 
                # cabeçalho como o nome da coluna.
        tabela_congelada2.heading(coluna, text=coluna)
        
        # Configura a largura e o alinhamento da coluna na tabela.
        tabela_congelada2.column(coluna, width=120, anchor='center')


    # Scroll vertical sincronizado
    # Cria um scrollbar vertical para o frame da tabela principal 
            # para permitir rolagem vertical dos dados.
    scrollbar_vertical = ttk.Scrollbar(frame_tabela,  # O frame onde o scrollbar será inserido.
                                       orient="vertical",  # Define a orientação do scrollbar como vertical.
                                       command=sincronizar_rolagem)  # A função que será chamada para sincronizar a rolagem entre as tabelas.
    
    # Adiciona o scrollbar ao layout, posicionando-o à direita 
            # do frame da tabela e permitindo que ele se expanda verticalmente.
    scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Criando a Tabela principal com todas as colunas, exceto 
            # as duas primeiras
    # Declara as variáveis globais 'colunas_tabela' e 'tabela' 
            # que serão usadas para gerenciar as colunas e 
            # a própria tabela.
    global colunas_tabela, tabela
    
    # Inicializa 'colunas_tabela' com as colunas do DataFrame 
            # exceto as duas primeiras, para serem usadas na 
            # tabela principal.
    colunas_tabela = list(df.columns[2:])  # Exclui as duas primeiras colunas que são congeladas em outras tabelas.
    
    # Cria a tabela principal no frame da tabela, definindo as 
            # colunas e configurações como apenas cabeçalhos visíveis.
    tabela = ttk.Treeview(frame_tabela,  # O frame onde a tabela será inserida.
                          columns=colunas_tabela,  # Colunas que serão exibidas na tabela.
                          show='headings',  # Mostra apenas os cabeçalhos das colunas, sem a coluna de índice padrão.
                          height=15)  # Define a altura da tabela para mostrar 15 linhas de uma vez.
    
    # Adiciona a tabela ao layout, posicionando-a à esquerda 
            # dentro do frame da tabela e permitindo que ela expanda e 
            # preencha tanto vertical quanto horizontalmente o espaço disponível.
    tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


    # Itera sobre cada coluna na lista de colunas da tabela 
            # principal para configurar suas propriedades
    for coluna in colunas_tabela:

        # Define o texto do cabeçalho de cada coluna 
                # como o nome da coluna
        tabela.heading(coluna, text=coluna)  

        # Define a largura de cada coluna para 100 pixels e 
                # alinha o texto ao centro
        tabela.column(coluna, width=100, anchor='center')  
    
    # Configuração do Scroll
    # Vincula o comando de rolagem vertical da tabela 
            # principal ao scrollbar vertical
    tabela.configure(yscrollcommand=scrollbar_vertical.set)  

    # Vincula o comando de rolagem vertical da primeira tabela 
            # congelada ao mesmo scrollbar
    tabela_congelada1.configure(yscrollcommand=scrollbar_vertical.set)  

    # Vincula o comando de rolagem vertical da segunda 
            # tabela congelada ao mesmo scrollbar
    tabela_congelada2.configure(yscrollcommand=scrollbar_vertical.set)  


    # Cria um scrollbar horizontal para permitir a rolagem 
            # horizontal da tabela principal.
    scrollbar_horizontal = ttk.Scrollbar(janela,  # A janela onde o scrollbar será adicionado.
                                         orient="horizontal",  # A orientação do scrollbar é horizontal.
                                         command=tabela.xview)  # Associa o comando xview da tabela ao scrollbar.
    
    # Empacota o scrollbar horizontal e configura para 
            # preencher horizontalmente na parte inferior da janela.
    scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)
    
    # Associa o scrollbar horizontal à tabela principal 
            # para controlar a rolagem horizontal.
    tabela.configure(xscrollcommand=scrollbar_horizontal.set)

    # --------------------------------------------------------
    # Vincula o evento <ButtonRelease-1> (clique do mouse) à 
            # função sincronizar_selecao para cada tabela
    tabela.bind("<ButtonRelease-1>", sincronizar_selecao)
    tabela_congelada1.bind("<ButtonRelease-1>", sincronizar_selecao)
    tabela_congelada2.bind("<ButtonRelease-1>", sincronizar_selecao)

    # --------------------------------------------------------
    
    # Chama a função para atualizar e mostrar os dados nas 
            # tabelas baseando-se nos filtros aplicados.
    atualizar_tabelas()

    # Inicia o loop principal da interface gráfica, 
            # permitindo interações do usuário.
    janela.mainloop()


# Executando a Interface
criar_interface()