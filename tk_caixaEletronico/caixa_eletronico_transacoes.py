#Tela Login - Interface
#Cria conexão com o Excel e Loga
import tkinter as tk #Importa a biblioteca para criar a interface gráfica
from tkinter import ttk #Importa o módulo ttk do Tkinter para obter estilos ou intens mais avançados
import tkinter.font as font #Para personalizar as fontes
from tkinter import messagebox #Exibe caixas de diálogo
import pandas as pd #Para trabalhar com os dados em formato tabular

def abrir_janela_operacoes(nome, conta, cpf):
    
        messagebox.showerror("Mensgem", "LOGIN EFETUADO COM SUCESSO!")

def Verificar_login(entry_conta, entry_senha):
    
    #Obtém os valores digitados pelo usuário no campo de entrada de dados
    conta = entry_conta.get()
    senha = entry_senha.get()
    
    #Limpa os campos de entrada de dados
    entry_conta.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    
    arquivo_excel = r"C:\python_projetos\python_rpa_projetos\tk_caixaEletronico\Base_Dados.xlsx"
    
    try:
        
        dados = pd.read_excel(arquivo_excel, sheet_name="Usuários")
        
        #Itera sobre as linhas da sheet de usuários
        for index, row in dados.iterrows():
            
            #if - se
            if str(row['Conta']) == str(conta) and str(row['Senha']) == str(senha):
                
                nome = row['Nome']
                cpf = row['CPF']
                
                #Fecho a tela de Login
                janela_login.destroy()
                
                #Abre a tela de operações
                abrir_janela_operacoes(nome, conta, cpf)
                
                break
    
    except Exception as e:
        
        messagebox.showerror("Erro", "Erro ao ler a planilha!")

janela_login = tk.Tk() #Cria a instancia do Tk para criar a janela
janela_login.title("Caixa Eletrônico") #Define o título da janela
janela_login.geometry("300x300") #Define as dimensões da janela

#Define a cor de fundo da janela
janela_login.configure(bg="#FFFFFF") #Cor branco

#Definindo uma variavel com a fonte padrão
custom_font = font.Font(family="Arial", size=16)

#Criando um campo de texto
label_conta = tk.Label(janela_login, 
                        text="Número da Conta: ",
                        font=custom_font, 
                        bg="#FFFFFF")
label_conta.pack(pady=10) #pack - Cria embaixo e centraliza 

#Campo de entrada de dados
entry_conta = tk.Entry(janela_login,
                        font=custom_font, 
                        bg="#FFFFFF")
entry_conta.pack(pady=5) #pack - Cria embaixo e centraliza

#-------------------------------

#Criando um campo de texto
label_senha = tk.Label(janela_login, 
                        text="Senha: ",
                        font=custom_font, 
                        bg="#FFFFFF")
label_senha.pack(pady=10) #pack - Cria embaixo e centraliza 

#Campo de entrada de dados
entry_senha = tk.Entry(janela_login,
                        show="*",
                        font=custom_font, 
                        bg="#FFFFFF")
entry_senha.pack(pady=5) #pack - Cria embaixo e centraliza

botao_entrar = tk.Button(janela_login, 
                        text="Entrar",
                        font=custom_font, 
                        bg="#FFFFFF",
                        command=lambda: Verificar_login(entry_conta, entry_senha)) #lambda - Cria uma função anônima que chama a Verificar_login
botao_entrar.pack(pady=10) #pack - Cria embaixo e centraliza


#Inicializa a janela na tela
janela_login.mainloop()