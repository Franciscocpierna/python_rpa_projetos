# Importação do módulo tkinter com um alias 'tk'
        # para construção da interface gráfica
import tkinter as tk

# Importação do módulo pandas com um alias 'pd' para 
        # manipulação de dados
import pandas as pd

# Definição da função carregar_dados_do_excel que carrega 
        # dados de um arquivo Excel e atualiza a tabela 
        # na interface gráfica
def carregar_dados_do_excel():
    
    # Declaração de variáveis globais que serão modificadas 
            # dentro desta função
    global df, colunas_ocultas, indice_salario
    
    # Carregamento dos dados do arquivo Excel 'tabela_exemplo.xlsx' 
            # para um DataFrame chamado 'df'
    df = pd.read_excel("tabela_exemplo.xlsx")
    
    # Criação de uma lista 'colunas' que contém os nomes 
            # das colunas do DataFrame 'df'
    colunas = list(df.columns)
    
    # Loop para remover a visualização do cabeçalho da tabela 
            # para evitar sobreposição ao atualizar a tabela
    for j in range(len(cabecalho)):
        
        # Remove a célula do cabeçalho na posição 'j' do grid de 
                # layout, ocultando-a visualmente
        cabecalho[j].grid_remove()
    
    # Loop duplo para remover as células da tabela da interface 
            # gráfica para evitar sobreposição ao atualizar os dados
    for i in range(len(tabela)):
        for j in range(len(tabela[i])):
            
            # Remove a célula na linha 'i' e coluna 'j' do grid 
                    # de layout, ocultando-a visualmente
            tabela[i][j].grid_remove()


    # Inicialização da variável 'coluna_atual' para rastrear a 
            # posição atual da coluna na interface gráfica
    coluna_atual = 0
    
    # Iteração sobre as colunas do DataFrame, utilizando a 
            # função enumerate para obter tanto o índice quanto o nome da coluna
    for j, coluna in enumerate(colunas):
        
        # Verificação se a coluna atual não está na lista 
                # de colunas ocultas
        if j not in colunas_ocultas:
            
            # Configuração do texto do cabeçalho na posição 
                    # 'coluna_atual' para o nome da coluna atual
            cabecalho[coluna_atual].config(text=coluna)
            
            # Posicionamento do cabeçalho no grid da janela, na linha 1 e 
                    # na coluna 'coluna_atual', e ajuste para que ele 
                    # preencha todo o espaço disponível (nsew: north-south-east-west)
            cabecalho[coluna_atual].grid(row=1, 
                                         column=coluna_atual, 
                                         sticky="nsew")
            
            # Configuração para que a coluna 'coluna_atual' do grid 
                    # expanda proporcionalmente ao redimensionar a 
                    # janela, garantindo que a coluna ajuste seu tamanho
            janela.grid_columnconfigure(coluna_atual, weight=1)
            
            # Verificação se o nome da coluna é "Salário" para 
                    # salvar seu índice para uso futuro
            if coluna == "Salário":

                # Salva o índice da coluna "Salário" na variável 
                        # global 'indice_salario'
                indice_salario = coluna_atual  
            
            # Incremento da variável 'coluna_atual' para passar 
                    # para a próxima coluna visível
            coluna_atual += 1


    # Este loop percorre cada linha do DataFrame 'df'. 'i' é 
            # o índice da linha atual.
    for i in range(len(df)):
        
        # A cada nova linha, 'coluna_atual' é zerada para começar a 
                # colocar células da esquerda para a direita na nova 
                # linha da interface gráfica.
        coluna_atual = 0
    
        # Este loop interno percorre cada coluna dentro da linha 
                # atual do DataFrame. 'j' é o índice da coluna.
        for j in range(len(df.columns)):
            
            # Verifica se a coluna atual está incluída na lista 
                    # 'colunas_ocultas'. Se não estiver, a célula 
                    # correspondente será criada e exibida.
            if j not in colunas_ocultas:
                
                # Configura o texto da célula na posição [i][coluna_atual] da 
                        # tabela da interface gráfica para o valor encontrado
                        # no DataFrame na posição [i, j]. 'iloc' é usado para acessar o 
                        # dado pelo índice numérico.
                tabela[i][coluna_atual].config(text=df.iloc[i, j])
    
                # Posiciona a célula na interface gráfica. 'row' define a 
                        # linha na interface gráfica, que é 'i+2' porque
                        # as primeiras duas linhas são usadas para título e 
                        # cabeçalho. 'column' é a coluna atual na interface.
                # 'sticky="nsew"' faz a célula expandir em todas as direções 
                        # (norte, sul, leste, oeste) para preencher o espaço disponível.
                tabela[i][coluna_atual].grid(row=i+2, 
                                             column=coluna_atual, 
                                             sticky="nsew")
    
                # Incrementa 'coluna_atual' para posicionar a próxima 
                        # célula na próxima coluna da mesma linha na interface.
                coluna_atual += 1
    
        # Após criar todas as células de uma linha, verifica-se se há 
                # necessidade de reposicionar o botão de agrupamento.
        # O botão '+' é posicionado na coluna do "Salário", 
                # usando 'indice_salario' para definir a coluna correta.
        # 'sticky="e"' faz o botão alinhar à direita dentro da célula da grid.
        btn_agrupar_colunas.grid(row=1, column=indice_salario, sticky="e")

      

