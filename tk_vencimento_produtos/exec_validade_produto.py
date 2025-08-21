"""
Exercício: Sistema de Validade de Produtos

Um mercado contratou você para desenvolver um programa que ajude a conferir e classificar 
a validade dos produtos em seu estoque. O programa deve permitir o cadastro de produtos com 
suas respectivas datas de validade e oferecer opções para consultar os produtos com base em 
sua situação de validade.

O programa deve fornecer as seguintes funcionalidades:

    Cadastrar Produto: O usuário pode cadastrar um novo produto informando seu código, nome e 
    data de validade.

    Consultar Produtos: O usuário pode escolher uma das opções disponíveis para visualizar os 
    produtos de acordo com sua situação de validade:
    
        "Tranquilo": Produtos com mais de 90 dias até a validade.
        "Alerta": Produtos com menos de 90 dias e mais de 30 dias até a validade.
        "Critico": Produtos com menos de 30 dias até a validade.
        "Produto Vencido": Produtos com a data de validade expirada.

    Sair: Encerrar o programa.

O programa deve utilizar a função datetime para obter a data atual do sistema e calcular a 
diferença em dias entre a data de validade e a data atual. Com base nessa diferença, o programa 
deve classificar a situação de validade dos produtos e exibir as informações relevantes.

Crie um programa em Python que implemente as funcionalidades descritas acima. O programa deve 
utilizar uma lista para armazenar os produtos cadastrados.

Observações:

    As datas devem ser inseridas no formato "dd/mm/aaaa".
    O programa deve tratar erros de entrada inválida para datas.
    Utilize a função strftime para formatar as datas de validade ao exibi-las.

Teste o programa cadastrando produtos e consultando-os com diferentes opções para verificar 
se a classificação e filtragem estão corretas.

Lembre-se de escrever um código limpo, organizado e com comentários para facilitar a compreensão.
"""

from datetime import datetime

#Lista de produtos
produtos = []

def cadastrar_produtos():
    
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    data_validade = input("Digite a data de validade (dd/mm/aaaa): ")
    
    try:
        
        data_validade = datetime.strptime(data_validade, "%d/%m/%Y").date()
        
    except ValueError:
        
        print("Formato de data inválido. Use o formato dd/mm/aaaa.\n")
        return
    
    produto = {
        "codigo": codigo,
        "nome": nome, 
        "validade": data_validade
    }
    
    #Adiciona o produto a lista
    produtos.append(produto)
    
    print("Produto cadastrado com sucesso!\n")
    

def lista_produtos_por_quantidade_dias(dias_min, dias_max):
    
    #Pega a data atual do computador
    data_atual = datetime.now().date()
    
    print(f"Produtos com {dias_min} a {dias_max} dias até a validade")
    
    #for - para
    for produto in produtos:
        
        diferenca_tempo = produto["validade"] - data_atual
        
        #if - se
        if dias_min <= diferenca_tempo.days <= dias_max:
            
            print(f"Código: {produto['codigo']}")
            print(f"Produto: {produto['nome']}")
            print(f"Data de Validade: {produto['validade'].strftime('%d/%m/%Y')}")
            print(f"Dias restantes: {diferenca_tempo.days}\n")
    
def consultar_produtos():
    
    opcao = ""
    
    while opcao != "S":
    
        print("\n---------- MENU -----------")
        print("1. Tranquilo (mais de 90 dias)")
        print("2. Alerta (entre 31 e 90 dias)")
        print("3. Critico (entre 1 e 30 dias)")
        print("4. Produto Vencido (data de validade expirada)")
        print("S. Sair\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            lista_produtos_por_quantidade_dias(91, float('inf')) #inf - Numero infinito positivo

        elif opcao == "2":

            lista_produtos_por_quantidade_dias(31, 90) 
            
        elif opcao == "3":

            lista_produtos_por_quantidade_dias(1, 30) 
            
        elif opcao == "4":

            lista_produtos_por_quantidade_dias(float('-inf'), 0) #inf - Numero infinito positivo


        elif opcao == "S":

            print("Saindo do Menu!\n")
            break

        else:

            print("Opção inválida. Tente novamente. \n")
        
    
opcao_menu = ""
while opcao_menu != "S":
    
    print("\n---------- MENU PRINCIPAL -----------")
    print("1. Cadastrar Produto")
    print("2. Consultar Produtos")
    print("S. Sair\n")
    
    opcao_menu = input("Escolha uma opção: ")
    
    if opcao_menu == "1":
        
        print("-------- CADASTRO PRODUTOS ------\n")
        cadastrar_produtos()
        
    elif opcao_menu == "2":
        
        print("-------- CONSULTAR PRODUTOS ------\n")
        consultar_produtos()
        
    elif opcao_menu == "S":
        
        print("Programa encerrado com sucesso!\n")
        break
        
    else:
        
        print("Opção inválida. Tente novamente. \n")