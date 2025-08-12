"""
Crie um algoritmo com o objetivo de controlar as vagas do Estacionamento, elas estão
divididas igualmente em quatro blocos (A, B, C, D) e numeradas a partir do
número um (1) em cada bloco.

O algoritmo deve possuir um menu com as seguintes opções de operação:

1 - Exibir painel de vagas
2 - Selecionar vaga automaticamente
3 - Selecionar vaga manualmente
4 - Liberar vaga
5 - Sair

Observações:

1 - Utilize - para representar vagas livre e X para representar vagas ocupadas

2 - O algoritmo deve automaticamente identificar uma vaga
    disponível no estacionamento e ocupá-la.

    O algoritmo deve dar prioridade ao bloco em que houver mais vagas
    desocupadas.

    Caso não seja encontrada nenhuma vaga desocupada, o sistema deve
    informar que não foi possível realizar a operação.
    
3 - Nesta opção o usuário deve informar em qual bloco e em qual vaga ele
    deseja estacionar seu carro.

    O algoritmo deve verificar se a vaga desejada pelo usuário se encontra
    disponível, caso não esteja o sistema deve informar que não foi
    possível realizar a operação.

4 - Nesta opção o usuário deve informar em qual bloco e em qual vaga ele irá liberar a vaga.
    
    O algoritmo deve verificar se a vaga desejada pelo usuário se encontra realmente 
    ocupada, caso não esteja o sistema deve informar que aquela
    vaga já estava desocupada.
    
5 - O algoritmo encerra a execução.
"""


# Esta função é responsável por exibir o estado atual das vagas de estacionamento.
def exibir_painel_vagas(vagas):
    

    # A linha abaixo imprime o cabeçalho do painel. Este cabeçalho 
    # inclui o rótulo "Bloco/vaga" seguido pelos números das 
    # vagas (de 1 a 5). O cabeçalho serve como um guia visual para entender como as 
    # vagas estão organizadas nos blocos.
    print("Bloco/vaga   1   2   3   4   5")
          
    # Inicia um loop que itera sobre cada par de chave-valor no dicionário 'vagas'.
    # 'bloco' é a chave (nome do bloco de estacionamento), e 'v' é o valor
    # associado (lista de vagas).
    for bloco, v in vagas.items():
          
        # Imprime o nome do bloco. O formato '{:<12}' especifica que a string deve ser alinhada à esquerda
        # ('<') em um campo de 12 caracteres de largura. Isso garante que todos os nomes de blocos ocupem 
        # a mesma largura na impressão, mantendo o alinhamento vertical. 'end=' ' evita que a linha seja
        # quebrada após a impressão do nome do bloco, permitindo que as vagas sejam impressas na mesma linha.
        print("{:<12}".format(bloco), end=' ')

        # Inicia um segundo loop que itera sobre cada elemento na lista de vagas 'v' para o bloco atual.
        for vaga in v:
          
            # Imprime o estado da vaga (ocupada ou desocupada). O formato '{:<3}' alinha a string à esquerda
            # em um campo de 3 caracteres de largura. Isso assegura um espaçamento uniforme entre as vagas.
            # Novamente, 'end=' ' é usado para manter a continuação na mesma linha.
            print("{:<3}".format(vaga), end=' ')

        # Imprime uma nova linha após listar todas as vagas de
        # um bloco. Isso separa visualmente um bloco do próximo,
        # facilitando a leitura do painel de vagas.
        print()
        
        
