import tkinter as tk
from tkinter import messagebox

#Lista para armazenar as reservas feitas pelo usuário
reservas = []

def verificar_conflito_reserva(hora_inicial, hora_final):
    
    #Verifica se existe um conflito entre a nova reserva e as reservas existentes.
    #Retorna True se houver um conflito, caso contrário, retorna False.
    for reserva in reservas:  # Itera sobre todas as reservas existentes
        
        #o índice 1 refere-se à hora inicial da reserva e o índice 0 refere-se à hora final 
        if hora_inicial < reserva[1] and hora_final > reserva[0]:
            
            # Verifica se há um conflito comparando os horários
            # Se a hora inicial for menor do que a hora final da reserva existente
            # E se a hora final for maior do que a hora inicial da reserva existente
            return True  # Há um conflito de horários
        
    return False  # Não há conflito de horários



def fazer_reserva():
    
    janela_fazer_reserva = tk.Toplevel()
    janela_fazer_reserva.title("Fazer Reserva")
    janela_fazer_reserva.configure(bg="#FFFFFF")  #Define a cor do fundo
    
    fonte_titulo = ("Arial 24 bold")
    fonte_label = ("Arial 24")
    fonte_Entry = ("Arial 16")
    fonte_btn_confirmar = ("Arial 18 bold")
    
    #======================================
    #Cria o frame que possui os botões
    frame_titulo= tk.Frame(janela_fazer_reserva, 
                            bg="#FFFFFF")
    frame_titulo.pack(pady = 20) #Cria e centraliza
    
    label_titulo = tk.Label(frame_titulo, 
                           text = "Fazer Reserva",
                           font = fonte_titulo,
                           bg="#FFFFFF")
    label_titulo.pack(pady = 20) #Cria e centraliza
    
    
    #======================================
    
    #Cria o frame que possui os botões
    frame_formulario= tk.Frame(janela_fazer_reserva, 
                            bg="#FFFFFF")
    frame_formulario.pack(pady = 20) #Cria e centraliza
    
    #Label
    label_inicial = tk.Label(frame_formulario, 
                           text = "Digite a hora inicial da reserva (Entre 09:00 e 23:00):",
                           font = fonte_label,
                           bg="#FFFFFF")
    label_inicial.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    
    #Campo de entrada de dados
    entry_inicial = tk.Entry(frame_formulario, 
                           text = "Digite a hora inicial da reserva (Entre 09:00 e 23:00):",
                           font = fonte_Entry,
                           bg="#FFFFFF")
    entry_inicial.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    
    #--------------
    
    #Label
    label_final = tk.Label(frame_formulario, 
                           text = "Digite a hora inicial da reserva (Entre 09:00 e 23:00):",
                           font = fonte_label,
                           bg="#FFFFFF")
    label_final.grid(row = 1, column = 0, padx = 10, pady = 10)
    
    
    #Campo de entrada de dados
    entry_final = tk.Entry(frame_formulario, 
                           text = "Digite a hora final da reserva (Entre 09:00 e 23:00):",
                           font = fonte_Entry,
                           bg="#FFFFFF")
    entry_final.grid(row = 1, column = 1, padx = 10, pady = 10)
    
    
    def fazer_reserva_click():
        
        hora_inicial = entry_inicial.get()
        hora_final = entry_final.get()
        
        if hora_inicial < "09:00" or hora_final > "23:00" or hora_inicial >= hora_final:
            
            tk.messagebox.showerror("Horário inválido", "Horário inválido. Tente novamente.")
            
            return
            
        if verificar_conflito_reserva(hora_inicial, hora_final):
            
            tk.messagebox.showerror("Conflito de horários", "Já existe uma reserva neste horário. Escolha outro horário.")
            
            return
            
        hora_inicial_str = hora_inicial[:-3] #Obtém a parte das horas da hora inicial
        minuto_inicial_str = hora_inicial[-2:] #Obtém a parte dos minutos da hora inicial
        hora_final_str = hora_final[:-3] #Obtém a parte das horas da hora final
        minuto_final_str = hora_final[-2:] #Obtém a parte dos minutos da hora final
        
        """
        Digite a hora inicial da reserva (entre 09:00 e 23:00): 09:00
        Digite a hora final da reserva (entre 09:00 e 23:00): 10:00
        hora_inicial_str: 09
        minuto_inicial_str: 00
        hora_final_str: 10
        minuto_final_str: 00
        """
        
        """
        (int(hora_final_str) * 60 + int(minuto_final_str)): Essa expressão realiza o 
        cálculo para converter a hora final da reserva em minutos. Primeiro, convertemos
        a parte das horas, hora_final_str, em um número inteiro usando int(hora_final_str). 
        Em seguida, multiplicamos esse valor por 60 para converter as horas em minutos. 
        Por fim, adicionamos a parte dos minutos, minuto_final_str, também convertida em um 
        número inteiro usando int(minuto_final_str). Assim, obtemos o total de minutos 
        correspondente à hora final da reserva.

        (int(hora_inicial_str) * 60 + int(minuto_inicial_str)): Essa expressão realiza o 
        mesmo cálculo descrito anteriormente, mas para a hora inicial da reserva. Convertemos 
        a parte das horas, hora_inicial_str, em um número inteiro usando int(hora_inicial_str). 
        Em seguida, multiplicamos esse valor por 60 para converter as horas em minutos. 
        Por fim, adicionamos a parte dos minutos, minuto_inicial_str, também convertida em um 
        número inteiro usando int(minuto_inicial_str). Assim, obtemos o total de minutos 
        correspondente à hora inicial da reserva.

        (int(hora_final_str) * 60 + int(minuto_final_str)) - (int(hora_inicial_str) * 60 + int(minuto_inicial_str)): 
        Nessa etapa, subtraímos o valor total de minutos da hora inicial do valor total de 
        minutos da hora final. Isso nos dá a duração da reserva em minutos. Por exemplo, se a hora 
        inicial for 09:00 e a hora final for 10:30, teremos (10 * 60 + 30) - (9 * 60 + 0), que 
        resultará em 90 minutos, correspondendo à duração da reserva.

        valor_total = duracao_minutos * 8 / 60: Após calcular a duração da reserva em 
        minutos, multiplicamos esse valor por 8, que é o valor por minuto para calcular 
        o valor total da reserva. Como o preço é dado por minuto, dividimos por 60 para 
        converter os minutos em horas. O resultado é armazenado na variável valor_total.
        """
        duracao_minutos = (int(hora_final_str) * 60 + int(minuto_final_str)) - (int(hora_inicial_str) * 60 + int(minuto_inicial_str))
        valor_total = duracao_minutos * 8 / 60
        
        
        reservas.append((hora_inicial, hora_final))
        
        mensagem = "\nA reserva das {}:{} às {}:{} foi feita com sucesso.".format(hora_inicial_str, minuto_inicial_str, hora_final_str, minuto_final_str)
        mensagem += "\nO valor total da reserva é de R${:.2f}\n".format(valor_total)
        
        tk.messagebox.showinfo("Reserva feita com sucesso", mensagem)
        
        #Fecha a janela de reservas
        janela_fazer_reserva.destroy()
        
    
    #Cria o botão
    btn_confirmar = tk.Button(janela_fazer_reserva, 
                           text = "Confirmar",
                           font = fonte_btn_confirmar,
                           command = fazer_reserva_click,
                           bg="#FFFFFF")
    btn_confirmar.pack(pady = 20)
    
    #Centraliza a janela
    janela_fazer_reserva.update_idletasks()
    
    # Obtém a largura atual da janela
    largura = janela_fazer_reserva.winfo_width()

    # Obtém a altura atual da janela
    altura = janela_fazer_reserva.winfo_height()

    # Calcula a posição x para centralizar a janela na tela
    posicao_x = (janela_fazer_reserva.winfo_screenwidth() // 2) - (largura // 2)

    # Calcula a posição y para centralizar a janela na tela
    posicao_y = (janela_fazer_reserva.winfo_screenheight() // 2) - (altura // 2)

    # Define a geometria da janela com a largura, altura, posição x e posição y
    janela_fazer_reserva.geometry('{}x{}+{}+{}'.format(largura, altura, posicao_x, posicao_y))
    

def ver_reservas():
    
    janela_ver_reservar = tk.Toplevel()
    janela_ver_reservar.title("Ver Reservas")
    janela_ver_reservar.configure(bg="#FFFFFF")
    
    frame_titulo = tk.Frame(janela_ver_reservar, bg="#FFFFFF")
    frame_titulo.pack(pady = 20)
    
    
    label_titulo = tk.Label(frame_titulo,
                           text= "Lista de Reservas",
                           font = "Arial 18",
                           bg="#FFFFFF")
    label_titulo.pack()
    
    frame_reservas = tk.Frame(janela_ver_reservar, bg="#FFFFFF")
    frame_reservas.pack()
    
    #Para cada itens da lista
    for reserva in reservas:
        
        #Cada linha da lista é uma reserva
        #Para cada reserva crio um label um em baixo do outro
        label_reserva = tk.Label(frame_reservas,
                                text = f"- {reserva[0]} às {reserva[1]}",
                                font = "Arial 16",
                                bg="#FFFFFF")
        label_reserva.pack(pady = 5)
        
    #Criando o botão que fecha a tela
    btn_fechar = tk.Button(janela_ver_reservar,
                          text = "Fechar",
                          command = janela_ver_reservar.destroy,
                          font = "Arial 18",
                          width = 20)
    btn_fechar.pack(pady = 10)
    
    #Centraliza a janela
    janela_ver_reservar.update_idletasks()
    
    # Obtém a largura atual da janela
    largura = janela_ver_reservar.winfo_width()

    # Obtém a altura atual da janela
    altura = janela_ver_reservar.winfo_height()

    # Calcula a posição x para centralizar a janela na tela
    posicao_x = (janela_ver_reservar.winfo_screenwidth() // 2) - (largura // 2)

    # Calcula a posição y para centralizar a janela na tela
    posicao_y = (janela_ver_reservar.winfo_screenheight() // 2) - (altura // 2)

    # Define a geometria da janela com a largura, altura, posição x e posição y
    janela_ver_reservar.geometry('{}x{}+{}+{}'.format(largura, altura, posicao_x, posicao_y))
   
    #Cria e exibe a janela    
    janela_ver_reservar.mainloop()
    
    
def tela_inicial():
    
    #Cria e exibe a tela inicial com os botões
    janela_inicial = tk.Tk()
    janela_inicial.title("Menu")
    janela_inicial.configure(bg="#FFFFFF")  #Define a cor do fundo
    
    fonte_titulo = ("Arial 24 bold")
    fonte_botoes = ("Arial 20")
    
    label_titulo = tk.Label(janela_inicial, 
                           text = "Sistema de Reservas",
                           font = fonte_titulo,
                           bg="#FFFFFF")
    label_titulo.pack(pady = 20) #Cria e centraliza
    
    #Cria o frame que possui os botões
    frame_botoes = tk.Frame(janela_inicial, 
                            bg="#FFFFFF")
    frame_botoes.pack(pady = 20) #Cria e centraliza
    
    #-----------------------
    
    btn_fazer_reserva = tk.Button(frame_botoes,
                                 text = "Fazer Reserva",
                                 command = fazer_reserva,
                                 font = fonte_botoes,
                                 width = 20)
    btn_fazer_reserva.pack(pady = 10) #Cria e centraliza
    
    #-----------------------
    
    btn_ver_reserva = tk.Button(frame_botoes,
                                 text = "Ver Reservas",
                                 command = ver_reservas,
                                 font = fonte_botoes,
                                 width = 20)
    btn_ver_reserva.pack(pady = 10) #Cria e centraliza
    
    #-----------------------
    
    btn_sair = tk.Button(frame_botoes,
                                 text = "Sair",
                                 command = janela_inicial.destroy,
                                 font = fonte_botoes,
                                 width = 20)
    btn_sair.pack(pady = 10) #Cria e centraliza
    
    #-------------------------------
    
    #Centraliza a janela
    janela_inicial.update_idletasks()
    
    # Obtém a largura atual da janela
    largura = janela_inicial.winfo_width()

    # Obtém a altura atual da janela
    altura = janela_inicial.winfo_height()

    # Calcula a posição x para centralizar a janela na tela
    posicao_x = (janela_inicial.winfo_screenwidth() // 2) - (largura // 2)

    # Calcula a posição y para centralizar a janela na tela
    posicao_y = (janela_inicial.winfo_screenheight() // 2) - (altura // 2)

    # Define a geometria da janela com a largura, altura, posição x e posição y
    janela_inicial.geometry('{}x{}+{}+{}'.format(largura, altura, posicao_x, posicao_y))
    
    #Cria e exibe na tela
    janela_inicial.mainloop()
    
    
#chamo a função
tela_inicial()
    