"""
21. Contagem de Segundas-Feiras no Dia 1º em um Intervalo de Datas

Escreva um programa em Python que solicita ao usuário um intervalo de 
        datas, com uma data de início e uma data de fim, e conta quantas 
        segundas-feiras caem no dia 1º de cada mês dentro desse intervalo. 
        
O programa deve validar as entradas e garantir que a data de início 
        seja anterior ou igual à data de fim.

Requisitos:
 - O programa deve solicitar que o usuário insira uma data de início e 
         uma data de fim no formato "AAAA-MM-DD".
- O programa deve verificar se o dia 1º de cada mês dentro do intervalo 
        dado é uma segunda-feira e contar quantas vezes isso ocorre.
- Se a data de início for posterior à data de fim, o programa deve 
        exibir uma mensagem de erro e solicitar que o usuário 
        insira novamente as datas.
- Caso o formato da data seja inválido, o programa deve solicitar a 
        correção até que o formato correto seja inserido.
"""

# Importando o módulo datetime, necessário para trabalhar com datas.
import datetime

# Definição da função que conta as segundas-feiras que caem 
        # no dia 1 de cada mês num intervalo de datas especificado.
def contar_segundas_feiras(data_inicio, data_fim):
    
    """
    Conta quantas segundas-feiras caem no dia 1º de cada mês 
            entre duas datas fornecidas.

    Parâmetros:
        - data_inicio (datetime.date): A data que inicia o 
                    intervalo de contagem.
        - data_fim (datetime.date): A data que termina o 
                    intervalo de contagem.

    Retorna:
        - int: O número de segundas-feiras que caem no dia 1º de 
                cada mês dentro do intervalo especificado.
    """

    # Inicialização do contador de segundas-feiras.
    contador_segundas = 0

    # Extração do ano e do mês das datas de início e fim.
    # Isso determina a partir de que ano e mês começar e onde terminar.
    ano_inicio, mes_inicio = data_inicio.year, data_inicio.month
    ano_fim, mes_fim = data_fim.year, data_fim.month

    # Loop que passa por cada ano no intervalo de anos desde o 
            # ano de início até o ano de fim.
    for ano in range(ano_inicio, ano_fim + 1):
        
        # Define o mês de início para o ano atual. Se for o 
                # primeiro ano do intervalo, começa do 'mes_inicio'.
        # Caso contrário, começa de janeiro (mes 1).
        mes_inicio_atual = mes_inicio if ano == ano_inicio else 1
        
        # Define o mês de fim para o ano atual. Se for o último 
                # ano do intervalo, termina no 'mes_fim'.
        # Caso contrário, termina em dezembro (mes 12).
        mes_fim_atual = mes_fim if ano == ano_fim else 12

        # Loop que passa por cada mês no ano atual, desde o 
                # mês de início até o mês de fim.
        for mes in range(mes_inicio_atual, mes_fim_atual + 1):
            
            # Criação de um objeto datetime.date para o primeiro 
                    # dia do mês corrente.
            # Isso é necessário para verificar o dia da semana 
                    # daquela data específica.
            data = datetime.date(ano, mes, 1)
            
            # Checagem se o primeiro dia do mês é uma segunda-feira.
            # 'weekday()' retorna 0 para segunda-feira, 1 para terça-feira, etc.
            if data.weekday() == 0:
                
                # Se for segunda-feira, incrementa o contador de segundas-feiras.
                contador_segundas += 1

    # Retorna o total de segundas-feiras encontradas que caem no 
            # primeiro dia dos meses no intervalo dado.
    return contador_segundas


# Definindo a função que solicita uma data do usuário.
def solicitar_data():
    
    """
    Solicita uma data do usuário e verifica se está no formato correto "AAAA-MM-DD".
    Se o formato estiver correto, retorna a data como um objeto datetime.date.
    Se estiver incorreto, solicita novamente.
    """
    
    # Inicia um loop infinito para continuar solicitando a data até 
            # que uma entrada válida seja recebida.
    while True:
        
        try:
            
            # Pede ao usuário para digitar uma data no formato especificado.
            data_str = input("Digite uma data (formato: AAAA-MM-DD): ")
            
            # Tenta converter a string de data em um objeto de data 
                    # utilizando strptime.
            # Se a string não estiver no formato "AAAA-MM-DD", uma 
                    # exceção ValueError será lançada.
            data = datetime.datetime.strptime(data_str, "%Y-%m-%d").date()
            
            # Se a data for convertida com sucesso, termina o loop 
                    # retornando o objeto de data.
            return data
            
        except ValueError:
            
            # Se um erro ValueError for capturado (formato errado), 
                    # informa o usuário e repete o loop.
            print("Data inválida. Tente novamente no formato AAAA-MM-DD.")

# Instrução para o usuário sobre o que será solicitado.
print("Por favor, insira o intervalo de datas.")

# Solicita ao usuário que forneça uma data de início 
        # utilizando a função 'solicitar_data'.
data_inicio = solicitar_data()

# Solicita ao usuário que forneça uma data de fim 
        # utilizando a mesma função.
data_fim = solicitar_data()


# Verifica se a data de início é anterior à data de fim para 
        # garantir que o intervalo seja válido.
if data_inicio > data_fim:
    
    # Se a data de início for posterior à data de fim, 
            # imprime uma mensagem de erro.
    print("A data de início deve ser anterior à data de fim.")
    
else:
    
    # Se a data de início for anterior ou igual à data de fim, 
            # procede com o cálculo.
    
    # Chama a função 'contar_segundas_feiras' passando as datas de 
            # início e fim como argumentos.
    # Esta função retorna o número de segundas-feiras que caem no 
            # primeiro dia de cada mês no intervalo especificado.
    resultado = contar_segundas_feiras(data_inicio, data_fim)
    
    # Imprime o resultado do cálculo, mostrando quantas segundas-feiras 
            # caem no dia 1º de cada mês no intervalo dado.
    print(f"O número de segundas-feiras que caem no dia 1º de cada mês entre {data_inicio} e {data_fim} é: {resultado}")