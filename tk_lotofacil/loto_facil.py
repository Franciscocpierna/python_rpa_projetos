# Importa o módulo tkinter e o renomeia para 'tk'. Tkinter é uma
        # biblioteca padrão do Python para criação de 
        # interfaces gráficas de usuário (GUI).
import tkinter as tk

# Importa o módulo 'ttk' do tkinter. 'ttk' (Themed Tkinter) é 
        # usado para acessar widgets estilizados do Tkinter que 
        # fornecem uma aparência mais moderna e temas adicionais em 
        # comparação com os widgets padrão do Tkinter.
from tkinter import ttk

# Importa os módulos 'Image' e 'ImageTk' da biblioteca PIL (Pillow). 
        # 'Image' é usado para manipular imagens em diferentes formatos. 
        # 'ImageTk' é utilizado para integrar imagens do PIL 
        # com widgets do Tkinter.
from PIL import Image, ImageTk

# Importa a biblioteca 'pandas' e a renomeia para 'pd'. Pandas é 
        # uma biblioteca de código aberto, proporcionando estruturas de 
        # dados de alto desempenho e ferramentas de análise de 
        # dados para a linguagem Python.
import pandas as pd

# Importa o módulo 'os' que fornece uma maneira portátil de usar 
        # funcionalidades dependentes do sistema operacional, como 
        # ler ou escrever arquivos, manipular caminhos, etc.
import os

# Importa a biblioteca 'random', que inclui funções para geração de 
        # números aleatórios, escolha de elementos aleatórios de uma 
        # lista, embaralhamento de dados, entre outros.
import random


# Função para conferir os números inseridos pelo usuário contra os jogos 
            # salvos, calculando os acertos e atualizando a interface gráfica.
def conferir_numeros():
    
    # Cria uma lista 'numeros_entrada' que coleta todos os números 
            # digitados pelo usuário nos campos de entrada.
    # 'entradas' é uma lista de widgets Entry do tkinter, cada um 
            # contendo um número fornecido pelo usuário.
    # 'entrada.get()' retorna o valor atual do campo Entry como uma 
            # string, que é convertido para inteiro usando 'int()'.
    numeros_entrada = [int(entrada.get()) for entrada in entradas]

    # Itera sobre cada linha de 'dados', que contém os jogos previamente 
            # carregados de um arquivo Excel.
    # 'enumerate(dados.values)' permite iterar sobre as linhas do DataFrame 
            # 'dados', fornecendo o índice da linha (linha) e os valores 
            # da linha (valores).
    for linha, valores in enumerate(dados.values):
        
        # Converte cada valor da linha para inteiro. Primeiro, converte o 
                # valor para float e depois para int, garantindo a conversão 
                # adequada de formatos numéricos.
        # Filtra também valores nulos usando 'pd.isna(val)' para 
                # evitar erros de tipo.
        valores_int = [int(float(val)) for val in valores if not pd.isna(val)]

        # Calcula os acertos comparando os números inseridos com os 
                # números da linha do jogo.
        # 'set(numeros_entrada)' cria um conjunto dos números digitados e 
                # 'set(valores_int)' cria um conjunto dos números na linha.
        # 'intersection' retorna um conjunto contendo os elementos 
                # comuns aos dois conjuntos.
        # 'len(...)' conta quantos números são comuns entre os dois 
                # conjuntos, resultando no número de acertos.
        acertos = len(set(numeros_entrada).intersection(valores_int))
        
        # Atualiza a coluna de acertos na interface gráfica.
        # Acessa o rótulo correspondente à coluna de acertos usando 
                # 'tabela_labels[linha][max_colunas]', onde max_colunas é o 
                # índice da coluna de acertos.
        lbl_acertos = tabela_labels[linha][max_colunas]

        # Atualiza o texto do rótulo para mostrar o número de acertos.
        lbl_acertos.config(text=f"Acertou {acertos}")  
        
        # Reinicia a cor de fundo de todas as células dos números para 
                # branco com texto preto.
        # Isso é feito para limpar qualquer destaque de verificações 
                # anteriores, garantindo que apenas os números corretos da 
                # tentativa atual sejam destacados.
        for coluna in range(len(valores_int)):
            
            # 'tabela_labels[linha][coluna]' acessa o rótulo específico que 
                    # representa um número na linha atual e coluna específica.
            # 'config(bg="white", fg="black")' altera a configuração de cor de 
                    # fundo (bg) para branco e cor do texto (fg) para preto.
            # Isso é aplicado a cada célula que representa um número na linha atual, 
                    # garantindo que todos os números sejam resetados visualmente.
            tabela_labels[linha][coluna].config(bg="white", fg="black")

        
        # Destaca os números corretos mudando a cor de fundo para azul e o 
                # texto para branco.
        # Isso é feito após a reinicialização das cores para garantir que 
                # apenas os números que correspondem aos valores inseridos 
                # pelo usuário sejam destacados.
        for coluna, val in enumerate(valores_int):
            
            # Checa se o valor atual 'val' está presente na lista 'numeros_entrada' que 
                    # contém os números fornecidos pelo usuário.
            if val in numeros_entrada:
                
                # Se o número está nos valores inseridos pelo usuário, muda a cor de 
                        # fundo do rótulo para azul e o texto para branco.
                # 'bg="blue", fg="white"' configura o rótulo para ter um fundo 
                        # azul (facilmente visível) com texto branco para alto contraste.
                tabela_labels[linha][coluna].config(bg="blue", fg="white")


        # Verifica se o número de acertos é 11 ou mais, o que é 
                # considerado um número elevado de acertos na Lotofácil.
        if acertos >= 11:
            
            # Se os acertos forem 11 ou mais, altera a cor de fundo do 
                    # rótulo de acertos para verde e o texto para branco.
            # Isso serve para destacar visualmente que o usuário teve um 
                    # número significativo de acertos.
            lbl_acertos.config(bg="green", fg="white")
            
        else:
            
            # Se os acertos forem menos que 11, mantém a cor de fundo do 
                    # rótulo de acertos como branco e o texto preto.
            # Isso indica uma quantidade menor de acertos, não 
                    # destacando o campo de forma especial.
            lbl_acertos.config(bg="white", fg="black")



# Define a função que cria uma janela para gerar um jogo 
        # aleatório, conhecido popularmente como "surpresinha".
