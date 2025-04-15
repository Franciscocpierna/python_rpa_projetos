"""
8 - Construa uma função que receba uma data no formato DD/MM/AAAA e 
        devolva uma string no formato D de mêsPorExtenso de AAAA.

Se a data for inválida (por exemplo, se o mês ou o dia não existirem), a 
        função deverá retornar NULL.
        
A função deve considerar os meses por extenso como: "Janeiro", "Fevereiro", etc.
"""

from datetime import datetime  # Importa a classe datetime do 
                               # módulo datetime para manipulação de datas.

# Dicionário para mapear os números dos meses aos 
        # seus respectivos nomes em português.
meses_por_extenso = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

# Definição da função 'data_por_extenso' que aceita uma 
        # string 'data_str' representando uma data.
def data_por_extenso(data_str):
    
    try:
        
        # A função `strptime` tenta converter a string 'data_str' 
                # em um objeto datetime.
        # O formato "%d/%m/%Y" especifica que a string 
                # deve estar no formato dia/mês/ano.
        data = datetime.strptime(data_str, "%d/%m/%Y")
        
        # Atribui o dia, o mês e o ano às variáveis 'dia', 'mes' e 
                # 'ano', respectivamente.
        dia = data.day
        mes = data.month
        ano = data.year

        # Constrói a string no formato "D de mêsPorExtenso 
                # de AAAA" usando o dicionário 'meses_por_extenso'
                # para converter o número do mês em seu nome por extenso.
        return f"{dia} de {meses_por_extenso[mes]} de {ano}"

    except ValueError:
        
        # O bloco 'except' captura o ValueError, que ocorre 
                # se 'data_str' não corresponder ao formato esperado
                # ou representar uma data inexistente (como 31 de fevereiro).
        # Retorna "NULL" para indicar que a data é inválida.
        return "NULL"

# Programa principal que testa a função com dois exemplos.
data_teste_1 = "10/10/2024"  # Data válida
data_teste_2 = "31/02/2020"  # Data inválida (Fevereiro geralmente não tem 31 dias)

# Exibe os resultados das funções chamadas 
        # com as datas de teste.
print(data_por_extenso(data_teste_1))  # Deve retornar: 10 de Outubro de 2024
print(data_por_extenso(data_teste_2))  # Deve retornar: NULL