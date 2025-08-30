from __future__ import print_function
from tkinter import *
from tkinter import ttk


import os.path


import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1UJdjzs3GUhbjmi54NUcVDkJ1zig6gqj2h42oOmc7NyM'
SAMPLE_RANGE_NAME = 'Dados!A1:E'

CREDENTIALS_FILE = 'token.json'

#https://docs.google.com/spreadsheets/d/1UJdjzs3GUhbjmi54NUcVDkJ1zig6gqj2h42oOmc7NyM/edit?usp=sharing

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(r'C:\python_projetos\google_sheets\token.json'):
        creds = Credentials.from_authorized_user_file(r'C:\python_projetos\google_sheets\token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                r'C:\python_projetos\google_sheets\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(r'C:\python_projetos\google_sheets\token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                  range=SAMPLE_RANGE_NAME).execute()
        
        #Lê os dados da planilha do google sheets
        valores = result.get('values', [])
        
              
        #Criando a janela do Tkinter
        root = Tk()
        root.configure(bg='white') #Cor do fundo
        root.title("Sistema Google Sheets")
        
        #----------------------------------
        #Cria o rótulo para exibir na tela
        estado_label = Label(root, text="Estado:", font="Arial 14", bg='white')
        estado_label.grid(row=0, column=0, padx=2, pady=2, stick="W")
        
        #Pega as informações da coluna A a partir da segunda linha
        estados = sorted(list(set(value[0] for value in valores[1:] )))
        
        #Cria a combobox
        estado_combobox = ttk.Combobox(root, values=estados, font="Arial 14")
        estado_combobox.grid(row=1, column=0, padx=2, pady=2, stick="W")
        
        #----------------------------------
        #Cria o rótulo para exibir na tela
        cidade_label = Label(root, text="Cidade:", font="Arial 14", bg='white')
        cidade_label.grid(row=0, column=1, padx=2, pady=2, stick="W")
        
        #Pega as informações da coluna B a partir da segunda linha
        cidades = sorted(list(set(value[1] for value in valores[1:] )))
        
        #Cria a combobox
        cidade_combobox = ttk.Combobox(root, values=cidades, font="Arial 14")
        cidade_combobox.grid(row=1, column=1, padx=2, pady=2, stick="W")
        
        #----------------------------------
        #Cria o rótulo para exibir na tela
        vendedor_label = Label(root, text="Vendedor:", font="Arial 14", bg='white')
        vendedor_label.grid(row=0, column=2, padx=2, pady=2, stick="W")
        
        #Pega as informações da coluna C a partir da segunda linha
        vendedores = sorted(list(set(value[2] for value in valores[1:] )))
        
        #Cria a combobox
        vendedor_combobox = ttk.Combobox(root, values=vendedores, font="Arial 14")
        vendedor_combobox.grid(row=1, column=2, padx=2, pady=2, stick="W")
        
        #----------------------------------
        #Cria o rótulo para exibir na tela
        produto_label = Label(root, text="Produto:", font="Arial 14", bg='white')
        produto_label.grid(row=0, column=3, padx=2, pady=2, stick="W")
        
        #Pega as informações da coluna D a partir da segunda linha
        produtos = sorted(list(set(value[3] for value in valores[1:] )))
        
        #Cria a combobox
        produtos_combobox = ttk.Combobox(root, values=produtos, font="Arial 14")
        produtos_combobox.grid(row=1, column=3, padx=2, pady=2, stick="W")
        
        #Cria uma treeview para exibir os dados da planilha
        tree = ttk.Treeview(root)
                
        #Define as colunas da Treeview com base nos valores da linha 1 da planilha
        colunas = valores[0]
        tree["columns"] = colunas
        
        #for - para
        #Define o cabeçalho da Treeview
        for linha in colunas:
            tree.heading(linha, text=linha)
        
        #Adiciona os valores da planilha à Treeview
        for row in valores[1:]:
            tree.insert("", "end", values=row)
            
        #row - linha
        #column - coluna
        #columnspan - Quantas colunas da tela vai oculpar
        #padx - Espaço entre as laterais da linha
        #pady - Espaço em cima e embaixo
        #stick - Remove os espaços em branco - NSEW (Norte, Sul, Leste e Oeste)
        #Exibe a Treeview
        #grid - A tela dividida em pequena parte como se fosse uma planilha
        tree.grid(row=3, column=0, columnspan=6, padx=5, pady=5, stick="NSEW")
        
        style = ttk.Style()
        style.theme_use("clam") #Definindo o tema para a treeview
        style.configure("Treeview", background="#FFFFE0", foreground="black",
                       font=("Arial 12"), rowheight=25, fiedlbackground="#FFFFE0",
                            bordercolor="#808080", borderwidth=1) #Define as cores, fundo, cor do texto, altura da linha, cor do campo, cor e larrgura da borda
        style.map("Treeview", background=[('selected', "#347083")], foreground=[('selected', 'white')]) #Define a cor de fundo e texto quando uma linha é selecionada
        
        #Oculta a primeira coluna deixando a largura como 0
        tree.column("#0", width=0, stretch=False)
        
        
        #Função que filtra os dados
        def filtro():
            
            #Lê as informações da planilha
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                      range=SAMPLE_RANGE_NAME).execute()

            #Lê os dados da planilha do google sheets
            valores = result['values']
            
            #Opçoes filtro pega o texto das combobox
            estado = estado_combobox.get()
            cidade = cidade_combobox.get()
            vendedor = vendedor_combobox.get()
            produto = produtos_combobox.get()
            
            dados_filtrados = [valores[0]] #Inclui a linha do cabeçalho
            for row in valores[1:]:
                
                if(not estado or row[0] == estado) and \
                    (not cidade or row[1] == cidade) and \
                    (not vendedor or row[2] == vendedor) and \
                    (not produto or row[3] == produto) and \
                    (not estado or row[0] == estado) :
                    dados_filtrados.append(row)
            
            #Limpa os dados
            for row in tree.get_children():
                tree.delete(row)
                
            #Atualiza os dados da treeview
            for row in dados_filtrados[1:]:
                tree.insert("", "end", values=row) 
                
            #Chama a função que lê os dados da treeview e soma os preço e qtd de linhas
            soma_precos()
                
        #Cria botão Filtro
        botao_filtrar = Button(root, text="Filtrar", font="Arial 14", command=filtro)
        botao_filtrar.grid(row=4, column=1, padx=2, pady=2, stick="NSEW") 
        
        def atualiza_cidades(event):
        
            #Obtem o estado selecionado
            estado = estado_combobox.get()
            
            #Pega as informações da coluna B a partir da segunda linha
            cidades = sorted(list(set([value[1] for value in valores[1:] if value[0] == estado])))
            
            #Popula a combobox com os valores correspondentes
            cidade_combobox['values'] = cidades
            
            #Chamo a função para filtrar os dados
            filtro()
            
            #Chama a função que lê os dados da treeview e soma os preço e qtd de linhas
            soma_precos()
        
        #Adiciona o evento a bombobox
        estado_combobox.bind("<<ComboboxSelected>>", atualiza_cidades)  
        
        #-----------------------------------------------
        
        def atualiza_vendedores(event):
        
            #Obtem o estado selecionado
            cidade = cidade_combobox.get()
            
            #Pega as informações da coluna C a partir da segunda linha
            vendedores = sorted(list(set([value[2] for value in valores[1:] if value[1] == cidade])))
            
            #Popula a combobox com os valores correspondentes
            vendedor_combobox['values'] = vendedores
            
            #Chamo a função para filtrar os dados
            filtro()
            
            #Chama a função que lê os dados da treeview e soma os preço e qtd de linhas
            soma_precos()
        
        #Adiciona o evento a bombobox
        cidade_combobox.bind("<<ComboboxSelected>>", atualiza_vendedores)  
        
        #-----------------------------------------------
        
        def atualiza_produtos(event):
        
            #Obtem o estado selecionado
            vendedor = vendedor_combobox.get()
            
            #Pega as informações da coluna D a partir da segunda linha
            produtos = sorted(list(set([value[3] for value in valores[1:] if value[2] == vendedor])))
            
            #Popula a combobox com os valores correspondentes
            produtos_combobox['values'] = produtos
            
            #Chamo a função para filtrar os dados
            filtro()
            
            #Chama a função que lê os dados da treeview e soma os preço e qtd de linhas
            soma_precos()
        
        #Adiciona o evento a bombobox
        vendedor_combobox.bind("<<ComboboxSelected>>", atualiza_produtos)  
        
        #-----------------------------------------------
        
        def chama_filtro_a_cada_mudanca(event):
            
            filtro()
            
            #Chama a função que lê os dados da treeview e soma os preço e qtd de linhas
            soma_precos()
        
        #Filtro as informações quando selecionar algo no campo de produtos
        produtos_combobox.bind("<<ComboboxSelected>>", chama_filtro_a_cada_mudanca)
            
        def novo_registro():
            
            #Cria uma janela secundária para cadastrar os dados
            janela_cadastro = Toplevel(root)
            janela_cadastro.title("Cadastrar Produto")
            
            Label(janela_cadastro, text="Estado:", font="Arial 16").grid(row=0, column=0, padx=2, pady=2) 
            estado_cadastro = Entry(janela_cadastro, font="Arial 16") #Campo de entrada de dados que pega o que o usuário digitar
            estado_cadastro.grid(row=0, column=1, padx=2, pady=2) 
            
            Label(janela_cadastro, text="Cidade:", font="Arial 16").grid(row=1, column=0, padx=2, pady=2) 
            cidade_cadastro = Entry(janela_cadastro, font="Arial 16") #Campo de entrada de dados que pega o que o usuário digitar
            cidade_cadastro.grid(row=1, column=1, padx=2, pady=2) 
            
            Label(janela_cadastro, text="Vendedor:", font="Arial 16").grid(row=2, column=0, padx=2, pady=2) 
            vendedor_cadastro = Entry(janela_cadastro, font="Arial 16") #Campo de entrada de dados que pega o que o usuário digitar
            vendedor_cadastro.grid(row=2, column=1, padx=2, pady=2) 
            
            Label(janela_cadastro, text="Produto:", font="Arial 16").grid(row=3, column=0, padx=2, pady=2) 
            produto_cadastro = Entry(janela_cadastro, font="Arial 16") #Campo de entrada de dados que pega o que o usuário digitar
            produto_cadastro.grid(row=3, column=1, padx=2, pady=2) 
            
            Label(janela_cadastro, text="Preço:", font="Arial 16").grid(row=4, column=0, padx=2, pady=2) 
            preco_cadastro = Entry(janela_cadastro, font="Arial 16") #Campo de entrada de dados que pega o que o usuário digitar
            preco_cadastro.grid(row=4, column=1, padx=2, pady=2) 
            
            def salvar_dados_google_sheets():
                
                #Obtem os valores dos campos de entrada de dados
                estado = estado_cadastro.get()
                cidade = cidade_cadastro.get()
                vendedor = vendedor_cadastro.get()
                produto = produto_cadastro.get()
                preco = preco_cadastro.get()
                
                creds = None
                if os.path.exists(CREDENTIALS_FILE): #Verifica se o arquivo de credenciais exsite
                    creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE, SCOPES) #Carrega as credenciais a partir do arquuivo
                    
                if not creds or not creds.valid: #Verifica se as credenciais são inválidas ou inexistes
                    if creds and creds.expired and creds.reflesh_token: #Verifica se as credenciais expiraram e existe um token de atualização
                        creds.refresh(Request()) #Atualiza as credenciais com o token de atualização
                    else:
                        
                        #Se não houver credenciais ou elas forem inválidas abre o fluxo de autenticação do Google Sheets
                        flow = InstalledAppFlow.from_client_secrets_file(                        
                            'credentials.json', SCOPES)
                        creds = flow.run_local_server(port=0) #Executa o fluxo de autenticação
                        
                    with open(CREDENTIALS_FILE, 'w') as token: #Abre o arquivo de credenciais para escrita
                        token.write(creds.to_json()) #Escreve as credenciais no arquivo
                        
                #Cria uma instancia da API da planilha do Google
                service = build('sheets', 'v4', credentials=creds)
                
                values = [[estado, cidade, vendedor, produto, preco]] #Cria uma lista com os valores obtidos dos campos de entrada
                
                body = {'values': values} #Cria um dicionário com a lista de valores

                # Call the Sheets API
                result = service.spreadsheets().values().append(
                                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME,
                                valueInputOption='USER_ENTERED', insertDataOption='INSERT_ROWS', body=body).execute()
                                #Executa o método append para adicionar uma nova linha à planilha do Google Sheets
            
                tree.delete(*tree.get_children()) #Remove todas as linhas da Treeview
                result = service.spreadsheets().values().get(
                            spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute() #Executa o método get() para obter os dados da planilha
                
                valores = result['values'] #Obtem os valores da planilha em formato de lista
                for row in valores[1:]:
                    tree.insert("", "end", values=row)
                    
                #Fecha a janela de cadastro
                janela_cadastro.destroy()
                    
                #Chama a função que lê os dados da treeview e soma os preço e qtd de linhas
                soma_precos()
                
            #Cria botão Filtro
            botao_salvar_novo_registro = Button(janela_cadastro, text="Cadastrar", font="Arial 16", command=salvar_dados_google_sheets)
            botao_salvar_novo_registro.grid(row=6, column=0, columnspan=2, padx=2, pady=2, stick="NSEW")
            
        #Cria botão Filtro
        botao_novo = Button(root, text="Novo", font="Arial 14", command=novo_registro)
        botao_novo.grid(row=4, column=0, padx=2, pady=2, stick="NSEW") 
        
        #------------------------------------------------------------------------------
        
        def janela_editar(event):
            
            #Obtem o item selecionado da treeview
            item_selecionado = tree.selection()[0]
            
            #Obtem os valores do item selecionado
            valores_selecionados = tree.item(item_selecionado)['values']
            
            #Cria uma janela secundária para cadastrar os dados
            janela_edicao = Toplevel(root)
            janela_edicao.title("Editar Produto")
            
            Label(janela_edicao, text="Estado:", font="Arial 16").grid(row=0, column=0, padx=2, pady=2) 
            estado_edicao = Entry(janela_edicao, font="Arial 16", textvariable=StringVar(value=valores_selecionados[0])) #Campo de entrada de dados que pega o que o usuário digitar
            estado_edicao.grid(row=0, column=1, padx=2, pady=2) 
            
            Label(janela_edicao, text="Cidade:", font="Arial 16").grid(row=1, column=0, padx=2, pady=2) 
            cidade_edicao = Entry(janela_edicao, font="Arial 16", textvariable=StringVar(value=valores_selecionados[1])) #Campo de entrada de dados que pega o que o usuário digitar
            cidade_edicao.grid(row=1, column=1, padx=2, pady=2) 
            
            Label(janela_edicao, text="Vendedor:", font="Arial 16").grid(row=2, column=0, padx=2, pady=2) 
            vendedor_edicao = Entry(janela_edicao, font="Arial 16", textvariable=StringVar(value=valores_selecionados[2])) #Campo de entrada de dados que pega o que o usuário digitar
            vendedor_edicao.grid(row=2, column=1, padx=2, pady=2) 
            
            Label(janela_edicao, text="Produto:", font="Arial 16").grid(row=3, column=0, padx=2, pady=2) 
            produto_edicao = Entry(janela_edicao, font="Arial 16", textvariable=StringVar(value=valores_selecionados[3])) #Campo de entrada de dados que pega o que o usuário digitar
            produto_edicao.grid(row=3, column=1, padx=2, pady=2) 
            
            Label(janela_edicao, text="Preço:", font="Arial 16").grid(row=4, column=0, padx=2, pady=2) 
            preco_edicao = Entry(janela_edicao, font="Arial 16", textvariable=StringVar(value=valores_selecionados[4])) #Campo de entrada de dados que pega o que o usuário digitar
            preco_edicao.grid(row=4, column=1, padx=2, pady=2) 
            
            def alterar_dados_google_sheets():
                
                #Obtem os valores dos campos de entrada de dados
                estado = estado_edicao.get()
                cidade = cidade_edicao.get()
                vendedor = vendedor_edicao.get()
                produto = produto_edicao.get()
                preco = preco_edicao.get()
                
                #Lê as credenciais do usuário ou pede autorização para acessar a planilha do Google Sheets
                creds = None
                if os.path.exists('token.json'): #Verifica se o arquivo de credenciais exsite
                    creds = Credentials.from_authorized_user_file('token.json', SCOPES) #Carrega as credenciais a partir do arquuivo
                    
                if not creds or not creds.valid: #Verifica se as credenciais são inválidas ou inexistes
                    if creds and creds.expired and creds.reflesh_token: #Verifica se as credenciais expiraram e existe um token de atualização
                        creds.refresh(Request()) #Atualiza as credenciais com o token de atualização
                    else:
                        
                        #Se não houver credenciais ou elas forem inválidas abre o fluxo de autenticação do Google Sheets
                        flow = InstalledAppFlow.from_client_secrets_file(                        
                            'credentials.json', SCOPES)
                        creds = flow.run_local_server(port=0) #Executa o fluxo de autenticação
                        
                    with open('token.json', 'w') as token: #Abre o arquivo de credenciais para escrita
                        token.write(creds.to_json()) #Escreve as credenciais no arquivo
                        
                #Cria uma instancia da API da planilha do Google
                service = build('sheets', 'v4', credentials=creds)
                
                #Quando colo o RAW significa que os dados serão salvos como eles estão
                value_input_option = 'RAW'
                
                values = [
                    [
                        estado,
                        cidade,
                        vendedor,
                        produto,
                        preco
                    ]
                ]
                
                #Converte o indice da linha em uma string / texto
                linha = str(tree.index(item_selecionado) + 2)
                
                #Usa a string format para criar a range que vamos alterar os dados
                range_ = f'Dados!A{linha}:E{linha}'
                
                body = {
                    
                    'values' : values
                    
                }

                # Call the Sheets API
                result = sheet.values().update(
                                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=range_,
                                valueInputOption=value_input_option, body=body).execute()
                                #Executa o método append para adicionar uma nova linha à planilha do Google Sheets
            
                #Atualiza a exibição da Treeview com os novos valores
                tree.item(item_selecionado, values=values[0])
                
                
                #Fecha a janela de edição
                janela_edicao.destroy()
                
                #Chama a função que lê os dados da treeview e soma os preço e qtd de linhas
                soma_precos()
            
                
            #Cria botão Filtro
            botao_alterar_dados = Button(janela_edicao, text="Salvar Alterações", font="Arial 16", command=alterar_dados_google_sheets)
            botao_alterar_dados.grid(row=6, column=0, columnspan=2, padx=2, pady=2, stick="NSEW")
          
        #Evendo de duplo clique na Treeview
        tree.bind("<Double-1>", janela_editar)
           
        def excluir_item():
            
            #Obtem o indice da linha selecionada na Treeview
            item_selecionado = tree.focus()
            index = tree.index(item_selecionado)
            
            #Obtem o ID da planilha e o intervalo da linha que deseja excluir
            spreadsheet_id = SAMPLE_SPREADSHEET_ID
            #range_ = f'Dados!A{index+2}:E{index+2}'
            
            #Cria uma solicitação para remover a linha
            request = {
                "deleteRange":{
                    "range": {
                        "sheetId": 0, #O id da planilha
                        "startRowIndex": index + 1,
                        "endRowIndex": index + 2,
                        "startColumnIndex": 0,
                        "endColumnIndex" : 5
                    },
                    "shiftDimension": "ROWS" #Indica que as célula abaixo devem ser movidas para cima
                    
                }
            }
            
            #Executa a solicitação para remover a linha
            service = build('sheets', 'v4', credentials=creds)
            response = service.spreadsheets().batchUpdate(spreadsheetId = spreadsheet_id, body={
                "requests":[request]
            }).execute()
            
            #Remove o item selecionado da treview
            tree.delete(item_selecionado)
            
            #Chama a função que lê os dados da treeview e soma os preço e qtd de linhas
            soma_precos()
                
        
        #row - linha
        #column - coluna
        #columnspan - Quantas colunas da tela vai oculpar
        #padx - Espaço entre as laterais da linha
        #pady - Espaço em cima e embaixo
        #stick - Remove os espaços em branco - NSEW (Norte, Sul, Leste e Oeste)
        #Exibe a Treeview
        #grid - A tela dividida em pequena partes como se fosse uma planilha
        #Cria botão Deletar
        botao_deletar = Button(root, text="Deletar", font="Arial 14", command=excluir_item)
        botao_deletar.grid(row=4, column=2, padx=2, pady=2, stick="NSEW") 

        
        #Cria o Label que exibe o total da coluna de preço e quantidade de itens na tela
        total_label = Label(root, text="Total: R$ 0", font="Arial 16")
        total_label.grid(row=5, column=0, columnspan=5, padx=2, pady=2, stick="W") 
        
        #Função que soma os preços dos produtos e conta a quantidade de linhas da treeview
        def soma_precos():
            
            #Obtém os indices de todas as linhas
            dados = tree.get_children()
            
            total = 0.0
            qtd_linhas = 0.0
            
            for linha in dados:
                
                valores_linha = tree.item(linha)['values']
                precos = []
                
                for v in valores_linha[4:]:
                    if isinstance(v, str):
                        preco = float(v.replace(',', '.'))
                        precos.append(preco)
                    else:
                        precos.append(v)
                        
                total += sum(precos)
                qtd_linhas += 1
                
            total_label.configure(text="Total: {:,.2f} - Linhas: {:,.0f}". format(total, qtd_linhas))
        
        #Chama a função para exibir o total de preços e quantidade de linha da Treeview
        soma_precos()
        
        import openpyxl
        
        def exportar_para_excel():
            
            #Cria um arquivo de Excel
            pasta_trabalho = openpyxl.Workbook()
            planilha = pasta_trabalho.active
            
            #Escreve os cabeçalhos das colunas
            colunas = [tree.heading(col)["text"] for col in tree["columns"]]
            planilha.append(colunas)
            
            #Escreve os dados das linhas na planilha
            for linha in tree.get_children():
                
                valores = [tree.item(linha)["values"][i] for i in range(len(colunas))]
                planilha.append(valores)
              
            #Salva o arquivo de excel
            pasta_trabalho.save("dados.xlsx")
        
        
        #row - linha
        #column - coluna
        #columnspan - Quantas colunas da tela vai oculpar
        #padx - Espaço entre as laterais da linha
        #pady - Espaço em cima e embaixo
        #stick - Remove os espaços em branco - NSEW (Norte, Sul, Leste e Oeste)
        #Exibe a Treeview
        #grid - A tela dividida em pequena partes como se fosse uma planilha
        #Cria botão Deletar
        botao_exportar = Button(root, text="Exportar", font="Arial 14", command=exportar_para_excel)
        botao_exportar.grid(row=4, column=3, padx=2, pady=2, stick="NSEW")
        
        def exportar_e_separar():
            
            #Cria um dicionário para armazenas as planilhas
            planilhas = {}
            
            #for - para
            #Percorre as linhas da Treeview e adiciona cada linha a planilha correspondente
            for linha in tree.get_children():
                
                #Obtem o valor da coluna A para usar como nome  da planilha
                valor_coluna_a = tree.item(linha)["values"][0]
                
                #Verifica se a planilha já existe no dicionário, senão criar
                if valor_coluna_a not in planilhas:
                    
                    planilhas[valor_coluna_a] = []
                    
                #Adiciona a linha à planilha correspondente
                planilhas[valor_coluna_a].append([str(valor) for valor in tree.item(linha)["values"]])
                
            #Salva cada planilha do dicionario em um arquivo de Excel Separado
            for nome_planilha, linhas in planilhas.items():
              
                #Cria um arquivo de Excel
                pasta_trabalho = openpyxl.Workbook()
                planilha = pasta_trabalho.active
                planilha.title = nome_planilha

                #Escreve os cabeçalhos das colunas
                colunas = [tree.heading(col)["text"] for col in tree["columns"]]
                planilha.append(colunas)

                #Escreve os dados das linhas na planilha
                for linha in linhas:

                    planilha.append(linha)

                #Salva o arquivo de excel
                pasta_trabalho.save(f"{nome_planilha}.xlsx")
        
        
        #row - linha
        #column - coluna
        #columnspan - Quantas colunas da tela vai oculpar
        #padx - Espaço entre as laterais da linha
        #pady - Espaço em cima e embaixo
        #stick - Remove os espaços em branco - NSEW (Norte, Sul, Leste e Oeste)
        #Exibe a Treeview
        #grid - A tela dividida em pequena partes como se fosse uma planilha
        #Cria botão Deletar
        botao_exportar_separar = Button(root, text="Exportar Separar", font="Arial 14", command=exportar_e_separar)
        botao_exportar_separar.grid(row=4, column=4, padx=2, pady=2, stick="NSEW")
        
        #Exibo a tela
        root.mainloop()

        
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()