def gerar_surpresinha():
    
    # Cria uma nova janela sobreposta à janela principal do 
            # aplicativo. 'Toplevel' é um widget que funciona como 
            # uma janela flutuante independente.
    janela_surpresinha = tk.Toplevel(janela_principal)
    
    # Define o título da nova janela.
    janela_surpresinha.title("Gerar Surpresinha")
    
    # Configura o fundo da janela para branco.
    janela_surpresinha.configure(background='white')
    
    # Chama a função 'centralizar_janela' para centralizar a 
            # janela_surpresinha na tela, definindo suas 
            # dimensões para 800x400 pixels.
    centralizar_janela(janela_surpresinha, 800, 400)

    # Cria um frame dentro da janela_surpresinha para conter os 
            # widgets (elementos interativos), com fundo branco.
    frame_surpresinha = tk.Frame(janela_surpresinha, bg='white')
    
    # Empacota o frame no layout da janela com um espaço vertical (pady) 
            # de 20 pixels para separá-lo de outros elementos.
    frame_surpresinha.pack(pady=20)

    # Define uma fonte comum para os textos dentro desta janela para 
            # garantir consistência visual.
    fonte = ("Arial", 20)

    # Configura colunas e linhas "fantasma" que não contêm widgets mas 
            # ajudam no alinhamento e na distribuição do espaço dentro da janela.
    # 'weight=1' atribui um peso igual para essas linhas e colunas, 
            # fazendo com que ocupem qualquer espaço extra igualmente.
    janela_surpresinha.grid_columnconfigure(0, weight=1)
    janela_surpresinha.grid_columnconfigure(2, weight=1)
    janela_surpresinha.grid_rowconfigure(0, weight=1)
    janela_surpresinha.grid_rowconfigure(2, weight=1)

    # Posiciona o frame_surpresinha na janela usando o gerenciador de 
            # layout grid na linha 1, coluna 1.
    frame_surpresinha.grid(row=1, column=1)

    # Cria um rótulo (Label) no frame 'frame_surpresinha'. Este rótulo 
            # serve para orientar o usuário a fornecer uma entrada específica:
            # no caso, a quantidade de números para gerar um jogo aleatório.
    tk.Label(frame_surpresinha, 
             
             # 'text="Escolha a quantidade de números:"' define o texto que 
                     # será exibido no rótulo, que instrui claramente o 
                     # usuário sobre o que deve ser feito.
             text="Escolha a quantidade de números:", 
             
             # 'font=fonte' aplica a fonte definida anteriormente ('Arial', 20) ao 
                     # texto do rótulo, garantindo que o texto seja facilmente legível.
             font=fonte, 
             
             # 'bg='white'' define a cor de fundo do rótulo como branco, 
                     # mantendo a consistência com o design geral da janela.
             bg='white', 
             
             # 'anchor='center'' alinha o texto do rótulo ao centro. Isso é 
                     # útil para garantir que o texto esteja esteticamente 
                     # centrado dentro do rótulo.
             anchor='center'
             
            ).grid(row=0, column=1, pady=10, sticky='ew')  # Posiciona o rótulo na grade do 'frame_surpresinha'.
             # 'row=0, column=1' coloca o rótulo na primeira linha e na 
                        # segunda coluna da grade.
             # 'pady=10' adiciona um padding vertical de 10 pixels, ajudando a 
                        # separar visualmente este rótulo de outros elementos adjacentes.
             # 'sticky='ew'' faz o rótulo se estender de leste a oeste dentro de sua 
                        # célula na grade, garantindo que o rótulo ocupe todo o 
                        # espaço horizontal disponível.

    
    # Cria um campo de entrada (Entry) no frame 'frame_surpresinha'. 
            # Este campo permite ao usuário inserir um número, especificando 
            # quantos números aleatórios deseja gerar.
    entrada_quantidade = tk.Entry(frame_surpresinha, 
                                  
                                  # 'width=5' define a largura do campo de entrada como 5 caracteres, 
                                          # o que é suficiente para os números esperados (15 a 20).
                                  width=5, 
                                  
                                  # 'font=fonte' aplica a mesma fonte definida anteriormente, 
                                          # garantindo consistência e legibilidade.
                                  font=fonte, 
                                  
                                  # 'justify='center'' alinha o texto digitado pelo usuário ao 
                                          # centro do campo de entrada, melhorando a estética e 
                                          # facilitando a leitura.
                                  justify='center'
                                  
                                 )

    entrada_quantidade.grid(row=1, 
                            column=1, 
                            pady=5, 
                            sticky='ew')  # Posiciona o campo de entrada na grade.
        # 'row=1, column=1' coloca o campo de entrada na segunda linha e na 
                # segunda coluna, diretamente abaixo do rótulo correspondente.
        # 'pady=5' adiciona um padding vertical de 5 pixels, criando um espaço 
                # entre este campo de entrada e outros elementos, ajudando a 
                # evitar um layout apertado.
        # 'sticky='ew'' faz com que o campo de entrada se estenda de leste a 
                # oeste dentro de sua célula na grade, utilizando completamente o 
                # espaço horizontal.


    # Define uma função interna que é chamada quando o 
            # botão "Criar" é pressionado.
    def criar_surpresinha():
        
        # Obtém o número de elementos que o usuário deseja 
                # gerar e converte para inteiro.
        num_numeros = int(entrada_quantidade.get())
        
        # Verifica se o número está dentro do intervalo 
                # permitido (15 a 20).
        if 15 <= num_numeros <= 20:
            
            # Gera uma lista de números aleatórios dentro do 
                    # intervalo [1, 25] e ordena.
            numeros_aleatorios = sorted(random.sample(range(1, 26), num_numeros))
            
            # Chama a função para exibir os números aleatórios 
                    # gerados na janela.
            exibir_jogo_aleatorio(janela_surpresinha, numeros_aleatorios, num_numeros)
            
        else:
            
            # Se o número não está no intervalo permitido, exibe 
                    # uma mensagem de erro.
            tk.Label(frame_surpresinha, 
                     text="Por favor, insira um número entre 15 e 20.", 
                     font=fonte, 
                     bg='white').grid(row=2, column=0, pady=5, sticky='nsew')

    # Cria um botão no frame 'frame_surpresinha', que permite ao usuário 
                    # iniciar a geração de um jogo aleatório, conhecido 
                    # como "surpresinha".
    botao_criar = tk.Button(frame_surpresinha, 
                            
                            # 'text="Criar"' define o texto que será exibido no botão. 
                                    # Este texto é uma instrução clara para o usuário 
                                    # sobre o que acontecerá quando o botão for pressionado.
                            text="Criar", 
                            
                            # 'command=criar_surpresinha' associa este botão à 
                                    # função 'criar_surpresinha'. 
                            # Quando o botão é clicado, essa função é chamada 
                                    # automaticamente. A função 'criar_surpresinha' 
                                    # contém toda a lógica 
                            # para validar a entrada do usuário e gerar os números 
                                    # aleatórios se a entrada for válida.
                            command=criar_surpresinha, 
                            
                            # 'font=fonte' especifica que o botão deve usar a mesma 
                                    # fonte definida anteriormente ('Arial', 20), 
                                    # garantindo consistência visual e legibilidade em 
                                    # toda a interface do usuário.
                            font=fonte)

    # Posiciona o botão na grade dentro de 'frame_surpresinha' usando o método 'grid'.
    botao_criar.grid(row=3,                  # 'row=3' coloca o botão na quarta linha da grade. 
                                                        # Esta posição é escolhida para dar espaço adequado 
                                              # entre o campo de entrada e o botão, evitando uma 
                                                        # interface apertada e melhorando a estética.
                     column=1,                # 'column=1' coloca o botão na segunda coluna, alinhando-o 
                                                        # diretamente abaixo do campo de entrada 
                                                        # e do rótulo acima, o que ajuda na organização lógica e 
                                                        # intuitiva dos componentes.
                     pady=10,                 # 'pady=10' adiciona 10 pixels de padding vertical acima e 
                                                        # abaixo do botão. Este espaço extra 
                                                        # ajuda a separar visualmente o botão de outros 
                                                        # elementos na interface, tornando-o mais acessível.
                     sticky='nsew')           # 'sticky="nsew"' faz com que o botão se expanda para 
                                                        # preencher completamente sua célula na grade. 
                                              # 'nsew' significa norte, sul, leste e oeste, indicando que o 
                                                        # botão deve se estender para tocar todos os lados da célula,
                                                        # maximizando sua área clicável e melhorando a usabilidade.



# Define a função que exibe os números aleatórios gerados na 
            # janela 'surpresinha'.
