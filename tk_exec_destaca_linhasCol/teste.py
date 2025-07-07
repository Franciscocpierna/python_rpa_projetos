import tkinter as tk
import pandas as pd

# Janela principal
janela = tk.Tk()
janela.title("Tabela Interativa com Dados de Excel")
# def destacar_celula(event):
#     print("Destacar célula")
# def restaurar_celula(event):
#     print("Destacar célula")
def exportar_para_excel():
     print("Exportar para Excel")    
    
df = pd.read_excel("tabela_exemplo.xlsx")    
# ...código anterior...
colunas = len(df.columns)

# 'len(df.columns)' conta o número total de 
        # colunas no DataFrame 'df'.
linhas = len(df)
# Inicia uma lista vazia chamada 'cabecalho' para armazenar 
# referências aos widgets de cabeçalho de coluna.
cabecalho = []

# Criação dos cabeçalhos (linha de títulos das colunas)
for j in range(colunas):
    celula_cabecalho = tk.Label(janela,
                                text="",           # <-- sem dados
                                bg="lightblue",
                                fg="black",
                                width=12, height=2,
                                borderwidth=1, relief="solid",
                                font=("Arial", 12, "bold"))
    celula_cabecalho.grid(row=2, column=j, sticky="nsew")
    cabecalho.append(celula_cabecalho)

# Inicia uma lista vazia chamada 'tabela' que irá armazenar todas as linhas da tabela
tabela = []

# Criação das células da tabela (sem dados)
for i in range(linhas):
    linha = []
    for j in range(colunas):
        celula = tk.Label(janela,
                          text="",           # <-- sem dados
                          bg="white",
                          fg="black",
                          width=12, height=3,
                          borderwidth=1, relief="solid",
                          font=("Arial", 10))
        celula.grid(row=i+3, column=j, sticky="nsew")
        #celula.bind("<Enter>", destacar_celula)
        #celula.bind("<Leave>", restaurar_celula)
        linha.append(celula)
    tabela.append(linha)

# Configuração do redimensionamento das colunas e linhas
for j in range(colunas):
    janela.grid_columnconfigure(j, weight=1)
for i in range(linhas):
    janela.grid_rowconfigure(i+3, weight=1)
    

btn_exportar = tk.Button(janela, 
                         
                         # 'text="Exportar para Excel"' define o texto que será 
                                 # exibido no botão, orientando o usuário 
                                 # sobre sua funcionalidade.
                         text="Exportar para Excel", 
                         
                         # 'command=exportar_para_excel' vincula o botão à função 
                                 # 'exportar_para_excel', que será chamada quando o 
                                 # botão for clicado.
                         command=exportar_para_excel, 
                         
                         # 'font=("Arial", 12)' define a fonte do texto no 
                                 # botão para Arial, tamanho 12.
                         font=("Arial", 12))

# Posiciona o botão na janela principal usando o 
        # gerenciador de layout 'grid'.
btn_exportar.grid(row=1, 
                  
                  # 'row=1' posiciona o botão na mesma linha que o 
                          # campo de entrada de filtro.
                  column=4, 
                  
                  # 'column=4' coloca o botão na quinta coluna.
                  padx=5, 
                  
                  # 'padx=5' adiciona um espaço horizontal de 5 
                          # pixels à esquerda e à direita do botão.
                  pady=5)
                  # 'pady=5' adiciona um espaço vertical de 5 pixels 
                            # acima e abaixo do botão.

    
entrada_filtro = tk.Entry(janela, 
                          
                          # 'font=("Arial", 12)' configura a fonte do 
                                  # texto dentro da entrada. "Arial" é o 
                                  # tipo de fonte e 12 é o tamanho.
                          font=("Arial", 12))

# Posiciona o campo de entrada na janela principal usando o 
        # gerenciador de layout 'grid'.
        
titulo = tk.Label(janela, 
                  
                  # 'text="Tabela de Informações"' define o texto que 
                          # será exibido no rótulo, servindo como título da tabela.
                  text="Tabela de Informações", 
                  
                  # 'font=("Arial", 16, "bold")' configura a fonte do 
                          # texto no rótulo. "Arial" é o tipo de fonte,
                          # 16 é o tamanho da fonte, e "bold" indica que o 
                          # texto será em negrito.
                  font=("Arial", 16, "bold"))

# Posiciona o rótulo do título na janela principal usando o 
        # gerenciador de layout 'grid'.
titulo.grid(row=0, 
            
            # 'row=0' posiciona o rótulo na primeira linha da grade.
            column=0, 
            
            # 'column=0' posiciona o rótulo na primeira coluna.
            columnspan=5, 
            
            # 'columnspan=5' faz com que o rótulo se estenda por cinco 
                    # colunas, garantindo que ele ocupe a largura 
                    # necessária para ser visível.
            pady=10)
            # 'pady=10' adiciona um espaço vertical de 10 pixels acima e 
                    # abaixo do título para separá-lo visualmente dos 
                    # outros elementos da interface.
        
entrada_filtro.grid(row=1, 
                    
                    # 'row=1' posiciona o campo de entrada na 
                            # segunda linha da grade.
                    column=0, 
                    
                    # 'column=0' posiciona o campo na primeira coluna.
                    columnspan=4, 
                    
                    # 'columnspan=4' faz com que o campo de entrada 
                            # se estenda por quatro colunas.
                    padx=5, 
                    
                    # 'padx=5' adiciona um espaço horizontal de 5 pixels à 
                            # esquerda e à direita do campo de entrada.
                    pady=5, 
                    
                    # 'pady=5' adiciona um espaço vertical de 5 pixels 
                            # acima e abaixo do campo de entrada.
                    sticky="ew")
                    # 'sticky="ew"' faz com que o campo de entrada se estique 
                            # para preencher toda a largura disponível, garantindo 
                            # que use todo o espaço horizontal das colunas que ocupa.
# ...código posterior...
janela.mainloop()


