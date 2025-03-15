"""op = input("Digite uma operação: (soma, subtração, multiplicação, divisão)")

if op == "soma":
    def soma(a, b):
        return a + b
    print(soma(2, 4))
elif op == "subtração":
    def subtracao(a, b):
        return a - b
    print(subtracao(10, 5))
elif op == "multiplicação":
    def multiplicacao(a, b):
        return a * b
    print(multiplicacao(2, 5))
elif op == "divisão":
    def divisao(a, b):
        return a / b
    print(divisao(10, 2))
else:
    print("Operação inválida.")
"""

def fabrica_de_funcoes(operador):
    
    def soma(*args):
        return sum(args)
    def subtracao(*args):
        resultado = args[0]
        for i in args[1:]:
            resultado -= i
        return resultado  
    def multiplicacao(*args):
        resultado = 1
        for i in args:
            resultado *= i
        return resultado
    def divisao(*args):
        resultado = args[0]
        for i in args[1:]:
            if i == 0:
                raise  ValueError("Divisão por zero! não permitida")	
            resultado /= i
        return resultado     
    if operador == "soma":
        return soma
    elif operador == "subtracao":
        return subtracao
    elif operador == "multiplicacao":
        return multiplicacao
    elif operador == "divisao":
        return divisao
    else:
        def operacao_nao_permitida(*args):
            return "operação não permitida"
        return operacao_nao_permitida
        
operacao = fabrica_de_funcoes("soma")
print(operacao(2, 4, 6, 8, 10))     
operacao = fabrica_de_funcoes("subtracao")
print(operacao(5, 3, 1  ))
operacao = fabrica_de_funcoes("multiplicacao")
print(operacao(2, 5, 2))
operacao = fabrica_de_funcoes("divisao")
print(operacao(10, 2, 1))  



     
     