# Definição da função 'expandir_colunas', que é chamada para 
        # mostrar todas as colunas que foram previamente ocultadas
def expandir_colunas():
    
    # Declaração de 'colunas_ocultas' como uma variável global para 
            # permitir a modificação do seu conteúdo globalmente no código
    global colunas_ocultas
    
    # Limpeza da lista 'colunas_ocultas', definindo-a como uma lista 
            # vazia, o que significa que nenhuma coluna estará oculta
    colunas_ocultas = []
    
    # Chamada da função 'carregar_dados_do_excel' para atualizar a 
            # visualização da tabela, mostrando todas as colunas
    carregar_dados_do_excel()
    
    # Configuração do botão 'btn_agrupar_colunas' para mostrar o texto "-", 
            # que indica que o botão agora serve para ocultar as colunas novamente.
    # A função 'command' é atualizada para 'agrupar_colunas', que é a 
            # função responsável por ocultar as colunas novamente 
            # quando o botão for pressionado.
    btn_agrupar_colunas.config(text="-", command=agrupar_colunas)


# Definição da função 'agrupar_colunas' que é usada para ocultar a 
        # maioria das colunas da tabela, deixando visíveis apenas as 
        # colunas extremas (a primeira e a última).
def agrupar_colunas():
    
    # Declaração de 'colunas_ocultas' como uma variável global para 
            # que as mudanças feitas aqui afetem o uso desta 
            # variável em todo o programa.
    global colunas_ocultas
    
    # Atribuição a 'colunas_ocultas' de uma lista de índices de 
            # colunas que serão ocultadas. A função 'range' é 
            # usada para criar uma lista de índices que começa em 1 e 
            # vai até o penúltimo índice de coluna de 'df.columns' 
            # (len(df.columns) - 1), efetivamente mantendo
            # visíveis apenas a primeira e a última coluna.
    colunas_ocultas = list(range(1, len(df.columns) - 1))
    
    # Chamada da função 'carregar_dados_do_excel' para atualizar a 
            # visualização da tabela na interface gráfica com 
            # as novas colunas ocultas.
    carregar_dados_do_excel()
    
    # Configuração do texto do botão 'btn_agrupar_colunas' para "+" 
            # indicando que o botão agora servirá para expandir as 
            # colunas agrupadas.
    # A função 'command' do botão é alterada para 'expandir_colunas', 
            # que é a função que reverterá o agrupamento quando o 
            # botão for pressionado.
    btn_agrupar_colunas.config(text="+", command=expandir_colunas)

    
