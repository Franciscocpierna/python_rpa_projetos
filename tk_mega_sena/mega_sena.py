# Importa o módulo tkinter e o renomeia como 'tk' para
        # simplificar o acesso às suas funções e classes.
# tkinter é uma biblioteca padrão do Python usada para
        # criar interfaces gráficas de usuário (GUIs).
import tkinter as tk

# Importa o módulo ttk de tkinter que contém temas e
        # estilos melhorados para os widgets da GUI,
# proporcionando uma aparência mais moderna e
        # funcionalidades adicionais.
from tkinter import ttk

# Importa a classe Image e ImageTk do módulo
        # PIL (Python Imaging Library, agora conhecido como Pillow),
# usado para abrir, manipular e salvar muitos formatos
        # diferentes de imagens. ImageTk é usado para criar
        # objetos de imagem compatíveis com tkinter.
from PIL import Image, ImageTk

# Importa o módulo pandas e o renomeia como 'pd'
        # para facilitar a manipulação de dados,
        # especialmente útil para leitura e escrita de
        # arquivos como Excel e para manipulação de grandes volumes de dados.
import pandas as pd

# Importa o módulo os, que fornece funções
        # para interagir com o sistema operacional,
        # usado aqui para manipular caminhos de
        # arquivos e verificar a existência de arquivos.
import os

# Importa o módulo random, que contém funções 
        # para gerar números aleatórios.
# É útil para operações como embaralhar ou 
        # selecionar itens aleatórios, como no 
        # caso de gerar números de loteria.
import random


# Define a função 'carregar_dados', que é responsável 
        # por carregar os dados de um arquivo Excel 
        # para a aplicação.
def carregar_dados():
    
    # Declara 'dados' e 'max_colunas' como variáveis globais. 
            # Isso permite que estas variáveis sejam acessadas e 
            # modificadas em outras partes do código.
    global dados, max_colunas
    
    # Carrega os dados da planilha 'Jogos' do arquivo 
            # Excel 'Jogos.xlsx'. 
    # A função 'read_excel' do pandas é utilizada aqui 
            # para ler o arquivo especificado e a aba 'Jogos'.
    dados = pd.read_excel('Jogos.xlsx', sheet_name='Jogos')
    
    # Calcula o número máximo de colunas não nulas em 
            # qualquer linha dos dados carregados.
    # 'notna()' cria uma máscara booleana onde 'True' 
            # significa que o dado é não nulo.
    # 'sum(axis=1)' soma os valores verdadeiros por 
            # linha, fornecendo o total de entradas não 
            # nulas por linha.
    # 'max()' extrai o maior valor dessa soma, indicando o 
            # máximo de colunas não nulas entre todas as linhas.
    max_colunas = dados.notna().sum(axis=1).max()
    
    # Chama a função 'criar_cabecalhos' passando 'max_colunas' 
            # como argumento.
    # Esta função é responsável por criar os cabeçalhos da 
            # tabela na interface gráfica baseando-se no 
            # número máximo de colunas calculado.
    criar_cabecalhos(max_colunas)
    
    # Itera sobre cada linha dos dados carregados. 'iterrows()' 
            # gera um iterador fornecendo o índice da linha e 
            # a linha em si (como uma série).
    for i, linha in dados.iterrows():
        
        # Converte a linha (uma série pandas) em uma lista e 
                # passa junto com o índice da linha e o número 
                # máximo de colunas para a função 'criar_linha_tabela'.
        # A função 'criar_linha_tabela' utiliza essas informações 
                # para adicionar os dados da linha específica à 
                # tabela na interface gráfica.
        criar_linha_tabela(list(linha), i, max_colunas)


# Define a função 'criar_cabecalhos', que é responsável por 
        # construir os cabeçalhos das colunas da tabela 
        # na interface gráfica.
# Recebe como argumento 'max_colunas', que é o número máximo de 
        # colunas de dados que podem existir, baseado na 
        # entrada de dados carregada.
def criar_cabecalhos(max_colunas):
    
    # Cria uma lista de cabeçalhos para as colunas. 
    # Utiliza uma compreensão de lista para gerar um 
            # cabeçalho 'Número X' para cada coluna, onde X é o 
            # número da coluna começando de 1 até 'max_colunas'.
    # Após os números, adiciona os cabeçalhos 'Acertos' e uma 
            # coluna vazia ('') ao final para operações 
            # futuras ou controle.
    cabecalhos = [f'Número {i+1}' for i in range(max_colunas)] + ['Acertos', '']
    
    # Itera sobre a lista de cabeçalhos com a função 'enumerate', 
            # que retorna tanto o índice da coluna (col) quanto o 
            # texto do cabeçalho (cabecalho).
    for col, cabecalho in enumerate(cabecalhos):
        
        # Cria um widget de rótulo (Label) usando a biblioteca tkinter. 
        # 'frame_rolavel' é o contêiner no qual o rótulo será colocado.
        # 'text=cabecalho' define o texto do rótulo com o 
                # nome do cabeçalho.
        # 'borderwidth=2' e 'relief="solid"' estilizam o 
                # rótulo com uma borda de largura 2 e um 
                # relevo sólido para destaque visual.
        # 'width=10' define a largura do rótulo para manter um 
                # tamanho consistente para todos os cabeçalhos.
        lbl = tk.Label(frame_rolavel, text=cabecalho, borderwidth=2, relief="solid", width=10)
        
        # Posiciona o rótulo na primeira linha do contêiner ('row=0') e 
                # na coluna correspondente ao seu índice.
        # 'sticky='nsew'' faz com que o rótulo se expanda e 
                # adira às bordas norte, sul, leste e oeste da 
                # célula da grade, ajudando a preencher 
                # completamente o espaço.
        lbl.grid(row=0, column=col, sticky='nsew')


# Define a função 'criar_linha_tabela', responsável por 
        # adicionar uma linha de dados à tabela na 
        # interface gráfica.
# Recebe 'valores' (lista dos valores para essa linha), 
        # 'linha' (índice da linha atual), e 
        # 'max_colunas' (número máximo de colunas da tabela).
