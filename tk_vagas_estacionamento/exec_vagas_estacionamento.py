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
        
    elif opcao == '2':
        
        if selecionar_vaga_automaticamente(vagas):
            
            print("Vaga selecionada automaticamente com sucesso!")
            
        else:
            
            print("Não foi possível encontrar uma vaga desocupada.")
        
        
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