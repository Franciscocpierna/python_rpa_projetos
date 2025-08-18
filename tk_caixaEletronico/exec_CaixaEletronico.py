#Crie um algoritmo de um caixa eletronico

def depositar(saldo):
    
    valor = float(input("\nDigite o valor a ser depositado: "))
    
    #Adiciona o valor ao saldo atual
    #saldo = saldo + valor
    saldo += valor
    
    print("\n\nDepósito realizado!")
    
    return saldo

def sacar(saldo):
    
    valor = float(input("\nDigite o valor a ser sacado: "))
    
    #Verifico se há saldo suficiente
    if valor <= saldo:
        
        #saldo = saldo - valor
        saldo -= valor
        
        print("\n\nSaque realizado!")
        
    else:
        
        print("\n\nSaldo insuficiente!")
        
    return saldo

def ver_saldo(saldo):
    
    print("\nSeu saldo atual é R$", saldo)


def caixa_eletronico():
    
    #Define o saldo inicial como zero
    saldo = 0.0
    opcao = ""
    
    #while - enquanto
    while opcao != "sair":
        
        print("\n=== Caixa Eletrônico ===")
        print("Opções: [d] Deposito")
        print("Opções: [s] Sacar")
        print("Opções: [v] Ver Saldo")
        print("Opções: [sair] Encerrar")
        
        opcao = input("\nEscolha uma opção: ")
        
        #if - se
        #elif - senão se
        #else - else
        if opcao == "d":
            
            #Chama a função depositar
            saldo = depositar(saldo)
            
        elif opcao == "s":
            
            #Chama a função depositar
            saldo = sacar(saldo)
            
        elif opcao == "v":
            
            #Chama a função depositar
            ver_saldo(saldo)
            
        elif opcao == "sair":
            
            print("\nOperação encerrada")
            
            break   
            
        else:
            
            print("\nOpção inválida. Tente novamente.")
            
#Chama a função
caixa_eletronico()            