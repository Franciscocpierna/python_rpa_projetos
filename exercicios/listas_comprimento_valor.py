"""
14. Dada uma lista de palavras, crie uma função que agrupe essas 
    palavras por seu comprimento. A função deve retornar um dicionário 
    onde as chaves são os comprimentos e os valores são listas de 
    palavras com aquele comprimento.

Objetivo: Usar dicionários em conjunto com listas, processamento 
de strings e organização de dados.
"""

# Define a função 'agrupar_por_comprimento' que aceita uma 
        # lista chamada 'palavras' como parâmetro.
def agrupar_por_comprimento(palavras):
    
    # Cria um dicionário vazio chamado 'agrupadas' para 
            # armazenar os grupos de palavras pelo seu comprimento.
    agrupadas = {}
    
    # Inicia um laço 'for' que percorre cada 'palavra' na lista 'palavras'.
    for palavra in palavras:
        
        # Usa a função 'len()' para calcular o comprimento da 'palavra' atual.
        comprimento = len(palavra)
        
        # Verifica se o comprimento atual já existe como 
                # chave no dicionário 'agrupadas'.
        if comprimento not in agrupadas:
            
            # Se não existir, cria uma nova entrada no dicionário com o 
                    # comprimento como chave e uma lista vazia como valor.
            agrupadas[comprimento] = []
            print("comprimento não existe, criando lista vazia ", agrupadas)  # Imprime o dicionário 'agrupadas' após a criação da nova chave.
        
        # Adiciona a 'palavra' atual à lista correspondente ao 
                # seu comprimento no dicionário.
        agrupadas[comprimento].append(palavra)
        print("palavras agrupadas ", agrupadas)  # Imprime o dicionário 'agrupadas' após cada iteração.
    
    # Retorna o dicionário 'agrupadas' que agora contém as palavras 
            # agrupadas por seu comprimento.
    return agrupadas

# Cria uma lista de palavras.
palavras = ["cachorro", "gato", "elefante", "ave", "rato", "onça", "girafa", "otorrinolaringologista", "paralelepipedo"]

# Chama a função 'agrupar_por_comprimento' passando a lista 'palavras' 
        # e armazena o resultado retornado na variável 'resultado'.
resultado = agrupar_por_comprimento(palavras)

# Itera sobre cada item no dicionário 'resultado'.
# A função 'items()' retorna uma lista de 
        # tuplas (chave, valor) do dicionário.
for comprimento, grupo in resultado.items():
    
    # Imprime o comprimento e a lista de palavras 
            # que possuem aquele comprimento.
    print(f"Palavras com {comprimento} letras: {grupo}")