def criar_linha_tabela(valores, linha, max_colunas):
    
    # Inicia um contador para rastrear o índice 
            # atual da coluna enquanto os dados são 
            # inseridos na linha.
    indice_coluna = 0  # Índice da coluna 
                             # para layout dinâmico
    
    # Itera sobre cada valor na lista de valores 
            # fornecida para a linha atual.
    for val in valores:
        
        # Verifica se o valor atual não é NA (não 
                # disponível/ausente). 
        # 'pd.notna(val)' retorna True se 'val' não for NA.
        if pd.notna(val):
            
            # Cria um rótulo (Label) para o valor, convertendo 
                    # o valor para inteiro e convertendo 
                    # novamente para string para exibição.
            # Define a borda do rótulo com largura 1 e 
                    # relevo sólido, e uma largura fixa 
                    # de 10 para uniformidade visual.
            lbl = tk.Label(frame_rolavel, text=str(int(val)), borderwidth=1, relief="solid", width=10)
            
            # Posiciona o rótulo na linha correspondente (linha+1, 
                    # pois a linha 0 é para cabeçalhos) e 
                    # na coluna atual 'indice_coluna'.
            # 'sticky='nsew'' faz com que o rótulo se expanda 
                    # para preencher a célula da grade em todas as direções.
            lbl.grid(row=linha+1, column=indice_coluna, sticky='nsew')
            
            # Armazena o rótulo no dicionário 'tabela_labels' 
                    # para fácil acesso posterior. O dicionário é 
                    # indexado por linha e coluna.
            tabela_labels[linha][indice_coluna] = lbl
            
            # Incrementa o índice da coluna para a próxima 
                    # iteração, movendo para a próxima coluna 
                    # na mesma linha.
            indice_coluna += 1


    # Inicia um loop para preencher quaisquer colunas restantes na 
            # linha atual que não tiveram valores atribuídos.
    # O loop começa no índice atual 'indice_coluna', onde o 
            # último valor foi colocado, e vai até 'max_colunas', 
            # o número máximo de colunas.
    for _ in range(indice_coluna, max_colunas):
        
        # Cria um rótulo (Label) vazio para as colunas que 
                # não possuem dados.
        # 'text=""' define o texto do rótulo como uma 
                # string vazia, indicando que não há dados para 
                # essa coluna na linha.
        # 'borderwidth=1' e 'relief="solid"' aplicam uma borda de 
                # espessura 1 com um estilo sólido para manter a 
                # consistência visual da tabela.
        # 'width=10' estabelece uma largura uniforme para todas as 
                # colunas, garantindo que a tabela mantenha um 
                # layout ordenado.
        lbl = tk.Label(frame_rolavel, text="", borderwidth=1, relief="solid", width=10)
        
        # Posiciona o rótulo criado na linha atual (linha+1 para 
                # ajustar o índice, já que a linha 0 é usada para 
                # cabeçalhos) e na coluna correspondente.
        # 'sticky='nsew'' é usado para garantir que o rótulo expanda e 
                # preencha completamente sua célula na grade, aderindo 
                # às bordas norte, sul, leste e oeste.
        lbl.grid(row=linha+1, column=indice_coluna, sticky='nsew')
        
        # Armazena o rótulo no dicionário 'tabela_labels', que mantém 
                # referências de todos os rótulos criados.
        # Isso é feito indexando o dicionário pela linha e coluna 
                # correntes, facilitando a referência futura para 
                # atualizações ou modificações.
        tabela_labels[linha][indice_coluna] = lbl
        
        # Incrementa o 'indice_coluna' para mover para a próxima 
                # coluna na mesma linha, preparando o índice para a 
                # próxima iteração do loop.
        # Isso assegura que cada nova coluna vazia seja preenchida 
                # sequencialmente até que todas as colunas 
                # até 'max_colunas' sejam atendidas.
        indice_coluna += 1


    # Adiciona um rótulo (Label) que servirá como campo de 
            # acertos na última coluna disponível da linha.
    # Este rótulo é usado para exibir o número de acertos que o 
            # usuário conseguiu em cada jogo.
    # 'text=""' inicializa o rótulo com um texto vazio, pois os 
            # acertos serão calculados e exibidos posteriormente.
    # 'borderwidth=1' e 'relief="solid"' aplicam uma borda de 
            # espessura 1 com estilo sólido, mantendo a 
            # uniformidade visual com os outros rótulos da tabela.
    # 'width=15' define uma largura maior para este rótulo em 
            # particular para acomodar a possibilidade de 
            # textos mais longos como "Acertou 15".
    lbl_acertos = tk.Label(frame_rolavel, text="", borderwidth=1, relief="solid", width=15)
    
    # Posiciona o rótulo de acertos na grade. Ele é colocado na 
            # linha especificada (linha+1 para compensar os 
            # cabeçalhos na linha 0)
    # e na coluna atual indicada por 'indice_coluna', que 
            # neste ponto refere-se à última coluna disponível 
            # após preencher todas as outras colunas com 
            # dados ou vazios.
    # 'sticky='nsew'' é utilizado para garantir que o rótulo 
            # expanda e preencha completamente sua célula 
            # na grade, fixando-se às bordas norte, sul, leste e oeste da célula.
    lbl_acertos.grid(row=linha+1, column=indice_coluna, sticky='nsew')
    
    # Armazena o rótulo de acertos no dicionário 'tabela_labels' 
            # para referência futura.
    # A chave é a combinação de linha e coluna 
            # atual ('linha', 'indice_coluna'), permitindo o 
            # acesso fácil ao rótulo para atualizações 
            # posteriores de texto,
            # como ao mostrar o número de acertos após a 
            # conferência dos números.
    tabela_labels[linha][indice_coluna] = lbl_acertos


    # Adiciona um botão denominado "Excluir" na interface gráfica, 
            # que permite ao usuário excluir a linha 
            # correspondente da tabela.
    # 'text="Excluir"' define o rótulo do botão, que é o 
            # texto exibido no próprio botão.
    # 'command=lambda r=linha: excluir_jogo(r)' define a 
            # ação que será executada quando o botão for pressionado.
    # A função 'lambda' é usada para passar o índice da 
            # linha atual como argumento para a função 'excluir_jogo'.
    # Isso permite que a função 'excluir_jogo' saiba qual 
            # linha deve ser removida quando o botão é clicado.
    btn_excluir = tk.Button(frame_rolavel, text="Excluir", command=lambda r=linha: excluir_jogo(r))
    
    # Posiciona o botão de "Excluir" na grade. 
    # 'row=linha+1' coloca o botão na linha seguinte ao índice da 
            # linha dos dados, ajustando-se pela presença dos 
            # cabeçalhos na linha 0.
    # 'column=indice_coluna+1' posiciona o botão na próxima coluna 
            # após o rótulo de acertos, garantindo que ele 
            # ocupe a coluna correta para ações.
    # 'sticky='nsew'' é usado para garantir que o botão expanda e 
            # preencha completamente sua célula na grade, 
            # fixando-se às bordas norte, sul, leste e oeste da célula.
    btn_excluir.grid(row=linha+1, column=indice_coluna+1, sticky='nsew')
    
    # Armazena o botão de "Excluir" no dicionário 'tabela_labels' 
            # para referência futura.
    # Isso é feito para manter uma organização e poder 
            # acessar facilmente o botão para eventuais 
            # modificações ou para fins de lógica de interface.
    # A chave para este botão no dicionário é definida pelo 
            # índice da linha e pela coluna (que é 
            # 'indice_coluna+1', a última coluna utilizada).
    tabela_labels[linha][indice_coluna+1] = btn_excluir


    
# Define a função 'excluir_jogo', que é chamada para remover um 
        # jogo especificado da tabela de dados e do arquivo Excel.
# 'linha' é o parâmetro que indica o índice da linha no 
        # DataFrame 'dados' que deve ser excluída.
def excluir_jogo(linha):
    
    # Declara que 'dados' é uma variável global, permitindo 
            # que esta função modifique o DataFrame 'dados' diretamente.
    global dados
    
    # Remove a linha especificada do DataFrame 'dados'.
    # 'dados.drop(linha)' exclui a linha do DataFrame 
            # onde 'linha' é o índice da linha a ser removida.
    # 'reset_index(drop=True)' é usado para reajustar os 
            # índices do DataFrame após a remoção da linha, 
            # para que não haja lacunas nos índices.
    # 'drop=True' indica que o antigo índice não deve ser 
            # adicionado como uma coluna no DataFrame resultante.
    dados = dados.drop(linha).reset_index(drop=True)
    
    # Salva o DataFrame 'dados' atualizado de volta no 
            # arquivo Excel 'Jogos.xlsx'.
    # 'to_excel' escreve o DataFrame no arquivo especificado.
    # 'sheet_name='Jogos'' especifica a aba do Excel 
            # onde os dados serão salvos.
    # 'index=False' garante que os índices do DataFrame 
            # não sejam escritos no arquivo, mantendo 
            # apenas os dados das colunas.
    dados.to_excel('Jogos.xlsx', sheet_name='Jogos', index=False)
    
    # Chama a função 'atualizar_tela' para atualizar a interface gráfica.
    # Isso é necessário para refletir as mudanças na 
            # tabela visual depois que uma linha é excluída, 
            # garantindo que a interface mostre o estado atual dos dados.
    atualizar_tela()


# Define a função 'atualizar_tela', que é chamada para recarregar e 
        # atualizar a interface gráfica após alterações nos 
        # dados, como adicionar ou excluir jogos.
def atualizar_tela():
    
    # Itera sobre todos os widgets (componentes como 
            # rótulos, botões, etc.) que são filhos do 'frame_rolavel'.
    # 'frame_rolavel' é um container na interface gráfica 
            # que contém os elementos visuais associados à 
            # exibição dos dados da tabela.
    for widget in frame_rolavel.winfo_children():
        
        # Destroi cada widget dentro do 'frame_rolavel'.
        # Isso é necessário para limpar a interface gráfica 
                # de qualquer representação anterior dos dados,
        # permitindo que uma nova representação atualizada 
                # seja exibida sem sobreposição ou erros de 
                # dados obsoletos.
        widget.destroy()
    
    # Chama a função 'carregar_dados' após a limpeza dos widgets antigos.
    # 'carregar_dados' é responsável por ler os dados do 
            # arquivo Excel ou de uma fonte de dados,
    # e então repopular o 'frame_rolavel' com os dados atualizados, 
            # recriando a visualização da tabela com as 
            # informações mais recentes.
    # Isso inclui recarregar os dados, recriar as linhas da 
            # tabela e configurar os cabeçalhos conforme necessário.
    carregar_dados()



