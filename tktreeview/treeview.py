# Importa o módulo tkinter e o renomeia para 'tk' para 
        # facilitar o acesso às suas funções.
import tkinter as tk

# Importa o submódulo 'ttk' de 'tkinter' que fornece acesso a 
        # widgets de interface de usuário mais avançados 
        # e com melhor aparência.
from tkinter import ttk

# Importa a biblioteca 'pandas', comummente usada para 
        # manipulação de dados, e a renomeia como 'pd'.
import pandas as pd



# Define a função 'calcular_media_turma' que recebe como parâmetro 'grupo',
        # que é um subconjunto de dados do DataFrame 
        # representando uma turma de alunos.
def calcular_media_turma(grupo):
    
    # Extrai as colunas 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4' do DataFrame 'grupo'
            # e calcula a média de cada linha, ou seja, a 
            # média das notas de cada aluno.
    # O parâmetro 'axis=1' especifica que a média deve ser 
            # calculada horizontalmente (across the columns).
    notas = grupo[['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4']].mean(axis=1)

    # Calcula a média das médias das notas dos alunos para 
            # obter a média geral da turma.
    # Isso resulta na média das médias individuais dos 
            # alunos, fornecendo a média da turma.
    return notas.mean()


# Define a função 'calcular_situacao' que recebe uma lista 'notas'.
def calcular_situacao(notas):
    
    # Calcula a média das notas somando todos os elementos 
            # da lista e dividindo pelo número de elementos.
    media = sum(notas) / len(notas)

    # Estrutura condicional para determinar a situação do 
            # aluno baseada na média calculada.
     # Se a média for 7 ou superior, o aluno é considerado "Aprovado".
    if media >= 7: 
        
        situacao = "Aprovado"

    # Se a média estiver entre 2 e 7 (não inclusivo), o 
            # aluno é considerado em "Recuperação".
    elif 2 <= media < 7:  
        
        situacao = "Recuperação"

    # Se a média for inferior a 2, o aluno é 
            # considerado "Reprovado".
    else:  
        
        situacao = "Reprovado"

    # Retorna dois valores: a média calculada e a 
            # situação do aluno como uma tupla.
    return media, situacao


# Esta função é chamada quando um aluno é selecionado 
            # na lista da interface gráfica.