# Inicialização da janela principal do programa 
        # usando a biblioteca Tkinter.
# 'tk.Tk()' é o comando que cria a janela 
        # raiz para a aplicação.
janela = tk.Tk()

# Configuração do título da janela principal.
# 'janela.title()' define o texto que aparecerá na 
        # barra de título da janela.
janela.title("Tabela Interativa com Agrupamento de Colunas")

# Carregamento dos dados do arquivo Excel para 
        # uso na aplicação.
# 'pd.read_excel("tabela_exemplo.xlsx")' lê os dados do 
        # arquivo especificado e os armazena em um 
        # DataFrame chamado 'df'.
# Este DataFrame será usado para manipulação e visualização 
        # de dados na interface gráfica.
df = pd.read_excel("tabela_exemplo.xlsx")

# Determinação do número de colunas no DataFrame.
# 'len(df.columns)' retorna o número de colunas 
        # no DataFrame 'df'.
# Esta informação é usada para ajudar a configurar a 
        # interface gráfica e controlar características 
        # como agrupamento de colunas.
colunas = len(df.columns)

# Determinação do número de linhas no DataFrame.
# 'len(df)' retorna o número de linhas no DataFrame 'df'.
# Essa contagem de linhas é crucial para construir a 
        # interface gráfica, pois define quantas linhas 
        # de dados serão mostradas.
linhas = len(df)

# Determinação do índice da coluna 'Salário', assumindo 
        # que é a última coluna do DataFrame.
# 'colunas - 1' calcula o índice do último item na lista de 
        # colunas, que é usado para localizar a coluna 'Salário'.
# Esse índice é importante para funcionalidades específicas, 
        # como posicionar um botão de agrupamento de colunas 
        # ao lado da coluna de salário.
indice_salario = colunas - 1


# Inicialização da lista 'colunas_ocultas' que será usada 
        # para controlar quais colunas devem ser ocultadas 
        # na interface gráfica.
# 'list(range(1, colunas - 1))' cria uma lista de índices, 
        # começando do segundo índice (1) até o penúltimo 
        # índice das colunas (colunas - 1),
# significando que todas as colunas entre a primeira e a 
        # última serão inicialmente ocultadas.
colunas_ocultas = list(range(1, colunas - 1))

# Criação e configuração do título da tabela na interface gráfica.
# 'tk.Label(janela, text="Tabela com Agrupamento de 
        # Colunas", font=("Arial", 16, "bold"))' cria um 
        # componente de texto (Label) que será adicionado à 
        # janela principal ('janela'). O texto do label é "Tabela 
        # com Agrupamento de Colunas", e a fonte é Arial, 
        # tamanho 16, negrito.
titulo = tk.Label(janela, 
                  text="Tabela com Agrupamento de Colunas", 
                  font=("Arial", 16, "bold"))

# Posicionamento do título na interface gráfica usando o método 'grid'.
# 'row=0' coloca o título na primeira linha do grid da interface.
# 'column=0' inicia o título na primeira coluna.
# 'columnspan=colunas' faz o título se estender por 
        # todas as colunas da interface, criando uma barra de 
        # título que abrange toda a largura.
# 'pady=10' adiciona um padding vertical de 10 pixels acima e 
        # abaixo do título para separá-lo visualmente dos 
        # outros elementos.
titulo.grid(row=0, 
            column=0, 
            columnspan=colunas, 
            pady=10)

# Inicialização da lista 'cabecalho' que armazenará os 
        # widgets para cada célula de cabeçalho da tabela.
# Cada célula de cabeçalho será um objeto Label que 
        # poderá ser configurado e posicionado na interface.
# Esta lista começa vazia e será preenchida à medida 
        # que as células de cabeçalho forem criadas 
        # no código subsequente.
cabecalho = []