# Define a função 'gerar_surpresinha', que é responsável por 
        # abrir uma nova janela na interface gráfica para 
        # permitir ao usuário gerar um conjunto de números 
        # aleatórios para a loteria, conhecido como "surpresinha".
def gerar_surpresinha():
    
    # Cria uma nova janela 'janela_surpresinha' como uma 
            # janela secundária (Toplevel) da 'janela_principal'.
    # 'Toplevel' é usado para criar janelas adicionais além 
            # da janela principal dentro de aplicações tkinter.
    janela_surpresinha = tk.Toplevel(janela_principal)
    
    # Define o título da janela secundária para "Gerar Surpresinha", 
            # dando ao usuário uma clara indicação do 
            # propósito desta janela.
    janela_surpresinha.title("Gerar Surpresinha")
    
    # Configura a cor de fundo da janela para branco. 
            # A escolha de uma cor de fundo clara, 
            # como o branco, oferece um design limpo e moderno.
    janela_surpresinha.configure(background='white')
    
    # Chama a função 'centralizar_janela' passando a 'janela_surpresinha' 
            # e as dimensões desejadas (800x400 pixels).
    # Esta função é responsável por centralizar a janela na 
            # tela do usuário, melhorando a experiência do 
            # usuário ao garantir que a janela apareça em 
            # uma posição conveniente.
    centralizar_janela(janela_surpresinha, 800, 400)

    # Cria um frame (contêiner) dentro da 'janela_surpresinha' 
            # para organizar outros widgets que serão 
            # adicionados posteriormente.
    # 'bg='white'' configura o fundo do frame para branco, 
            # mantendo a consistência com o design da janela.
    frame_surpresinha = tk.Frame(janela_surpresinha, bg='white')
    
    # Empacota o 'frame_surpresinha' na janela, utilizando o 
            # padding vertical de 20 pixels ('pady=20').
    # O uso de 'pack' com 'pady' ajuda a adicionar espaço 
            # vertical entre o frame e outros elementos na 
            # janela, evitando um design apertado.
    frame_surpresinha.pack(pady=20)

    # Define uma variável 'fonte' para ser usada nos widgets 
            # dentro da janela, especificando o tipo de 
            # letra "Arial" e tamanho 20.
    # A escolha de uma fonte e tamanho adequados melhora a 
            # legibilidade e a estética da interface gráfica.
    fonte = ("Arial", 20)

    # Configura a distribuição de espaço dentro da 
            # 'janela_surpresinha' usando o método 'grid'.
    # Este método divide a janela em uma grade onde os 
            # widgets podem ser posicionados.
    # A configuração 'weight=1' para as colunas e linhas 
            # especificadas assegura que elas se expandam 
            # proporcionalmente com a janela, melhorando a 
            # responsividade do layout.
    
    # Define que a coluna 0 da grade na janela deve se 
            # expandir, tomando espaço adicional quando a 
            # janela é redimensionada.
    janela_surpresinha.grid_columnconfigure(0, weight=1)

    # Define que a coluna 2 da grade também se expanda, 
            # garantindo que o conteúdo da coluna 1 (central) 
            # seja ladeado por espaços que se ajustam ao 
            # tamanho da janela.
    janela_surpresinha.grid_columnconfigure(2, weight=1)

    # Configura a linha 0 da grade para que se expanda, 
            # ajudando a manter o conteúdo verticalmente centralizado.
    janela_surpresinha.grid_rowconfigure(0, weight=1)

    # Configura a linha 2 da grade para expansão, 
            # similarmente à linha 0, contribuindo para a 
            # centralização vertical dos widgets.
    janela_surpresinha.grid_rowconfigure(2, weight=1)
    
    # Cria um rótulo (Label) dentro de 'frame_surpresinha', 
            # que pede ao usuário para escolher a quantidade de números.
    # 'text="Escolha a quantidade de números:"' 
            # define o texto do rótulo.
    # 'font=fonte' aplica a fonte definida 
            # anteriormente (Arial, tamanho 20), 
            # garantindo que o texto seja claro e legível.
    # 'bg='white'' define o fundo do rótulo como branco, 
            # consistente com o esquema de cores geral.
    # 'anchor='center'' centraliza o texto dentro do rótulo.
    # O método 'grid' posiciona o rótulo na primeira 
            # linha (row=0) e na coluna do meio (column=1) 
            # da grade dentro do frame.
    # 'pady=10' adiciona um espaço vertical de 10 pixels 
            # acima e abaixo do rótulo para evitar um 
            # layout apertado.
    # 'sticky='ew'' faz com que o rótulo se expanda 
            # horizontalmente para preencher a célula da 
            # grade, assegurando que o texto esteja centralizado.
    tk.Label(frame_surpresinha, text="Escolha a quantidade de números:", font=fonte, bg='white', anchor='center').grid(row=0, column=1, pady=10, sticky='ew')
    
    # Cria um widget de entrada (Entry) onde o usuário pode 
            # digitar a quantidade de números que deseja gerar.
    # 'width=5' define a largura do campo de entrada, 
            # suficiente para a maioria das entradas numéricas.
    # 'font=fonte' aplica a mesma fonte usada no rótulo, 
            # mantendo a consistência visual.
    # 'justify='center'' centraliza o texto digitado 
            # dentro do campo de entrada.
    # O método 'grid' posiciona o campo de entrada na 
            # linha abaixo do rótulo (row=1), na mesma 
            # coluna (column=1).
    # 'pady=5' adiciona um espaço vertical de 5 pixels 
            # acima e abaixo do campo de entrada.
    # 'sticky='ew'' estende o campo de entrada horizontalmente 
            # para preencher a célula da grade, garantindo 
            # alinhamento e apresentação adequados.
    entrada_quantidade = tk.Entry(frame_surpresinha, width=5, font=fonte, justify='center')
    entrada_quantidade.grid(row=1, column=1, pady=5, sticky='ew')

    
    # Define a função 'criar_surpresinha' que é chamada 
            # quando o usuário solicita a geração de um 
            # conjunto aleatório de números para a 
            # loteria, conhecido como "surpresinha".
    def criar_surpresinha():
        
        # Obtém o número digitado pelo usuário no campo de 
                # entrada 'entrada_quantidade' e converte para inteiro.
        # Isso determina quantos números aleatórios o 
                # usuário deseja gerar.
        num_numeros = int(entrada_quantidade.get())
    
        # Verifica se o número inserido está dentro do 
                # intervalo permitido de 6 a 20.
        # Isso garante que o usuário não solicite menos de 6 
                # ou mais de 20 números, o que pode ser um 
                # requisito baseado em regras de jogos de loteria.
        if 6 <= num_numeros <= 20:
            
            # Gera uma lista de números aleatórios.
            # 'random.sample' seleciona 'num_numeros' únicos 
                    # aleatoriamente do intervalo de 1 a 60, 
                    # garantindo que não haja repetições.
            # 'sorted()' organiza os números em ordem crescente 
                    # para melhor apresentação e análise.
            numeros_aleatorios = sorted(random.sample(range(1, 61), num_numeros))
    
            # Chama a função 'exibir_jogo_aleatorio' passando a 
                    # 'janela_surpresinha', a lista de 'numeros_aleatorios' 
                    # e o 'num_numeros'.
            # Esta função é responsável por exibir os números 
                    # gerados na interface, permitindo ao 
                    # usuário visualizar o resultado.
            exibir_jogo_aleatorio(janela_surpresinha, numeros_aleatorios, num_numeros)
            
        else:
            
            # Caso o número inserido esteja fora do intervalo 
                    # permitido, mostra uma mensagem de erro para o usuário.
            # Cria um rótulo dentro de 'frame_surpresinha' 
                    # informando ao usuário para inserir um 
                    # número dentro do intervalo válido.
            # 'text="Por favor, insira um número entre 6 e 20."' 
                    # informa claramente o problema e o 
                    # que o usuário precisa fazer.
            # 'font=fonte' e 'bg='white'' mantêm a consistência 
                    # estética com o resto da interface.
            # 'anchor='center'' centraliza o texto dentro do rótulo.
            # 'grid(row=2, column=1, pady=5, sticky='ew')' 
                    # posiciona o rótulo abaixo dos campos de 
                    # entrada e mensagem anterior, usando 'grid' 
                    # para manter o alinhamento.
            tk.Label(frame_surpresinha, 
                     text="Por favor, insira um número entre 6 e 20.", 
                     font=fonte, bg='white', anchor='center').grid(row=2, column=1, pady=5, sticky='ew')


    # Cria um botão na interface gráfica dentro do 'frame_surpresinha'.
    # Este botão é designado para que o usuário inicie o processo de 
            # geração de um conjunto aleatório de números da 
            # loteria, a "surpresinha".
    
    # 'text="Criar"' define o texto exibido no botão, que é "Criar". 
            # Este rótulo é direto e informa claramente a ação 
            # que será executada ao clicar no botão.
    # 'command=criar_surpresinha' associa este botão à 
            # função 'criar_surpresinha'. Quando o botão é 
            # clicado, essa função é chamada.
    # Essa função realiza a geração de números aleatórios 
            # dentro do intervalo especificado pelo usuário ou 
            # exibe uma mensagem de erro se o intervalo não 
            # for apropriado.
    # 'font=fonte' aplica a fonte previamente definida (Arial, tamanho 20) 
            # ao texto do botão, garantindo consistência 
            # visual e legibilidade.
    # 'bg='white'' define a cor de fundo do botão como branco, 
            # mantendo a estética uniforme com o restante da interface.
    botao_criar = tk.Button(frame_surpresinha, 
                            text="Criar", 
                            command=criar_surpresinha, 
                            font=fonte, bg='white')
    
    # Posiciona o botão 'botao_criar' na interface 
            # usando o método 'grid'.
    # 'row=3' coloca o botão na terceira linha do 
            # layout de grade dentro de 'frame_surpresinha'.
    # 'column=1' coloca o botão na segunda coluna (índice 1), 
            # que é centralizada devido às configurações de 
            # expansão definidas anteriormente para as colunas 0 e 2.
    # 'pady=10' adiciona um espaço vertical de 10 pixels acima e 
            # abaixo do botão, criando um layout mais espaçoso e 
            # visualmente agradável.
    # 'sticky='ew'' faz com que o botão se expanda para preencher 
            # todo o espaço horizontal da célula de grade em 
            # que está posicionado.
    # Isso garante que o botão seja claramente visível e 
            # facilmente acessível, ocupando toda a largura 
            # disponível na coluna.
    botao_criar.grid(row=3, column=1, pady=10, sticky='ew')