def exibir_informacoes_aluno(event):
    
    # 'arvore.selection()[0]' obtém o identificador do item que 
            # foi selecionado pelo usuário na lista (Treeview).
    item_selecionado = arvore.selection()[0]
    
    # 'arvore.item(item_selecionado, 'values')' obtém os dados 
            # associados ao item selecionado, como o nome do aluno, etc.
    info_aluno = arvore.item(item_selecionado, 'values')
    
    # Este 'if' verifica se alguma informação foi realmente selecionada 
            # para evitar tentar usar dados que não existem.
    if info_aluno:
        
        # O nome do aluno é armazenado na primeira posição da 
                # lista de valores, que é extraída aqui.
        nome_aluno = info_aluno[0]
        
        # Busca no DataFrame 'df' por uma linha onde o nome do aluno 
                # corresponde ao nome selecionado.
        # 'df['Nome'] == nome_aluno' cria um filtro para as linhas com o 
                # mesmo nome e 'iloc[0]' pega a primeira linha que corresponder.
        aluno_dados = df[df['Nome'] == nome_aluno].iloc[0]
        
        # Cria uma lista das notas do aluno, acessando as colunas 
                # específicas de notas no DataFrame.
        notas = [aluno_dados['Nota 1'], aluno_dados['Nota 2'], aluno_dados['Nota 3'], aluno_dados['Nota 4']]
        
        # A função 'calcular_situacao' é chamada com a lista de 
                # notas do aluno para calcular sua média e determinar se 
                # está aprovado, em recuperação ou reprovado.
        media, situacao = calcular_situacao(notas)
        
        # Limpa o campo onde o nome do aluno é exibido e insere o 
                # nome do aluno selecionado.
        entrada_nome.delete(0, tk.END)
        entrada_nome.insert(0, nome_aluno)
        
        # Limpa o campo de entrada da nota 1 para garantir 
                # que não haja informações antigas.
        entrada_nota1.delete(0, tk.END)
        
        # Insere a primeira nota do aluno no campo de entrada da nota 1.
        entrada_nota1.insert(0, notas[0])

        # Limpa o campo de entrada da nota 2 para garantir 
                # que não haja informações antigas.
        entrada_nota2.delete(0, tk.END)
        
        # Insere a segunda nota do aluno no campo de entrada da nota 2.
        entrada_nota2.insert(0, notas[1])

        # Limpa o campo de entrada da nota 3 para garantir 
                # que não haja informações antigas.
        entrada_nota3.delete(0, tk.END)
        
        # Insere a terceira nota do aluno no campo de entrada da nota 3.
        entrada_nota3.insert(0, notas[2])

        # Limpa o campo de entrada da nota 4 para garantir 
                # que não haja informações antigas.
        entrada_nota4.delete(0, tk.END)
        
        # Insere a quarta nota do aluno no campo de entrada da nota 4.
        entrada_nota4.insert(0, notas[3])

        # Limpa o campo de entrada da média para garantir 
                # que não haja informações antigas.
        entrada_media.delete(0, tk.END)
        
        # Insere a média calculada do aluno no campo de entrada 
                # da média, formatada para duas casas decimais.
        entrada_media.insert(0, f"{media:.2f}")

        # Limpa o campo de entrada da situação para garantir 
                # que não haja informações antigas.
        entrada_situacao.delete(0, tk.END)
        
        # Insere a situação do aluno (Aprovado, Recuperação, Reprovado) 
                # no campo de entrada da situação.
        entrada_situacao.insert(0, situacao)

        # Verifica a situação do aluno para definir a cor de 
                # fundo e a cor do texto do campo de entrada da situação.
        if situacao == "Aprovado":
            
            # Define a cor de fundo como verde e a cor do texto 
                    # como branco se o aluno estiver aprovado.
            entrada_situacao.config(bg="green", fg="white")
            
        elif situacao == "Recuperação":
            
            # Define a cor de fundo como amarelo e a cor do texto 
                    # como preto se o aluno estiver em recuperação.
            entrada_situacao.config(bg="yellow", fg="black")
            
        else:  # Caso o aluno esteja reprovado
            
            # Define a cor de fundo como vermelho e a cor do texto 
                    # como branco se o aluno estiver reprovado.
            entrada_situacao.config(bg="red", fg="white")



# Carrega os dados de um arquivo Excel para um DataFrame do pandas.
# 'notas_estudantes.xlsx' é o nome do arquivo e 'Dados' é 
            # o nome da aba dentro do arquivo Excel.
df = pd.read_excel('notas_estudantes.xlsx', sheet_name='Dados')

# Inicia a construção da interface gráfica utilizando 
        # a biblioteca tkinter.
# Cria o objeto 'janela_principal' que serve como a 
        # janela principal do programa.
janela_principal = tk.Tk()

# Define o título da janela principal, que aparecerá 
        # na barra de título da janela.
janela_principal.title("Notas dos Estudantes")

# Define uma fonte padrão que será usada nos widgets 
        # (elementos interativos) da interface.
# 'Arial' é o tipo de fonte, e '14' é o tamanho da fonte.
fonte_padrao = ('Arial', 14)

# Cria um widget Treeview dentro da 'janela_principal'. Um 
        # Treeview é usado para exibir uma lista hierárquica de itens.
# 'style="mystyle.Treeview"' aplica um estilo personalizado 
        # chamado 'mystyle.Treeview'.
arvore = ttk.Treeview(janela_principal, style="mystyle.Treeview")

# Posiciona o Treeview dentro da 'janela_principal'. 'side='left'' 
        # coloca o Treeview no lado esquerdo da janela.
# 'fill='y'' faz com que o Treeview se expanda verticalmente 
        # para preencher o espaço disponível.
arvore.pack(side='left', fill='y')


# Cria um objeto de estilo para personalizar a aparência 
        # dos widgets do ttk, como a Treeview.
style = ttk.Style()

# Configura o estilo personalizado 'mystyle.Treeview' para o Treeview.
# Define a fonte padrão para os itens dentro do Treeview e 
        # ajusta a altura de cada linha para 30 pixels.