# Esta função seleciona automaticamente uma vaga de estacionamento desocupada.
# É útil quando o usuário não tem preferência por uma vaga específica e deseja 
# apenas uma vaga disponível.
def selecionar_vaga_automaticamente(vagas):

    # Cria um dicionário vazio chamado num_vagas_desocupadas. Este dicionário será 
    # usado para armazenar o número de vagas desocupadas em cada bloco de estacionamento.
    # A chave será o nome do bloco e o valor será o número de vagas desocupadas.
    num_vagas_desocupadas = {}

    # Inicia um loop que percorre cada par chave-valor no dicionário 'vagas'.
    # 'bloco' representa a chave (o nome do bloco de estacionamento) e 'vagas_em_bloco' 
    # é o valor associado (uma lista de vagas no bloco).
    for bloco, vagas_em_bloco in vagas.items():
          
        # Conta o número de vagas desocupadas em cada bloco. Isso é feito utilizando o método
        # .count('-'), que retorna quantas vezes o caractere '-' (indicando uma vaga desocupada)
        # aparece na lista de vagas do bloco. O resultado é armazenado no dicionário 
        # num_vagas_desocupadas, com o nome do bloco como chave.
        num_vagas_desocupadas[bloco] = vagas_em_bloco.count('-')

    # Ordena os blocos de estacionamento com base no número de vagas desocupadas, em ordem
    # decrescente. Isso é feito utilizando a função sorted(), que retorna uma nova lista.
    # num_vagas_desocupadas é o dicionário que queremos ordenar.
    # key=num_vagas_desocupadas.get é uma função que é chamada para cada elemento da lista
    # de blocos, retornando o número de vagas desocupadas para aquele bloco.
    # reverse=True especifica que a lista deve ser ordenada em ordem decrescente, ou seja,
    # os blocos com mais vagas desocupadas virão primeiro.
    blocos_ordenados = sorted(num_vagas_desocupadas, key=num_vagas_desocupadas.get, reverse=True)

    # Esta parte do código é responsável por tentar encontrar uma vaga desocupada
    # dentro dos blocos de estacionamento, seguindo a ordem de prioridade estabelecida
    # (blocos com mais vagas desocupadas primeiro).

    # Inicia um loop que percorre cada bloco na lista 'blocos_ordenados'.
    # Lembre-se de que 'blocos_ordenados' contém os nomes dos blocos ordenados
    # de acordo com o número de vagas desocupadas, do maior para o menor.
    for bloco in blocos_ordenados:
          
        # Inicia um segundo loop que itera sobre cada vaga no bloco atual.
        # A função enumerate() é usada aqui para obter tanto o índice (i) quanto
        # o valor (vaga) para cada elemento na lista de vagas do bloco.
        # 'i' é o índice da vaga na lista, e 'vaga' é o estado atual da vaga
        # (ocupada ou desocupada).
        for i, vaga in enumerate(vagas[bloco]):
          
            # Verifica se a vaga atual está desocupada. Uma vaga desocupada é 
            # representada pelo caractere '-'.
            if vaga == '-':
          
                # Se a vaga está desocupada, a função ocupa essa vaga. Isso é feito
                # substituindo '-' por 'X' no índice correspondente da lista de vagas
                # para o bloco. 'X' é usado para indicar que a vaga agora está ocupada.
                vagas[bloco][i] = 'X'
          
                # Após ocupar uma vaga, a função retorna True. Isso indica que uma vaga foi 
                # selecionada e ocupada com sucesso.
                return True

    # Se o código chegar a este ponto, significa que todas as vagas em todos os blocos
    # estão ocupadas (nenhuma vaga desocupada foi encontrada em nenhum dos blocos).
    # Portanto, a função retorna False, indicando que não foi possível selecionar uma vaga.
    return False
                
        
# Esta função permite que o usuário selecione manualmente uma vaga de estacionamento.
# O usuário especifica o bloco e o número da vaga que deseja ocupar.
def selecionar_vaga_manualmente(vagas, bloco, numero_vaga):

    # Primeira verificação: se o bloco de estacionamento existe.
    # O método .get() é usado para buscar o valor associado à chave 'bloco' no dicionário 'vagas'.
    # Se 'bloco' não existir no dicionário, .get() retornará None.
    if vagas.get(bloco) is None:
        
        # Se o bloco não existir, informa o usuário e retorna False, indicando que a operação falhou.
        print("O bloco informado não existe.")
        
        return False
    
    # Segunda verificação: se o número da vaga é válido.
    # Verifica se 'numero_vaga' está dentro do intervalo válido de vagas para o bloco especificado.
    # O intervalo válido é de 1 até o número total de vagas no bloco (inclusive).
    # len(vagas[bloco]) retorna o número total de vagas no bloco.
    if not (1 <= numero_vaga <= len(vagas[bloco])):
        
        # Se o número da vaga estiver fora do intervalo válido, informa 
        # o usuário e retorna False.
        print("A vaga informada não existe.")
        return False
    
    # Terceira verificação: se a vaga especificada está desocupada.
    # As vagas são indexadas a partir de 0, então 'numero_vaga - 1' é 
    # usado para acessar a vaga correta.
    # Uma vaga desocupada é indicada por '-'.
    if vagas[bloco][numero_vaga - 1] == '-':
        
        # Se a vaga estiver desocupada, marca-a como ocupada substituindo '-' por 'X'.
        vagas[bloco][numero_vaga - 1] = 'X'
        
        # Retorna True, indicando que a vaga foi selecionada e ocupada com sucesso.
        return True
    
    # Último caso: a vaga já está ocupada.
    else:
        
        # Se a vaga já estiver ocupada, informa o usuário e retorna False.
        print("A vaga informada já está ocupada.")
        return False
    
    
