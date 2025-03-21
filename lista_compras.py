# Inicializa a lista de compras vazia
lista_compras = []

# Loop principal para manter o programa em execução
while True:
    
    print("\nMenu:")
    print("1. Adicionar item à lista")
    print("2. Remover item da lista")
    print("3. Exibir lista de compras")
    print("4. Sair")

    # Solicita ao usuário que escolha uma opção do menu
    opcao = int(input("Escolha uma opção: "))

    # Se a opção escolhida for 1:
    if opcao == 1:
        
        # Solicita o item a ser adicionado
        item = input("Digite o item que deseja adicionar à lista: ")
        
        # Adiciona o item à lista de compras utilizando o método append()
        lista_compras.append(item)
        
        print("Item adicionado à lista!")

    # Se a opção escolhida for 2:
    elif opcao == 2:
        
        # Verifica se a lista de compras está vazia
        if len(lista_compras) == 0:
            
            print("A lista de compras está vazia.")
            
        else:
            
            # Solicita o item a ser removido
            item = input("Digite o item que deseja remover da lista: ")
            
            # Verifica se o item está presente na lista
            if item in lista_compras:
            
                # Remove o item da lista utilizando o método remove()
                lista_compras.remove(item)
                
                print("Item removido da lista!")
                
            else:
                
                print("O item não está na lista.")

    # Se a opção escolhida for 3:
    elif opcao == 3:
        
        print("\nLista de Compras:")
        
        # Itera sobre os itens da lista de compras
        for item in lista_compras:
            
            # Imprime cada item com um hífen no início
            print("-", item)

    # Se a opção escolhida for 4:
    elif opcao == 4:
        
        print("Saindo...")
        
        # Encerra o loop e sai do programa
        break

    # Se a opção escolhida não for válida:
    else:
        
        print("Opção inválida. Escolha uma opção válida.")

    # Adiciona uma linha em branco após cada operação
    print()
        