style.configure("mystyle.Treeview", font=fonte_padrao, rowheight=30)

# Configura o estilo para os cabeçalhos das colunas no Treeview 
        # usando 'mystyle.Treeview.Heading'.
# A fonte é definida como Arial, tamanho 16 e em negrito, o 
        # que destaca os cabeçalhos das colunas.
style.configure("mystyle.Treeview.Heading", font=('Arial', 16, 'bold'))

# Define as configurações da coluna principal (identificada por "#0") na Treeview.
# 'width=300' define a largura inicial da coluna como 300 pixels.
# 'minwidth=300' garante que a largura mínima da coluna 
        # seja 300 pixels, impedindo que seja menor que isso.
arvore.column("#0", width=300, minwidth=300)

# Define o cabeçalho da coluna principal na Treeview.
# 'text="Turma (Média da Turma)"' define o texto do cabeçalho.
# 'anchor=tk.W' alinha o texto do cabeçalho à esquerda (West).
arvore.heading("#0", text="Turma (Média da Turma)", anchor=tk.W)

# Agrupa os dados do DataFrame 'df' por 'Turma'. 
# Isso organiza os dados de forma que cada grupo contenha 
        # todas as linhas pertencentes à mesma turma.
turmas = df.groupby('Turma')


# Inicia um loop que percorre cada grupo de dados 
        # retornados pelo agrupamento por 'Turma'.
# 'turma' é o nome da turma e 'grupo' são os dados 
        # associados a essa turma.
for turma, grupo in turmas:
    
    # Chama a função 'calcular_media_turma' passando o 'grupo' de 
            # dados de uma turma específica para calcular a média 
            # das notas da turma.
    media_turma = calcular_media_turma(grupo)
    
    # Prepara o texto que será mostrado na Treeview para essa turma, 
            # incluindo o nome da turma e sua média, formatada com duas casas decimais.
    texto_turma = f"{turma} (Média: {media_turma:.2f})"
    
    # Insere um novo item na Treeview com o texto da turma. 'end' 
            # indica que o item será inserido ao final da lista de 
            # itens já existentes.
    # 'open=False' especifica que os subitens desse item não 
            # serão mostrados expandidos inicialmente.
    turma_id = arvore.insert('', 
                             'end', 
                             text=texto_turma, open=False)
    
    # Dentro de cada grupo de turma, itera sobre cada aluno. '_,' 
            # ignora o índice enquanto 'aluno' contém os dados do aluno.
    for _, aluno in grupo.iterrows():
        
        # Insere cada aluno como um subitem do item da turma na 
                # Treeview. O nome do aluno é mostrado ligeiramente indentado.
        # 'values=(aluno['Nome'],)' define que o nome do aluno será 
                # armazenado em um formato que permite futuras 
                # manipulações ou referências.
        arvore.insert(turma_id, 
                      'end', 
                      text=f"{aluno['Nome']}", values=(aluno['Nome'],))


# Cria um container chamado 'frame_info' dentro da janela principal 
        # para organizar visualmente os elementos gráficos 
        # relacionados às informações do aluno.
frame_info = tk.Frame(janela_principal)

# Posiciona o 'frame_info' no lado esquerdo da janela principal. 
# 'fill='both'' faz com que o frame expanda tanto vertical 
        # quanto horizontalmente.
# 'expand=True' permite que o frame expanda para ocupar qualquer 
        # espaço extra disponível na janela. 
# 'padx=10' e 'pady=10' adicionam um espaçamento interno 
        # de 10 pixels em todas as direções.
frame_info.pack(side='left', 
                fill='both', 
                expand=True, 
                padx=10, 
                pady=10)

# Cria um rótulo (etiqueta) dentro do 'frame_info' 
        # que contém o texto "Nome:".
# 'font=fonte_padrao' aplica a fonte previamente 
        # definida ao texto do rótulo.
# O método 'grid' é usado para posicionar o rótulo na 
        # primeira linha (row=0) e primeira coluna (column=0) 
        # do grid no frame.
# 'sticky=tk.W' alinha o rótulo à esquerda (West) 
        # dentro da célula do grid.