# Define a função 'exibir_jogo_aleatorio' que é responsável 
        # por mostrar os números aleatórios gerados na 
        # interface da janela "Surpresinha".
# A função recebe três parâmetros: 'janela_surpresinha', 
        # que é a janela onde os números serão exibidos, 
        # 'numeros_aleatorios', que é a lista de números gerados,
        # e 'num_numeros', que indica a quantidade de números 
        # que foram gerados.
def exibir_jogo_aleatorio(janela_surpresinha, numeros_aleatorios, num_numeros):
    
    # Inicia removendo todos os widgets existentes na 
            # 'janela_surpresinha' para preparar para uma 
            # nova exibição de resultados.
    # Este passo é importante para garantir que não haja 
            # elementos visuais antigos ou irrelevantes 
            # que possam confundir o usuário.
    for widget in janela_surpresinha.winfo_children():
        widget.destroy()  # Destroi cada widget (componentes como 
                                # labels, buttons, frames, etc.) 
                                # encontrado na janela.

    # Configura novamente o fundo da 'janela_surpresinha' 
            # para branco, garantindo um fundo 
            # limpo para a nova exibição de conteúdo.
    janela_surpresinha.configure(background='white')

    # Cria um novo 'frame' chamado 'frame_resultado' 
            # dentro da 'janela_surpresinha' para 
            # organizar o conteúdo que será exibido.
    # 'bg='white'' define o fundo do frame como branco, 
            # mantendo a consistência do design limpo e claro.
    frame_resultado = tk.Frame(janela_surpresinha, bg='white')

    # Empacota o 'frame_resultado' na 'janela_surpresinha' 
            # usando o método 'pack', que organiza o 
            # frame dentro da janela.
    # 'pady=20' adiciona um espaçamento vertical de 20 
            # pixels acima e abaixo do frame, contribuindo 
            # para um layout visualmente agradável.
    frame_resultado.pack(pady=20)

    # Define uma variável 'fonte' para ser usada nos widgets 
            # dentro do frame. Especifica a família da 
            # fonte e o tamanho.
    # '("Arial", 20)' escolhe a fonte Arial de tamanho 20, 
            # que é clara e legível, adequada para a 
            # exibição de números.
    fonte = ("Arial", 20)


    # Configura o comportamento de expansão para as 
            # colunas e linhas especificadas dentro 
            # da 'janela_surpresinha', assegurando que a 
            # interface se ajuste adequadamente ao redimensionar a janela.
    # Isso é importante para manter uma disposição visual coerente e 
            # esteticamente agradável independentemente das 
            # dimensões da janela.
    
    # Configura a coluna 0 da 'janela_surpresinha' para expandir, 
            # absorvendo espaço extra se disponível.
    janela_surpresinha.grid_columnconfigure(0, weight=1)

    # Configura a coluna 2 da 'janela_surpresinha' para expandir de 
            # maneira similar à coluna 0, mantendo um 
            # balanceamento simétrico.
    janela_surpresinha.grid_columnconfigure(2, weight=1)

    # Configura a linha 0 da 'janela_surpresinha' para expandir, o 
            # que ajuda a manter o conteúdo verticalmente centralizado.
    janela_surpresinha.grid_rowconfigure(0, weight=1)

    # Configura a linha 2 da 'janela_surpresinha' para expandir, 
            # complementando a configuração da linha 0 e mantendo a 
            # centralização vertical.
    janela_surpresinha.grid_rowconfigure(2, weight=1)
    
    # Posiciona o 'frame_resultado' dentro da 'janela_surpresinha' 
            # utilizando o método 'grid'.
    # O frame é colocado na linha 1 e coluna 1, que é a área 
            # central da janela, cercada por colunas e linhas 
            # configuradas para expandir.
    frame_resultado.grid(row=1, column=1)
    
    # Cria um rótulo (Label) dentro de 'frame_resultado' para 
            # anunciar o tipo de jogo e a quantidade de números gerados.
    # 'text=f"Jogo Aleatório ({num_numeros} números):"' forma uma 
            # string que informa ao usuário que os números 
            # apresentados são de um jogo aleatório e indica 
            # quantos números estão incluídos.
    # 'font=fonte' aplica a fonte Arial de tamanho 20 ao texto, 
            # garantindo legibilidade.
    # 'bg='white'' define a cor de fundo do rótulo como 
            # branco, mantendo o design limpo.
    # 'anchor='center'' centraliza o texto dentro do rótulo.
    # 'grid(row=0, column=1, pady=10, sticky='ew')' posiciona o 
            # rótulo na primeira linha do frame e na coluna 
            # central, com um padding vertical de 10 pixels para 
            # espaço extra, e expande o rótulo para preencher a 
            # largura da célula.
    tk.Label(frame_resultado, 
             text=f"Jogo Aleatório ({num_numeros} números):", 
             font=fonte, bg='white', anchor='center').grid(row=0, column=1, pady=10, sticky='ew')
    
    # Cria outro rótulo dentro de 'frame_resultado' para 
            # mostrar os números gerados.
    # 'text=" ".join(map(str, numeros_aleatorios))' converte 
            # cada número na lista 'numeros_aleatorios' para 
            # string e os une com espaços, formando uma única 
            # string de números separados por espaços.
    # 'font=fonte', 'bg='white'' e 'anchor='center'' aplicam as 
            # mesmas configurações de fonte, cor de fundo e 
            # ancoragem usadas anteriormente.
    # 'grid(row=1, column=1, pady=5, sticky='ew')' posiciona 
            # este rótulo na linha seguinte ao rótulo do título, 
            # também na coluna central, com um padding vertical 
            # de 5 pixels, e expande o rótulo para preencher a 
            # largura da célula.
    tk.Label(frame_resultado, 
             text=" ".join(map(str, numeros_aleatorios)), 
             font=fonte, bg='white', anchor='center').grid(row=1, column=1, pady=5, sticky='ew')


    # Define a função 'salvar_jogo' que será chamada quando o 
            # usuário clicar no botão "Salvar Jogo".
    def salvar_jogo():
        
        # Chama a função 'adicionar_jogo', passando a 
                # lista de 'numeros_aleatorios' como argumento.
        # Esta função é responsável por adicionar o conjunto de 
                # números gerados ao armazenamento permanente ou 
                # a uma lista de jogos salvos.
        adicionar_jogo(numeros_aleatorios)
        
        # Destroi a 'janela_surpresinha', fechando a janela após a 
                # ação de salvar, limpa a interface para o usuário.
        janela_surpresinha.destroy()
        
        # Chama a função 'atualizar_tela' para atualizar a 
                # tela principal do aplicativo, refletindo 
                # quaisquer mudanças feitas (como a adição de um novo jogo).
        atualizar_tela()
    
    # Cria um botão chamado 'botao_salvar' dentro do 'frame_resultado'.
    # 'text="Salvar Jogo"' define o texto do botão, que 
            # indica a ação de salvar o jogo atual.
    # 'command=salvar_jogo' associa este botão à 
            # função 'salvar_jogo', que é chamada quando o botão é clicado.
    # 'font=fonte' aplica a fonte predefinida (Arial, tamanho 20), 
            # mantendo a consistência visual.
    # 'bg='white'' define a cor de fundo do botão como 
            # branco, integrando-se ao esquema de cores 
            # geral da interface.
    # O botão é posicionado usando 'grid' no 'frame_resultado' 
            # na linha 2, coluna 1, com um espaçamento 
            # vertical ('pady') de 5 pixels e estendendo-se 
            # horizontalmente ('sticky='ew').
    botao_salvar = tk.Button(frame_resultado, 
                             text="Salvar Jogo", 
                             command=salvar_jogo, 
                             font=fonte, bg='white')
    botao_salvar.grid(row=2, column=1, pady=5, sticky='ew')
    
    # Cria um botão chamado 'botao_cancelar' com funcionalidades 
            # similares ao 'botao_salvar' mas para cancelar a operação.
    # 'text="Cancelar"' informa claramente a ação que o botão 
            # realizará, que é cancelar qualquer operação e fechar a janela.
    # 'command=janela_surpresinha.destroy' define a ação do 
            # botão para destruir e fechar a 'janela_surpresinha', 
            # cancelando a operação sem salvar.
    # 'font=fonte', 'bg='white'' mantêm a consistência visual.
    # Posicionado na linha 3, coluna 1 do 'frame_resultado', também 
            # com um espaçamento vertical de 5 pixels e 
            # expandindo-se horizontalmente.
    botao_cancelar = tk.Button(frame_resultado, 
                               text="Cancelar", 
                               command=janela_surpresinha.destroy, 
                               font=fonte, bg='white')
    botao_cancelar.grid(row=3, column=1, pady=5, sticky='ew')



