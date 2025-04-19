"""
Exercício: Comparação de Preços e Desconto Adicional para Cinco Produtos

Objetivo: Desenvolver um programa que obtenha do usuário o preço de cinco
produtos e indique qual produto deve ser comprado com base no menor preço. 

Além disso, se o usuário optar por comprar o produto recomendado, o programa oferecerá um desconto.

Instruções:

    1. Solicite ao usuário que informe o preço de cinco produtos.
    2. Determine e exiba qual dos cinco produtos é o mais barato.
    3. Informe ao usuário a diferença de preço entre o produto mais barato e os outros quatro.
    4. Pergunte ao usuário se ele deseja comprar o produto mais barato agora.
        a. Se o usuário responder "sim", ofereça um desconto de 5% sobre o preço 
        do produto mais barato e informe o novo preço.
        
        b. Se o usuário responder "não", exiba uma mensagem: "Lembre-se de sempre 
        buscar o melhor negócio!"
    
    5. Caso o usuário escolha comprar o produto mais barato com o desconto, 
    peça um método de pagamento:
    
    a. Se o método de pagamento for "dinheiro", ofereça um desconto adicional de 2%.
        b. Se for "cartão", informe que o pagamento pode ser dividido em até 3 vezes sem juros.
    
    6.Exiba um resumo da compra, incluindo produto escolhido, preço original, desconto 
    aplicado e preço final.

Observações: O programa deve considerar que o usuário fornecerá apenas valores numéricos 
válidos para os preços. As respostas do usuário para perguntas como a intenção de compra 
podem ser "sim" ou "não", e o programa deve ser insensível a maiúsculas e minúsculas (ou 
seja, "Sim", "sim" e "SIM" são consideradas a mesma resposta).
"""

#Solução:

# Primeiro, vamos criar uma lista para armazenar os preços dos produtos.
produtos = []

#1. Solicite ao usuário que informe o preço de cinco produtos.
# Inicia um loop que se repetirá 5 vezes (de 1 a 5, inclusive)
for i in range(1, 6):
    
    # Solicita ao usuário o preço do produto atual e converte a entrada para um número do tipo float
    preco = float(input(f"Digite o preço do {i}º produto: R$ "))
    
    # Adiciona o preço informado à lista de produtos
    produtos.append(preco)
    
    
#2. Determine e exiba qual dos cinco produtos é o mais barato.
produto_mais_barato = min(produtos)

print(f"\nO produto mais barato custa R$ {produto_mais_barato:.2f}")


#3. Informe ao usuário a diferença de preço entre o produto mais barato e os outros quatro.

for i, preco in enumerate(produtos):
    print(f"Produto {i} custa R$ {preco:.2f}")
"""
enumerate(produtos, 1): Isso cria um iterador que percorre 
a lista produtos, começando do índice 1. O valor 1 é passado 
como o segundo argumento para indicar a partir de qual número 
o contador deve começar.
"""


for i, preco in enumerate(produtos, 1):
    
    diferenca = preco - produto_mais_barato
    print(f"A diferença de preço entre o produto {i} e o produto mais barato é R$ {diferenca:.2f}")
    print(f"produtos[0] {produtos[0]}")
    print(f"produtos[0] {produtos[i]}")
    
"""
4. Pergunte ao usuário se ele deseja comprar o produto mais barato agora.
        a. Se o usuário responder "sim", ofereça um desconto de 5% sobre o preço 
        do produto mais barato e informe o novo preço.
        
        b. Se o usuário responder "não", exiba uma mensagem: "Lembre-se de sempre 
        buscar o melhor negócio!"
"""

# Definir desconto_adicional como 0 no início
desconto_adicional = 0

resposta_compra = input("Você deseja comprar o produto mais barato agora? (sim/não) ").strip().lower()

# Verifica se a resposta do usuário para comprar o produto mais barato foi 'sim'
if resposta_compra == 'sim':
    
    # Calcula o desconto de 5% sobre o preço do produto mais barato
    desconto = produto_mais_barato * 0.05
    
    # Calcula o novo preço subtraindo o desconto
    preco_com_desconto = produto_mais_barato - desconto
    
    # Mostra para o usuário o novo preço após o desconto de 5%
    print(f"\nCom o desconto de 5%, o novo preço é R$ {preco_com_desconto:.2f}")
    
    """
    5. Caso o usuário escolha comprar o produto mais barato com o desconto, 
    peça um método de pagamento:
    
        a. Se o método de pagamento for "dinheiro", ofereça um desconto adicional de 2%.
            b. Se for "cartão", informe que o pagamento pode ser dividido em até 3 vezes sem juros.
    """
    
    # Solicita ao usuário o método de pagamento e converte para minúsculas para facilitar a comparação
    metodo_pagamento = input("Qual será o método de pagamento? (dinheiro/cartão) ").strip().lower()
    
    # Verifica se o método de pagamento é dinheiro
    if metodo_pagamento == "dinheiro":
        
        # Calcula um desconto adicional de 2% para pagamento em dinheiro
        desconto_adicional = preco_com_desconto * 0.02
        
        # Calcula o preço final subtraindo o desconto adicional
        preco_final = preco_com_desconto - desconto_adicional
        
        # Mostra para o usuário o novo preço após o desconto adicional
        print(f"\nCom o desconto adicional para pagamento em dinheiro, o preço final é R$ {preco_final:.2f}")
    
    # Verifica se o método de pagamento é cartão
    elif metodo_pagamento == "cartão":
        
        # Informa ao usuário que pode dividir o pagamento em até 3 vezes sem juros
        print("\nO pagamento pode ser dividido em até 3 vezes sem juros.")
        preco_final = preco_com_desconto

        """
        6.Exiba um resumo da compra, incluindo produto escolhido, preço original, desconto 
        aplicado e preço final.
        """
    # Mostra um resumo da compra incluindo detalhes do produto, preço original, desconto e preço final
    print(f"\nResumo da Compra:")
    print(f"Produto escolhido: Produto mais barato")
    print(f"Preço original: R$ {produto_mais_barato:.2f}")
    print(f"Desconto aplicado: R$ {desconto + desconto_adicional:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")
    
# Caso a resposta do usuário para comprar o produto mais barato não tenha sido 'sim'
else:
    
    # Mostra uma mensagem incentivando o usuário a buscar melhores ofertas
    print("\nLembre-se de sempre buscar o melhor negócio!")
    
    