tk.Label(frame_info, 
         text="Nome:", 
         font=fonte_padrao).grid(row=0, column=0, sticky=tk.W)

# Cria um campo de entrada para inserção de texto, 
        # chamado 'entrada_nome', dentro do 'frame_info'.
# 'width=30' define a largura do campo de entrada, 
        # permitindo que ele contenha aproximadamente 30 caracteres.
# 'font=fonte_padrao' aplica a mesma fonte definida 
        # anteriormente ao texto dentro do campo de entrada.
entrada_nome = tk.Entry(frame_info,
                        width=30, 
                        font=fonte_padrao)

# O campo de entrada é posicionado ao lado do rótulo "Nome:" usando o método 'grid'.
# É posicionado na primeira linha (row=0) e segunda coluna (column=1).
# 'padx=5' e 'pady=5' adicionam um espaçamento de 5 pixels 
        # em torno do campo de entrada para evitar que os 
        # elementos gráficos fiquem muito juntos.
entrada_nome.grid(row=0, 
                  column=1, 
                  padx=5, 
                  pady=5)


# Cria um rótulo (label) dentro do 'frame_info', que é o 
        # frame que contém as informações do aluno.
# Este rótulo é para o campo "Nota 1:".
# 'font=fonte_padrao' aplica a fonte padrão previamente definida 
        # ao texto do rótulo, mantendo a consistência visual da interface.
# O método 'grid' posiciona o rótulo na segunda linha (row=1) e na 
        # primeira coluna (column=0) do layout de grade do frame.
# 'sticky=tk.W' alinha o texto do rótulo à esquerda (West) 
        # dentro de sua célula no layout de grade.
tk.Label(frame_info, 
         text="Nota 1:", 
         font=fonte_padrao).grid(row=1, column=0, sticky=tk.W)

# Cria um campo de entrada (Entry) para que o usuário possa 
        # digitar a primeira nota do aluno.
# Este campo é chamado 'entrada_nota1'.
# 'width=10' define a largura do campo de entrada para 10 
        # caracteres, o que é suficiente para a maioria das notas.
# 'font=fonte_padrao' aplica a mesma fonte definida anteriormente ao 
        # texto dentro do campo de entrada, mantendo a consistência visual.
entrada_nota1 = tk.Entry(frame_info, 
                         width=10, 
                         font=fonte_padrao)

# O método 'grid' é usado para posicionar o campo de 
        # entrada ao lado do rótulo "Nota 1:".
# É posicionado na segunda linha (row=1) e na segunda coluna (column=1).
# 'padx=5' e 'pady=5' adicionam um espaçamento de 5 pixels ao 
        # redor do campo de entrada, evitando que os elementos 
        # gráficos fiquem muito próximos e melhorando a estética.
entrada_nota1.grid(row=1, column=1, padx=5, pady=5)


# Cria um rótulo (label) dentro do 'frame_info', o qual contém 
        # as informações do aluno.
# Este rótulo é especificamente para o campo "Nota 2:".
# 'font=fonte_padrao' é utilizado para aplicar a fonte definida 
        # previamente, garantindo consistência na apresentação 
        # visual de toda a interface.
# O método 'grid' é utilizado para posicionar o rótulo na 
        # terceira linha (row=2) e na primeira coluna (column=0) 
        # do layout em grade no frame.
# 'sticky=tk.W' faz com que o texto do rótulo alinhe à 
        # esquerda (West) dentro da célula no layout em grade, 
        # garantindo clareza e boa organização visual.
tk.Label(frame_info, 
         text="Nota 2:", 
         font=fonte_padrao).grid(row=2, column=0, sticky=tk.W)

# Cria um campo de entrada (Entry), nomeado 'entrada_nota2', 
        # onde o usuário pode digitar a segunda nota do aluno.
# 'width=10' especifica que o campo de entrada deve ter largura 
        # suficiente para acomodar até 10 caracteres, adequado para a 
        # maioria dos formatos de notas.
# 'font=fonte_padrao' aplica a fonte padrão ao texto dentro do 
        # campo de entrada, mantendo a uniformidade com outros 
        # elementos da interface.