# Define a função 'adicionar_jogo' que é chamada para inserir um 
        # novo jogo de números aleatórios na tabela de 
        # dados e no arquivo Excel.
# 'numeros_aleatorios' é o parâmetro que contém a lista de 
        # números gerados que devem ser adicionados.
def adicionar_jogo(numeros_aleatorios):
    
    # Declara que 'dados' e 'max_colunas' são variáveis globais, o 
            # que permite que esta função modifique essas 
            # variáveis fora do seu escopo local.
    global dados, max_colunas
    
    # Cria uma nova linha como uma série do pandas. 
            # A série é formada pelos números aleatórios 
            # seguidos por valores None para preencher até o 
            # número total de colunas em 'dados'.
    # Isso assegura que a nova linha tenha a mesma estrutura de 
            # colunas que as existentes no DataFrame 'dados'.
    # 'index=dados.columns' garante que a nova série use o mesmo 
            # índice de colunas que o DataFrame 'dados', para 
            # uma integração correta.
    nova_linha = pd.Series(numeros_aleatorios + [None]*(len(dados.columns) - len(numeros_aleatorios)), index=dados.columns)
    
    # Adiciona a nova linha ao DataFrame 'dados'. 'pd.concat' é 
            # usado para concatenar a nova linha ao DataFrame existente.
    # '[dados, nova_linha.to_frame().T]' converte a série 'nova_linha' 
            # em um DataFrame e transpõe (.T) para ajustar como 
            # uma linha ao invés de coluna.
    # 'ignore_index=True' é especificado para reindexar o 
            # DataFrame resultante, evitando conflitos de índice.
    dados = pd.concat([dados, nova_linha.to_frame().T], ignore_index=True)
    
    # Salva o DataFrame 'dados' atualizado de volta ao 
            # arquivo Excel 'Jogos.xlsx'.
    # 'sheet_name='Jogos'' especifica a aba do Excel 
            # onde os dados serão salvos.
    # 'index=False' garante que os índices do DataFrame não 
            # sejam escritos no arquivo, mantendo apenas os dados das colunas.
    dados.to_excel('Jogos.xlsx', sheet_name='Jogos', index=False)
    
    # Este bloco de código é responsável por adicionar visualmente o 
            # novo jogo de números à tabela na interface gráfica.

    # 'linha' é calculada para determinar a posição (índice) 
            # da última linha no DataFrame 'dados'.
    # 'dados.shape[0]' retorna o número total de linhas no 
            # DataFrame, e subtraindo 1 obtemos o índice 
            # da última linha adicionada.
    linha = dados.shape[0] - 1
    
    # Chama a função 'criar_linha_tabela' para adicionar 
            # uma nova linha na tabela da interface gráfica.
    # A lista 'numeros_aleatorios + [None]*(max_colunas - len(numeros_aleatorios))' 
            # prepara os dados para a nova linha:
    # 'numeros_aleatorios' são os números que foram gerados 
            # aleatoriamente e devem ser mostrados na tabela.
    # '[None]*(max_colunas - len(numeros_aleatorios))' adiciona 
            # células vazias suficientes para preencher o resto 
            # das colunas na tabela, assegurando que a 
            # linha tem a largura correta.
    # 'linha' é o índice da linha onde os dados devem ser inseridos.
    # 'max_colunas' é o número total de colunas que a 
            # tabela deve ter, garantindo que a nova linha 
            # se ajuste à estrutura existente da tabela.
    criar_linha_tabela(numeros_aleatorios + [None]*(max_colunas - len(numeros_aleatorios)), linha, max_colunas)
    

# Define a função 'conferir_numeros', que é responsável 
            # por verificar e exibir o número de 
            # acertos para cada linha de jogo.