def exibir_jogo_aleatorio(janela_surpresinha, numeros_aleatorios, num_numeros):
    
    # Limpa todos os widgets (como botões, rótulos, etc.) que 
            # estavam anteriormente na janela 'surpresinha'.
    # 'winfo_children()' retorna uma lista de todos os widgets que 
            # são filhos da janela 'surpresinha'.
    for widget in janela_surpresinha.winfo_children():
        
        # 'destroy()' é um método que remove completamente o widget da 
                # interface gráfica, liberando recursos e limpando a tela.
        widget.destroy()

    # Configura o fundo da janela 'surpresinha' para branco após 
            # limpar os widgets antigos.
    janela_surpresinha.configure(background='white')

    # Cria um novo frame chamado 'frame_resultado' dentro da 
            # janela 'surpresinha', com fundo branco também.
    frame_resultado = tk.Frame(janela_surpresinha, bg='white')
    
    # 'pack()' é um gerenciador de geometria usado para adicionar o 
            # frame à janela. 'pady=20' adiciona um espaço 
            # vertical para estética.
    frame_resultado.pack(pady=20)

    # Define uma fonte comum para todos os textos que 
            # aparecerão neste frame.
    fonte = ("Arial", 20)

    # Configura colunas e linhas 'fantasma' na janela 'surpresinha'. 
            # Essas colunas e linhas não contêm widgets diretamente, mas são 
            # usadas para controlar o espaço entre os widgets reais e 
            # a borda da janela.
    janela_surpresinha.grid_columnconfigure(0, weight=1)

    # Configura a coluna 0 (a primeira coluna à esquerda) para 
            # ter um 'weight' (peso) de 1. 
    # Isso significa que essa coluna vai expandir para preencher qualquer 
            # espaço extra disponível, ajudando a centralizar os widgets que 
            # serão colocados nas colunas centrais.
    janela_surpresinha.grid_columnconfigure(2, weight=1)
    
    # Configura a coluna 2 (a terceira coluna à direita) de maneira semelhante à 
            # coluna 0, garantindo que o espaço extra também seja distribuído 
            # igualmente à direita.
    
    janela_surpresinha.grid_rowconfigure(0, weight=1)
    # Configura a linha 0 (a primeira linha no topo da janela) 
            # para ter um 'weight' de 1. 
    # Isso permite que a linha expanda verticalmente para preencher o 
            # espaço extra, empurrando os widgets centrais um pouco para baixo.
    
    janela_surpresinha.grid_rowconfigure(2, weight=1)
    # Configura a linha 2 (a terceira linha na parte inferior da 
            # janela) de forma semelhante à linha 0, 
    # garantindo que o espaço extra na parte inferior também ajude a 
            # centralizar verticalmente os widgets na linha central.
    
    # Essas configurações criam um "buffer" de espaço ao redor dos widgets 
            # centrais, tornando o layout mais agradável visualmente e menos apertado.


    # Adiciona 'frame_resultado' ao grid da janela, colocando-o 
            # estrategicamente no centro para boa visualização.
    frame_resultado.grid(row=1, column=1)
    # Posiciona 'frame_resultado' na linha 1, coluna 1 da janela 'surpresinha'. 
    # Esta é a célula central dado que as colunas e linhas fantasma 
            # ocupam as bordas, o que garante que este frame seja o 
            # foco visual principal.
    
    # Cria e posiciona um rótulo no frame para mostrar o título e a 
            # quantidade de números gerados.
    tk.Label(frame_resultado, 

             # Texto dinâmico que indica a quantidade de números no jogo aleatório.
             text=f"Jogo Aleatório ({num_numeros} números):",  

             # Aplica a fonte previamente definida, garantindo
                     # consistência e legibilidade.
             font=fonte,  

             # Define o fundo do rótulo como branco, mantendo o
                     # esquema de cores limpo e simples.
             bg='white'  

            # Posiciona este rótulo na primeira linha (row=0) do frame,
                    # utilizando 'sticky='nsew'' para garantir que o
                    # rótulo se expanda para preencher toda a célula.
            ).grid(row=0, column=0, pady=10, sticky='nsew')
    
    
    # Cria e posiciona outro rótulo abaixo do primeiro para 
            # mostrar os números aleatórios gerados.
    tk.Label(frame_resultado, 

             # Junta a lista de números aleatórios em uma única
                     # string, separando cada número por um espaço.
             text=" ".join(map(str, numeros_aleatorios)),  
             font=fonte, 
             bg='white'
            ).grid(row=1, column=0, pady=5, sticky='nsew')
    # Posiciona este rótulo na segunda linha (row=1) do frame, diretamente 
            # abaixo do rótulo do título, também expandindo para preencher toda a célula.
    
    # Esses rótulos fornecem informações claras e visíveis sobre o resultado 
            # da "surpresinha", tornando a interface interativa e informativa.


    # Define uma função interna 'salvar_jogo' que será chamada 
            # quando o usuário clicar no botão "Salvar Jogo".
    def salvar_jogo():
        
        # Chama a função 'adicionar_jogo' para adicionar os 
                # números gerados à lista de jogos salvos.
        adicionar_jogo(numeros_aleatorios)
        
        # Fecha a janela 'surpresinha' após salvar os números.
        janela_surpresinha.destroy()
        
        # Atualiza a tela principal para refletir as mudanças 
                # após o novo jogo ser adicionado.
        atualizar_tela()

    # Cria um botão dentro do 'frame_resultado' que permite ao 
                # usuário salvar o jogo gerado aleatoriamente.
    botao_salvar = tk.Button(frame_resultado, 
                             
                             # 'text="Salvar Jogo"' define o texto exibido no botão, que é 
                                     # uma instrução clara para o usuário sobre a ação 
                                     # que o botão realizará.
                             text="Salvar Jogo", 
                             
                             # 'command=salvar_jogo' associa este botão à função 'salvar_jogo'. 
                                     # Essa função é chamada quando o botão é clicado,
                             # executando a lógica para salvar o jogo gerado nos 
                                     # registros ou banco de dados.
                             command=salvar_jogo, 
                             
                             # 'font=fonte' aplica a fonte definida anteriormente para o 
                                     # texto do botão, garantindo que ele seja coerente com o 
                                     # resto da interface e facilmente legível.
                             font=fonte, 
                             
                             # 'bg='white'' define a cor de fundo do botão como branco, 
                                     # mantendo a consistência com o esquema de cores da interface.
                             bg='white')

    # Usa o gerenciador de layout 'grid' para posicionar o 
            # botão 'Salvar Jogo' no frame.
    # 'row=2' coloca o botão na terceira linha do
            # 'grid' no 'frame_resultado'.
    botao_salvar.grid(row=2,                  

                      # 'column=0' especifica que o botão deve ocupar a primeira coluna.
                      column=0,               

                      # 'pady=5' adiciona 5 pixels de espaço vertical acima e
                              # abaixo do botão para separá-lo de outros elementos.
                      pady=5,                 

                      # 'sticky="nsew"' faz com que o botão expanda para
                              # preencher completamente sua célula no grid,
                              # tocando todas as bordas da célula, o que melhora a
                              # aparência e a facilidade de clique.
                      sticky='nsew')          
                                              


    # Cria um botão dentro do 'frame_resultado' que permite ao usuário 
            # cancelar a operação de geração de jogo.
    botao_cancelar = tk.Button(frame_resultado, 
                               
                               # 'text="Cancelar"' define o texto exibido no botão, 
                                       # indicando sua função de cancelar a operação e fechar a janela.
                               text="Cancelar", 
                               
                               # 'command=janela_surpresinha.destroy' vincula uma 
                                       # função que fechará (destruirá) a janela 'surpresinha' 
                                       # quando o botão for clicado.
                               # Isso permite ao usuário abortar a operação sem 
                                       # salvar os números gerados.
                               command=janela_surpresinha.destroy, 
                               
                               # 'font=fonte' garante que o texto do botão use a mesma 
                                       # fonte dos outros textos na interface, mantendo a 
                                       # consistência visual.
                               font=fonte, 
                               
                               # 'bg='white'' define a cor de fundo do botão como branco, 
                                       # alinhado com o design geral da interface.
                               bg='white')

    # Posiciona o botão 'Cancelar' usando o gerenciador de layout 'grid'.
    # 'row=3' posiciona o botão na quarta linha do 'grid' no
            # 'frame_resultado', colocando-o abaixo do botão 'Salvar Jogo'.
    botao_cancelar.grid(row=3,                

                        # 'column=0' coloca o botão na primeira coluna, alinhando-o
                                    # verticalmente com o botão 'Salvar Jogo' acima.
                        column=0,             

                        # 'pady=5' adiciona 5 pixels de espaço vertical para um
                                    # layout não apertado e uma estética melhor.
                        pady=5,               

                        # 'sticky="nsew"' assegura que o botão expanda para preencher
                                    # toda a célula no grid, melhorando a
                                    # acessibilidade e a aparência.
                        sticky='nsew')        



# Define a função 'adicionar_jogo' que recebe uma lista de 
            # números aleatórios como parâmetro.
def adicionar_jogo(numeros_aleatorios):
    
    # Declara 'dados' e 'max_colunas' como variáveis globais para 
            # permitir a modificação dentro desta função.
    global dados, max_colunas

    # Cria uma nova linha como uma série pandas, contendo os números 
            # aleatórios e preenchendo o restante das colunas com None (Nulo),
    # para que a quantidade de colunas na nova linha corresponda ao 
            # número de colunas no DataFrame 'dados'.
    nova_linha = pd.Series(numeros_aleatorios + [None]*(len(dados.columns) - len(numeros_aleatorios)), 
                           
                           # O índice para a série é definido como as colunas do 
                                   # DataFrame 'dados' para garantir alinhamento correto.
                           index=dados.columns)

    # Concatena o DataFrame 'dados' existente com a nova linha convertida em 
            # DataFrame e transposta (de série para formato tabular).
    dados = pd.concat([dados, nova_linha.to_frame().T], 
                      
                      # 'ignore_index=True' é usado para reindexar o DataFrame 
                              # resultante, garantindo a continuidade dos índices.
                      ignore_index=True)

    # Salva o DataFrame atualizado de volta ao arquivo Excel 
            # 'Jogos_Lotofacil.xlsx' para persistência de dados.
    dados.to_excel('Jogos_Lotofacil.xlsx', sheet_name='Jogos', index=False)

    # Atualiza a tabela na interface gráfica com o novo jogo adicionado.
    # Calcula o índice da última linha adicionada ao DataFrame, 
            # que corresponde ao novo jogo.
    linha = dados.shape[0] - 1

    # 'dados.shape[0]' retorna o número total de linhas no 
            # DataFrame 'dados'.
    # Subtraindo 1 do total de linhas, obtemos o índice da 
            # última linha, que é onde o novo jogo foi adicionado.
    
    # Chama a função 'criar_linha_tabela' para adicionar visualmente a 
            # nova linha à tabela na GUI.
    criar_linha_tabela(numeros_aleatorios + [None]*(max_colunas - len(numeros_aleatorios)), 
                       
                       # Aqui, estamos preparando a lista de valores a 
                               # serem adicionados à tabela.
                       # 'numeros_aleatorios' é a lista de números do novo jogo. 
                       # Adicionamos 'None' para cada coluna faltante, garantindo 
                               # que o número de elementos na lista
                               # corresponda ao número máximo de colunas ('max_colunas') no DataFrame.
                       # Isto é necessário porque a tabela na interface gráfica 
                               # precisa ter todas as suas colunas preenchidas
                       # para manter a consistência visual e estrutural.
                       linha,  # Este é o índice da linha onde a nova linha deve ser adicionada na interface gráfica.
                       max_colunas)  # Este é o número total de colunas que a tabela deve ter.



# Define a função para abrir uma janela que permite ao 
            # usuário cadastrar jogos manualmente.