# Este loop cria uma célula de cabeçalho para cada 
        # coluna disponível no DataFrame.
# 'for j in range(colunas)' itera de 0 até o 
        # número total de colunas menos um.
for j in range(colunas):
    
    # Criação de um componente Label, que será usado 
            # como uma célula de cabeçalho na tabela.
    # 'tk.Label(janela, ...)' cria um novo Label na janela principal.
    # 'text=""' inicializa o label sem texto, que 
            # será configurado posteriormente.
    # 'bg="lightblue"' define a cor de fundo do 
            # label para azul claro.
    # 'fg="black"' define a cor da fonte para preto.
    # 'width=12' e 'height=2' definem a largura e 
            # altura do label, respectivamente.
    # 'borderwidth=1' define a largura da borda 
            # do label para 1 pixel.
    # 'relief="solid"' define o estilo da borda como sólido.
    # 'font=("Arial", 12, "bold")' configura a fonte do 
            # texto do label para Arial, tamanho 12, negrito.
    celula_cabecalho = tk.Label(janela, 
                                text="", 
                                bg="lightblue", 
                                fg="black", 
                                width=12, 
                                height=2, 
                                borderwidth=1, 
                                relief="solid", 
                                font=("Arial", 12, "bold"))

    # Posicionamento da célula de cabeçalho na 
            # interface gráfica.
    # 'row=1' coloca a célula na segunda linha da 
            # grid (a primeira linha geralmente é para títulos ou controles).
    # 'column=j' coloca a célula na coluna 'j', correspondendo à 
            # sua posição na ordem das colunas.
    # 'sticky="nsew"' faz com que a célula expanda em todas 
            # as direções (norte, sul, leste, oeste) para 
            # preencher seu espaço no grid.
    celula_cabecalho.grid(row=1, 
                          column=j, 
                          sticky="nsew")

    # Adição da célula de cabeçalho à lista 'cabecalho'.
    # Esta lista armazena todas as células de cabeçalho 
            # criadas para que possam ser configuradas 
            # ou modificadas posteriormente.
    cabecalho.append(celula_cabecalho)


# Inicialização da lista 'tabela', que armazenará todas as 
        # linhas da tabela. Cada linha será uma lista 
        # de células (labels).
tabela = []

# O loop externo itera sobre cada linha do DataFrame. 
        # 'linhas' é o número total de linhas no DataFrame.
for i in range(linhas):
    
    # Inicialização da lista 'linha', que armazenará as 
            # células (labels) para a linha atual.
    linha = []

    # O loop interno itera sobre cada coluna do DataFrame 
            # para criar uma célula para cada coluna na linha atual.
    for j in range(colunas):
        
        # Criação de um componente Label, que será usado 
                # como uma célula na tabela.
        # 'tk.Label(janela, ...)' cria um novo Label na janela principal.
        # 'text=""' inicializa o label sem texto, que será 
                # configurado posteriormente com dados.
        # 'bg="white"' define a cor de fundo do label 
                # para branco.
        # 'fg="black"' define a cor da fonte para preto, 
                # garantindo contraste com o fundo branco.
        # 'width=12' e 'height=3' definem a largura e altura 
                # do label, respectivamente.
        # 'borderwidth=1' define a largura da borda do label para 1 pixel.
        # 'relief="solid"' define o estilo da borda como sólido.
        # 'font=("Arial", 10)' configura a fonte do texto 
                # do label para Arial, tamanho 10.
        celula = tk.Label(janela, 
                          text="", 
                          bg="white", 
                          fg="black", 
                          width=12, 
                          height=3, 
                          borderwidth=1, 
                          relief="solid", 
                          font=("Arial", 10))

        # Posicionamento da célula na interface gráfica.
        # 'row=i+2' coloca a célula na linha 'i+2' da 
                # grid. O '+2' é para ajustar o índice de linha 
                # começando após o cabeçalho e título.
        # 'column=j' coloca a célula na coluna 'j', correspondendo à 
                # sua posição na ordem das colunas.
        # 'sticky="nsew"' faz com que a célula expanda em 
                # todas as direções (norte, sul, leste, oeste) 
                # para preencher seu espaço no grid.
        celula.grid(row=i+2, column=j, sticky="nsew")

        # Adição da célula à lista 'linha', que armazena 
                # todas as células da linha atual.
        linha.append(celula)
    
    # Após construir todas as células para a linha atual, a 
            # lista 'linha' é adicionada à lista 'tabela'.
    # Isso constrói a estrutura da tabela linha por linha.
    tabela.append(linha)