def conferir_numeros():
    
    # Cria uma lista 'numeros_entrada' que contém os 
            # números digitados pelo usuário, convertidos 
            # para inteiros.
    # 'entradas' é uma lista de widgets de entrada (Entry) de 
            # onde os números são obtidos usando o método '.get()'.
    numeros_entrada = [int(entrada.get()) for entrada in entradas]

    # Inicia uma iteração sobre cada linha dos dados 
            # carregados, utilizando a função 'enumerate' 
            # que fornece dois valores: 
    # 'linha', que é o índice numérico da linha atual 
            # dentro do loop, e 'valores', que são os 
            # dados contidos nessa linha específica.
    for linha, valores in enumerate(dados.values):
        
        # Prepara uma lista 'valores_int' onde serão armazenados os 
                # valores da linha convertidos para inteiros.
        # Esta conversão é necessária porque os dados podem 
                # ser lidos como strings ou floats do arquivo 
                # Excel, e precisamos de inteiros para a comparação.
        # A conversão para float primeiro assegura que qualquer 
                # representação numérica possa ser convertida 
                # corretamente para inteiro.
        # A função 'pd.notna(val)' é utilizada para filtrar e 
                # converter apenas os valores que não 
                # são NA (não disponíveis ou células vazias).
        valores_int = [int(float(val)) for val in valores if not pd.isna(val)]
    
        # Calcula o número de acertos efetuando uma interseção 
                # entre os conjuntos de 'numeros_entrada' e 'valores_int'.
        # 'set(numeros_entrada)' converte a lista de números 
                # inseridos pelo usuário em um conjunto (set), 
                # que é uma estrutura de dados que permite 
                # operações de conjuntos.
        # 'set(valores_int)' converte a lista de números da 
                # linha atual em um conjunto.
        # 'intersection()' é um método que retorna um novo 
                # conjunto contendo apenas elementos que 
                # são comuns aos dois conjuntos.
        # 'len(...)' é usado para contar o número de elementos no 
                # conjunto resultante da interseção, que 
                # representa o total de acertos.
        acertos = len(set(numeros_entrada).intersection(valores_int))
        
        # Acessa o rótulo (Label) da tabela, específico para 
                # exibir os acertos na linha atual, usando o 
                # dicionário 'tabela_labels'.
        # Este dicionário foi previamente preenchido com 
                # referências a todos os rótulos de dados e 
                # acertos criados para cada linha da tabela.
        # '[linha][max_colunas]' especifica que estamos 
                # acessando o rótulo da coluna onde os acertos 
                # são exibidos para a linha atual.
        # '.config(text=f"Acertou {acertos}")' atualiza a 
                # propriedade de texto do rótulo para mostrar o 
                # número de acertos.
        # A mensagem formatada "Acertou {acertos}" é clara e 
                # direta, informando ao usuário quantos números 
                # ele acertou na linha correspondente.
        lbl_acertos = tabela_labels[linha][max_colunas]
        lbl_acertos.config(text=f"Acertou {acertos}")

        
        # Este bloco de código é responsável por reiniciar a 
                # apresentação visual dos rótulos de cada 
                # número na linha processada.
        # O objetivo é limpar qualquer destaque previamente 
                # aplicado antes de aplicar novos destaques 
                # baseados nos resultados atuais.
        # Ele itera sobre o número de colunas que contêm 
                # valores inteiros válidos, que foram 
                # filtrados e convertidos anteriormente.
        for coluna in range(len(valores_int)):
            
            # Acessa cada rótulo correspondente a um número na 
                    # linha atual, utilizando o índice 'linha' e 'coluna'.
            # O método '.config()' é utilizado para modificar a 
                    # configuração do rótulo, especificamente a 
                    # cor de fundo e a cor do texto.
            # 'bg="white"' define a cor de fundo do rótulo para 
                    # branco, e 'fg="black"' define a cor do 
                    # texto para preto.
            # Essas configurações asseguram que todos os rótulos 
                    # retornem a um estado neutro antes de 
                    # aplicar novos destaques.
            tabela_labels[linha][coluna].config(bg="white", fg="black")
        
        # Este bloco itera novamente sobre os valores da linha 
                # para aplicar um novo destaque aos números que 
                # foram corretamente acertados pelo usuário.
        # 'enumerate(valores_int)' permite iterar sobre a lista de 
                # valores inteiros, fornecendo tanto o 
                # índice (coluna) quanto o valor (val) de cada elemento.
        for coluna, val in enumerate(valores_int):
            
            # Verifica se o valor atual (val) está contido na 
                    # lista de números inseridos pelo 
                    # usuário ('numeros_entrada').
            # Esta comparação determina se o número foi acertado.
            if val in numeros_entrada:
                
                # Se o número foi acertado, o rótulo correspondente é 
                        # destacado visualmente.
                # 'bg="blue"' altera a cor de fundo do rótulo 
                        # para azul, e 'fg="white"' altera a cor 
                        # do texto para branco.
                # Essa combinação de cores destaca o número acertado, 
                        # tornando-o facilmente identificável para o usuário.
                tabela_labels[linha][coluna].config(bg="blue", fg="white")


        # Este bloco de código é responsável por verificar a 
                # quantidade de acertos e ajustar a apresentação 
                # visual do rótulo de acertos conforme o resultado.
        # A condição avalia se a variável 'acertos' é maior ou 
                # igual a 4, o que indica um número significativo 
                # de acertos no contexto do jogo.
        if acertos >= 4:
            
            # Se o número de acertos for 4 ou mais, o rótulo de 
                    # acertos é destacado com uma configuração 
                    # visual que indica um bom desempenho.
            # 'bg="green"' configura a cor de fundo do rótulo 
                    # para verde. A cor verde é comumente associada a 
                    # sucesso e é visualmente chamativa, facilitando a 
                    # identificação de um bom resultado.
            # 'fg="white"' configura a cor do texto para branco, 
                    # proporcionando um contraste alto com o fundo 
                    # verde, o que melhora a legibilidade e o impacto visual.
            lbl_acertos.config(bg="green", fg="white")
            
        else:
            
            # Se o número de acertos for menos que 4, o rótulo de 
                    # acertos mantém uma aparência neutra.
            # 'bg="white"' configura a cor de fundo do rótulo para 
                    # branco, uma cor neutra que indica um resultado 
                    # padrão ou abaixo do esperado.
            # 'fg="black"' configura a cor do texto para preto, 
                    # mantendo o contraste padrão e legibilidade 
                    # adequada sem destacar o rótulo.
            # Essa configuração assegura que apenas os resultados 
                    # positivamente notáveis sejam destacados visualmente.
            lbl_acertos.config(bg="white", fg="black")



# Define a função 'centralizar_janela', que é usada para 
        # posicionar a janela de forma centralizada na tela do usuário.
# Recebe três parâmetros: 'janela', que é a janela a 
        # ser centralizada, e 'largura' e 'altura', que 
        # definem as dimensões desejadas para essa janela.