entrada_nota2 = tk.Entry(frame_info, 
                         width=10, 
                         font=fonte_padrao)

# Utiliza o método 'grid' para posicionar este campo de 
        # entrada ao lado do rótulo "Nota 2:".
# Posicionado na terceira linha (row=2) e segunda coluna (column=1).
# 'padx=5' e 'pady=5' adicionam espaçamentos de 5 pixels em 
        # torno do campo, evitando que os elementos fiquem 
        # muito apertados e melhorando a estética e usabilidade.
entrada_nota2.grid(row=2, 
                   column=1, 
                   padx=5, 
                   pady=5)


# Cria um rótulo (label) dentro do 'frame_info', que é o 
        # painel usado para agrupar as informações do aluno na interface.
# Este rótulo é destinado ao campo "Nota 3:".
# 'font=fonte_padrao' aplica a fonte definida anteriormente 
        # para manter a uniformidade visual em toda a interface.
# O método 'grid' posiciona o rótulo na quarta linha (row=3) e na 
        # primeira coluna (column=0) do layout de grade do painel.
# 'sticky=tk.W' alinha o texto do rótulo à esquerda (West), garantindo 
        # que a etiqueta seja facilmente associada ao campo de entrada ao lado.
tk.Label(frame_info, text="Nota 3:", 
         font=fonte_padrao).grid(row=3, column=0, sticky=tk.W)

# Cria um campo de entrada (Entry), chamado 'entrada_nota3', 
        # que permite ao usuário digitar a terceira nota do aluno.
# 'width=10' define que o campo de entrada acomodará até 10 
        # caracteres, que é adequado para a maioria dos formatos de notas.
# 'font=fonte_padrao' garante que o texto dentro do campo de 
        # entrada esteja visualmente alinhado com o restante dos elementos na interface.
entrada_nota3 = tk.Entry(frame_info, 
                         width=10, 
                         font=fonte_padrao)

# O método 'grid' é usado para posicionar o campo de entrada 
        # ao lado do rótulo "Nota 3:", facilitando a associação visual entre eles.
# É colocado na quarta linha (row=3) e segunda coluna (column=1).
# 'padx=5' e 'pady=5' adicionam espaçamento de 5 pixels ao redor 
        # do campo de entrada, evitando que os elementos gráficos 
        # fiquem muito próximos e melhorando a usabilidade.
entrada_nota3.grid(row=3, column=1, padx=5, pady=5)


# Cria um rótulo (label) dentro do painel 'frame_info', 
        # que organiza visualmente as informações do aluno.
# Este rótulo é especificamente para o campo "Nota 4:".
# 'font=fonte_padrao' utiliza a fonte padrão definida para 
        # toda a interface, mantendo a consistência visual.
# O método 'grid' é usado para posicionar o rótulo na quinta 
        # linha (row=4) e na primeira coluna (column=0) dentro 
        # do layout de grade do painel.
# 'sticky=tk.W' faz com que o texto do rótulo alinhe à 
        # esquerda (West), o que ajuda a identificar 
        # claramente o campo ao qual o rótulo se refere.
tk.Label(frame_info, 
         text="Nota 4:", 
         font=fonte_padrao).grid(row=4, column=0, sticky=tk.W)

# Cria um campo de entrada (Entry) chamado 'entrada_nota4', 
        # onde o usuário pode inserir a quarta nota do aluno.
# 'width=10' estabelece que o campo de entrada suporta até 
        # 10 caracteres, adequado para digitar notas.
# 'font=fonte_padrao' aplica a mesma fonte dos outros elementos 
        # da interface, assegurando uniformidade.
entrada_nota4 = tk.Entry(frame_info, 
                         width=10, 
                         font=fonte_padrao)

# Utiliza o método 'grid' para alinhar este campo de 
        # entrada ao lado do seu correspondente rótulo "Nota 4:".
# É posicionado na quinta linha (row=4) e na segunda coluna (column=1).
# 'padx=5' e 'pady=5' adicionam um espaçamento de 5 pixels em 
        # torno do campo, proporcionando uma margem suficiente 
        # para facilitar a interação do usuário.
entrada_nota4.grid(row=4, column=1, padx=5, pady=5)


