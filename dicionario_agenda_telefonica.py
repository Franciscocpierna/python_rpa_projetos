def mostrar_menu():
    
    print("\nMENU:")
    print("1. Adicionar contato")
    print("2. Alterar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("5. Sair")

# Função para adicionar um novo contato ao dicionário de contatos.
def adicionar_contato(contatos):
    
    # Obtém o nome do contato.
    nome = input("\nDigite o nome do contato: ")
    
    # Obtém o número de telefone.
    telefone = input("Digite o número de telefone: ")
    
    # Adiciona/Atualiza o contato no dicionário.
    contatos[nome] = telefone
    print(contatos)
    print("\nContato adicionado com sucesso!")
    
# Função para alterar um contato existente.
def alterar_contato(contatos):
    
    # Obtém o nome do contato a ser alterado.
    nome_atual = input("\nDigite o nome do contato que deseja alterar: ")

    # Verifica se o contato existe.
    if nome_atual in contatos:
        
        # Solicita as novas informações ao usuário.
        novo_nome = input("Digite o novo nome para o contato (deixe em branco para manter o nome atual): ")
        novo_telefone = input("Digite o novo número de telefone (deixe em branco para manter o atual): ")
        
        # Altera o nome, se fornecido.
        if novo_nome:
            
            # Verifica se o novo nome já está em uso.
            if novo_nome in contatos:
                
                print("\nO nome informado já está em uso. Por favor, tente um nome diferente.")
                
                return
            
            # Adiciona o novo nome com os dados antigos.
            contatos[novo_nome] = contatos[nome_atual]
            
            # Remove o nome antigo.
            del contatos[nome_atual]
            
        else:
            
            # Mantém o nome original, se nenhum novo nome for fornecido.
            novo_nome = nome_atual
        
        # Altera o telefone, se fornecido pelo usuário.
        if novo_telefone:
            
            # Atualiza o telefone do contato no dicionário.
            contatos[novo_nome] = novo_telefone

        
        print("\nContato atualizado com sucesso!")
        
    else:
        
        print("\nContato não encontrado!")
        
# Função para remover um contato do dicionário.
def remover_contato(contatos):
    
    # Obtém o nome do contato a ser removido.
    nome = input("\nDigite o nome do contato que deseja remover: ")

    # Verifica se o contato existe e o remove.
    if nome in contatos:
        
        del contatos[nome]
        
        print("\nContato removido com sucesso!")
        
    else:
        
        print("\nContato não encontrado!")

    
# Função para listar todos os contatos no dicionário.
def listar_contatos(contatos):
    
    # Verifica se há contatos no dicionário.
    if not contatos:
        
        print("\nNenhum contato registrado!")
        
    # Itera e exibe todos os contatos.
    for nome, telefone in contatos.items():
        
        print(f"\nNome: {nome}")
        print(f"Telefone: {telefone}")

    
# Função principal para executar o programa.
def main():
    
    # Inicializa um dicionário vazio para contatos.
    contatos = {}
    
    # Loop infinito para a interação do usuário.
    while True:
        
        # Exibe o menu.
        mostrar_menu()
        
        # Obtém a escolha do usuário.
        escolha = input("Escolha uma opção: ")

        # Condicional para direcionar a ação com base na opção escolhida pelo usuário.
        
        # Se o usuário escolher a opção 1:
        if escolha == "1":
            
            # Chama a função para adicionar um novo contato.
            adicionar_contato(contatos)
        
        # Se o usuário escolher a opção 2:
        elif escolha == "2":
            
            # Chama a função para alterar um contato existente.
            alterar_contato(contatos)
        
        # Se o usuário escolher a opção 3:
        elif escolha == "3":
            
            # Chama a função para remover um contato.
            remover_contato(contatos)
        
        # Se o usuário escolher a opção 4:
        elif escolha == "4":
            
            # Chama a função para listar todos os contatos.
            listar_contatos(contatos)
        
        # Se o usuário escolher a opção 5:
        elif escolha == "5":
            
            # Encerra o loop e, consequentemente, o programa.
            break  
        
        # Se o usuário escolher uma opção que não está no menu:
        else:
            
            # Exibe uma mensagem de erro.
            print("\nOpção inválida!")


# Chama a função principal para executar o programa.
main()
