def soma(*args):
    
    """Função que retorna a soma de vários números."""
    resultado = sum(args)
    return resultado

total = soma(2, 4, 6, 8, 10)
print("A soma dos números é:", total)


def soma(a, b):
    
    """Função que retorna a soma de dois números."""
    return  a + b

total = soma(2, 4)
print("A soma dos números é:", total)

print("#"*50 ) 
print()
def exibir_informacoes(nome="Allan", idade=39, cidade="Desconhecida"):
    
    """Função que exibe informações pessoais."""
    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)
    print()
    
    
print("#"*50 )
# Argumentos sem valores default
exibir_informacoes("João", 25, "São Paulo")

# Argumento com valor default
exibir_informacoes("Maria", 30)
print("#"*50 )

def estatisticas(*args):
    
    return sum(args) / len(args), max(args), min(args)


numeros = list(map(float, input("Digite uma sequência de números separados por espaços: ").split()))
print("numeros=",numeros)
media, maior, menor = estatisticas(*numeros)

print(f"Média: {media}")
print(f"Maior Número: {maior}")
print(f"Menor Número: {menor}")