def centralizar_janela(janela, largura, altura):
    
    # Obtém a largura total da tela do dispositivo 
            # onde a janela está sendo exibida.
    # 'winfo_screenwidth()' é um método que retorna a 
            # largura da tela em pixels.
    largura_tela = janela.winfo_screenwidth()
    
    # Obtém a altura total da tela do dispositivo.
    # 'winfo_screenheight()' é um método que retorna a 
            # altura da tela em pixels.
    altura_tela = janela.winfo_screenheight()
    
    # Calcula a posição no eixo X para a janela ser centralizada.
    # A posição no eixo X é determinada subtraindo 
            # metade da largura da janela de metade da 
            # largura total da tela.
    # Isso assegura que a janela esteja alinhada 
            # horizontalmente ao centro da tela.
    pos_x = (largura_tela // 2) - (largura // 2)
    
    # Calcula a posição no eixo Y para a janela ser centralizada.
    # Similarmente ao cálculo para o eixo X, subtrai-se 
            # metade da altura da janela de metade da 
            # altura total da tela.
    # Isso garante que a janela esteja alinhada 
            # verticalmente ao centro da tela.
    pos_y = (altura_tela // 2) - (altura // 2)
    
    # Configura a geometria da janela usando as 
            # dimensões e posições calculadas.
    # 'geometry' é um método que define as dimensões e a 
            # posição da janela em formato de string "{largura}x{altura}+{pos_x}+{pos_y}".
    # Isso posiciona a janela nas coordenadas calculadas, 
            # efetivamente centralizando-a na tela.
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")





# Cria a janela principal da aplicação utilizando a 
        # biblioteca tkinter. 
# 'tk.Tk()' inicializa a janela principal para a 
        # aplicação GUI.
janela_principal = tk.Tk()

# Define o título da janela principal, que aparecerá na 
        # barra de título da janela.
# 'title("Conferidor de Jogos da Mega Sena")' estabelece um 
        # título que descreve o propósito da janela, neste 
        # caso, como um aplicativo para conferir jogos da Mega Sena.
janela_principal.title("Conferidor de Jogos da Mega Sena")

# Configura as dimensões iniciais da janela principal.
# 'geometry("1200x700")' define a largura e altura da 
        # janela em pixels, especificando que a janela terá 
        # 1200 pixels de largura e 700 pixels de altura.
janela_principal.geometry("1200x700")

# Define se a janela pode ser redimensionada ou não.
# 'resizable(False, False)' desabilita tanto o redimensionamento 
        # horizontal quanto o vertical, fixando o 
        # tamanho da janela.
janela_principal.resizable(False, False)

# Chama a função 'centralizar_janela' para centralizar a 
        # janela principal na tela do usuário.
# 'centralizar_janela(janela_principal, 1200, 550)' passa a 
        # janela principal e as dimensões desejadas 
        # para centralização.
# Isso assegura que a janela apareça centralizada na tela, 
        # fornecendo uma melhor apresentação 
        # visual e acessibilidade.
centralizar_janela(janela_principal, 1200, 550)

# Inicia o processo para adicionar uma imagem de 
        # cabeçalho na janela principal.
# 'image_path' contém o caminho para o arquivo de imagem 
        # que será usado como cabeçalho, neste caso, uma 
        # imagem representando a Mega Sena.
image_path = "mega-sena.jpg"

# Verifica se o arquivo de imagem especificado por 
        # 'image_path' existe no sistema de arquivos.
# 'os.path.exists(image_path)' retorna True se o 
        # arquivo existir e False caso contrário.
if os.path.exists(image_path):
    
    # Abre a imagem localizada em 'image_path' utilizando a 
            # biblioteca PIL (Python Imaging Library).
    # 'Image.open(image_path)' lê o arquivo de imagem e 
            # retorna um objeto de imagem que pode 
            # ser manipulado.
    img = Image.open(image_path)
    
    # Redimensiona a imagem para se ajustar à largura e 
            # altura desejadas.
    # 'resize((1200, 200), Image.LANCZOS)' redimensiona a 
            # imagem para 1200 pixels de largura e 
            # 200 pixels de altura,
    # utilizando o filtro LANCZOS, que é um método de 
            # alta qualidade para redimensionamento de imagem.
    img = img.resize((1200, 200), Image.LANCZOS)
    
    # Converte a imagem redimensionada em um formato que 
            # pode ser utilizado com tkinter.
    # 'ImageTk.PhotoImage(img)' cria um objeto PhotoImage 
            # que pode ser usado como uma imagem em widgets tkinter.
    photo = ImageTk.PhotoImage(img)

    # Cria um rótulo (Label) na janela principal e 
            # configura a imagem do rótulo para ser a 
            # imagem redimensionada.
    # 'tk.Label(janela_principal, image=photo)' cria o 
            # rótulo e associa a imagem 'photo' a ele.
    label_imagem = tk.Label(janela_principal, image=photo)
    
    # Mantém uma referência à imagem associada ao rótulo 
            # para evitar que o garbage collector do Python a remova.
    # 'label_imagem.image = photo' assegura que a imagem 
            # permaneça na memória enquanto o rótulo estiver em uso.
    label_imagem.image = photo
    
    # Adiciona o rótulo à janela principal com um 
            # padding vertical (pady) de 10 pixels 
            # para espaçamento.
    # 'pack(pady=10)' organiza o rótulo na janela e 
            # adiciona espaço acima e abaixo do rótulo.
    label_imagem.pack(pady=10)
    
else:
    
    # Se o arquivo de imagem não for encontrado, 
            # imprime uma mensagem de erro no console.
    # 'print(f"Erro: o arquivo {image_path} não foi 
            # encontrado.")' fornece um feedback útil 
            # para o usuário ou desenvolvedor,
    # indicando que a imagem não pôde ser carregada 
            # porque o arquivo não foi localizado no 
            # caminho especificado.
    print(f"Erro: o arquivo {image_path} não foi encontrado.")


# Cria um rótulo (Label) para o título da janela principal.
# 'tk.Label' é usado para criar um widget de texto. 
        # 'janela_principal' especifica o container (a 
        # janela principal) onde o rótulo será adicionado.
# 'text="Conferidor de Jogos da Mega Sena"' define o texto 
        # que será exibido no rótulo, indicando o 
        # propósito da janela.
# 'font=("Arial", 16)' configura a fonte do texto 
        # para Arial com tamanho 16, garantindo 
        # legibilidade e uma aparência profissional.
titulo = tk.Label(janela_principal, 
                  text="Conferidor de Jogos da Mega Sena", 
                  font=("Arial", 16))

# Adiciona o rótulo do título à janela principal com um 
        # padding vertical (pady) de 10 pixels para espaçamento.
# 'pack(pady=10)' organiza o rótulo na janela e adiciona 
        # espaço acima e abaixo do rótulo para evitar que 
        # fique muito próximo de outros elementos.
titulo.pack(pady=10)

# Cria um frame (quadro) dentro da janela principal para 
        # organizar as entradas de números.
# 'tk.Frame' é usado para criar um container genérico 
        # dentro da janela. 'janela_principal' 
        # especifica onde o frame será adicionado.
frame_entradas = tk.Frame(janela_principal)

# Adiciona o frame de entradas à janela principal com um 
        # padding vertical (pady) de 10 pixels 
        # para espaçamento.
# 'pack(pady=10)' organiza o frame na janela e adiciona 
        # espaço acima e abaixo do frame, garantindo um 
        # layout espaçado e organizado.
frame_entradas.pack(pady=10)

# Inicializa duas listas vazias: 'entradas' e 'labels'.
# 'entradas' será usada para armazenar os widgets de 
        # entrada (Entry) onde o usuário digitará os números.
# 'labels' será usada para armazenar os rótulos (Label) 
        # que descrevem cada campo de entrada.
entradas = []
labels = []

# Cria seis pares de rótulos (Label) e campos de 
        # entrada (Entry) para a inserção de números 
        # da loteria pelo usuário.
# Utiliza um loop para iterar de 0 a 5, criando um 
        # par de rótulo e campo de entrada para cada iteração.

for i in range(6):
    
    # Cria um rótulo (Label) para o campo de 
            # entrada correspondente.
    # 'frame_entradas' é o container onde o 
            # rótulo será adicionado.
    # 'text=f"Número {i+1}:"' define o texto do 
            # rótulo, que é "Número 1:", "Número 2:", ..., até "Número 6:".
    label = tk.Label(frame_entradas, text=f"Número {i+1}:")
    
    # Posiciona o rótulo na grade dentro do 'frame_entradas'.
    # 'row=0' coloca o rótulo na primeira linha do frame.
    # 'column=i*2' define a coluna onde o rótulo 
            # será colocado, espaçando as colunas dos 
            # rótulos e entradas.
    # 'padx=5' adiciona um padding horizontal de 5 
            # pixels em ambos os lados do rótulo para 
            # evitar que fique muito próximo de outros elementos.
    label.grid(row=0, column=i*2, padx=5)
    
    # Adiciona o rótulo à lista 'labels' para referência futura.
    labels.append(label)
    
    # Cria um campo de entrada (Entry) para a 
            # inserção do número correspondente.
    # 'frame_entradas' é o container onde o campo de 
            # entrada será adicionado.
    # 'width=5' define a largura do campo de entrada, 
            # suficiente para que o usuário digite um número.
    entrada = tk.Entry(frame_entradas, width=5)
    
    # Posiciona o campo de entrada na grade dentro do 'frame_entradas'.
    # 'row=0' coloca o campo de entrada na primeira linha do frame.
    # 'column=i*2+1' define a coluna onde o campo de 
            # entrada será colocado, que é uma posição à 
            # direita do rótulo correspondente.
    # 'padx=5' adiciona um padding horizontal de 5 pixels em 
            # ambos os lados do campo de entrada para evitar 
            # que fique muito próximo de outros elementos.
    entrada.grid(row=0, column=i*2+1, padx=5)
    
    # Adiciona o campo de entrada à lista 'entradas' 
            # para referência futura.
    entradas.append(entrada)


# Cria um botão denominado "Conferir" dentro do 'frame_entradas'.
# 'text="Conferir"' define o texto exibido no botão, 
        # indicando sua função para o usuário.
# 'command=conferir_numeros' associa o botão à 
        # função 'conferir_numeros', que será chamada 
        # quando o botão for clicado.
botao_conferir = tk.Button(frame_entradas, 
                           text="Conferir", 
                           command=conferir_numeros)

# Posiciona o botão "Conferir" na grade dentro do 'frame_entradas'.
# 'row=0' coloca o botão na primeira linha do frame.
# 'column=12' posiciona o botão na 13ª coluna (índice 12) 
        # da grade, ao lado dos campos de entrada.
# 'padx=5' adiciona um padding horizontal de 5 pixels em 
        # ambos os lados do botão, para evitar que fique 
        # muito próximo de outros elementos.
botao_conferir.grid(row=0, column=12, padx=5)

# Cria um botão denominado "Surpresinha" dentro do 'frame_entradas'.
# 'text="Surpresinha"' define o texto exibido no botão, 
        # indicando sua função de gerar números aleatórios.
# 'command=gerar_surpresinha' associa o botão à função 
        # 'gerar_surpresinha', que será chamada quando o 
        # botão for clicado.
botao_surpresinha = tk.Button(frame_entradas, 
                              text="Surpresinha", 
                              command=gerar_surpresinha)

# Posiciona o botão "Surpresinha" na grade dentro do 'frame_entradas'.
# 'row=0' coloca o botão na primeira linha do frame.
# 'column=13' posiciona o botão na 14ª coluna (índice 13) 
        # da grade, ao lado do botão "Conferir".
# 'padx=5' adiciona um padding horizontal de 5 pixels em 
        # ambos os lados do botão, para evitar que fique 
        # muito próximo de outros elementos.
botao_surpresinha.grid(row=0, column=13, padx=5)


# Cria um frame (quadro) para a tabela personalizada que 
        # irá conter os dados e a barra de rolagem.
# 'tk.Frame' é usado para criar um container genérico 
        # dentro da janela. 'janela_principal' especifica 
        # onde o frame será adicionado.
frame_tabela = tk.Frame(janela_principal)

# Adiciona o frame da tabela à janela principal.
# 'pack(pady=10, fill=tk.BOTH, expand=True)' organiza o 
        # frame na janela, adicionando espaço acima e abaixo do frame.
# 'fill=tk.BOTH' permite que o frame se expanda para 
        # preencher tanto a largura quanto a altura disponíveis na janela.
# 'expand=True' permite que o frame expanda para preencher 
        # qualquer espaço extra na janela, garantindo que a 
        # tabela ocupe todo o espaço disponível.
frame_tabela.pack(pady=10, fill=tk.BOTH, expand=True)


# Cria um widget canvas dentro do 'frame_tabela'. 
# O canvas é uma área de desenho que pode ser usada para 
        # criar gráficos, desenhar formas, exibir imagens ou 
        # criar interfaces mais complexas.
# 'frame_tabela' é o container onde o canvas será adicionado.
canvas = tk.Canvas(frame_tabela)

# Cria uma barra de rolagem horizontal (scrollbar_x) dentro do 'frame_tabela'.
# 'orient="horizontal"' define a orientação da barra 
        # de rolagem como horizontal.
# 'command=canvas.xview' associa a barra de rolagem ao 
        # método 'xview' do canvas, permitindo que a 
        # barra de rolagem controle a visualização 
        # horizontal do canvas.
scrollbar_x = tk.Scrollbar(frame_tabela, 
                           orient="horizontal", 
                           command=canvas.xview)

# Cria uma barra de rolagem vertical (scrollbar_y) dentro do 'frame_tabela'.
# 'orient="vertical"' define a orientação da 
        # barra de rolagem como vertical.
# 'command=canvas.yview' associa a barra de rolagem 
        # ao método 'yview' do canvas, permitindo que a 
        # barra de rolagem controle a visualização 
        # vertical do canvas.
scrollbar_y = tk.Scrollbar(frame_tabela, 
                           orient="vertical", 
                           command=canvas.yview)

# Cria um frame (quadro) dentro do canvas, que 
        # será usado como uma área rolável.
# O frame rolável permitirá que os widgets dentro 
        # dele sejam rolados usando as barras de 
        # rolagem do canvas.
frame_rolavel = tk.Frame(canvas)


# Liga um evento de configuração ao frame rolável 
        # para ajustar a região de rolagem do canvas.
# 'frame_rolavel.bind' é usado para ligar um 
        # evento ao 'frame_rolavel'.
# O evento "<Configure>" é disparado sempre que o 
        # frame rolável é redimensionado ou 
        # configurado de alguma maneira.

frame_rolavel.bind(
    "<Configure>",  # Evento de configuração/redimensionamento do frame rolável

    # Define uma função lambda que será chamada 
            # quando o evento "<Configure>" ocorrer.
    # 'e' é o parâmetro do evento que representa o 
            # objeto de evento passado pelo bind.
    lambda e: canvas.configure(
        
        # Configura a região de rolagem do canvas para 
                # garantir que toda a área do frame rolável seja rolável.
        # 'scrollregion=canvas.bbox("all")' ajusta a 
                # região de rolagem do canvas para abranger 
                # toda a área delimitada pelo conteúdo do frame rolável.
        # 'canvas.bbox("all")' retorna as coordenadas da 
                # bounding box que engloba todos os widgets filhos do canvas.
        scrollregion=canvas.bbox("all")
        
    )
)

# Quando o frame rolável é redimensionado ou 
        # configurado, o evento "<Configure>" é disparado.
# A função lambda associada a este evento é chamada, 
        # recebendo o evento como parâmetro 'e'.
# Dentro da função lambda, 'canvas.configure(scrollregion=canvas.bbox("all"))' é chamado.
# 'canvas.bbox("all")' calcula a bounding box (região 
        # delimitadora) que engloba todos os 
        # widgets filhos do canvas.
# 'canvas.configure(scrollregion=canvas.bbox("all"))' 
        # ajusta a região de rolagem do canvas para 
        # abranger toda essa bounding box.
# Isso garante que toda a área do frame rolável 
        # possa ser rolada usando as barras de rolagem do canvas.


# Cria uma janela dentro do canvas para o frame rolável.
# 'canvas.create_window((0, 0), window=frame_rolavel, anchor="nw")' 
        # coloca o 'frame_rolavel' no ponto (0, 0) 
        # dentro do canvas.
# 'anchor="nw"' assegura que o ponto de ancoragem da 
        # janela seja o canto superior esquerdo (noroeste).
canvas.create_window((0, 0), 
                     window=frame_rolavel, 
                     anchor="nw")

# Configura o canvas para usar as barras de rolagem 
        # horizontais e verticais.
# 'xscrollcommand=scrollbar_x.set' associa a barra 
        # de rolagem horizontal ao canvas, para que 
        # a posição da barra de rolagem controle a 
        # visualização horizontal.
# 'yscrollcommand=scrollbar_y.set' faz o mesmo 
        # para a barra de rolagem vertical.
canvas.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

# Posiciona o canvas e as barras de rolagem dentro do 
        # frame da tabela usando o método 'grid'.
# Isso organiza os elementos na grade, assegurando que 
        # todos os componentes se ajustem adequadamente 
        # dentro do frame da tabela.

# Posiciona o canvas na primeira linha e primeira 
        # coluna do 'frame_tabela'.
# 'sticky="nsew"' expande o canvas para preencher 
        # completamente a célula da grade, aderindo às 
        # bordas norte, sul, leste e oeste da célula.
canvas.grid(row=0, column=0, sticky="nsew")

# Posiciona a barra de rolagem horizontal na 
        # segunda linha e primeira coluna do 'frame_tabela'.
# 'sticky="ew"' expande a barra de rolagem 
        # horizontal para preencher toda a largura da célula.
scrollbar_x.grid(row=1, column=0, sticky="ew")

# Posiciona a barra de rolagem vertical na primeira 
        # linha e segunda coluna do 'frame_tabela'.
# 'sticky="ns"' expande a barra de rolagem vertical 
        # para preencher toda a altura da célula.
scrollbar_y.grid(row=0, column=1, sticky="ns")

# Configura o 'frame_tabela' para se expandir e preencher a janela.
# Isso assegura que o frame da tabela ocupe todo o 
        # espaço disponível na janela, tornando a 
        # interface responsiva e adaptável.

# Configura a linha 0 do 'frame_tabela' para se 
        # expandir, ajustando-se ao redimensionamento.
# 'weight=1' assegura que a linha 0 do frame se 
        # expanda proporcionalmente quando a 
        # janela é redimensionada.
frame_tabela.grid_rowconfigure(0, weight=1)

# Configura a coluna 0 do 'frame_tabela' para se 
        # expandir, ajustando-se ao redimensionamento.
# 'weight=1' assegura que a coluna 0 do frame se 
        # expanda proporcionalmente quando a 
        # janela é redimensionada.
frame_tabela.grid_columnconfigure(0, weight=1)

# Cria um dicionário para armazenar os labels (rótulos) da tabela.
# Este dicionário será usado para acessar e atualizar 
        # os rótulos de cada célula da tabela conforme necessário.
# 'tabela_labels' é um dicionário onde cada chave é 
        # um índice de linha e o valor é outro dicionário 
        # que armazena os rótulos das colunas dessa linha.
tabela_labels = {}

# Inicializa o dicionário 'tabela_labels' com um 
        # número máximo de 100 linhas.
# O loop 'for linha in range(100)' itera de 0 a 99, 
        # criando uma entrada para cada linha.
for linha in range(100):  # Supondo um máximo de 100 linhas para os dados
    
    # Para cada linha, cria um dicionário vazio. 
            # Este dicionário interno armazenará os 
            # rótulos de cada coluna para essa linha.
    tabela_labels[linha] = {}

# Chama a função 'carregar_dados' para carregar os 
        # dados da tabela do arquivo Excel.
# 'carregar_dados()' lê os dados do arquivo Excel e 
        # popula a tabela na interface gráfica com os 
        # dados carregados.
carregar_dados()

# Inicia o loop principal da interface gráfica.
# 'janela_principal.mainloop()' inicia o loop de 
        # eventos do tkinter, que mantém a janela 
        # aberta e responsiva às interações do usuário.
janela_principal.mainloop()