# Criação de um botão na interface gráfica utilizando a 
        # biblioteca Tkinter.
# 'tk.Button(janela, ...)' cria um novo botão dentro da 
        # janela principal 'janela'.
# 'text="+"' define o texto exibido no botão como '+', 
        # que indica a funcionalidade de expandir as 
        # colunas agrupadas.
# 'command=expandir_colunas' associa este botão à função 
        # 'expandir_colunas', que será executada quando o 
        # botão for clicado.
# 'font=("Arial", 12)' configura a fonte do texto do 
        # botão para Arial, tamanho 12.
# 'width=3' define a largura do botão suficiente para 
        # acomodar o texto '+', garantindo que o botão 
        # não ocupe muito espaço.
btn_agrupar_colunas = tk.Button(janela, 
                                text="+", 
                                command=expandir_colunas, 
                                font=("Arial", 12), 
                                width=3)

# Posicionamento do botão na interface gráfica.
# 'row=1' coloca o botão na segunda linha da grid (a primeira 
        # linha é geralmente reservada para títulos ou cabeçalhos).
# 'column=indice_salario' coloca o botão na coluna especificada 
        # pelo 'indice_salario', que é o índice da coluna "Salário".
# Isso posiciona o botão diretamente ao lado ou na coluna onde o 
        # agrupamento de colunas será controlado, tornando 
        # sua funcionalidade intuitiva.
# 'sticky="e"' faz com que o botão alinhe à direita dentro da 
        # célula da grid. A opção "e" (leste) assegura que o 
        # botão fique à direita,
        # facilitando o acesso e a visualização.
btn_agrupar_colunas.grid(row=1, column=indice_salario, sticky="e")


# Configuração das colunas do layout grid da janela 
        # para que se ajustem automaticamente ao tamanho da janela.
# O loop itera sobre cada coluna da tabela.
for j in range(colunas):
    
    # 'janela.grid_columnconfigure(j, weight=1)' define o 
            # peso da coluna 'j' para 1.
    # O peso determina como o espaço adicional é distribuído 
            # entre as colunas quando a janela é redimensionada.
    # Um peso igual para todas as colunas significa que 
            # todas elas se expandirão proporcionalmente com o 
            # redimensionamento da janela.
    janela.grid_columnconfigure(j, weight=1)

# Configuração das linhas para ajustar automaticamente o 
        # tamanho conforme a tabela é redimensionada.
# O loop itera sobre cada linha que será usada para dados, começando 
        # de 'i+2' porque as primeiras duas linhas são usadas 
        # para título e cabeçalhos.
for i in range(linhas):
    
    # 'janela.grid_rowconfigure(i+2, weight=1)' configura o 
            # peso da linha 'i+2' para 1.
    # Isso permite que cada linha de dados expanda proporcionalmente 
            # quando a janela é redimensionada, assegurando que o 
            # conteúdo seja visível e adequadamente distribuído no 
            # espaço vertical disponível.
    janela.grid_rowconfigure(i+2, weight=1)

# Chamada da função 'carregar_dados_do_excel()' para carregar os 
        # dados do arquivo Excel na tabela da interface gráfica.
carregar_dados_do_excel()


# Iniciar o loop principal da interface
janela.mainloop()