# Cria um rótulo (label) dentro do painel 'frame_info', 
        # destinado a organizar as informações do aluno.
# Este rótulo é para o campo "Média:".
# 'font=fonte_padrao' usa a fonte padrão previamente definida, 
        # garantindo que a aparência do texto seja consistente 
        # com o restante da interface.
# O método 'grid' posiciona o rótulo na sexta linha (row=5) e 
        # na primeira coluna (column=0) do layout de grade.
# 'sticky=tk.W' alinha o texto do rótulo à esquerda (West), 
        # assegurando que ele seja facilmente legível e claramente 
        # associado ao campo de entrada ao lado.
tk.Label(frame_info, 
         text="Média:", 
         font=fonte_padrao).grid(row=5, column=0, sticky=tk.W)

# Cria um campo de entrada (Entry) chamado 'entrada_media', 
        # onde o usuário pode visualizar ou inserir a média 
        # calculada das notas do aluno.
# 'width=10' define a largura do campo para acomodar até 10 
        # caracteres, o que é adequado para mostrar valores 
        # numéricos formatados, como a média.
# 'font=fonte_padrao' aplica a mesma fonte usada nos outros 
        # campos de entrada, mantendo a uniformidade 
        # visual da interface.
entrada_media = tk.Entry(frame_info, 
                         width=10, 
                         font=fonte_padrao)

# O método 'grid' é usado para posicionar este campo de 
        # entrada na sexta linha (row=5) e segunda 
        # coluna (column=1) ao lado do rótulo "Média:".
# 'padx=5' e 'pady=5' adicionam espaçamento em torno do 
        # campo de entrada, proporcionando uma margem que 
        # separa visualmente este campo dos outros, facilitando a interação.
entrada_media.grid(row=5, 
                   column=1, 
                   padx=5, 
                   pady=5)


# Cria um rótulo (label) dentro do painel 'frame_info', 
        # que é usado para organizar as informações do aluno.
# Este rótulo é para o campo "Situação:".
# 'font=fonte_padrao' aplica a fonte padrão definida anteriormente, 
        # garantindo que o texto seja consistente visualmente 
        # com os outros elementos da interface.
# O método 'grid' é usado para posicionar o rótulo na 
        # sétima linha (row=6) e na primeira coluna (column=0) 
        # do layout de grade.
# 'sticky=tk.W' alinha o texto do rótulo à esquerda (West), 
        # facilitando a associação visual clara com o campo 
        # de entrada correspondente ao lado.
tk.Label(frame_info, 
         text="Situação:", 
         font=fonte_padrao).grid(row=6, column=0, sticky=tk.W)

# Cria um campo de entrada (Entry), denominado 'entrada_situacao', 
        # onde o usuário pode visualizar ou editar a situação do 
        # aluno (aprovado, recuperação, reprovado).
# 'width=15' oferece espaço suficiente para acomodar as 
        # palavras que descrevem a situação do aluno sem cortes.
# 'font=fonte_padrao' é usado para manter a consistência 
        # da fonte com os outros campos da interface.
entrada_situacao = tk.Entry(frame_info, 
                            width=15, 
                            font=fonte_padrao)

# Utiliza o método 'grid' para alinhar este campo de 
        # entrada na sétima linha (row=6) e segunda 
        # coluna (column=1), ao lado do rótulo "Situação:".
# 'padx=5' e 'pady=5' adicionam um espaçamento adequado ao 
        # redor do campo de entrada, melhorando a estética e 
        # facilitando a interação.
entrada_situacao.grid(row=6, 
                      column=1, 
                      padx=5, 
                      pady=5)

# Vincula um evento à Treeview chamada 'arvore'. O evento é 
        # disparado quando um item é selecionado pelo usuário.
# "<<TreeviewSelect>>" é o tipo de evento que ocorre quando a 
        # seleção muda na Treeview.
# 'exibir_informacoes_aluno' é a função que é chamada quando o evento ocorre, 
        # responsável por atualizar os campos de entrada com as 
        # informações do aluno selecionado.
arvore.bind("<<TreeviewSelect>>", exibir_informacoes_aluno)

# Iniciar o loop da interface
janela_principal.mainloop()