def cadastrar_manual():
    
    # Cria uma nova janela de nível superior, que será usada 
            # para o cadastro manual de jogos.
    janela_manual = tk.Toplevel(janela_principal)
    
    # Define o título da nova janela.
    janela_manual.title("Cadastrar Jogo Manualmente")
    
    # Configura a cor de fundo da janela para branco, o que 
            # ajuda na clareza visual e consistência do design.
    janela_manual.configure(background='white')
    
    # Chama a função para centralizar a janela no centro da 
            # tela, com as dimensões especificadas (1200x600 pixels).
    centralizar_janela(janela_manual, 1200, 600)

    # Cria um frame dentro da janela manual que servirá como o 
            # contêiner principal para outros widgets.
    frame_manual = tk.Frame(janela_manual, bg='white')
    
    # Adiciona o frame ao layout da janela, posicionando-o 
            # com um espaço vertical (pady) de 20 pixels.
    # O espaço ajuda a evitar que os componentes fiquem 
            # muito juntos, melhorando a estética.
    frame_manual.pack(pady=20)

    # Define uma fonte comum para todos os textos dentro da 
            # janela, garantindo consistência visual.
    fonte = ("Arial", 20)

    # Configura colunas e linhas 'fantasma' ao redor do frame 
            # central para ajudar na distribuição do espaço.
    # Essas colunas e linhas não contêm widgets mas são 
            # usadas para criar margens ao redor do conteúdo central,
            # garantindo que o layout central não fique 
            # grudado nas bordas da janela.
    janela_manual.grid_columnconfigure(0, weight=1)
    janela_manual.grid_columnconfigure(2, weight=1)
    janela_manual.grid_rowconfigure(0, weight=1)
    janela_manual.grid_rowconfigure(2, weight=1)

    # Posiciona o frame_manual no centro do grid da 
            # janela_manual. Ele é colocado na linha 1, coluna 1,
    # que é efetivamente o centro da janela devido às 
            # configurações das colunas e linhas 'fantasma'.
    frame_manual.grid(row=1, column=1)


    # Cria um rótulo dentro do 'frame_manual'. Este rótulo 
            # serve para instruir o usuário sobre o que deve ser 
            # feito na próxima etapa da interface.
    tk.Label(frame_manual, 
             
             # 'text="Escolha a quantidade de números:"' define o 
                     # texto exibido no rótulo, fornecendo instruções 
                     # claras ao usuário.
             text="Escolha a quantidade de números:",
             
             # 'font=fonte' aplica a fonte definida anteriormente, 
                     # garantindo que o texto seja grande o suficiente para 
                     # ser lido facilmente e mantenha a consistência 
                     # estética com outros textos na interface.
             font=fonte, 
             
             # 'bg='white'' define a cor de fundo do rótulo como branco, 
                     # mantendo o design limpo e claro da interface.
             bg='white', 
             
             # 'anchor='center'' alinha o texto ao centro do rótulo, 
                     # melhorando a estética e tornando o texto mais 
                     # visível dentro do espaço designado.
             anchor='center'

            # Posiciona o rótulo na primeira linha (row=0) do
                     # 'grid' dentro do frame.
            ).grid(row=0,                   

                   # Posiciona o rótulo na primeira coluna (column=0).
                   column=0,                

                   # Permite que o rótulo se estenda por 5 colunas, aumentando sua
                           # largura para acomodar o texto de forma adequada.
                   columnspan=5,            

                   # Adiciona um padding vertical de 10 pixels
                           # acima e abaixo do rótulo, dando espaço
                           # suficiente entre os elementos.
                   pady=10,                 

                   # Faz com que o rótulo se expanda para preencher
                           # todo o espaço horizontal disponível na célula.
                   sticky='ew')             

    # Cria um campo de entrada ('Entry') para que o usuário possa 
            # digitar a quantidade de números que deseja inserir no jogo.
    entrada_quantidade_manual = tk.Entry(frame_manual, 
                                         
                                         # 'width=5' define a largura do campo de entrada, 
                                                 # permitindo que o usuário veja claramente até cinco 
                                                 # caracteres, o que é suficiente para os números 
                                                 # típicos inseridos neste contexto.
                                         width=5, 
                                         
                                         # 'font=fonte' aplica a mesma fonte usada no rótulo, 
                                                 # mantendo a consistência visual e facilitando a leitura.
                                         font=fonte, 
                                         
                                         # 'justify='center'' centraliza o texto digitado no campo, o 
                                                 # que é útil para uma melhor apresentação e 
                                                 # legibilidade dos números inseridos.
                                         justify='center'
                                         
                                        )
    
    # Posiciona o campo de entrada no 'grid' do 'frame_manual'.
    # Posiciona o campo de entrada na segunda linha (row=1),
            # diretamente abaixo do rótulo.
    entrada_quantidade_manual.grid(row=1,        

                                   # Posiciona na primeira coluna (column=0).
                                   column=0,      

                                   # Permite que o campo de entrada se estenda por 5 colunas,
                                           # assim como o rótulo acima, garantindo alinhamento.
                                   columnspan=5,  

                                   # Adiciona um padding vertical de 5 pixels, proporcionando um
                                           # espaço adequado entre este campo e outros elementos.
                                   pady=5,        

                                   # Faz com que o campo de entrada se expanda horizontalmente para
                                           # preencher toda a largura disponível na célula.
                                   sticky='ew')   


    # Define a função 'criar_entradas_manual', que cria dinamicamente os 
            # campos de entrada para os números do jogo, com base na 
            # quantidade especificada pelo usuário.
    def criar_entradas_manual():
        
        # Obtém o número de campos de entrada que o usuário deseja criar, 
                # convertendo a entrada do campo 'entrada_quantidade_manual' 
                # para um inteiro.
        num_numeros_manual = int(entrada_quantidade_manual.get())
    
        # Verifica se o número de campos de entrada está dentro do 
                # intervalo permitido (entre 15 e 20).
        if 15 <= num_numeros_manual <= 20:
            
            # Remove todos os widgets atualmente no 'frame_manual' para 
                    # garantir que a interface seja limpa antes de adicionar novos widgets.
            # 'winfo_children()' retorna uma lista de todos os widgets 
                    # filhos dentro do 'frame_manual'.
            for widget in frame_manual.winfo_children():
                
                # 'destroy()' remove completamente o widget da 
                        # interface gráfica.
                widget.destroy()
    
            # Cria e posiciona um novo rótulo no 'frame_manual' 
                    # para instruir o usuário a inserir os números do jogo.
            tk.Label(frame_manual, 
                     
                     # Texto do rótulo que orienta o usuário a inserir os números.
                     text="Insira os números do jogo:", 
                     
                     # Aplicação da fonte previamente definida para 
                             # consistência visual.
                     font=fonte, 
                     
                     # Define o fundo do rótulo como branco.
                     bg='white', 
                     
                     # Alinha o texto ao centro do rótulo.
                     anchor='center'

                    # Posiciona o rótulo na primeira linha do grid do frame.
                    ).grid(row=0,  

                           # Posiciona o rótulo na primeira coluna do grid do frame.
                           column=0,  

                           # Permite que o rótulo se estenda por 5 colunas,
                                   # para maior visibilidade.
                           columnspan=5,

                           # Adiciona um padding vertical de 10 pixels
                                   # acima e abaixo do rótulo.
                           pady=10,  

                           # Faz com que o rótulo se expanda horizontalmente
                                   # para preencher toda a célula.
                           sticky='ew')  
    
            # Inicializa uma lista para armazenar os widgets de 
                    # entrada dos números.
            entradas_numeros_manual = []

            # Loop para criar os campos de entrada dos números do jogo, 
                    # baseado na quantidade especificada pelo usuário.
            for i in range(num_numeros_manual):
                
                # Cria um rótulo para cada número, numerando-os 
                        # sequencialmente (Número 1, Número 2, etc.).
                tk.Label(frame_manual, 
                         
                         # Define o texto do rótulo para mostrar o 
                                 # número sequencial.
                         text=f"Número {i+1}:", 
                         
                         # Aplica a fonte previamente definida para 
                                 # consistência visual.
                         font=fonte, 
                         
                         # Define a cor de fundo do rótulo como branco.
                         bg='white'

                        # Calcula a linha em que o rótulo deve ser posicionado. Utiliza a
                                 # divisão inteira por 5 para agrupar rótulos e entradas em filas de 5.
                        ).grid(row=(i//5)*2+1,

                               # Calcula a coluna em que o rótulo deve ser posicionado. Utiliza o
                                       # operador módulo para distribuir os rótulos em 5 colunas.
                               column=(i%5),

                               # Adiciona um padding vertical de 5 pixels para
                                       # separar visualmente os rótulos.
                               pady=5,  

                               # Adiciona um padding horizontal de 5 pixels
                                       # para separar visualmente os rótulos.
                               padx=5,  

                               # Faz com que o rótulo se expanda horizontalmente
                                       # para preencher a célula da grade.
                               sticky='ew')  
            
                # Cria um campo de entrada para cada número, alinhando-se 
                        # com o rótulo correspondente.
                entrada = tk.Entry(frame_manual, 
                                   
                                   # Define a largura do campo de entrada para 5 
                                           # caracteres, suficiente para inserir os números.
                                   width=5, 
                                   
                                   # Aplica a mesma fonte usada nos rótulos para 
                                           # manter a consistência visual.
                                   font=fonte, 
                                   
                                   # Centraliza o texto digitado no campo de entrada.
                                   justify='center')

                # Calcula a linha em que o campo de entrada deve ser
                        # posicionado, logo abaixo do rótulo correspondente.
                entrada.grid(row=(i//5)*2+2,

                             # Posiciona o campo de entrada na mesma
                                     # coluna que o rótulo correspondente.
                             column=(i%5),

                             # Adiciona um padding vertical de 5 pixels para
                                     # separar visualmente os campos de entrada.
                             pady=5,  

                             # Adiciona um padding horizontal de 5 pixels para
                                     # separar visualmente os campos de entrada.
                             padx=5,  

                             # Faz com que o campo de entrada se expanda
                                     # horizontalmente para preencher a célula da grade.
                             sticky='ew')  
            
                # Adiciona o campo de entrada criado à lista 'entradas_numeros_manual' para 
                        # posterior acesso e manipulação dos valores inseridos.
                entradas_numeros_manual.append(entrada)


            # Define a função 'salvar_jogo_manual', que coleta os números inseridos 
                    # manualmente pelo usuário, valida a quantidade e salva o jogo.
            def salvar_jogo_manual():
                
                # Coleta os números inseridos em cada campo de entrada, 
                        # converte-os para inteiros e cria uma lista. 
                # Apenas os campos que contêm valores são 
                        # considerados ('if entry.get()' garante isso).
                numeros_jogo_manual = [int(entry.get()) for entry in entradas_numeros_manual if entry.get()]
                
                # Verifica se a quantidade de números inseridos está 
                        # dentro do intervalo permitido (15 a 20).
                if 15 <= len(numeros_jogo_manual) <= 20:
                    
                    # Chama a função 'adicionar_jogo' para adicionar o 
                            # jogo ao conjunto de dados.
                    # Os números são classificados em ordem crescente 
                            # antes de serem adicionados.
                    adicionar_jogo(sorted(numeros_jogo_manual))
                    
                    # Fecha a janela de cadastro manual após salvar os números.
                    janela_manual.destroy()
                    
                    # Chama a função 'atualizar_tela' para atualizar a 
                            # interface gráfica, refletindo o novo jogo adicionado.
                    atualizar_tela()
                    
                else:
                    
                    # Se a quantidade de números não estiver no intervalo 
                            # permitido, exibe uma mensagem de erro na interface.
                    tk.Label(frame_manual, 
                             
                             text="Por favor, insira entre 15 e 20 números.", 
                             
                             font=fonte, 
                             
                             bg='white'

                            # Posiciona a mensagem de erro na sexta linha do grid.
                            ).grid(row=6,  

                                   # Posiciona a mensagem na primeira coluna.
                                   column=0,  

                                   # A mensagem se estende por 5 colunas, tornando-a visível.
                                   columnspan=5,

                                   # Adiciona um padding vertical de 5 pixels para espaçamento.
                                   pady=5,  

                                   # Faz com que o rótulo se expanda para preencher
                                           # horizontalmente a célula.
                                   sticky='nsew')  


            # Cria um botão dentro do 'frame_manual' que permite ao 
                    # usuário salvar o jogo inserido manualmente.
            botao_salvar_manual = tk.Button(frame_manual, 
                                            
                                            # Define o texto exibido no botão como "Salvar Jogo".
                                            text="Salvar Jogo", 
                                            
                                            # Associa o comando 'salvar_jogo_manual' ao botão, que 
                                                    # será executado quando o botão for clicado.
                                            command=salvar_jogo_manual, 
                                            
                                            # Aplica a fonte definida anteriormente para 
                                                    # manter a consistência visual.
                                            font=fonte, 
                                            
                                            # Define a cor de fundo do botão como branco, 
                                                    # mantendo o design limpo e claro.
                                            bg='white')

            # Posiciona o botão 'Salvar Jogo' na grade do 'frame_manual'.
            # Calcula a linha em que o botão deve ser posicionado. A posição é
                    # determinada com base no número de entradas criadas.
            botao_salvar_manual.grid(row=(num_numeros_manual//5)*2+3,  

                                     # Posiciona o botão na segunda coluna.
                                     column=1,  

                                     # Adiciona um padding vertical de 10 pixels, proporcionando
                                             # espaço entre o botão e outros elementos.
                                     pady=10,  

                                     # Faz com que o botão se expanda para preencher a
                                            # célula da grade horizontalmente e verticalmente.
                                     sticky='nsew')  


            # Cria um botão dentro do 'frame_manual' que permite ao 
                    # usuário cancelar a operação de cadastro manual.
            botao_cancelar_manual = tk.Button(frame_manual, 
                                              
                                              # Define o texto exibido no botão como "Cancelar".
                                              text="Cancelar", 
                                              
                                              # Associa o comando 'janela_manual.destroy' ao botão, 
                                                      # que fechará a janela quando o botão for clicado.
                                              command=janela_manual.destroy, 
                                              
                                              # Aplica a mesma fonte para consistência visual.
                                              font=fonte, 
                                              
                                              # Define a cor de fundo do botão como branco.
                                              bg='white')

            # Posiciona o botão 'Cancelar' na grade do 'frame_manual'.
            # Calcula a linha em que o botão deve ser posicionado.
                    # A posição é determinada com base no número de entradas criadas.
            botao_cancelar_manual.grid(row=(num_numeros_manual//5)*2+3,  

                                       # Posiciona o botão na quarta coluna.
                                       column=3, 

                                       # Adiciona um padding vertical de 10 pixels.
                                       pady=10,  

                                       # Faz com que o botão se expanda para preencher a
                                               # célula da grade horizontalmente e verticalmente.
                                       sticky='nsew')  

        # Se a quantidade de números inserida não estiver entre 15 e 20, 
                # exibe uma mensagem de erro.
        else:
            
            tk.Label(frame_manual, 
                     
                     # Define o texto do rótulo de erro.
                     text="Por favor, insira entre 15 e 20 números.", 
                     
                     # Aplica a fonte definida anteriormente.
                     font=fonte, 
                     
                     # Define a cor de fundo do rótulo como branco.
                     bg='white'

                    # Posiciona o rótulo de erro na terceira linha do grid.
                    ).grid(row=2,  

                           # Posiciona o rótulo na primeira coluna.
                           column=0,  

                           # O rótulo se estende por 5 colunas para melhor visibilidade.
                           columnspan=5,  

                           # Adiciona um padding vertical de 5 pixels.
                           pady=5,  

                           # Faz com que o rótulo se expanda para preencher
                                   # horizontalmente a célula.
                           sticky='nsew')  


    # Cria um botão dentro do 'frame_manual' que permite ao 
            # usuário criar campos de entrada para os números.
    botao_criar_manual = tk.Button(frame_manual, 
                                   
                                   # Define o texto exibido no botão como "Criar".
                                   text="Criar", 
                                   
                                   # Associa o comando 'criar_entradas_manual' ao 
                                           # botão, que será executado quando o botão for clicado.
                                   command=criar_entradas_manual, 
                                   
                                   # Aplica a mesma fonte para consistência visual.
                                   font=fonte, 
                                   
                                   # Define a cor de fundo do botão como branco.
                                   bg='white')

    # Posiciona o botão 'Criar' na grade do 'frame_manual'.
    # Posiciona o botão na terceira linha do grid.
    botao_criar_manual.grid(row=2,  

                            # Posiciona o botão na primeira coluna.
                            column=0,  

                            # O botão se estende por 5 colunas, garantindo
                                    # visibilidade e espaço suficiente para o texto.
                            columnspan=5,  

                            # Adiciona um padding vertical de 10 pixels.
                            pady=10,  

                            # Faz com que o botão se expanda para
                                    # preencher horizontalmente a célula.
                            sticky='nsew')



# Define uma função chamada 'carregar_dados' para carregar e 
        # manipular os dados do jogo da Lotofácil de um arquivo Excel.
def carregar_dados():
    
    # A palavra-chave 'global' é usada para declarar que 
            # 'dados' e 'max_colunas' são variáveis globais.
    # Isso significa que essas variáveis podem ser acessadas e 
            # modificadas em qualquer parte do código fora desta função.
    global dados, max_colunas

    # Usa a função 'read_excel' da biblioteca pandas para ler o 
            # arquivo Excel chamado 'Jogos_Lotofacil.xlsx'.
    # 'sheet_name='Jogos'' especifica que apenas a aba 
            # chamada 'Jogos' deve ser lida.
    dados = pd.read_excel('Jogos_Lotofacil.xlsx', sheet_name='Jogos')

    # 'dados.notna()' retorna um DataFrame onde cada célula é True 
            # se não for NA/NaN, ou seja, se contiver dados válidos.
    # '.sum(axis=1)' calcula a soma ao longo do eixo das linhas (axis=1), 
            # o que dá o número de células não nulas em cada linha.
    # '.max()' então encontra o valor máximo dessas somas, o que indica o 
            # número máximo de colunas válidas (não nulas) em qualquer 
            # linha do DataFrame.
    # Esse valor é armazenado em 'max_colunas', que será usado para 
            # definir a largura da tabela na interface gráfica.
    max_colunas = dados.notna().sum(axis=1).max()

    # Chama a função 'criar_cabecalhos' e passa 'max_colunas' como argumento.
    # Esta função é responsável por criar os cabeçalhos da tabela 
            # na interface gráfica.
    criar_cabecalhos(max_colunas)

    # 'dados.iterrows()' é um gerador que itera sobre as linhas do 
            # DataFrame 'dados' como pares (índice, linha).
    # 'i' é o índice da linha e 'linha' é a linha (como uma série pandas).
    for i, linha in dados.iterrows():
        
        # A função 'criar_linha_tabela' é chamada para cada 
                # linha do DataFrame.
        # Ela recebe a linha atual convertida em lista ('list(linha)'), o 
                # índice da linha ('i') e o valor de 'max_colunas'.
        # Esta função é usada para criar visualmente cada linha da 
                # tabela na interface gráfica.
        criar_linha_tabela(list(linha), i, max_colunas)


# Define uma função chamada 'criar_cabecalhos' que é usada para 
        # criar os cabeçalhos da tabela na interface gráfica.
# Esta função recebe um parâmetro chamado 'max_colunas', que indica o 
        # número máximo de colunas com dados válidos no arquivo Excel.
def criar_cabecalhos(max_colunas):
    
    # Cria uma lista de cabeçalhos para a tabela. Utiliza uma compreensão de 
            # lista para gerar uma série de cabeçalhos
    # numerados de 'Número 1' até 'Número {max_colunas}'. Após os números, 
            # adiciona 'Acertos' e um cabeçalho vazio para uso futuro.
    # Por exemplo, se max_colunas for 5, cabecalhos será ['Número 1', 
            # 'Número 2', ..., 'Número 5', 'Acertos', ''].
    cabecalhos = [f'Número {i+1}' for i in range(max_colunas)] + ['Acertos', '']

    # Itera sobre a lista de cabeçalhos usando um loop. 'enumerate' fornece um 
            # índice (col) e o valor (cabecalho) para cada item na lista.
    # 'col' representa o índice da coluna na interface gráfica, começando de 0.
    # 'cabecalho' é o texto do cabeçalho correspondente a essa coluna.
    for col, cabecalho in enumerate(cabecalhos):
        
        # Cria um objeto 'Label' do Tkinter. 'Label' é um widget usado para 
                # exibir texto ou imagens.
        # 'frame_rolavel' é o contêiner onde este rótulo será colocado. 
                # 'frame_rolavel' é um frame.
        # 'text=cabecalho' define o texto do rótulo como o cabeçalho atual.
        # 'borderwidth=2' define a largura da borda do rótulo como 2 pixels.
        # 'relief="solid"' configura o estilo da borda para ser sólido.
        # 'width=10' estabelece a largura do rótulo como 10 caracteres.
        lbl = tk.Label(frame_rolavel, text=cabecalho, borderwidth=2, relief="solid", width=10)

        # Posiciona o rótulo na primeira linha (row=0) da grade no 'frame_rolavel'. 
                # A coluna é definida pelo índice 'col'.
        # 'sticky='nsew'' faz com que o rótulo se expanda e adira ao 
                # norte, sul, leste e oeste da célula da grade, garantindo 
                # que preencha todo o espaço disponível.
        lbl.grid(row=0, column=col, sticky='nsew')


# Define uma função chamada 'criar_linha_tabela' que cria visualmente 
        # uma linha de tabela na interface gráfica.
# Recebe três parâmetros: 'valores' que é uma lista dos 
        # valores para essa linha,
# 'linha' que é o índice da linha, e 'max_colunas' que é o 
        # número máximo de colunas preenchidas com dados.
def criar_linha_tabela(valores, linha, max_colunas):
    
    # Inicializa o índice da coluna. Este índice é usado para 
            # rastrear em qual coluna o próximo widget deve ser colocado.
    indice_coluna = 0

    # Itera sobre cada valor na lista de valores fornecida.
    for val in valores:
        
        # Verifica se o valor não é NA (não disponível). A função 
                # 'pd.notna' é usada para verificar se há dados válidos.
        if pd.notna(val):
            
            # Cria um rótulo (Label) com o valor, que é convertido 
                    # para inteiro e então para string.
            # O rótulo tem uma borda sólida com largura de 1 pixel e 
                    # uma largura fixa de 10 caracteres.
            lbl = tk.Label(frame_rolavel, text=str(int(val)), 
                           borderwidth=1, 
                           relief="solid", 
                           width=10)
            
            # Posiciona o rótulo na grade. O rótulo é colocado na 
                    # linha especificada ('linha'+1 para compensar o 
                    # cabeçalho) e na coluna atual ('indice_coluna').
            lbl.grid(row=linha+1, column=indice_coluna, sticky='nsew')
            
            # Armazena o rótulo no dicionário 'tabela_labels' para 
                    # futuras referências ou atualizações.
            tabela_labels[linha][indice_coluna] = lbl
            
            # Incrementa o índice da coluna para que o próximo valor 
                    # seja colocado na próxima coluna.
            indice_coluna += 1
    
    # Este bloco de código é responsável por preencher quaisquer colunas 
                    # restantes na linha da tabela com rótulos vazios.
    # Isso garante que todas as linhas da tabela tenham o mesmo número de 
            # colunas, mesmo que algumas colunas não contenham dados.
    for _ in range(indice_coluna, max_colunas):
        
        # Cria um rótulo vazio. 'tk.Label' cria um widget de rótulo no Tkinter.
        # 'frame_rolavel' é o contêiner onde o rótulo será colocado.
        # 'text=""' define o texto do rótulo como uma string vazia, 
                # pois esta coluna não tem dados a serem exibidos.
        # 'borderwidth=1' define a largura da borda do rótulo como 1 pixel, o 
                # que ajuda a visualizar os limites de cada célula na tabela.
        # 'relief="solid"' define o estilo da borda do rótulo como sólido, 
                # proporcionando uma borda visível ao redor do rótulo.
        # 'width=10' estabelece a largura do rótulo como 10 caracteres, 
                # garantindo que todas as colunas tenham uma largura uniforme.
        lbl = tk.Label(frame_rolavel, text="", borderwidth=1, relief="solid", width=10)
        
        # Posiciona o rótulo na grade. O método 'grid' é usado para 
                # adicionar o rótulo ao layout da grade no 'frame_rolavel'.
        # 'row=linha+1' coloca o rótulo na linha especificada mais um (para 
                # compensar o cabeçalho que está na primeira linha).
        # 'column=indice_coluna' coloca o rótulo na coluna atual que 
                # está sendo preenchida.
        # 'sticky='nsew'' faz com que o rótulo se expanda e adira às 
                # bordas norte (n), sul (s), leste (e) e oeste (w) da célula da grade,
        # o que ajuda a preencher completamente a célula.
        lbl.grid(row=linha+1, column=indice_coluna, sticky='nsew')
    
        # Armazena o rótulo no dicionário 'tabela_labels', que é usado 
                # para manter uma referência aos widgets de rótulo para 
                # futuras atualizações.
        # 'linha' é a chave do dicionário para a linha atual, e 
                # 'indice_coluna' é a subchave para a coluna atual.
        tabela_labels[linha][indice_coluna] = lbl
    
        # Incrementa 'indice_coluna' para mover para a próxima coluna 
                # que precisa ser preenchida.
        indice_coluna += 1


    # Adiciona um rótulo para os 'acertos' na próxima coluna após os dados. 
            # Este rótulo servirá para mostrar quantos números corretos 
            # foram acertados em cada jogo cadastrado.

    # Cria um widget Label (rótulo) no frame 'frame_rolavel'. 
    # 'frame_rolavel' é um contêiner onde todos os elementos da 
            # tabela (dados dos jogos) estão sendo organizados.
    lbl_acertos = tk.Label(frame_rolavel, 
                           
                           # 'text=""' - inicialmente, o texto do rótulo é definido 
                                   # como vazio porque o número de acertos só será determinado 
                           # após a conferência dos números, que acontece em 
                                   # uma operação posterior.
                           text="", 
                           
                           # 'borderwidth=1' - define a largura da borda do rótulo 
                                   # como 1 pixel. Isso ajuda a delinear visualmente os 
                                   # elementos da GUI, tornando mais fácil para o usuário 
                                   # distinguir entre os diferentes componentes da tabela.
                           borderwidth=1, 
                           
                           # 'relief="solid"' - especifica que o rótulo terá uma borda 
                                   # sólida. O "relief" define o estilo da borda,
                           # e um relief "solid" cria uma borda visível e proeminente ao redor do 
                                   # rótulo, o que é útil para destacar o campo de acertos.
                           relief="solid", 
                           
                           # 'width=15' - define a largura do rótulo como 15 unidades. Essa 
                                   # largura é escolhida para garantir que haja espaço suficiente
                           # para exibir a quantidade de acertos sem cortar o texto, 
                                   # proporcionando uma leitura clara e sem obstruções.
                           width=15)

                          
    # Configura o posicionamento do rótulo dentro da grade (grid) usando:
    # 'row=linha+1' - define a linha para posicionar o rótulo, incrementando 'linha' 
            # por 1 para ajustar à linha correta (considerando o cabeçalho).
    # 'column=indice_coluna' - coloca o rótulo na coluna calculada após 
            # preencher os dados da linha.
    # 'sticky='nsew'' - faz o rótulo expandir-se para preencher toda a célula da 
            # grade em todas as direções (norte, sul, leste, oeste).
    lbl_acertos.grid(row=linha+1, 
                     column=indice_coluna, 
                     sticky='nsew')
                           
    # Salva uma referência ao rótulo no dicionário 'tabela_labels' para permitir 
            # atualizações futuras. A chave usada é uma tupla de (linha, indice_coluna).
    tabela_labels[linha][indice_coluna] = lbl_acertos
    
    # Adiciona um botão 'Excluir' que permite ao usuário remover a linha 
            # correspondente da tabela.
    # Cria um widget Button (botão) no frame 'frame_rolavel' com o texto "Excluir".
    btn_excluir = tk.Button(frame_rolavel, text="Excluir", 
                            
                            # Define uma função anônima (lambda) como comando que 
                                    # será executado quando o botão for pressionado.
                            # 'lambda r=linha: excluir_jogo(r)' captura o valor atual 
                                    # de 'linha' e passa para a função 'excluir_jogo'.
                            # Isso permite que a função 'excluir_jogo' saiba qual linha 
                                    # deve ser excluída sem confusão de índices.
                            command=lambda r=linha: excluir_jogo(r))

    # Configura o posicionamento do botão na grade, similar ao rótulo de 
            # acertos, mas na próxima coluna ('indice_coluna+1').
    btn_excluir.grid(row=linha+1, column=indice_coluna+1, sticky='nsew')

    # Salva uma referência ao botão no dicionário 'tabela_labels' usando a 
            # chave (linha, indice_coluna+1), permitindo acesso fácil 
            # para modificações futuras.
    tabela_labels[linha][indice_coluna+1] = btn_excluir



# Define a função 'excluir_jogo', que é responsável por remover 
        # uma linha específica do DataFrame e do arquivo Excel.
def excluir_jogo(linha):
    
    # Declara 'dados' como uma variável global para permitir que esta 
            # função modifique o DataFrame global 'dados'.
    global dados

    # Remove a linha especificada do DataFrame 'dados'. 
    # 'drop(linha)' é o método usado para excluir a linha cujo 
            # índice é fornecido pelo argumento 'linha'.
    # 'reset_index(drop=True)' é chamado em seguida para reajustar os 
            # índices do DataFrame depois da remoção da linha,
            # garantindo que não haja lacunas nos índices. 'drop=True' evita 
            # que o índice antigo seja adicionado como uma coluna no DataFrame.
    dados = dados.drop(linha).reset_index(drop=True)

    # Salva o DataFrame atualizado de volta ao arquivo Excel 
            # 'Jogos_Lotofacil.xlsx' para atualizar os dados salvos.
    # 'to_excel' é o método utilizado para escrever o 
            # DataFrame em um arquivo Excel.
    # 'sheet_name='Jogos'' especifica a aba do arquivo Excel 
            # onde os dados devem ser salvos.
    # 'index=False' é usado para evitar que o índice do DataFrame 
            # seja salvo no arquivo, mantendo o arquivo limpo apenas com os dados.
    dados.to_excel('Jogos_Lotofacil.xlsx', sheet_name='Jogos', index=False)

    # Chama a função 'atualizar_tela' para atualizar a representação 
            # visual da tabela na interface gráfica,
    # refletindo a remoção da linha no display visual para que os 
            # usuários possam ver imediatamente que a linha foi de fato excluída.
    atualizar_tela()


# Define a função 'atualizar_tela', que é responsável por 
        # atualizar ou recarregar a interface gráfica da tabela de dados.
def atualizar_tela():
    
    # Itera sobre todos os widgets (como rótulos, botões, etc.) 
            # que são filhos do 'frame_rolavel'.
    # 'frame_rolavel' é um contêiner na interface gráfica que 
            # contém os elementos da tabela de dados.
    for widget in frame_rolavel.winfo_children():
        
        # 'widget.destroy()' é um método que remove 
                # completamente o widget da interface gráfica.
        # Isso é usado aqui para limpar todos os elementos 
                # gráficos antigos antes de recarregar ou atualizar a tabela.
        widget.destroy()

    # Chama a função 'carregar_dados', que é responsável por 
            # carregar os dados do arquivo Excel ou de uma fonte de dados
            # e por reconstruir a tabela na interface gráfica com os dados atualizados.
    carregar_dados()
    

# Define a função 'centralizar_janela', que ajusta a posição de 
            # uma janela na tela para que apareça centralizada.
def centralizar_janela(janela, largura, altura):
    
    # Obtém a largura total da tela do dispositivo em que a 
            # aplicação está sendo executada.
    # 'winfo_screenwidth()' é um método que retorna a 
            # largura da tela em pixels.
    largura_tela = janela.winfo_screenwidth()
    
    # Obtém a altura total da tela do dispositivo.
    # 'winfo_screenheight()' é um método que retorna a 
            # altura da tela em pixels.
    altura_tela = janela.winfo_screenheight()
    
    # Calcula a posição x da janela para que ela fique 
            # centralizada horizontalmente.
    # Isso é feito subtraindo metade da largura da janela de 
            # metade da largura da tela.
    pos_x = (largura_tela // 2) - (largura // 2)
    
    # Calcula a posição y da janela para que ela fique 
            # centralizada verticalmente.
    # Isso é feito subtraindo metade da altura da janela de 
            # metade da altura da tela.
    pos_y = (altura_tela // 2) - (altura // 2)
    
    # Configura a geometria da janela para usar as dimensões 
            # especificadas e as posições x e y calculadas.
    # 'geometry' é um método que define as dimensões e a 
            # posição da janela na forma "larguraxaltura+posx+posy".
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")


# Cria a janela principal da aplicação.
janela_principal = tk.Tk()

# Define o título da janela principal, que aparecerá na 
            # barra de título da janela.
janela_principal.title("Conferidor de Jogos da Lotofácil")

# Define o tamanho inicial da janela principal para 1200 pixels de 
        # largura por 700 pixels de altura.
janela_principal.geometry("1200x700")

# Configura a janela principal para não ser redimensionável em 
        # ambas as direções (horizontal e vertical).
janela_principal.resizable(False, False)

# Define a cor de fundo da janela principal para branco, 
        # proporcionando uma aparência limpa e clara.
janela_principal.configure(background='white')

# Centraliza a janela principal na tela, com as 
        # dimensões especificadas (1200x550 pixels).
centralizar_janela(janela_principal, 1200, 550)

# Adicionando a imagem de cabeçalho
image_path = "lotofacil.jpg"

# Verifica se o arquivo de imagem especificado existe no 
        # caminho fornecido.
if os.path.exists(image_path):
    
    # Abre a imagem usando a biblioteca PIL (Python Imaging Library).
    img = Image.open(image_path)
    
    # Redimensiona a imagem para ajustar-se às dimensões 
            # desejadas (1200x200 pixels).
    # O método LANCZOS é utilizado para a interpolação durante o 
            # redimensionamento para manter a qualidade da imagem.
    img = img.resize((1200, 200), Image.LANCZOS)
    
    # Converte a imagem PIL em um formato compatível com 
            # Tkinter para exibição.
    photo = ImageTk.PhotoImage(img)
    
    # Cria um rótulo (Label) na janela principal para exibir a imagem.
    # 'image=photo' define a imagem a ser exibida no rótulo.
    label_imagem = tk.Label(janela_principal, image=photo)
    
    # Manter a referência da imagem: é importante manter 
            # uma referência da imagem
    # para evitar que seja coletada pelo coletor de lixo, o 
            # que poderia causar a imagem a desaparecer.
    label_imagem.image = photo
    
    # Posiciona o rótulo na janela principal com um 
            # espaçamento vertical (pady) de 10 pixels
            # para separar a imagem de outros elementos na interface.
    label_imagem.pack(pady=10)
    
else:
    
    # Caso o arquivo de imagem não seja encontrado, 
            # imprime uma mensagem de erro no console,
            # indicando que o arquivo especificado não foi encontrado.
    print(f"Erro: o arquivo {image_path} não foi encontrado.")


# Cria um rótulo (Label) para o título da janela principal.
titulo = tk.Label(janela_principal, 
                  
                  # Define o texto do rótulo como "Conferidor de Jogos da Lotofácil".
                  text="Conferidor de Jogos da Lotofácil", 
                  
                  # Define a fonte do texto como Arial, tamanho 16.
                  font=("Arial", 16))

# Posiciona o rótulo do título na janela principal.
titulo.pack(pady=10)  # Adiciona um espaçamento vertical (pady) de 10 pixels 
                        # acima e abaixo do título para separar visualmente de 
                        # outros elementos.

frame_entradas = tk.Frame(janela_principal)
frame_entradas.pack(pady=10)

# Inicializa as listas que irão armazenar os 
        # widgets de entrada e seus respectivos rótulos.
entradas = []  # Lista para armazenar os widgets de entrada.
labels = []    # Lista para armazenar os rótulos associados aos widgets de entrada.


# Loop para criar rótulos e campos de entrada em 3 linhas e 5 colunas.
for i in range(3):  # Itera sobre as 3 linhas.
    
    for j in range(5):  # Itera sobre as 5 colunas.
        
        # Cria um rótulo (Label) para cada campo de entrada, 
                # numerado sequencialmente.
        # 'text=f"Número {i*5 + j + 1}:"' define o texto do rótulo com 
                # um número sequencial, calculado a partir dos índices 'i' e 'j'.
        label = tk.Label(frame_entradas, text=f"Número {i*5 + j + 1}:")
        
        # Posiciona o rótulo na grade do 'frame_entradas'.
        # 'row=i' posiciona o rótulo na linha correspondente ao 
                # índice 'i' do loop.
        # 'column=j*2' posiciona o rótulo na coluna correspondente ao 
                # índice 'j' multiplicado por 2.
        # Isso é feito para garantir que os rótulos ocupem colunas 
                # pares, deixando as colunas ímpares para os 
                # campos de entrada.
        # 'padx=5, pady=5' adiciona espaçamento horizontal e 
                # vertical de 5 pixels ao redor do rótulo.
        label.grid(row=i, 
                   column=j*2, 
                   padx=5, 
                   pady=5)
        
        # Adiciona o rótulo à lista de rótulos.
        labels.append(label)
        
        # Cria um campo de entrada (Entry) com largura 
                # definida para 5 caracteres.
        entrada = tk.Entry(frame_entradas, width=5)
        
        # Posiciona o campo de entrada na grade do 'frame_entradas', 
                # ao lado do rótulo correspondente.
        # 'row=i' posiciona o campo de entrada na mesma linha 
                # que o rótulo correspondente.
        # 'column=j*2+1' posiciona o campo de entrada na coluna 
                # imediatamente à direita do rótulo correspondente.
        # Isso é feito para garantir que os campos de entrada 
                # ocupem colunas ímpares, logo após os rótulos.
        # 'padx=5, pady=5' adiciona espaçamento horizontal e 
                # vertical de 5 pixels ao redor do campo de entrada.
        entrada.grid(row=i, column=j*2+1, padx=5, pady=5)
        
        # Adiciona o campo de entrada à lista de entradas.
        entradas.append(entrada)


# Cria um botão dentro do 'frame_entradas' para 
        # conferir os números inseridos.
botao_conferir = tk.Button(frame_entradas, 
                           
                           # Define o texto exibido no botão como "Conferir".
                           text="Conferir", 
                           
                           # Associa o comando 'conferir_numeros' ao 
                                   # botão, que será executado quando o botão for clicado.
                           command=conferir_numeros)

# Posiciona o botão 'Conferir' na grade do 'frame_entradas'.
# 'row=3' posiciona o botão na quarta linha.
# 'column=10' posiciona o botão na décima primeira coluna.
# 'padx=5, pady=5' adiciona espaçamento horizontal e 
        # vertical de 5 pixels ao redor do botão.
botao_conferir.grid(row=3, column=10, padx=5, pady=5)


# Cria um botão dentro do 'frame_entradas' 
        # para gerar uma Surpresinha.
botao_surpresinha = tk.Button(frame_entradas, 
                              
                              # Define o texto exibido no botão como "Surpresinha".
                              text="Surpresinha", 
                              
                              # Associa o comando 'gerar_surpresinha' ao 
                                      # botão, que será executado quando o botão for clicado.
                              command=gerar_surpresinha)

# Posiciona o botão 'Surpresinha' na grade do 'frame_entradas'.
# 'row=3' posiciona o botão na quarta linha.
# 'column=11' posiciona o botão na décima segunda coluna.
# 'padx=5, pady=5' adiciona espaçamento horizontal e 
        # vertical de 5 pixels ao redor do botão.
botao_surpresinha.grid(row=3, column=11, padx=5, pady=5)


# Cria um botão dentro do 'frame_entradas' para permitir o 
        # cadastro manual de números.
botao_manual = tk.Button(frame_entradas, 
                         
                         # Define o texto exibido no botão como "Cadastrar Manual".
                         text="Cadastrar Manual", 
                         
                         # Associa o comando 'cadastrar_manual' ao botão, 
                                 # que será executado quando o botão for clicado.
                         command=cadastrar_manual)

# Posiciona o botão 'Cadastrar Manual' na grade do 'frame_entradas'.
# 'row=3' posiciona o botão na quarta linha.
# 'column=12' posiciona o botão na décima terceira coluna.
# 'padx=5, pady=5' adiciona espaçamento horizontal e 
        # vertical de 5 pixels ao redor do botão.
botao_manual.grid(row=3, column=12, padx=5, pady=5)


# Cria um frame dentro da janela principal para a tabela 
        # personalizada com barra de rolagem.
frame_tabela = tk.Frame(janela_principal)

# Posiciona o frame na janela principal.
# 'pady=10' adiciona um espaçamento vertical de 10 pixels acima e abaixo do frame.
# 'fill=tk.BOTH' permite que o frame se expanda para preencher 
        # todo o espaço disponível tanto horizontalmente 
        # quanto verticalmente.
# 'expand=True' permite que o frame cresça e encolha conforme a 
        # janela principal é redimensionada, mantendo a 
        # tabela visível e ajustada.
frame_tabela.pack(pady=10, fill=tk.BOTH, expand=True)


# Cria um canvas dentro do 'frame_tabela'.
canvas = tk.Canvas(frame_tabela)

# Cria uma barra de rolagem horizontal e associa seu 
        # comando ao movimento horizontal do canvas.
scrollbar_x = tk.Scrollbar(frame_tabela, 
                           orient="horizontal",  # Define a orientação da barra de rolagem como horizontal.
                           command=canvas.xview)  # Associa a função de rolagem horizontal do canvas à barra de rolagem.

# Cria uma barra de rolagem vertical e associa seu 
        # comando ao movimento vertical do canvas.
scrollbar_y = tk.Scrollbar(frame_tabela, 
                           orient="vertical",  # Define a orientação da barra de rolagem como vertical.
                           command=canvas.yview)  # Associa a função de rolagem vertical do canvas à barra de rolagem.

# Cria um frame rolável dentro do canvas, que será o 
        # contêiner para os widgets que precisam de rolagem.
frame_rolavel = tk.Frame(canvas)


# Associa um evento ao 'frame_rolavel' que ajusta a 
        # área de rolagem do 'canvas' sempre que o 
        # tamanho do 'frame_rolavel' é alterado.
frame_rolavel.bind(
    
    # O evento "<Configure>" é disparado sempre que o 
            # 'frame_rolavel' é redimensionado ou reconfigurado.
    "<Configure>",
    
    # A função lambda é usada para definir o comando que será 
            # executado quando o evento "<Configure>" for disparado.
    lambda e: canvas.configure(
        
        # 'scrollregion' define a região que pode ser 
                # rolada dentro do 'canvas'.
        # 'canvas.bbox("all")' retorna as coordenadas da 
                # caixa delimitadora que engloba todos os 
                # elementos dentro do 'canvas'.
        # Isso garante que a área de rolagem do 'canvas' seja 
                # ajustada para incluir todo o conteúdo do 'frame_rolavel'.
        scrollregion=canvas.bbox("all")
        
    )
)


# Cria uma janela dentro do canvas, onde o frame_rolavel será colocado.
# A posição (0, 0) define a origem (canto superior esquerdo) do 
        # frame_rolavel dentro do canvas.
# O parâmetro 'anchor="nw"' garante que o frame_rolavel seja 
        # ancorado no canto noroeste (superior esquerdo) do canvas.
canvas.create_window((0, 0), window=frame_rolavel, anchor="nw")

# Configura o canvas para usar as barras de rolagem horizontal e vertical.
# 'xscrollcommand=scrollbar_x.set' associa a barra de rolagem 
        # horizontal ao movimento horizontal do canvas.
# 'yscrollcommand=scrollbar_y.set' associa a barra de rolagem 
        # vertical ao movimento vertical do canvas.
canvas.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

# Posiciona o canvas na grade do frame_tabela.
# 'row=0, column=0' posiciona o canvas na primeira linha e 
        # primeira coluna do frame_tabela.
# 'sticky="nsew"' faz com que o canvas se expanda para preencher 
        # todo o espaço disponível na célula.
canvas.grid(row=0, column=0, sticky="nsew")

# Posiciona a barra de rolagem horizontal na grade do frame_tabela.
# 'row=1, column=0' posiciona a barra de rolagem horizontal na 
        # segunda linha e primeira coluna do frame_tabela.
# 'sticky="ew"' faz com que a barra de rolagem se expanda 
        # horizontalmente para preencher toda a largura do frame.
scrollbar_x.grid(row=1, column=0, sticky="ew")

# Posiciona a barra de rolagem vertical na grade do frame_tabela.
# 'row=0, column=1' posiciona a barra de rolagem vertical na 
        # primeira linha e segunda coluna do frame_tabela.
# 'sticky="ns"' faz com que a barra de rolagem se expanda 
        # verticalmente para preencher toda a altura do frame.
scrollbar_y.grid(row=0, column=1, sticky="ns")

# Configura o frame_tabela para se expandir e preencher a 
        # janela principal conforme necessário.
# 'grid_rowconfigure(0, weight=1)' define que a primeira linha do 
        # frame_tabela deve expandir para preencher o espaço disponível.
frame_tabela.grid_rowconfigure(0, weight=1)

# 'grid_columnconfigure(0, weight=1)' define que a primeira 
        # coluna do frame_tabela deve expandir para preencher o 
        # espaço disponível.
frame_tabela.grid_columnconfigure(0, weight=1)


# Dicionário para armazenar os labels (rótulos) da tabela.
# As chaves do dicionário serão os números das linhas, e os 
        # valores serão outros dicionários
        # que armazenam os labels para cada coluna dessa linha.
tabela_labels = {}

# Loop para inicializar o dicionário com 100 linhas.
# Supondo um máximo de 100 linhas para os dados.
for linha in range(100):  # Itera de 0 a 99, totalizando 100 linhas.
    
    # Para cada linha, adiciona uma entrada no dicionário 
            # 'tabela_labels' onde a chave é o número da linha
    # e o valor é um dicionário vazio que será usado para 
            # armazenar os labels das colunas.
    tabela_labels[linha] = {}

# Chama a função 'carregar_dados' para carregar os 
        # dados do arquivo Excel e preencher a tabela.
# Esta função popula o 'frame_rolavel' com os labels 
        # necessários, preenchendo as células da tabela 
        # conforme os dados carregados.
carregar_dados()

# Inicia o loop principal da janela.
# Este loop mantém a janela aberta e responsiva, 
        # permitindo a interação do usuário.
janela_principal.mainloop()