# Esta função permite ao usuário liberar uma vaga de estacionamento que está atualmente ocupada.
# Para isso, o usuário precisa fornecer o bloco e o número da vaga que deseja liberar.
def liberar_vaga(vagas, bloco, numero_vaga):

    # Primeira verificação: se o bloco de estacionamento fornecido existe no dicionário 'vagas'.
    # Utiliza o método .get() do dicionário para tentar recuperar as vagas associadas ao bloco.
    # Se o bloco não existir no dicionário, o método .get() retornará None.
    if vagas.get(bloco) is None:
        
        # Se o bloco não existir, uma mensagem de erro é exibida informando o usuário.
        # A função então retorna False, indicando que a operação de liberação da vaga falhou.
        print("O bloco informado não existe.")
        return False
    
    # Segunda verificação: se o número da vaga informada é válido para o bloco especificado.
    # Isso é feito verificando se o número da vaga está dentro do intervalo de 1 até o número total de vagas no bloco.
    # len(vagas[bloco]) retorna a quantidade de vagas no bloco, que é o limite superior do intervalo válido.
    # A comparação '1 <= numero_vaga <= len(vagas[bloco])' verifica se 'numero_vaga' está dentro desse intervalo.
    if not (1 <= numero_vaga <= len(vagas[bloco])):
        
        # Se o número da vaga estiver fora desse intervalo, uma mensagem de erro é exibida.
        # A função retorna False, sinalizando que a vaga especificada não existe e, portanto, não pode ser liberada.
        print("A vaga informada não existe.")
        return False

    
    # Terceira verificação: se a vaga especificada está atualmente ocupada.
    # Para acessar a vaga especificada, usamos 'vagas[bloco][numero_vaga - 1]'.
    # O índice é 'numero_vaga - 1' porque as listas em Python são indexadas a partir de 0,
    # então precisamos subtrair 1 do número da vaga para obter a posição correta na lista.
    # A vaga ocupada é representada pelo caractere 'X'.
    if vagas[bloco][numero_vaga - 1] == 'X':
        
        # Se a vaga estiver ocupada, ela é liberada.
        # Isso é feito substituindo 'X' por '-', indicando que a vaga agora está desocupada.
        vagas[bloco][numero_vaga - 1] = '-'
        
        # A função então retorna True, indicando que a vaga foi liberada com sucesso.
        return True
    
    # Último caso: se a vaga já estiver desocupada.
    # Este bloco será executado se a condição do if acima não for verdadeira, ou seja,
    # se a vaga não estiver marcada com 'X' (não está ocupada).
    else:
        
        # Se a vaga já estiver desocupada (marcada com '-'), uma mensagem de erro é exibida.
        # A função retorna False, indicando que não foi possível realizar a operação de liberação,
        # pois a vaga já estava disponível.
        print("A vaga informada já estava desocupada.")
        return False
    

# Inicialização do dicionário 'vagas' para gerenciar as vagas de estacionamento.
# O dicionário é estruturado com chaves representando os blocos de estacionamento (A, B, C, D)
# e os valores são listas representando as vagas em cada bloco.
# Cada lista contém 5 vagas, inicialmente todas desocupadas, indicadas pelo caractere '-'.
vagas = {
    'A': ['-'] * 5,  # Cria uma lista de 5 vagas desocupadas para o bloco 'A'.
    'B': ['-'] * 5,  # Mesmo para o bloco 'B'.
    'C': ['-'] * 5,  # Mesmo para o bloco 'C'.
    'D': ['-'] * 5   # Mesmo para o bloco 'D'.
}

# Inicializa a variável 'opcao' como uma string vazia.
# Esta variável será usada para armazenar a escolha do usuário no menu do programa.
opcao = ''

