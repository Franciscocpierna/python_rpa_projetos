"""
Crie um algoritmo em Python onde solicite ao usuário que digite um horário 
entre 09:00 e 23:00, o usuário deve informar a hora inicial e hora final, 
cada hora custa 8 reais, mas o algoritmo deve verificar se já existe uma 
reserva neste horário se existir, deve solitar que digite um horário diferente e 
tabém tenha a opção de ver as reservas
"""

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

def fazer_reservar():
    
    while True:
        
        hora_inicial = input("Digite a hora inicial da reserva (entre 09:00 e 23:00): ")
        hora_final = input("Digite a hora final da reserva (entre 09:00 e 23:00): ")
        
        if hora_inicial < "09:00" or hora_final > "23:00" or hora_inicial >= hora_final:
            
            print("Horário inválido. Tente novamente.")
            continue
            
        if verificar_conflito_reserva(hora_inicial, hora_final):
            
            print("Já existe uma reserva neste horário. Escolha outro horário.")
            continue
            
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
        
        print("\nA reserva das {}:{} às {}:{}".format(hora_inicial_str, minuto_inicial_str, hora_final_str, minuto_final_str))
        print("O valor total da reserva é de R${:.2f}\n".format(valor_total))
        
        break
        
#Exibe todas as reservas
def ver_reservas():

    print("\nReservas:")
    
    for reserva in reservas:
    
        print(f" - {reserva[0]} às {reserva[1]}")
        
#Enquanto for verdadeiro
while True:
    
    print("\n1. Fazer Reserva")
    print("2. Ver Reservas")
    print("3. Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    #if - se
    if opcao == "1":
        
        fazer_reservar()
        
    elif opcao == "2":
        
        ver_reservas()
        
    elif opcao == "3":
        
        break
        
    else:
        
        print("Opção inválida. Tente novamente.")