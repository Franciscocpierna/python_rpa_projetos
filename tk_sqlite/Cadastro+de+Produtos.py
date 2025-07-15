#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importa o modulo pyodbc para conexão com bando de dados
import pyodbc

#Importa o módulo tkinter para construção de interfaces gráficas
from tkinter import *

#Importa a classe ttk do módulo tkinter
from tkinter import ttk

#Função que verifica se as credenciais do usuário estão corretas
def verifica_credenciais():
    
    #Driver - Drive
    #Server - Servidor
    #Database - Nome do Banco de Dados
    conexao = pyodbc.connect("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db")

    #cursor - Ferramenta para exercutar os comandos em SQL
    cursor = conexao.cursor()
    
    #Executando uma query que seleniona os usuários que possuem o nome de usuário e senha inseridos pelo usuário
    cursor.execute("SELECT * FROM Usuarios WHERE Nome = ? AND Senha = ?", (nome_usuario_entry.get(), senha_usuario_entry.get()))
    
    #Recebendo o resultado da query
    usuario = cursor.fetchone()
    
    #if - se
    if usuario:
        
        #Destruindo / Fechando a janela de Login
        janela_principal.destroy()
        
        #Driver - Drive
        #Server - Servidor
        #Database - Nome do Banco de Dados
        dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=Projeto_Compras.db")

        #UID - Login
        #PWD - Senha

        #Criando a conexao
        conexao = pyodbc.connect(dadosConexao)

        #Cria um objeto cursor para executar os comandos SQL no banco de dados
        cursor = conexao.cursor()

        #Executa um comando SQL para selecionar todos os valores da tabela de Produtos
        conexao.execute("Select * From Produtos")

        print("Conectado com sucesso!")

        def listar_dados():

            #Limpa os valores da treeview
            for i in treeview.get_children():        
                treeview.delete(i)

            #Executa um comando SQL para selecionar todos os valores da tabela de Produtos
            cursor.execute("Select * From Produtos")

            #Armazena os valores retornados pelo comando SQL em uma variável
            valores = cursor.fetchall()

            #Adiciona os valores na Treeview
            for valor in valores:

                #Popula linha por linha
                treeview.insert("", "end", values=(valor[0], valor[1], valor[2], valor[3]))

        #Criando uma janela tkinter com o título "Cadastro de Produtos"
        janela = Tk()
        janela.title("Cadastro de Produtos")

        #Definindo a cor de fundo para a janela
        janela.configure(bg="#F5F5F5")

        #Deixando a janela em tela cheia
        janela.attributes("-fullscreen", True)

        Label(janela, text="Nome do Produto: ", font="Arial 16", bg="#F5F5F5").grid(row=0, column=2, padx=10, pady=10)
        nome_produto = Entry(janela, font="Arial 16")
        nome_produto.grid(row=0, column=3, padx=10, pady=10)

        Label(janela, text="Descrição do Produto: ", font="Arial 16", bg="#F5F5F5").grid(row=0, column=5, padx=10, pady=10)
        descricao_produto = Entry(janela, font="Arial 16")
        descricao_produto.grid(row=0, column=6, padx=10, pady=10)

        Label(janela, text="Produtos", font="Arial 16", fg="blue", bg="#F5F5F5").grid(row=2, column=0, columnspan=10, padx=10, pady=10)


        #Função para cadastrar o produto
        def cadastrar():

            #Cria uma nova janela para cadastrar o produto
            janela_cadastrar = Toplevel(janela)
            janela_cadastrar.title("Cadastrar Produto")

            #bg - background (cor do fundo)
            #Definindo a cor de fundo da janela
            janela_cadastrar.configure(bg="#FFFFFF")

            #Define a largura e altura da janela
            largura_janela = 450
            altura_janela = 230

            #Obtem a largura e altura da tela computador
            largura_tela = janela_cadastrar.winfo_screenwidth()
            altura_tela = janela_cadastrar.winfo_screenheight()


            #Calcula a posição da janela para centraliza-la na tela
            """
            Essas linhas calculam a posição em que a janela deve ser
            exibida na tela do computador de forma centralizada. 
            A posição x é definida pela diferença entre a largura da tela
            e a largura da janela, dividida por 2. Já a posição y é definida
            pela diferença entre a altura da tela e a altura da janela, também
            dividida por 2. O operador "//" é utilizado para realizar a divisão
            inteira, ou seja, retornar apenas o resultado inteiro da divisão.
            """
            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            #Define a posição da janela
            """
            define a geometria da janela principal, especificando a 
            largura e altura da janela, bem como a posição onde a janela 
            será exibida na tela, usando as variáveis previamente definidas 
            para a posição x e y da janela. O formato utilizado é uma string 
            que contém os valores de largura, altura, posição x e posição y da 
            janela separados por "x" e "+" e passados ​​como argumentos para o m
            étodo geometry() da janela principal.

            O formato '{}'x'{}'+'{}'+'{}' é uma string de formatação que espera
            quatro valores, que correspondem à largura da janela, altura da janela, 
            posição x da janela e posição y da janela, respectivamente.

            Esses valores são passados na ordem especificada para a string de formatação e, 
            em seguida, são utilizados para definir a geometria da janela através do 
            método geometry do objeto janela_principal.
            """
            janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y ))


            for i in range(5):
                janela_cadastrar.grid_rowconfigure(i, weight=1)


            for i in range(2):
                janela_cadastrar.grid_columnconfigure(i, weight=1)

            #Adiciona bordas para cada campo de entrada
            estilo_borda = {"borderwidth": 2, "relief": "groove"}

            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
            #fg - foreground (cor da letra)
            #row - linha
            #column - coluna
            #pady - espaço
            Label(janela_cadastrar, text="Nome do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, stick="W")
            nome_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
            nome_produto_cadastrar.grid(row=0, column=1, padx=10, pady=10)

            Label(janela_cadastrar, text="Descrição do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, stick="W")
            descricao_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
            descricao_produto_cadastrar.grid(row=1, column=1, padx=10, pady=10)

            Label(janela_cadastrar, text="Preço do Produto:", font=("Arial", 12), bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, stick="W")
            preco_produto_cadastrar = Entry(janela_cadastrar, font=("Arial", 12), **estilo_borda)
            preco_produto_cadastrar.grid(row=2, column=1, padx=10, pady=10)

            #Cria uma função para salvar os dados no banco de dados
            def salvar_dados():

                #Cria uma tupla com os valores dos campos de texto
                novo_produto_cadastrar = (nome_produto_cadastrar.get(), descricao_produto_cadastrar.get(), preco_produto_cadastrar.get())

                #Executa um comando SQL para inserir os dados na tabela Produtos no banco de dados
                cursor.execute("INSERT INTO Produtos (NomeProduto, Descricao, Preco) Values (?, ?, ?)", novo_produto_cadastrar)
                conexao.commit() #Gravando no BD

                print("Dados cadastrados com sucesso!")

                #Fecha a janela de cadastro
                janela_cadastrar.destroy()

                #Chama a função para listar os valores do banco de dados na treeview
                listar_dados()        

            #columnspan - quantas colunas vai ocupar no grid   
            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
            botao_salvar_dados = Button(janela_cadastrar, text="Salvar", font=("Arial", 12), command=salvar_dados)
            botao_salvar_dados.grid(row=3, column=0, columnspan=2, padx=10, pady=10, stick="NSEW")

            #columnspan - quantas colunas vai ocupar no grid   
            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
            botao_cancelar = Button(janela_cadastrar, text="Cancelar", font=("Arial", 12), command=janela_cadastrar.destroy)
            botao_cancelar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, stick="NSEW")

        #Cria um botão para gravar os dados na tabela Produtos do banco de dados
        botao_gravar = Button(janela, text="Novo", command=cadastrar, font="Arial 26")
        botao_gravar.grid(row=4, column=0, columnspan=4, stick="NSEW", padx=20, pady=5)

        #Define o estilo da Treeview
        style = ttk.Style(janela)

        #Criando a Treeview
        treeview = ttk.Treeview(janela, style="mystyle.Treeview")

        style.theme_use("default")

        #Configurando
        style.configure("mystyle.Treeview", font=("Arial", 14))

        treeview = ttk.Treeview(janela, style="mystyle.Treeview", columns=("ID", "NomeProduto", "Descricao", "Preco"), show="headings", height=20)

        treeview.heading("ID", text="ID")
        treeview.heading("NomeProduto", text="Nome do Produto")
        treeview.heading("Descricao", text="Descrição do Produto")
        treeview.heading("Preco", text="Preço do Produto")
        #A primeira coluna, identificada como "#0"
        #A opção "stretch=NO" indica que a coluna não deve esticar para preencher o espaço disponível.
        treeview.column("#0", width=0, stretch=NO)
        treeview.column("ID", width=100)
        treeview.column("NomeProduto", width=300)
        treeview.column("Descricao", width=500)
        treeview.column("Preco", width=200)

        #columnspan - quantas colunas vai ocupar no grid   
        #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
        treeview.grid(row=3, column=0, columnspan=10, stick="NSEW")

        #Chama a função para listar os valores do banco de dados na treeview
        listar_dados()

        def editar_dados(event):

            #Obtém o item selecionado na Treeview
            item_selecionado = treeview.selection()[0]

            #Obtém os valores do item selecionado
            valores_selecionados = treeview.item(item_selecionado)['values']

            #Cria uma nova janela para cadastrar o produto
            janela_edicao = Toplevel(janela)
            janela_edicao.title("Editar Produto")

            #bg - background (cor do fundo)
            #Definindo a cor de fundo da janela
            janela_edicao.configure(bg="#FFFFFF")

            #Define a largura e altura da janela
            largura_janela = 500
            altura_janela = 200

            #Obtem a largura e altura da tela computador
            largura_tela = janela_edicao.winfo_screenwidth()
            altura_tela = janela_edicao.winfo_screenheight()


            #Calcula a posição da janela para centraliza-la na tela
            pos_x = (largura_tela // 2) - (largura_janela // 2)
            pos_y = (altura_tela // 2) - (altura_janela // 2)

            #Define a posição da janela
            janela_edicao.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y ))


            for i in range(5):
                janela_edicao.grid_rowconfigure(i, weight=1)


            for i in range(2):
                janela_edicao.grid_columnconfigure(i, weight=1)

            #Adiciona bordas para cada campo de entrada
            estilo_borda = {"borderwidth": 2, "relief": "groove"}

            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
            #fg - foreground (cor da letra)
            #row - linha
            #column - coluna
            #pady - espaço
            Label(janela_edicao, text="Nome do Produto:", font=("Arial", 16), bg="#FFFFFF").grid(row=0, column=0, padx=10, pady=10, stick="W")
            nome_produto_edicao = Entry(janela_edicao, font=("Arial", 16), **estilo_borda, bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[1]))
            nome_produto_edicao.grid(row=0, column=1, padx=10, pady=10)

            Label(janela_edicao, text="Descrição do Produto:", font=("Arial", 16), bg="#FFFFFF").grid(row=1, column=0, padx=10, pady=10, stick="W")
            descricao_produto_edicao = Entry(janela_edicao, font=("Arial", 16), **estilo_borda, bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[2]))
            descricao_produto_edicao.grid(row=1, column=1, padx=10, pady=10)

            Label(janela_edicao, text="Preço do Produto:", font=("Arial", 16), bg="#FFFFFF").grid(row=2, column=0, padx=10, pady=10, stick="W")
            preco_produto_edicao = Entry(janela_edicao, font=("Arial", 16), **estilo_borda, bg="#FFFFFF", textvariable=StringVar(value=valores_selecionados[3]))
            preco_produto_edicao.grid(row=2, column=1, padx=10, pady=10)

            #Cria uma função para salvar os dados no banco de dados
            def salvar_edicao():

                #Obtém os novos valores do item selecionado no Treeview
                nome_produto = nome_produto_edicao.get()
                nova_descricao = descricao_produto_edicao.get()
                novo_preco = preco_produto_edicao.get()

                #Atualiza os valores do item selecionado
                treeview.item(item_selecionado, values=(valores_selecionados[0], nome_produto, nova_descricao, novo_preco))

                #Executa um comando SQL para inserir os dados na tabela Produtos no banco de dados
                cursor.execute("UPDATE Produtos SET NomeProduto = ?, Descricao = ?, Preco = ? WHERE ID = ?",
                              (nome_produto, nova_descricao, novo_preco, valores_selecionados[0]))

                conexao.commit() #Gravando no BD

                print("Dados alterados com sucesso!")

                #Fecha a janela de cadastro
                janela_edicao.destroy()

                #Chama a função para listar os valores do banco de dados na treeview
                #listar_dados()        

            #columnspan - quantas colunas vai ocupar no grid   
            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
            botao_salvar_edicao = Button(janela_edicao, text="Alterar", font=("Arial", 12), bg="#008000",fg="#FFFFFF", command=salvar_edicao)
            botao_salvar_edicao.grid(row=4, column=0, padx=20, pady=20)

            def deletar_registro():

                #Recupera o id do registro selecionado na treeview
                selected_item = treeview.selection()[0]
                id = treeview.item(selected_item)['values'][0]

                #Deleta o registro do banco de dados
                cursor.execute("DELETE FROM Produtos WHERE id = ?", (id))

                conexao.commit()

                #fecha a janela de edição
                janela_edicao.destroy()

                #Rrecarregar os dados sem o novo resgistro
                listar_dados()

            #columnspan - quantas colunas vai ocupar no grid   
            #stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
            botao_deletar_edicao = Button(janela_edicao, text="Deletar", font=("Arial", 16), bg="#FF0000",fg="#FFFFFF", command=deletar_registro)
            botao_deletar_edicao.grid(row=4, column=1, padx=20, pady=20)


        #Adiciona o evento de duplo clique na Treeview para editar os dados do produto
        treeview.bind("<Double-1>", editar_dados)

        #Configura a janela para utilizar a barra de menus criada
        menu_barra = Menu(janela)
        janela.configure(menu=menu_barra)

        #Cria o menu chamado Arquivo
        """
        O parâmetro "tearoff=0" é utilizado no tkinter para controlar 
        a exibição de uma linha pontilhada no início de menus cascata. 
        Ao definir "tearoff=0", a linha pontilhada não será exibida e o 
        menu cascata ficará fixo na janela, não podendo ser destacado 
        ou movido para outra posição.
        """
        menu_arquivo = Menu(menu_barra, tearoff=0)
        menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)

        #Cria uma opção no menu "Arquivo" chamada "Cadastrar"
        menu_arquivo.add_command(label="Cadastrar", command=cadastrar)

        #Cria uma opção no menu "Arquivo" chamada "Sair"
        menu_arquivo.add_command(label="Sair", command=janela.destroy)

        #Limpo os dados da treeview
        def limparDados():

            #Limpanda os valores da treeview
            for i in treeview.get_children():

                #Deleto linha por linha
                treeview.delete(i)

        def filtrar_dados(nome_produto, descricao_produto):

            #if - se
            #Verifica se os campos estão vazio
            if not nome_produto.get() and not descricao_produto.get():

                listar_dados()

                #Se ambos os campos estiverem vazios, não faz nada
                return

            sql = "SELECT * FROM Produtos"

            params = []

            if nome_produto.get():

                """
                Concatena a string 'sql' com a 
                cláusula SQL 'WHERE NomeProduto LIKE ?'. 
                Essa cláusula é usada para filtrar 
                resultados de uma consulta de banco de dados
                com base em um padrão de correspondência 
                de texto, representado pelo caractere 
                curinga '?' na cláusula 'LIKE'. 
                Em resumo, essa linha está adicionando 
                uma condição de filtro à consulta SQL 
                para buscar registros que tenham o campo 
                'NomeProduto' correspondente ao padrão 
                especificado.
                """
                sql += " WHERE NomeProduto LIKE ?"

                """
                Adiciona um parâmetro de consulta à lista 'params'. 
                Esse parâmetro é uma string que é composta por três partes concatenadas:

                1 - O caractere curinga '%' no início da string, que representa qualquer
                número de caracteres (ou nenhum) antes do padrão de correspondência de 
                texto.
                2 - O valor do campo 'nome_produto' (obtido com o método 'get()' do 
                widget de entrada de texto correspondente).
                3 - Outro caractere curinga '%' no final da string, que representa 
                qualquer número de caracteres (ou nenhum) depois do padrão de 
                correspondência de texto.

                Essa string será usada como o valor do parâmetro na cláusula 'LIKE' 
                da consulta SQL, permitindo que a consulta retorne registros que 
                tenham o campo 'NomeProduto' correspondente ao padrão especificado 
                pelo usuário na interface do programa. Em resumo, essa linha de 
                código está criando um parâmetro de consulta dinamicamente com base 
                no texto digitado pelo usuário e adicionando-o à lista de parâmetros 
                que serão usados na consulta SQL.
                """
                params.append('%' + nome_produto.get() + '%')

            if descricao_produto.get():

                """
                verifica se o campo de entrada de texto 'descricao_produto' 
                tem algum valor preenchido. Se tiver, ele adiciona uma cláusula SQL 
                adicional à consulta em andamento ('sql') para filtrar os resultados 
                com base em um padrão de correspondência de texto na coluna 'Descricao'.

                Se o campo 'nome_produto' também tiver um valor preenchido, é adicionada 
                uma cláusula 'AND' para juntar as duas condições de filtro. Caso contrário, 
                é adicionada a cláusula 'WHERE' para começar a filtrar diretamente pela 
                coluna 'Descricao'.

                A linha 'params.append' cria um parâmetro de consulta dinamicamente com base 
                no texto digitado pelo usuário no campo 'descricao_produto', adicionando-o à 
                lista 'params' de parâmetros que serão usados na consulta SQL. Esse parâmetro 
                de consulta contém um padrão de correspondência de texto, representado pelos 
                caracteres curinga '%' antes e depois do valor do campo 'descricao_produto'.

                Em resumo, esse código adiciona uma condição de filtro à consulta SQL com 
                base no campo 'descricao_produto', permitindo que o usuário filtre os 
                resultados com base em dois campos diferentes ('NomeProduto' e 'Descricao') 
                ao mesmo tempo, caso ambos estejam preenchidos.
                """
                if nome_produto.get():
                    sql += " AND"
                else:
                    sql += " WHERE"
                sql += " Descricao LIKE ?"
                params.append('%' + descricao_produto.get() + '%')

            cursor.execute(sql, tuple(params))
            produtos = cursor.fetchall()

            #Limpa os dados da treeview
            limparDados()

            #Preenche treeview com os dados filtrados
            for dado in produtos:

                treeview.insert('', 'end', values=(dado[0], dado[1], dado[2], dado[3]))


        """
        Associa um evento de liberação de tecla ('KeyRelease') 
        ao widget de entrada de texto chamado 'nome_produto'. 
        Quando o evento de liberação de tecla ocorrer, a função 
        lambda definida será executada.

        Essa função lambda recebe um objeto de evento 
        (geralmente abreviado como 'e') como seu argumento 
        e chama uma outra função chamada 'filtrar_dados'. 
        A função 'filtrar_dados' é passada como argumentos 
        os widgets 'nome_produto' e 'descricao_produto'.

        O objetivo dessa linha de código é permitir que o usuário 
        filtre os dados mostrados no programa com base no que 
        foi digitado no campo 'nome_produto'. Quando o usuário 
        digita algo no campo 'nome_produto' e solta a tecla, a 
        função 'filtrar_dados' é chamada para atualizar a exibição 
        dos dados de acordo com o que foi digitado.
        """
        nome_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descricao_produto))
        descricao_produto.bind('<KeyRelease>', lambda e: filtrar_dados(nome_produto, descricao_produto))

        #Deleta o registro
        def deletar():

                #Recupera o id do registro selecionado na treeview
                selected_item = treeview.selection()[0]
                id = treeview.item(selected_item)['values'][0]

                #Deleta o registro do banco de dados
                cursor.execute("DELETE FROM Produtos WHERE id = ?", (id))

                conexao.commit()

                #Rrecarregar os dados sem o novo resgistro
                listar_dados()


        #Cria um botão para gravar os dados na tabela Produtos do banco de dados
        botao_deletar = Button(janela, text="Deletar", command=deletar, font="Arial 26")
        botao_deletar.grid(row=4, column=4, columnspan=4, stick="NSEW", padx=20, pady=5)


        #Inicia a janela Tkinter
        janela.mainloop()

        #Fechar o cursor e a conexao
        cursor.close()
        conexao.close()
        
        
    else:
        
        mensagem_lbl = Label(janela_principal, text="Nome de usuário ou senha incorretos", fg="red")
        mensagem_lbl.grid(row=3, column=0, columnspan=2)