# Inicia um loop que continuará executando até que o usuário decida sair do programa.
# O loop se repete enquanto 'opcao' for diferente de '5' (a opção de sair do programa).
while opcao != '5':
          
    # Imprime o menu de opções do programa a cada iteração do loop.
    # Este menu é exibido para o usuário escolher a ação que deseja realizar.
    print("\n--- Menu ---")
    print("1 - Exibir painel de vagas")         # Opção para exibir o estado das vagas.
    print("2 - Selecionar vaga automaticamente") # Opção para selecionar uma vaga automaticamente.
    print("3 - Selecionar vaga manualmente")    # Opção para selecionar uma vaga manualmente.
    print("4 - Liberar vaga")                   # Opção para liberar uma vaga ocupada.
    print("5 - Sair")                           # Opção para sair do programa.

    
    # Solicita ao usuário para inserir uma opção.
    # O método .upper() é aplicado ao input para converter a entrada do usuário em letras maiúsculas.
    # Isso garante que a comparação da opção seja feita de forma consistente, independentemente de 
    # como o usuário digita (maiúsculas ou minúsculas).
    opcao = input("Escolha uma opção: ").upper()


    # Verifica se a opção escolhida pelo usuário é '1'.
    if opcao == '1':
        
        # Se a opção for '1', a função exibir_painel_vagas é chamada.
        # Esta função exibe o estado atual das vagas em cada bloco do estacionamento.
        # Cada vaga é representada como 'X' (ocupada) ou '-' (desocupada).
        exibir_painel_vagas(vagas)
        
        
    # Verifica se a opção escolhida pelo usuário é '2'.
    elif opcao == '2':
        
        # Se a opção for '2', a função selecionar_vaga_automaticamente é chamada.
        # Esta função tenta encontrar e ocupar automaticamente uma vaga desocupada.
        
        # A função retorna True se uma vaga desocupada foi encontrada e ocupada com sucesso.
        if selecionar_vaga_automaticamente(vagas):
            
            # Se a vaga foi selecionada com sucesso, imprime uma mensagem de confirmação.
            print("Vaga selecionada automaticamente com sucesso!")
          
        # Se a função retornar False, significa que não foi possível encontrar uma vaga desocupada.
        else:
            
            # Nesse caso, uma mensagem informando que não há vagas disponíveis é exibida.
            print("Não foi possível encontrar uma vaga desocupada.")

            
    # Verifica se a opção escolhida pelo usuário é '3'.
    elif opcao == '3':
        
        # Se a opção for '3', isso indica que o usuário deseja selecionar uma vaga manualmente.

        # Solicita ao usuário que informe o bloco de estacionamento onde deseja selecionar a vaga.
        # O método .upper() é aplicado ao input para converter a entrada do usuário em letras maiúsculas,
        # garantindo a consistência na comparação de nomes de blocos, independentemente de como 
        # o usuário digita (maiúsculas ou minúsculas).
        bloco = input("Informe o bloco: ").upper()
          
        # Solicita ao usuário que informe o número da vaga que deseja ocupar.
        # O input é convertido para um inteiro usando int(), pois os números das vagas 
        # são tratados como inteiros no programa.
        numero_vaga = int(input("Informe o número da vaga: "))
          
        # Chama a função selecionar_vaga_manualmente, passando o dicionário 'vagas', 
        # o bloco e o número da vaga escolhidos pelo usuário.
        # A função tentará ocupar a vaga especificada, se ela estiver desocupada.
        if selecionar_vaga_manualmente(vagas, bloco, numero_vaga):
            
            # Se a vaga for selecionada com sucesso (função retorna True),
            # uma mensagem de confirmação é exibida.
            print("Vaga selecionada manualmente com sucesso!")

            
    # Verifica se a opção escolhida pelo usuário é '4'.
    elif opcao == '4':
        
        # Se a opção for '4', isso indica que o usuário deseja liberar uma vaga de estacionamento.

        # Solicita ao usuário que informe o bloco de estacionamento onde a vaga a ser liberada está localizada.
        # O método .upper() é aplicado ao input para converter a entrada do usuário em letras maiúsculas,
        # assegurando que a comparação de nomes de blocos seja consistente, independentemente de como 
        # o usuário digita (maiúsculas ou minúsculas).
        bloco = input("Informe o bloco: ").upper()
          
        # Solicita ao usuário que informe o número da vaga que deseja liberar.
        # O input é convertido para um inteiro usando int(), uma vez que os números das vagas 
        # são tratados como inteiros no programa.
        numero_vaga = int(input("Informe o número da vaga: "))
          
        # Chama a função liberar_vaga, passando o dicionário 'vagas', o bloco e o número da vaga
        # escolhidos pelo usuário. A função tentará liberar a vaga especificada.
        if liberar_vaga(vagas, bloco, numero_vaga):
            
            # Se a vaga for liberada com sucesso (função retorna True),
            # uma mensagem de confirmação é exibida.
            print("Vaga liberada com sucesso!")
        
        
    # Verifica se a opção escolhida pelo usuário é '5'.
    elif opcao == '5':
        
        # Se a opção for '5', isso indica que o usuário deseja sair do programa.
        # Uma mensagem de encerramento é exibida.
        print("Encerrando o programa...")
        
    # Caso nenhuma das opções válidas ('1', '2', '3', '4', '5') seja escolhida.
    else:
        
        # Se o usuário inserir uma opção que não corresponde a nenhuma das opções válidas,
        # uma mensagem informando que a opção é inválida é exibida.
        # O loop então continua, permitindo que o usuário faça outra escolha.
        print("Opção inválida. Por favor, escolha uma opção válida.")