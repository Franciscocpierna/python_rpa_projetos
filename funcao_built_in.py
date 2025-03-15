"""
funções internas built-in
print(), len(),input(), etc
Conversão de tipos: int(), float(),str(), etc 

"""

nome = "Maria"
print("ola, ", nome)
lista = [1,2,3]
print(len(lista))
#nome = input("digite seu nome: ")
#print("Seu nome é "+nome)
print(" Conversão de numeros inteiro")
numero_decimal = 7.9
numero_inteiro= int(float(numero_decimal))
print("numero inteiro", numero_inteiro)
print(" Conversão de numeros float")
numero_str="8.9"
numero_float= float(numero_str)
print(numero_float)
print(" Converter para um tipo texto str")
numero_int= 19
numero_para_str= str(numero_int)
print(numero_para_str)
print("recursão funções que chamam a si mesmo, riscos e sua limitação")


def contar_regrecivamente(n):
    
    if n > 0:
        print("numero é : ", n)
        contar_regrecivamente(n-1)
contar_regrecivamente(5)    



def calcula_fatorial(n):
 
    if n == 0:
        return 1
    return n*calcula_fatorial(n-1)
  

print(calcula_fatorial(5))  # Saída: 120

print("riscos e sua limitação da recursão")

"""def recursao_infinita(n):
    print(n)
    return recursao_infinita(n+1)
    
recursao_infinita(1) """  
    
print("Documentação e anotação de funçoes")
"""
""" 
# linha usa #

def somar(n,y):
  """
  essa função soma 2 numeros
  retorna int float de acordo com parametros
  """

  return n+y

print(somar(4,7)) 
print(somar.__doc__) #imprime a docstrings da função

print("anotação de tipos (Type Hints)")

def multiplicar(a: int, b:int) -> int:
    
    return a*b
print(multiplicar(4,5))
    