#Criando a janela principal para a tela de login
janela_principal = Tk()
janela_principal.title("Tela de Login")

#bg - background (cor do fundo)
#Definindo a cor de fundo da janela
janela_principal.configure(bg="#F5F5F5")

#Define a largura e altura da janela
largura_janela = 450
altura_janela = 300

#Obtem a largura e altura da tela computador
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()


#Calcula a posição da janela para centraliza-la na tela
"""
Essas linhas calculam a posição em que a janela deve ser
exibida na tela do computador de forma centralizada. 
A posição x é definida pela diferença entre a largura da tela
e a largura da janela, dividida por 2. Já a posição y é definida
pela diferença entre a altura da tela e a altura da janela, também
dividida por 2. O operador "//" é utilizado para realizar a divisão
inteira, ou seja, retornar apenas o resultado inteiro da divisão.
"""
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

#Define a posição da janela
"""
define a geometria da janela principal, especificando a 
largura e altura da janela, bem como a posição onde a janela 
será exibida na tela, usando as variáveis previamente definidas 
para a posição x e y da janela. O formato utilizado é uma string 
que contém os valores de largura, altura, posição x e posição y da 
janela separados por "x" e "+" e passados ​​como argumentos para o m
étodo geometry() da janela principal.

O formato '{}'x'{}'+'{}'+'{}' é uma string de formatação que espera
quatro valores, que correspondem à largura da janela, altura da janela, 
posição x da janela e posição y da janela, respectivamente.

Esses valores são passados na ordem especificada para a string de formatação e, 
em seguida, são utilizados para definir a geometria da janela através do 
método geometry do objeto janela_principal.
"""
janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y ))

#stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
#fg - foreground (cor da letra)
#row - linha
#column - coluna
#columnspan - quantas colunas vai ocupar no grid
#pady - espaço
titulo_lbl = Label(janela_principal, text="Tela de Login", font="Arial 20", fg="blue", bg="#F5F5F5")
titulo_lbl.grid(row=0, column=0, columnspan=2, pady=20)

#Campo label
nome_usuario_lbl = Label(janela_principal, text="Nome de Usuário", font="Arial 14 bold", bg="#F5F5F5")
nome_usuario_lbl.grid(row=1, column=0, stick="e") #NSEW

#Campo label
senha_usuario_lbl = Label(janela_principal, text="Senha", font="Arial 14 bold", bg="#F5F5F5")
senha_usuario_lbl.grid(row=2, column=0, stick="e") #NSEW

#Criando um entry para o campo Nome de Usuario com a fonte Arial tamanho 14
nome_usuario_entry = Entry(janela_principal, font="Arial 14")
nome_usuario_entry.grid(row=1, column=1, pady=10 )

#Criando um entry para o campo Nome de Usuario com a fonte Arial tamanho 14
senha_usuario_entry = Entry(janela_principal, show="*", font="Arial 14")
senha_usuario_entry.grid(row=2, column=1, pady=10 )

#stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
entrar_btn = Button(janela_principal, text="Entrar", font="Arial 14", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, stick="NSEW")

#stick - Preenche as laterais NSEW (Norte, Sul, Leste e Oeste)
sair_btn = Button(janela_principal, text="Sair", font="Arial 14", command=janela_principal.destroy)
sair_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, stick="NSEW")

"""
Esse código está dentro de um laço "for" que executa 5 vezes
e serve para configurar o comportamento de uma grade (ou "grid") no tkinter.
A função "grid_rowconfigure()" permite definir a configuração de uma 
determinada linha na grade, com dois parâmetros: 
o índice da linha e um peso (ou "weight") que determina 
como essa linha deve se comportar em relação às outras linhas da grade.

No código em questão, o laço "for" está configurando as 5 linhas
da grade da janela_principal com um peso igual a 1. 
Isso significa que todas as linhas terão a mesma altura 
e que a altura da janela será dividida igualmente entre elas.
"""
for i in range(5):
    janela_principal.grid_rowconfigure(i, weight=1)

"""
Este código é usado para definir a configuração das colunas da grade
na janela principal. Ele utiliza um loop "for" para iterar através de 
duas colunas da grade e chama o método "grid_columnconfigure" do 
objeto "janela_principal" para definir o "weight" (peso) como 1.

O parâmetro "weight" é uma propriedade do gerenciador de layout do 
Tkinter que define a prioridade de expansão das colunas (ou linhas) 
quando a janela é redimensionada. Valores mais altos de "weight" significam
que a coluna irá expandir mais do que as outras colunas que possuem valores 
mais baixos de "weight". Ao configurar as colunas com um "weight" de 1, 
a janela principal será capaz de expandir uniformemente as colunas em toda 
a largura da janela quando ela for redimensionada.
"""
for i in range(2):
    janela_principal.grid_columnconfigure(i, weight=1)

#Inicia a janela Tkinter
janela_principal.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




