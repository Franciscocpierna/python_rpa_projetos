"""
def soma(*args):
    
    #Função que retorna a soma de vários números.
    resultado = sum(args)
    return resultado

total = soma(2, 4, 6, 8, 10)
print("A soma dos números é:", total)


def soma(a, b):
    
    #Função que retorna a soma de dois números.
    return  a + b

total = soma(2, 4)
print("A soma dos números é:", total)

print("#"*50 ) 
print()
def exibir_informacoes(nome="Allan", idade=39, cidade="Desconhecida"):
    
    #Função que exibe informações pessoais.
    print("Nome:", nome)
    print("Idade:", idade)
    print("Cidade:", cidade)
    print()
    
#
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
"""
print("#"*50 )
def exibir_informacoes(**kwargs):
    
    #Função que exibe informações pessoais.
    for chave, valor in kwargs.items():
        print(chave +": "+ str(valor))
    print()
exibir_informacoes(nome="João", idade=25)    
exibir_informacoes(nome="João", idade=25, cidade="São Paulo")

print("#"*50 )
def exibir_informacoes1(**teste):
    
    #Função que exibe informações pessoais.
    for chave, valor in teste.items():
        print(chave +": "+ str(valor))
    print()
exibir_informacoes1(nome="João", idade=25)    
exibir_informacoes1(nome="João", idade=25, cidade="São Paulo")
print("#"*50 )
variavel_global = "eu sou uma variável global"

def funcao_exemplo():
    global n  
    n=10 
    varivel_local = "eu sou uma variável local"
    print(varivel_local)
    #Função que exibe uma variável global.
    print(variavel_global)
funcao_exemplo()    
print("#"*50 )
print(n)
print("\n"+"-"*50+"\n")
def funcao_externa():
    variavel_externa = "eu sou uma variável externa"
    print(variavel_externa)
    def funcao_interna():
        nonlocal variavel_externa
        variavel_externa = "eu fui modificada pela função interna"
        print(variavel_externa)
    funcao_interna()       
    print(variavel_externa)
funcao_externa()  

print("#"*50 )
def saudacao():
       
    return "ola mundo"
cumprimentar= saudacao
print(cumprimentar())
print("#"*50 )

def saudaco_nome(nome):
    return f"ola {nome}"

def cumprimentar(funcao, nome):
    return funcao(nome)
ele = cumprimentar(saudaco_nome, "João")
print(ele) # ola João ou fazer a linha abaixo
#print(cumprimentar(saudaco_nome, "João"))
print("#"*50)

#retornando funçoes de outras funções
def nivel_saudacao(nivel):
    def saudacao_basica():
        return "oi"
    def saudacao_avancada():
        return "ola, tudo bem?"
    if nivel == "basico":
        return saudacao_basica
    else:
        return saudacao_avancada
cumprimento = nivel_saudacao("basico")
print(cumprimento())     

